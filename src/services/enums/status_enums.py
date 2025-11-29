# src/services/enums/status_enums.py
from enum import Enum

class StatusEnums(Enum):
    BAD_REQUEST = -3
    UNAUTHORIZED = -2
    CRITICAL_FAIL = -1
    FAIL = 0
    SUCCESS = 1
    SUCCESS_WITHOUT_DATA = 2
    SUCCESS_WITH_WARNING = 3
