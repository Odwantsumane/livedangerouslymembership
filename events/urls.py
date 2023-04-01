from django.urls import path
from members import views as v
from . import views as vs

urlpatterns = [
    path('', vs.home, name='main'),
    path('login_user/', v.login_user, name='login_user'),
    path('signup/', v.signup_user, name='signup_user'),
    path('products/',vs.products, name='products'),
    path('members/',v.members, name='members'),
    path('members/details/<int:id>', v.details, name='details'),
    path('chat/', vs.chat, name="chat"),
    path('chat/<int:id>', vs.delete, name="delete"),
    path('logout/', v.logout_user, name="logout"),
    path('images/', vs.images, name="images"),
    path('camping/', vs.camping, name="camping"),
    path('canoeing/', vs.canoeing, name="canoeing"),
    path('skydiving/', vs.skydiving, name="skydiving"),
    path('hiking/', vs.hiking, name="hiking"),
    path('gearup/', vs.gearup, name="gearup"),
    path('gearup/skydivinggear/', vs.skydivingGear, name="skydivingg"),
    path('gearup/canoeinggear/', vs.canoeingGear, name="canoeingg"),
    path('gearup/campinggear/', vs.campingGear, name="campingg"),
    path('gearup/hikinggear/', vs.hikingGear, name="hikingg"),
    path('cart/', vs.cart, name="cart"),

    path('campp/', vs.campprod, name="camp_products"),
    path('hikp/', vs.hikprod, name="hiking_products"),
    path('canp/', vs.canprod, name="can_products"),
    path('skyp/', vs.skyprod, name="sky_products"),

    path('prods/',v.productItems, name='productItems'),
]
    