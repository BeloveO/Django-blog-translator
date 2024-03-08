from . import views
from django.urls import URLPattern, path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('logout/', views.log_out, name='logout'),
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.log_in, name='login'),
    path('post/<pk>/<slug:slug>', views.BlogView.as_view(), name='blog_view'),
    path('about/', views.AboutView.as_view(), name='about_view'),
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)