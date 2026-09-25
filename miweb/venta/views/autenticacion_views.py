from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Error de usuario o clave')
        else:
            messages.error(request, 'Ingrese los datos')
    return render(request, 'venta/autenticacion/login.html')


@login_required
def home(request):
    user_permissions = {
        'can_manage_clients': (
            request.user.is_superuser or
            request.user.groups.filter(name='grp_cliente').exists() or
            request.user.has_perm('venta.add_cliente')
        ),
        'can_manage_products': (
            request.user.is_superuser or
            request.user.groups.filter(name='grp_producto').exists()
        ),
        'can_manage_providers': (
            request.user.is_superuser or
            request.user.groups.filter(name='grp_proveedor').exists()
        ),
        'can_manage_sales': (
            request.user.is_superuser or
            request.user.groups.filter(name='grp_venta').exists()
        ),
        'is_admin': request.user.is_superuser
    }

    context = {
        'user_permissions': user_permissions,
        'user': request.user
    }
    return render(request, 'venta/autenticacion/home.html', context)


def user_logout(request):
    logout(request)
    messages.success(request, 'Sesion cerrada correctamente')
    return redirect('login')