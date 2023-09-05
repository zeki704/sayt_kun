from django.shortcuts import render, HttpResponse

from app1.models import Category, News, Contact, Comments
import requests as red

from app1.services import get_all_ctg, search_new


# Create your views here.

def valyuta():
    url = 'https://cbu.uz/oz/arkhiv-kursov-valyut/json/'

    data = {

    }

    headers = {

    }
    response = red.get(url , headers=headers, data=data)

    return response.json()

# def ctgs():
#     return Category.objects.all()


def ctg(requests, _id):
    try:
        ctg = Category.objects.get(id=_id)
    except:
        ctx = {
            "error": True,
            "ctgs": get_all_ctg()
        }
        return render(requests, 'category.html', ctx)

    ctg_news = News.objects.filter(ctg=ctg).order_by('-id')

    ctx = {
        "ctgs": get_all_ctg(),
        "ctg": ctg,
        "ctg_news": ctg_news[1:4],
        "ctg_new1": ctg_news[5:9],
        "val": valyuta()

    }
    if len(ctg_news) > 0:
        ctx['big'] = ctg_news[0]
    return render(requests, 'category.html', ctx)


def cnt(requests):
    ctx = {
        "ctgs": get_all_ctg(),
        "val": valyuta()

    }

    if requests.POST:
        ism = requests.POST.get('ism')
        sms = requests.POST.get('sms')
        tel = requests.POST.get('tel')
        contact = Contact.objects.create(ism=ism, tel=tel, massage=sms)
        ctx['contact'] = contact

    return render(requests, 'contact.html', ctx)


def index(requests):


    news = News.objects.all().order_by('-pk')


    sqlctgs= get_all_ctg()


    sport_ctg = Category.objects.get(name='Sport')
    sport_news = News.objects.filter(ctg=sport_ctg)

    uzb_ctg = Category.objects.get(name="O'zbekiston")
    uzb_new = News.objects.filter(ctg=uzb_ctg)

    biznes_ctg = Category.objects.get(name="Biznes")
    biznes_news = News.objects.filter(ctg=biznes_ctg)

    econo_ctg = Category.objects.get(name="Iqtisodiyot")
    econo_news = News.objects.filter(ctg=econo_ctg)

    chet_ctg = Category.objects.get(name="Xorijiy")
    chet_news = News.objects.filter(ctg=chet_ctg)



    ctx = {
        "ctgs": sqlctgs,

        "big": news[0],

        "act_news": news[1],

        "pop_news": news[4:8],

        "list_new": news[8:15],

        "sport": sport_news,

        "sport_head": sport_news[:3],

        "sport_head1": sport_news[4:7],

        "uzb": uzb_new[:2],

        "uzb1": uzb_new[2:],

        "uzb2": uzb_new,

        "biznes": biznes_news,

        "iqt": econo_news,

        "xorij": chet_news,

        "val": valyuta()

    }

    return render(requests, 'index.html', ctx)


def srch(requests):

    savol = requests.GET.get('s', None)
    news = search_new(savol)

    print(news)


    ctx = {
        "val": valyuta(),
        "ctgs": get_all_ctg(),
        "news" : news,
        "len" : len(news),
        "savol": savol

    }
    return render(requests, 'search.html', ctx)


def view(requests, pk):
    new = News.objects.filter(id=pk).first()
    chet_ctg = Category.objects.get(name="Xorijiy")
    chet_news = News.objects.filter(ctg=chet_ctg)
    if not new:
        return render(requests, 'view.html', {
            "ctgs": get_all_ctg(),
            "error": True,
            "val":valyuta()
        })

    new.view = new.view + 1
    new.save()
    if requests.POST:
        user = requests.POST.get('user', )
        izoh = requests.POST.get('comment')

        cnt = Comments.objects.create(user=user, comment=izoh, new=new)
        cnt.save()

    comments = Comments.objects.filter(new=new, trash=False).order_by('-pk')

    ctx = {
        "ctgs": get_all_ctg(),
        "new": new,
        "new1": chet_news,
        "val": valyuta(),
        "comments": comments,
        "len_comment": len(comments),

    }
    return render(requests, 'view.html', ctx)


# def alljson(requests):
#     file =open('./all.json', 'rb')
#     js = file.read()
#     file.close()
#
#
#     return HttpResponse(js)