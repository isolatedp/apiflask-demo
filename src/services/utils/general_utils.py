# src/services/utils/general_utils.py
import uuid
from typing import Union
import traceback

import shortuuid

from src.extends import extends


class GeneralUtils:
    def generate_uuid(self) -> str:
        return str(uuid.uuid4())

    def generate_shortuuid(self, prefix: str="", length: int=6) -> str:
        """
        生成短 UUID (建議長度 6 時，重試次數至少 3 次)
        Args:
            prefix (str): 前綴詞
            length (int): 長度
        Returns:
            str: 短 UUID
        """
        safe_alphabet = "ABCDEFGHJKLMNPQTUVWXYabcdefghjkmnpqrtuvwxyz346789"
        shortuuid.set_alphabet(safe_alphabet)
        uid = shortuuid.uuid()[:length]
        return f"{prefix}{uid}"
