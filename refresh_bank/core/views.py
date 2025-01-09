from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from bank_info.models import Bank

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['bankrupt'] = Bank.objects.first().status
        return context
