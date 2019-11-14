class CultureConfig:
    class Language:
        SUPPORTED = {"eng": 0, "fa": 1}
        current_lan = "eng"

    class Currency:
        SUPPORTED = {"IRR", "USD", "EUR"}
        currency = "IRR"

    class DateTime:
        SUPPORTED_FORMAT = {"gregorian", "solar", "moon"}
        datetime_format = "gregorian"

    def __init__(self, lan="eng", currency="IRR", datetime_format="gregorian"):
        self.is_lan_supported(lan)
        self.Language.current_lan = lan
        self.is_currency_supported(currency)
        self.Currency.currency = currency
        self.is_datetime_format_supported(datetime_format)
        self.DateTime.datetime_format = datetime_format

    # region Static Methods
    @staticmethod
    def is_lan_supported(lan):
        if lan not in CultureConfig.Language.SUPPORTED:
            raise ValueError("Selected Language is not supported")

    @staticmethod
    def is_currency_supported(currency):
        if currency not in CultureConfig.Currency.SUPPORTED:
            raise ValueError("Selected Currency is not supported")

    @staticmethod
    def is_datetime_format_supported(datetime_format):
        if datetime_format not in CultureConfig.DateTime.SUPPORTED_FORMAT:
            raise ValueError("Selected Date Time Format is not supported")

    @staticmethod
    def get_lang_order() -> int:
        return CultureConfig.Language.SUPPORTED[CultureConfig.Language.current_lan]
    # endregion


class LanguageLocalization:
    lan_dictionary: dict
    __num = 0

    def __init__(self,i18n:dict):
        __num = CultureConfig.get_lang_order()
        self.lan_dictionary = i18n

    def translate(self, sentence: str) -> str:
        return self.lan_dictionary[sentence][self.__num]


class DateTimeLocalization:
    pass


class CurrencyLocalization:
    pass
