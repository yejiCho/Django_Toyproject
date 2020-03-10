from django.db import models

# Create your models here.

class Order(models.Model):
    # 어떤 앱 안에 있는 class 설정
    # on_delete : 연결된 사용자가 삭제 됐을때, order를어떻게 관리할건지
    fcuser = models.ForeignKey('fcuser.Fcuser',on_delete=models.CASCADE,verbose_name='사용자')
    product = models.ForeignKey('product.Product',on_delete=models.CASCADE,verbose_name='상품')
    quantity = models.IntegerField(verbose_name='수량')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='등록일')

    def __str__(self):
        return str(self.fcuser) + ' ' + str(self.product)

    class Meta:
        db_table = 'fc_order'
        verbose_name = '주문'
        verbose_name_plural = '주문' # 복수