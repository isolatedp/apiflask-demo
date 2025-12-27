# src/services/custom_enums/status_enums.py
from enum import Enum


class StatusEnum(Enum):
    ERROR = -9
    AUTHORIZATION_ERROR = -5
    DATA_VALIDATION_ERROR = -1
    FAILED = 0
    SUCCESS = 1
    SUCCESS_WITH_WARNING = 2
    SUCCESS_WITHOUT_DATA = 3