from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Type

from src.core.db import get_db as get_async_session
from src.schemas.territory import (
    CountryCreate, CountryUpdate, CountryRead,
    RegionCreate, RegionUpdate, RegionRead,
    CityCreate, CityUpdate, CityRead,
    DistrictCreate, DistrictUpdate, DistrictRead,
    MicroDistrictCreate, MicroDistrictUpdate, MicroDistrictRead,
    StreetCreate, StreetUpdate, StreetRead
)
import src.service.territory_service as svc

router = APIRouter(prefix="/territory", tags=["Territory"])


def register_crud(
    prefix: str,
    model_name: str,
    svc_mod,
    SchemaC: Type,
    SchemaU: Type,
    SchemaR: Type,
):
    @router.post(f"{prefix}", response_model=SchemaR)
    async def _create(data: SchemaC, db: AsyncSession = Depends(get_async_session)):
        return await getattr(svc_mod, f"create_{model_name}")(db, data)

    @router.get(f"{prefix}/", response_model=list[SchemaR])
    async def _list(db: AsyncSession = Depends(get_async_session)):
        return await getattr(svc_mod, f"get_{model_name}s")(db)

    @router.get(f"{prefix}/{{item_id}}", response_model=SchemaR)
    async def _read(item_id: int, db: AsyncSession = Depends(get_async_session)):
        item = await getattr(svc_mod, f"get_{model_name}")(db, item_id)
        if not item:
            raise HTTPException(status_code=404, detail=f"{model_name.capitalize()} not found")
        return item

    @router.put(f"{prefix}/{{item_id}}", response_model=SchemaR)
    async def _update(item_id: int, data: SchemaU, db: AsyncSession = Depends(get_async_session)):
        updated = await getattr(svc_mod, f"update_{model_name}")(db, item_id, data)
        if not updated:
            raise HTTPException(status_code=404, detail=f"{model_name.capitalize()} not found")
        return updated

    @router.delete(f"{prefix}/{{item_id}}")
    async def _delete(item_id: int, db: AsyncSession = Depends(get_async_session)):
        await getattr(svc_mod, f"delete_{model_name}")(db, item_id)
        return {"detail": f"{model_name.capitalize()} deleted"}


register_crud("/countries", "country", svc, CountryCreate, CountryUpdate, CountryRead)
register_crud("/regions", "region", svc, RegionCreate, RegionUpdate, RegionRead)
register_crud("/cities", "city", svc, CityCreate, CityUpdate, CityRead)
register_crud("/districts", "district", svc, DistrictCreate, DistrictUpdate, DistrictRead)
register_crud("/microdistricts", "microdistrict", svc, MicroDistrictCreate, MicroDistrictUpdate, MicroDistrictRead)
register_crud("/streets", "street", svc, StreetCreate, StreetUpdate, StreetRead)
