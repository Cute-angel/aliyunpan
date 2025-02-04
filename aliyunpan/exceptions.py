class AliyunpanException(BaseException):
    def __init__(self, message='', *args, **kwargs):
        super(AliyunpanException, self).__init__(*args, **kwargs)
        self.message = message

    def __str__(self):
        return self.message


class InvalidRefreshToken(AliyunpanException):
    """无效的refresh_token"""

    def __str__(self):
        return self.message or 'Is not a valid refresh_token.'


class InvalidPassword(AliyunpanException):
    """无效的密码"""


class LoginFailed(AliyunpanException):
    """登录失败"""


class ConfigurationFileError(AliyunpanException, FileNotFoundError):
    """配置文件错误"""


class ConfigurationFileNotFoundError(ConfigurationFileError):
    """找不到配置文件"""


class InvalidConfiguration(ConfigurationFileError):
    """无效的配置文件"""
