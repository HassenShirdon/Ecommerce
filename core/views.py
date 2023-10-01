from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
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


@login_required
def cart(request):
    if request.user.is_authenticated:
        user_cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = user_cart.cart_items.all()
        total_price = sum(item.item.price *
                          item.quantity for item in cart_items)

        context = {
            'cart_items': cart_items,
            'total_price': total_price,
            'empty_cart': not bool(cart_items),  # Check if cart is empty
        }

        return render(request, 'core/cart.html', context)
    else:
        # Handle case when user is not authenticated (optional)
        return render(request, 'core/cart.html', {'empty_cart': True})


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


def add_to_cart(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    user_cart, created = Cart.objects.get_or_create(user=request.user)

    # Try to get an existing cart item for the given item
    cart_item, created = CartItem.objects.get_or_create(
        cart=user_cart, item=item)

    if not created:
        # If the cart item already exists, increase its quantity by 1
        cart_item.quantity += 1
        cart_item.save()
    else:
        # If it's a new cart item, set the quantity to 1
        cart_item.quantity = 1
        cart_item.save()

    return JsonResponse({'success': True})
# View for the cart


def checkout(request):
    user_cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=user_cart)
    total_price = sum(item.item.price * item.quantity for item in cart_items)

    return render(request, 'core/checkout.html', {'cart_items': cart_items, 'total_price': total_price})
