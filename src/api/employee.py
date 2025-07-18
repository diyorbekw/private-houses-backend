from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.db import get_db as get_async_session
from src.schemas.employee import EmployeeCreate, EmployeeUpdate, EmployeeOut
from src.service.employee_service import EmployeeService

router = APIRouter(prefix="/employees", tags=["Employees"])


@router.post("/", response_model=EmployeeOut)
async def create_employee(
    data: EmployeeCreate,
    session: AsyncSession = Depends(get_async_session)
):
    return await EmployeeService.create_employee(session, data)


@router.get("/", response_model=list[EmployeeOut])
async def get_all_employees(session: AsyncSession = Depends(get_async_session)):
    return await EmployeeService.get_all_employees(session)


@router.get("/{employee_id}", response_model=EmployeeOut)
async def get_employee(employee_id: int, session: AsyncSession = Depends(get_async_session)):
    employee = await EmployeeService.get_employee_by_id(session, employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


@router.put("/{employee_id}", response_model=EmployeeOut)
async def update_employee(
    employee_id: int,
    data: EmployeeUpdate,
    session: AsyncSession = Depends(get_async_session)
):
    employee = await EmployeeService.get_employee_by_id(session, employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return await EmployeeService.update_employee(session, employee_id, data)


@router.delete("/{employee_id}")
async def delete_employee(employee_id: int, session: AsyncSession = Depends(get_async_session)):
    employee = await EmployeeService.get_employee_by_id(session, employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    await EmployeeService.delete_employee(session, employee_id)
    return {"detail": "Employee deleted"}
