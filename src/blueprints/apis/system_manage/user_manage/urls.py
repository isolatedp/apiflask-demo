# src/blueprints/apis/system_manage/user_manage/urls.py
from apiflask import APIBlueprint


user_manage_bp = APIBlueprint("user_manage", __name__, url_prefix="/user-manage")

@user_manage_bp.get("/user-manage/")
def get_users(**kwargs):
    """
    取得使用者列表
    """
    pass

@user_manage_bp.get("/user-manage/<uid>/")
def get_user(uid: str, **kwargs):
    """
    取得使用者
    """
    pass

@user_manage_bp.post("/user-manage/")
def create_user(**kwargs):
    """
    建立使用者
    """
    pass

@user_manage_bp.put("/user-manage/<uid>/")
def update_user(uid: str, **kwargs):
    """
    更新使用者
    """
    pass
    
@user_manage_bp.delete("/user-manage/<uid>/")
def delete_user(uid: str, **kwargs):
    """
    刪除使用者
    """
    pass

@user_manage_bp.put("/user-manage/<uid>/enable/")
def enable_user(uid: str, **kwargs):
    """
    啟用使用者
    """
    pass

@user_manage_bp.put("/user-manage/<uid>/disable/")
def disable_user(uid: str, **kwargs):
    """
    停用使用者
    """
    pass

@user_manage_bp.put("/user-manage/<uid>/reset-password/")
def reset_password(uid: str, **kwargs):
    """
    重置密碼
    """
    pass

@user_manage_bp.put("/user-manage/<uid>/change-password/")
def change_password(uid: str, **kwargs):
    """
    更改密碼
    """
    pass

@user_manage_bp.put("/user-manage/<uid>/roles/")
def set_user_roles(uid: str, **kwargs):
    """
    設定使用者角色(批次更新)
    """
    pass
