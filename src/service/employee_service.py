from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException
from src.models.employee import Employee
from src.schemas.employee import EmployeeCreate, EmployeeUpdate
from src.service.audit_log_service import AuditLogger
from src.utils.common import model_to_dict


async def create_employee(session: AsyncSession, data: EmployeeCreate, actor_id: int, actor_type: str) -> Employee:
    emp = Employee(**data.model_dump())
    session.add(emp)
    await session.commit()
    await session.refresh(emp)

    logger = AuditLogger(session)
    await logger.log(actor_type, actor_id, "create", "Employee", emp.id, None, model_to_dict(emp))

    return emp


async def get_employee_by_id(session: AsyncSession, employee_id: int) -> Employee:
    result = await session.execute(select(Employee).where(Employee.id == employee_id))
    emp = result.scalar_one_or_none()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return emp


async def update_employee(session: AsyncSession, employee_id: int, data: EmployeeUpdate, actor_id: int, actor_type: str) -> Employee:
    emp = await get_employee_by_id(session, employee_id)
    old_data = model_to_dict(emp)

    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(emp, key, value)
    await session.commit()
    await session.refresh(emp)

    logger = AuditLogger(session)
    await logger.log(actor_type, actor_id, "update", "Employee", emp.id, old_data, model_to_dict(emp))

    return emp


async def deactivate_employee(session: AsyncSession, employee_id: int, actor_id: int, actor_type: str) -> None:
    emp = await get_employee_by_id(session, employee_id)
    old_data = model_to_dict(emp)
    emp.is_active = False
    await session.commit()

    logger = AuditLogger(session)
    await logger.log(actor_type, actor_id, "deactivate", "Employee", emp.id, old_data, model_to_dict(emp))

