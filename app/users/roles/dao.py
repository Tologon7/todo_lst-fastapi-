from app.dao.base import BaseDAO
from app.users.roles.models import Role


class RoleDAO(BaseDAO):
    model = Role
