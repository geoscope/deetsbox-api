# from .dependencies import get_query_token, get_token_header
from fastapi import Depends, FastAPI
from .routers import repositories
from scalar_fastapi import get_scalar_api_reference

app = FastAPI(
    docs_url=None,
    redoc_url=None,
    # dependencies=[Depends(get_query_token), Depends(get_token_header)],
)

app.include_router(repositories.router)


@app.get("/health")
async def root():
    return {"status": "OK"}


@app.get("/scalar", include_in_schema=False)
async def scalar_html():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Deetsbox API Reference",
    )
