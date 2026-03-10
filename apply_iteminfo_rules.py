# -*- coding: utf-8 -*-
"""Apply 0 resist/0 def and 0 atk rules to ItemInfo.txt. Output GBK."""

import re

PATH = 'ItemInfo.txt'
NAME, TYPE, LEVEL = 1, 10, 24
MIN_ATK, MAX_ATK, DEF_CONST, PHYS_RESIST, REMARK = 60, 61, 62, 73, 94

WEAPON_TYPES = set(str(x) for x in range(1, 10))
WEAPON_ARMOR_TYPES = WEAPON_TYPES | {'11', '20', '22', '26', '27', '28', '29', '30'}

EXCLUDE_NAMES = {'\u9ed1\u9f99\u4e4b\u5fc3', '\u9ed1\u9f99\u4e4b\u9b42', '\u9ed1\u9f99\u4e4b\u77b3'}

PREFIXES = ('\u8bc5\u5492\u4e4b', '\u5e7d\u7075', '\u8ff7\u4e4b', '\u6b7b\u795e')

BATCH4_NAMES = {
    '\u8bc5\u5492\u4e4b\u7075\u94a2\u7532', '\u5492\u7eb9\u91cd\u5251', '\u5492\u7eb9\u523a\u5251',
    '\u5492\u7eb9\u7d27\u8eab\u8863', '\u8bc5\u5492\u4e4b\u543b', '\u5492\u672f\u4e4b\u6756',
    '\u8ff7\u6cd5\u4e4b\u6756', '\u7b26\u6587\u5916\u8863', '\u5e7d\u6cd5\u4e4b\u8884',
    '\u5492\u6587\u6cd5\u6756', '\u5e7d\u5316\u4e4b\u6756', '\u8ff7\u5492\u6cd5\u6756',
    '\u5492\u6587\u4e4b\u8884', '\u5e7d\u5492\u4e4b\u8884', '\u8ff7\u5492\u6cd5\u8884',
    '\u8bc5\u5492\u4e4b\u523a', '\u8ff7\u5e7d\u4e4b\u523a', '\u5492\u706b\u6597\u84df', '\u8ff7\u5e7d\u6597\u84df',
}
BATCH4_PATTERNS = (
    '\u5e7d\u7075\u6218\u7532\u624b\u5957', '\u5e7d\u7075\u6218\u7532\u9774', '\u5e7d\u7075\u62a4\u624b',
    '\u5e7d\u7075\u62a4\u817f', '\u5e7d\u5492\u624b\u5957', '\u5e7d\u6cd5\u624b\u5957',
    '\u5e7d\u5492\u9774', '\u5e7d\u6cd5\u9774', '\u5e7d\u7075\u76ae\u624b\u5957',
)
BATCH3_NAMES = (
    '\u9ed1\u6697\u4f7f\u8005', '\u54c8\u8fea\u65af\u4e4b\u6cea', '\u4fee\u9f99\u4e4b\u6094\u609f',
    '\u51a5\u6cb3\u4e4b\u8a93\u8a00', '\u51a5\u9b42\u8150\u9aa8', '\u4fee\u9f99\u4e4b\u5b88\u62a4',
    '\u51a5\u6cb3\u4e4b\u8eaf\u4f53', '\u5730\u72f1\u7684\u8986\u76d6', '\u51a5\u9b42\u9644\u4f53',
    '\u9ed1\u6697\u7684\u9634\u5f71', '\u54c8\u8fea\u65af\u7684\u675f\u7f1a',
)


def norm_name(s):
    s = re.sub(r'\(A\)|\(B\)|\(\u9177\)|\u00b7\u6539', '', s)
    s = re.sub(r'^(\u6dc4\u6ce5|\u70c8\u7130|\u5bd2\u51b0)\u5c01\u5370\u7684', '', s)
    s = re.sub(r'^\u5f3a\u5316-', '', s)
    return s.strip()


def is_weapon(t):
    return t in WEAPON_TYPES


def need_0_resist_def(row):
    name = row[NAME]
    if name in EXCLUDE_NAMES:
        return False
    if '\u5e74\u517d' in name or '\u8f69\u714c' in name:
        return True
    if '\u9ed1\u9f99' in name:
        return True
    try:
        lv = int(row[LEVEL])
        rem = row[REMARK] if len(row) > REMARK else ''
        if lv >= 45 and 'boss' in rem.lower():
            return True
    except (ValueError, IndexError):
        pass
    return False


def need_prefix(row):
    name = row[NAME]
    t = row[TYPE]
    if t in ('31', '34', '41'):
        return False
    if t not in WEAPON_ARMOR_TYPES:
        return False
    return any(name.startswith(p) for p in PREFIXES)


def need_batch3(row):
    name = norm_name(row[NAME])
    for bn in BATCH3_NAMES:
        if bn in name or name.startswith(bn):
            return True
    return False


def need_batch4(row):
    name = row[NAME]
    base = norm_name(name)
    for n in BATCH4_NAMES:
        if n in base or base.startswith(n) or n in name:
            return True
    for p in BATCH4_PATTERNS:
        if p in name:
            return True
    return False


def main():
    with open(PATH, 'r', encoding='gbk') as f:
        lines = f.readlines()
    if not lines:
        return
    header = lines[0]
    data = [l.rstrip('\n').split('\t') for l in lines[1:]]
    changes_r, changes_a = [], []
    for i, row in enumerate(data):
        if len(row) <= max(REMARK, PHYS_RESIST):
            continue
        name = row[NAME]
        t = row[TYPE]
        need_r = need_0_resist_def(row) or need_prefix(row) or need_batch3(row) or need_batch4(row)
        if need_r:
            if row[PHYS_RESIST] != '0,0':
                row[PHYS_RESIST] = '0,0'
                changes_r.append((i + 2, name, 'phys'))
            if row[DEF_CONST] != '0,0':
                row[DEF_CONST] = '0,0'
                changes_r.append((i + 2, name, 'def'))
        if need_r and is_weapon(t):
            if row[MIN_ATK] != '0,0':
                row[MIN_ATK] = '0,0'
                changes_a.append((i + 2, name))
            if row[MAX_ATK] != '0,0':
                row[MAX_ATK] = '0,0'
                changes_a.append((i + 2, name))
    with open(PATH, 'w', encoding='gbk', newline='') as f:
        f.write(header)
        for row in data:
            f.write('\t'.join(row) + '\n')
    print('0resist/0def:', len(changes_r), ' 0atk:', len(changes_a))


if __name__ == '__main__':
    main()
