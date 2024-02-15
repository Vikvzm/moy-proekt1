from django.db import models
from django.urls import reverse


# Create your models here.
class Catalog(models.Model):
    name_group = models.CharField('Вид группы', max_length=60)
    compound = models.CharField('Состав', max_length=100)
    img = models.ImageField('Изображение', upload_to='my_gallery/%Y')  # %Y папка по году

    def __str__(self):
        return self.name_group

    def get_url_catalog_hobby(self):
        return reverse('hobby_catalog', args=[self.id])

    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = "Каталоги"


class Hobby(models.Model):
    '''Данные'''
    # id = models.IntegerField('id')
    name = models.CharField('Название', max_length=100)
    catalog = models.CharField('Каталог', max_length=60)
    description = models.TextField('Описание', default='разные')
    price = models.IntegerField('Цена')
    date = models.DateField('Дата размещения')
    img = models.ImageField('Изображение', upload_to='my_gallery/%Y')  # %Y папка по году
    catalog_new = models.ForeignKey(Catalog, on_delete=models.CASCADE, null=True, related_name='hobby')
    catalog_top = models.ManyToManyField(Catalog, related_name='hobbys')

    def __str__(self):
        return f'{self.name}, {self.price}'

    def get_url_hobby(self):
        return reverse('one_hobby_detali', args=[self.id])

    def get_url_working_hobby(self):
        return reverse('hobby_working_detali', args=[self.id])

    class Meta:
        verbose_name = 'Композицию'
        verbose_name_plural = "Композиции"


class Comments(models.Model):
    ''' Коментарий'''
    email = models.EmailField()
    name = models.CharField('Имя', max_length=50)
    text_comments = models.TextField('Текст коментария', max_length=2000)
    post_hobby = models.ForeignKey(Hobby, verbose_name='Публикация', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.post_hobby}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = "Комментарии"


class Likes(models.Model):
    '''лайки'''
    ip = models.CharField(max_length=100)
    pos = models.ForeignKey(Hobby, verbose_name='Публикация', on_delete=models.CASCADE)
