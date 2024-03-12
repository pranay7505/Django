from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):

    peoples = [ 
               {'name': "pranay patil", 'age': 21}, 
               {'name': "Ritesh patil", 'age': 23}, 
               {'name': "aditi solanki", 'age': 21}, 
               {'name': "ketan khursange", 'age': 20}
            ]
    
    
    

    
    
    return render(request,'index.html', context={'peoples' : peoples})


def raj(request):
    return HttpResponse('''<h2>the man who is always stant in front on me.</h2>
                        <p styel="color: red;">
                        so hello there i am pranay patil and i am learning Django which is framework of python 

                        </p>''')

