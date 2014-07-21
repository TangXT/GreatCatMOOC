from .devstack import *

LANGUAGES = ( ('zh_CN', 'CHINESE (CHINA)'), )
TIME_ZONE = 'Asia/Shanghai'
LANGUAGE_CODE = 'zh_CN'

# Platform Email console
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp@gmail.com'
EMAIL_PORT = 587     # 587 for Gmail,25 for others
EMAIL_USE_TLS = True # True or False according to your server. (True for Gmail.)
EMAIL_HOST_USER = 'dabingbaozhang@gmail.com'
EMAIL_HOST_PASSWORD = 'dabingbao'

DEFAULT_FROM_EMAIL = 'dabingbaozhang@gmail.com'
DEFAULT_FEEDBACK_EMAIL = 'dabingbaozhang@gmail.com'
SERVER_EMAIL = 'dabingbaozhang@gmail.com'
TECH_SUPPORT_EMAIL = 'dabingbaozhang@gmail.com'
CONTACT_EMAIL = 'dabingbaozhang@gmail.com'
BUGS_EMAIL = 'dabingbaozhang@gmail.com'
ADMINS = (
          ('GreatCat Admins', 'dabingbaozhang@gmail.com')
          )
MANAGERS = ADMINS