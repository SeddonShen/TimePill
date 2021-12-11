from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse, JsonResponse
from login.models import User
import json


def add_article(request):
    if request.method == "POST":
        if request.session.get('is_login', None):
            user_id = request.session.get('user_id', None)
            print(user_id)
            print(request.session.get('user_name', None))
            req = json.loads(request.body)
            print(req)
            key_flag = req.get("title") and req.get("content") and len(req) == 2
            # 判断请求体是否正确
            if key_flag:
                title = req["title"]
                content = req["content"]
                '''插入数据'''
                add_art = Article(title=title, content=content, status="alive", author_id_id=user_id)
                add_art.save()
                return JsonResponse({"status": "200", "msg": "publish article success."})
            else:
                return JsonResponse({"status": "400", "msg": "please check param."})
        else:
            return JsonResponse({"status": "404", "msg": "please log in."})
    # 查询所有文章和状态
    if request.method == "GET":
        articles = []
        query_art = Article.objects.all()
        for article in query_art:
            article_dict = {'id': article.id, 'title': article.title, 'content': article.content,
                            'status': article.status, 'author': article.author_id.name}
            articles.append(article_dict)
        return JsonResponse({"status": "200", "articles": articles, "msg": "query articles success."}, safe=False)


def modify_article(request, art_id):
    if request.session.get('is_login', None):
        print(request.session.get('user_id', None))
        print(request.session.get('user_name', None))
        if request.method == "POST":
            req = json.loads(request.body)
            try:
                article = Article.objects.get(id=art_id)
                key_flag = req.get("title") and req.get("content") and len(req) == 2
                if key_flag:
                    title = req["title"]
                    content = req["content"]
                    '''更新数据'''
                    article = Article.objects.get(id=art_id)
                    article.title = title
                    article.content = content
                    article.save()
                    return JsonResponse({"status": "200", "msg": "modify article success."})
            except Article.DoesNotExist:
                return JsonResponse({"status": "300", "msg": "article is not exists,fail to modify."})

        # 删除文章
        if request.method == "DELETE":
            # print(art_id)
            # return JsonResponse({"status": "200", "msg": "delete article success."})
            try:
                art = Article.objects.get(id=art_id)
                art.delete()
                return JsonResponse({"status": "200", "msg": "delete article success."})
            except Article.DoesNotExist:
                return JsonResponse({"status": "300", "msg": "article is not exists,fail to delete."})

    else:
        return JsonResponse({"status": "404", "msg": "please log in."})