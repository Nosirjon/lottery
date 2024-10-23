from sqlalchemy import select
from database import new_session, TaskOrm
from main import STaskAdd

class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        async with new_session() as session:
            try:
                task_dict = data.model_dump()  # Ensure this method exists in STaskAdd

                task = TaskOrm(**task_dict)   
                session.add(task)
                await session.flush()  # Ensure the task is added to the session
                await session.commit()  # Commit the transaction
                return task.id  # Return the newly created task ID
            except Exception as e:
                await session.rollback()  # Roll back if there's an error
                raise e  # Optionally re-raise the exception for higher-level handling

    @classmethod
    async def find_all(cls):
        async with new_session() as session:
            try:
                query = select(TaskOrm)
                result = await session.execute(query)
                task_models = result.scalars().all()  # Retrieve the task instances
                return task_models  # Optionally map to a Pydantic model for response
            except Exception as e:
                # Handle the exception as necessary
                raise e  # Re-raise for higher-level handling
