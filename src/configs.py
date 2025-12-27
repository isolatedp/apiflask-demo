# src/configs.py
import os
from pathlib import Path
from urllib.parse import quote_plus

import yaml
from dotenv import load_dotenv


class ConfigLoader:
    def __init__(self):
        self._setup_mode()
        self.paths = self._setup_paths()
        settings_file_path = self.paths.get('settings_file_path')
        self.settings = self._load_settings(settings_file_path)
        self._setup_database()

    def _setup_mode(self):
        load_dotenv()
        self.app_mode = os.getenv('APP_MODE', 'prod')

    def _setup_paths(self):
        app_mode = self.app_mode
        app_path = os.path.dirname(os.path.abspath(__file__))
        app_path = Path(app_path)
        project_path = app_path.parent
        log_path = os.path.join(project_path, "logs/app")
        settings_path = os.path.join(project_path, "settings")

        if app_mode not in ['prod', 'dev']:
            app_mode = 'prod'

        if app_mode == 'prod':
            settings_file_name = 'settings.yaml'
        elif app_mode == 'dev':
            settings_file_name = 'settings_dev.yaml'
        settings_file_path = os.path.join(settings_path, settings_file_name)
        return {
            'project_path': project_path,
            'app_path': app_path,
            'log_path': log_path,
            'settings_path': settings_path,
            'settings_file_path': settings_file_path
        }

    def _load_settings(self, file_path):
        settings = {}
        with open(file_path, 'r', encoding='utf-8') as f:
            settings = yaml.safe_load(f)
        return settings

    def _setup_database(self):
        database_config = self.settings.get('DATABASE', {})
        multi_flag = False

        # 確認是否有設定主資料庫
        if 'DEFAULT' not in database_config:
            raise ValueError("DEFAULT database configuration is required")
        
        # 確認是否有多個資料庫設定
        if len(database_config) > 1:
            multi_flag = True

        # 處理主資料庫設定
        default_db = database_config['DEFAULT']
        default_url = self._generate_database_url(default_db)
        self.settings['SQLALCHEMY_DATABASE_URI'] = default_url
        self.settings['SQLALCHEMY_ENGINE_OPTIONS'] = self._generate_engine_options(default_url)

        if multi_flag:
            # TODO 處理多資料庫設定
            pass

    def _generate_database_url(self, db_config):
        db_type = db_config.get('DB_TYPE')
        if not db_type:
            raise ValueError("DB_TYPE is required in database configuration")

        if db_type in ['mysql', 'mariadb']:
            host = db_config.get('HOST', 'localhost')
            port = db_config.get('PORT', '3306')
            user = db_config.get('USER', 'root')
            pwd = quote_plus(db_config.get('PWD', ''))
            db_name = db_config.get('DB_NAME', '')
            return f"mysql+pymysql://{user}:{pwd}@{host}:{port}/{db_name}"

    def _generate_engine_options(self, db_url):
        engine_options = {
            'pool_pre_ping': True,
        }

        if db_url.startswith('mysql'):
            engine_options.update({
                'pool_size': 3,
                'max_overflow': 6,
                'pool_timeout': 30,
                'pool_recycle': 1800,
            })
        elif db_url.startswith('sqlite'):
            engine_options.update({
                "connect_args": {"check_same_thread": False},
            })

        return engine_options

class Configs:
    _loader = ConfigLoader()
    _settings = _loader.settings

    # 專案環境變數
    APP_MODE = _loader.app_mode

    # 專案路徑資訊
    PROJECT_PATH = _loader.paths.get('project_path')
    APP_PATH = _loader.paths.get('app_path')
    SETTINGS_FILE_PATH = _loader.paths.get('settings_file_path')

    # 專案時區
    APP_TIMEZONE = _settings.get('APP_TIMEZONE', 'UTC')

    # FLASK
    SECRET_KEY = _settings.get('SECRET_KEY')

    # FLASK_JWT_EXTENDED
    JWT_SECRET_KEY = _settings.get("JWT_SECRET_KEY", None)
    JWT_ACCESS_TOKEN_EXPIRES = _settings.get("JWT_ACCESS_TOKEN_EXPIRES", 4 * 60 * 60) # 4 hours
    JWT_REFRESH_TOKEN_EXPIRES = _settings.get("JWT_REFRESH_TOKEN_EXPIRES", 8 * 60 * 60) # 8 hours

    # FLASK-CORS
    CORS_ORIGINS = _settings.get("CORS_ORIGINS", [])

    # FLASK-SQLALCHEMY
    SQLALCHEMY_DATABASE_URI = _settings.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ENGINE_OPTIONS = _settings.get("SQLALCHEMY_ENGINE_OPTIONS", {})
    bind_data = _settings.get("SQLALCHEMY_BINDS", {})
    if bind_data:
        SQLALCHEMY_BINDS = bind_data
    
    # AES 安全編碼
    AES_SECRET_KEY = _settings.get("AES_SECRET_KEY", None)
