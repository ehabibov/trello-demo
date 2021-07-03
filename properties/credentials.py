import configparser
import definitions


class Credentials:

    def __init__(self):
        creds_path = definitions.OAUTH_CONFIG_PATH
        creds = configparser.ConfigParser()
        creds.read(creds_path)
        self._api_key = creds['Credentials']['apiKey']
        self._api_token = creds['Credentials']['apiToken']
        self._email = creds['Credentials']['email']
        self._password = creds['Credentials']['password']

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
