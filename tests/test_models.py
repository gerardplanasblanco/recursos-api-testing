import pytest
from catalog.models import Autor, Recurs

@pytest.mark.django_db
def test_crear_recurs():
    autor = Autor.objects.create(nom="Autor Test")

    recurs = Recurs.objects.create(
        titol="Recurs Test",
        categoria="video",
        autor=autor
    )

    assert recurs.titol == "Recurs Test"