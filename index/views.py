from django.shortcuts import render
from captcha import CreateCaptcha
from django import forms
from django.shortcuts import HttpResponse
# Create your views here.
code = None


class ContactForm(forms.Form):
    input_code = forms.CharField()


def index(request):
    global code
    x = CreateCaptcha()
    image = x.gen_code()
    image.save('index/static/code.png')
    code = x.text
    print(code)
    form = ContactForm()
    return render(request, 'index.html', {'form': form})


def check(request):
    global code
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            input_code = form.cleaned_data['input_code']
            if input_code == code:
                return HttpResponse('验证成功! 正确验证码是: %s ' % code)
            else:
                return HttpResponse('验证失败！ 正确验证码是: %s,输入为 %s' % (code, input_code))
    return HttpResponse('Something is wrong! Please return<a href="127.0.0.1:8000">主页</a>')
