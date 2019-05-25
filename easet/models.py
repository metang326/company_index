from django.db import models

class product(models.Model):
	name=models.CharField(max_length=64,verbose_name='备件名称')
	typeID=models.CharField(max_length=64,verbose_name='规格型号')
	num=models.IntegerField(verbose_name='数量')
	price=models.FloatField(verbose_name='单价')
	sumPrice=models.FloatField(verbose_name='总价')
	discount=models.CharField(max_length=32,null=True,blank=True,default=' ',verbose_name='折算')
	position=models.CharField(max_length=32,null=True,blank=True,default=' ',verbose_name='货位')
	code=models.CharField(max_length=32,null=True,blank=True,default=' ',verbose_name='编码')
	describe=models.TextField(null=True,blank=True,default=' ',verbose_name='说明')
	
	def __str__(self):
		return self.name


	'''  superuser tangmy easet880128'''