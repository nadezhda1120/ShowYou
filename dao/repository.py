import uuid

from dao.idGenerator import IdGeneratorUuid


class RepositoryIterator:
    def __init__(self, values: list):
        self._values = values
        self._next_index = -1

    def __next__(self):
        self._next_index += 1
        if self._next_index < len(self._values):
            return self._values[self._next_index]
        raise StopIteration()


class Repository:
    def __init__(self):
        self._items = {}
        self._idGenerator = IdGeneratorUuid()
        #self._id_generator

    def __add__(self, other):
        self._items.update(other._items)
        return self

    def create(self, item):
        if item.id is None:
            item.id =self._idGenerator.get_next_id()
        self._items[item.id] = item
        return item

    def update(self, item):
        self.find_by_id(item.id)
        self._items[item.id] = item
        return item

    def delete_by_id(self, id):
        if id in self._items:
            old = self._items[id]
        else:
            return None
            #raise ExceptionNotFound
        del self._items[id]
        return old

    def find_all(self) -> list:
        return list(self._items.values())

    def find_by_id(self, id):
        if id not in self._items:
            return None
            # raise EntityNotFoundException()
        return self._items[id]

    def __iter__(self):
        for item in list(self._items.values()):
            yield item

    def add_all(self, items):
        self._items.update(map(lambda item: (item.id, item), items))

    def count(self):
        return len(self._items)


    #
    # #do I need it here
    # def find_by_username(self, username):
    #     for i in range(0, len(self._items)):
    #         if self._items[i]['username'] == username:
    #             return self._items[username]
    #     return None
    # #change




