# src/services/custom_enums/action_type_enums.py
from enum import Enum


class ActionTypeEnum(Enum):
    REQUEST = "請求"
    GET = "取得"
    INSERT = "新增"
    UPDATE = "更新"
    DELETE = "刪除"
    ACTIVE = "啟用"
    