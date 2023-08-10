from django.forms.widgets import Select

class CustomSelectWithPlaceholder(Select):
    def __init__(self, placeholder=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.placeholder = placeholder

    def create_option(self, *args, **kwargs):
        option = super().create_option(*args, **kwargs)
        if option['value'] == '':
            option['attrs']['disabled'] = True
            option['attrs']['selected'] = True
            if self.placeholder:
                option['label'] = self.placeholder
        return option