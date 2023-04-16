from fastapi import APIRouter, Response
from data.load_data import load_data
from models.build import Build
from config.database import connection
from starlette.status import *
from schemas.build import build_entity, builds_entity
from bson import ObjectId

build = APIRouter()


@build.get('/load-data', response_model=list[Build], tags=["builds"])
def get_data():
    if load_data():
        return Response(status_code=HTTP_200_OK)
    return Response(status_code=HTTP_400_BAD_REQUEST)


@build.get('/builds', response_model=Build, tags=["builds"])
def get_builds():
    return builds_entity(connection.data.builds.find())


@build.get('/builds/{id}', response_model=Build, tags=["builds"])
def get_build(id: str):
    return build_entity(connection.data.builds.find_one({'_id': ObjectId(id)}))


@build.put('/builds/{id}', response_model=Build, tags=["builds"])
def update_user(id: str, build: Build):
    connection.data.builds.find_one_and_update({
        "_id": ObjectId(id)
    }, {
        "$set": dict(build)
    })
    return build_entity(connection.data.builds.find_one({"_id": ObjectId(id)}))


@build.delete('/builds/{id}', response_model=Build, tags=["builds"])
def delete_build(id: str):
    build_entity(connection.data.builds.find_one_and_delete({'_id': ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)
