from django.urls import path
from .views import index, createusers
from django.contrib.auth import views as authViews
urlpatterns = [

    path('', index, name='index'),
    path('create/', createusers, name='createusers'),
    path('exit/', authViews.LogoutView.as_view(next_page='/'), name='exit'),
    path('completeuser/', authViews.LogoutView.as_view(next_page='/'), name='completeuser'),

]
#test