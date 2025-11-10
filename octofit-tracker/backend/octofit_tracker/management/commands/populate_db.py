from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Users
        users = [
            User.objects.create(email='tony@stark.com', name='Tony Stark', team=marvel.name),
            User.objects.create(email='steve@rogers.com', name='Steve Rogers', team=marvel.name),
            User.objects.create(email='bruce@wayne.com', name='Bruce Wayne', team=dc.name),
            User.objects.create(email='clark@kent.com', name='Clark Kent', team=dc.name),
        ]

        # Activities
        Activity.objects.create(user='Tony Stark', activity_type='Running', duration=30, date=date.today())
        Activity.objects.create(user='Steve Rogers', activity_type='Cycling', duration=45, date=date.today())
        Activity.objects.create(user='Bruce Wayne', activity_type='Swimming', duration=60, date=date.today())
        Activity.objects.create(user='Clark Kent', activity_type='Flying', duration=120, date=date.today())

        # Leaderboard
        Leaderboard.objects.create(user='Tony Stark', points=100)
        Leaderboard.objects.create(user='Steve Rogers', points=90)
        Leaderboard.objects.create(user='Bruce Wayne', points=110)
        Leaderboard.objects.create(user='Clark Kent', points=120)

        # Workouts
        Workout.objects.create(name='Super Strength', description='Strength workout for heroes', difficulty='Hard')
        Workout.objects.create(name='Speed Run', description='Speed workout for heroes', difficulty='Medium')
        Workout.objects.create(name='Flight Training', description='Flight workout for heroes', difficulty='Hard')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
