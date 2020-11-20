from django.urls import path

from .views import *

urlpatterns = [
    path('', lambda req: redirect('top/'), name='main'),
    path('admin/', lambda req: redirect('admin/'), name='admin'),
    path('top/', display_top_of_images, name='top'),
    path('top/vote_for_image/', vote_for_image, name='vote_for_image'),
    path('upload/', image_post_view, name='upload'),
    path('latest/', display_latest_of_images, name='latest'),
    path('user/', display_user_page, name='user'),
    path('user/del_image/', delete_image, name='del_image'),
    path('user/public_image/', public_image, name='public_image')
]
