from configparser import ConfigParser


def read_settings():
    settings = dict()
    config = ConfigParser()
    config.read('settings.ini')
    settings["api_token"] = config.get('api_auth', 'token')
    settings["mysql_host"] = config.get('database', 'mysql_host')
    settings["mysql_password"] = config.get('database', 'mysql_password')
    settings["mysql_port"] = config.get('database', 'mysql_port')
    settings["mysql_user"] = config.get('database', 'mysql_user')
    settings["mysql_database"] = config.get('database', 'mysql_database')
    return settings