# src/configs.py
import os
import yaml
from dotenv import load_dotenv

class ConfigLoader:
    """
    設定檔載入器
    """
    def __init__(self):
        self._setup_mode()
        self.paths = self._setup_paths(self.app_mode)
        settings_file_path = self.paths["settings_file_path"]
        self.settings = self._load_settings(settings_file_path)
        
    def _setup_mode(self):
        """
        設定專案模式
        """
        self.app_mode = os.getenv("APP_MODE", "prod")
        
        if self.app_mode not in ["prod", "dev"]:
            raise ValueError("專案啟動發生錯誤，請檢查 APP_MODE 環境變數是否正確。")
        
    def _setup_paths(self, app_mode: str = "prod") -> dict:
        """
        設定專案路徑
        """
        # 取得當前文件的父目錄(即程式根目錄)
        app_path = os.path.dirname(os.path.abspath(__file__))
        # 取得程式根目錄的父目錄(即專案根目錄)
        project_path = os.path.dirname(app_path)
        # 取得設定檔路徑
        settings_path = os.path.join(project_path, "settings")
        settings_filename = "settings"
        if app_mode == "dev":
            settings_filename += "-dev"
        settings_filename += ".yaml"
        settings_file = os.path.join(settings_path, settings_filename)
        
        return {
            "app_path": app_path,
            "project_path": project_path,
            "settings_file_path": settings_file,
        }
    
    def _load_settings(self, settings_file_path: str) -> dict:
        """
        載入設定檔
        """
        with open(settings_file_path, "r") as f:
            settings = yaml.safe_load(f)
        return settings
    
class Configs:
    """
    設定檔
    """
    _loader = ConfigLoader()
    _settings = _loader.settings
    
    # 專案環境變數
    APP_MODE = _loader.app_mode
    
    # 專案路徑資訊
    PROJECT_PATH = _loader.paths["project_path"]
    APP_PATH = _loader.paths["app_path"]
    SETTINGS_FILE_PATH = _loader.paths["settings_file_path"]
    
    # 專案時區
    APP_TIMEZONE = _settings.get("APP_TIMEZONE", "Asia/Taipei")
    
    # FLASK
    SECRET_KEY = _settings.get("SECRET_KEY", None)
    
    # FLASK-JWT-EXTENDED
    JWT_SECRET_KEY = _settings.get("JWT_SECRET_KEY", None)
    JWT_ACCESS_TOKEN_EXPIRES = _settings.get("JWT_ACCESS_TOKEN_EXPIRES", 4 * 60 * 60)
    JWT_REFRESH_TOKEN_EXPIRES = _settings.get("JWT_REFRESH_TOKEN_EXPIRES", 8 * 60 * 60)
    
    # FLASK-CORS
    CORS_ORIGINS = _settings.get("CORS_ORIGINS", ["*"])
    
    # FLASK-SQLALCHEMY
    
    # AES 安全編碼
    AES_SECRET_KEY = _settings.get("AES_SECRET_KEY", None)
    