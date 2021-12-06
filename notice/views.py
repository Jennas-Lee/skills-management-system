from django.shortcuts import render, HttpResponse
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

        notice = Notice(title=title, contents=contents, user=request.user)

        try:
            print(contents)

            notice.save()

            return HttpResponse("""
                <script>
                    alert('공지사항 작성이 완료되었습니다.');
                    location.href = '/';
                </script>
            """)

        except:
            return HttpResponse("""
                <script>
                    alert('오류가 발생했습니다. 이 오류가 지속되면 개발자에게 연락주세요.');
                    window.history.back();
                </script>
            """)


def viewer_notice(request, id):
    notice = Notice.objects.filter(pk=id).last()

    return render(request, 'viewer.html', {'notice': notice})
