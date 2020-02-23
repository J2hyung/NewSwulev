from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.

def login(request):

    return render(request, 'login.html')

def main(request):

    board = Board.objects.all
    lecture = Lecture.objects.all
    

    return render(request, 'main.html', {'board':board, 'lecture':lecture})

def detail(request, lectureid):

    current_lecture = get_object_or_404(Lecture, pk=lectureid)
    boards = Board.objects.filter(lecture = current_lecture)

    return render(request, 'detail.html', {'current_lecture' : current_lecture, 'boards': boards})

def mypage(request):
    return render(request, 'mypage.html')

def signup(request):
    #user1 = Lecture.objects.raw('select * from swuapp_lecture')[0]
    if request.method == 'POST':
            user_id = request.POST['id']
            user_pw = request.POST['passwd']
            user = User(userid=user_id, userpw=user_pw)
            user.save()
            if user is not None:
                return redirect('main')
            else:
                return render(request, 'signup.html', {'error': 'ID 또는 PW가 올바르지 않습니다.'})
    else:
        return render(request, 'signup.html')
    # user1 = Lecture.objects.raw('select * from swuapp_lecture')[0]
    # return render(request, 'login.html', {'user1':user1})
