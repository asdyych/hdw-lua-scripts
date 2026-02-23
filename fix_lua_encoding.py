# -*- coding: utf-8 -*-
"""Fix Lua file encoding: convert mixed GBK/UTF-8/corrupt bytes to valid GBK."""
import os
import sys

def fix_file(path: str, output_path: str | None = None) -> None:
    """Read path, fix encoding, write as GBK. If output_path omitted, overwrites."""
    with open(path, "rb") as f:
        data = bytearray(f.read())

    result = []
    i = 0
    while i < len(data):
        if data[i] < 0x80:  # ASCII
            result.append(data[i:i+1].decode("ascii"))
            i += 1
            continue
        if i + 1 < len(data):
            try:
                result.append(data[i:i+2].decode("gbk"))
                i += 2
                continue
            except UnicodeDecodeError:
                pass
        for n in (3, 2, 1):
            if i + n <= len(data):
                try:
                    result.append(data[i:i+n].decode("utf-8"))
                    i += n
                    break
                except UnicodeDecodeError:
                    continue
        else:
            result.append(" ")  # replace unrecoverable byte
            i += 1

    out = "".join(result)
    dest = output_path or path
    with open(dest, "w", encoding="gbk", newline="") as f:
        f.write(out)
    print(f"Fixed: {path} -> {dest} (GBK)")


if __name__ == "__main__":
    for p in sys.argv[1:] or ["ItemEffect.lua"]:
        if os.path.isfile(p):
            fix_file(p)
        else:
            print(f"Skip (not file): {p}")
