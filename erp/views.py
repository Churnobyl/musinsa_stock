from django.shortcuts import render, redirect
from .models import Stuff, Inventory, History
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from accounts.models import UserModel


def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect('/erp')
    else:
        return redirect('/sign-in')


def erp(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            all_stuff = Stuff.objects.select_related('inventory').order_by('-created_at')
            return render(request, 'erp/home.html', {'all_stuff': all_stuff})
        else:
            return redirect('/sign-in')
    elif request.method == 'POST':
        pass


@login_required
def detailed_erp(request, id):
    stuff_data = Stuff.objects.select_related('inventory').get(goods=id)
    submit_user = UserModel.objects.get(id=stuff_data.user_id_id)
    history_data = History.objects.filter(goods_id=id).order_by('-history_time')
    # a = Inbound.objects.all()
    # b = Outbound.objects.all()
    # print(a | b)

    return render(request, 'erp/erp_detail.html', {'erp_detail': stuff_data, 'username': submit_user.username, 'history_data': history_data})


@login_required
def erp_goods_new(request):
    user = request.user.is_authenticated
    if user:
        if request.method == 'GET':
            return render(request, 'erp/erp_goods_new.html')
        elif request.method == 'POST':
            goods_name = request.POST.get('goods_name', '')
            goods_category = request.POST.get('goods_category', '')
            goods_color = request.POST.get('goods_color', '')
            goods_size = request.POST.get('goods_size', '')
            image = request.POST.get('goods_image', '')
            stock = int(request.POST.get('stock', ''))
            author = request.user.id

            if goods_name == ''\
                or goods_category == ''\
                or goods_color == ''\
                or goods_size == ''\
                or image == ''\
                    or stock == '':
                return render(request, 'erp/erp_goods_new.html', {'error': "필수 입력 사항입니다."})

            exist_item = Stuff.objects.filter(goods_name=goods_name, goods_color=goods_color, goods_size=goods_size)
            if exist_item:
                return render(request, 'erp/erp_goods_new.html', {'error': "이미 있는 상품입니다."})
            else:
                new_one = Stuff.objects.create(goods_name=goods_name, goods_category=goods_category, goods_color=goods_color, goods_size=goods_size, image=image, user_id_id=author)
                Inventory.objects.create(inventory_id=new_one.goods, stock=stock)
                History.objects.create(goods_id=new_one.goods, count=stock, in_out='N')
                return redirect('/erp')
    else:
        return render(request, 'accounts/signin.html')

@login_required
def erp_goods_stock(request, goods_id):
    user = request.user.is_authenticated
    stuff_data = Stuff.objects.get(goods=goods_id)
    submit_user = UserModel.objects.get(id=stuff_data.user_id_id)
    history_data = History.objects.filter(goods_id=goods_id).order_by('-history_time')
    if user:
        if request.method == 'GET':

            return render(request, 'erp/erp_stock_new.html', {'erp_detail': stuff_data, 'username': submit_user.username})
        elif request.method == 'POST':
            checking = request.POST.get('check_bound', '')
            stock = int(request.POST.get('stock', ''))

            inventory_query = Inventory.objects.filter(inventory_id=goods_id)

            if checking == 'I':  # 입고
                History.objects.create(goods_id=goods_id, count=stock, in_out=checking)
                add_stock = inventory_query.values('stock')[0]['stock'] + stock
                inventory_query.update(stock=add_stock)
            elif checking == 'O':  # 출고
                if stock > inventory_query.values_list('stock')[0][0]:
                    return render(request, 'erp/erp_stock_new.html',
                                  {'erp_detail': stuff_data, 'username': submit_user.username,
                                   'history_data': history_data,
                                   'error': "재고가 부족합니다."})

                History.objects.create(goods_id=goods_id, count=stock, in_out=checking)
                sub_stock = inventory_query.values('stock')[0]['stock'] - stock
                inventory_query.update(stock=sub_stock)
            return render(request, 'erp/erp_detail.html', {'erp_detail': stuff_data, 'username': submit_user.username, 'history_data': history_data})
    else:
        return render(request, 'accounts/signin.html')
