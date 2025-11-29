# src/services/utils/datetime_utils.py
from datetime import datetime
from pytz import timezone

from configs import Configs


def get_current_datetime():
    """
    依專案時區取得當前時間
    """
    app_timezone = Configs.APP_TIMEZONE
    app_tz = timezone(app_timezone)
    now = datetime.now(app_tz)
    return now
