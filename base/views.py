from django.shortcuts import render, redirect
from django.http import HttpResponse     #"django.http" is a module of Django and "HttpResponse" is class 
from .models import Todo       #models is our local module and "Todo" is class

# Create your views here.
def home(request):
   # return HttpResponse('homeaaa')     #view should send  either "HttpResponse","Json Response" or "Template"
   todo_objs = Todo.objects.all()
   content = {'todos':todo_objs}  #while sending data to "html" file, datas must be send in Dictionary form.
   return render(request,"index.html",context=content)

def create(request):
   if request.method =="POST":
      name1 = request.POST.get('cname')
      description1 = request.POST.get('cdescription')
      status1 = request.POST.get('cstatus')

      Todo.objects.create(name=name1,description=description1,status=status1) 
      return redirect("home88")
      #name: This is the value you want to set for the name field of your Todo model.
      #description: This is the value you want to set for the description field of your Todo Model.
      #status: This is the value you want to set for the status field of your Todo model.
                                                                              
   return render(request,"create.html")  

def edit(request,pk):
   todo_obj = Todo.objects.get(id=pk)
   #print(todo_obj)
   #print(todo_obj.name)

   if request.method =="POST":
      name_update = request.POST.get('cname')
      description_update = request.POST.get('cdescription')
      status_update = request.POST.get('cstatus')
   
      todo_obj.name = name_update
      todo_obj.description = description_update
      todo_obj.status = status_update
      todo_obj.save()
      return redirect("home88")
   
   content = {'todo':todo_obj}  
   return render(request,"edit.html",context=content) #context" refers to the Dictionary data that is passed from the views to the templates. 

def delete(request,pk):
    todo_obj = Todo.objects.get(id=pk)
    todo_obj.delete()
    return redirect("home88")
   
def delete_all_datas(request):
    Todo.objects.all().delete()
    return redirect("home88")


   