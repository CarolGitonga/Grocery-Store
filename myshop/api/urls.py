from django.urls import path, include
from . import views


from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

app_name = 'api'
router = routers.DefaultRouter() #parent router

router.register('products', views.ProductsViewSet)
router.register('categories', views.CategoryViewSet)
router.register("carts", views.CartViewSet)


product_router = routers.NestedDefaultRouter(router, 'products', lookup='product')#child router
product_router.register('reviews', views.ReviewViewSet, basename='product_reviews')


urlpatterns = [
    path('', include(router.urls)),
    path("", include(product_router.urls)),
#     path('products/<str:pk>', views.ApiProduct.as_view()),
#     path('categories', views.APICategories.as_view()),
#     path('categories/<str:pk>', views.APICategory.as_view())
]