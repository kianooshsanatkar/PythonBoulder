from abc import ABC

from core.handler.basecq import BaseQuery


class InfraBaseQuery(BaseQuery, ABC):

    def __init__(self, user, uow, adapter):
        super().__init__(user, uow)
        self.adp = adapter
