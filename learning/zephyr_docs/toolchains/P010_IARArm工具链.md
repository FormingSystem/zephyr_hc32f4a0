---
id: learning.zephyr-docs.toolchains.tc_iar
title: IAR Arm工具链
kind: reference
status: maintained
domains: [zephyr, toolchains]
source_url: https://docs.zephyrproject.org/latest/develop/toolchains/iar_arm_toolchain.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_IAR Arm工具链

原文：[IAR Arm工具链](https://docs.zephyrproject.org/latest/develop/toolchains/iar_arm_toolchain.html)。本次读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 10.1\_安装与配置

在主机上下载并安装 [IAR Arm 工具链](https://www.iar.com/products/architectures/arm/) v9.70 或更新版本，可选择 IAR Embedded Workbench 或 IAR Build Tools，以及永久许可证（Perpetual Licensing）或订阅许可证（Subscription Licensing）。

确保主机已安装 [Zephyr SDK](P002_ZephyrSDK.md)。设置以下[环境变量](P003_环境变量.md)：

- `ZEPHYR_TOOLCHAIN_VARIANT` 设为 `iar`。
- `IAR_TOOLCHAIN_PATH` 设为工具链安装目录。

使用云许可证（Cloud License）的版本，需要把 `IAR_LMS_BEARER_TOKEN` 设为有效的许可证持有者令牌（license bearer token），用于订阅许可。

Linux 默认安装路径示例：

```bash
# Linux (default installation path):
export IAR_TOOLCHAIN_PATH=/opt/iar/cxarm-<version>/arm
export ZEPHYR_TOOLCHAIN_VARIANT=iar
export IAR_LMS_BEARER_TOKEN="<BEARER-TOKEN>"
```

Windows 命令提示符示例：

```bat
# Windows:
set IAR_TOOLCHAIN_PATH=c:\<path>\cxarm-<version>\arm
set ZEPHYR_TOOLCHAIN_VARIANT=iar
set IAR_LMS_BEARER_TOKEN="<BEARER-TOKEN>"
```

> 译注：示例中的 `<version>`、`<path>` 与 `<BEARER-TOKEN>` 是占位符。官方安装路径示意不绑定本仓库位置。本页没有执行安装或设置许可证令牌。

## 10.2\_已知限制（Known Limitations）

- IAR 工具链使用 `ilink` 链接，依赖 Zephyr 的 `CMAKE_LINKER_GENERATOR`。`ilink` 与面向 GNU ld 的 Zephyr 链接脚本模板不兼容。
- 汇编文件（`.S-files`，即扩展名为 `.S` 的文件）使用 Zephyr SDK 随附的 GNU 汇编器（GNU Assembler）。
- C 库仅支持 Minimal libc，不支持 C++。
- 某些 Zephyr 子系统或模块可能包含依赖 GNU 内建功能（GNU Intrinsics）的 C 或汇编代码，尚未更新为与 `iar` 完全兼容。
- 不支持 TrustedFirmware。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：自定义CMake工具链](P009_自定义CMake工具链.md) · [本模块主线目录](../reading/toolchains.md) · [全部主线](../reading/README.md) · [下一篇：嵌入式链接器（ELD）](P011_嵌入式链接器ELD.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P009_自定义CMake工具链.md) · [返回大纲](大纲.md) · [下一章](P011_嵌入式链接器ELD.md)

</details>

<!-- reading-navigation:end -->
