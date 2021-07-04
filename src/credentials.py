import configparser
import definitions


class Credentials:

    def __init__(self):
        credentials_path = definitions.OAUTH_CONFIG_PATH
        credentials = configparser.ConfigParser()
        credentials.read(credentials_path)
        self._api_key = credentials['Credentials']['apiKey']
        self._api_token = credentials['Credentials']['apiToken']
        self._email = credentials['Credentials']['email']
        self._password = credentials['Credentials']['password']

    @property
    def api_key(self):
        return self._api_key

    @property
    def api_token(self):
        return self._api_token

    @property
    def email(self):
        return self._email

    @property
    def password(self):
        return self._password
