from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.home, name="Home"),
    path("home", views.User_home, name="home"),
    path("upload", views.upload, name="upload"),
    path("display_image", views.display_image, name="display image"),
    path("display_video", views.display_video, name="display video"),
    path("Login", views.Login, name="Login"),
    path("Signup", views.Signup, name="Signup"),
    path("home/upload_image", views.upload_image, name="image"),
    path("home/upload_video", views.upload_video, name="video"),
    path("add_img_id", views.add_img_id, name="add_img_id"),
    path("add_vid_id", views.add_vid_id, name="add_vid_id"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
