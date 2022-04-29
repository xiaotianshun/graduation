from django.urls import path
from image_search.views.search.manager import Search, FuzzySearch

urlpatterns = [
    path('', Search, name='search'),
    path('fuzzy', FuzzySearch, name='fuzzy_search'),
]
