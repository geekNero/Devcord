from django.urls import path
from . import views
urlpatterns = [
    path('home',views.home,name="home"),
    path('search',views.search,name='search'),
    path('add/<str:username>',views.add_friend,name='friend_request'),
    path('remove/<str:username>',views.remove,name='remove'),
    path('profile/<str:username>',views.profile,name='profile'),
    path('cancel/<str:username>',views.cancel_request,name='cancel'),
    path('accept/<str:username>',views.accept,name='accept'),
    # path('addf/<int:userID>/',views.send_friend_request,name='sfr'),
    # path('acceptf/<int:requestID/',views.accept_friend_request,name='afr'),
]