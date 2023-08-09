from django.shortcuts import render, get_object_or_404
from .models import Category, Item,  Cart, CartItem, Order, OrderItem
from django.views import generic

# View for listing all categories


def category(request):
    return {
        'categories': Category.objects.all()
    }


# View for displaying details of a category


# View for listing all items


def home(request):
    items = Item.objects.all()
    return render(request, 'core/index.html', {'items': items})


def shop(request):
    items = Item.objects.all()
    orders = Order.objects.all()
    return render(request, 'core/shop.html', {'items': items, 'orders': orders, })


def about_us(request):
    return render(request, 'core/about.html')


class itemDetailView(generic.DetailView):
    model = Item
    template_name = 'core/item_detail.html'

# View for displaying user profile


def cart_detail(request, cart_id):
    cart = get_object_or_404(Cart, id=cart_id)
    return render(request, 'core/cart_detail.html', {'cart': cart})

# View for listing all orders


def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})

# View for displaying details of an order


def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order_detail.html', {'order': order})


def contact(request):
    return render(request, 'core/contact.html')


def checkout(request):
    return render(request, 'core/cart.html')


def t_shirts_view(request):
    t_shirts = Item.objects.filter(category='T-Shirts')
    return render(request, 't_shirts.html', {'items': t_shirts})


def category_list(request, category_slug=None):
    categories = Category.objects.all()
    category = None
    items = Item.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        items = items.filter(category=category)

    return render(request, 'core/shop.html', {'category': category, 'items': items, 'categories': categories})


def search_results(request):
    results = request.GET.get('query')
    if results:
        results = Item.objects.filter(name__icontains=results)
    else:
        results = []

    return render(request, 'core/search_result.html', {'results': results})
