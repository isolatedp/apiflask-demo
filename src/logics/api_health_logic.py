# src/logics/api_health_logic.py
import traceback
from services.utils import generate_return
from cruds.db_health_cruds import get_db_health

class ApiHealthLogic:
    def __init__(self):
        self.status = False
        self.message = ""
        self.data = None
        
    def _init_return_params(self):
        self.status = False
        self.message = ""
        self.data = None
    
    def get_system_health(self):
        """
        取得 API 系統運行狀態
        """
        self._init_return_params()
        try:
            result = get_db_health()
            if not isinstance(result, dict) or 'status' not in result.keys():
                raise Exception("ApiHealthLogic.get_system_health Return Unknown Structure.")
            if not result['status']:
                return result
            
            self.status = True
            self.message = ""
            self.data = None
        except Exception as _:
            error = traceback.format_exc()
            self.status = False
            self.message = "logics/api_health_logic/ ApiHealthLogic.get_system_health: "
            self.data = None
        
        return generate_return(self.status, self.message, self.data)
    