from rest_framework.routers import DefaultRouter
from .views import DeveloperViewSet, TeamViewSet, SkillViewSet


router = DefaultRouter()
router.register(r'developers', DeveloperViewSet, 'developer')
router.register(r'teams', TeamViewSet, 'team')
router.register(r'skills', SkillViewSet, 'skill')

urlpatterns = router.urls
