# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from models import User
from forms import AdminUserChangeForm, AdminUserCreationForm
from visits.models import Subscription


class SubscriptionInline(admin.StackedInline):
    model = Subscription
    readonly_fields = ['expire_date']
    extra = 1
    max_num = 1
    fk_name = 'user'
    inline_classes = ('grp-collapse grp-open',)


class CustomUserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = AdminUserChangeForm
    add_form = AdminUserCreationForm

    inlines = [SubscriptionInline]

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'is_superuser', 'is_active', 'get_full_name')
    list_filter = ('is_superuser',)
    fieldsets = (
        ('', {
            'fields': ('first_name', 'last_name', 'gender',
                       'pastimes', 'url'),
        }),
        ('Permissions', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('is_superuser', 'is_active', 'is_staff', 'groups'),
        }),
        ('Important dates', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('last_login',),
        }),
        ('Other', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('email', 'password'),
        })
    )
    add_fieldsets = (
        (None, {
            'fields': ('email', 'first_name', 'last_name', 'url',
                       'pastimes', 'comment', 'password1', 'password2')
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

    def get_queryset(self, request):
        qs = super(CustomUserAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(is_superuser=False)
        return qs

    def get_readonly_fields(self, request, obj=None):
        fields = self.readonly_fields
        if not request.user.is_superuser:
            fields += ('is_active', 'is_staff', 'is_superuser', 'groups')
        return fields

    def get_formsets(self, request, obj=None):
        for inline in self.get_inline_instances(request, obj):
            # hide PurchaseInline in the edit view
            if isinstance(inline, SubscriptionInline) and obj is None:
                yield inline.get_formset(request, obj)



# Now register the new UserAdmin...
admin.site.register(User, CustomUserAdmin)
# ... and, since we're not using Django's builtin permissions,
# unregister the Group model from admin.
#admin.site.unregister(Group)
