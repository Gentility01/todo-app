from django.urls import path
from . import views

urlpatterns = [
   path('', views.homeview, name='home'),
   path('new/', views.addTodoView, name='addview'),
   path('complete/<todo_id>', views.complete_todo, name= 'complete'),
   path('deletecomplete', views.deleteCompleted, name='deletecompleted'),
   path('deleteall', views.deleteAll, name='deletedall')
    
]
