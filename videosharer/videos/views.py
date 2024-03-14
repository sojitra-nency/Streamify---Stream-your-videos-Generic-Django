from django.shortcuts import render, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView
from django.views import View
from .models import Comment, Video, Category
from .forms import CommentForm
from django.db.models import Q
from django.core.paginator import Paginator

class Index(ListView):
    model = Video
    template_name = 'videos/index.html'
    context_object_name = 'video_list'
    ordering = ['-date_posted']
    paginate_by = 3  

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 10
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]

        context['page_range'] = page_range
        return context
    

class CreateVideo(LoginRequiredMixin, CreateView):
    model = Video
    fields = ['title', 'description', 'video_file', 'thumbnail', 'category']
    template_name = 'videos/create_video.html'
    
    def form_valid(self, form):
        form.instance.uploader = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('video-detail', kwargs={'pk': self.object.pk})

class DetailVideo(View):
    def get(self, request, pk , *args, **kwargs):
        video = Video.objects.get(pk=pk)
        form = CommentForm()
        comments = Comment.objects.filter(video=video).order_by('-created_on')
        paginator = Paginator(comments, 3) 
        page_number = request.GET.get('page')
        comments_page = paginator.get_page(page_number)
        categories = Video.objects.filter(category=video.category)[:14]
        context = {
            'object': video,
            'comments': comments_page,
            'has_other_pages': comments_page.has_other_pages(),
            'categories': categories,
            'form': form,
        }
        return render(request, 'videos/video_detail.html', context)
    
    def post(self, request, pk , *args, **kwargs):
        video = Video.objects.get(pk=pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = Comment(
                user=self.request.user,
                video=video,
                comment=form.cleaned_data['comment']    
            )
            comment.save()

        comments = Comment.objects.filter(video=video).order_by('-created_on')
        categories = Video.objects.filter(category=video.category)[:14]
        context = {
            'object': video,
            'comments': comments,
            'categories': categories,
            'form': form,
            
        }
        return render(request, 'videos/video_detail.html', context)

class UpdateVideo(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Video
    fields = ['title', 'description']
    template_name = 'videos/create_video.html'
    
    def get_success_url(self):
        return reverse('video-detail', kwargs={'pk': self.object.pk})
    
    def test_func(self):
        video = self.get_object()
        return self.request.user == video.uploader
            
class DeleteVideo(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Video
    template_name = 'videos/delete_video.html'
    
    def get_success_url(self):
        return reverse('index')
    
    def test_func(self):
        video = self.get_object()
        return self.request.user == video.uploader
    
class VideoCategoryList(View):
    def get(self, request, pk, *args, **kwargs):
        category = Category.objects.get(pk=pk)
        videos = Video.objects.filter(category=pk).order_by('-date_posted')
        paginator = Paginator(videos, 1)  
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        context = {
            'videos': page_obj,
            'category': category,
        }
        return render(request, 'videos/video_category.html', context)
    

class SearchVideo(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('q')
        query_list = Video.objects.filter(
                Q(title__icontains=query) | 
                Q(description__icontains=query) |
                Q(category__name__icontains=query) |
                Q(uploader__username__icontains=query)
            ).order_by('-date_posted')
        
        paginator = Paginator(query_list, 1)  # 3 videos per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        context = {
            'query_list': page_obj,
        }
        return render(request, 'videos/search.html', context)