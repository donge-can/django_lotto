

# DB - SQL 느낌
# SQL을 직접 작성하는 것 보다 훨씬 쉽게 DB 다룰 수 있음.
# ORM Object-Relational Mapping 을 활용한다고 함


# Create your models here.

from django.db import models
from django.utils import timezone
import random


class GuessNumbers(models.Model):
    name = models.CharField(max_length = 24) # 로또 번호 리스트의 이름
    text = models.CharField(max_length = 255) # 로또 번호 리스트에 대한 설명
    lottos = models.CharField(max_length = 255, default = '[1,2,3,4,5,6]') # 로또 번호들이 담길 str
    num_lotto = models.IntegerField(default = 5) # 6 개 번호 set의 갯수

    update_date = models.DateTimeField()

    def generate(self): # 로또 번호를 자동으로 생성
        self.lottos = ""
        origin = list(range(1, 46)) # 1~46의 숫자 리스트

        for _ in range(0, self.num_lotto) :
            random.shuffle(origin)
            guess = origin[:6]
            guess.sort()
            self.lottos += str(guess) + '\n' # 로또 번호 str에 6개 번호 set 추가

        self.update_date = timezone.now()
        self.save()

    def __str__(self):
        return "pk {} : {} - {}".format(self.pk, self.name, self.text)
        # pk는 자동생성됨
