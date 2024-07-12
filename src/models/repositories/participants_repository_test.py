# import pytest # type: ignore
# import uuid
# from participants_repository import ParticipantsRepository
# from src.models.settings.db_connection_handler import db_connection_handler

# db_connection_handler.connect()
# trip_id = str(uuid.uuid4())

# @pytest.mark.skip(reason="interacao com o banco")
# def test_registry_participant():
#     conn = db_connection_handler.get_connection()
#     participants_repository = ParticipantsRepository(conn)

#     participants_infos = {
#         "id": str(uuid.uuid4()),
#         "trip_id": trip_id,
#         "emails_to_invite_id": ,
#         "name":
#     }