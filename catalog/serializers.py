from rest_framework import serializers
from .models import Autor, Recurs


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ['id', 'nom', 'cognoms', 'email', 'data_naixement', 'carrec']


class RecursListSerializer(serializers.ModelSerializer):
    autor = AutorSerializer(read_only=True)
    autor_id = serializers.PrimaryKeyRelatedField(
        queryset=Autor.objects.all(), source='autor', write_only=True
    )

    class Meta:
        model = Recurs
        fields = [
            'id', 'titol', 'descripcio', 'categoria', 'data_publicacio',
            'is_active', 'autor', 'autor_id'
        ]

    def validate_titol(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError('El títol ha de tenir com a mínim 3 caràcters.')
        return value


class AutorDetailSerializer(serializers.ModelSerializer):
    recursos = RecursListSerializer(many=True, read_only=True)

    class Meta:
        model = Autor
        fields = ['id', 'nom', 'cognoms', 'email', 'data_naixement', 'carrec', 'recursos']
