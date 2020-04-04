from django.core.management.base import BaseCommand
from django.utils import timezone
from djangofullthrottleapp.models import Users, ActivityPeriods
from faker import Faker
import datetime
from django.utils import timezone

class Command(BaseCommand):
    help = 'Seed Databsae with Uers and Activties seed-db 5 or seed-db 5 --logs 20 '

    def add_arguments(self, parser):
        parser.add_argument('uc', type=int, help='Indicates the number of users to be created')
        parser.add_argument('-ac', '--logs', type=int, help='Indicates the number of activities per User')

    def handle(self, *args, **kwargs):
        # Add Users first
        # a if a < b else b 
        user_count = 2 if kwargs['uc'] == None else kwargs['uc']
        activity_count =5 if kwargs['logs'] == None else kwargs['logs']

        print(user_count)
        print(activity_count)

        faker = Faker()
        # for each command it will insert two Users and Activities
        for _ in range(user_count):
            uuid_Temp = faker.uuid4()
            uid = uuid_Temp[:8].upper()
            user_obj = Users(
                u_id= uid,
                u_name = faker.first_name() + ' ' + faker.last_name(),
                u_timezone =faker.timezone()
            )
            user_obj.save()

            user_added = Users.objects.get(u_id=uid)

            for _ in range(activity_count):
                startTime = faker.date_time_this_month()
                user_activities = ActivityPeriods(
                    ap_u_id = user_added,
                    ap_starttime = startTime,
                    ap_endtime = startTime + datetime.timedelta(minutes = 10)
                )
                user_activities.save()
            self.stdout.write("***User Inserted***")
        




            
        