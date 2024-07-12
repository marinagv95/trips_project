from typing import Dict
from src.drivers.email_sender import send_email
import uuid



class TripCreator:
    def __init__(self, trips_repository, email_repository) -> None:
        self.__trips_repository = trips_repository
        self.__email_repository = email_repository

    def create(self, body) -> Dict:
        try:
            emails = body.get("email_to_invite")

            trip_id = str(uuid.uuid4())
            trip_infos = {**body, "id": trip_id}

            self.__trips_repository.create_trip(trip_infos)

            if emails:
                for email in emails:
                    self.__email_repository.registry_email(
                        {"email": email, "trip_id": trip_id, "id": str(uuid.uuid4())}
                    )

            send_email(
                [body["owner_email"]],
                f"http://localhost:3000/trips/{trip_id}/confirm"
                
                       )

            return {"body": {"id": trip_id}, "status_code": 201}
        except Exception as exception:
            return {
                "body": {"error": "Bad Request", "message": str(exception)},
                "status_code": 400,
            }
