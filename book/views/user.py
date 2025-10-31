from book.forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, get_object_or_404, render
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from book.models import Favorite, Books


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "book/register.html", {"form": form})
    
    def post(self, request):
        form = RegisterForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.create_user(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=password
            )
            user.set_password(password)
            return redirect('login')
        
    
class LoginUserView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "book/login.html", {"form": form})
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f"Welcome back, {user.username}!")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")

            return render(request, "book/login.html", {"form": form})
        
        data = {
            'form': form
        }
        return render(request, "book/login.html", context=data)

def logout_admin(request):
    logout(request)
    return redirect('home')

class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "book/profile.html")
    
    def post(self, request):
        user = request.user
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        if first_name and last_name:
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            messages.success(request, "Profile updated successfully.")
        return redirect("profile")
    
class ChangePasswordView(LoginRequiredMixin, View):
    def post(self, request):
        user = request.user
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        conf_password = request.POST.get('conf_password') 
        if not user.check_password(old_password):
            messages.error(request, "Old password is incorrect.")
        elif new_password != conf_password:
            messages.error(request, "New passwords do not match.")
        elif old_password == new_password:
            messages.error(request, "New password cannot be the same as the old password.")
        else:
            user.set_password(new_password)
            user.save()
            messages.success(request, "Password changed successfully.")
            return redirect("login")

        return redirect("profile")


class FavoritView(LoginRequiredMixin, View):
    def get(self, request):
        favorite = Favorite.objects.filter(user=request.user).select_related('book')
        return render(request, "book/favorite.html", context={'favorite': favorite})
    
class AddFavoriteView(LoginRequiredMixin, View):
    def get(self, request, book_id):
        book = get_object_or_404(Books, id=book_id)
        Favorite.objects.get_or_create(user=request.user, book=book)
        messages.success(request, f"Added {book.title} to favorites.")
        return redirect('books')
    
class RemoveFavoriteView(LoginRequiredMixin, View):
    def get(self, request, book_id):
        book = get_object_or_404(Books, id=book_id)
        favorite = get_object_or_404(Favorite, user=request.user, book=book)
        favorite.delete()
        messages.success(request, f"Removed {book.title} from favorites.")
        return redirect('favorite')