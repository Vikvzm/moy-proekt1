from django.db import models
from hobby.models import Hobby


class Order(models.Model):
    first_name = models.CharField("Имя", max_length=50)
    last_name = models.CharField("Фамилия", max_length=50)
    email = models.EmailField("Почтовый ящик")
    address = models.CharField("Адрес", max_length=250)
    postal_code = models.CharField("Индекс", max_length=20)
    city = models.CharField("Город",  max_length=100)
    created = models.DateTimeField("Заказ создан", auto_now_add=True)
    updated = models.DateTimeField("Обновлено",auto_now=True)
    paid = models.BooleanField("Оплачено",default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE , related_name='items')
    product = models.ForeignKey(Hobby, on_delete=models.CASCADE , related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity