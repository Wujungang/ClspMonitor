import logging

from celery_tasks.main import app

logger = logging.getLogger("django")

# 验证码短信模板
SMS_CODE_TEMP_ID = 1

@app.task(name='send_sms_code')
def send_sms_code(mobile,code,expire):
    try:
        print(mobile +"發送短信，驗證碼為"+code)
    except Exception as e:
        logger.error("发送验证码短信[异常][ mobile: %s, message: %s ]" % (mobile, e))