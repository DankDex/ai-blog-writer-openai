##OPEN API STUFF
OPENAI_API_KEY = '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'



## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
