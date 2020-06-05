# Create your views here.

from django.http import JsonResponse
from user_act.models import User
import json
from collections import OrderedDict

def get_user_data(request):
    result = OrderedDict({"ok": True})
    users = User.objects.all()
    user_list = []
    for user in users:
        cur_user_info = OrderedDict()
        cur_user_info['id'] = user.user_id
        cur_user_info['real_name'] = user.user_name
        cur_user_info['tz'] = user.user_tz
        act_list = []
        all_acts = user.activities.all()
        for act in all_acts:
            act_list.append(OrderedDict({'start_date':act.start_date.strftime('%b %d %Y %I:%M%p'),'end_date':act.end_date.strftime('%b %d %Y %I:%M%p')}))			
        cur_user_info['activity_periods'] = act_list
        user_list.append(cur_user_info)
    result['members'] = user_list
    return JsonResponse(result)
    
    
