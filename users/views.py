from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from users.forms import profileUpdateForm, userUpdateForm
from users.models import Profile as Pro
from users.models import  Demandes as Dem
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
#from memberships.models import Membership, UserMembership, Subscription
from django.core.mail import send_mail
from django.core.mail import EmailMessage


# Create your views here.

@login_required
def Profile(request):
    #user_membership = get_user_membership(request)
    #user_subscription = get_user_subscription(request)
    if request.method == 'POST':
        u_form = userUpdateForm(request.POST,instance=request.user)
        p_form = profileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Votre compte a été mis à jour avec succès!')
            return redirect('users:profile')
    else:
        u_form = userUpdateForm(instance=request.user)
        p_form = profileUpdateForm(instance=request.user.profile)

    context= {
        'u_form':u_form,
        'p_form':p_form,
        #'user_membership':user_membership,
        #'user_subscription': user_subscription
    }
    return render(request,'profile/profile.html',context)

@login_required
def Demandes(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        prof = request.user.profile
        demande = Dem(profile=prof, name=name, email=email, phone_number=phone_number)
        demande.save()
        prof_id = prof.id
        Pro.objects.filter(id=prof_id).update(is_teacher=True)
        
        message = 'Votre demande de compte enseignant a été acceptée! Vous pouvez maintenant retourner sur SchooliEducation et télécharger des cours et des conférences, bon travail!'
        send_mail(
            'SchooliEducation, la demande a été acceptée.',
            message,
            'yvindjhonnelmahoukou@gmail.com',
            [email],
            fail_silently=False,
        )
        send_mail(
            'SchooliEducation',
            'Quelqu\'un a demandé un compte enseignant. Moi info: ' + name + ' , ' + email + ' , ' + phone_number + ' , ' + str(prof) + '.',
            'yvindjhonnelmahoukou@gmail.com',
            ['yvindjhonnelmahoukou@gmail.com'],
            fail_silently=False,
        )
        messages.info(request, f'La demande a été envoyée avec succès, vous serez averti par email.')
        return redirect('courses:home')

    else:
        return render(request,'profile/teacher_sign_up.html')


