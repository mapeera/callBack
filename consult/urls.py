from django.urls import path
from . import views


app_name = 'consult'


urlpatterns = [
    path('create-consult',views.ConsultView.as_view(), name='create-consult'),
    path('create-book',views.BookingView.as_view(), name='create-book'),
    path('create-trans',views.CreateTrans.as_view(), name='create-trans')
]