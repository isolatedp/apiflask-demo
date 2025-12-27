# src/controllers/default_controller.py
import http
import traceback
from http import HTTPStatus
from typing import List, Any
from datetime import datetime
from pytz import timezone

from src.configs import Configs
from src.services.custom_enums.response_type_enums import ResponseTypeEnum
from src.services.custom_enums.status_enums import StatusEnum
from src.services.custom_enums.action_type_enums import ActionTypeEnum
from src.services.custom_enums.result_enums import ResultEnum
from src.services.custom_enums.resource_enums import ResourceEnum
from src.logics.default_logics import DefaultLogics

class DefaultController:
    def generate_response(
        self,
        messages: List[str],
        data: Any,
        http_code: int = HTTPStatus.OK.value,
        status: int = StatusEnum.SUCCESS.value,
        response_type: str = ResponseTypeEnum.JSON.value,
        ):
        try:
            timezone_config = Configs.APP_TIMEZONE or None
            app_tz = timezone(timezone_config)
            response_dt = datetime.now(app_tz)
            response_dt_str = response_dt.strftime('%Y-%m-%d %H:%M:%S %Z')

            response_content = {
                'responseType': response_type,
                'status': status,
                'messages': messages,
                'data': data,
                'responseDt': response_dt_str
            }
        except Exception as _:
            error_msg = traceback.format_exc()

            timezone_config = Configs.APP_TIMEZONE or 'UTC'
            app_tz = timezone(timezone_config)
            response_dt = datetime.now(app_tz)
            response_dt_str = response_dt.strftime('%Y-%m-%d %H:%M:%S %Z')
            default_msg = ActionTypeEnum.REQUEST.value + ResultEnum.ERROR.value + '。'
            default_msg += (ResultEnum.WAIT_AND_RETRY.value + '，' + ResultEnum.KEEP_ERROR_AND_CONTACT.value + '。')

            http_code = HTTPStatus.INTERNAL_SERVER_ERROR.value
            status = StatusEnum.ERROR.value
            response_type = ResponseTypeEnum.JSON.value
            response_content = {
                'responseType': response_type,
                'status': status,
                'messages': messages,
                'data': data,
                'responseDt': response_dt_str
            }
        return response_content, http_code
    
    def get_health(self, *args, **kwargs):
        try:
            result = DefaultLogics().get_health()
            if not result['status']:
                http_code = HTTPStatus.BAD_REQUEST.value
                status = StatusEnum.FAILED.value
                default_msg = ActionTypeEnum.GET.value + ResourceEnum.HEALTH.value + ResultEnum.FAILED.value + '。'
                messages = [default_msg]
                data = None
            elif result['status']:
                # 此分支可再對於資料細分查詢成功無資料狀態
                http_code = HTTPStatus.OK.value
                status = StatusEnum.SUCCESS.value
                default_msg = ActionTypeEnum.GET.value + ResourceEnum.HEALTH.value + ResultEnum.SUCCESS.value + '。'
                messages = [default_msg]
                data = result['data']

        except Exception as _:
            error_msg = traceback.format_exc()
            http_code = HTTPStatus.INTERNAL_SERVER_ERROR.value
            status = StatusEnum.ERROR.value
            default_msg = ActionTypeEnum.GET.value + ResourceEnum.HEALTH.value + ResultEnum.ERROR.value + '。'
            default_msg += (ResultEnum.WAIT_AND_RETRY.value + '，' + ResultEnum.KEEP_ERROR_AND_CONTACT.value + '。')
            messages = [default_msg]
            data = None
        return self.generate_response(http_code=http_code, status=status, messages=messages, data=data)
