# src/services/custom_enums/result_enums.py
from enum import Enum


class ResultEnum(Enum):
    ERROR = "發生異常錯誤"
    WAIT_AND_RETRY = "請稍後再試"
    KEEP_ERROR_AND_CONTACT = "若問題持續發生，請聯絡管理人員"
    FAILED = "失敗"
    SUCCESS = "成功"