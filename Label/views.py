from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

from django.shortcuts import render
from django.views.decorators import csrf


from .models import LabelAnnotation
from .models import Count

# Create your views here.

def disp(request):
    list = LabelAnnotation.objects.all()
    html = ''
    for var in list:
        html += '<p>{}, qid:{}, qcontent:{}, uid:{}, label = {}</p>'.format(var.id, var.qid, var.qcontent, var.uid, var.score)

    return HttpResponse(html)



def job(request):
    count_total = Count.objects.get(qid='total')
    list = LabelAnnotation.objects.all()
    for var in list:
        if not var.labeled:
            qid = var.qid
            count_query = Count.objects.get(qid=qid)
            # html = '<p>{}, qid:{}, qcontent:{}, uid:{}</p>'.format(var.id, var.qid, var.qcontent, var.uid)
            return render(request, 'label_job.html',
                          {
                              'qcontent': var.qcontent,
                              'doc_link': '/static/html/{}/{}.html'.format(qid, var.uid),
                              'doc_name': '{}.html'.format(var.uid),
                              'finish_total': str(count_total.processed),
                              'total': str(count_total.total),
                              'finish_query': str(count_query.processed),
                              'total_query': str(count_query.total),
                              'id': var.id
                          })


    html = 'All the query-document pairs have been annotated'
    return HttpResponse(html)


def job_process(request):
    list = Count.objects.all()
    html = ''
    for var in list:
        qid, processed, total = var.qid, var.processed, var.total
        if processed < total:
            html += '<p><font color="red">qid:{}, processing:{}/{}</font></p>'.format(qid, processed, total)
        else:
            html += '<p>qid:{}, processing:{}/{}</p>'.format(qid, processed, total)

    return HttpResponse(html)


def job_behind(request):
    request.encoding = 'utf-8'
    if 'label' in request.GET and 'id' in request.GET:
        label = int(request.GET['label'])
        id = int(request.GET['id'])
        print('received label: {} with id = {}'.format(label, id))
        if label in {-1, 0, 1, 2, 3}:
            label_record = LabelAnnotation.objects.get(id=id)
            qid = label_record.qid
            count_record = Count.objects.get(qid=qid)
            count_total = Count.objects.get(qid='total')
            if not label_record.labeled:
                label_record.score = label
                label_record.labeled = True
                label_record.save()

                count_record.processed += 1
                count_record.save()

                count_total.processed += 1
                count_total.save()


    return HttpResponseRedirect('/label/job')