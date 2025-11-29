# src/services/utils/generate_response.py
from .datetime_utils import get_current_datetime


def generate_response(http_code: int = 500, status: int = 0, messages = None, data = None) -> tuple:
    """
    產生 API 回應
    """
    if messages is None:
        messages = []
    
    response_dt = get_current_datetime()
    response_dt_str = response_dt.strftime("%Y-%m-%d %H:%M:%S")
    
    result = {
        'status': status,
        'messages': messages,
        'data': data,
        'timestamp': response_dt_str
    }
    return result, http_code 


def generate_return(status: bool, messages = None, data = None) -> dict:
    """
    內部回傳統一格式
    """
    if messages is None:
        messages = []
    
    return {
        'status': status,
        'messages': messages,
        'data': data
    }
