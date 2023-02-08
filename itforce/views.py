from django.db.models.deletion import ProtectedError
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render,reverse
from .models import Order, Customer, ProductBrand, ProductCategory, OrderStatus, Service


def index(request):
    order = Order.objects.order_by('-created_at')
    return render(request, 'blog/index.html', {'order':order})

def create_order(request):
    if request.method == 'POST':
        order = Order()
        order.customer = Customer.objects.get(id = request.POST.get('customer'))
        order.service = Service.objects.get(id = request.POST.get('service'))
        order.product_brand = ProductBrand.objects.get(id = request.POST.get('product_brand'))
        order.product_category = ProductCategory.objects.get(id = request.POST.get('product_category'))
        order.status = OrderStatus.objects.get(id = request.POST.get('status'))
        order.serial_number = request.POST.get('serial_number')
        order.price = request.POST.get('price')
        order.additional_info = request.POST.get('additional_info')
        order.save()
        context = {
            'id': order.id,
            'customer':order.customer,
            'service':order.service,
            'product_category':order.product_category,
            'product_brand':order.product_brand,
            'serial_number':order.serial_number,
            'price':order.price,
            'additional_info':order.additional_info,
            'status':order.status          
        }
    return redirect('index')

def customers(request):
    customers=Customer.objects.order_by('-date')
    return render(request,'blog/customer.html',{'customers':customers})

def product_category(request):
    products_categories=ProductCategory.objects.order_by('date')
    return render(request,'blog/category.html',{'products_categories':products_categories})

def order_status(request):
    order_status=OrderStatus.objects.order_by('-date')
    return render(request,'blog/order_status.html', {'order_status':order_status})

def services(request):
    services=Service.objects.order_by('-date')
    return render(request,'blog/service.html',{'services':services})

def create_customer(request):
    if request.method=='POST':
        customer=Customer()
        customer.name=request.POST.get('name')
        customer.phone=request.POST.get('phone')
        customer.save()
    return redirect(reverse('customer'))

def edit_customer(request,id):
    customer=object.get(id=id)
    if request.method=='POST':
        customer.name=request.POST.get('name')
        customer.phone=request.POST.get('phone')
        customer.save()
    return redirect(reverse('customer'))


def delete_customer(request, id):
    customer=object.get(id=id)
    if request=='POST':
        try:
            customer.delete()
            return redirect(reverse('customer'))
        except ProtectedError:
            return HttpResponse('Извините новы не можете удалить пользователя.Он используется в заказе')
    return render(request,'blog/delete_customer.html',{'customer':customer})

def create_order_status(request):
    if request.method=='POST':
        order_status=OrderStatus()
        order_status.time=request.POST.get('time')
        order_status.save()
    return redirect(reverse('order_status'))

def create_service(request):
    if request.method=='POST':
        service=Service()
        service.title=request.POST.get('title')
        service.description=request.POST.get('description')
        service.save()
    return redirect(reverse('service'))

def create_product_category(request):
    if request.method=='POST':
        product_category=ProductCategory()
        product_category.title=request.POST.get('time')
        product_category.save()
    return redirect(reverse('product_category'))

def create_product_brand(request):
    if request.method=='POST':
        product_brand=ProductBrand()
        product_brand.title=request.POST.get('title')
        product_brand.save()
    return redirect(reverse('product_brand'))

def delete_status(request, id):
    order_status=OrderStatus.objects.get(id=id)
    if request.method=='POST':
        try:
            order_status.delete()
            return redirect(reverse('order_status'))
        except ProtectedError:
            return HttpResponse('Извините н овы не можете удалить пользователя.Он используется в заказе')
    return render(request,'blog/delete_order_status.html',{'order_status':order_status})

def delete_category(request, id):
    product_category=ProductCategory.objects.get(id=id)
    if request.method=='POST':
        try:
            product_category.delete()
            return redirect(reverse('product_category'))
        except ProtectedError:
            return HttpResponse('Извините н овы не можете удалить пользователя.Он используется в заказе')
    return render(request,'blog/delete_category.html',{'product_category':product_category})

def delete_service(request, id):
    service=Service.objects.get(id=id)
    if request.method=='POST':
        try:
            service.delete()
            return redirect(reverse('service'))
        except ProtectedError:
            return HttpResponse('Извините н овы не можете удалить пользователя.Он используется в заказе')
    return render(request,'blog/delete_service.html',{'service':service})

def delete_product_brand(request, id):
    product_brand=ProductBrand.objects.get(id=id)
    if request.method=='POST':
        try:
            product_brand.delete()
            return redirect(reverse('product_brand'))
        except ProtectedError:
            return HttpResponse('Извините н овы не можете удалить пользователя.Он используется в заказе')
    return render(request,'blog/delete_product_brand.html',{'product_brand':product_brand})

    
def delete_order(request, id):
    order=Order.objects.get(id=id)
    if request.method=='POST':
        try:
            order.delete()
            return redirect(reverse('index'))
        except ProtectedError:
            return HttpResponse('Извините н овы не можете удалить пользователя.Он используется в заказе')
    return render(request,'blog/delete_order.html',{'order':order})

def delete_customer(request, id):
    customer=Customer.objects.get(id=id)
    if request.method=='POST':
        try:
            customer.delete()
            return redirect(reverse('customer'))
        except ProtectedError:
            return HttpResponse('Извините н овы не можете удалить пользователя.Он используется в заказе')
    return render(request,'blog/delete_customer.html',{'delete_customer':delete_customer})

def show(request,id):
    order=Order.objects.get(id=id)
    context={'order':order}
    return render(request,'blog/show.html',context)

def show_category(request,id):
    category=ProductCategory.objects.get(id=id)
    context={'category':category}
    return render(request,'blog/show_category.html',context)

def show_customer(request,id):
    customer=Customer.objects.get(id=id)
    context={'customer':customer}
    return render(request,'blog/show_customer.html',context)

def show_order_status(request,id):
    order_status=OrderStatus.objects.get(id=id)
    context={'order_status':order_status}
    return render(request,'blog/show_order_status.html',context)

def show_service(request,id):
    service=Service.objects.get(id=id)
    context={'service':service}
    return render(request,'blog/show_service.html',context)

















