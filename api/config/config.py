class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'my_secured_key_here'
    SECURITY_PASSWORD_SALT = 'my_security_password_here'
    JWT_SECRET_KEY="b'\x99\xceK\x0ev\x9b\xb6\xf7q\x89`\x92\xcf]"
    SQLALCHEMY_DATABASE_URI = "sqlite:///./users.db" 

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_ECHO = False
