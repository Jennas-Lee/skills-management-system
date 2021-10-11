from django.shortcuts import render
from django.core.paginator import Paginator

from notice.models import Notice


def list_notice(request):
    notice = Notice.objects.all()
    paginator = Paginator(notice, 20)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'notice/list.html', {'page_obj': page_obj})


def create_notice(request):
    if request.method == 'GET':
        return render(request, 'notice/create.html')
    # elif request.method == 'POST':
    #
