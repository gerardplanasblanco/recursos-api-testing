from rest_framework.routers import DefaultRouter
from .views import AutorViewSet, RecursViewSet

router = DefaultRouter()
router.register(r'autors', AutorViewSet, basename='autors')
router.register(r'recursos', RecursViewSet, basename='recursos')

urlpatterns = router.urls
