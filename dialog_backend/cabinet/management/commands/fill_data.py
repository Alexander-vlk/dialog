from datetime import timedelta
import random

from django.core.management import BaseCommand
from django.utils import timezone

from auth_service.models import AppUser
from data_tracking.models import Medication, MedicationTake


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = AppUser.objects.get(username='petrov')

        MedicationTake.objects.filter(user=user).delete()

        metformin = Medication.objects.get(name='Метформин')
        novorapid = Medication.objects.get(name='Новорапид')
        levemir = Medication.objects.get(name='Левемир')

        start_date = timezone.now() - timedelta(days=60)
        end_date = timezone.now()

        current_date = start_date

        created = 0

        while current_date <= end_date:
            # Небольшой шанс пропустить день
            if random.random() < 0.05:
                current_date += timedelta(days=1)
                continue

            MedicationTake.objects.create(
                user=user,
                medication=metformin,
                dose=1000,
                taken_at=current_date.replace(
                    hour=8,
                    minute=0,
                    second=0,
                    microsecond=0,
                ),
            )
            created += 1

            MedicationTake.objects.create(
                user=user,
                medication=metformin,
                dose=1000,
                taken_at=current_date.replace(
                    hour=20,
                    minute=0,
                    second=0,
                    microsecond=0,
                ),
            )
            created += 1

            MedicationTake.objects.create(
                user=user,
                medication=novorapid,
                dose=random.choice([4, 5, 6, 7]),
                taken_at=current_date.replace(
                    hour=8,
                    minute=0,
                    second=0,
                    microsecond=0,
                ),
            )
            created += 1

            MedicationTake.objects.create(
                user=user,
                medication=novorapid,
                dose=random.choice([5, 6, 7, 8]),
                taken_at=current_date.replace(
                    hour=13,
                    minute=0,
                    second=0,
                    microsecond=0,
                ),
            )
            created += 1

            MedicationTake.objects.create(
                user=user,
                medication=novorapid,
                dose=random.choice([4, 5, 6, 7]),
                taken_at=current_date.replace(
                    hour=19,
                    minute=0,
                    second=0,
                    microsecond=0,
                ),
            )
            created += 1

            MedicationTake.objects.create(
                user=user,
                medication=levemir,
                dose=random.choice([12, 14, 16]),
                taken_at=current_date.replace(
                    hour=22,
                    minute=0,
                    second=0,
                    microsecond=0,
                ),
            )
            created += 1

            current_date += timedelta(days=1)

        self.stdout.write(
            self.style.SUCCESS(
                f'Создано записей о приеме лекарств: {created}'
            )
        )