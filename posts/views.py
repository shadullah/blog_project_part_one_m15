from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django.utils.decorators import method_decorator


@login_required
# Create your views here.
def add_post(req):
    if req.method == 'POST':
        post_form = forms.postForm(req.POST)
        if post_form.is_valid():
            post_form.instance.author = req.user
            post_form.save()
            return redirect('add_post')
    else:
        post_form = forms.postForm()
    return render(req, 'add_post.html', {'form': post_form})

# add post using clASS based view
@method_decorator(login_required, name='dispatch')
class addPostCreatView(CreateView):
    model = models.Post
    form_class = forms.postForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('add_post')
    def form_valid(self, form):
        form.instance.author = self.req.user
        return super().form_valid(form)


@login_required
def edit_post(req, id):
    post = models.Post.objects.get(pk=id)
    post_form = forms.postForm(instance=post)
    
    if req.method == 'POST':
        post_form = forms.postForm(req.POST, instance=post)
        if post_form.is_valid():
            post_form.instance.author = req.user
            post_form.save()
            return redirect('/')
    return render(req, 'add_post.html', {'form': post_form})

@method_decorator(login_required, name='dispatch')
class editClassView(UpdateView):
    model = models.Post
    form_class = forms.postForm
    template_name = 'add_post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')


@login_required
def delete_post(req, id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('/')

class deleteClassView(DeleteView):
    model = models.Post
    template_name = 'delete_post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')




class detailsPageClass(DetailView):
    model = models.Post
    pk_url_kwarg = 'id'
    template_name = 'blog_details.html'

    def post(self, req, *args, **kwargs):
        comment_form = forms.CmntForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_Cmmnt = comment_form.save(commit=False)
            new_Cmmnt.post = post
            new_Cmmnt.save()
        return self.get(req, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object 
        comments = post.comments.all()
        comment_form = forms.CmntForm()

        context['comments'] = comments
        context['comment_form']=comment_form
        return context



