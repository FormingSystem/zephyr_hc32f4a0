---
id: learning.zephyr-docs.qemu-other-reference.page-1
title: QEMU_LEON3仿真开发板
kind: reference
status: maintained
domains: [zephyr, boards, qemu]
source_url: https://docs.zephyrproject.org/latest/boards/qemu/leon3/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_QEMU\_LEON3仿真开发板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/qemu/leon3/doc/index.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

## 1.1\_开发板概况与概述

<a id="qemu_leon3"></a>

名称：`qemu_leon3`。厂商：[Gaisler](https://docs.zephyrproject.org/latest/boards/index.html#vendor=gaisler)。状态：未积极维护（Not Actively Maintained）。架构（Architecture）：[sparc](https://docs.zephyrproject.org/latest/boards/index.html#arch=sparc)；片上系统（System on Chip，SoC）：[leon3](https://docs.zephyrproject.org/latest/boards/index.html#soc=leon3)。

<a id="board-github-link"></a>

[浏览开发板源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/boards/qemu/leon3)。

<a id="overview"></a>

LEON3 QEMU 开发板配置用于仿真（Emulation）LEON3 处理器。

<a id="programming-and-debugging"></a>

## 1.2\_编程与调试

`qemu_leon3` 支持以下运行器（Runner）及关联 west 命令：

| 运行器 | `west flash` | `west debug` | `west debugserver` |
| --- | --- | --- | --- |
| `qemu` | 支持，默认 | 支持，默认 | 支持 |

应用可按仿真开发板的通常方式构建和运行，详见[构建应用](../application/P001_应用开发.md#build-an-application)和[运行应用](https://docs.zephyrproject.org/latest/develop/application/index.html#application-run)。

<a id="flashing"></a>

虽然这是仿真开发板，不能实际“烧写”（Flash），但可以用此配置运行基本应用和内核测试。

使用此配置在 QEMU 仿真环境中运行基本 Zephyr 应用及内核测试，例如[基础同步示例（Basic Synchronization）](../basic_samples/P029_基本同步示例.md#synchronization)。从 Zephyr 仓库根目录执行；原代码注释 `From the root of the zephyr repository` 也表示这一位置。

```shell
# From the root of the zephyr repository
west build -b qemu_leon3 samples/synchronization
west build -t run
```

这会构建包含同步示例应用的镜像（Image），使用 QEMU 启动，并显示以下控制台输出：

```text
*** Booting Zephyr OS build zephyr-v2.4.0-27-g7b37fdd5303b  ***
threadA: Hello World from qemu_leon3!
threadB: Hello World from qemu_leon3!
threadA: Hello World from qemu_leon3!
threadB: Hello World from qemu_leon3!
threadA: Hello World from qemu_leon3!
threadB: Hello World from qemu_leon3!
threadA: Hello World from qemu_leon3!
threadB: Hello World from qemu_leon3!
threadA: Hello World from qemu_leon3!
threadB: Hello World from qemu_leon3!
```

按 `CTRL+A`，再按 `x` 退出 QEMU。

<a id="debugging"></a>

详细概述参见[应用调试](https://docs.zephyrproject.org/latest/develop/debug/index.html#application-debugging)。

> 译注：命令、输出和历史版本号按官方原文保留；本次翻译未运行固件，也未安装工具链。

---

[本册大纲](大纲.md) · [全站进度](../PROGRESS.md) · [下一章](P002_QEMU_MIPS_Malta仿真开发板.md)
