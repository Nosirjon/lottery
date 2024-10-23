from typing import Optional
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


engine = create_async_engine(
    "sqlite+aiosqlite:///base.db"
)

async_session = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

class Model(DeclarativeBase):
    pass

class TaskOrm(Model):
    __tablename__ = "base"

    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[str]]

async def create_table():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)

async def delete_table():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)


async def example_usage():
    async with async_session() as session:
        
        pass
