# src/logics/default_logics.py
import traceback
from typing import Any

from sqlalchemy import text

from src.extends import extends


class DefaultLogics:
    def __init__(self):
        self.db = extends.db

    def generate_return(
        self, 
        status: bool = True, 
        message: str = '', 
        data: Any = None) -> dict:
        return {
            'status': status,
            'message': message,
            'data': data
        }

    def failed_result(
        self, 
        result_obj: Any
        ) -> bool:
        if not isinstance(result_obj, dict) or 'status' not in result_obj:
            error_msg = f"Unknown Return Structure."
            raise Exception(error_msg)
        return not result_obj['status']
    
    def get_health(self):
        try:
            result_data = {
                'api_health': 1
            }

            # 確認資料庫連線是否正常(若無資料庫可註解掉)
            result = self.get_database_health()
            if self.failed_result(result):
                return result
            database_health = result['data']
            result_data.update({
                'database_health': database_health
            })

            status = True
            message = ''
            data = result_data

        except Exception as _:
            error_msg = traceback.format_exc()
            status = False
            message = ''
            data = None
        return self.generate_return(status=status, message=message, data=data)

    def get_database_health(self):
        """
        確認資料庫是否正常
        """
        try:
            self.db.session.execute(text('SELECT 1'))
            result_data = {
                'default_db': 1
            }

            # TODO 多資料庫處理

            status = True
            message = ''
            data = result_data
        except Exception as _:
            error_msg = traceback.format_exc()
            status = False
            message = ''
            data = {'default_db': 0}
        return self.generate_return(status=status, message=message, data=data)
