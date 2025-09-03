from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

router_v1 = DefaultRouter()
router_v1.register("posts", PostViewSet, basename="posts")
router_v1.register("groups", GroupViewSet, basename="groups")
router_v1.register("follow", FollowViewSet, basename="follow")

comment_list = CommentViewSet.as_view({"get": "list", "post": "create"})
comment_detail = CommentViewSet.as_view(
    {"get": "retrieve", "patch": "partial_update",
     "put": "update", "delete": "destroy"})

urlpatterns = [
    path("v1/", include(router_v1.urls)),
    path("v1/posts/<int:post_id>/comments/", comment_list),
    path("v1/posts/<int:post_id>/comments/<int:pk>/", comment_detail),
    path("v1/jwt/create/", TokenObtainPairView.as_view()),
    path("v1/jwt/refresh/", TokenRefreshView.as_view()),
    path("v1/jwt/verify/", TokenVerifyView.as_view()),
]
