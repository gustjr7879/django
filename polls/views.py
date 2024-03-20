from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hyunskki Django Test")
#간단한 뷰를 설정했다. 뷰를 호출하려면 이와 연결된 url이 있어야되는데 이를 위해서 URLconf가 사용된다.
#URL conf를 생성하려면 urls.py라는 파일을 만들어야한다.