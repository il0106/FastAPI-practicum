from scr.database import postgres_sync_engine
from scr.models import metadata_obj


def create_init_tables():
    metadata_obj.drop_all(postgres_sync_engine)
    metadata_obj.create_all(postgres_sync_engine)





