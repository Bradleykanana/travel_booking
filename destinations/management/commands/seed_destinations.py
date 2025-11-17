from django.core.management.base import BaseCommand
from destinations.models import Destination

class Command(BaseCommand):
    help = 'Seed the database with required Nordic destinations.'

    def handle(self, *args, **options):
        destinations = [
            {'name': 'Norway', 'description': 'Fjords, Viking history, northern lights.'},
            {'name': 'Sweden', 'description': 'Forests, archipelagos, Stockholm culture.'},
            {'name': 'Denmark', 'description': 'Castles, hygge, Copenhagen.'},
            {'name': 'Finland', 'description': 'Saunas, Lapland, aurora borealis.'},
            {'name': 'Iceland', 'description': 'Geysers, volcanoes, waterfalls.'},
            {'name': 'Estonia', 'description': 'Tallinn, medieval towers, beaches.'},
        ]
        for dest in destinations:
            obj, created = Destination.objects.get_or_create(name=dest['name'], defaults={'description': dest['description']})
            if created:
                self.stdout.write(self.style.SUCCESS(f"Added destination: {dest['name']}"))
            else:
                self.stdout.write(self.style.WARNING(f"Destination already exists: {dest['name']}"))
