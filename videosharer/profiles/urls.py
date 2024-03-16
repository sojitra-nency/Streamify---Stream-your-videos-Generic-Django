from django.urls import path
from .views import ProfileView, UpdateProfile, GetAllUsers, ProfileRUDView

urlpatterns = [
    path('<int:pk>/', ProfileView.as_view(), name='profile'),
    path('<int:pk>/update/', UpdateProfile.as_view(), name='update-profile'),

    # path("all-users/", GetAllUsers.as_view(), name="all-users"),
    # path("user/<int:pk>", ProfileRUDView.as_view(), name="user-rud"),
]