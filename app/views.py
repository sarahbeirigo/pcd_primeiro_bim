from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from .models import Raffle
from .forms import RaffleForm

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_verification = request.POST.get('password_verification')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        context = {
            'email': email,
            'first_name': first_name,
            'last_name': last_name,
        }

        if password != password_verification:
            messages.error(request, 'As senhas não coincidem.')
            return render(request, 'registration/form.html', context)

        if User.objects.filter(username=email).exists():
            messages.error(request, 'Este email já está registrado.')
            return render(request, 'registration/form.html', context)

        user = User.objects.create_user(username=email, email=email, password=password, first_name=first_name, last_name=last_name)
        login(request, user)
        return redirect('dashboard_main')

    return render(request, 'registration/form.html')

def forgot_password(request):
    return render(request, 'forgot_password.html')

def reset_password(request):
    return render(request, 'reset_password.html')

@login_required
def dashboard_main(request):
    return render(request, 'dashboard/main.html')

@login_required
def raffle_list_admin(request):
    rifas = Raffle.objects.filter(user=request.user)
    return render(request, 'dashboard/raffles/admin_list.html', {'rifas': rifas})

@login_required
def raffle_create(request):
    if request.method == 'POST':
        form = RaffleForm(request.POST, request.FILES)
        if form.is_valid():
            rifa = form.save(commit=False)
            rifa.user = request.user
            rifa.avaliable_tickets = rifa.total_tickets
            rifa.save()
            return redirect('raffle_list_admin')
    else:
        form = RaffleForm()
    return render(request, 'dashboard/raffles/form.html', {'form': form, 'action': 'create'})

@login_required
def raffle_edit(request, pk):
    rifa = get_object_or_404(Raffle, pk=pk, user=request.user)
    if request.method == 'POST':
        form = RaffleForm(request.POST, request.FILES, instance=rifa)
        if form.is_valid():
            form.save()
            return redirect('raffle_list_admin')
    else:
        form = RaffleForm(instance=rifa)
    return render(request, 'dashboard/raffles/form.html', {'form': form, 'action': 'edit', 'rifa': rifa})

@login_required
def raffle_detail(request, pk):
    rifa = get_object_or_404(Raffle, pk=pk, user=request.user)
    form = RaffleForm(instance=rifa)

    for field in form.fields.values():
        field.disabled = True

    return render(request, 'dashboard/raffles/form.html', {
        'form': form,
        'action': 'detail',
        'rifa': rifa
    })

@login_required
def raffle_delete(request, pk):
    rifa = get_object_or_404(Raffle, pk=pk, user=request.user)
    if request.method == 'POST':
        rifa.delete()
        return redirect('raffle_list_admin')
    return render(request, 'dashboard/raffles/confirm_delete.html', {'rifa': rifa})

def raffle_list_public(request):
    rifas = Raffle.objects.filter(status='active')
    return render(request, 'dashboard/raffles/public_list.html', {'rifas': rifas})
