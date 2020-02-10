from django.db import models

class Fcuser(models.Model):
    username = models.CharField(max_length=64,
                                verbose_name='username')
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