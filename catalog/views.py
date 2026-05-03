import csv
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Autor, Recurs
from .serializers import AutorSerializer, AutorDetailSerializer, RecursListSerializer


class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return AutorDetailSerializer
        return AutorSerializer

    @action(detail=True, methods=['get'])
    def recursos(self, request, pk=None):
        autor = self.get_object()
        serializer = RecursListSerializer(autor.recursos.all(), many=True)
        return Response(serializer.data)


class RecursViewSet(viewsets.ModelViewSet):
    serializer_class = RecursListSerializer

    def get_queryset(self):
        queryset = Recurs.objects.select_related('autor').all()
        search = self.request.query_params.get('search')
        categoria = self.request.query_params.get('categoria')
        is_active = self.request.query_params.get('is_active')

        if search:
            queryset = queryset.filter(titol__icontains=search) | queryset.filter(descripcio__icontains=search)
        if categoria:
            queryset = queryset.filter(categoria=categoria)
        if is_active in {'true', 'false'}:
            queryset = queryset.filter(is_active=(is_active == 'true'))
        return queryset.order_by('titol')

    @action(detail=False, methods=['get'], url_path='export/csv')
    def export_csv(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="recursos.csv"'
        writer = csv.writer(response)
        writer.writerow(['id', 'titol', 'categoria', 'data_publicacio', 'is_active', 'autor'])
        for recurs in self.get_queryset():
            writer.writerow([
                recurs.id,
                recurs.titol,
                recurs.categoria,
                recurs.data_publicacio,
                recurs.is_active,
                str(recurs.autor),
            ])
        return response
