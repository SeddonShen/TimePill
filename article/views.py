from django.shortcuts import render, redirect
from .models import Article
from .models import Comment
from django.http import HttpResponse, JsonResponse
from login.models import User
from django.db.models import Q
import django.utils.timezone as timezone
import json
from django.conf import settings


def add_article(request):
    if request.method == "POST":
        if request.session.get('is_login', None):
            user_id = request.session.get('user_id', None)
            print(user_id)
            print(request.session.get('user_name', None))
            req = json.loads(request.body)
            print(req)
            print(len(req))
            if req.get("diary_type") == "primary":
                key_flag = req.get("title") and req.get("content") and len(req) == 4
                if key_flag:
                    title = req["title"]
                    content = req["content"]
                    square_open = req["square_open"]
                    # expire_time = req["expire_time"]
                    diary_type = req["diary_type"]
                    status = True
                    add_art = Article(
                        title=title,
                        content=content,
                        square_open=square_open,
                        # expire_time=expire_time,
                        status=status,
                        author_id_id=user_id,
                        diary_type=diary_type,
                        # add_date=timezone.now,
                        # mod_date=timezone.now
                    )
                    add_art.save()
                    return JsonResponse({"status": "200", "msg": "publish article success."})
                else:
                    return JsonResponse({"status": "400", "msg": "please check param."})
            else:
                key_flag = req.get("title") and req.get("content") and len(req) == 5
                if key_flag:
                    title = req["title"]
                    content = req["content"]
                    square_open = req["square_open"]
                    expire_time = req["expire_time"]
                    diary_type = req["diary_type"]
                    '''插入数据'''
                    status = False
                    add_art = Article(
                        title=title,
                        content=content,
                        square_open=square_open,
                        expire_time=expire_time,
                        status=status,
                        author_id_id=user_id,
                        diary_type=diary_type,
                        # add_date=timezone.now,
                        # mod_date=timezone.now
                    )
                    add_art.save()
                    return JsonResponse({"status": "200", "msg": "publish pill success."})
                else:
                    return JsonResponse({"status": "400", "msg": "please check param."})
            # 判断请求体是否正确
        else:
            return JsonResponse({"status": "404", "msg": "please log in."})
    # 查询所有文章和状态
    if request.method == "GET":
        if request.session.get('is_login', None):
            user_id = request.session.get('user_id', None)
            print(user_id)
            print(request.session.get('user_name', None))
            articles = []
            query_art = Article.objects.filter(Q(square_open=True) & Q(status=True))
            # query_art = Article.objects.all()
            for article in query_art:
                article_dict = {'id': article.id, 'title': article.title, 'content': article.content,
                                'status': article.status, 'author': article.author_id.name,
                                'diary_type': article.diary_type}
                articles.append(article_dict)
            return JsonResponse({"status": "200", "articles": articles, "msg": "query articles success."}, safe=False)
        else:
            return JsonResponse({"status": "404", "msg": "please log in."})
    return JsonResponse({"status": "405", "msg": "unknown error."})


def modify_article(request, art_id):
    print('ssd', request.method)
    print('modify_article')
    print(request.method, art_id)
    if request.method == "POST":
        if request.session.get('is_login', None):
            user_id = request.session.get('user_id', None)
            print(user_id)
            print(request.session.get('user_name', None))
            req = json.loads(request.body)
            try:
                article = Article.objects.get(id=art_id)
                key_flag = req.get("title") and req.get("content") and len(req) == 4
                print(len(req))
                if user_id == article.author_id.id:
                    # print('hello0')
                    if key_flag:
                        # print('hello1')
                        title = req["title"]
                        content = req["content"]
                        square_open = req["square_open"]
                        '''更新数据'''
                        article = Article.objects.get(id=art_id)
                        if article.diary_type == 'pill':
                            return JsonResponse({"status": "409", "msg": "is your pill."})
                        article.title = title
                        article.content = content
                        article.square_open = square_open
                        article.save()
                        # print('hello2')
                        return JsonResponse({"status": "200", "msg": "modify article success."})
                else:
                    return JsonResponse({"status": "406", "msg": "not your article."})
            except Article.DoesNotExist:
                return JsonResponse({"status": "300", "msg": "article is not exists,fail to modify."})
        else:
            return JsonResponse({"status": "404", "msg": "please log in."})

    # 删除文章
    if request.method == "DELETE":
        if request.session.get('is_login', None):
            user_id = request.session.get('user_id', None)
            print(user_id)
            print(request.session.get('user_name', None))
            # print(art_id)
            # return JsonResponse({"status": "200", "msg": "delete article success."})
            try:
                art = Article.objects.get(id=art_id)
                if user_id == art.author_id.id:
                    art.delete()
                    return JsonResponse({"status": "200", "msg": "delete article success."})
                else:
                    return JsonResponse({"status": "406", "msg": "not your article."})
            except Article.DoesNotExist:
                return JsonResponse({"status": "300", "msg": "article is not exists,fail to delete."})
        else:
            return JsonResponse({"status": "404", "msg": "please log in."})
    if request.method == "GET":
        if request.session.get('is_login', None):
            user_id = request.session.get('user_id', None)
            print(user_id)
            article = Article.objects.get(id=art_id)
            if user_id == article.author_id.id:
                print(request.session.get('user_name', None))
                article_dict = {'id': article.id, 'title': article.title, 'content': article.content,
                                'status': article.status, 'author': article.author_id.name}
                return JsonResponse({"status": "200", "article": article_dict, "msg": "list article detail success."},
                                    safe=False)
            else:
                return JsonResponse({"status": "406", "msg": "not your article."})

        else:
            return JsonResponse({"status": "404", "msg": "please log in."})
    return JsonResponse({"status": "405", "msg": "unknown error."})


def myarticles(request):
    # 查询所有文章和状态
    if request.method == "GET":
        if request.session.get('is_login', None):
            user_id = request.session.get('user_id', None)
            print(user_id)
            print(request.session.get('user_name', None))
            articles = []
            query_art = Article.objects.filter(Q(author_id=user_id) & Q(diary_type='primary'))
            # print(query_art.__dict__)
            for article in query_art:
                article_dict = {'id': article.id, 'title': article.title, 'content': article.content,
                                'status': article.status, 'author': article.author_id.name,
                                'diary_type': article.diary_type}
                articles.append(article_dict)
            return JsonResponse({"status": "200", "articles": articles, "msg": "query user articles success."},
                                safe=False)
        else:
            return JsonResponse({"status": "404", "msg": "please log in."})
    return JsonResponse({"status": "405", "msg": "unknown error."})


def mypills(request):
    # 查询所有文章和状态
    if request.method == "GET":
        if request.session.get('is_login', None):
            user_id = request.session.get('user_id', None)
            print(user_id)
            print(request.session.get('user_name', None))
            articles = []
            query_art = Article.objects.filter(Q(author_id=user_id) & Q(diary_type='pill'))
            # print(query_art.__dict__)
            for article in query_art:
                if (article.status):
                    article_dict = {'id': article.id, 'title': article.title, 'content': article.content,
                                    'status': article.status, 'author': article.author_id.name,
                                    'diary_type': article.diary_type}
                else:
                    article_dict = {'id': article.id, 'title': '未解封的胶囊', 'content': '耐心等待',
                                    'status': article.status, 'author': article.author_id.name,
                                    'diary_type': article.diary_type}
                articles.append(article_dict)
            return JsonResponse({"status": "200", "articles": articles, "msg": "query user articles success."},
                                safe=False)
        else:
            return JsonResponse({"status": "404", "msg": "please log in."})
    return JsonResponse({"status": "405", "msg": "unknown error."})


def articledetail(request, art_id):
    print('method:', request.method)
    # GET请求获取信息
    if request.method == "GET":
        if request.session.get('is_login', None):
            user_id = request.session.get('user_id', None)
            print(user_id)
            article = Article.objects.get(id=art_id)
            if user_id == article.author_id.id:
                print(request.session.get('user_name', None))
                article_dict = {'id': article.id,
                                'title': article.title,
                                'content': article.content,
                                'square_open': article.square_open,
                                'expire_time': article.expire_time,
                                'status': article.status,
                                'diary_type': article.diary_type,
                                'author': article.author_id.name,
                                'add_date': article.add_date,
                                'mod_date': article.mod_date
                                }
                return JsonResponse({"status": "200", "article": article_dict, "msg": "list pill detail success."},
                                    safe=False)
            else:
                return JsonResponse({"status": "406", "msg": "not your pill."})

        else:
            return JsonResponse({"status": "404", "msg": "please log in."})
    return JsonResponse({"status": "405", "msg": "unknown error."})


def pilldetail(request, art_id):
    print('method:', request.method)
    # GET请求获取信息
    if request.method == "GET":
        if request.session.get('is_login', None):
            user_id = request.session.get('user_id', None)
            print(user_id)
            article = Article.objects.get(id=art_id)
            if user_id == article.author_id.id:
                print(request.session.get('user_name', None))
                if (article.status):
                    article_dict = {'id': article.id,
                                    'title': article.title,
                                    'content': article.content,
                                    'square_open': article.square_open,
                                    'expire_time': article.expire_time,
                                    'status': article.status,
                                    'diary_type': article.diary_type,
                                    'author': article.author_id.name,
                                    'add_date': article.add_date,
                                    'mod_date': article.mod_date
                                    }
                else:
                    article_dict = {'id': article.id,
                                    'title': article.title,
                                    'content': '暂未解封',
                                    'square_open': article.square_open,
                                    'expire_time': article.expire_time,
                                    'status': article.status,
                                    'diary_type': article.diary_type,
                                    'author': article.author_id.name,
                                    'add_date': article.add_date,
                                    'mod_date': article.mod_date
                                    }
                return JsonResponse({"status": "200", "article": article_dict, "msg": "list pill detail success."},
                                    safe=False)
            else:
                return JsonResponse({"status": "406", "msg": "not your pill."})

        else:
            return JsonResponse({"status": "404", "msg": "please log in."})
    return JsonResponse({"status": "405", "msg": "unknown error."})


# 邮件发送
def send_mail(email):
    from django.core.mail import EmailMultiAlternatives
    subject = '您有时间胶囊到期啦'

    text_content = '''感谢使用l时间胶囊\
                        如果你看到这条消息，说明你的邮箱服务器不提供HTML链接功能，请联系管理员！'''

    html_content = '''
                <p>感谢使用时间胶囊！</p>
                <p>请回到时间胶囊TimePill官网查看到期的胶囊信息！</p>
                    '''
    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def pron(request):
    # 查询所有文章和状态
    if request.method == "GET":
        '''查找数据'''
        query_art = Article.objects.filter(Q(diary_type='pill') & Q(status=False) & Q(expire_time__lt=timezone.now()))
        articles = []
        for article in query_art:
            # is pill and status is false
            # print(article.__dict__)
            # print(article.author_id.email)
            print(article.expire_time)
            send_mail(article.author_id.email)
            article.status = True
            article.save()
        # now = timezone.now()
        # print(now)
        # article.status = True
        # article.save()
        return JsonResponse({"status": "200", "msg": "pron task run success."})
    return JsonResponse({"status": "405", "msg": "unknown error."})


def show_comment(request, art_id):
    print('Method', request.method)
    print('modify_article')
    print(request.method, art_id)

    if request.method == "GET":
        user_id = request.session.get('user_id', None)
        print(user_id)
        # comments = Comment.objects.filter(article=Article.objects.get(id=art_id))
        comments = Comment.objects.filter(article=art_id)
        print(comments.__dict__)
        comments_show = []
        for comment in comments:
            if comment.pre_comment is None:
                comment_dict = {
                    'id': comment.id,
                    'comment_content': comment.comment_content,
                    'comment_author': comment.comment_author.name,
                    'comment_time': comment.comment_time,
                    'pre_comment': None
                }
            else:
                comment_dict = {
                    'id': comment.id,
                    'comment_content': comment.comment_content,
                    'comment_author': comment.comment_author.name,
                    'comment_time': comment.comment_time,
                    'pre_comment': comment.pre_comment.id
                }
            comments_show.append(comment_dict)
            # print(comment.id,
            #       comment.article.id,
            #       comment.comment_content,
            #       comment.comment_author,
            #       comment.comment_time,
            #       comment.pre_comment
            # )
        return JsonResponse({"status": "200", "comments": comments_show, "msg": "query success."})
    return JsonResponse({"status": "405", "msg": "unknown error."})


def add_comment(request, art_id):
    if request.method == "POST":
        # if True:
        if request.session.get('is_login', None):
            # user_id = 1
            user_id = request.session.get('user_id', None)
            print(user_id)
            # print(request.session.get('user_name', None))
            req = json.loads(request.body)
            print(req)
            print(len(req))
            comment_content = req["comment_content"]
            article = Article.objects.get(id=art_id)
            comment_author = article.author_id
            pre_comment = req["pre_comment"]
            print('ssd ssd', pre_comment)
            if pre_comment is None:
                print("父评论")
            else:
                pre_comment = Comment.objects.get(id=pre_comment)
            add_com = Comment(
                article=article,
                comment_content=comment_content,
                comment_author=comment_author,
                pre_comment=pre_comment,
                comment_time=timezone.now
            )
            add_com.save()
            return JsonResponse({"status": "200", "msg": "publish comment success."})
            # 判断请求体是否正确
        else:
            return JsonResponse({"status": "404", "msg": "please log in."})

    return JsonResponse({"status": "405", "msg": "unknown error."})


def modify_comment(request, comm_id):
    print('ssd', request.method)
    print('modify_comment')
    print(request.method, comm_id)
    # 删除Comment
    if request.method == "DELETE":
        # if True:
        if request.session.get('is_login', None):
            user_id = request.session.get('user_id', None)
            # user_id = 1
            print(user_id)
            print(request.session.get('user_name', None))
            try:
                com = Comment.objects.get(id=comm_id)
                print(user_id, com.comment_author.id)
                if user_id == com.comment_author.id:
                    com.delete()
                    return JsonResponse({"status": "200", "msg": "delete comment success."})
                else:
                    return JsonResponse({"status": "406", "msg": "not your comment."})
            except Article.DoesNotExist:
                return JsonResponse({"status": "300", "msg": "comment is not exists,fail to delete."})
        else:
            return JsonResponse({"status": "404", "msg": "please log in."})

    return JsonResponse({"status": "405", "msg": "unknown error."})