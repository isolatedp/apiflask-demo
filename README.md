# 開發環境
- Windows 11 x64
- WSL
- Python 3.13
- pyenv
- uv
# 專案套件
- python-dotenv==1.2.1
- pytz==2025.2
- pyyaml==6.0.3
- uwsgi==2.0.31
- apiflask==3.0.2
    # 專案結構
    -- Project Root/ - 專案資料夾
        |-- .gitignore 排除版控設定檔
        |-- .python-version python 版本檔案
        |-- pyproject.toml python 套件設定檔
        |-- uv.lock python 套件設定檔(固定版本用)
        |-- .flaskenv 專案環境變數設定檔
        |-- docker/ - Docker Image 資料夾
            |-- Dockerfile - Docker Image 設定檔
        |-- docker-compose.yaml Docker Container 設定檔
        |-- settings/ - 設定檔資料夾
            |-- settings.yaml Product 設定檔
            |-- settings-dev.yaml Development 設定檔
            |-- settings-example.yaml 參考設定檔
            |-- uwsgi.ini - uWSGI 設定檔
        |-- src/ 程式代碼資料夾
            |-- app.py - Flask 主程式
            |-- configs.py - Flask 設定檔
            |-- wsgi.py - WSGI 主程式
        |-- logs/ - log 資料夾
            |-- uwsgi.log - uWSGI log 檔
        |-- README.md 專案說明文件

# 部屬說明
- 需建立 logs/uwsgi.log 
