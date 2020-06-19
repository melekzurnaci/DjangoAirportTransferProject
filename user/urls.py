from django.urls import path

from . import views

urlpatterns = [
    # ex: /home/
    path('', views.index, name='index'),
    path('update/', views.user_update, name='user_update'),
    path('password/', views.change_password, name='change_password'),
    path('transfers/', views.transfers, name='transfers'),
    path('transferdetail/<int:id>', views.transferdetail, name='transferdetail'),
    path('comments/', views.comments, name='comments'),
    path('deletecomment/<int:id>', views.deletecomment , name='deletecomment'),
    #  path('addcomment/<int:id>', views.addcomment, name='addcomment'),

    # ex: /polls/5/
    #path('<int:question_id>/', views.detail, name='detail'),

]