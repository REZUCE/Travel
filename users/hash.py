from django.contrib.auth.hashers import BasePasswordHasher
from collections import OrderedDict


# пароль будет храниться в бд без хэша
class PlainTextPassword(BasePasswordHasher):
    algorithm = "plain"

    def salt(self):
        return ''

    def encode(self, password, salt):
        assert salt == ''
        return password

    def verify(self, password, encoded):
        return password == encoded

    def safe_summary(self, encoded):
        return OrderedDict([
            (_('algorithm'), self.algorithm),
            (_('hash'), encoded),
        ])
