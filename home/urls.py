from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name="index"),
    # path('home1/', views.home1, name="home1"),
    path('add', views.add, name="add"),
    path('edit/<int:Id>', views.edit, name="edit"),
    path('do_update_record/<int:Id>',
         views.do_update_record, name='do_update_record'),
    path('delete/<int:Id>', views.delete, name="delete"),
    path('viewData/<int:Id>', views.viewData, name="viewData"),

]
