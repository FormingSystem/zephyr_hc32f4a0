<!-- SPDX-License-Identifier: Apache-2.0 -->

# P003_Windows 可复制操作

> 历史命令附件：保留原编号与实验记录。Markdown 已重排，当前操作从 [大纲](../../大纲.md) 和 [当前命令索引](../current/README.md) 进入。

对应 [完整正文](../../P005_SDK准备与编译器选型.md)。按正文选择 GNU / Minimal、在线 / 已有包、自动发现 / 显式路径，不依次执行所有文件。PowerShell 与 UCRT64 的前提写在各文件开头。配置示例仅在 P002—P005 准备齐全后执行；它们不直接编译或运行固件。

| 完整操作 | 正文位置 |
| --- | --- |
| [sdk-gnu.txt](sdk-gnu.txt) | [GNU 路线：核验摘要并解压](../../P005_SDK准备与编译器选型.md#section-5-2-1) |
| [sdk-minimal.txt](sdk-minimal.txt) | [Minimal 路线：先解压 SDK 框架](../../P005_SDK准备与编译器选型.md#section-5-2-1) |
| [sdk-arm-online.txt](sdk-arm-online.txt) | [Minimal 在线补装 ARM](../../P005_SDK准备与编译器选型.md#install-arm) |
| [sdk-arm-offline.txt](sdk-arm-offline.txt) | [已有 ARM 包：直接补到 SDK/gnu](../../P005_SDK准备与编译器选型.md#install-arm) |
| [sdk-verify.txt](sdk-verify.txt) | [安装完成：核验 SDK 与 ARM GCC](../../P005_SDK准备与编译器选型.md#section-5-2-4) |
| [sdk-register.txt](sdk-register.txt) | [可选：让当前用户的工程自动发现 SDK](../../P005_SDK准备与编译器选型.md#sdk-registry) |
| [sdk-environment.txt](sdk-environment.txt) | [不注册：从当前终端传入 SDK 根](../../P005_SDK准备与编译器选型.md#sdk-environment) |
| [sdk-configure.txt](sdk-configure.txt) | [不注册：给应用配置命令传入 SDK 根](../../P005_SDK准备与编译器选型.md#sdk-configure) |
| [sdk-standalone.txt](sdk-standalone.txt) | [独立工具链：完整配置示例](../../P005_SDK准备与编译器选型.md#standalone-toolchain) |
| [sdk-evidence.txt](sdk-evidence.txt) | [配置后核对工程实际选中的工具](../../P005_SDK准备与编译器选型.md#sdk-evidence) |
| [west-git-check.txt](west-git-check.txt) | [west 下载前的 Git 检查](../../P005_SDK准备与编译器选型.md#west-git-handoff) |
