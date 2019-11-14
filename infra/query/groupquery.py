from infra.datahandler import objectmodels as model
from infra.query.infrabasequery import InfraBaseQuery


class GetGroupById(InfraBaseQuery):

    def run(self, group_id):
        with self.__data_handler__ as repo:
            group_model = repo.get(model.Group(group_id))
            return self.__model_translator__.group_translator(group_model)


class GetGroupByTitle(InfraBaseQuery):

    def run(self, group_name):
        with self.__data_handler__ as repo:
            group_model = repo.session.query(model.Group).filter_by(Title=group_name).first()
            return self.__model_translator__.group_translator(group_model)
