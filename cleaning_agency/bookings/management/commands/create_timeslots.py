from django.core.management.base import BaseCommand
from django.utils import timezone
from bookings.models import TimeSlot
from datetime import time

class Command(BaseCommand):
    help = 'Create TimeSlot instances for each hour from 6 AM to 10 PM.'

    def handle(self, *args, **kwargs):
        times = [time(hour=hour) for hour in range(6, 22)]  # 6 AM to 10 PM
        for t in times:
            TimeSlot.objects.get_or_create(time=t)
        self.stdout.write(self.style.SUCCESS('Successfully created TimeSlot instances'))