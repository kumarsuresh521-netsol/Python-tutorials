from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from .models import Store

class IndexView(generic.ListView):
    template_name = 'mystore/index.html'
    context_object_name = 'store_list'
    
    def get_queryset(self):
        return Store.objects.order_by('id')[:5]

class DetailView(generic.DetailView):
    model = Store
    template_name = 'mystore/detail.html'
    context_object_name = 'store_detail'
    
# def index(request):
#     store_list = Store.objects.order_by('store_name')
#     context = {'store_list':store_list}
#     return render(request, 'mystore/index.html', context)
# 
# def detail(request, store_id):
#     store_detail = get_object_or_404(Store, pk=store_id)
#     return render(request, 'mystore/detail.html', {'store_detail': store_detail})