from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth import authenticate ,login ,logout 
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q,Sum
from django.contrib.auth import get_user_model

User = get_user_model()

@login_required(login_url= 'login_account')
def receipes(request):
    if request.method == 'POST':
        receipe_name=request.POST.get('receipe_name')
        receipe_description=request.POST.get('receipe_description')
        receipe_image=request.FILES.get('receipe_image')
    

        Receipe.objects.create(receipe_name=receipe_name,
                           receipe_description=receipe_description,
                           receipe_image=receipe_image)

        return redirect('/receipes/')
    
    
    return render(request, 'receipes.html')

@login_required(login_url= 'login_account/')
def view_receipes(request):
    receipes = None 
    if request.method == 'POST':
        receipe_name = request.POST.get('receipe_name')
        receipes = Receipe.objects.filter(receipe_name__icontains=receipe_name)
    return render(request, 'view_receipes.html', {'receipes': receipes})

@login_required(login_url= 'login_account/')
def delete_receipes(request):
    receipe_deleted = False
    receipe_name = None
    if request.method == 'POST':
        receipe_name=request.POST.get('receipe_name')
        receipe = Receipe.objects.filter(receipe_name=receipe_name).first()
        if receipe:
            receipe.delete()
            receipe_deleted = True
        
    context = {
        'receipe_deleted': receipe_deleted,
        'receipe_name': receipe_name
    }

    return render(request, 'delete_receipes.html',context)


@login_required(login_url= 'login_account/')
def update_receipes(request):
    if request.method == 'POST':
        receipe_name = request.POST.get('receipe_name')
        new_receipe_name = request.POST.get('new_receipe_name')
        new_receipe_description = request.POST.get('new_receipe_description') 

        try:
            recipe = Receipe.objects.get(receipe_name=receipe_name)
            recipe.receipe_name = new_receipe_name
            recipe.receipe_description = new_receipe_description
            recipe.save()
            message = "Recipe updated successfully!"
        except Receipe.DoesNotExist:
            message = "Recipe does not exist."
            
        return render(request, 'update_receipes.html', {'message': message})
    else:
        return render(request, 'update_receipes.html')


def login_account(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request,'Invalid username')
            return redirect('login_account')

        user =authenticate(username=username, password=password)
        if user is None:
            messages.error(request,'Invalid password')
            return redirect('login_account')
        
        else:
            login(request,user)
            return redirect('receipes')

    return render(request, 'login.html')


def logout_account(request):
    logout(request)
    return redirect('/login_account/')

def register(request):
    if request.method == 'POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password=request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error_message': 'Username already exists. Please choose another one.'})

        user=User.objects.create(
            first_name =first_name,
            last_name = last_name,
            username =  username,
              )
        
        user.set_password(password)
        user.save()

        messages.success(request, "Account created successfully")

        return redirect('/register/')
    return render(request, 'register.html')


def get_student(request):
    query_set = Student.objects.all()
    
    if request.GET.get('search'):
        search = request.GET.get('search')
        query_set= query_set.filter(
        
            Q(student_name__icontains = search) |
            Q(department__department__icontains = search) |   
            Q(student_id__student_id__icontains = search) |
            Q(student_email__icontains = search)
        ) 

    paginator = Paginator(query_set, 15) 

    page_number = request.GET.get("page" ,1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'report/students.html' ,{'query_set': page_obj})

def see_marks(request,student_id):
    query_set = SubjectMarks.objects.filter(student__student_id__student_id=student_id)
    total_marks = query_set.aggregate(total_marks = Sum('marks'))
  
    return render(request, 'report/see_marks.html' ,{'query_set': query_set,'total_marks' : total_marks})
