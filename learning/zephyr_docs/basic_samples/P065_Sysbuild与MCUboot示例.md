---
id: learning.zephyr-docs.basic_samples.page-65
title: Sysbuild与MCUboot示例
kind: reference
status: maintained
domains: [zephyr, basic_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/sysbuild/with_mcuboot/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="with_mcuboot"></a>

# 第65章\_Sysbuild与MCUboot示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/sysbuild/with_mcuboot/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 65.1 概述（Overview）

本示例演示通过系统构建（Sysbuild）构建应用时，如何自动将MCUboot作为引导加载程序（Bootloader）加入构建。它还展示如何创建针对特定镜像的Kconfig配置片段，调整额外镜像的配置。

<a id="sysbuild-specific-settings"></a>

## 65.2 Sysbuild专用设置（Sysbuild specific settings）

通过Sysbuild构建时，此示例会自动加入MCUboot。这由Sysbuild专用Kconfig配置文件`sysbuild.conf`实现：其中的`SB_CONFIG_BOOTLOADER_MCUBOOT=y`在系统构建时启用引导加载程序。

`sysbuild/mcuboot.conf`作为附加片段，与MCUboot默认配置文件合并。原文说明，该文件调整MCUboot日志等级、禁止版本降级，并将其配置为仅升级模式（Upgrade-only mode）。

使用`west`为`reel_board`同时构建示例与MCUboot：

```sh
west build -b reel_board --sysbuild samples/sysbuild/with_mcuboot
```

执行输出：

```text
*** Booting Zephyr OS build v3.2.0-rc3-209-gdcf4201d3573  ***
*** Booting Zephyr OS build v3.2.0-rc3-209-gdcf4201d3573  ***
Address of sample 0xc000
Hello sysbuild with mcuboot! nrf52840dk
```

第一行`Booting Zephyr OS build`由MCUboot自身打印，之后的行由`with_mcuboot`示例打印。示例还会打印自身在闪存（Flash）中的位置。

> 译注——配置归属与日志：当前`sysbuild.conf`还设置`SB_CONFIG_MCUBOOT_MODE_OVERWRITE_ONLY=y`，由Sysbuild控制覆盖式升级（Overwrite-only）模式；当前`sysbuild/mcuboot.conf`设置的是日志等级与防降级选项。原文将这些设置概括在同一片段中，具体归属应以所用版本为准。原命令目标是`reel_board`，展示日志却来自`nrf52840dk`；`0xc000`同样只是该示例日志中的闪存位置，不能当成所有开发板固定地址。这些是目标固件信息，不是本地仓库路径。


> 译注——实现依据：[samples/sysbuild/with_mcuboot/sysbuild.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sysbuild/with_mcuboot/sysbuild.conf)、[samples/sysbuild/with_mcuboot/sysbuild/mcuboot.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sysbuild/with_mcuboot/sysbuild/mcuboot.conf)。这些链接对应本次核对的官方main来源，内容会随分支变化，所保存快照的摘要见[来源记录](../SOURCES.md)。下方本仓库源码仅用于版本对照。

对应官方文档源码：[samples/sysbuild/with_mcuboot/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sysbuild/with_mcuboot/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/sysbuild/with_mcuboot/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/sysbuild/with_mcuboot/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P064_Sysbuild多板目标问候示例.md) · [返回大纲](大纲.md) · [下一章](P066_外部模块示例目录.md)
