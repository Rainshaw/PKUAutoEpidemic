from django.urls import path, re_path
from . import views

app_name = 'epidemic'


urlpatterns = [
    path('', views.NoIndexView.as_view()),
    path('index/', views.IndexView.as_view(), name='index'),
    path('info_create/', views.InfoCreateView.as_view(), name='info-create'),
    path('success/', views.InfoCreateSuccessView.as_view(), name='create-success'),
    re_path('^view_detail/(?P<token>.*)$', views.InfoDetailView.as_view(), name='info-detail'),
    re_path('^info_update/(?P<token>.*)$', views.InfoUpdateView.as_view(), name='info-update'),

]
