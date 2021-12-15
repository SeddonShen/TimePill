from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse, JsonResponse
from login.models import User
from django.db.models import Q
import django.utils.timezone as timezone
import json


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
    print(request.method,art_id)
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
                    print('hello0')
                    if key_flag:
                        print('hello1')
                        title = req["title"]
                        content = req["content"]
                        square_open = req["square_open"]
                        '''更新数据'''
                        article = Article.objects.get(id=art_id)
                        article.title = title
                        article.content = content
                        article.square_open = square_open
                        article.save()
                        print('hello2')
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
                                'status': article.status, 'author': article.author_id.name}
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
                                    'status': article.status, 'author': article.author_id.name}
                else:
                    article_dict = {'id': article.id, 'title': '未解封的胶囊', 'content': '耐心等待',
                                    'status': article.status, 'author': article.author_id.name}
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
                if(article.status):
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
