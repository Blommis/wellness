from django import forms


class RecipeForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
