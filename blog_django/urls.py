from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import about
from django.conf import settings
from django.conf.urls.static import static
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView

urlpatterns = [
    path('', PostListView.as_view(),name="blog-home"),
    path('about/', about,name="about"),
    path('post/<int:pk>/', PostDetailView.as_view(),name="detail-post"),
    path('post/<int:pk>/update', PostUpdateView.as_view(),name="post-update"),
    path('post/<int:pk>/delete', PostDeleteView.as_view(),name="post-delete"),
    path('post/create_post/', PostCreateView.as_view(),name="post_create"),
    path("post/view_post/<int:id_user>/", UserPostListView.as_view(),name="user_post"),
    path("password_reset/", auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"),name="password_reset"),
    path("password_reset_done/", auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),name="password_reset_done"),
    path("password_reset_confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"),name="password_reset_confirm"),
    path("password_reset_complete/", auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"),name="password_reset_complete"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)