from django.shortcuts import render
from .models import ListShop
from django.core.paginator import Paginator


def list_for_shop(request):
    list_shop = ListShop.objects.all()
    paginator = Paginator(list_shop, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'list_for_shop/list_for_shop.html', {'list_shop': page_obj})


def cart(request):
    list_shop = ListShop.objects.all()
    return render(request, 'list_for_shop/cart.html', {'list_shop': list_shop})


def check_out(request):
    return render(request, 'list_for_shop/check_out.html', {})


def detail_shop(request, pk):
    list_shop = ListShop.objects.get(id=pk)
    list_shop_loop = ListShop.objects.all()[:4]
    return render(request, 'list_for_shop/detail_shop.html', {'list_shop': list_shop, 'list_shop_loop': list_shop_loop})


def search_area(request):
    q = request.GET.get('q')
    list_shop = ListShop.objects.filter(title__icontains=q)
    paginator = Paginator(list_shop, 1)
    page_number = request.GET.get('page')
    obj_page = paginator.get_page(page_number)
    return render(request, 'list_for_shop/list_for_shop.html', {'list_shop': obj_page})
