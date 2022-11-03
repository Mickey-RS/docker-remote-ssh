from fastapi import FastAPI
from routes.user import user
from API_tags import tags_metadata, contact_info

app = FastAPI(
    title="Docker API",
    description="Esto se va a ver chulísimo en producción 7u7r",
    version="1.0.0",
    openapi_tags=tags_metadata,
    contact=contact_info
)

app.include_router(user)
