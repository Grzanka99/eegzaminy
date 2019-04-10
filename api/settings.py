class Settings(object):
    DEBUG = True

    HOST = '192.168.1.105'
    PORT = 9000

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@0.0.0.0:port/Eegzamin'

    CORS_RESOURCES = {
    r"/v1/*": {
        "origins": [
            "http://localhost",
            "http://127.0.0.1:*",
            "http://192.168.8.*",
            "http://192.168.8.*:*",
            "https://localhost",
            "https://*.eegzaminy.pl",
            "http://test.eegzaminy.pl/",
            "*",
        ]
    }
}