# src/blueprints/apis/system_manage/function_manage/urls.py
from apiflask import APIBlueprint


function_manage_bp = APIBlueprint("function_manage", __name__, url_prefix="/function-manage")

@function_manage_bp.get("/function-manage/")
def get_functions(**kwargs):
    """
    取得功能列表
    """
    pass

@function_manage_bp.get("/function-manage/<uid>/")
def get_function(uid: str, **kwargs):
    """
    取得功能
    """
    pass

@function_manage_bp.post("/function-manage/")
def create_function(**kwargs):
    """
    建立功能
    """
    pass

@function_manage_bp.put("/function-manage/<uid>/")
def update_function(uid: str, **kwargs):
    """
    更新功能
    """
    pass
    
@function_manage_bp.delete("/function-manage/<uid>/")
def delete_function(uid: str, **kwargs):
    """
    刪除功能  
    """
    pass

@function_manage_bp.put("/function-manage/<uid>/enable/")
def enable_function(uid: str, **kwargs):
    """
    啟用功能
    """
    pass

@function_manage_bp.put("/function-manage/<uid>/disable/")
def disable_function(uid: str, **kwargs):
    """
    停用功能
    """
    pass
