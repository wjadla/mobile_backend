import uuid

from model.person import Person
from config import database


class PersonRepo():


    @staticmethod
    async  def retrieve():
        _person = []
        collection = database.get_collection('person').find()
        async for person in collection:
            _person.append(person)
            return _person

    @staticmethod
    async def insert(person: Person):
          id = str(uuid.uuid4())
          _person = {
              "id": id,
              "email": person.email,
              "password": person.password,
              "job": person.job,
              "role_name": person.role_name
          }
          await database.get_collection('person').insert_one(_person)

    @staticmethod
    async def update(id: str, person: Person):
        _person = await database.get_collection('person').find_one({'_id': id})
        _person['email'] = person.email
        _person['password'] = person.password
        _person['job'] = person.job
        _person['role_name'] = person.role_name

        await database.get_collection('person').update_one({"id": id}, {"$set}": _person})


    @staticmethod
    async def retrieve_id(id: str):
        return await database.get_collection('person').find_one({"_id": id})




    @staticmethod
    async def delete(id: str):
        await database.get_collection('person').delete_one({"id": id})
