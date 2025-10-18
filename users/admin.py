from django.contrib import admin
from users.models import CustomUser
from django.contrib.auth.admin import UserAdmin
from users.forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    # Formulários para adicionar e alterar usuários
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    # Campos exibidos no admin
    list_display = ('email', 'username', 'name', 'birth_date', 'is_staff', 'is_active',)
    list_filter = ('is_staff','is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Informações Pessoais', {'fields': ('name', 'description', 'birth_date',)}),
        ('Permissões', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions',)}),
        ('Datas Importantes', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'name', 'password1', 'password2',
                       'description', 'birth_date', 'is_staff', 'is_active',),
        }),
    )
    search_fields = ('email', 'username', 'name',)
    ordering = ('-date_joined', 'email',)

# Registro no admin
admin.site.register(CustomUser, CustomUserAdmin)
