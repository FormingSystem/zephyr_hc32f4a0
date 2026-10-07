<!-- SPDX-License-Identifier: Apache-2.0 -->

# P003_Windows 可复制操作

对应 [完整正文](../../P003_SDK准备与编译器选型_Windows.md) 与 26 页 PPT。按正文选择 GNU / Minimal、在线 / 已有包、自动发现 / 显式路径，不依次执行所有文件。PowerShell 与 UCRT64 的前提写在各文件开头。配置示例仅在 P002—P005 准备齐全后执行；它们不直接编译或运行固件。

| 完整操作 | PPT 页 | 正文位置 |
| --- | --- | --- |
| [sdk-gnu.txt](sdk-gnu.txt) | 9 | [GNU 路线：核验摘要并解压](../../P003_SDK准备与编译器选型_Windows.md#section-3-2-1) |
| [sdk-minimal.txt](sdk-minimal.txt) | 10 | [Minimal 路线：先解压 SDK 框架](../../P003_SDK准备与编译器选型_Windows.md#section-3-2-1) |
| [sdk-arm-online.txt](sdk-arm-online.txt) | 11 | [Minimal 在线补装 ARM](../../P003_SDK准备与编译器选型_Windows.md#install-arm) |
| [sdk-arm-offline.txt](sdk-arm-offline.txt) | 12 | [已有 ARM 包：直接补到 SDK/gnu](../../P003_SDK准备与编译器选型_Windows.md#install-arm) |
| [sdk-verify.txt](sdk-verify.txt) | 13 | [安装完成：核验 SDK 与 ARM GCC](../../P003_SDK准备与编译器选型_Windows.md#section-3-2-4) |
| [sdk-register.txt](sdk-register.txt) | 17 | [可选：让当前用户的工程自动发现 SDK](../../P003_SDK准备与编译器选型_Windows.md#sdk-registry) |
| [sdk-environment.txt](sdk-environment.txt) | 18 | [不注册：从当前终端传入 SDK 根](../../P003_SDK准备与编译器选型_Windows.md#sdk-environment) |
| [sdk-configure.txt](sdk-configure.txt) | 19 | [不注册：给应用配置命令传入 SDK 根](../../P003_SDK准备与编译器选型_Windows.md#sdk-configure) |
| [sdk-standalone.txt](sdk-standalone.txt) | 23 | [独立工具链：完整配置示例](../../P003_SDK准备与编译器选型_Windows.md#standalone-toolchain) |
| [sdk-evidence.txt](sdk-evidence.txt) | 24 | [配置后核对工程实际选中的工具](../../P003_SDK准备与编译器选型_Windows.md#sdk-evidence) |
