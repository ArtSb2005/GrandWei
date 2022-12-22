from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView

from Balancing.models import BalancingProduct
from main.models import IndexProduct, IndexProductImage


class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['BalancingProduct'] = BalancingProduct.objects.all().order_by('-id')[:5]
        context['IndexProduct'] = IndexProduct.objects.all().order_by('-id')[:5]
        return context

class KnRostPageView(ListView):
    model = IndexProduct
    template_name = "products.html"
    context_object_name = 'products'

    def detail_view(request, id):
        post = get_object_or_404(IndexProduct, id=id)
        photos = IndexProductImage.objects.filter(post=post)
        return render(request, 'product.html', {
            'post': post,
            'photos': photos
        })


