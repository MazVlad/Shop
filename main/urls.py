from django.urls import path
from .views import *

app_name = 'main'
urlpatterns = [
    path('',Index.as_view(),name='index'),
    path('category/<int:cat_id>/', show_category, name='category'),
    path('post/<int:pk>/', ShowPost.as_view(), name='post'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path("search/", search.as_view(), name='search'),

]