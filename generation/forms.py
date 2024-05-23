from django import forms


class StyleForm(forms.Form):

    style = forms.ChoiceField(
        label='Выберите стиль*',
        required=True,
        choices=(
                    ('Гиперреализм', 'Гиперреализм'), 
                    ('Аниме', 'Аниме'),
                    ('Детская книжная иллюстрация', 'Детская книжная иллюстрация'),
                    ('Фэнтези', 'Фэнтези'),
                    ('Комиксный', 'Комиксный'),
                    ('Кубизм', 'Кубизм'),
                ),
        widget=forms.Select(attrs={'id': 'style'})
    )

    frm = forms.ChoiceField(
        label='Выберите соотношение сторон*',
        required=True,
        choices=(
                ('1:1', '1:1'),
                ('16:9', '16:9'),
                ('9:16', '9:16'),
                ('3:4', '3:4'),
                ('4:3', '4:3'),
            ),
        widget=forms.Select(attrs={'id': 'frm'})
    )

    quality = forms.ChoiceField(
        label='Выберите разрешение*',
        required=True,
        choices=(
                    ('Низкое', 'Низкое'), 
                    ('Среднее', 'Среднее'),
                    ('Высокое', 'Высокое'),
                    ('Ультра', 'Ультра')
                ),
        widget=forms.Select(attrs={'id': 'quality'})
    )


class CharacterForm(forms.Form):
    
    character = forms.CharField(
        label='Кто изображён? Как выглядит?*',
        max_length=100,
        required=True,
        widget=forms.Textarea(attrs={"id": "character"})
    )

    action = forms.CharField(
        label='Что делает? Какие предметы использует?*',
        max_length=100,
        widget=forms.Textarea(attrs={"id": "action"})
    )

    place = forms.CharField(
        label='Где находится? Какие детали?*',
        max_length=100,
        widget=forms.Textarea(attrs={"id": "avoidance"})
    ) 

    avoidance = forms.CharField(
        label='Чего постараться избежать?*',
        max_length=100,
        widget=forms.Textarea(attrs={"id": "avoidance"})
    ) 
