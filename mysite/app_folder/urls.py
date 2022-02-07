from django.urls import path
from . import views

app_name = 'app_folder'
urlpatterns = [
    path('top_page/', views.top_page, name='top_page'),
    path('search/', views.search, name='search'),
    path('hello/', views.hello, name='hello'),
    path('poll/', views.poll, name='poll'),
    path('poll/<int:question_id>/', views.detail, name='detail'),
    path('poll/<int:question_id>/results/', views.results, name='results'),
    path('poll/<int:question_id>/vote/', views.vote, name='vote'),
    path('input/', views.input_page, name='input'),
    path('colorful/', views.colorful, name='colorful'),
    path('new_sample/', views.new_sample, name='new_sample'),
    path('add_question/', views.add_question, name='add_question'),
    path('allfile/', views.allfile, name='allfile'),
    path('upload/', views.modelform_upload, name='upload'),
    ]
