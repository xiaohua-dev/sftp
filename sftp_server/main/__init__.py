import sys
import os
Base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(Base_dir)

__all__ = ['Json_handle']

bb= {
    "name": "xiaopeng",
    "password": "76cd438bd0e8899a61aff632ace54dbb",
    "path": "/home/xiaopeng",
    "space": 0 }

aa = Json_handle("xx",bb).ReadJson()
print(aa)
