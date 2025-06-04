from rest_framework.routers import SimpleRouter

from cabinet.views.private import UserViewSet


router = SimpleRouter()
router.register(r'users', UserViewSet)


urlpatterns = []

urlpatterns.extend(router.urls)
