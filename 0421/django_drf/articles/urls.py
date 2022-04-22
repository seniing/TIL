from django.urls import path
from . import views
# no app_name
urlpatterns = [
    path('json-3/', views.article_json_3), # no name
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
    path('comments/', views.comment_list),
    path('articles/<int:article_pk>/comments/', views.comment_create),
    path('comments/<int:comment_pk>/', views.comment_detail),

]
