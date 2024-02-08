from django.db.models import Q
from rest_framework.generics import ListAPIView

from .models import Product, Category, Tag
from .serializers import ProductSerializer, CategorySerializer, TagSerializer


class ProductListView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.select_related('category').prefetch_related('tags')

        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category=category)

        tags = self.request.query_params.getlist('tag')
        if tags:
            queryset = queryset.filter(tags__in=tags).distinct()

        search_query = self.request.query_params.get('search')
        if search_query:
            queryset = queryset.filter(Q(name__icontains=search_query))

        return queryset


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagListView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer