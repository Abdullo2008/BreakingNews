from django.urls import path
from .views import index, Contact_Page_View, single, categories_all, NewsCreateView, NewsDeleteView, NewsUpdateView, \
    SearchView

urlpatterns = [
    path('', index.as_view(), name="index"),
    path('contact/', Contact_Page_View, name="contact_page"),
    path('new/<int:id>/', single, name="single"),
    path('category/<int:id>/', categories_all, name="categories_all"),
    path('news/create', NewsCreateView.as_view(), name='news_create_page'),
    path('news/<pk>/delete', NewsDeleteView.as_view(), name='news_delete_page'),
    path('news/<pk>/update', NewsUpdateView.as_view(), name='news_update_page'),
    path('search/', SearchView, name='search'),
]
