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
        # 取得當前文件的路徑
        current_file_path = os.path.dirname(os.path.abspath(__file__))
        # 取得當前文件的父目錄(即程式根目錄)
        app_path = os.path.dirname(current_file_path)
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
    
Configs = ConfigLoader().settings
