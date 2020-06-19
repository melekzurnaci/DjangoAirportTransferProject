from django.urls import path

from . import views

urlpatterns = [
    # ex: /home/
    path('', views.index, name='index'),

    # path('deletefromcart/<int:id>', views.deletefromcart, name='deletefromcart'),
    path('transfercar/<int:id>', views.transfercar, name='transfercar'),
    path('transferform/<int:id>', views.transferform, name='transferform'),
    path('transfercompleted/<int:id>', views.transfercompleted, name='transfercompleted'),
    path('transfercarCancel/<int:id>', views.transfercarCancel, name='transfercarCancel'),
]
