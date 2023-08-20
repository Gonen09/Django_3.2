from django import forms


class ArticleForm (forms.Form):

    title = forms.CharField()
    content = forms.CharField()

    # recupera un campo limpio (html parseado) especifico, title
    """
    def clean_title(self):

        cleaned_data = self.cleaned_data  # dictionary form form
        print(cleaned_data)
        title = cleaned_data.get('title')

        if title.lower().strip() == "the office":
            raise forms.ValidationError("Este titulo ya esta ingresado")

        print("title", title)

        return title
    """

    def clean(self):

        cleaned_data = self.cleaned_data
        print("all data", cleaned_data)
        title = cleaned_data.get('title')
        content = cleaned_data.get("content")

        if title.lower().strip() == "the office":
            self.add_error('title', 'Este titulo ya esta ingresado.')

        if "office" in content or "office" in title.lower():
            self.add_error('content', 'Office cannot be in content')
            raise forms.ValidationError("Office is not allowed")

        return cleaned_data
