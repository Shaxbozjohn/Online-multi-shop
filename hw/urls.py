from django.urls import path
from  . import views


urlpatterns = [
    path("", views.homepage, name = "home"),
    path("products", views.products_page, name="products"),
    path("login", views.login_page, name="login"),
    path("profile", views.profile_page, name="profile"),
    path("order-create", views.order_create_page, name="order-create"),
    path('category/<int:category_id>/', views.products_by_category, name="products_by_category")
]