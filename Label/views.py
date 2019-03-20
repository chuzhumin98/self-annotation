from django.http import HttpResponse
from django.shortcuts import render_to_response

from django.shortcuts import render
from django.views.decorators import csrf


from .models import LabelAnnotation

# Create your views here.

def disp(request):
    list = LabelAnnotation.objects.all()
    html = ''
    for var in list:
        html += '<p>{}, qid:{}, qcontent:{}, uid:{}<p>'.format(var.id, var.qid, var.qcontent, var.uid)

    return HttpResponse(html)


def job(request):
    list = LabelAnnotation.objects.all()
    for var in list:
        if not var.labeled:
            html = '<p>{}, qid:{}, qcontent:{}, uid:{}<p>'.format(var.id, var.qid, var.qcontent, var.uid)
            return render(request, 'label_job.html',
                          {
                              'qcontent': var.qcontent,
                              'doc_link': '/static/html/{}/{}.html'.format(var.qid, var.uid),
                              'doc_name': '{}.html'.format(var.uid)
                          })
        else:
            html = 'All the query-document pairs have been annotated'
            return HttpResponse(html)


def job_process(request):
    list = LabelAnnotation.objects.all()
    total_num = len(list)
    cnt_labeled = 0
    html = ''
    for var in list:
        if var.labeled:
            cnt_labeled += 1
    html += 'the labeled process is {}/{}'.format(cnt_labeled, total_num)
    return HttpResponse(html)