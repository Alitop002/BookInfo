from django.urls import path
from .views import HomeView,BooksAsView,RegisterView,LoginUserView,DetailView,FavoritView,logout_admin,ProfileView, ChangePasswordView,Category_as_View,AddFavoriteView,RemoveFavoriteView
urlpatterns = [
    path("", HomeView.as_view(), name='home'),
    path("books/", BooksAsView.as_view(),name='books'),
    path("register/", RegisterView.as_view() ,name='register'),
    path("login/",LoginUserView.as_view() , name='login'),
    path('detail/', DetailView.as_view(), name='detail'),
    path('detail/<int:book_id>/', DetailView.as_view(), name='detail'),
    path('category/', Category_as_View.as_view(), name='category'),
    path('favorite/',FavoritView.as_view() , name='favorite'),
    path('add-favorite/<int:book_id>/',AddFavoriteView.as_view() , name='add-favorite'),
    path('remove-favorite/<int:book_id>/',RemoveFavoriteView.as_view() , name='remove-favorite'),
    path('logout/', logout_admin, name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),

]
