from django.shortcuts import render, redirect, HttpResponse,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import LensProduct,CustomerDetails
from .forms import LensProductForm, CustomerForm,UserCreationForm, AuthenticationForm,customerDetailsform
from .models import LensProduct,cart,Customer
from django.utils.timezone import now
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings
import uuid
from paypal.standard.forms import PayPalPaymentsForm
from django.urls import reverse 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomerSerializer


# Home view
def show(request):
    products = LensProduct.objects.all()
    context = { 'products': products}
    return render(request, 'home.html', context)

# Contact view
def contact(request):
    return HttpResponse("Contact Us")

# Edit view
def edit(request, rid):
    return HttpResponse("Edit ID: " + rid)

# View specific product
from django.shortcuts import render, get_object_or_404
from .models import LensProduct

from django.shortcuts import render
from .models import LensProduct

from django.shortcuts import render
from .models import LensProduct

def eyeglass_view(request):
    rim_type = request.GET.get("rim_type")  # Get selected rim type from URL

    # Filter products that belong only to the Eye Glasses category
    products = LensProduct.objects.filter(
        is_deleted=False, 
        productCategory=LensProduct.CategoryChoices.EYE_GLASSES
    )

    # Apply rim type filter if selected
    if rim_type:
        products = products.filter(productRimType=rim_type)

    context = {
        "products": products,
        "rim_types": LensProduct.RimTypeChoices.choices,
        "selected_rim": rim_type,
    }

    return render(request, "eyeglasses.html", context)

from django.shortcuts import render
from .models import LensProduct

def sun_glass_view(request):
    rim_type = request.GET.get("rim_type")  # Get selected rim type from URL

    # Filter products that belong only to the Sunglasses category
    products = LensProduct.objects.filter(
        is_deleted=False, 
        productCategory=LensProduct.CategoryChoices.SUN_GLASSES
    )

    # Apply rim type filter if selected
    if rim_type:
        products = products.filter(productRimType=rim_type)

    context = {
        "products": products,
        "rim_types": LensProduct.RimTypeChoices.choices,
        "selected_rim": rim_type,
    }

    return render(request, "sun_glass.html", context)

def power_glass_view(request):
    rim_type = request.GET.get("rim_type")  # Get selected rim type from URL

    # Filter products that belong only to the Power Glasses category
    products = LensProduct.objects.filter(
        is_deleted=False, 
        productCategory=LensProduct.CategoryChoices.POWER_GLASSES
    )

    # Apply rim type filter if selected
    if rim_type:
        products = products.filter(productRimType=rim_type)

    context = {
        "products": products,
        "rim_types": LensProduct.RimTypeChoices.choices,
        "selected_rim": rim_type,
    }

    return render(request, "power_glasses.html", context)


def contact_lens_view(request):
    rim_type = request.GET.get("rim_type")  # Get selected rim type from URL

    # Filter products that belong only to the Contact Lenses category
    products = LensProduct.objects.filter(
        is_deleted=False,
        productCategory=LensProduct.CategoryChoices.CONTACT_LENSES
    )

    # Apply rim type filter if selected
    if rim_type:
        products = products.filter(productRimType=rim_type)

    context = {
        "products": products,
        "rim_types": LensProduct.RimTypeChoices.choices,
        "selected_rim": rim_type,
    }

    return render(request, "contact_lens.html", context)


def reading_glass_view(request):
    rim_type = request.GET.get("rim_type")  # Get selected rim type from URL

    # Filter products that belong only to the Reading Glasses category
    products = LensProduct.objects.filter(
        is_deleted=False,
        productCategory=LensProduct.CategoryChoices.READING_GLASSES
    )

    # Apply rim type filter if selected
    if rim_type:
        products = products.filter(productRimType=rim_type)

    context = {
        "products": products,
        "rim_types": LensProduct.RimTypeChoices.choices,
        "selected_rim": rim_type,
    }

    return render(request, "reading_glass.html", context)



def accessories_view(request):
    rim_type = request.GET.get("rim_type")  # Get selected rim type from URL

    # Filter products that belong only to the Contact Lenses category
    products = LensProduct.objects.filter(
        is_deleted=False,
        productCategory=LensProduct.CategoryChoices.CONTACT_LENSES
    )

    # Apply rim type filter if selected
    if rim_type:
        products = products.filter(productRimType=rim_type)

    context = {
        "products": products,
        "rim_types": LensProduct.RimTypeChoices.choices,
        "selected_rim": rim_type,
    }

    return render(request, "accessories.html", context)

def computer_glass_view(request):
    rim_type = request.GET.get("rim_type")  # Get selected rim type from URL

    # Filter products that belong only to the Contact Lenses category
    products = LensProduct.objects.filter(
        is_deleted=False,
        productCategory=LensProduct.CategoryChoices.CONTACT_LENSES
    )

    # Apply rim type filter if selected
    if rim_type:
        products = products.filter(productRimType=rim_type)

    context = {
        "products": products,
        "rim_types": LensProduct.RimTypeChoices.choices,
        "selected_rim": rim_type,
    }

    return render(request, "computer_glasses.html", context)

def kids_eye_glasses(request):
    rim_type = request.GET.get("rim_type")

    products = LensProduct.objects.filter(
        is_deleted=False,
        productCategory=LensProduct.CategoryChoices.K_EYE_GLASSES
    )

    if rim_type:
        products = products.filter(productRimType=rim_type)

    context = {
        "products": products,
        "rim_types": LensProduct.RimTypeChoices.choices,
        "selected_rim": rim_type,
    }

    return render(request, "kids_eye_glasses.html", context)


def kids_sun_glasses(request):
    rim_type = request.GET.get("rim_type")

    products = LensProduct.objects.filter(
        is_deleted=False,
        productCategory=LensProduct.CategoryChoices.k_SUN_GLASSES
    )

    if rim_type:
        products = products.filter(productRimType=rim_type)

    context = {
        "products": products,
        "rim_types": LensProduct.RimTypeChoices.choices,
        "selected_rim": rim_type,
    }

    return render(request, "kids_sun_glasses.html", context)


# def power_glass_view(request):
#     products = LensProduct.objects.filter(productCategory="POWER_GLASSES", is_deleted=False)
#     return render(request, 'power_glasses.html', {"products": products})

# def sun_glass_view(request):
#     products = LensProduct.objects.filter(productCategory="SUN_GLASSES", is_deleted=False)
#     return render(request, 'sun_glass.html', {"products": products})

def computer_glass_view(request):
    products = LensProduct.objects.filter(productCategory="COMPUTER_GLASSES", is_deleted=False)
    return render(request, 'computer_glasses.html', {"products": products})

# def contact_lens_view(request):
#     products = LensProduct.objects.filter(productCategory="CONTACT_LENSES", is_deleted=False)
#     return render(request, 'contact_lens.html', {"products": products})

def accessories_view(request):
    products = LensProduct.objects.filter(productCategory="ACCESSORIES", is_deleted=False)
    return render(request, 'accessories.html', {"products": products})


def viewproduct(request, id):
    products = LensProduct.objects.filter(id=id)
    return render(request, 'viewproduct.html', {'products': products})

    
def addproduct(request):
    if request.method=="POST":
        form=LensProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=LensProductForm()
    return render(request,'addproductcrud.html',{'form':form})


def deleteproductcrud(request, id):
    # Use `get_object_or_404` to handle non-existent products gracefully
    product = get_object_or_404(LensProduct, id=id, is_deleted=False)
    product.is_deleted = True
    product.delete_details = now()
    product.save()
    return render(request,'eyeglass.html')

# products=LensProduct.objects.filter(is_deleted=False)


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def register_customer(request):
    try:
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            if password != confirm_password:
                messages.error(request, 'Passwords do not match.')
                return redirect('register')

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken.')
                return redirect('register')

            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email is already registered.')
                return redirect('register')

            user_obj = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password
            )
            user_obj.save()

            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')

    except Exception as e:
        print(f"Error: {e}")
        messages.error(request, 'An error occurred during registration. Please try again.')

    return render(request, 'register.html')




from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, "Both fields are required")
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully logged in")
                return redirect('home')  # Redirect prevents form resubmission
            else:
                messages.error(request, "Invalid username or password")

        return redirect('login')  # Redirect to clear duplicate messages

    return render(request, 'login.html')




import random
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def forgetpassword(request):
    if request.method == "POST":
        email = request.POST.get('email')

        users = User.objects.filter(email=email)
        print(users)

        if users.exists():
            user = users.first()
            otp = random.randint(100000, 999999)
            request.session['reset_otp'] = otp
            request.session['reset_email'] = email
            request.session['otp_purpose'] = "password_reset"
            request.session.modified = True  # Ensure session updates

            subject = "Password Reset Request - Your OTP Inside"
            message = f"""
            Hello {user.username},

            We received a request to reset your password. To proceed, please use the One-Time Password (OTP) below:

            🔐 *Your OTP:* {otp}

            This OTP is valid for a limited time. If you did not request this, please ignore this email, and your account will remain secure.

            For security reasons, never share your OTP with anyone.

            Best regards,  
            Your Support Team
            """

            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [email], fail_silently=False)
                messages.success(request, "An OTP has been sent to your email.")
                return redirect('verifyotp')
            except Exception as e:
                print(f"Email Error: {e}")
                messages.error(request, "Failed to send OTP. Please try again.")

        else:
            messages.error(request, "Email not found! Please enter a registered email.")

    return render(request, 'forgot_password.html')

def verifyotp(request):
    if request.method == "POST":
        entered_otp = request.POST.get('otp')
        stored_otp = request.session.get('reset_otp')
        
        if stored_otp and entered_otp == str(stored_otp):
            return redirect('resetpassword')
        else:
            messages.error(request, "Invalid OTP! Please enter a valid OTP or try again")
            
    return render(request, 'verifyotp.html')



def resetpassword(request):
    if request.method == "POST":
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        email = request.session.get('reset_email')

        if new_password == confirm_password:
            try:
                user =  User.objects.get(email=email)
                user.set_password(new_password)
                user.save()

                del request.session['reset_otp']
                del request.session['reset_email']

                messages.success(request,"Password reset successful ! You can login ")
                return redirect('login')
            except User.DoesNotExist:
                messages.error(request,"Somthing went wrong")
                return redirect('forgetpassword')
        else:
            messages.error(request,"Password do not match ! Try again")
            return render(request, 'resetpassword.html')
    return render(request,'resetpassword.html')

@login_required(login_url='login')
def addtocart(request,id):
    userid=request.user.id
    user_details=User.objects.filter(id=userid)

    products=LensProduct.objects.filter(id=id)
    print(products)
    # q1=Q(pid=products[0])
    # q2=Q(uid=user_details[0])
    
    if products :
        q1=Q(pid=products[0])
        q2=Q(uid=user_details[0])

        prod=cart.objects.filter(q1 & q2)

        n=len(prod)
        context={}
        context['products']=products
        if n==1:
            context['msg']="All ready in Cart"
            return render(request,'viewproduct.html',context)
        else:
            addtocartprod=cart.objects.create(pid=products[0],uid=user_details[0])
            addtocartprod.save()
            context['success']="Successfully Added to cart!!!"
            return render(request,'viewproduct.html',context)
    
    else :
        return HttpResponse(" Error ")


from decimal import Decimal
from decimal import Decimal
from django.shortcuts import render
from .models import cart  # Ensure correct model import

from decimal import Decimal
from django.shortcuts import render

from decimal import Decimal
from django.shortcuts import render
from .models import cart

def viewcart(request):
    userid = request.user.id
    products = cart.objects.filter(uid=userid)
    
    total = Decimal("0")  # Ensure it's a Decimal
    valid_products = []  # List to store only valid products
    
    for i in products:
        if i.pid:  # Check if product exists
            total += i.pid.productPrice * i.qty
            valid_products.append(i)  # Add only valid products

    del_charge = Decimal("15") if total <= 200 else Decimal("10") if total <= 500 else Decimal("0")
    grand_total = total + del_charge

    return render(request, 'viewcart.html', {
        'products': valid_products,  # Only valid products
        'total': total,
        'del_charge': del_charge,
        'grand_total': grand_total
    })


# def viewcart(request):
#     userid = request.user.id
#     print(f"User ID: {userid}")

#     # Fetch cart items for both product types
#     cart_items = cart.objects.filter(uid=userid).select_related('pid')

#     print(f"Cart Products: {cart_items}")

#     total = Decimal("0.00")  # Use Decimal for precise calculations
#     valid_products = []  # Store only valid products

#     # Delivery charge calculation
#     del_charge = Decimal("15") if total <= 200 else Decimal("10") if total <= 500 else Decimal("0")

#     grand_total = total + del_charge

#     print(f"Total: {total}, Delivery Charge: {del_charge}, Grand Total: {grand_total}")

#     return render(request, 'viewcart.html', {
#         'products': valid_products,
#         'total': total,
#         'del_charge': del_charge,
#         'grand_total': grand_total
#     })



from django.contrib import messages

def signout(request):
    logout(request)
    messages.success(request, "You're successfully logged out.")  # Add success message
    return redirect('home')  # Redirect to home page



def updateqty(request,qv,id):
    c=cart.objects.filter(id=id)
    if qv=='1':
        t=c[0].qty+1
        c.update(qty=t)

        return redirect('/viewcart')
    else:
        if c[0].qty>1:
            t=c[0].qty-1
            c.update(qty=t)
    return redirect('/viewcart')


def searchdata(request):
    if request.method == 'POST':
        searchData = request.POST.get('search', '').strip()
        print("Search Query Received:", searchData)  # Debugging
        result = LensProduct.objects.filter(productName__icontains=searchData)
        print("Queryset Results:", result)  # Debugging

        return render(request, 'search.html', {'result': result})
    else:
        return render(request, 'search.html')


def remove(request,id):
    products=cart.objects.filter(id=id)
    print(products)
    products.delete()
    return redirect('viewcart')

    
from django.shortcuts import render, redirect  # ✅ Ensure `render` is imported
from .forms import customerDetailsform  # ✅ Ensure the form is imported

import re
from django.core.exceptions import ValidationError

import re
from django.core.exceptions import ValidationError

def validate_pincode(value):
    """ Ensure PIN code is a valid 6-digit number """
    value_str = str(value)  # Convert to string
    if not re.match(r"^\d{6}$", value_str):  
        raise ValidationError("Invalid PIN code. It must be a 6-digit number.")

def customerDetails(request):
    if request.method == "POST":
        fm = customerDetailsform(request.POST)
        if fm.is_valid():
            # ✅ Delete old addresses before saving a new one
            CustomerDetails.objects.filter(user=request.user).delete()

            # ✅ Create a new customer detail entry
            customer = fm.save(commit=False)
            customer.user = request.user

            # ✅ Validate and save
            try:
                validate_pincode(str(customer.pincode))  # Ensure it's a string
                customer.save()
                print("✅ Address Saved:", customer.custname, customer.custAddress)  # Debugging
                return redirect('checkout')  # ✅ Redirect to checkout
            except ValidationError as e:
                fm.add_error("pincode", e.message)  # Show error in form
        else:
            print("❌ Form validation failed", fm.errors)  # Debugging output

    else:
        fm = customerDetailsform()

    return render(request, 'checkoutdetails.html', {'form': fm})


from django.contrib import messages

from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid

from decimal import Decimal
import uuid
import re
from django.conf import settings
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Order, OrderItem, cart, CustomerDetails
from paypal.standard.forms import PayPalPaymentsForm

def checkout(request):
    user = request.user

    # ✅ Fetch customer details (including address)
    customer = CustomerDetails.objects.filter(user=user).last()
    if not customer:
        messages.warning(request, "Please complete your profile details before checkout.")
        return redirect("profile")

    # ✅ Validate Email and Pincode (convert pincode to string)
    if not re.match(r"[^@]+@[^@]+\.[^@]+", customer.custEmail):
        messages.error(request, "Invalid email address.")
        return redirect("profile")

    if not re.match(r"^\d{6}$", str(customer.pincode)):  # Convert pincode to string before matching
        messages.error(request, "Invalid PIN code. Must be 6 digits.")
        return redirect("profile")

    # ✅ Fetch cart items
    cart_items = cart.objects.filter(uid=user.id).select_related("pid")
    if not cart_items.exists():
        messages.warning(request, "Your cart is empty.")
        return redirect("viewcart")

    # ✅ Calculate total amount
    total_amount = sum(Decimal(item.pid.productPrice) * item.qty for item in cart_items)
    
    # ✅ Apply delivery charge
    delivery_charge = Decimal("50") if total_amount <= 2000 else Decimal("20") if total_amount <= 5000 else Decimal("0")
    grand_total = total_amount + delivery_charge

    # ✅ Generate unique order ID
    order_id = str(uuid.uuid4())

    # ✅ Create Order (Initially Pending)
    order = Order.objects.create(
        user=user,
        order_id=order_id,
        total_amount=grand_total,
        payment_status="Pending",
        order_status="Pending"
    )

    # ✅ Save Order Items
    for item in cart_items:
        OrderItem.objects.create(order=order, product=item.pid, quantity=item.qty)

    # ✅ Set up PayPal payment
    host = request.get_host()
    paypal_checkout = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": grand_total,
        "item_name": "Eyecraft Order",
        "invoice": order_id,
        "currency_code": "USD",
        "notify_url": f"http://{host}{reverse('paypal-ipn')}",
        "return_url": f"http://{host}{reverse('paymentsuccess')}?invoice={order_id}",
        "cancel_url": f"http://{host}{reverse('paymentfailed')}",
    }
    paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)

    context = {
        "customer": customer,  # ✅ Include Customer Details (Address)
        "cart_items": cart_items,
        "total_amount": total_amount,
        "delivery_charge": delivery_charge,
        "grand_total": grand_total,
        "paypalpayment": paypal_payment,
    }

    return render(request, "checkout.html", context)



from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Order

def paymentsuccess(request):
    order_id = request.GET.get('invoice')  # Get order_id from PayPal response

    try:
        order = Order.objects.get(order_id=order_id)
        order.payment_status = "Completed"  # ✅ Mark as Completed
        order.order_status = "Processing"  # ✅ Update order status
        order.save()

        # ✅ Store order details in session for success page
        request.session["order_id"] = order.order_id
        request.session["total_amount"] = str(order.total_amount)

        messages.success(request, "Payment successful! Your order is being processed.")

        return redirect("payment_success_page")  # ✅ Redirect to a different success page
    except Order.DoesNotExist:
        messages.error(request, "Order not found.")
        return redirect("home")  # ✅ Redirect to home instead of looping


def payment_success_page(request):
    order_id = request.session.get("order_id", None)
    total_amount = request.session.get("total_amount", None)

    if not order_id or not total_amount:
        return redirect("home")  # ✅ Redirect to home if session data is missing

    return render(request, "paymentsuccess.html", {"order_id": order_id, "total_amount": total_amount})




from django.shortcuts import render
from .models import Order

from django.core.mail import send_mail
from django.conf import settings

import pytz
from django.utils.timezone import localtime
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render
from .models import Order

def orders(request):
    # Fetch user orders sorted by creation time
    user_orders = Order.objects.filter(user=request.user).order_by("created_at")

    if not user_orders.exists():
        messages.info(request, "No orders found.")
        return render(request, "orders.html", {"orders": user_orders})

    # Convert all order timestamps to IST
    ist_timezone = pytz.timezone("Asia/Kolkata")
    for order in user_orders:
        order.created_at = order.created_at.astimezone(ist_timezone)

    # Get the first order
    first_order = user_orders.first()
    ist_time = first_order.created_at.strftime('%b %d, %Y %H:%M IST')  # 24-hour format

    # Email details
    subject = "Order Confirmation - Thank You for Shopping!"
    message = f"""\ 
Dear {request.user.username},

Thank you for your purchase! 🎉 Your first order has been successfully placed.

🛍 **Order Details**:
- Order ID: {first_order.id}
- Date: {ist_time}
- Total Amount: ₹{first_order.total_amount}

We will update you once your order is shipped. 🚚

Thank you for shopping with us! ❤️

Best Regards,  
Your Store Team
"""

    recipient_email = request.user.email

    try:
        send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient_email], fail_silently=False)
        messages.success(request, "Your order is placed! A confirmation email has been sent.")
    except Exception as e:
        print(f"Email Error: {e}")
        messages.error(request, "Your order was placed, but we couldn't send an email.")

    return render(request, "orders.html", {"orders": user_orders})



def paymentfailed(request):
    messages.error(request, "Payment failed or was canceled. Please try again.")
    return redirect("checkout")  # Redirect back to checkout page


class crudapi(APIView):
    def get(self,request):
        id=request.data.get('id',None)
        if id:
            try:
                customer=CustomerDetails.objects.get(id=id)
                customerdata=CustomerSerializer(customer)
                print(customer)
                return Response(customerdata.data,status=status.HTTP_200_OK)
            except:
                return Response({'msg':'Data is not available'},status=status.HTTP_400_BAD_REQUEST)
        else:
            customer.CustomerDetails.objects.all()
            print(customer)
            customerdata=CustomerSerializer(customer,many=True)
            print(customerdata)
            return Response(customerdata.data,status=status.HTTP_200_OK)


    def post(self,request):
        CustomerDetails=request.data
        print(CustomerDetails)
        customerdata=CustomerSerializer(data=CustomerDetails)
        print(customerdata)
        if customerdata.is_valid():
            customerdata.save()
            return Response({'Msg':'This is post request'},status=status.HTTP_200_OK)
        return Response({'Msg':'Data is not available'},status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request):
        new_data=request.data
        id=new_data.get('id',None)
        print(id)
        if id:
            try:
                customer_data=CustomerDetails.objects.get(id=id)
                print(customer_data)
                customer_data=CustomerSerializer(customer_data,new_data,partial=True)
                if customer_data.is_valid():
                    customer_data.save()
                    return Response({'Msg':'This is patch request'},status=status.HTTP_200_OK)
            except:
                return Response({'Msg':'data is not available'},status=status.HTTP_404_NOT_FOUND)
    
    def delete(self,request):
        id=request.data.get('id',None)
        print(id)
        if id:
            try:
                customer=CustomerDetails.objects.get(id=id)
                customer.delete()
                return Response({'Msg':'Data is successfully deleted'},status=status.HTTP_200_OK)
            except:
                return Response({'Msg':'Data is not available'},status=status.HTTP_400_BAD_REQUEST)
        return Response({'Msg':'Please provide id'},status=status.HTTP_200_OK)
    
from django.shortcuts import render, get_object_or_404, redirect
from .models import LensProduct
from .forms import LensProductForm


def update_product_view(request, id): 
    product = get_object_or_404(LensProduct, id=id)

    if request.method == "POST":
        form = LensProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('viewproduct', id=product.id)
    else:
        form = LensProductForm(instance=product)

    context = {
        'form': form,
        'product': product,
    }

    return render(request, 'update_product.html', context)



def delete_product_view(request, id):
    product = get_object_or_404(LensProduct, id=id)
    product.delete()  # Permanently delete the product
    return redirect('eyeglass')  # Redirect to eyeglasses page

from django.db.models import Count

from django.shortcuts import render, get_object_or_404
from django.db.models import Count


def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

from django.shortcuts import render, redirect
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm


from django.shortcuts import render, redirect
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm
import uuid

# def paypal_payment(request):
#     if request.method == "POST":
#         amount = request.POST.get("amount")

#         if not amount:  # Ensure amount is provided
#             return redirect("checkout")

#         invoice_id = f"INV-{uuid.uuid4().hex[:10]}"  # Generate a unique invoice ID

#         paypal_dict = {
#             "business": settings.PAYPAL_RECEIVER_EMAIL,
#             "amount": amount,
#             "item_name": "Order Payment",
#             "invoice": invoice_id,
#             "currency_code": "USD",  # Update this if using a different currency
#             "notify_url": request.build_absolute_uri("/paypal-ipn/"),
#             "return_url": request.build_absolute_uri("/payment-success/"),
#             "cancel_return": request.build_absolute_uri("/payment-failed/"),
#         }

#         form = PayPalPaymentsForm(initial=paypal_dict)

#         # Redirect directly to PayPal payment page
#         return redirect(form.get_redirect_url())

#     return redirect("checkout")


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomerDetails


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CustomerDetails
from .forms import customerDetailsform

def update_address(request):
    if request.method == "POST":
        user = request.user
        customer, created = CustomerDetails.objects.get_or_create(user=user)

        form = customerDetailsform(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, "Address updated successfully!")
            return redirect("checkout")
        else:
            messages.error(request, "Failed to update address. Please check your input.")

    else:
        form = customerDetailsform()

    return render(request, "update_address.html", {"form": form})



from .models import LensProduct

def view_product(request, id):
    product = get_object_or_404(LensProduct, id=id)
    return render(request, 'viewproduct.html', {'products': [product]})


