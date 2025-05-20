from django.contrib.auth import get_user_model 
from rest_framework import generics # we need for generic views

from rest_framework import viewsets 
from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, UserSerializer

from rest_framework.permissions import IsAdminUser # for user permission 

'''
when we using generics you see how we have to methods PostList, PostDetail, UserList, UserDetail
and we are using queryset like 4 time, but we want to make it simple using viewset, viewset can handle multiple 
actions in on class, so for Post actions, we will have both PostList and PostDetail in one PostViewSet class, and 
User actions UserList and UserDetail in one UserViewSet class. that way we avoid repition and if we also ue viewsets
with router(which generate urls authomatically) it would save us a lot of time as out code base grow and got more 
end points

'''

# using viewset, we have 2 classes instead of 4, so you can imagine how it save so much developer time,
# as the code grows 

# remeber we can use router in combination with viewsets
# work directly with viewsets to automatically generate URL patterns for us.
'''
Our current posts/urls.py file has four URL patterns: two for blog posts and two for users. We can
instead adopt a single route for each viewset. So two routes instead of four URL patterns. That
sounds better, right?

Django REST Framework has two default routers: SimpleRouter and DefaultRouter. We will
use SimpleRouter but its also possible to create custom routers for more advanced functionality.

'''

class PostViewSet(viewsets.ModelViewSet): 
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
class UserViewSet(viewsets.ModelViewSet): 
    permission_classes = [IsAdminUser]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer



# Using generics we would have this
'''
class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
class UserList(generics.ListCreateAPIView): # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
class UserDetail(generics.RetrieveUpdateDestroyAPIView): # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
'''

