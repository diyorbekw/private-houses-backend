from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from src.models import Employee
from src.schemas.employee import EmployeeCreate, EmployeeUpdate


class EmployeeService:
    @staticmethod
    async def create_employee(session: AsyncSession, data: EmployeeCreate) -> Employee:
        employee = Employee(**data.dict())
        session.add(employee)
        await session.commit()
        await session.refresh(employee)
        return employee

    @staticmethod
    async def get_employee_by_id(session: AsyncSession, employee_id: int) -> Employee:
        result = await session.execute(select(Employee).where(Employee.id == employee_id))
        return result.scalar_one_or_none()

    @staticmethod
    async def get_all_employees(session: AsyncSession) -> list[Employee]:
        result = await session.execute(select(Employee))
        return result.scalars().all()

    @staticmethod
    async def update_employee(session: AsyncSession, employee_id: int, data: EmployeeUpdate) -> Employee:
        await session.execute(
            update(Employee)
            .where(Employee.id == employee_id)
            .values(**data.dict(exclude_unset=True))
        )
        await session.commit()
        return await EmployeeService.get_employee_by_id(session, employee_id)

    @staticmethod
    async def delete_employee(session: AsyncSession, employee_id: int) -> None:
        await session.execute(delete(Employee).where(Employee.id == employee_id))
        await session.commit()
