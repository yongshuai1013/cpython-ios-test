# cpython-ios-test

測試：完整 CPython（Termux `pkg install python` 同級的真 Python）能不能編進 iOS App。

做法：UIKit 空殼 App ＋ BeeWare Python-Apple-support 3.13-b18 的 `Python.xcframework`
（真 CPython 3.13，最低 iOS 13）＋ 官方 `install_python` 後處理（把完整標準庫搬進包內
`python/`、lib-dynload 的 .so 轉成 framework 形式）＋ 隨包 `App/main.py`。
宿主以官方 testbed 的隔離配置初始化 CPython 後執行 main.py，輸出顯示在畫面上。

main.py 的證明點：`sys.version`、`sys.platform == "ios"`、`sys.implementation.name == "cpython"`、
json／hashlib，以及 sqlite3（C 擴展模組）查詢——全過才算真 CPython 定案。

未簽名構建：後處理跳過 codesign，裝機走 TrollStore（安裝時統一簽名）。
