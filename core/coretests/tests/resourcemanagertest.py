from core.local import LanguageLocalization, CultureConfig
import unittest

i18n_texts = {
    'Language': ('ENGLISH', 'فارسی'),

}


class Texts:
    Language = 'Language'


class ResourceManager:
    __locale = LanguageLocalization(i18n_texts)

    @staticmethod
    def translate(text: str) -> str:
        return ResourceManager.__locale.translate(text)


class ResourceManagerTest(unittest.TestCase):

    def test_English(self):
        self.assertEqual('ENGLISH',ResourceManager.translate(Texts.Language))
        self.assertNotEqual('فارسی',ResourceManager.translate(Texts.Language))


    def test_Farsi(self):
        CultureConfig.set_current_language('fa')
        self.assertEqual('فارسی',ResourceManager.translate(Texts.Language))
        self.assertNotEqual('English',ResourceManager.translate(Texts.Language))