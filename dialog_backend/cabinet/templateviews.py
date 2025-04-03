from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render


def index(request):
    return render(request, 'cabinet/index.html')


@login_required
def cabinet(request, cabinet_id):
    if request.user.userprofile.id != cabinet_id:
        raise Http404

    context = {
        'cabinet': request.user.userprofile,
    }

    return render(request, 'cabinet/cabinet.html', context)
