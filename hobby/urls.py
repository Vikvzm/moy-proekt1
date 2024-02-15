from django.urls import path, include, re_path
from . import views
from .views import HobbyListView, One_Hobby,AddComments, done, test_modul, Test_modul, o_nas, CatalogListView

urlpatterns = [

    re_path(r'^search/$', views.post_search, name='post_search'),
    path('', HobbyListView.as_view(), name='hobby_list_glavnay'),
    path('catalog', CatalogListView.as_view(), name='hobby_catalog'),
    path('catalog/detail', views.CatalogListViewDetail.as_view(), name='hobby_catalog_detail'),
    path('<int:pk>', One_Hobby.as_view(), name='one_hobby_detali'),
    path('review/<int:pk>', AddComments.as_view(), name='add_comments'),
    path('done', done, name='done_add_comments'),
    path('o_nas', o_nas, name='o_nas_info'),
    path('<int:pk>/add_likes', views.AddLike.as_view(), name='add_likes'),
    path('<int:pk>/del_likes', views.DelLike.as_view(), name='del_likes'),
    # path('test', test_modul, name='test_modul'),
    path('test', Test_modul.as_view(), name='test_modul'),
    path('glav/<int:pk>/add_likes', views.AddLike.as_view(), name='add_likes'),
    path('glav/<int:pk>/del_likes', views.DelLike.as_view(), name='del_likes'),
    path('glav', views.Hobby_working_home.as_view(), name='hobby_working_home'),
    path('glav/<int:pk>', views.Hobby_working_detali.as_view(), name='hobby_working_detali'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registration', views.registration, name='user-registration'),




    ]