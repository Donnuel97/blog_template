from email.policy import default
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
#to beautify the post form field
from ckeditor.fields import RichTextField #u have to pip install
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    #this function rediects especially for class based views
    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.name


#User profile models
class Profile(models.Model):
    user = models.OneToOneField(User, null=True,on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    website_url = models.CharField(max_length=200,null=True, blank=True)
    facebook_url = models.CharField(max_length=200,null=True, blank=True)
    twitter_url = models.CharField(max_length=200,null=True, blank=True)
    instagram_url = models.CharField(max_length=200,null=True, blank=True)
    pintrest_url = models.CharField(max_length=200,null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse("post_list")


#user post models
class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    title_tag = models.CharField(max_length=200)
    text = RichTextField(blank='True', null='True')
    image = models.ImageField(null=True, blank=True, upload_to="images/", default='default.jpg')#sets the default, picks the default from the media folder
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=250)
    likes = models.ManyToManyField(User, related_name = 'blog_posts')
    #snippet = models.CharField(max_length=250)



    #this function helps to add the total number of likes on a post
    def total_likes(self):
        return self.likes.count()
        
    #this method handles wen blog is published
    def publish(self):
        self.published_date = timezone.now()
        self.save() 

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    #the below function is a django function method cuz django looks for it
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk':self.pk})

    #send the user straightbto home page.
    #def get_absolute_url(self):
        #return reverse("post_list")

    #further test required   
    #def get_absolute_url(self):
        #return reverse("post_detail", args=(str(self.id)))


    def __str__(self):
        return self.title



class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = RichTextField(blank='True', null='True')
    create_date = models.DateTimeField(default=timezone.now)
    #approved_comment = models.BooleanField(default=False)

    #def approve(self):
    #    self.approved_comment = True
    #    self.save()

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return '%s - %s' % (self.post.title, self.author)