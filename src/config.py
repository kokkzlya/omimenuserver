import os

_ = os.getenv

class Config:
    REDIS_URL = _("REDIS_URL", "redis://localhost:6379")
    SECRET_KEY = _("SECRET_KEY", "thoushaltchangethissecretkey")
    SQL_URL = _("SQL_URL", "postgresql://omi:omi@localhost/omi")
