from apps.posts.views import PostAPIViewSet, PostImageViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('posts', PostAPIViewSet)
router.register('post-images', PostImageViewSet)

urlpatterns = router.urls

