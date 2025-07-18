from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.db import get_db as get_session
from src.schemas.employee import EmployeeCreate, EmployeeUpdate, EmployeeResponse
from src.service import employee_service
from src.utils.auth import require_role

router = APIRouter(prefix="/employees", tags=["Employees"])


@router.post("/", response_model=EmployeeResponse)
async def create_employee(
    data: EmployeeCreate, 
    session: AsyncSession = Depends(get_session),
    current_user = Depends(require_role("admin"))
):
    return await employee_service.create_employee(session, data)


@router.get("/{employee_id}", response_model=EmployeeResponse)
async def get_employee(
    employee_id: int, 
    session: AsyncSession = Depends(get_session),
    current_user = Depends(require_role("admin"))
):
    return await employee_service.get_employee_by_id(session, employee_id)


@router.put("/{employee_id}", response_model=EmployeeResponse)
async def update_employee(
    employee_id: int, 
    data: EmployeeUpdate, 
    session: AsyncSession = Depends(get_session),
    current_user = Depends(require_role("admin"))
):
    return await employee_service.update_employee(session, employee_id, data)
