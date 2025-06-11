from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

app = FastAPI(docs_url=None, redoc_url=None)


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/scalar", include_in_schema=False)
async def scalar_html():
    return get_scalar_api_reference (
        openapi_url=app.openapi_url,
        title=app.title,
    )
