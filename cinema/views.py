from datetime import date

from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse

from cinema.forms import *
from cinema.models import *
from django.http import HttpResponse

# Create your views here.


def welcome(request):
    return render(request, 'welcome.html')


def index(request):
    user_id = request.GET.get('user_id', None)
    return render(request, 'index.html', {'user_id': user_id})


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def show_movies(request):
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies})


def show_movie_info(request, movie_id):
    movie = Movie.objects.filter(pk=movie_id).first()
    return render(request, 'movie_info.html', {'movie': movie})


def add_movies(request):
    movies = maoyanTop100()
    print(movies)
    for movie in movies:
        Movie.objects.create(movie_id=movie[0], movie_name=movie[2], starring=movie[3], release_datetime=movie[4],
                             score=movie[5], img=movie[1])
    return HttpResponse('100条电影数据添加成功！')


# 爬取猫眼Top100电影数据
def maoyanTop100():
    import requests
    from bs4 import BeautifulSoup
    urls = ['https://maoyan.com/board/4?offset={}'.format(i) for i in range(0, 100, 10)]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
        'Cookie': 'mta=222214055.1603977692790.1605667197555.1605667216476.84; uuid_n_v=v1; uuid=A8B9B7F019E911EB9D95490677AB0FF651894580EC0942CDA95D1D5CD9BEE13D; _lxsdk_cuid=175748545b3c8-0d6dc6ca2c5b4d-3c634103-144000-175748545b3c8; _lxsdk=A8B9B7F019E911EB9D95490677AB0FF651894580EC0942CDA95D1D5CD9BEE13D; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; __mta=222214055.1603977692790.1605606918555.1605606922430.33; _csrf=e50e37a20022fed414d7d479d61fb627bd72f61c2be692b12edc786fdb91dea2; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1604192299,1605603303,1605612340,1605665922; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1605667216; _lxsdk_s=175d9259dda-76-0bc-84b%7C%7C32'
    }
    id = 0
    movies_info = []
    for url in urls:
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, 'lxml')
        movies = soup.find_all('dd')

        for movie in movies:
            id += 1
            imgurl = movie.find('img', class_='board-img')['data-src']
            info = movie.find('div', class_='movie-item-info')
            name = info.find('p', class_='name').get_text()
            star = info.find('p', class_='star').get_text().replace('主演：', '').strip()
            release_time = info.find('p', class_='releasetime').get_text().replace('上映时间：', '').strip()
            score = movie.find('p', class_='score').get_text()
            imgaddr = 'uploads/' + imgurl.split('/')[4].split('.')[0] + '.jpg'
            with open(f'static/{imgaddr}', 'wb') as f:
                imgcontent = requests.get(imgurl, headers=headers).content
                f.write(imgcontent)
            movies_info.append([id, imgaddr, name, star, release_time, score])
    return movies_info


def handle_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        User.objects.create(
            name=form.data['name'],
            sex=form.data['gender'] == 'male',
            age=form.data['age'],
            phone=form.data['contact'],
            username=form.data['username'],
            password=form.data['password'],
            register_date=date.today()
        )
        user = User.objects.filter(username=form.data['username']).first()
        messages.success(request, '注册成功！')
        return redirect(reverse('index') + f'?user_id={user.user_id}')
    else:
        messages.error(request, '注册失败！')
    return redirect(reverse('welcome'))


def handle_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = form.data['username']
        password = form.data['password']
        user = User.objects.filter(username=username,password=password).first()
        if user is not None:
            messages.success(request, '登录成功！')
            return redirect(reverse('index') + f'?user_id={user.user_id}')
        else:
            messages.error(request, '用户名或密码错误，登录失败！')
    return redirect(reverse('welcome'))
