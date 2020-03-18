from django.urls import path
# from posts.views import index, cbview
from posts.views import show, add, edit, delete,send_mails
# from django.views.generic import TemplateView



urlpatterns = [
    path('', show.as_view(), name='show'),
    path('add/', add.as_view(), name='post.add'),
    path('edit/<int:pk>/', edit.as_view(), name='post.edit'),
    path('delete/<int:pk>/', delete.as_view(), name='post.delete'),
    path('mails/', send_mails, name='mails')

]