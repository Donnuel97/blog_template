from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView#connected to the about view
from .models import *
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from .forms import * 
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

#for list page of category to show remove Def get_context_data, further manipulation in frontend.


###########################################################################
#####################-----CLASS BASED VIEWS-------#########################
class AboutView(TemplateView):
    template_name = 'about.html'

    #this handles listing of categories on base.html and links the listed categories to the various destination
    #even though other pages pull from the base file these category func will not work excxept we add it to the views handling these pages
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AboutView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
    

#handles home page
class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    ordering = ['-create_date']

     #this handles listing of categories on base.html and links the listed categories to the various destination
    #even though other pages pull from the base file these category func will not work excxept we add it to the views handling these pages
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostListView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    #this handles listing of categories on base.html and links the listed categories to the various destination
    #even though other pages pull from the base file these category func will not work excxept we add it to the views handling these pages
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context['liked'] = liked
        return context


class CreatePostView(CreateView):
    #login_url = '/login/'
    #redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    template_name = 'post_form.html'
    #fields = '__all__'
    model = Post

    #this handles listing of categories on base.html and links the listed categories to the various destination
    #even though other pages pull from the base file these category func will not work excxept we add it to the views handling these pages
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(CreatePostView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    #fields = ['title','title_tag','text']
    form_class = EditForm

    #this handles listing of categories on base.html and links the listed categories to the various destination
    #even though other pages pull from the base file these category func will not work excxept we add it to the views handling these pages
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(UpdatePostView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

    #this handles listing of categories on base.html and links the listed categories to the various destination
    #even though other pages pull from the base file these category func will not work excxept we add it to the views handling these pages
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostDeleteView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class AddCommentView(CreateView):
    form_class = CommentForm
    template_name = 'add_comment.html'
    model = Comment

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)    

    success_url = reverse_lazy('post_list')
    #fields = '__all__'

    

###########################################################################
##################-----FUNCTION BASED VIEWS-------#########################

#the next views handles the categorization capabilities
#in the second line, category is used because that is the name of the field in the table u want to query\access.
def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html',{'cats':cats.title().replace('-', ' '),'category_posts':category_posts})


def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'categories_list.html',{'cat_menu_list':cat_menu_list})



#Like and dislike function view
def likeview(request,pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        Liked = False
    else:
        post.likes.add(request.user)
        liked = True
    
    return HttpResponseRedirect(reverse('post_detail',args=[str(pk)]))
