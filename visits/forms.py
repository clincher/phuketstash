# -*- coding: utf-8 -*-

from django.forms.models import BaseInlineFormSet


class PaymentInlineFormSet(BaseInlineFormSet):
    """
    Generates an inline formset that is required
    """

    def _construct_form(self, i, **kwargs):
        """
        Override the method to change the form attribute empty_permitted
        """
        form = super(PaymentInlineFormSet, self)._construct_form(
            i, **kwargs)
        form.empty_permitted = True
        return form