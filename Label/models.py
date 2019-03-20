from django.db import models

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=20)

class LabelAnnotation(models.Model):
    qid = models.CharField(max_length=20)
    qcontent = models.CharField(max_length=50)
    uid = models.CharField(max_length=20)
    score = models.IntegerField(default=-2) # 0，1，2，3四级标注，-1表示乱码
    labeled = models.BooleanField(default=False) # 是否已经被标注过了
