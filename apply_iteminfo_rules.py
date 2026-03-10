# -*- coding: utf-8 -*-
"""Apply 0 resist/0 def and 0 atk rules to ItemInfo.txt. Output GBK."""

import re

PATH = 'ItemInfo.txt'
NAME, TYPE, LEVEL = 1, 10, 24
MIN_ATK, MAX_ATK, DEF_CONST, PHYS_RESIST, REMARK = 60, 61, 62, 73, 94

WEAPON_TYPES = set(str(x) for x in range(1, 10))
# 1-9 weapon, 11/20/22/23/24/26/27/28/29/30 armor (23=gloves, 24=boots)
WEAPON_ARMOR_TYPES = WEAPON_TYPES | {'11', '20', '22', '23', '24', '26', '27', '28', '29', '30'}

EXCLUDE_NAMES = {'\u9ed1\u9f99\u4e4b\u5fc3', '\u9ed1\u9f99\u4e4b\u9b42', '\u9ed1\u9f99\u4e4b\u77b3'}

# startswith: curse/phantom/mystery/death + ghost/undead/wraith/curse-mark/shadow
# + 濠电姷鏁告慨鎾儉婢舵劕绾ч幖瀛樻尭娴滅偓淇婇妶鍕妽闁告瑥绻橀弻锝夊箣閿濆棭妫勭紒鐐劤椤兘寮婚敐鍛傜喓绱掑Ο闀愭埛闂備浇妗ㄧ粈渚€顢栭崶顒€绠熼柟闂寸缁秹鏌涢鐘茬仼缂佷緤绠撳Λ鍛搭敃閵忊€愁槱缂備礁顑嗙敮鈥愁嚕閺屻儱绠瑰ù锝呮贡閸欏棝姊虹紒妯荤闁稿﹤婀遍埀顒佺啲閹凤拷/闂傚倸鍊搁崐鎼佸磹閹间礁纾瑰瀣捣閻棗銆掑锝呬壕濡ょ姷鍋涢ˇ鐢稿极瀹ュ绀嬫い鎰╁灮娴滀即鏌ｆ惔锛勭暛闁稿骸宕叅闁挎洖鍊稿Ч鍙夌節婵犲倸顏х紒璇叉閺屾洟宕煎┑鍥ф闂侀潻绲界紞濠囧蓟濞戙垹绠ｉ柣妯荤ゴ閺嬪懘姊洪崫鍕潶闁告梹鍨块獮鍐Χ婢跺﹦锛滃┑鐐村灦閿曗晜瀵奸敓锟�/闂傚倸鍊搁崐鎼佸磹妞嬪海鐭嗗〒姘ｅ亾妤犵偞鐗犻、鏇氱秴闁搞儺鍓﹂弫鍐煥閺囨浜鹃梺姹囧€楅崑鎾舵崲濞戙垹绠ｆ繛鍡楃箳娴犲ジ鏌熼崗鍏肩稇闁挎洦浜濠氭晬閸曨亝鍕冮柣鐘叉处瑜板啯鎱ㄦ惔锝囩＝濞达絽鎼宀勬煕閵娿儳鍩ｇ€殿喖顭锋俊鎼佸煛閸屾矮绨介梻浣呵归張顒傜矙閹达富鏁傞柨鐕傛嫹/闂傚倸鍊搁崐鎼佸磹妞嬪海鐭嗗〒姘ｅ亾妤犵偞鐗犻、鏇氱秴闁搞儺鍓﹂弫鍐煥閺囨浜鹃梺姹囧€濈粻鏍蓟閿濆憘鐔封枎閹勵唲缂傚倸鍊风拋鏌ュ疾閻樺樊鍤曢柛顐ｆ礀闁卞洦鎱ㄥ鍡楀箺闁绘繃娲熷铏圭矙鐠恒劎顔夌紓渚囧枟閹瑰洤顕ｆ繝姘╅柍鍝勫€告禍鐐烘⒑缁嬫寧婀扮紒瀣灴椤㈡棃鏁撻敓锟�/濠电姷鏁告慨鎾儉婢舵劕绾ч幖瀛樻尭娴滅偓淇婇妶鍕妽闁告瑥绻橀弻锝夊箣閿濆棭妫勭紒鐐劤椤兘寮婚敐澶婃闁圭ǹ瀛╅崕鎾绘⒑閹肩偛濡界紒璇插暣婵＄敻宕熼姘敤闂侀潧臎閸涱垰甯掗梻鍌欒兌鏋紒缁樺灩閸掓帡骞樼拠鑼舵憰闂侀潧艌閺呮粓宕戦崱娑欑厱閻忕偛澧介埥澶嬨亜韫囥儲瀚� for robe/staff
PREFIXES = ('\u8bc5\u5492\u4e4b', '\u5e7b\u7075', '\u8ff7\u4e4b', '\u6b7b\u795e',
            '\u5e7d\u7075', '\u6b7b\u7075', '\u4ea1\u7075', '\u5492\u7eb9', '\u6697\u5f71',
            '\u5e7b\u5492', '\u5492\u6587', '\u8ff7\u5492', '\u8ff7\u6cd5', '\u5e7b\u6cd5', '\u5492\u706b', '\u8ff7\u5e7b', '\u7834\u9b54', '\u8ff7\u96fe')

BATCH4_NAMES = {
    '\u8bc5\u5492\u4e4b\u7075\u94a2\u7532', '\u5492\u7eb9\u91cd\u5251', '\u5492\u7eb9\u523a\u5251',
    '\u5492\u7eb9\u7d27\u8eab\u8863', '\u8bc5\u5492\u4e4b\u543b', '\u5492\u672f\u4e4b\u6756',
    '\u8ff7\u6cd5\u4e4b\u6756', '\u7b26\u6587\u5916\u8863', '\u5e7b\u6cd5\u4e4b\u8884',
    '\u5492\u6587\u6cd5\u6756', '\u5e7b\u5316\u4e4b\u6756', '\u8ff7\u5492\u6cd5\u6756',
    '\u5492\u6587\u4e4b\u8884', '\u5e7b\u5492\u4e4b\u8884', '\u8ff7\u5492\u6cd5\u8884',
    '\u8bc5\u5492\u4e4b\u523a', '\u8ff7\u5e7b\u4e4b\u523a', '\u5492\u706b\u6597\u84df', '\u8ff7\u5e7b\u6597\u84df',
    '\u6b66\u58eb\u4e4b\u8bc5\u5492\u7eb9\u8eab',
}
BATCH4_PATTERNS = (
    '\u5e7b\u7075\u6218\u7532\u624b\u5957', '\u5e7b\u7075\u6218\u7532\u9774', '\u5e7b\u7075\u62a4\u624b',
    '\u5e7b\u7075\u62a4\u817f', '\u5e7b\u5492\u624b\u5957', '\u5e7b\u6cd5\u624b\u5957',
    '\u5e7b\u5492\u9774', '\u5e7b\u6cd5\u9774', '\u5e7b\u7075\u76ae\u624b\u5957', '\u5e7b\u7075\u62ab\u98ce',
)
BATCH3_NAMES = (
    '\u9ed1\u6697\u4f7f\u8005', '\u54c8\u8fea\u65af\u4e4b\u6cea', '\u4fee\u9f99\u4e4b\u6094\u609f',
    '\u51a5\u6cb3\u4e4b\u8a93\u8a00', '\u51a5\u9b42\u8150\u9aa8', '\u4fee\u9f99\u4e4b\u5b88\u62a4',
    '\u51a5\u6cb3\u4e4b\u8eaf\u4f53', '\u5730\u72f1\u7684\u8986\u76d6', '\u51a5\u9b42\u9644\u4f53',
    '\u9ed1\u6697\u7684\u9634\u5f71', '\u54c8\u8fea\u65af\u7684\u675f\u7f1a',
)


def norm_name(s):
    s = re.sub(r'\(A\)|\(B\)|\(\u9177\)|\u00b7\u6539', '', s)
    s = re.sub(r'^\[?\u9177\]?', '', s)
    s = re.sub(r'^(\u6dc4\u6ce5|\u70c8\u7130|\u5bd2\u51b0|\u4e0d\u6b7b|\u708e\u98d2)\u5c01\u5370\u7684', '', s)
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
    base = norm_name(name)
    t = row[TYPE]
    if t in ('31', '34', '41'):
        return False
    if t not in WEAPON_ARMOR_TYPES:
        return False
    if any(base.startswith(p) for p in PREFIXES):
        return True
    if '\u8bc5\u5492' in base:
        return True
    return False


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
