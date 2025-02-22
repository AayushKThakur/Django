from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('products/', views.all_products, name = 'all_products')
    path('prdocuts/<int:product_id>/', views.products_details_by_id, name = "products_by_id"),
    path("products/name/<str:product_name>/", views.prodct_by_name, name = "product_by_name")

]