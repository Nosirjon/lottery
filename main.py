from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_table, delete_table


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_table()
    print('База очищена')
    await create_table()
    print('База готова')
    yield
    print('Выключение')

app = FastAPI(lifespan=lifespan)


tasks = []

