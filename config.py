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
