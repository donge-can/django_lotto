from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import GuessNumbers
from .forms import PostForm
from django.shortcuts import render, redirect

def index(request):
    # site_1\lotto\templates\lotto\default.html

    # site_1\member\templates\index.html (127.0.0.1:8000/member)
    # site_1\products\template\index.html (127.0.0.1:8000/products)

    # 장고는 html 파일을 다 합쳐서 보관함(위의 html을 개별적으로)
    # templates\index.html, index.html, index.html
    # 하지만 합쳐서 보관할 때, 이름이 겹치기 때문에
    # 폴더를 새롭게 만든 후 html 을 만들어준다.

    # site_1\member\templates\member\index.html (127.0.0.1:8000/member)
    # site_1\products\template\products\index.html (127.0.0.1:8000/products)
    # lottos = GuessNumbers.objects.get(name = '로또 번호 1번') # DB에 저장된 GuessNumbers 객체 가져오기
    lottos = GuessNumbers.objects.all()

    return render(request, 'lotto/default.html', {'lottos':lottos})
    # render : 지정한 html 파일 가져와서, 사용자의 request 데이터를 눈 앞에
    # 보여주는 그런 역할

def hello(request):
    return HttpResponse("<h1 style ='color:red;'> Hello, world!</h1>")

def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            lotto = form.save(commit = False)
            lotto.generate()
            return redirect('index')
    else:
        form = PostForm()

        return render(request, 'lotto/form.html', {'form':form})



def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(pk = lottokey)
    return render(request, 'lotto/detail.html', {"lotto": lotto})
