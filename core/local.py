from core.exceptions import ValidationException


class CultureConfig:
    CURRENT_LANG = "eng"
    LANGUAGES = {"eng": 0, "fa": 1}

    CURRENCIES = {"IRR", "USD", "EUR"}
    CURRENT_CURR = "IRR"

    DATE_FORMAT = {"gregorian", "solar", "moon"}
    CURRENT_DATE = "gregorian"

    def __init__(self, lan="eng", currency="IRR", datetime_format="gregorian"):
        self.is_lan_supported(lan)
        self.CURRENT_LANG = lan
        self.is_currency_supported(currency)
        self.CURRENT_CURR = currency
        self.is_datetime_format_supported(datetime_format)
        self.CURRENT_DATE = datetime_format

    @staticmethod
    def set_current_language(lang: str):
        lang = lang.lower()
        CultureConfig.is_lan_supported(lang)
        CultureConfig.CURRENT_LANG = lang

    # region Static Methods
    @staticmethod
    def is_lan_supported(lan):
        if lan not in CultureConfig.LANGUAGES:
            raise ValueError("Selected Language is not supported")

    @staticmethod
    def is_currency_supported(currency):
        if currency not in CultureConfig.CURRENCIES:
            raise ValueError("Selected Currency is not supported")

    @staticmethod
    def is_datetime_format_supported(datetime_format):
        if datetime_format not in CultureConfig.DATE_FORMAT:
            raise ValueError("Selected Date Time Format is not supported")

    @staticmethod
    def get_lang_order() -> int:
        return CultureConfig.LANGUAGES[CultureConfig.CURRENT_LANG]
    # endregion


class LanguageLocalization:
    lan_dictionary: dict

    def __init__(self, i18n: dict):
        self.__num = CultureConfig.get_lang_order
        self.lan_dictionary = i18n

    def translate(self, sentence: str) -> str:
        return self.lan_dictionary[sentence][self.__num()]


class DateTimeLocalization:
    pass


class CurrencyLocalization:
    pass
