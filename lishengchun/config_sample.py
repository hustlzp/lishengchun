# coding: utf-8

# set False in production
DEBUG = True

AUTH_USERNAME = ''
AUTH_PASSWORD = ''

# site domain
SITE_DOMAIN = "http://www.lishengchun.com"
IMAGE_SERVER_URL = "http://localhost:8080"
HOST_STRING = ""

# image upload path
UPLOADS_DEFAULT_DEST = "/var/www/lsc_uploads"
UPLOADS_DEFAULT_URL = "%s/lsc_uploads/" % IMAGE_SERVER_URL

# app config
SECRET_KEY = "A0Zr98j/3yX R~XHH!jmN]LWX/,?RT"
PERMANENT_SESSION_LIFETIME = 3600 * 24 * 7
SESSION_COOKIE_NAME = 'lsc_session'

# db config
DB_HOST = ""
DB_USER = ""
DB_PASSWORD = ""
DB_NAME = ""
SQLALCHEMY_DATABASE_URI = "mysql://%s:%s@%s/%s" % (DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)

# smtp config
SMTP_SERVER = ""
SMTP_PORT = 25
SMTP_USER = ""
SMTP_PASSWORD = ""
SMTP_FROM = ""
SMTP_ADMIN = ""

# Flask debug toolbar
DEBUG_TB_INTERCEPT_REDIRECTS = False