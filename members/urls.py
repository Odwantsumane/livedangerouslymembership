from django.urls import path
from . import views
from events import views as v

urlpatterns = [
    path('', views.members, name='members'),
    # path('details/<int:id>', views.details, name='details'),
    #path('', views.main, name='main'),
    path('testing/', views.testing, name='testing'),
    path('prods/',views.productItems, name='productItems')
]