# recursos_api

Projecte Django que implementa una API REST amb Django REST Framework per gestionar **autors** i **recursos**.

## Funcionalitats

- CRUD complet de recursos
- CRUD complet d'autors
- Relació `Autor 1..* Recurs`
- Filtres a `/api/recursos/?categoria=...&search=...&is_active=true`
- Endpoint de recursos d'un autor: `/api/autors/<id>/recursos/`
- Exportació CSV: `/api/recursos/export/csv/`
- Documentació navegable: `/api/docs/`

## Instal·lació ràpida

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
# .venv\Scripts\activate    # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_demo
python manage.py runserver 0.0.0.0:8000
```

## Endpoints principals

- `GET /api/recursos/`
- `POST /api/recursos/`
- `GET /api/recursos/<id>/`
- `GET /api/autors/`
- `GET /api/autors/<id>/`
- `GET /api/autors/<id>/recursos/`
- `GET /api/recursos/export/csv/`
- `GET /api/docs/`

## Exemple de POST

```json
{
  "titol": "Nou recurs",
  "descripcio": "Recurs creat des del portal",
  "categoria": "guia",
  "data_publicacio": "2026-03-17",
  "is_active": true,
  "autor_id": 1
}
```
