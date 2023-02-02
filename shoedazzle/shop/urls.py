from unicodedata import name
from django.contrib.auth import views as auth_views

from shop.forms import LoginForm, MyPasswordResetForm,MyPasswordChangeForm

from .import views
from django.urls import path,include
urlpatterns = [
    
    path("",views.index,name="shopHome"),
    path("about",views.about,name="shopabout"),
    path("signup",views.signup,name="shopsignup"),
    path("contact",views.contact,name="shopcontact"),
    # path("logout",views.handlelogout,name="shoplogout"),
    path("vivek",views.vivek,name="shopvivek"),
    path("product",views.product,name="shopproduct"),
    path("product1",views.product1,name="shopproduct1"),
    path("cart",views.cart,name="shopcart"),
    path('registration', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('login',auth_views.LoginView.as_view(template_name='shop/login.html',authentication_form=LoginForm),name='login'),
    path('password-reset',auth_views.PasswordResetView.as_view(template_name='shop/password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),
    path('passwordchange',auth_views.PasswordChangeView.as_view(template_name='shop/passwordchange.html',form_class=MyPasswordChangeForm,  success_url='/passwordchangedone/'),name='passwordchange'),
    path('logout',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    path("category/<slug:val>",views.CategoryView.as_view(),name="category")
   
    ]