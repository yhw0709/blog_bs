
from django import forms

from users.models import Users


class UserForm(forms.Form):
    username = forms.CharField(required=True)
    userpwd = forms.CharField(required=True)
    userpwd2 = forms.CharField(required=True)

    # def clean(self):
    #     # 校验用户名是否已经注册过
    #     user = Users.objects.filter(username=self.cleaned_data.get('username')).first()
    #     if user:
    #         # 已经被注册
    #         raise forms.ValidationError({'username': '用户名重复！'})
    #
    #     else:
    #         # 没有被注册
    #         pass
    #     if self.cleaned_data.get('password') != self.cleaned_data.get('password2'):
    #         raise forms.ValidationError({'password2': '两次密码不一致'})
    #     return self.cleaned_data


class ArticleForm(forms.Form):
    title = forms.CharField(required=True)
    keywords = forms.CharField(required=False)
    describe = forms.CharField(required=False)
    content = forms.CharField(required=False)
