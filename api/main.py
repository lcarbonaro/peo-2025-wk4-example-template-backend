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
#DATABASE_URL = ""  # TBD  fill in with your own databse url from vercel
#conn = psycopg2.connect(DATABASE_URL)
#cur = conn.cursor()

# Create table if not exists
#cur.execute("""
#CREATE TABLE IF NOT EXISTS urls (
#    short_code TEXT PRIMARY KEY,
#    long_url TEXT NOT NULL
#)
#""")
#conn.commit()


@app.get("/")
def root():
    return {"Hello": "World"}



    