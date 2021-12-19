from django.shortcuts import render
from .check import Check

rounds_history = {}
round = 0

# Create your views here.
def index_view(request):
    return render(request, 'index.html')


def game_view(request):
    global context
    if request.method == 'GET':
        return render(request, 'game.html')
    else:
        try:
            context = ''
            user_numbers = list(map(int, request.POST.get('user_numbers').split()))
            check = Check(user_numbers)
            error = check.validation()
            if error:
                context += error
            else:
                result = check.get_result()
                context += result

        except ValueError:
            context += 'The value should be integers'

        global round
        round += 1
        rounds_history[round] = context

        print(rounds_history)
        return render(request, 'game.html', {'context': context})


def history_view(request):
    return render(request, 'history.html', {'rounds_history': rounds_history})
