from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('product/<int:id>', views.product, name='product'),
    path('product/<int:id>/update', views.update_product, name='update_product'),
    path('add', views.add_product, name='add_product'),
    path('delete/<int:id>', views.delete_product, name='delete_product'),
    path('login', views.login_view, name='login_view'),
    path('logout', views.logout_view, name='logout_view'),    
]