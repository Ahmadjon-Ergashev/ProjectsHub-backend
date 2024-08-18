from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet
from .models import Company

router = DefaultRouter()
router.register(r'companies', CompanyViewSet, 'company')

urlpatterns = router.urls
