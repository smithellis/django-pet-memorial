from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Donation, Memorial, Hospital, CustomUser, Profile, Fund, Donation

class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False
    can_change = False
    verbose_name = 'Detail'
    verbose_name_plural = 'Details'

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username','email','is_staff','is_active','is_superuser']
    inlines = (ProfileInLine,)

class CustomMemorialAdmin(admin.ModelAdmin):
    list_display = ['hospital', 'create_date', 'status', 'pet_name']
    list_filter = ['hospital', 'create_date', 'status', 'pet_name']
    search_fields = ['hospital', 'create_date', 'status', 'pet_name']

class CustomHospitalAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'state']
    search_fields = ['name', 'phone', 'state']

class CustomDonationAdmin(admin.ModelAdmin):
    list_display = ['hospital', 'date', 'payment_status']
    search_fields = ['hospital', 'date', 'payment_status']

class CustomFundsAdmin(admin.ModelAdmin):
    list_display = ['fund_name', 'description']
    search_fields = ['fund_name', 'description']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Memorial, CustomMemorialAdmin)
admin.site.register(Hospital, CustomHospitalAdmin)
admin.site.register(Fund, CustomFundsAdmin)
admin.site.register(Donation, CustomDonationAdmin)