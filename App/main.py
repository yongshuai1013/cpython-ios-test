# main.py — 證明跑的是完整 CPython（Termux 同級），不是閹割解釋器
import sys
import os
import platform
import json
import hashlib
import sqlite3
import sysconfig

lines = []
lines.append(f"version: {sys.version.split()[0]}")
lines.append(f"platform: {sys.platform} / {platform.machine()}")
lines.append(f"impl: {sys.implementation.name}")
lines.append(f"json: {json.dumps({'lang': 'python', 'full': True}, sort_keys=True)}")
lines.append(f"sha256('ios'): {hashlib.sha256(b'ios').hexdigest()[:16]}")

# sqlite3 是 C 擴展模組：能用就證明 lib-dynload 的 framework 化載入成立
con = sqlite3.connect(":memory:")
con.execute("create table t (x)")
con.execute("insert into t values (41), (1)")
row = con.execute("select sum(x) from t").fetchone()
lines.append(f"sqlite sum: {row[0]}")

stdlib = sysconfig.get_paths()["stdlib"]
lines.append(f"stdlib entries: {len(os.listdir(stdlib))}")
lines.append("OK - 真 CPython 在 App 內運行")
print("\n".join(lines))
