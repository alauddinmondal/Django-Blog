from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


class PostsConfig(AppConfig):
    name = 'posts'
    verbose_name = 'Blogging System'


class MyadminConfig(AdminConfig):
    default_site = 'posts.admin.myAdminsite'
    verbose_name = ("Alauddin Main Administration")