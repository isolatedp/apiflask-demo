# src/services/utils/security_utils.py
import bcrypt, json, hashlib, base64


def _check_bcrypt_condition(raw_data):
    """
    驗證資料是否符合限制（最多 72 個字節）
    Args:
        raw_data: 要驗證的資料，可以是字串、列表或字典
        
    Returns:
        bool: 符合條件返回 True，否則返回 False
    """
    if isinstance(raw_data, str):
        return _check_string_bcrypt_condition(raw_data)
    elif isinstance(raw_data, list):
        result = [_check_string_bcrypt_condition(item) for item in raw_data]
        return all(result)
    elif isinstance(raw_data, dict):
        result = [_check_string_bcrypt_condition(item) for item in raw_data.values()]
        return all(result)
    else:
        return False

def _check_string_bcrypt_condition(raw_data):
    """
    驗證單個字串是否符合 bcrypt 長度限制（最多 72 個字節）
    Args:
        raw_data: 要驗證的字串
        
    Returns:
        bool: 符合條件返回 True，否則返回 False
    """
    if not isinstance(raw_data, str):
        return False
    if not raw_data.isascii():
        return False
    return len(raw_data) <= 72

def generate_hash(raw_data):
    """
    生成資料的哈希值
    Args:
        raw_data: 要生成哈希的資料，可以是字串、數字、布林值、列表或字典
        
    Returns:
        str: 生成的哈希值，如果失敗返回 False
    """
    if isinstance(raw_data, str):
        return _generate_hash_for_string(raw_data)
    elif isinstance(raw_data, (bool, int, float)):
        raw_data = str(raw_data)
        return _generate_hash_for_string(raw_data)
    elif isinstance(raw_data, (list, dict)):
        raw_data = json.dumps(raw_data, sort_keys=True)
        return _generate_hash_for_string(raw_data)
    else:
        return False
    
def _generate_hash_for_string(raw_data):
    """
    為字串生成 bcrypt 哈希值
    
    此函數會先對字串進行預處理，然後使用 bcrypt 生成安全的哈希值。
    
    Args:
        raw_data: 要生成哈希的字串
        
    Returns:
        str: 生成的哈希字串，如果輸入不是字串或處理失敗則返回 False
    """
    # 檢查輸入是否為字串類型
    if not isinstance(raw_data, str):
        return False
    
    # 預處理字串以符合 bcrypt 要求
    raw_data = _bcrypt_pre_process_for_string(raw_data)
    
    # 驗證字串是否符合 bcrypt 的長度限制
    if not _check_bcrypt_condition(raw_data):
        return False
        
    # 將字串轉換為 UTF-8 編碼的 bytes
    raw_data = raw_data.encode('utf-8')
    
    # 使用 bcrypt 生成加鹽哈希
    hash_data = bcrypt.hashpw(raw_data, bcrypt.gensalt())
    
    # 將二進制哈希值解碼為 UTF-8 字串
    hash_data = hash_data.decode('utf-8')
    
    return hash_data

def _bcrypt_pre_process_for_string(raw_data):
    """
    預處理字串資料以符合 bcrypt 要求
    Args:
        raw_data: 要預處理的字串資料
        
    Returns:
        str: 處理後的字串
    """
    raw_data = raw_data.encode('utf-8')
    # 轉成 bytes 以便 bcrypt 處理
    raw_data = hashlib.sha256(raw_data).digest()
    # 轉成 base64 URL safe
    raw_data = base64.urlsafe_b64encode(raw_data)
    # 轉回字符串
    raw_data = raw_data.decode('utf-8')
    return raw_data
    
def verify_hash(raw_data, hash_data):
    """
    驗證 raw_data 是否符合 hash_data
    """
    if isinstance(raw_data, str):
        return _verify_hash_for_string(raw_data, hash_data)
    elif isinstance(raw_data, (bool, int, float)):
        raw_data = str(raw_data)
        return _verify_hash_for_string(raw_data, hash_data)
    elif isinstance(raw_data, (list, dict)):
        raw_data = json.dumps(raw_data, sort_keys=True)
        return _verify_hash_for_string(raw_data, hash_data)
    else:
        return False

def _verify_hash_for_string(raw_data, hash_data):
    if not isinstance(raw_data, str):
        return False
    raw_data = _bcrypt_pre_process_for_string(raw_data)
    # 轉成 UTF8
    raw_data = raw_data.encode('utf-8')
    hash_data = hash_data.encode('utf-8')
    result = bcrypt.checkpw(raw_data, hash_data)
    return result
