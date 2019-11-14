from core.local import LanguageLocalization

i18n_texts = {
    "PASSWORD_VALUE_NOT_VALID": ("Password value is not valid", "مقدار پسوورد وارد شده معتبر نمی باشد"),
    "MOBILE_NOT_VALID": ("Mobile number value is not valid", "شماره تلفن همراه وارد شده معتبر نمی باشد"),
    "USER_NEED_CONTACT": ("Please insert a valid email address or mobile number",
                          "لطفا یک ایمیل آدرس یا شماره همراه معتبر وارد نمایید"),
    "EMAIL_NOT_VALID": ("Email value is not valid", "ایمیل وارد شده معتبر نمی باشد"),
    "USER_NAME_NOT_VALID": ("Username value is not valid", "یوزرنیم وارد شده صحیح نمی باشد."),
    'ALREADY_LOGGED_IN': ('you have already logged in.','شما قبلا وارد سیستم شده اید'),
    "LOGIN_VALUE_INCORRECT":("username or password is incorrect!","یوزرنیم با پسوورد وارد یافت نشد!")

}


class Texts:
    PASSWORD_VALUE_NOT_VALID = "PASSWORD_VALUE_NOT_VALID"
    MOBILE_NOT_VALID = "MOBILE_NOT_VALID"
    USER_NEED_CONTACT = "USER_NEED_CONTACT"
    EMAIL_NOT_VALID = "EMAIL_NOT_VALID"
    USER_NAME_NOT_VALID = "USER_NAME_NOT_VALID"
    ALREADY_LOGGED_IN = 'ALREADY_LOGGED_IN'
    LOGIN_VALUE_INCORRECT = "LOGIN_VALUE_INCORRECT"


class ResourceManager:
    __locale = LanguageLocalization(i18n_texts)

    @staticmethod
    def translate(text: str) -> str:
        return ResourceManager.__locale.translate(text)