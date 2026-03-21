# -*- coding: utf-8 -*-
"""Comprehensive mojibake fix for item_browser.html"""
import os
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'item_browser.html')

with open(path, 'r', encoding='utf-8') as f:
    s = f.read()

count = 0
# (garbled_pattern, correct_text) - try multiple variants for problematic chars
pairs = [
    # 鎬 + U+E006/CANCEL TAG or U+E046 + 墿 -> 角色
    (chr(0x91AC) + chr(0xE006) + chr(0x58BF), '\u89d2\u8272'),
    (chr(0x91AC) + chr(0xE046) + chr(0x58BF), '\u89d2\u8272'),
    # 鏈姞杞芥枃浠� (various endings)
    ('\u93de\u59d0\u675c\u6770\u679f\u6c5f\ufffd', '\u672a\u52a0\u8f7d\u6587\u4ef6'),
    ('\u94fe\u59d0\u675c\u6770\u679f\u6c5f\ufffd', '\u672a\u52a0\u8f7d\u6587\u4ef6'),
    # 纭淇敼
    ('\u7eb8\u8bca\u6559', '\u786e\u8ba4\u4fee\u6539'),
    # 链夋湭淇濆瓨淇敼锛岀瀹氳鍒囨崲鍚楋紵
    ('\u93de\u5c4f\u672a\u6e05\u5b89\u752e\u90e6\u6559\u6539\u9509\u2c68\u2022\u6e01\u51b2\u5208\u5203\u5219\u804a\uff1f', 
     '\u6709\u672a\u4fdd\u5b58\u4fee\u6539\uff0c\u786e\u5b9a\u8981\u5207\u6362\u5417\uff1f'),
    # 璇峰湪宸︿晶閫夋嫨鎬 + special + 墿
    ('\u73bb\u5c65\u5728\u5bdb\u5ff8\u6c0e\u95a2\u5ac0' + chr(0x91AC) + chr(0xE006) + chr(0x58BF), 
     '\u8bf7\u5728\u5de6\u4fa7\u9009\u62e9\u89d2\u8272'),
    ('\u73bb\u5c65\u5728\u5bdb\u5ff8\u6c0e\u95a2\u5ac0' + chr(0x91AC) + chr(0xE046) + chr(0x58BF), 
     '\u8bf7\u5728\u5de6\u4fa7\u9009\u62e9\u89d2\u8272'),
]
for old, new in pairs:
    n = s.count(old)
    if n:
        s = s.replace(old, new)
        count += n

# Also try without the special char - maybe it's just 鎬墿 in some encodings
s = s.replace('\u91ac\u58bf', '\u89d2\u8272')
s = s.replace('\u93de\u59d0\u675c\u6770\u679f\u6c5f', '\u672a\u52a0\u8f7d\u6587\u4ef6')

with open(path, 'w', encoding='utf-8') as f:
    f.write(s)
print('Replaced', count, 'patterns')
