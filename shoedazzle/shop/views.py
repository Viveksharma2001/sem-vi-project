from django.shortcuts import render,redirect
from http.client import HTTPResponse
from django.http import HttpResponse
from shop.forms import CustomerProfileForm, CustomerRegistrationForm
from django.views import View
from shop.models import Contact,product
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):

    mshoes=product.objects.filter(category='MS')
    wshoes=product.objects.filter(category='WS')
    bshoes=product.objects.filter(category='BS')
    gshoes=product.objects.filter(category='GS')
    
    
    return render(request,'shop/index.html',{"data":mshoes,"data1":wshoes,"data2":bshoes,"data3":gshoes})
    

def vivek(request):
    return render(request,'shop/vivek.html')


# def product(request):
#     return render(request,'shop/product.html')

def product1(request):
    return render(request,'shop/product1.html')

def cart(request):
    return render(request,'shop/cart.html')

class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request, 'shop/registration.html',{'form':form})
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulation !! Registered Successfully')
            form.save()
        return render(request, 'shop/registration.html',{'form':form})


class CategoryView(View):
    def get(self,request,val):
        product=product.objects.filter(category=val)
        title=product.objects.filter(category=val).values('title')
        return render(request,'shop/category.html',locals())



# def login(request):
#     if request.method=='POST':
#         #get the post parameters
#         loginUsername=request.POST['loginUsername']
#         Pass=request.POST['Pass']
#         User=authenticate(username=loginUsername,password=Pass)

#         if User is not None:
#             login(request,User)
#             messages.success(request,"Successfully Logged In")
#             return redirect('shopHome')
#         else:
#             messages.error(request,"Invalid Credntials,Please try again")
#             return redirect('shopHome')
    
#     return render(request,'shop/login.html')
   
# def handlelogout(request):
#    logout(request)
#    messages.success(request,"Successfully Logged Out")
#    return redirect('shopHome')
     
  

def signup(request):
    
    if request.method=='POST':
        #get the post parameters
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        Pass1=request.POST['Pass1']
        Pass2=request.POST['Pass2']

        # check for errornous inputs
        if len(username)>10:
            messages.error(request,"username must be under 10 characters")
            return redirect('shopsignup')
        if Pass1!=Pass2:
            messages.error(request,"password does not match")
            return redirect('shopsignup')
        if not username.isalnum():
            messages.error(request,"username should only contain letters and numbers")
            return redirect('shopsignup')
            


        #create the user
        myuser=User.objects.create_user(username,email,Pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,"your V_IceCreams account has been Succesfully Created")
        return redirect('shoplogin')
    if request.method=='GET':
        return render(request,'shop/signup.html')

    

    #return render(request,'shop/signup.html')
    

    

        


  
def contact(request):
    if request.method=="POST":
        fname= request.POST.get('fname')
        lname= request.POST.get('lname')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        desc= request.POST.get('desc')
       # print(name,email,phone,desc)
        contact= Contact(fname=fname,lname=lname, email=email, phone=phone, desc=desc)
        contact.save()
        messages.success(request, 'Your form has been submited!!!')
    
    #return HttpResponse("this is contact pages")
    return render(request,'shop/contact.html')
    

def about(request):
    return render(request,'shop/about.html')
