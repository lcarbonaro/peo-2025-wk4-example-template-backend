import os
import psycopg2

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Database connection
conn = psycopg2.connect( os.environ.get("DATABASE_URL") )
cur = conn.cursor()

# Create table if not exists
cur.execute("""
CREATE TABLE IF NOT EXISTS testing (
    itemId   TEXT PRIMARY KEY,
    itemDesc TEXT NOT NULL
)
""")
conn.commit()


@app.get("/")
def root():
    return {"Hello": "World"}



    