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


##### IMPORTANT!!  Fill in with your own database url from vercel #####
DATABASE_URL = "postgresql://neondb_owner:npg_h0WerfPSg4Xa@ep-icy-hall-advpwzpk-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require"
#######################

# Database connection
conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()

# Create table if not exists
cur.execute("""
CREATE TABLE IF NOT EXISTS items (
    itemId   TEXT PRIMARY KEY,
    itemDesc TEXT NOT NULL
)
""")
conn.commit()


@app.get("/")
def root():
    return {"Hello": "World"}



    