# 协作材料改写（q11）

## Issue

**空白 name 参数时程序未报错**

- 环境：Windows（具体版本待确认）、Python 3.12
- 复现命令：`sdt-greet --name " "`
- 期望结果：以退出码 2 结束并输出参数校验错误
- 实际结果：输出 `Hello,      !`，退出码 0

## 提交信息

fix: 拒绝空白 name 参数并返回退出码 2

在 main() 中增加空白校验：name 仅含空白字符时调用 p.error()，
使程序以 SystemExit(2) 结束；同时补充回归测试 test_blank_name_exits_2。

## 评审意见

- Blocking：空白 name 仍输出问候语并以 0 退出，与 CLI 参数契约不符，
  脚本会误判调用成功；建议合并空白校验修复并补充测试。
- Suggestion：输出前对 name 统一去首尾空白，避免前端传参差异导致显示不一致。
