from django.shortcuts import render, get_object_or_404, reverse
from django.views import View
from django.views.generic.edit import UpdateView
from .models import Profile
from videos.models import Video
from django.core.paginator import Paginator


from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserSerializer, ProfileSerializer 
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination

class ProfileView(View): 

    def get(self, request, pk, *args, **kwargs):
        profile = get_object_or_404(Profile, pk=pk)
        videos = Video.objects.all().filter(uploader=request.user).order_by('-date_posted')

        paginator = Paginator(videos, 1)  
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'profile': profile,
            'videos': page_obj,
        }

        return render(request, 'profiles/profile.html', context)


class UpdateProfile(UpdateView):
    model = Profile
    fields = ['name', 'location', 'image']
    template_name = 'profiles/update_profile.html'

    def form_valid(self, form):
        if not form.instance.image:
            form.instance.image = 'uploads/profile_pics/default.jpg'
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.object.pk})
    



# class UserPagination(PageNumberPagination):
#     page_size = 1

# class GetAllUsers(APIView):
    
#     def get(self, request):
#         users = User.objects.all()
#         paginator = UserPagination()
#         serializer = UserSerializer(users, many=True)
#         page = paginator.paginate_queryset(serializer.data, request) 
#         return Response(page)

# class ProfileRUDView(RetrieveUpdateDestroyAPIView):
#     # authentication_classes = [IsAuthenticated]
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
