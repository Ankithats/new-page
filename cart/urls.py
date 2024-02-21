from django.urls import path
from . import views
app_name='cart'
urlpatterns = [
    path('addcart/<int:id>',views.addcart,name='addcart'),
    path(' displaycart/',views.displaycart,name='displaycart'),
    path('remove/<int:id>',views.remove,name='remove'),
    path('reduce/<int:id>',views.reduce,name='reduce'),
    path('placeorder/<int:id>',views.placeorder,name='placeorder'),
    

   
]