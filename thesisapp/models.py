import datetime

from django.db import models
from django.db.models import F, Sum, Count
# Create your models here.

class Thesis(models.Model):
    title_th = models.CharField(max_length=255, default="")
    title_eng = models.CharField(max_length=255, default="")
    type = models.CharField(max_length=50, default="")
    institute = models.CharField(max_length=125, default="")
    major = models.CharField(max_length=50, default="")
    year = models.IntegerField(default=0)
    callnumber = models.CharField(max_length=50, default="")
    pages = models.IntegerField(default=1)
    abstract = models.TextField(default="")
    file = models.FileField(upload_to='static/pdf/', default="")

    # def __str__(self):
    #     return Author.getAuthorList(self.id) + "(" + self.year + ")" + self.title_th
    def __str__(self):
        return self.title_th + " ("+self.title_eng+") " + self.type + " " + self.year
    def getCountAdvise(self):
        count = Advisor.objects.filter(thisis=self).aggregate(count=Count('id'))
        return count['count']
    def getCountAuthor(self):
        count = Advisor.objects.filter(thisis=self).aggregate(count=Count('id'))
        return count['count']

class Author(models.Model):
    thesis = models.ForeignKey(Thesis, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default="")
    surname = models.CharField(max_length=50, default="")
    number = models.IntegerField(default=1)
    def __str__(self):
        return self.name + "  " + self.surname
    def getAuthorList(self, id):
        return Advisor.objects.filter(id=id).order_by(self.number)

class Advisor(models.Model):
    thesis = models.ForeignKey(Thesis, on_delete=models.CASCADE)
    title = models.CharField(max_length=35, default="อาจารย์")
    name = models.CharField(max_length=50, default="")
    surname = models.CharField(max_length=50, default="")
    status = models.CharField(max_length=35, default="ที่ปรึกษาหลัก")
    def __str__(self):
        return self.title + self.name + "  " + self.surname + " " + self.thesis.title_th

class Keyword(models.Model):
    thesis = models.ForeignKey(Thesis, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=35, default="")
    def __str__(self):
        return self.keyword

