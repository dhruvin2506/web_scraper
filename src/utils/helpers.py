import re
from typing import Optional
from urllib.parse import urljoin

def clean_text(text: str) -> str:
    if not text:
        return ""
    return re.sub(r'\s+', ' ', text.strip())

def build_url(base_url: str, path: str) -> str:
    return urljoin(base_url, path)

def extract_price(text: Optional[str]) -> Optional[float]:
    if not text:
        return None
    matches = re.findall(r'\d+\.?\d*', text)
    return float(matches[0]) if matches else None