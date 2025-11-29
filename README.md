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
- bcrypt==5.0.0
- shortuuid==1.0.13
# 開發套件
- debugpy==1.8.17
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
        |-- blueprints/ - Route 資料夾(處理 API 路由並指向 Controller)
        |-- controllers/ - Controller 資料夾(處理 API 回應依需求指向 Logic)
        |-- logics/ - Logic 資料夾(處理請求邏輯)
        |-- cruds/ - CRUD 資料夾(處理資料庫互動邏輯)
        |-- models/ - Model 資料夾(資料庫資料模型)
        |-- services/ - Service 資料夾(通用服務邏輯)
    |-- logs/ - log 資料夾
        |-- uwsgi.log - uWSGI log 檔
    |-- README.md 專案說明文件

# 設定檔管理說明
本專案設定檔分兩層結構，其一是 settings<*>.yaml，其二是 configs.py，
- settings<*>.yaml 為專案環境變數設定檔
- configs.py 將 yaml 檔映射專案環境變數，並提供彈性派生屬性處理，例如組合 DATABASE 資料。

# 部屬說明
- 需建立 logs/uwsgi.log 
