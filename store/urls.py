from django.urls import path
from .views import views,Signup,Login,logout,SearchResultsView,Updateprofile
from .middlewares import LoginCheckMiddleware,LogoutCheckMiddleware


urlpatterns = [
    path('',views.store,name="store"),
    path('cart/',views.cart,name="cart"),
    path('checkout/',views.checkout,name="checkout"),
    path('updete_Item/',views.updeteItem,name="updete_Item"),
    path('updete_favorite/',views.updetefavorite,name="updete_favorite"),
    path('process_order/',views.processOrder,name="process_order"),
    path('favorite/',views.favorite,name="favorite"),
    path('signup/',LogoutCheckMiddleware(Signup.as_view()),name="signup"),
    path('login',LogoutCheckMiddleware(Login.as_view()), name='login'),
    path('logout',LoginCheckMiddleware(logout), name='logout'),
    path('search', SearchResultsView.as_view(), name='search_results'),
    path('updateprofile/', Updateprofile.as_view(), name='updateprofile'),
    path('profile/',views.profile,name="profile"),
]