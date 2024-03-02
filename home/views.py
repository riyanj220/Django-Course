from django.shortcuts import render
from django.http import HttpResponse


def home(request):

    people=[
        {'name': 'John', 'age':19}, 
        {'name': 'Ali', 'age':20}, 
        {'name': 'Riyan', 'age':16}, 
        {'name': 'abcd', 'age':25}, 
    ]
    for person in people:
        person['can_vote']=person['age'] >18
    
    for i in people:
        if i['age'] in people:
            return render(request,'index.html',context={'page':'Django Tutorial'})
            
    vegetables=['aalo','tomato','cheese','carrot']
    return render(request,'index.html',context={'page':'Django Tutorial','people':people,'vehgetables':vegetables,'age':i})
    
def contact(request):
    context ={'page':'Contact'}
    return render(request,'contact.html',context)

def about(request):
    context ={'page':'About'}
    return render(request,'about.html',context)


