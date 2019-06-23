from django import forms

from users.models import User


class UserLoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=20, min_length=5,
                               error_messages={
                                   'required': '用户名必填',
                                   'max_length': '用户名不能超过20个字符',
                                   'min_length': '用户名不能少于5个字符'
                               })
    password = forms.CharField(required=True, min_length=8, max_length=20,
                               error_messages={
                                   'required': '密码必填',
                                   'max_length': '密码不能超过20个字符',
                                   'min_length': '密码不能少于5个字符'
                               })

    def clean(self):
        user = User.objects.filter(username=self.cleaned_data.get('username')).first()
        if not user:
            raise forms.ValidationError({'username': '未注册的用户名'})
        return self.cleaned_data


class UserRegisterForm(forms.Form):
    """
    用户注册验证表单
    """
    username = forms.CharField(required=True, max_length=20, min_length=5,
                               error_messages={
                                   'required': '用户名必填',
                                   'max_length': '用户名不能超过20个字符',
                                   'min_length': '用户名不能少于5个字符'
                               })
    password = forms.CharField(required=True, min_length=8, max_length=20,
                               error_messages={
                                   'required': '密码必填',
                                   'max_length': '密码不能超过20个字符',
                                   'min_length': '密码不能少于5个字符'
                               })
    cpassword = forms.CharField(required=True, min_length=8, max_length=20,
                                error_messages={
                                    'required': '确认密码必填',
                                    'max_length': '确认密码不能超过20个字符',
                                    'min_length': '确认密码不能少于5个字符'
                                })
    email = forms.CharField(required=True, error_messages={
                                'required': '邮箱必填'
                            })
    allow = forms.BooleanField(required=True,
                               error_messages={
                                   'required': '协议必选'
                               })

    # def clean(self):
    #     if self.cleaned_data['password'] != self.cleaned_data['cpassword']:
    #         raise forms.ValidationError({'password': '两次密码不一致'})
    #
    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     user = User.objects.filter(username=username).first()
    #     if user:
    #         raise forms.ValidationError({'username': '用户名重复'})
    #     else:
    #         return username

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        cpassword = self.cleaned_data.get('cpassword')
        user = User.objects.filter(username=username)
        if user:
            raise forms.ValidationError({'username': '用户名重复'})
        if password != cpassword:
            raise forms.ValidationError({'cpassword': '两次密码不一致'})

        return self.cleaned_data
