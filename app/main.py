from fastapi import FastAPI

from .api.pig_latin import pig_latin

app = FastAPI()

app.include_router(pig_latin, prefix='/piglatinize', tags=['piglatinize'])