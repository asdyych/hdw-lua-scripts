# -*- coding: utf-8 -*-
"""Append new ItemInfo entries with GBK encoding to preserve Chinese."""
import os

def main():
    path = os.path.join(os.path.dirname(__file__), "ItemInfo.txt")
    for enc in ("gbk", "gb18030", "gb2312", "utf-8"):
        try:
            with open(path, "r", encoding=enc) as f:
                lines = f.readlines()
            break
        except UnicodeDecodeError:
            continue
    else:
        raise SystemExit("Cannot decode ItemInfo.txt")

    # Use 10825 as template for makeup boxes (cols: 0=id, 1=name, 2=icon, 12=price, -7=ItemUse, -1=note)
    idx_10825 = next((i for i, l in enumerate(lines) if l.startswith("10825\t")), None)
    if idx_10825 is None:
        raise SystemExit("10825 not found")
    template_10825 = lines[idx_10825].rstrip("\n\r").split("\t")

    makeup_entries = [
        (10831, "1级小叶子的化妆盒一千连", "xyzhzh01q", "50000000", "ItemUse_10801q", "1级小叶子的化妆盒一千连开,祝您好运连连!"),
        (10832, "2级小叶子的化妆盒一千连", "xyzhzh02q", "100000000", "ItemUse_10802q", "2级小叶子的化妆盒一千连开,祝您好运连连!"),
        (10833, "3级小叶子的化妆盒一千连", "xyzhzh03q", "200000000", "ItemUse_10803q", "3级小叶子的化妆盒一千连开,祝您好运连连!"),
        (10834, "4级小叶子的化妆盒一千连", "xyzhzh04q", "400000000", "ItemUse_10804q", "4级小叶子的化妆盒一千连开,祝您好运连连!"),
        (10835, "5级小叶子的化妆盒一千连", "xyzhzh05q", "800000000", "ItemUse_10805q", "5级小叶子的化妆盒一千连开,祝您好运连连!"),
        (10836, "6级小叶子的化妆盒十连", "xyzhzh06x", "0", "ItemUse_10806x", "6级小叶子的化妆盒十连开"),
        (10837, "7级小叶子的化妆盒十连", "xyzhzh07x", "0", "ItemUse_10807x", "7级小叶子的化妆盒十连开"),
        (10838, "8级小叶子的化妆盒十连", "xyzhzh08x", "0", "ItemUse_10808x", "8级小叶子的化妆盒十连开"),
        (10839, "9级小叶子的化妆盒十连", "xyzhzh09x", "0", "ItemUse_10809x", "9级小叶子的化妆盒十连开"),
        (10840, "10级小叶子的化妆盒十连", "xyzhzh10x", "0", "ItemUse_10810x", "10级小叶子的化妆盒十连开"),
        (10841, "11级小叶子的化妆盒十连", "xyzhzh11x", "0", "ItemUse_10811x", "11级小叶子的化妆盒十连开"),
        (10842, "12级小叶子的化妆盒十连", "xyzhzh12x", "0", "ItemUse_10812x", "12级小叶子的化妆盒十连开"),
        (10843, "13级小叶子的化妆盒十连", "xyzhzh13x", "0", "ItemUse_10813x", "13级小叶子的化妆盒十连开"),
    ]
    # Find ItemUse column index: first col that starts with "ItemUse_"
    idx_use = next(i for i, v in enumerate(template_10825) if v.startswith("ItemUse_"))
    new_makeup = []
    for did, name, icon, price, use, note in makeup_entries:
        t = template_10825[:]
        t[0], t[1], t[2] = str(did), name, icon
        t[22] = price
        t[idx_use] = use
        t[-2] = note  # note column (last col is often empty, note is -2)
        new_makeup.append("\t".join(t) + "\n")

    for j, newline in enumerate(new_makeup):
        lines.insert(idx_10825 + 1 + j, newline)

    # Use 11208 as template for gem boxes
    idx_11208 = next((i for i, l in enumerate(lines) if l.startswith("11208\t")), None)
    if idx_11208 is None:
        raise SystemExit("11208 not found")
    template_11208 = lines[idx_11208].rstrip("\n\r").split("\t")

    gem_entries = [
        (11250, "九级3属性宝石宝箱", "nyola3q", "ItemUse_3sxbox9", "双击开启后获得9级3属性宝石一个"),
        (11251, "九级4属性宝石宝箱", "nyola4q", "ItemUse_4sxbox9", "双击开启后获得9级4属性宝石一个"),
    ]
    idx_use_gem = next(i for i, v in enumerate(template_11208) if v.startswith("ItemUse_"))
    new_gems = []
    for did, name, icon, use, note in gem_entries:
        t = template_11208[:]
        t[0], t[1], t[2] = str(did), name, icon
        t[idx_use_gem] = use
        t[-2] = note
        new_gems.append("\t".join(t) + "\n")

    insert_after_11208 = idx_11208 + 1 + len(new_makeup)
    for j, newline in enumerate(new_gems):
        lines.insert(insert_after_11208 + j, newline)

    # Write with GBK to match original
    with open(path, "w", encoding="gbk", newline="\n") as f:
        f.writelines(lines)
    print("ItemInfo.txt updated with GBK encoding")

if __name__ == "__main__":
    main()
