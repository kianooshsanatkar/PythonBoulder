from abc import ABC

from core.handler.basecq import BaseCommand


class InfraBaseCommand(BaseCommand, ABC):

    def __init__(self, user, uow, adapter):
        super().__init__(user, uow)
        self.adp = adapter
