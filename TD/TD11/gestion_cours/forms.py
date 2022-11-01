from django.forms import ModelForm, ModelMultipleChoiceField, Form


class IntervenantSelectForm(Form):
    pass


def getIntervenantSelectFormUsingKey(key):
    return type(f"{key.upper()}IntervenantSelectForm", (IntervenantSelectForm,),
                {f"intervenants_{key}": ModelMultipleChoiceField(queryset=Intervenant.objects)})


class CoursForm(ModelForm):
    class Meta:
        model = Cours
        fields = "__all__"
        exclude = ["etudiants"]
        labels = {}