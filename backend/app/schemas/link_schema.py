from pydantic import BaseModel, HttpUrl, Field, validator
from typing import Optional
import re

class LinkRequest(BaseModel):
    originalUrl: HttpUrl
    expireAt: Optional[str] = None
    customCode: Optional[str] = None

    @validator("customCode")
    def validate_custom_code(cls, code):
        # Settings(Các settings này cho customCode có thể để riêng ở file cài đặt sau)
        minLength = 2
        maxLength = 30
        
        # P0. Nếu customCode bỏ trống thì ko cần check
        if code is None or code == "":
            return code
        
        # P1. Check độ dài của customCode (code = customCode nhận được)
        if (len(code) < minLength) or (len(code) > maxLength):
            raise ValueError(f"Độ dài của mã rút gọn phải nằm trong khoảng từ {minLength} đến {maxLength} kí tự")
        
        # P2. Check customCode có kí tự không hợp lệ
        pattern = r"^[A-Za-z0-9\-]+$"
        if not re.fullmatch(pattern, code):
            raise ValueError("Mã rút gọn chỉ được chứa chữ cái hoa/thường, số hoặc dấu '-'")
        
        # P3. Check customCode có vị trí dấu '-' không thoả mãn
        if (code[0] == '-') or (code[len(code) - 1] == '-'):
            raise ValueError("Mã rút gọn không được có dấu '-' ở đầu hoặc ở cuối")
        if ("--" in code):
            raise ValueError("Mã rút gọn không được có hai hay nhiều dấu '-' nằm kề nhau")
        
        # Thoả mãn thì trả về customCode
        return code

class LinkResponse(BaseModel):
    shortUrl: str
    qrCode: str