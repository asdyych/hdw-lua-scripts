# -*- coding: utf-8 -*-
"""Fix remaining mojibake in item_browser.html"""
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(script_dir, 'item_browser.html')

with open(path, 'r', encoding='utf-8') as f:
    s = f.read()

# 鎬 + U+E046 + 墿 -> 角色
char_garbled = '\u91ac\ue046\u58bf'
s = s.replace(char_garbled, '\u89d2\u8272')

# 鏈 + 姞杞芥枃浠 + replacement char -> 未加载文件
s = s.replace('\u93de\u672a\u52a0\u8f7d\u6587\u4ef6', '\u672a\u52a0\u8f7d\u6587\u4ef6')
# Try common patterns for 未加载文件
s = s.replace('\u94fe\u59d0\u675c\u6770\u679f\u6c5f\u4e8f\ufffd', '\u672a\u52a0\u8f7d\u6587\u4ef6')
s = s.replace('\u93de\u59d0\u675c\u6770\u679f\u4e8f\ufffd', '\u672a\u52a0\u8f7d\u6587\u4ef6')

# Read file to get exact string for 鏈姞杞芥枃浠�
idx = s.find('currentFilePath')
if idx >= 0:
    snippet = s[idx:idx+80]
    # Find the garbled pattern
    for i, c in enumerate(snippet):
        if ord(c) > 0x4e00 and ord(c) < 0x9fff:
            pass  # Chinese range

# Use literal string - 鏈姞杞芥枃浠�
garbled_unloaded = '\u93de\u59d0\u675c\u6770\u679f\u4e8f'
if garbled_unloaded in s:
    s = s.replace(garbled_unloaded + '\ufffd', '\u672a\u52a0\u8f7d\u6587\u4ef6')
    s = s.replace(garbled_unloaded, '\u672a\u52a0\u8f7d\u6587\u4ef6')

# 纭淇敼 -> 确认修改
s = s.replace('\u7ebf\u786e\u8bca\u6539\u6559', '\u786e\u8ba4\u4fee\u6539')
s = s.replace('\u7eb8\u786e\u8bca\u6539', '\u786e\u8ba4\u4fee\u6539')
# 纭€€€淇€敼 
s = s.replace('\u7eb8\ufffd\ufffd\ufffd\u8bca\u6559', '\u786e\u8ba4\u4fee\u6539')

# 鏈夋湭淇濆瓨淇敼锛岀'瀹氳鍒囨崲鍚楋紵 -> 有未保存修改，确定要切换吗？
s = s.replace('\u93de\u5c4f\u672a\u6e05\u5b89\u752e\u90e6\u6559\u6539\u9509\u2c68\u2022\u6e01\u51b3\u5208\u5203\u5219\u804a\uff1f', 
              '\u6709\u672a\u4fdd\u5b58\u4fee\u6539\uff0c\u786e\u5b9a\u8981\u5207\u6362\u5417\uff1f')

# 璇峰湪宸﹀晶閫夋嫨鎬墿 -> 请在左侧选择角色
s = s.replace('\u73bb\u5c65\u5728\u5bdb\u5ff8\u6c0e\u95a2\u5ac0\u91ac\u58bf', '\u8bf7\u5728\u5de6\u4fa7\u9009\u62e9\u89d2\u8272')
s = s.replace('\u73bb\u5c65\u5728\u5bdb\u5ff8\u6c0e\u95a2\u5ac0' + char_garbled, '\u8bf7\u5728\u5de6\u4fa7\u9009\u62e9\u89d2\u8272')

with open(path, 'w', encoding='utf-8') as f:
    f.write(s)
print('Fix applied')
