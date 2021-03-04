from django.shortcuts import render


# Create your views here.
def test_render(request):
    return render(request, 'DoorSystem/test.html')


def index_render(reqeust):
    return render(reqeust, 'DoorSystem/index.html')
