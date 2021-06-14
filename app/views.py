from django.shortcuts import render,redirect
from .models import todo

# Create your views here.

def HomeView(request):
	TodoList = todo.objects.all() 
	if request.GET:
		if 'delete' in request.GET.keys():
			todo(id = request.GET['delete']).delete()
			return redirect('home')
	if request.POST:
		todo(affair = request.POST['add'] ).save()
		return redirect('home')
	context = {
		'todo':TodoList
	}
	return render(request , 'home.html' , context)
def detail(request ,pk):
	item = todo.objects.get(id = pk)
	if request.POST:
		if 'complete' in request.POST.keys():
			todo.objects.filter(id = pk).update(affair=request.POST['text'] , complete=True)
		else:
			todo.objects.filter(id = pk).update(affair=request.POST['text'] , complete=False)
		return redirect('home')
	context = {
		'item':item,
		"name":f"{item.affair}"
	}
	return render(request , 'detail.html' ,context)
