from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import BookListApiView,book_list_view,BookDetailApiView,BookDeleteApiView, \
    BookUpdateApiView,BookCreateApiView,BookListCreateApiView,BookUpdateDeleteView,BookViewSet


router = SimpleRouter()
router.register('books', BookViewSet, basename='books')


urlpatterns = [
    path('books/', BookListApiView.as_view(),),
    path('booklistcreate/', BookListCreateApiView.as_view()),
    path('bookupdatedelete/<int:pk>/', BookUpdateDeleteView.as_view()),
    path('books/create/', BookCreateApiView.as_view()),
    path('books/<int:pk>', BookDetailApiView.as_view()),
    path('books/<int:pk>/update/', BookUpdateApiView.as_view()),
    path('books/<int:pk>/delete/', BookDeleteApiView.as_view()),
]

urlpatterns = urlpatterns + router.urls

#cdrf.co ----- rest frameworkdagi barcha viewlar wu yerda