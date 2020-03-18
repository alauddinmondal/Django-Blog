from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from posts.models import Posts, Gallery, PostsForm, myCategory
from django.views.generic import TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.http import JsonResponse, HttpResponse
from django.core.mail import send_mail,send_mass_mail, mail_admins, mail_managers

class index(FormView):
    template_name = 'index.html'
    form_class = PostsForm
    success_url = '/'

class show(TemplateView):
    template_name = 'list_post.html'
    model = Posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Posts.objects.all()
        return context
    
    

class add(CreateView):
    # model = Posts
    # fields = '__all__'
    form_class = PostsForm
    template_name = 'posts/posts_form.html'
    success_url = '/'

    def form_invalid(self,form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        files = self.request.FILES.getlist('thumbnail')
        # post = form.save(commit=False)
        # post.save()
        response = super().form_valid(form)
        for f in files:
            gallery = Gallery(post_id=self.object.pk, images=f)
            gallery.save()
        # return super().form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk':self.object.pk,
                'success': 'Record added successfuly'
               
            }
            return JsonResponse(data)
        else:
            return response
        
    

class edit(UpdateView):
    # model = Posts
    # fields = '__all__'
    form_class = PostsForm
    success_url = '/'

    def get_queryset(self):
        id = self.kwargs['pk']
        return Posts.objects.filter(pk=id)

    def form_invalid(self,form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        Gallery.objects.filter(post_id=self.kwargs['pk']).delete()
        files = self.request.FILES.getlist('thumbnail')
        # post = form.save(commit=False)
        # post.save()
        response = super().form_valid(form)
        for f in files:
            gallery = Gallery(post_id=self.object.pk, images=f)
            gallery.save()
        # return super().form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk':self.object.pk,
                'success': 'Record added successfuly'  
            }
            return JsonResponse(data)
        else:
            return response
    


class delete(DeleteView):
    model = Posts
    success_url = reverse_lazy('show')
    

def send_mails(request):
    mail_admins('I found error','Dear admin we have found many errors',fail_silently=False)
    mail_managers('I found error','Dear admin we have found many errors',fail_silently=False)

    return HttpResponse('This is has been sent to our Managers')