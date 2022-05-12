from django.shortcuts import render,get_object_or_404,redirect
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,PasswordChangeForm
from django.urls import reverse_lazy
from .forms import * 
from django.contrib.auth.views import PasswordChangeView
from blog.models import *

# Create your views here.

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('post_list')

    def get_object(self):
        return self.request.user



class PassWordChangeView(PasswordChangeView):
    form_class = PasswordUpdateForm
    #form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')
    #success_url = reverse_lazy('home')


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        context["page_user"] = page_user
        return context


class EditProfilePageView(generic.UpdateView):
    form_class = ProfilePageForm
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    success_url = reverse_lazy('login')
    #fields = ['bio','profile_pic','website_url','facebook_url','twitter_url','instagram_url','pintrest_url']


#this class view creates the user profile
class CreateProfilePageView(CreateView):
    model = Profile
    template_name = 'registration/create_user_profile.html'
    #fields = '__all__'
    form_class = ProfilePageForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)    
##################################FUNCTION VIEWS################################################

def password_success(request):
    return render(request, 'registration/password_success.html', {})