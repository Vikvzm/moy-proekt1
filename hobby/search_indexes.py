from haystack import indexes
from .models import Hobby

class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    # name = indexes.CharField(model_attr='name')
    # name = indexes.CharField(document=True, use_template=True)
    # description = indexes.CharField(model_attr='description')

    # id = indexes.IntegerField(model_attr='id')
    name = indexes.CharField(model_attr='name')
    catalog = indexes.CharField(model_attr='catalog')
    description = indexes.CharField(model_attr='description')
    price = indexes.IntegerField(model_attr='price')
    date = indexes.DateField(model_attr='date')
    catalogs = indexes.CharField(model_attr="catalog")


    def get_model(self):
        return Hobby

    def index_queryset(self, using=None):
        # return self.get_model().objects.all()
        return self.get_model().objects.all()
