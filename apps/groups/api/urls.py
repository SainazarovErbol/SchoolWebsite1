from apps.groups.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('posts', GroupAPIVewSet)

urlpatterns = router.urls
