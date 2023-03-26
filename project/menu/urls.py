from django.urls import path
from .import views
app_name = 'menu'

urlpatterns = [
    
    path('collections',views.collections , name= 'collections'),
    path('collections/<str:slug>', views.collectionsview, name="collectionsview"),
    path('collections/<str:cate_slug>/<str:prod_slug>',views.productview,name="productview"),
    path('cart/',views.cart, name='cart')
    # path('dum/',views.dum, name='dum',),
]
