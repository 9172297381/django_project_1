from django.urls import path
from . import views 
from .views import register_customer,login_view
from .views import crudapi



urlpatterns = [
    path('', views.show, name='home'),
    path('contact/', views.contact, name='contact'),
    path('edit/<rid>/', views.edit, name='edit'),
    path('viewproduct/<int:id>/', views.viewproduct, name='viewproduct'),
    path('addcart/<int:id>/', views.addtocart, name='addtocart'),
    path('addproduct',views.addproduct,name='addproduct'),
    path('deleteproductcrud/<int:id>/',views.deleteproductcrud,name="deleteproductcrud"),
    path('updateproduct/<int:id>/', views.update_product_view, name='updateproduct'),
    path('deleteproduct/<int:id>/', views.delete_product_view, name='deleteproduct'),
    path('register/', views.register_customer,name='register'),
    path('login/',login_view,name='login'),
    path('viewcart/',views.viewcart, name='viewcart'),
    path('logout/',views.signout,name='logout'),
    path('updateqty/<qv>/<id>/',views.updateqty),
    path('searchdata',views.searchdata,name="searchdata"),
    path('remove/<int:id>',views.remove,name='remove'),
    path('checkoutdetails/', views.customerDetails,name="checkoutdetails"),
    path('checkout/', views.checkout, name='checkout'),  # No ID required
    path('checkout/<int:id>/', views.checkout, name='checkout_with_id'),
    path('paymentsuccess',views.paymentsuccess,name='paymentsuccess'),
    path('paymentfailed',views.paymentfailed,name='paymentfailed'),
    # path('orders/',views.orders,name='orders'),
    path('orders/', views.orders, name='orders'),
    path('drf_crud/',views.crudapi.as_view()),
    path('eyeglasses/', views.eyeglass_view, name='eyeglass'),  # URL pattern for eyeglasses
    path('power-glasses/', views.power_glass_view, name='power_glass'),
    path('sun-glasses/', views.sun_glass_view, name='sun_glass'),
    path('computer-glasses/', views.computer_glass_view, name='computer_glass'),
    path('contact-lenses/', views.contact_lens_view, name='contact_lens'),
    path('accessories/', views.accessories_view, name='accessories'),
    path('about-us/', views.about_view, name='about'),
    path('contact-us/', views.contact_view, name='contact'),
    path("update_address/", views.update_address, name="update_address"),
    path("payment-success-page/", views.payment_success_page, name="payment_success_page"),
    path('product/<int:id>/', views.view_product, name='view_product'),
    path('forget-password/', views.forgetpassword, name='forget-password'),
    path('verifyotp/',views.verifyotp,name='verifyotp'),
    path('resetpassword/',views.resetpassword,name='resetpassword'),
    # path('paypal-payment/', views.paypal_payment, name='paypal_payment'),
       
]

