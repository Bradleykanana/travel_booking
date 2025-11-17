from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from reviews.models import Review
from destinations.models import Destination
import random
from django.utils import timezone

class Command(BaseCommand):
    help = 'Seed the database with sample reviews from random users and destinations.'

    def handle(self, *args, **kwargs):
        # Delete all existing reviews before seeding new ones
        Review.objects.all().delete()
        usernames = [
            'odin', 'freya', 'thor', 'loki', 'sigurd', 'astrid', 'bjorn', 'helga', 'ivar', 'ragnar',
            'leif', 'gunhild', 'magnus', 'sigrid', 'egil', 'solveig', 'tove', 'ulfr', 'hilda', 'roald'
        ]
        for uname in usernames:
            if not User.objects.filter(username=uname).exists():
                User.objects.create_user(username=uname, password='nordictrail')

        users = list(User.objects.filter(username__in=usernames))
        destinations = list(Destination.objects.all())
        comments = [
            "From the moment we arrived, the staff made us feel like true Vikings. The fjord kayaking was exhilarating, and the evening feast in the longhouse was a highlight. Every detail was authentic and memorable.",
            "I traveled with my family and we were blown away by the breathtaking scenery and the immersive Norse storytelling. Our guide, Astrid, was knowledgeable and passionate. We left with new friends and unforgettable memories.",
            "The trail exploration was both challenging and rewarding. I especially loved the historical reenactments and the opportunity to learn about Viking culture firsthand. The food was hearty and delicious, and the accommodations were cozy.",
            "Nordic Trails exceeded my expectations. The attention to detail, from the themed activities to the personalized service, made this trip stand out. I recommend it to anyone seeking adventure and a taste of history.",
            "As a solo traveler, I felt welcomed and included in every activity. The group dinners were lively, and the hiking routes offered stunning views. I can't wait to return and experience more!"
        ]
        ratings = [5, 5, 4, 5, 5]

        for i in range(5):
            user = random.choice(users)
            destination = random.choice(destinations) if destinations else None
            Review.objects.create(
                user=user,
                destination=destination,
                rating=ratings[i],
                comment=comments[i],
                created_at=timezone.now() - timezone.timedelta(days=random.randint(0, 60)),
            )
        self.stdout.write(self.style.SUCCESS('5 detailed sample reviews seeded successfully.'))
