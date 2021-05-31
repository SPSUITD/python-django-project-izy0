from .models import Users
from django.forms import ModelForm, TextInput, Textarea,Select

ROOM_CHOISE=[
('0','Только главная'),
('1','Хром'),
('2','Погода'),
]

class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = ['name','message','room']

        widgets = {
            "name": TextInput(attrs={
                'placeholder':'Имя',
                'class':'form-name'
            }),
            "message": Textarea(attrs={
                'placeholder':'Сообщение',
                'class':'form-message'
            }),
            "room": Select(
            choices=ROOM_CHOISE

            )
            # "room": Select(choices=ROOM_CHOISE)
        }
