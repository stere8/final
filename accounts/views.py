# accounts/views.py
from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from listings.models import Listing
from .forms import UserForm, UserUpdateForm
from django.contrib.auth import views as auth_views, logout as auth_logout
from django.db.models import Q
from .models import User


def superuser_required(view_func):
    decorated_view_func = user_passes_test(lambda u: u.is_superuser, login_url='listing_list')(view_func)
    return decorated_view_func


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')  # Redirect to a login page or another page after successful signup
    else:
        form = UserForm()
    return render(request, 'accounts/signup.html', {'form': form})


class CustomLoginView(auth_views.LoginView):
    template_name = 'registration/login.html'
    next_page = 'listing_list'  # Redirect to 'listing_list' after login

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('listing_list')  # Replace with your desired redirect URL
        return super().dispatch(request, *args, **kwargs)


def custom_logout(request):
    auth_logout(request)
    return redirect('login')  # Redirect to the login page after logout


@superuser_required
def account_search(request):
    search_term = request.GET.get('q', '')
    filtered_listings = User.objects.filter(
        Q(username__icontains=search_term) | Q(email__icontains=search_term) | Q(first_name__icontains=search_term) | Q(last_name__icontains=search_term)
    )  # Search by title and description

    paginator = Paginator(filtered_listings, 5)  # Set the number of listings per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'accounts': page_obj, 'is_paginated': page_obj.has_other_pages(), 'is_from_search': True,
               'search_term': search_term}
    return render(request, 'accounts/accounts_list.html', context)


@superuser_required
def accounts_list(request):
    users_list = User.objects.all()
    p = Paginator(users_list, 5)  # Set the number of listings per page

    page = request.GET.get('page')
    accounts = p.get_page(page)

    context = {'accounts': accounts}
    return render(request, 'accounts/accounts_list.html', context)


@superuser_required
def account_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    reserved_listings = Listing.objects.filter(reserved_by_id=user.id)
    print(reserved_listings, user.id)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('account_detail', pk=user.pk)
    else:
        form = UserUpdateForm(instance=user)

    context = {
        'account': user,
        'reserved_listings': reserved_listings,
        'form': form
    }
    return render(request, 'accounts/accounts_detail.html', context)