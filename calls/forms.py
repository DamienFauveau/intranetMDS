from django import forms

from users.forms import ModelFormWithSubmit
from .models import Call, CallTag


class NewCallForm(ModelFormWithSubmit):

    tags = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=CallTag.objects.all(),
        )

    class Meta:
        model = Call
        fields = ('title', 'call_category', 'customer', 'tags', 'content', 'solved', )


class NewCallCustomerForm(ModelFormWithSubmit):

    tags = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=CallTag.objects.all(),
        )

    class Meta:
        model = Call
        fields = ('title', 'call_category', 'tags', 'content', )

class CallFormAssign(ModelFormWithSubmit):

    tags = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=CallTag.objects.all(),
        )

    class Meta:
        model = Call
        fields = ('customer', )