from django.shortcuts import redirect, render

from django.http import HttpResponse

from lists.models import Item, List

""" def home_page(request):
    return HttpResponse('<html><title>To-Do lists</title></html>') """

def home_page(request):
    """ if request.method == 'POST':
        return HttpResponse(request.POST['item_text']) """

    """ item = Item()
    item.text = request.POST.get('item_text', '')
    item.save() """

    """ if request.method == 'POST':
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text)
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')
        return redirect('/lists/the-only-list-in-the-world/') """
    """ else:
        new_item_text = '' """

    """ return render(request, 'home.html', {
        # 'new_item_text': request.POST.get('item_text', '')
        'new_item_text': new_item_text
    }) """
    #items = Item.objects.all()
    # return render(request, 'home.html')
    #return render(request, 'home.html', {'items': items})
    return render(request, 'home.html')

def view_list(request,list_id):
    list_ = List.objects.get(id=list_id)
    #items = Item.objects.all()
    #items = Item.objects.filter(list=list_)
    # return render(request, 'home.html', {'items': items})
    #return render(request, 'list.html', {'items': items})
    return render(request, 'list.html', {'list': list_})

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    # return redirect('/lists/the-only-list-in-the-world/')
    return redirect(f'/lists/{list_.id}/')

def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')