from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from .forms import Addproject
from .models import Todolist


# Create your views here.
def home(request):
    form = Addproject()
    datas = Todolist.objects.all()
    context = {'form':form, 'datas':datas}
    return render(request, 'app/home.html', context)


def save_data(request):
    if request.method == "POST":
        pid = request.POST['id']
        ttl = request.POST['title']
        des = request.POST['description']
        ddl = request.POST['deadline']

        if (pid == ""):
            todo = Todolist(title=ttl, description=des, deadline=ddl)
            status = "new_register"

        else:
            todo = Todolist(id=pid, title=ttl, description=des, deadline=ddl)
            status = "updated"
        todo.save()

        queryset = Todolist.objects.all()
        all_json_data = list(queryset.values())
        context = {
            'status': status,
            'id': todo.id,
            'title': todo.title,
            'description': todo.description,
            'created_on': todo.created_on,
            'deadline': todo.deadline,
            'all_data': all_json_data
        }

        return JsonResponse(context)

    else:
        return JsonResponse({'status':0})


def delete_data(request):
    if request.method == "POST":
        id = request.POST.get('pid')
        project_data = Todolist.objects.get(pk=id)
        project_data.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})



def edit_data(request):
    if request.method == "POST":
        id = request.POST.get('pid')
        project = Todolist.objects.get(pk=id)
        project_data = {
            'id': project.id,
            'title': project.title,
            'description': project.description,
            'created_on': project.created_on,
            'deadline': project.deadline
        }
        return JsonResponse(project_data)



