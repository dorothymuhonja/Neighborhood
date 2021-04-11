from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login 
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from .models import *
from .forms import *

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})


def index(request):
    return render(request,"index.html")


# @login_required
# @csrf_protect
# def logout(request):
#     django_logout(request)
#     return HttpResponseRedirect('login')

@login_required
@csrf_protect
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'profile/profile.html', context)


def neighborhoods(request):
    all_hoods = Neighborhood.objects.all()
    all_hoods = all_hoods[::-1]

    context = {
        'all_hoods': all_hoods,
    }
    return render(request, 'neighborhoods.html', context)


@login_required
@csrf_protect
def join_neighborhood(request, id):
    neighborhood = get_object_or_404(Neighborhood, id=id)
    request.user.profile.neighborhood = neighborhood
    request.user.profile.save()
    messages.success(request, 'You have successfully joined this neighborhood')
    return redirect('neighborhoods')


@login_required
@csrf_protect
def leave_neighborhood(request, id):
    neighborhood = get_object_or_404(Neighborhood, id=id)
    request.user.profile.neighborhood = None
    request.user.profile.save()
    messages.success(request, 'You have succesfully left this neighborhood')
    return redirect('neighborhoods')


@login_required
@csrf_protect
def single_neighborhood(request, hood_id):
    neighborhood = Neighborhood.objects.get(id=hood_id)
    business = Business.objects.filter(neighborhood=neighborhood)
    posts = Post.objects.filter(neighborhood=neighborhood)
    posts = posts[::-1]
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            business_form = form.save(commit=False)
            business_form.neighborhood = neighborhood
            business_form.user = request.user.profile
            business_form.save()
            return redirect('single-hood', neighborhood.id)
    else:
        form = BusinessForm()
    context = {
        'neighborhood': neighborhood,
        'business': business,
        'form': form,
        'posts': posts
    }
    return render(request, 'single_hood.html', context)


@login_required
@csrf_protect
def create_post(request, hood_id):
    neighborhood = Neighborhood.objects.get(id=hood_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.neighborhood = neighborhood
            post.user = request.user.profile
            post.save()
            messages.success(request, 'You have created a post')
            return redirect('single-hood', neighborhood.id)

    else:
        form = PostForm()
    return render(request, 'post.html', {'form': form})

