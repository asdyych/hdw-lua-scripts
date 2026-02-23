# -*- coding: utf-8 -*-
"""Fix ItemInfo.txt encoding: replace corrupted lines with correct GBK Chinese."""
import os

ITEMINFO = os.path.join(os.path.dirname(__file__), "ItemInfo.txt")

# Correct Chinese for makeup boxes (id, name_col1, note_col_last)
FIX_MAP = {
    10831: ("1级小叶子的化妆盒一千连", "1级小叶子的化妆盒一千连开,祝您好运连连!"),
    10832: ("2级小叶子的化妆盒一千连", "2级小叶子的化妆盒一千连开,祝您好运连连!"),
    10833: ("3级小叶子的化妆盒一千连", "3级小叶子的化妆盒一千连开,祝您好运连连!"),
    10834: ("4级小叶子的化妆盒一千连", "4级小叶子的化妆盒一千连开,祝您好运连连!"),
    10835: ("5级小叶子的化妆盒一千连", "5级小叶子的化妆盒一千连开,祝您好运连连!"),
    10836: ("6级小叶子的化妆盒十连", "6级小叶子的化妆盒十连开"),
    10837: ("7级小叶子的化妆盒十连", "7级小叶子的化妆盒十连开"),
    10838: ("8级小叶子的化妆盒十连", "8级小叶子的化妆盒十连开"),
    10839: ("9级小叶子的化妆盒十连", "9级小叶子的化妆盒十连开"),
    10840: ("10级小叶子的化妆盒十连", "10级小叶子的化妆盒十连开"),
    10841: ("11级小叶子的化妆盒十连", "11级小叶子的化妆盒十连开"),
    10842: ("12级小叶子的化妆盒十连", "12级小叶子的化妆盒十连开"),
    10843: ("13级小叶子的化妆盒十连", "13级小叶子的化妆盒十连开"),
    11250: ("九级3属性宝石宝箱", "双击开启后获得9级3属性宝石一个"),
    11251: ("九级4属性宝石宝箱", "双击开启后获得9级4属性宝石一个"),
}

REMOVE_IDS = {10844, 10845, 10846}


def main():
    for enc in ("gbk", "utf-8", "gb18030"):
        try:
            with open(ITEMINFO, "r", encoding=enc) as f:
                raw = f.read()
            break
        except UnicodeDecodeError:
            continue
    else:
        raise SystemExit("Cannot decode ItemInfo.txt")

    lines = raw.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    result = []
    fixed = 0
    removed = 0

    for line in lines:
        if "\t" not in line:
            result.append(line)
            continue
        parts = line.split("\t")
        try:
            iid = int(parts[0])
        except (ValueError, IndexError):
            result.append(line)
            continue

        if iid in REMOVE_IDS:
            removed += 1
            continue

        if iid in FIX_MAP:
            name, note = FIX_MAP[iid]
            parts[1] = name
            parts[-2] = note
            result.append("\t".join(parts))
            fixed += 1
        else:
            result.append(line)

    out = "\n".join(result)
    if not out.endswith("\n"):
        out += "\n"

    with open(ITEMINFO, "w", encoding="gbk", newline="\n") as f:
        f.write(out)

    print(f"Fixed {fixed} lines, removed {removed} lines, saved as GBK")


if __name__ == "__main__":
    main()
