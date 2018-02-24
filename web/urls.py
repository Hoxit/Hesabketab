
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^submit/expense/$', views.submit_expense, name='Submit_expense'),
    url(r'^submit/income/$', views.submit_income, name='Submit_income'),
    url(r'^accounts/register/$', views.register, name='Register')

]