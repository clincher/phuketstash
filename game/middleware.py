# -*- coding: utf-8 -*-
from datetime import date

from game.models import Game


class GameMiddleware(object):
    def process_request(self, request):
        try:
            request.game = Game.objects.filter(
                is_active=True, start_date__gte=date.today())[0]
        except Game.DoesNotExist:
            request.game = None
