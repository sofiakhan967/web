from django.http import HttpResponse
from django.shortcuts import render,HttpResponse
from . models import Post
import requests
from newsapi import NewsApiClient
from django.core.paginator import Paginator
# Create your views here.
def home(request):
    return render(request,'home.html')





def blogs(request):
    details=Post.objects.all().order_by('-date')
    p=Paginator(details,3)
    page_number=request.GET.get('page')
    try:
        page_obj=p.get_page(page_number)
    except PageNotAnInteger:
        page_obj=p.page(1)
    except EmptyPage:
        page_obj=p.page(p.num_pages)
    context={'page_obj':page_obj}    
    return render(request,'blogs.html',context)


def blog(request,slug):
    data=Post.objects.filter(slug=slug).first()
    context={'data':data}
    return render(request,'blog.html',context)


def about(request):
    return render(request,'about.html')    


def contact(request):
    return render(request,'contact.html')        

def news(request):
     newsapi=NewsApiClient(api_key='16a47766bd39463ca9d97545bfc37725')
     all_articles= newsapi.get_everything(q='general',
                                            domains='ndtv.com',
                                            language='en',
                                            page_size=80)
    
     b=all_articles['articles']

     p=Paginator(b,3)
     page_number=request.GET.get('page')
     try:
         page_obj=p.get_page(page_number)
     except PageNotAnInteger:
         page_obj=p.page(1)
     except EmptyPage:
         page_obj=p.page(p.num_pages)
     context={'page_obj':page_obj}                                           

                                          
    # url=f'https://newsapi.org/v2/top-headlines?country=in&category=technology&science&apiKey={api_key}'
   #  res=requests.get(url)
     #data=res.json()
     
     #articles =data['articles']
     #context={'b':b}
     #print(data)
     return render(request,'news.html',context)


def cryptoprice(request):
    
    return render(request,'Cryptoprice.html')    