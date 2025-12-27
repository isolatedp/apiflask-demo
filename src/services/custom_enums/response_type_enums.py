# src/services/custom_enums/response_type_enums.py
from enum import Enum

class ResponseTypeEnum(Enum):
    JSON = "json"
    HTML = "html"
    FILE = "file"