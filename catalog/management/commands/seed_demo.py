from django.core.management.base import BaseCommand
from catalog.models import Autor, Recurs


class Command(BaseCommand):
    help = 'Carrega dades de prova per a l\'API'

    def handle(self, *args, **options):
        if Autor.objects.exists() or Recurs.objects.exists():
            self.stdout.write(self.style.WARNING('Ja hi ha dades. No s\'han duplicat.'))
            return

        a1 = Autor.objects.create(
            nom='Anna', cognoms='Serra', email='anna.serra@example.com', carrec='Professora'
        )
        a2 = Autor.objects.create(
            nom='Marc', cognoms='Pujol', email='marc.pujol@example.com', carrec='Consultor TIC'
        )

        Recurs.objects.create(
            titol='Introducció a Django',
            descripcio='Guia bàsica per començar amb Django i les seves apps.',
            categoria='guia',
            data_publicacio='2026-03-01',
            is_active=True,
            autor=a1,
        )
        Recurs.objects.create(
            titol='REST APIs amb DRF',
            descripcio='Vídeo explicatiu sobre serializers, viewsets i routers.',
            categoria='video',
            data_publicacio='2026-03-02',
            is_active=True,
            autor=a1,
        )
        Recurs.objects.create(
            titol='Bones pràctiques de fetch',
            descripcio='Article amb exemples de peticions GET i POST des del frontend.',
            categoria='article',
            data_publicacio='2026-03-03',
            is_active=True,
            autor=a2,
        )

        self.stdout.write(self.style.SUCCESS('Dades de prova carregades correctament.'))
