from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.views.generic import UpdateView

from cabinet.forms import UserProfileEditForm
from cabinet.models import UserProfile


def index(request):
    """View для главной страницы"""
    return render(request, 'cabinet/index.html')


@login_required
def cabinet(request):
    """View для страницы личного кабинета"""
    context = {
        'cabinet': request.user.userprofile,
    }

    return render(request, 'cabinet/cabinet.html', context)


@require_http_methods(['GET', 'POST'])
@login_required
def edit_profile(request):
    """View редактирования профиля"""
    if request.method == 'POST':
        form = UserProfileEditForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            request.user.username = form.cleaned_data['username']
            request.user.email = form.cleaned_data['email']
            request.user.first_name = form.cleaned_data['first_name']
            request.user.last_name = form.cleaned_data['last_name']
            request.user.save()

            cabinet_url = reverse('cabinet')
            return redirect(f'{cabinet_url}?success_edit_profile=true')

    form = UserProfileEditForm(instance=request.user.userprofile)

    template = 'cabinet/edit_profile.html'
    context = {
        'form': form,
    }
    return render(request, template, context)

