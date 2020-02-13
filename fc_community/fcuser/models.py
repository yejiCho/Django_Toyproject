from django.db import models

class Fcuser(models.Model):
    # [Django] class has no objects member error
    # https://ssungkang.tistory.com/entry/Django-class-has-no-objects-member-%EC%97%90%EB%9F%AC
    objects = models.Manager()
    username = models.CharField(max_length=64,
                                verbose_name='username')
    useremail = models.EmailField(max_length=128,
                                verbose_name='useremail')
    password = models.CharField(max_length=64,
                                verbose_name='password')
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                verbose_name='datetime')

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'fastcampus_fcuser'
        verbose_name = 'fastcampus_user'
        verbose_name_plural = 'fastcampus_user'