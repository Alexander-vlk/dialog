from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render


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
