from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import ListView

from Balancing.models import BalancingProduct, BalancingProductImage


class BalancingPageView(ListView):
    model = BalancingProduct
    template_name = "products-balancing.html"
    context_object_name = 'products'

    def detail_view(request, id):
        post = get_object_or_404(BalancingProduct, id=id)
        photos = BalancingProductImage.objects.filter(post=post)
        return render(request, 'product-balancing.html', {
            'post': post,
            'photos': photos
        })