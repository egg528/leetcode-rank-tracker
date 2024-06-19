import pytz
from datetime import datetime


def get_now(timezone='Asia/Seoul') -> str:
    KST = pytz.timezone(timezone)
    return datetime.now(KST).strftime('%Y-%m-%d')