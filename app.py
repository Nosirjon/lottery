from typing import Annotated
from fastapi import APIRouter, Depends
from repository import TaskRepository

from main import STaskAdd

router = APIRouter(
    
)

@router.post("/tasks")
async def add_task(
    task: Annotated[STaskAdd, Depends()]
):
    task_id = await TaskRepository.add_one(task)
    return {'ok': True, 'task_id': task_id}


@router.get('/home')
async def get_tasks():
    tasks = await TaskRepository.find_all()
    return {'tasks': tasks}