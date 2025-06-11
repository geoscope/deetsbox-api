from fastapi import APIRouter

from ..dependencies import get_token_header

router = APIRouter(
    prefix="/repositories",
    tags=["repositories"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get("/", tags=["repositories"])
async def read_repositories():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/{id}", tags=["repositories"])
async def get_repository(id: str):
    return {"username": id}


@router.post("/", tags=["repositories"])
async def create_repository(id: str):
    return {"username": id}


@router.put("/{id}", tags=["repositories"])
async def update_repository(id: str):
    return {"username": id}


@router.delete("/{id}", tags=["repositories"])
async def delete_repository(id: str):
    return {"username": id}
