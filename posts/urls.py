from django.urls import path
# from .views import PostList, PostDetail # needed when we don't use viewsets

from rest_framework.routers import SimpleRouter # using router
from .views import UserViewSet, PostViewSet # we need the viewsets since router works directly with viewsets

router = SimpleRouter()

router.register("users", UserViewSet, basename="users")
router.register("", PostViewSet, basename="posts")

urlpatterns = router.urls





# when using generics, or hardcoding without viewset
'''
urlpatterns = [
    path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path("", PostList.as_view(), name="post_list"),
]

'''
