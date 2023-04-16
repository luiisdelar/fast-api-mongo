from fastapi import FastAPI
from routes.builds import build

app = FastAPI( 
    title="Builds API",
    description="this is a simple REST API using fastapi and mongodb"
)
app.include_router(build)