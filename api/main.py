import psycopg2
from psycopg2.extras import RealDictCursor  # to return response as json objects

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import os # to fetch environment variables from vercel 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)


def get_db_connection():
    # connection string from environment variable
    DATABASE_URL = os.environ.get("DATABASE_URL")
    conn = psycopg2.connect(DATABASE_URL)
    return conn

@app.get("/")
def root():
    return {"Hello": "World"}



    