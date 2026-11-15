---
id: learning.zephyr-docs.board-samples.page-26
title: 蓝牙活动期间写入Nordic闪存
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/nordic/flash/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="nordic-flash"></a>

# 第26章\_Nordic 蓝牙低功耗活动期间写入闪存（Nordic flash write during Bluetooth LE activity）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/nordic/flash/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/nordic/flash/README.rst/..)

<a id="overview"></a>

## 26.1 概述（Overview）

本示例在蓝牙低功耗（Bluetooth Low Energy，Bluetooth LE）无线电处于活动状态时，测试 Nordic nRF51、nRF52 和 nRF54 系列芯片的片上闪存写入。它启动可连接广播（Connectable advertising），随后对 `storage_partition` 执行一系列 [`flash_area_write()`](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gaa56052f8d6bf4f6966752bc21f5cceb8) 调用，记录每次写入的返回码与耗时。

> 译注——实际存储操作：本次 main.c 会先调用 flash_area_erase(fa, 0, fa->fa_size)，擦除整个 storage_partition，再最多写入八次、每次 64 字节。这个示例会修改分区内容；运行前必须确认该分区用途，不能在仍需保留设置或绑定数据的分区上直接试验。

同时，示例执行主动扫描（Active scanning）并打印收到的每份广播报告，在写入闪存时增加无线电资源竞争。扫描通过 [`CONFIG_BT_OBSERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_OBSERVER) 启用（默认开启）；可以在构建时关闭该选项，构建不含扫描器的示例。写入循环完成后，广播与扫描都会停止。

Flash 驱动使用闪存同步 ticker（Flash synchronization ticker），协调闪存写入与无线电活动的先后执行。如果闪存写入时隙太短，`flash_area_write` 可能在闪存超时时限到达后返回 `-ETIMEDOUT`，从而破坏蓝牙绑定信息的持久化，以及无线电活动期间执行的任何设置写入。

> 译注——观察成功与失败：err=0 表示该次 API 返回成功；-ETIMEDOUT 是超时错误。示例最终成功消息只说明这次写入循环完成，并不证明绑定持久化的全部流程通过。应同时检查广播／扫描启动与停止的错误输出。

要构建不含扫描器的版本，在构建时禁用该选项，例如：

```text
west build -b nrf54l15dk/nrf54l15/cpuapp \
  samples/boards/nordic/flash -- -DCONFIG_BT_OBSERVER=n
```

<a id="requirements"></a>

## 26.2 前提条件（Requirements）

一块 nRF51、nRF52 或 nRF54 系列 Nordic 开发板，具有片上 Flash 控制器、`storage_partition` 固定分区（Fixed partition）和 Bluetooth LE 控制器，例如：

- [nRF51 DK](https://docs.zephyrproject.org/latest/boards/nordic/nrf51dk/doc/index.html#nrf51dk)

- [nRF52840 DK](https://docs.zephyrproject.org/latest/boards/nordic/nrf52840dk/doc/index.html#nrf52840dk)

- [nRF54L15 DK](https://docs.zephyrproject.org/latest/boards/nordic/nrf54l15dk/doc/index.html#nrf54l15dk)

<a id="building-and-running"></a>

## 26.3 构建与运行（Building and Running）

> 译注——执行前提：除本页另有说明的目录外，west 命令从读者自己的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行。先准备[入门指南](../getting_started/大纲.md)所需的主机工具、west 工作区、模块与目标工具链；应用、配置及 overlay 为官方源码，构建目录由工具生成。构建成功后再按目标板文档烧录，失败时返回构建输出或板文档检查；下方日志是官方预期示例，本次未执行硬件步骤。

```text
west build -b nrf54l15dk/nrf54l15/cpuapp samples/boards/nordic/flash
west flash
```

烧录后，开发板以 `Zephyr Flash sample` 为名称广播，并在广播期间写入闪存。成功运行时的输出示例如下：

```text
*** Booting Zephyr OS build ... ***
Bluetooth LE advertising, writing to flash while radio is active
iter 0 err=0 (2 ms)
iter 1 err=0 (2 ms)
...
Successfully completed flash write while radio was active
```

<a id="see-also"></a>

## 26.4 另请参阅（See also）

[闪存（Flash）](../flash_reference/P001_Flash公共接口.md)

[通用访问配置文件（Generic Access Profile，GAP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html)

[蓝牙 API（Bluetooth APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__bluetooth.html)

> 译注——实现入口：[上游 samples/boards/nordic/flash/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/nordic/flash/src/main.c)与[上游 samples/boards/nordic/flash/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/nordic/flash/prj.conf)。仓库源码仅作参照，版本可能与本次官方页面不同；本地链接按文档位置相对解析。

对应官方文档源码：[samples/boards/nordic/flash/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/nordic/flash/README.rst)。

[上一章](P025_动态引脚控制.md) · [返回大纲](大纲.md) · [下一章](P027_Nordic_IronSide_SE固件更新.md)
