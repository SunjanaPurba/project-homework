from django.urls import path

from .views.fbv_views import book_list, book_add, book_update, book_delete



urlpatterns = [
    path('fbv/', book_list, name='book_list')
]
from .views.cbv_views import BookListView, BookCreateView, BookUpdateView, BookDeleteView


urlpatterns = [
    #FBVs
    path('fbv/', book_list, name='book_list'),         
    path('fbv/add/', book_add, name='book_add'),       
    path('fbv/update/<int:pk>/', book_update, name='book_update'),  
    path('fbv/delete/<int:pk>/', book_delete, name='book_delete'), 

    #CBVs
    path('cbv/', BookListView.as_view(), name='book_list'), 
    path('cbv/add/', BookCreateView.as_view(), name='book_add'), 
    path('cbv/update/<int:pk>/', BookUpdateView.as_view(), name='book_update'),
    path('cbv/delete/<int:pk>/', BookDeleteView.as_view(), name='book_delete'),  
]
