from django import forms

# Forms de ejemplo:
 
# class ProfesorForm(forms.Form):
#     name = forms.CharField(max_length=40, min_length=3, label='Nombre')
#     last_name = forms.CharField(max_length=40, label='Apellido')
#     email = forms.EmailField(label='Correo electrónico')
#     profession = forms.CharField(max_length=40, label='Profesión')
    
# class HomeworkForm(forms.Form):
#     name = forms.CharField(max_length=40, min_length=3, label='Nombre de la Entrega')
#     due_date = forms.DateField(
#         label='Fecha de Entrega',
#         widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'})
#     )
#     is_delivered = forms.BooleanField(label='Entregado', required=False)

class ConductorForm(forms.Form):
    full_name = forms.CharField(max_length=40, min_length=3, label="Nombre completo")
    day_of_birth = forms.CharField(max_length=40, 
                                   label='Fecha de nacimiento',
                                   widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'})
                                   )
    email = forms.EmailField(label="Correo electrónico")
    has_license = forms.BooleanField(label='Licencia aprobada', required=False)
    
class LicenciaForm(forms.Form):
    number = forms.CharField(max_length=40, min_length=5, label="Numero de licencia" )
    year = forms.IntegerField(label="Año de licencia")
    
class AutoForm(forms.Form):
    brand = forms.CharField(max_length=40, min_length=2, label="Marca")
    model = forms.CharField(max_length=40, min_length=3, label="Modelo")
    year = forms.IntegerField(label="Año del vehiculo")