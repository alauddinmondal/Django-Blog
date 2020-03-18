from django.db import models
from django import forms
# from django.urls import reverse
from django.core import validators
from django.core.validators import ValidationError
from django.contrib.auth.models import User
from tinymce.widgets import TinyMCE
from tinymce.models import HTMLField
from django.utils.html import format_html


# Create your models here.

def min_length_check(val):
    if len(val) <= 10:
        raise ValidationError("%(vals)s must be greater than 10", params={'vals':val})

class myCategory(models.Model):
    title = models.CharField(validators=[min_length_check], max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Posts(models.Model):
    STATUS_CHOICES = [
    ('d', 'Draft'),
    ('p', 'Published'),
    ('w', 'Withdrawn'),
    ]
    title = models.CharField(validators=[min_length_check], max_length=255)  
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    thumbnail = models.FileField(upload_to='posts/', null=True)
    category = models.ManyToManyField(myCategory, related_name='categories', default=0)
    content = HTMLField(validators=[min_length_check])
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = models.Manager

    def __str__(self):
        return self.title
    
    def show_thumbnail(self):
        return format_html('<img src="/static/%s" width="100" />'%self.thumbnail)
    show_thumbnail.short_description = 'Post Thumbnail'

    def show_content(self):
        return format_html(self.content)
    show_content.short_description = 'Post Content'
    
    # def get_absolute_url(self):
    #     return reverse('show', kwargs={'pk': self.pk})

    class Meta:
        db_table = 'post'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created_at']



class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title','content','thumbnail','user','category']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'This is a post title'}),
            'content': TinyMCE(attrs={'class':'form-control','placeholder':'Enter title'}),
            'thumbnail':forms.FileInput(attrs={'class':'form-control','placeholder':'upload file', 'multiple':True}),
            'user': forms.Select(attrs={'class':'form-control'}),
            'category': forms.CheckboxSelectMultiple(attrs={'class':'list-group list-group-horizontal listNone'}),
        }

        labels = {
            'title': 'Enter Post Title',
            'content': 'Please enter some text here',
            'thumbnail':'Please select any file',
        }

        help_texts = { }

        error_messages = { }

    def clean(self):
        fields = self.cleaned_data
        keys = list(fields.keys())

        if len(fields['title']) <= 10:
            raise validators.ValidationError("%(vals)s must be greater than 10", params={'vals':keys[0]})


        if len(fields['content']) <= 50:
            raise validators.ValidationError("%(vals)s must be greater than 10", params={'vals':keys[1]})

class Gallery(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    images = models.FileField(upload_to='posts/', blank=True, null=True)
