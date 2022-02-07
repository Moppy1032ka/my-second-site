import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
# 検索に使うdatabaseみたいなの
class SampleDB(models.Model):
    class Meta:
        db_table = 'sample_table' # DB内で使用するテーブルの名前
        verbose_name_plural = 'sample_table' # Admin(管理)サイトで表示するテーブルの名前
    # 文字をいれる場所1
    sample1 = models.CharField('sample1', max_length=255, null=True, blank=True)
    # 文字を入れる場所2
    sample2 = models.CharField('sample2', max_length=255, null=True, blank=True)

# 質問箱
class Question(models.Model):
    question_text = models.CharField(max_length=250)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

# 選択
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  
    choice_text = models.CharField(max_length=250)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

# ファイルのアップロード
class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents')
    uploaded_at = models.DateTimeField('upload date', default=timezone.now)
    def __str__(self):
        return self.description
