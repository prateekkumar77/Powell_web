from . import views
from django. urls import path, re_path

urlpatterns = [
    path("", views.home, name='home'),
    path('admin1/', views.admin_panel, name='admin_panel'),
    path('admin1/generate_pdf', views.gen_pdf, name='admin_panel'),
    path('admin1/pending_test', views.pending_test, name='admin_panel'),
    re_path(r'generate_pdf$', views.gen_pdf, name='generate_pdf'),
    re_path(r'download_pdf$', views.download, name='download_pdf'),
    path('check_result/view_pdf', views.view_pdf, name='check_result'),
    path('check_result/download_pdf', views.download, name='check_result'),
    path('check_result/', views.check_result, name='check_result'),
    path('register/', views.register, name='register'),
    re_path(r'^view_pdf$', views.view_pdf, name='view_pdf'),
    re_path(r'pending_test$', views.pending_test, name='pending_test')
]
