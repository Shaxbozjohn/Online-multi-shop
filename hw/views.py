from django.shortcuts import render, get_object_or_404
from  .models import ProductsCategory , Products

def homepage(request):

    return render(request,template_name="index.html")



def products_page(request):
    categorys = ProductsCategory.objects.all()
    a = Products.objects.filter(caregory__name="New Products")
    context = {
        'categorys': categorys,
        'product': Products.objects.all()
    }
    return render(
        request=request,
        template_name="products.html",
        context=context)
def login_page(request):
    return render(
        request=request,
        template_name="login.html")

def profile_page(request):
    return render(
        request=request,
        template_name="profile.html")

def order_create_page(request):
    return render(
        request=request,
        template_name="order-create.html")

def products_by_category(request, category_id):
    category = get_object_or_404(ProductsCategory, pk=category_id)
    products = Products.objects.filter(caregory=category)

    return render(
        request=request,
        template_name="products_by_category.html",
        context={'category': category, "products": products}
    )