from mongoengine import Document

from db.repo.absrepo import AbsRepository


class BaseRepository(AbsRepository):
    def add(self, entity: Document):
        if entity:
            entity.save()

    def add_range(self, entities: [Document]):
        for entity in entities:
            self.add(entity)

    def remove(self, entity: Document):
        if entity:
            entity.save()

    def remove_range(self, entities: [Document]):
        for entity in entities:
            self.remove(entity)

    def get(self, entity: Document):
        entity.objects(id=entity.id)

    def get_all(self, start, count):
        raise NotImplementedError()

    def find(self):
        raise NotImplementedError()

    def find_all(self):
        raise NotImplementedError()
