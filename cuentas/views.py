from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import REDIRECT_FIELD_NAME, authenticate, login, get_user_model
# Create your views here.
from .forms import UserRegisterForm, UserEditForm
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404


User = get_user_model()


@login_required
def home(request):
    return render(request, template_name='cuentas/home.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'cuentas/register.html', {'form': form})
    else:
        form = UserRegisterForm()
    return render(request, 'cuentas/register.html', {'form': form})


@login_required
def edit_user(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'cuentas/editar.html', {'form': form})
    else:
        form = UserEditForm(instance=request.user)
    return render(request, 'cuentas/editar.html', {'form': form})


def es_tipo_admin(user):
    if user.tipo == 'admin':
        return True
    else:
        return False


@login_required
def admin_edit_user(request, pk):
    # chequeamos en la vista el tipo de usuario
    if request.user.tipo == 'admin':
        # si tiene autorización, procedemos como 
        # normalemnte lo hacemos con los formularios
        if request.method == 'POST':
            user = get_object_or_404(User, pk=pk) # esto es solo para manejar el error
            form = UserEditForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                return redirect('home')
            else:
                return render(request, 'cuentas/editar.html', {'form': form})
        else:
            try:
                user = User.objects.get(pk=pk)
                form = UserEditForm(instance=user)
            except ObjectDoesNotExist:
                form = UserEditForm()
        return render(request, 'cuentas/editar.html', {'form': form})
    else:
        # si no tiene permiso, mostramos mensaje de no autorizado
        return redirect('perm_error')


@user_passes_test(es_tipo_admin)
def admin_edit_user2(request, pk):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=User.objects.get(pk=pk))
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'cuentas/editar.html', {'form': form})
    else:
        try:
            user = User.objects.get(pk=pk)
            form = UserEditForm(instance=user)
        except ObjectDoesNotExist:
            form = UserEditForm()
    return render(request, 'cuentas/editar.html', {'form': form})
    

def permission_error(request):
    return render(request=request, template_name='cuentas/no_autorizado.html')
