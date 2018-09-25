"""
导入规则：
1.先引入python自带的库
换行
2.引入第三方
换行
3.引入自定义的
"""
from django import forms
from django.contrib.auth.models import User


class UserForm(forms.Form):
    """
    校验注册信息
    """
    # username = forms.CharField(required=True)
    # password = forms.CharField(required=True)
    # password2 = forms.CharField(required=True)

    username = forms.CharField(required=True,
                               max_length=5,
                               min_length=2,
                               error_messages={
                                   'required': '用户必填',
                                   'max_length': '长度不能超过5位',
                                   'min_length': '长度不能少于2位'
                               })
    password = forms.CharField(required=True,
                               min_length=6,
                               error_messages={
                                   'required': '密码必填',
                                   'min_length': '长度不能少于6位'
                               })
    password2 = forms.CharField(required=True,
                                min_length=6,
                                error_messages={
                                    'required': '密码必填',
                                    'min_length': '长度不能少于6位'
                                })

    def clean(self):
        # 校验用户名是否已经注册过
        user = User.objects.filter(username=self.cleaned_data.get('username'))
        if user:
            # 已经被注册
            raise forms.ValidationError({'username': '用户名已经存在，请直接登录'})
            pass
        else:
            # 没有被注册
            pass
        # 校验密码和确认密码是否相同
        if self.cleaned_data.get('password') != self.cleaned_data.get('password2'):
            raise forms.ValidationError({'password2': '两次密码不一致'})
        return self.cleaned_data


class CheckUserForm(forms.Form):
    username = forms.CharField(required=True,
                               max_length=5,
                               min_length=2,
                               error_messages={
                                   'required': '用户必填',
                                   'max_length': '长度不能超过5位',
                                   'min_length': '长度不能少于2位'
                               })
    password = forms.CharField(required=True,
                               min_length=6,
                               error_messages={
                                   'required': '密码必填',
                                   'min_length': '长度不能少于6位'
                               })

    def clean(self):
        # 校验用户名是否已经注册过
        user = User.objects.filter(username=self.cleaned_data.get('username')).first()
        if user:
            # 已经被注册
            pass
        else:
            # 没有被注册
            raise forms.ValidationError({'username': '用户名不存在！'})

        # # 校验密码和确认密码是否相同
        # if self.cleaned_data.get('password') == user.password:
        #     pass
        # else:
        #     raise forms.ValidationError({'password': '密码错误'})
        #
        # return self.cleaned_data
