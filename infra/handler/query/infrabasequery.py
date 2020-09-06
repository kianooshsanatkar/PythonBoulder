from core.handler.basecq import BaseQuery
from infra.datahandler.repository import InfraRepository
from infra.translator.toentity import ObjectModelTranslator
from infra.translator.toobjectmodel import EntityTranslator


class InfraBaseQuery(BaseQuery):
    __data_handler__ : InfraRepository
    __entity_translator__ = EntityTranslator
    __model_translator__ = ObjectModelTranslator
