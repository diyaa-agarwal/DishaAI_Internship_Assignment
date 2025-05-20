from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import tasks

app = FastAPI()

# Enable CORS for your React app (change origin to your frontend URL or localhost)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or wherever your frontend runs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tasks.router, prefix="/api")
