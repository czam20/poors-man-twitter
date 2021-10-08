from rest_framework import routers
from rest_framework.routers  import DefaultRouter
from .views import TweetViewSet

router = DefaultRouter()
router.register(r'', TweetViewSet, basename="tweet")
urlpatterns = router.urls