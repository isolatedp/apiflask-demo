# src/services/enums/messages_enums.py
from enum import Enum


class MessagesEnums(Enum):
    """
    訊息對應
    """
    SUCCESS = '成功'
    FAIL = '異常，請稍後再試。若問題持續發生請聯絡系統管理人員'


class FunctionsEnums(Enum):
    """
    功能名稱對應
    """
    SYSTEM_HEALTH = '系統狀態'
    

class ActionEnums(Enum):
    """
    請求動作對應
    """
    REQUEST = '請求'
    GET = '取得'
    POST = '新增'
    PUT = '修改'
    DELETE = '刪除'
    