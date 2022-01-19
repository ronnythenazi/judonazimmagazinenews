from django.urls import path, include
#from magazine import urls
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import  *

app_name = 'social'

urlpatterns = [

path('notification/post/<int:notification_pk>/<int:post_pk>', PostNotification.as_view(), name="post-notification"),
path('notification/profile/<int:notification_pk>/<int:profile_pk>', FollowNotification.as_view(), name="follow-notification"),
path('notification/comment/<int:notification_pk>/<int:post_pk>/<int:comment_pk>', CommentNotification.as_view(), name="comment-notification"),
path('notification/comment_of_comment/<int:notification_pk>/<int:post_pk>/<int:comment_pk>/<int:com_of_com_pk>', ComOfComNotification.as_view(), name="com-of-com-notification"),
path('notification/remove_notification/<int:notification_pk>', remove_notification, name = 'remove-notification'),
path('notification/ajax', ajax_notifications, name = 'ajax-notifications'),
path('notification/ajax/comment', ajax_notification_comment, name = 'ajax_notification_comment'),
path('notification/ajax/comment-of-comment', ajax_notification_com_of_com, name = 'ajax_notification_com_of_com'),

]
