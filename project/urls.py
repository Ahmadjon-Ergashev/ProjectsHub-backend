from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, TagViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, 'project')
router.register(r'tags', TagViewSet, 'tag')

urlpatterns = router.urls
