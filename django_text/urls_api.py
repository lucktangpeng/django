from rest_framework import routers

from book_text.views import BookModelViewSet, TypeModelViewSet, AuthorModelViewSet

router = routers.DefaultRouter()

router.register("book",BookModelViewSet)
router.register("type",TypeModelViewSet)
router.register("author",AuthorModelViewSet)

urlpatterns = router.urls

urlpatterns += [
]
