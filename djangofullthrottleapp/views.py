from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from djangofullthrottleapp.models import Users, ActivityPeriods
from djangofullthrottleapp.serializers import UserSerializer
# Create your views here.

def todo(request):
    usr = Users.objects.all()
    return render(request, 'index.html',{'user':usr})
def activitylogs(request,id):
    print("***************************")
    activitylogs = ActivityPeriods.objects.filter(ap_u_id = id)
    print("&&&&&&&&&&&&&&&&",activitylogs)
    return render(request, 'activity.html',{'act':activitylogs})


def users(request):
    usersCollection = Users.objects.all()
    serializer = UserSerializer(usersCollection, many=True)
    members = serializer.data
    response = {
        "ok": True,
        "members": members
    }
    return JsonResponse(response, safe=False)

# Create your views here.
