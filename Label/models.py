from django.db import models

# Create your models here.
class Count(models.Model):
    qid = models.CharField(max_length=20, primary_key=True) # 还包括total
    processed = models.IntegerField(default=0) # 已完成标注个数
    total = models.IntegerField(default=0) #总的需标注个数

class LabelAnnotation(models.Model):
    qid = models.CharField(max_length=20)
    qcontent = models.CharField(max_length=50)
    uid = models.CharField(max_length=20)
    score = models.IntegerField(default=-2) # 0，1，2，3四级标注，-1表示乱码
    labeled = models.BooleanField(default=False) # 是否已经被标注过了

