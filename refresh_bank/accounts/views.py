from django.shortcuts import render , redirect
from django.views.generic import FormView ,View
from django.contrib.auth.views import LoginView , LogoutView 
# Create your views here.
from .forms import UserRegistrationForm
from django.urls import reverse_lazy
from django.contrib.auth import login , logout
from .forms import UserUpdateForm

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin

from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

def send_email(user,subject,body): 
        email = EmailMultiAlternatives(
            subject=subject,
            body='',
            from_email= 'ReFresh Bank <noreply@example.com>',
            to=[user.email],
        )
        email.attach_alternative(body, "text/html")
        email.send()


class UserRegistrationView(FormView):
    template_name = 'accounts/user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('register')

    def form_valid(self, form):
        print(form.cleaned_data )
        user = form.save()
        login(self.request,user)
        return super().form_valid(form) # form_valid function all hoba jodi sob tik thaka
    
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('home')

from django.core.mail import send_mail

class UserLoginView(LoginView):
    template_name = 'accounts/user_login.html'
    def get_success_url(self): 
        context = {
            'user':self.request.user, 
        }
        body = render_to_string('email_templates/login_email.html',context)
        send_email(self.request.user,'Login Success',body)

        return reverse_lazy('home')

# RedirectView
class UserLogoutView(LoginRequiredMixin,LogoutView):
    # next_page = reverse_lazy('home')
    def get_success_url(self): 
        logout(self.request)
        return reverse_lazy('home') 
    



class UserBankAccountUpdateView(LoginRequiredMixin,View):
    template_name = 'accounts/profile.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        password_form = PasswordChangeForm(user=request.user,data=request.POST)

        return render(request, self.template_name, {'form': form,'password_form':password_form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        password_form = PasswordChangeForm(user=request.user,data=request.POST)

        if password_form.is_valid():
            password_form.save() 
            update_session_auth_hash(request,password_form.user)

            context = {
                'user':self.request.user
            }
            body = render_to_string('email_templates/password_update_email.html',context)
            send_email(self.request.user,'Password Changed Update',body)

            return redirect('profile')  # Redirect to the user's profile page

        
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the user's profile page
        return render(request, self.template_name, {'form': form,'password_form':password_form})