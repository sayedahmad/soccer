from django.shortcuts import render, HttpResponse
from django.views import View
from match.models import Match
from datetime import date, timedelta
from django.utils import timezone
# Create your views here.


class HomeView(View):

    def get(self, request, *args, **kwargs):

        some_day_last_week = timezone.now().date() - timedelta(days=7)
        monday_of_last_week = some_day_last_week - \
            timedelta(days=(some_day_last_week.isocalendar()[2] - 1))
        monday_of_this_week = monday_of_last_week + timedelta(days=7)
        last_week_matchs = Match.objects.filter(match_date__gte=monday_of_last_week, match_date__lt=monday_of_this_week).all()
        context = {
            'matchs': last_week_matchs,
        }
        return render(request, "soccer_game/home.html", context)
