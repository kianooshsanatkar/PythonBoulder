
class SocialMediaAccount:
    def __eq__(self, o: object) -> bool:
        raise NotImplementedError()

    def __str__(self) -> str:
        raise NotImplementedError()

    def read(self, number: str):
        raise NotImplementedError()

    pass


class InstagramAccount(SocialMediaAccount):
    pass


class FacebookAccount(SocialMediaAccount):
    pass


class TwitterAccount(SocialMediaAccount):
    pass


class LinkedinAccount(SocialMediaAccount):
    pass


class TelegramAccount(SocialMediaAccount):
    pass
