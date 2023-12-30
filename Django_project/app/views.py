"""
Definition of views.
"""

from datetime import datetime
from django.http import HttpRequest,HttpResponseRedirect
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils.encoding import force_str
from DjangoFA.tokens import generate_token



from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html')

def bodyshape_view(request):
    return render(request, 'app/bodyshape.html')

def skintype_view(request):
    return render(request, 'app/skintype.html')

def trends_view(request):
    return render(request, 'app/trends.html')

def customer(request):
    return render(request, 'app/customer_review.html')

def trends_men_view(request):
    return render(request, 'app/menfalltrends2023.html')

def trends_women_view(request):
    return render(request, 'app/wintertrendswomen2023.html')

def trends_spring_view(request):
    return render(request, 'app/spring2023trends.html')

def figuref(request):
    return render(request, 'app/figure_fit.html')


from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes

from django.core.mail import EmailMessage
from django.conf import settings

# Assuming you have these imports for token generation:
# from .tokens import generate_token  # Your token generation logic

def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)  # Temporarily prevent saving
            
            # Additional validations
            if User.objects.filter(username=user.username).exists():
                messages.error(request, "Username already exists! Please try another username.")
                return render(request, "app/signup.html", {'form': form})
            
            if User.objects.filter(email=user.email).exists():
                messages.error(request, "Email already registered.")
                return render(request, "app/signup.html", {'form': form})
            
            # Save the user now
            user.is_active = False
            user.save()

            # Send welcome email
            subject = "Welcome to Fashion Advisor"
            message = f"Hello {user.first_name}!\nWelcome to Fashion Advisor!\nThank you for visiting our website."
            from_email = settings.EMAIL_HOST_USER
            to_list = [user.email]
            send_mail(subject, message, from_email, to_list, fail_silently=True)

            # Send confirmation email
            current_site = get_current_site(request)
            email_subject = "Confirm your email"
            message = render_to_string('app/email_confirmation.html', {
                'name': user.first_name,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': generate_token.make_token(user)
            })
            email = EmailMessage(email_subject, message, settings.EMAIL_HOST_USER, [user.email])
            email.fail_silently = True
            email.send()

            messages.success(request, "Your account has been successfully created. Please check your email to confirm your registration.")
            return redirect('home')
    
    else:
        form = CustomUserCreationForm()

    return render(request, "app/signup.html", {'form': form})


def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                fname = user.first_name
                messages.success(request, f'Welcome, {fname}!')
                return render(request, "app/index.html", {'fname': fname})
            else:
                messages.error(request, "Invalid username or password.")
                return redirect('signin')  # You can also render the same login page if desired
        else:
            for error in form.errors.values():
                messages.error(request, error)
            return redirect('home')  # Redirect to the login page with the errors

    else:
        form = AuthenticationForm()
    return render(request, "app/signin.html", {'form': form})

def signout_view(request):
    logout(request)
    return redirect('home') # redirecting to the home page 'index.html'


def activate(request, uidb64, token):
    try:
        uid= force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser= None

    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        return redirect('home')
    
    else:
        return render(request, 'app/activation_failed.html')


# figure and fit view place holder

#def figurefit(request):
    
 #   return render(request, 'app/test.html')


def customerRev(request):
    
    return render(request, 'app/Customer_review_page.html')


def advisor(request):
    
    return render(request, 'app/Influencers.html')



from .forms import StylePreferenceForm

def figurefit(request):
    if request.method == 'POST':
        form = StylePreferenceForm(request.POST)
        if form.is_valid():
            # Normally, you would do something with the data here,
            # but if you're handling image display in the template with JavaScript,
            # just pass the valid form back to the template.
            return render(request, 'app/test.html', {'form': form})
    else:
        # If it's a GET request, just show the unbound form
        form = StylePreferenceForm()


    return render(request, 'app/test.html', {'form': form})


from django.shortcuts import render, redirect
from .forms import CustomerReviewForm

def customer_review(request):
    if request.method == 'POST':
        form = CustomerReviewForm(request.POST)
        if form.is_valid():
            form.save()  # This saves the Customer Review to the database
            return redirect('app/customer_review_page.html')  # Redirect to a success page
    else:
        form = CustomerReviewForm()  # An unbound form for GET request

    return render(request, 'app/customer_review_page.html', {'form': form})







    
