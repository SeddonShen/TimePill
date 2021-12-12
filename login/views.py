from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, redirect
from .models import User, ConfirmString
from .forms import UserForm, RegisterForm
import hashlib
import datetime
from django.conf import settings
from django.http import JsonResponse


# 密码加密
def hash_code(s, salt='mysite'):
    h = hashlib.sha3_256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()


# 邮件确认码
def make_confirm_string(user):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    code = hash_code(user.name, now)
    # 创建用户及哈希值
    ConfirmString.objects.create(code=code, user=user, )
    return code


# 邮件发送
def send_mail(email, code):
    from django.core.mail import EmailMultiAlternatives
    subject = '来自时间胶囊TimePill的注册确认邮件'

    text_content = '''感谢注册l时间胶囊\
                        如果你看到这条消息，说明你的邮箱服务器不提供HTML链接功能，请联系管理员！'''

    html_content = '''
                <p>感谢注册时间胶囊！</p>
                <p><a href="http://{}/confirm/?code={}" target=blank>请点击此处链接进行确认验证</a></p>
                    <p>请尽快点击上述链接完成注册确认！</p>
                    <p>此链接有效期为{}天！</p>
                    '''.format('127.0.0.1:8000', code, settings.CONFIRM_DAYS)

    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


# 主页
def index(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    return render(request, 'login/index.html')


def login(request):
    if request.session.get('is_login', None):  # 不允许重复登录
        # return redirect('/index/')
        # print(request.session.__dict__)
        user_id = request.session.get('user_id', None)
        user_name = request.session.get('user_name', None)
        session_key = request.session.session_key
        # 'is_login': True, 'user_id': 9, 'user_name': 'seddon'}}
        response = JsonResponse({'request': 'Have Login', 'user_id': user_id, 'user_name': user_name, 'sessionid':session_key})
        response["Access-Control-Allow-Origin"] = "http://127.0.0.1:8010"

        response["Access-Control-Allow-Credentials"] = "true"

        response["Access-Control-Allow-Methods"] = "*"
        # response["Access-Control-Expose-Headers"] = ""
        response["Access-Control-Allow-Headers"] = "*"

        return response
    # date = {'flag': date_flag, 'msg': date_msg}
    if request.method == 'POST':
        login_form = UserForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            # 用户名字符合法性验证
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            try:
                user = User.objects.get(name=username)
            except:
                message = '用户名不存在！'
                # return render(request,'login/login.html',locals())
                return JsonResponse({'request': message})
            # 判断邮件验证
            if not user.has_confirmed:
                message = '该用户还未经过邮件确认！'
                return JsonResponse({'request': message})
                # return render(request, 'login/login.html', locals())
            if user.password == hash_code(password):
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                session_key = request.session.session_key
                # return redirect('/index/')
                # return JsonResponse(
                #     {'request': 'Have Login', 'user_id': user_id, 'user_name': user_name, 'sessionid': session_key})
                return JsonResponse({'request': 'Login ok', 'user_id': user.id, 'user_name': user.name, 'sessionid': session_key})
            else:
                message = '密码不正确！'
                return JsonResponse({'request': message})
                # return render(request,'login/login.html',locals())

        else:
            return JsonResponse({'request': '未知错误'})
            # return render(request, 'login/login.html', locals())
    login_form = UserForm()
    return JsonResponse({'request': '请输入账密'})
    # return render(request, 'login/login.html',locals())


def register(request):

    if request.session.get('is_login', None):  # 不允许重复登录
        user_id = request.session.get('user_id', None)
        user_name = request.session.get('user_name', None)
        session_key = request.session.session_key
        # 'is_login': True, 'user_id': 9, 'user_name': 'seddon'}}
        response = JsonResponse({'request': 'Have Login', 'user_id': user_id, 'user_name': user_name, 'sessionid':session_key})
        response["Access-Control-Allow-Origin"] = "http://127.0.0.1:8010"
        response["Access-Control-Allow-Credentials"] = "true"
        response["Access-Control-Allow-Methods"] = "*"
        # response["Access-Control-Expose-Headers"] = ""
        response["Access-Control-Allow-Headers"] = "*"

        return response

    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        print(register_form.is_valid())
        print(register_form.__dict__)
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            email = register_form.cleaned_data.get('email')
            sex = register_form.cleaned_data.get('sex')
            # 判断用户是否存在
            same_name_user = User.objects.filter(name=username)
            if same_name_user:
                message = '用户名已经存在'
                # return render(request, 'login/register.html', locals())
                return JsonResponse({'request': message})
            same_email_user = User.objects.filter(email=email)
            if same_email_user:
                message = '该邮箱已经被注册了！'
                # return render(request, 'login/register.html', locals())
                return JsonResponse({'request': message})
            new_user = User()
            new_user.name = username
            new_user.password = hash_code(password1)
            new_user.email = email
            new_user.sex = sex
            new_user.save()
            code = make_confirm_string(new_user)
            send_mail(email, code)
            return JsonResponse({'request': 'reg ok'})
            # return redirect('/login/')
        else:
            return render(request, 'login/register.html', locals())
    register_form = RegisterForm()
    # return render(request, 'login/register.html', locals())
    return JsonResponse({'request': 'unknown error'})

def user_confirm(request):
    code = request.GET.get('code', None)
    message = ''
    try:
        confirm = ConfirmString.objects.get(code=code)
    except:
        message = '无效的确认需求'
        return render(request, '/login/confirm.html', locals())

    c_time = confirm.c_time
    now = datetime.datetime.now()
    if now > c_time + datetime.timedelta(settings.CONFIRM_DAYS):
        confirm.user.delete()
        message = '您的邮件验证已经过期！请重新注册！'
        return render(request, 'login/confirm.html', locals())

    else:
        confirm.user.has_confirmed = True
        confirm.user.save()
        confirm.delete()
        message = '感谢确认，请使用账户登录！'
        return render(request, 'login/confirm.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/login/")

    request.session.flush()
    # 或者使用下面的方法清除缓存数据
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/login/")
