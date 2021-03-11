from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi.middleware.cors import CORSMiddleware
from ApiRouters.organization import OrganizationRouter
from ApiRouters.faq import FAQRouter
from AWS.aws import AWSRouter

origins = [
"*"
]
database = "sqlite:///database.sqlite?check_same_thread=False"

app = FastAPI()
app.include_router(AWSRouter)
app.add_middleware(DBSessionMiddleware, db_url=database)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)
