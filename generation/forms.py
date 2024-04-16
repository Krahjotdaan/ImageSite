from django import forms


class StyleForm(forms.Form):

    style = forms.ChoiceField(
        label='Выберите стиль*',
        required=True,
        choices=(('Гиперреализм', 'Гиперреализм'), 
                 ('Аниме', 'Аниме')),
        widget=forms.Select(attrs={'id': 'style'})
    )

    frm = forms.ChoiceField(
        label='Выберите соотношение сторон*',
        required=True,
        choices=(('16:9', '16:9'), 
                 ('1:1', '1:1')),
        widget=forms.Select(attrs={'id': 'frm'})
    )

    quality = forms.ChoiceField(
        label='Выберите качество*',
        required=True,
        choices=(('Низкое', 'Низкое'), 
                 ('Среднее', 'Среднее'),
                 ('Высокое', 'Высокое')),
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
        label='Что делает? Какие предметы использует?',
        max_length=100,
        widget=forms.Textarea(attrs={"id": "action"})
    )

    place = forms.CharField(
        label='Где находится? Какие детали?',
        max_length=100,
        widget=forms.Textarea(attrs={"id": "avoidance"})
    ) 

    avoidance = forms.CharField(
        label='Чего постараться избежать?',
        max_length=100,
        widget=forms.Textarea(attrs={"id": "avoidance"})
    ) 
