from django.http import HttpResponse

# ver vxvdebi view-ebs :D ამას შეეშვი საერთოდ polls
def index(request):
    return HttpResponse("okay, its working, i guess ")