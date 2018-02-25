from django.urls import path, re_path

from . import views

urlpatterns = [ 
	path('', views.index, name='index'),
	path('add', views.addTodo, name='add'),
	path('complete/<todo_id>', views.completeTodo, name='complete'),
	path('uncomplete/<todo_id>', views.uncompleteTodo, name='uncomplete'),
    path('deletecomplete', views.deleteCompleted, name='deletecomplete'),
    path('deleteall', views.deleteAll, name='deleteall')
   # re_path(r'^details/(?P<id>\w{0,50})/$', views.details),
    #re_path(r'^add', views.add, name='add')
]