from django.core.management.base import BaseCommand
from django.utils import timezone
from user_act.models import User, ActivityPeriod
import datetime

class Command(BaseCommand):
    help = 'custom command --- used to insert new user activity'

    def add_arguments(self, parser):
        parser.add_argument('user_id', type=str, help='id of user')
        parser.add_argument('user_name', type=str, help='name of user')
        parser.add_argument('user_tz', type=str, help='tz of user')
        parser.add_argument('start_date', type=str, help='start date of user_activity')
        parser.add_argument('end_date', type=str, help='end date of user_activity')

    def handle(self, *args, **kwargs):
        user_id = kwargs['user_id']
        user_name = kwargs['user_name']
        user_tz = kwargs['user_tz']
        try:
            start_date = datetime.datetime.strptime(kwargs['start_date'], format)
            end_date = datetime.datetime.strptime(kwargs['end_date'], format)
        except:
            self.stdout.write("Error! Date values should be string of this format ----- Mar 01 2020 11:11AM")
            return
        existing_user = User.objects.filter(user_id=user_id)
        format = '%b %d %Y %I:%M%p'

        if (existing_user):
            record = existing_user[0].activities.create(start_date=start_date,end_date=end_date)
            record.save()
            self.stdout.write("----------------------- User Exists! Activity updated!")
        else:
            start_date = datetime.datetime.strptime(kwargs['start_date'], format)
            end_date = datetime.datetime.strptime(kwargs['end_date'], format)
            new_user = User(user_id=user_id, user_name=user_name, user_tz=user_tz)
            new_user.save()
            new_act = new_user.activities.create(start_date=start_date,end_date=end_date)
            new_act.save()        
            self.stdout.write("----------------------- New User! Activity inserted!")
