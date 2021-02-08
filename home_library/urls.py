from django.urls import path  
from django.conf.urls.static import static
from django.conf import settings
from .views import BookList, AuthorList, PublisherList, FriendList, AuthorEdit, AuthorCreate, AuthorDelete, \
    PublisherCreate, PublisherEdit, PublisherDelete, FriendEdit, FriendCreate, FriendDelete, BookDetail, \
        BookEdit, BookCreate, BookDelete
app_name = 'home_library'

urlpatterns = [
    path('', BookList.as_view(), name='index'),
    path('book/<int:pk>/', BookDetail.as_view(), name='book_detail'),
    path('book/<int:pk>/edit/', BookEdit.as_view(), name='book_edit'),
    path('book/add/', BookCreate.as_view(), name='book_add'),
    path('book/<int:pk>/delete/', BookDelete.as_view(), name='book_delete'),
    path('return_book/', BookEdit.return_book, name='return_book'),
    path('authors/', AuthorList.as_view(), name='authors'),
    path('publishers/', PublisherList.as_view(), name='publishers'),
    path('friends/', FriendList.as_view(), name='friends'),
    path('author/<int:pk>/edit/', AuthorEdit.as_view(), name='author_edit'),
    path('author/add/', AuthorCreate.as_view(), name='author_add'),
    path('author/<int:pk>/delete/', AuthorDelete.as_view(), name='author_delete'),
    path('publisher/<int:pk>/edit/', PublisherEdit.as_view(), name='publisher_edit'),
    path('publisher/add/', PublisherCreate.as_view(), name='publisher_add'),
    path('publisher/<int:pk>/delete/', PublisherDelete.as_view(), name='publisher_delete'),
    path('friend/<int:pk>/edit/', FriendEdit.as_view(), name='friend_edit'),
    path('friend/add/', FriendCreate.as_view(), name='friend_add'),
    path('friend/<int:pk>/delete/', FriendDelete.as_view(), name='friend_delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
