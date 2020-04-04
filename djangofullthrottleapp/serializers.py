from rest_framework import serializers
from djangofullthrottleapp.models import Users, ActivityPeriods


class ActivityPeriodSerializer(serializers.ModelSerializer):
   
    
    start_time = serializers.DateTimeField(format="%b %d %Y %H:%M%p",source='ap_starttime')
    end_time = serializers.DateTimeField(format="%b %d %Y %H:%M%p",source='ap_endtime')
    
    class Meta:
        model = ActivityPeriods
        fields = ('start_time', 'end_time')


class UserSerializer(serializers.ModelSerializer):

     id = serializers.CharField(source='u_id')
     real_name = serializers.CharField(source='u_name')
     tz=serializers.CharField(source='u_timezone')

     activity_periods = ActivityPeriodSerializer(many=True)
     

     class Meta:
         model = Users
         fields = ('id', 'real_name', 'tz', 'activity_periods')

