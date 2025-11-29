# src/cruds/db_health_cruds.py
from services.utils import generate_return


def get_db_health():
    try:
        status = True
        message = ""
        data = None
    except Exception as _:
        error = traceback.format_exc()
        status = False
        message = "cruds/db_health_cruds/ get_db_health: " + error
        data = None
    return generate_return(status, message, data)
