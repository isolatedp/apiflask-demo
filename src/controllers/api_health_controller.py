# src/controllers/api_health_controller.py
import traceback
from http import HTTPStatus

from services.utils import generate_response
from services.enums.status_enums import StatusEnums
from services.enums.messages_enums import ActionEnums, FunctionsEnums, MessagesEnums
from logics.api_health_logic import ApiHealthLogic


class ApiHealthController:
    def get_system_health(self):
        """
        取得 API 系統運行狀態
        """
        try:
            result = ApiHealthLogic().get_system_health()
            if not isinstance(result, dict) or 'status' not in result.keys():
                raise Exception("ApiHealthController.get_system_health Return Unknown Structure.")
            
            if not result['status']:
                http_code = HTTPStatus.BAD_REQUEST.value
                status = StatusEnums.FAIL.value
                message = ActionEnums.GET.value + FunctionsEnums.SYSTEM_HEALTH.value + MessagesEnums.FAIL.value
                messages = [message]
                if result.get('message'):
                    messages.append(result.get('message'))
                data = None
            else:
                http_code = HTTPStatus.OK.value
                status = StatusEnums.SUCCESS.value
                message = ActionEnums.GET.value + FunctionsEnums.SYSTEM_HEALTH.value + MessagesEnums.SUCCESS.value
                messages = [message]
                if result.get('message'):
                    messages.append(result.get('message'))
                data = result['data']
            
        except Exception as _:
            error = traceback.format_exc()
            http_code = HTTPStatus.INTERNAL_SERVER_ERROR.value
            status = StatusEnums.FAIL.value
            message = ActionEnums.GET.value + FunctionsEnums.SYSTEM_HEALTH.value + MessagesEnums.FAIL.value
            messages = [message, error]
            data = None
        
        return generate_response(http_code=http_code, status=status, messages=messages, data=data)