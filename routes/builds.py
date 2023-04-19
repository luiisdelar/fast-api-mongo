from fastapi import APIRouter, Response, Depends
from data.load_data import load_data
from models.build import Build
from config.database import connection
from starlette.status import *
from schemas.build import build_entity, builds_entity
from bson import ObjectId
from middlewares.decode_token import decode_token

build = APIRouter()

@build.get('/load-data', response_model=list[Build], tags=["builds"])
def get_data(decoded_token = Depends(decode_token)):
    if load_data():
        return Response(status_code=HTTP_200_OK)
    return Response(status_code=HTTP_400_BAD_REQUEST)


@build.get('/builds', tags=["builds"])
def get_builds(decoded_token = Depends(decode_token)):
    return builds_entity(connection.data.builds.find())


@build.get('/builds/{id}', response_model=Build, tags=["builds"])
def get_build(id: str):
    return build_entity(connection.data.builds.find_one({'_id': ObjectId(id)}))


@build.put('/builds/{id}', response_model=Build, tags=["builds"])
def update_user(id: str, build: Build, decoded_token = Depends(decode_token)):
    connection.data.builds.find_one_and_update({
        "_id": ObjectId(id)
    }, {
        "$set": dict(build)
    })
    return build_entity(connection.data.builds.find_one({"_id": ObjectId(id)}))


@build.delete('/builds/{id}', response_model=Build, tags=["builds"])
def delete_build(id: str, decoded_token = Depends(decode_token)):
    build_entity(connection.data.builds.find_one_and_delete({'_id': ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)
