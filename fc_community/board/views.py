from django.shortcuts import render
from django.http import Http404
from fcuser.models import Fcuser
from .models import Board
from .forms import BoardForm


def board_detail(request,pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        # django에서 제공해주는 기능 에러 발생
        raise Http404('게시글을 찾을 수 없습니다.')

    return render(request,'board_detail.html',{'board':board})

def board_write(request):
    # 사용자 로그인 유무 확인
    if request.session.get('user'):
        
        return redirect('/fcuser/login')

    if request.method == 'POST':
        form = BoardFrom(request.POST)
        if form.ist_valid():
            user_id = request.session.get('user')
            fcuser = Fcuser.objects.get(pk=user_id)

            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleand_data['contents']
            board.write = fcuser
            board.save()

            return redirect('/board/list/')
    else:
        form = BoardForm()
    
    return render(request, 'board_write.html',{'form':form})


def board_list(request):

    boards = Board.objects.all().order_by('-id')

    return render(request,'board_list.html',{'boards':boards})