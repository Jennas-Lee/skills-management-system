from django.shortcuts import render
from django.core.paginator import Paginator

from notice.models import Notice


def list_notice(request):
    notice = Notice.objects.all().order_by('pk')
    paginator = Paginator(notice, 15)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    previous = page_obj.previous_page_number if page_obj.has_previous() else 1
    next = page_obj.next_page_number if page_obj.has_next() else page_obj.paginator.num_pages

    return render(request, 'list.html', {'page_obj': page_obj, 'previous': previous, 'next': next})


def create_notice(request):
    if request.method == 'GET':
        return render(request, 'create.html')

    elif request.method == 'POST':
        title = request.POST.get('title')
        contents = request.POST.get('contents')
        attachements = request.POST.get('attachments')
