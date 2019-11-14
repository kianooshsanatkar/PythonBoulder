from core.local import LanguageLocalization

i18n_texts = {
    'USER_HAS_NOT_ACCESS': ('you have no permission to perform this action.', 'شما دسترسی لازم را دارا نمی باشید.'),

}


class Texts:
    USER_HAS_NOT_ACCESS = 'USER_HAS_NOT_ACCESS'


class ResourceManager:
    __locale = LanguageLocalization(i18n_texts)

    @staticmethod
    def translate(text: str) -> str:
        return ResourceManager.__locale.translate(text)
