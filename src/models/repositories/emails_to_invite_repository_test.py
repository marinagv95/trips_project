import pytest
import uuid
from src.models.settings.db_connection_handler import db_connection_handler
from .emails_to_invite_repository import EmailToInviteRepository

db_connection_handler.connect()
trip_id = str(uuid.uuid4())


@pytest.mark.skip(reason="interacao com o banco")
def test_registry_email():
    conn = db_connection_handler.get_connection()
    email_to_invite_repository = EmailToInviteRepository(conn)

    email_trips_infos = {
        "id": str(uuid.uuid4()),
        "trip_id": trip_id,
        "email": "olaMundo@email.com",
    }

    email_to_invite_repository.registry_email(email_trips_infos)
    print(email_trips_infos)


@pytest.mark.skip(reason="interacao com o banco")
def test_find_email_from_trip():
    conn = db_connection_handler.get_connection()
    email_to_invite_repository = EmailToInviteRepository(conn)

    emails = email_to_invite_repository.find_email_from_trip(trip_id)
    print()
    print(emails)
