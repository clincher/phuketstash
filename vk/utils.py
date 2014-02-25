# -*- coding: utf-8 -*-


from vkontakte_api.utils import api_call

friends_ids = api_call('friends.get', **{'fields': 'nickname', 'count': 1})#,domain,sex,bdate,city,country,timezone,photo_50,photo_100,photo_200_orig,has_mobile,contacts,education,online,relation,last_seen,status,can_write_private_message,can_see_all_posts,can_post,universities'})

for friend in friends_ids:
    print friend
    #break