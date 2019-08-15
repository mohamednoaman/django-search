from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Medicine
from django.db.models import Q


class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = Medicine
    template_name = 'search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Medicine.objects.filter(
            Q(title__icontains=query) | Q(price__icontains=query)
        )
        return object_list
    

    '''
    def get_queryset(self): # new
        return City.objects.filter(name__icontains='Boston')


    queryset = Medicine.objects.filter(title__icontains='Panadol')
    '''