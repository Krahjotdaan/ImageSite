from django import forms


class StyleForm(forms.Form):

    number_of_images = forms.IntegerField(
        label='Сколько картинок требуется(макс. 10)',
        max_value=10,
        min_value=1,
        required=True,
        widget=forms.NumberInput(attrs={'id': 'number_of_images'})
    )

    style = forms.ChoiceField(
        label='Выберите стиль',
        required=True,
        choices=(('Гиперреализм', 'Гиперреализм'), 
                 ('Аниме', 'Аниме')),
        widget=forms.Select(attrs={'id': 'style'})
    )

    format = forms.ChoiceField(
        label='Выберите соотношение сторон',
        required=True,
        choices=(('16:9', '16:9'), 
                 ('1:1', '1:1')),
        widget=forms.Select(attrs={'id': 'format'})
    )

    quality = forms.ChoiceField(
        label='Выберите качество',
        required=True,
        choices=(('Низкое', 'Низкое'), 
                 ('Среднее', 'Среднее'),
                 ('Высокое', 'Высокое')),
        widget=forms.Select(attrs={'id': 'quality'})
    )


class CharacterForm(forms.Form):
    pass