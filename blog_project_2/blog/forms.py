from django import forms
from .models import *

#in other to impliment multiple choice functionality, there are two ways of doing it, on being to hardcode it into the system.as shown below....the problem is that its not dynamic so is inefficient
#choices = [('coding','coding'),('sports','sports'),('entertainment','entertainment')]#while using select boxes u have to put it double, one to remember the value the other is the value...LOL
choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author','title','title_tag','category','image','text')

        #widget helps ablication of form designs on django forms wen using django generated forms
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control','Placeholder':'Enter Blog Title'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'client', 'type':'hidden'}),#hidden hides the aspect of the form
            #'author':forms.Select(attrs={'class':'form-control'}),
            'text':forms.Textarea(attrs={'class':'form-control'}),
            'category':forms.Select(choices=choice_list,attrs={'class':'form-control','Placeholder':'select category'}),
            #'snippet':forms.Textarea(attrs={'class':'form-control'}),
            #'title':forms.TextInput(attrs={'class':'textinputclass'}),
            #'text' :forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
            }


class EditForm(forms.ModelForm):
    
    class Meta():
        model = Post
        fields = ('title','title_tag','text','image')

        #widget helps ablication of form designs on django forms wen using django generated forms
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control','Placeholder':'Enter Blog Title'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            'text':forms.Textarea(attrs={'class':'form-control'}),
            
            }



class CommentForm(forms.ModelForm):
    
    class Meta():
        model = Comment
        fields = ('author','text')

        #widget helps ablication of form designs on django forms wen using django generated forms
        widgets = {
            'author':forms.TextInput(attrs={'class':'form-control','Placeholder':'Enter Name'}),
            'text':forms.Textarea(attrs={'class':'form-control'}),            
            }
