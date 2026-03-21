# -*- coding: utf-8 -*-
"""Fix mojibake in item_browser.html"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r'd:\hdw\什么鬼lua脚本\item_browser.html'
with open(path, 'r', encoding='utf-8') as f:
    s = f.read()

# UI / display strings (garbled -> correct)
repl = [
    ('鎬墿', '角色'),
    ('鏈姞杞芥枃浠�', '未加载文件'),
    ('璇峰湪宸︿晶閫夋嫨鎬墿', '请在左侧选择角色'),
    ('璇峰湪宸︿晶閫夋嫨物品', '请在左侧选择物品'),
    ('鎬墿列表', '角色列表'),
    ('鎬墿详情', '角色详情'),
    ('鎸塈D鎴栧悕绉版悳绱⑩€�', '按ID或名称搜索...'),
    ('鏈夋湭淇濆瓨淇敼锛岀瀹氳鍒囨崲鍚楋紵', '有未保存修改，确定要切换吗？'),
    ('淇敼浠呭湪鍐呭瓨涓敓鏁堬紝闇€鐐瑰嚮"保存文件"鍐欏叆纾佺洏', '修改仅在内存中生效，需点击"保存文件"写入磁盘'),
    ('纭淇敼', '确认修改'),
    ('鎼滅储瀛楁锛堟敮鎸佷腑鏂囧悕/鍘熷瀛楁鍚嶏級鈥�', '搜索字段(支持中文名/原始字段名)...'),
    ('鏈嶅姟鍣�', '服务器'),
    ('鉂� 璇诲彇澶辫触锛�', 'Read failed: '),
    ('鉂� 淇濆瓨澶辫触锛�', 'Save failed: '),
    ('鎵€閫夊睘鎬у潎鏃犳湁鏁堝€�', '所选属性均无效'),
    ('浠呮樉绀哄凡閫夊睘鎬э紙鍙垏鎹㈠埌鍏ㄩ儴灞炴€э級', '仅显示已选属性(可切换到全部属性)'),
    ('鍏ㄩ儴灞炴€э紙瀛楁寰堝锛屽缓璁敤鎼滅储锛�', '全部属性(字段很多，建议用搜索)'),
]
for old, new in repl:
    c = s.count(old)
    if c:
        s = s.replace(old, new)
        print(f"Replaced {c}x", flush=True)

with open(path, 'w', encoding='utf-8') as f:
    f.write(s)
print("Done")
