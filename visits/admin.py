# -*- coding: utf-8 -*-
from django.contrib import admin

from models import Visit, Subscription, Plan, Payment
from forms import EmptyPermittedFormSet


class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


class AdministrantedModelAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        if not obj.administrant:
            obj.administrant = request.user
        super(AdministrantedModelAdmin, self).save_model(
            request, obj, form, change)


class PaymentAdmin(AdministrantedModelAdmin):
    list_display = ('subscription', 'value', 'pay_date')


class PaymentInline(admin.StackedInline):
    model = Payment
    extra = 1
    readonly_fields = ('pay_date', 'administrant')
    formset = EmptyPermittedFormSet

    inline_classes = ('grp-collapse grp-open',)


class VisitInline(admin.StackedInline):
    model = Payment
    extra = 1
    readonly_fields = ('administrant')
    formset = EmptyPermittedFormSet

    inline_classes = ('grp-collapse grp-open',)


class SubscriptionAdmin(AdministrantedModelAdmin):
    list_display = ('user', 'credit', 'administrant', 'plan')
    inlines = [PaymentInline, VisitInline]
    readonly_fields = ['administrant']

    def save_formset(self, request, form, formset, change):
        if isinstance(formset, PaymentInlineFormSet):
            for form in formset.forms:
                form.instance.administrant = request.user
        super(SubscriptionAdmin, self).save_formset(
            request, form, formset, change)


class VisitAdmin(AdministrantedModelAdmin):
    pass


admin.site.register(Visit, VisitAdmin)
admin.site.register(Plan, PlanAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
