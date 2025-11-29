# src/blueprints/apis/system_manage/role_manage/urls.py
from apiflask import APIBlueprint


role_manage_bp = APIBlueprint("role_manage", __name__, url_prefix="/role-manage")

@role_manage_bp.get("/role-manage/")
def get_roles(**kwargs):
    """
    取得角色列表
    """
    pass

@role_manage_bp.get("/role-manage/<uid>/")
def get_role(uid: str, **kwargs):
    """
    取得角色
    """
    pass

@role_manage_bp.post("/role-manage/")
def create_role(**kwargs):
    """
    建立角色
    """
    pass

@role_manage_bp.put("/role-manage/<uid>/")
def update_role(uid: str, **kwargs):
    """
    更新角色
    """
    pass
    
@role_manage_bp.delete("/role-manage/<uid>/")
def delete_role(uid: str, **kwargs):
    """
    刪除角色
    """
    pass

@role_manage_bp.put("/role-manage/<uid>/enable/")
def enable_role(uid: str, **kwargs):
    """
    啟用角色
    """
    pass

@role_manage_bp.put("/role-manage/<uid>/disable/")
def disable_role(uid: str, **kwargs):
    """
    停用角色
    """
    pass

@role_manage_bp.put("/role-manage/<uid>/permissions/")
def set_role_permissions(uid: str, **kwargs):
    """
    設定角色權限(批次更新)
    """
    pass
