from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.views.generic import DetailView, ListView
from django.views import View
from .models import Hobby, Likes, Catalog
from .forms import CommentsForm, SearchForm
from cart.forms import CartAddProductForm
from haystack.query import SearchQuerySet


# Create your views here.
def product_detail(request, id, slug):
    product = get_object_or_404(Hobby,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'hobby/index-base.html', {'product': product,
                                                     'cart_product_form': cart_product_form})


class HobbyListView(ListView):
    template_name = 'hobby/hobby_glavnay.html'
    model = Hobby
    context_object_name = 'hobbys'


class One_Hobby(DetailView):
    template_name = 'hobby/one_hobby_dedali.html'
    model = Hobby
    # cart_product_form = CartAddProductForm()
    # context_object_name = 'hobbys'


class CatalogListView(ListView):
    template_name = 'hobby/index-catalog.html'
    model = Catalog
    context_object_name = 'catalogs'



class AddComments(View):
    '''Добавление комментария'''

    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_hobby_id = pk
            form.save()
            # return HttpResponseRedirect(f'/{pk}')
            return HttpResponseRedirect('/done')
        else:
            form = CommentsForm()
        return redirect(f'/{pk}')
        # return render(request, f'/{pk}')


def done(request):
    return render(request, 'hobby/index-done.html')


def o_nas(request):
    return render(request, 'hobby/index-o-has.html')


def get_client_ip(request):
    '''получение ip адреса клиента'''
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]  # берем оригинальный ип-адрес из списка который выгрузиться
    else:
        ip = request.META.get('REMOTE_ADDR')  # берем ип-адрес системы с которрой отправлен запрос клиента
    return ip


class AddLike(View):
    ''' добовляем лайк'''

    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            Likes.objects.get(ip=ip_client, pos_id=pk)
            return redirect(f'/glav/{pk}')
        except:
            new_like = Likes()
            new_like.ip = ip_client
            new_like.pos_id = int(pk)
            new_like.save()
            return redirect(f'/glav/{pk}')


class DelLike(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            lik = Likes.objects.get(ip=ip_client)
            lik.delete()
            return redirect(f'/glav/{pk}')
        except:
            return redirect(f'/glav/{pk}')


def test_modul(request):
    return render(request, 'hobby/index.html')


class Test_modul(ListView):
    template_name = 'hobby/index.html'
    model = Hobby
    context_object_name = 'hobbis'


'''рабочая'''


class Hobby_working_home(ListView):
    template_name = 'hobby/index-home.html'
    model = Hobby
    context_object_name = 'hobbys'


class Hobby_working_base(ListView):
    template_name = 'hobby/index-home.html'
    model = Hobby
    context_object_name = 'hobbys'


class Hobby_working_detali(DetailView):
    template_name = 'hobby/index-detali.html'
    model = Hobby

"""вывод деталей каталога"""

class CatalogListViewDetail(ListView):
    template_name = 'hobby/index-catalog-detail.html'
    model = Hobby
    context_object_name = 'hobbys'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['data'] = self.kwargs['data']
    #     return context
    def get_queryset(self):
        queryset = super().get_queryset()
        filter_qr = queryset.filter(catalog_new_id=1)
        return filter_qr


"""Регистрация"""

def registration(request):
    return render(request, 'hobby/index-registration.html')


"""для поисковой системы"""


def post_search(request):
    form = SearchForm()
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            cd = form.cleaned_data
            results = SearchQuerySet().models(Hobby).filter(content__contains=cd['query']).load_all()
            # count total results
            total_results = results.count()
            return render(request,
                  'hobby/post/search.html',
                  {'form': form,
                   'cd': cd,
                   'results': results,
                   'total_results': total_results   })
    return render(request,
                  'hobby/post/search.html',
                  {'form': form
                   })