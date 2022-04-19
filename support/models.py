from multiprocessing.connection import answer_challenge
from turtle import update
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Faq(models.Model):
    class Category(models.TextChoices):
        account = 'AC', ('Account')
        normal = 'NO', ('Normal')
        etc = 'ET', ('Etc')
    qusetion = models.TextField(verbose_name='질문')
    categroy = models.CharField(
        verbose_name='카테고리',
        max_length=2,
        choices=Category.choices,
        default=Category.normal,
    )
    answer = models.TextField(verbose_name='답변')
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='생성일시', auto_now_add=True)
    modifier = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True,related_name='+')
    update_at = models.DateTimeField(verbose_name='최종수정일', auto_now=True)