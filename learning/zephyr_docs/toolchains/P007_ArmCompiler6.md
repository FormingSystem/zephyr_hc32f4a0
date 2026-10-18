---
id: learning.zephyr-docs.toolchains.tc_arm6
title: Arm Compiler 6
kind: reference
status: maintained
domains: [zephyr, toolchains]
source_url: https://docs.zephyrproject.org/latest/develop/toolchains/arm_compiler_6.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_Arm Compiler 6

原文：[Arm Compiler 6](https://docs.zephyrproject.org/latest/develop/toolchains/arm_compiler_6.html)。本次读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 7.1\_安装与环境变量

下载并安装适用于当前操作系统、包含 [Arm Compiler 6](https://developer.arm.com/tools-and-software/embedded/arm-compiler/downloads/version-6) 的开发套件（Development Suite）。

设置以下[环境变量（Environment Variable）](P003_环境变量.md)：

- 将 `ZEPHYR_TOOLCHAIN_VARIANT` 设为 `armclang`。
- 将 `ARMCLANG_TOOLCHAIN_PATH` 设为工具链安装目录。

Arm Compiler 6 需要用 `ARMLMD_LICENSE_FILE` 指向许可证文件（License File）或许可证服务器（License Server）。

Linux、macOS 的许可证文件和服务器设置示例：

```bash
# Linux, macOS, license file:
export ARMLMD_LICENSE_FILE=/<path>/license_armds.dat
# Linux, macOS, license server:
export ARMLMD_LICENSE_FILE=8224@myserver
```

Windows 命令提示符（Command Prompt）的对应示例：

```bat
# Windows, license file:
set ARMLMD_LICENSE_FILE=c:\<path>\license_armds.dat
# Windows, license server:
set ARMLMD_LICENSE_FILE=8224@myserver
```

如果 Arm Compiler 6 随 Arm Development Studio 安装，还必须将 `ARM_PRODUCT_DEF` 指向产品定义文件（Product Definition File）。另见[产品与工具包配置](https://developer.arm.com/tools-and-software/software-development-tools/license-management/resources/product-and-toolkit-configuration)。例如，Arm Development Studio 安装在 `/opt/armds-2020-1`，使用 Gold 许可证时，应将 `ARM_PRODUCT_DEF` 指向 `/opt/armds-2020-1/gold.elmap`。

> 译注：以上路径是官方示例及占位符，需对应读者实际安装位置；它们不是本仓库的固定位置，也不要求更改仓库所在盘符。这里保留原始命令供对照，未执行安装或许可证配置。

## 7.2\_已知支持边界

**注意：**Arm Compiler 6 使用 `armlink` 链接，它与面向 GNU ld 的 Zephyr 链接脚本模板（Linker Script Template）不兼容。Zephyr 对 Arm Compiler 6 的支持使用 CMake 链接脚本生成器（CMake Linker Script Generator），能够生成散布加载文件（Scatter File）。基础散布加载支持已经具备，但 ld 模板覆盖的某些功能，生成器尚未完全支持。

部分 Zephyr 子系统或模块还可能包含依赖 GNU 内建功能（GNU Intrinsics）的 C 或汇编代码，尚未更新为与 `armclang` 完全兼容。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：主机工具链](P006_主机工具链.md) · [本模块主线目录](../reading/toolchains.md) · [全部主线](../reading/README.md) · [下一篇：Arm嵌入式工具链（ATfE）](P008_Arm嵌入式工具链.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P006_主机工具链.md) · [返回大纲](大纲.md) · [下一章](P008_Arm嵌入式工具链.md)

</details>

<!-- reading-navigation:end -->
