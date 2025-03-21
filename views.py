from django.shortcuts import render, redirect
# from django.http import HttpResponse 
from  django.contrib import messages
from django.contrib.auth.models import User ,auth


  
def login(request):

     if (request.method=='POST'):
          username=request.POST['username']
          password=request.POST['password']
          user=auth.authenticate(username=username, password=password)

          if user is not None:
               auth.login(request,user)
               return redirect('/')
          else:
               messages.info(request,'invalid credentials')

               return render(request,'login.html')

     else:
          return render(request,'login.html')



def register(request):
     #  return HttpResponse("hi rupam")
     
     if(request.method=='POST'):
          first_name=request.POST['first_name']
          last_name=request.POST['last_name']
          email=request.POST['email']
          username=request.POST['username']
          password=request.POST['password']
          confpassword=request.POST['cfpassword']
          
          if(password==confpassword):

               if User.objects.filter(username=username).exists():
                    # print("sorry  user already taken")
                    messages.info(request,'sorry  user already taken')
                    # return redirect('register')
                    return render(request,'registration.html') 
               
               elif User.objects.filter(email=email).exists():
                    # print("sorry  email already taken")
                    messages.info(request,'sorry  email already taken')  #messages akta pre define function for message passing
                    # return redirect('register')  # jodi error hoi then ai register function ta tei ghure aseb and registrar
                    return render(request,'registration.html')

               else:     
                    user=User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name,password=password)
                    user.save()
                    print("user created")
          else:
               print("sorry password not match")
               messages.info(request,'sorry password not match')
               # return redirect('register')
               return render(request,'registration.html')

          return redirect('/')
     

     else:

         return render(request,'registration.html')  
    