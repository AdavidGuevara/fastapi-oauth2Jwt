from routes.user_routes import user
from fastapi import FastAPI


app = FastAPI(
    title="FastAPI, JWT and OAUTH2",
    description="an example of authentication in FastAPI",
    version="1.0",
)

app.include_router(user)
