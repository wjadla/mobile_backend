from fastapi import APIRouter
from repository.personRepo import PersonRepo
from model.person import Person, Response

personRouter = APIRouter()


@personRouter.get("/person/")
async def person():
    _personList = await PersonRepo.retrieve()
    return Response(code=200, status="OK", message="success retrieve of data", result=_personList).dict(
        exclude_none=True)


@personRouter.post("/create")
async def create(person: Person):
    await PersonRepo.insert(person)
    return Response(code=200, status="OK", message="success create of person").dict(exclude_none=True)


@personRouter.get("/person/{id}")
async def get_id(id:str):
    _person = await PersonRepo.retrieve_id(id)
    return Response(code=200, status="OK", message="success retrieve of person with id").dict(exclude_none=True)


@personRouter.post("/person/update")
async def update(person: Person):
    await PersonRepo.update(person.id, person)
    return Response(code=200, status="OK", message="success update of person").dict(exclude_none=True)


@personRouter.delete("/person/{id}")
async def delete (id: str):
    await PersonRepo.delete(id)
    return Response(code=200, status="OK", message="success delete of person").dict(exclude_none=True)