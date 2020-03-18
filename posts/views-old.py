from django.shortcuts import render, redirect
from posts.models import Posts, Gallery, PostsForm, myCategory
from django.views.generic import TemplateView, ListView, View

# Create your views here.

def index(request):
    form = PostsForm()
    data = Posts.objects.all()
    mycathere = myCategory.objects.all()
    
    if request.method == 'POST':
        form = PostsForm(request.POST, request.FILES)
        files = request.FILES.getlist('thumbnail')        
        if form.is_valid():
            post = form.save(commit=False)
            form.save()
            for f in files:
                gallery = Gallery(post=post,images=f)
                gallery.save()
            form.save(commit=False)
            return redirect('/')
    return render(request, 'index.html', {'title':'Add new post', 'form':form, 'datas':data, 'catsgry': mycathere})



# def cbview(request):
#     return render(request, 'class_view.html', {})

# class cbview(TemplateView):
#     template_name='class_view.html'

# class cbview(ListView):
#     model = Posts
#     template_name='class_view.html'

# class cbview(View):
#     template_name='class_view.html'
    
#     def get(self, request):
#         data = Posts.objects.all()
#         form = PostsForm()    
#         return render(request, self.template_name, {'object_list':data, 'form':form})


class cbview(TemplateView):
    template_name='class_view.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'object_list': Posts.objects.all(),
            'form':PostsForm()
        }
        return context

    def post(self, request):
        form = PostsForm(request.POST, request.FILES)
        files = request.FILES.getlist('thumbnail')        
        if form.is_valid():
            post = form.save(commit=False)
            form.save()
            for f in files:
                gallery = Gallery(post=post,images=f)
                gallery.save()
            
            return redirect('/cbview')



    