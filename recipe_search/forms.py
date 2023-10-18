from django import forms


class FormTopics(forms.Form):
    name = forms.CharField(required=False)
    labels = {
        "name": "test"
    }
