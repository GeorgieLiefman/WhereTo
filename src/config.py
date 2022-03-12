import os

class Config(object):
    """
    A class for Flask's config object ehich allows for assigning values to configuration 
    variables, which will be then accessed throughout our application. 
    """
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    
    MAX_CONTENT_LENGTH = 1*1024*1024
    
    SECRET_KEY = os.environ.get("SECRET_KEY")
    
    @property
    def SQLALCHEMY_DATABASE_URI(self):
        """
        This function is used to locate the variables needed to run the application.

        Returns:
            Connects the application to the PostgreSQL database.
        """
        URI_VARS = ["DB_USER", "DB_PASS", "DB_NAME", "DB_DOMAIN"]
        uri_dict = {item: os.environ.get(item) for item in URI_VARS}
        for key in URI_VARS:
            if uri_dict[key] is None:
                raise ValueError(f"{key} is not set.")
        return f"postgresql+psycopg2://{uri_dict['DB_USER']}:{uri_dict['DB_PASS']}@{uri_dict['DB_DOMAIN']}/{uri_dict['DB_NAME']}"


class DevelopmentConfig(Config):
    """
    A class to set the configuration settings when the app is in development. 
    """
    DEBUG = True


class ProductionConfig(Config):
    """
    A class to set the configuration settings when the app is in production. 
    """
    pass


class TestingConfig(Config):
    """
    A class to set the configuration settings when the app is in testing. 
    """
    TESTING = True
environment = os.environ.get("FLASK_ENV")
if environment == "production":
    app_config = ProductionConfig()
elif environment == "testing":
    app_config = TestingConfig()
else:
    app_config = DevelopmentConfig()