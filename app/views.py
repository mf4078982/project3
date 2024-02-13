from django.shortcuts import render,HttpResponseRedirect
from .models import MY_MO
from .forms import MY_FO

# Create your views here.
def add(request):
    m = MY_MO.objects.all()
    if request.method == 'POST':
        s = MY_FO(request.POST)
        if s.is_valid():
            s.save()
            s = MY_FO()
    else:
        s = MY_FO()   
    return render(request, 'add.html',{'forms':s,'nice':m})
def delete(request,id):
    m = MY_MO.objects.get(pk=id)
    if request.method == 'POST':
        m.delete()
    
    return HttpResponseRedirect('/')
def upd(request,id):
    m = MY_MO.objects.get(pk=id)
    if request.method == 'POST':
        s = MY_FO(request.POST,instance=m)
        if s.is_valid():
            s.save()
            s = MY_FO()
    else:
        s = MY_FO(instance=m)
            
    return render(request, 'update.html',{'forms':s})