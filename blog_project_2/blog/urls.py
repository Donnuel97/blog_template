from django.urls import path
from . import views #this import imports function based views



urlpatterns = [
	path('', views.PostListView.as_view(), name="post_list"),
	path('post/<int:pk>', views.PostDetailView.as_view(), name="post_detail"),
	path('about/', views.AboutView.as_view(), name="about"),
	path('new_post/', views.CreatePostView.as_view(), name="post_new"),
	path('add_category/', views.AddCategoryView.as_view(), name="add_category"),
	path('post/<int:pk>/comment/', views.AddCommentView.as_view(), name="add_comment"),
    #path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name="post_edit"),
    #path('post/<int:pk>/remove/', views.PostDeleteView.as_view(), name="post_remove"),

	####### old formats of calling model id ########
	#path('post/(?P<pk>\d+)', views.PostDetailView.as_view(), name="post_detail"),
	path('post/edit/<int:pk>', views.UpdatePostView.as_view(), name="post_edit"),
    path('post/remove/<int:pk>', views.PostDeleteView.as_view(), name="post_remove"),

	#COmments
	#path('article/<int:pk>/comments', views.AddCommentView.as_view(), name="add_comment_to_post"),
	#path('post/(?P<pk>\d+)/comment', views.add_comment_to_post, name="add_comment_to_post"),
	#path('comment/(?P<pk>\d+)/approve', views.comment_approve, name="comment_approve"),
	#path('comment/(?P<pk>\d+)/remove', views.comment_remove, name="comment_remove"),

	#path('post/(?P<pk>\d+)/publish', views.post_publish, name="post_publish"),
	
    #path('drafts/', views.DraftListView.as_view(), name="post_draft_list"),
	path('category/<str:cats>/', views.CategoryView, name="category_view"),
	path('category-list/', views.CategoryListView, name="category_list"),
	#path('post/<int:pk>/comment', views.add_comment_to_post, name="add_comment_to_post"),
	#path('comment/<int:pk>/approve', views.comment_approve, name="comment_approve"),
	#path('comment/<int:pk>/remove', views.comment_remove, name="comment_remove"),
	#path('post/<int:pk>/publish', views.post_publish, name="post_publish"),
	
	#like views
	path('like/<int:pk>', views.likeview, name="like_post"),
]

