---
id: learning.zephyr-docs.qemu-catalog-reference.page-6
title: QEMU_Xtensa
kind: reference
status: maintained
domains: [zephyr, boards, qemu]
source_url: https://docs.zephyrproject.org/latest/boards/qemu/xtensa/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_QEMU\_Xtensa

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/qemu/xtensa/doc/index.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

<a id="qemu_xtensa"></a>

## 6.1\_开发板概况与概述

名称：`qemu_xtensa`。厂商：[Cadence Design Systems Inc.](https://docs.zephyrproject.org/latest/boards/index.html#vendor=cdns)。状态：持续维护（Maintained）。架构（Architecture）：[xtensa](https://docs.zephyrproject.org/latest/boards/index.html#arch=xtensa)；片上系统（SoC）：[dc233c](https://docs.zephyrproject.org/latest/boards/index.html#soc=dc233c)、[sample_controller32](https://docs.zephyrproject.org/latest/boards/index.html#soc=sample_controller32)。

<a id="board-github-link"></a>

[浏览开发板源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/boards/qemu/xtensa)。

<a id="overview"></a>

此 QEMU 开发板配置用于仿真 Xtensa 架构，为 Xtensa 仿真环境（Simulation Environment）提供支持。

<a id="programming-and-debugging"></a>

## 6.2\_编程与调试

原页列出 `qemu_xtensa` 支持的运行器（Runner）及关联 west 命令：

| 运行器 | `west flash` | `west debug` | `west debugserver` |
| --- | --- | --- | --- |
| `qemu` | 支持，默认 | 支持，默认 | 支持 |

以[基础同步示例（Basic Synchronization）](../basic_samples/P029_基本同步示例.md#synchronization)为例，下面的命令从 Zephyr 仓库根目录执行，原代码注释也表示这一位置。

```shell
# From the root of the zephyr repository
west build -b qemu_xtensa/dc233c samples/synchronization
west build -t run
```

这会构建包含同步示例的镜像（Image），使用 QEMU 启动，并显示以下控制台输出：

```text
***** BOOTING ZEPHYR OS v1.8.99 - BUILD: Jun 27 2017 13:09:26 *****
threadA: Hello World from xtensa!
threadB: Hello World from xtensa!
threadA: Hello World from xtensa!
threadB: Hello World from xtensa!
threadA: Hello World from xtensa!
threadB: Hello World from xtensa!
threadA: Hello World from xtensa!
threadB: Hello World from xtensa!
threadA: Hello World from xtensa!
threadB: Hello World from xtensa!
```

按 `CTRL+A`，再按 `x` 退出 QEMU。

<a id="debugging"></a>

详细概述参见[应用调试](https://docs.zephyrproject.org/latest/develop/debug/index.html#application-debugging)。

> 译注：命令、日志和版本号按官方示例保留，本次翻译未构建或运行固件。

---

[上一章](P005_QEMU_X86_Lakemont.md) · [本册大纲](大纲.md) · [全站进度](../PROGRESS.md)
