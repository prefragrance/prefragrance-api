from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        user = super().save_user(request, user, form, False)
        user.nickname = data.get("nickname")
        user.name = data.get("name")
        user.age = data.get("age")
        user.gender = data.get("gender")
        user.save()
        return user
