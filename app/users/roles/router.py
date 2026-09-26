from fastapi import APIRouter, Depends

from app.users.roles.dao import RoleDAO
from app.users.dependencies import get_admin_user
from app.users.models import Users
from app.users.roles.schemas import SRoleAdd
from app.exceptions import RoleAlreadyExistsException


router = APIRouter(
    prefix="/roles",
    tags=["Роли"]
)


@router.post("/add_role")
async def add_role(role_data: SRoleAdd, admin_rights: Users = Depends(get_admin_user)):
    existing_role = await RoleDAO.find_one_or_none(name=role_data.name)
    if existing_role:
        raise RoleAlreadyExistsException()
    await RoleDAO.add(name=role_data.name)


@router.get("/all_roles")
async def show_all_roles(admin_rights: Users = Depends(get_admin_user)):
    result = await RoleDAO.find_all()
    return result
