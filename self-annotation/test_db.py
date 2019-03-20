from django.http import HttpResponse
from django.shortcuts import render_to_response

from django.shortcuts import render
from django.views.decorators import csrf

from Label.models import LabelAnnotation



def testdb(request):
    test1 = LabelAnnotation(qid='0001', uid='00001', qcontent='清华大学')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")

def disp(request):
    list = LabelAnnotation.objects.all()
    html = ''
    for var in list:
        html += '<p>{}, qid:{}, qcontent:{}, uid:{}<p>'.format(var.id, var.qid, var.qcontent, var.uid)

    return HttpResponse(html)


def search_form(request):
    return render_to_response('search_form.html')


def search(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET:
        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)


def search_post(request):
    ctx ={}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)