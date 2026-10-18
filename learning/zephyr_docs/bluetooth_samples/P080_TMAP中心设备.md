---
id: learning.zephyr-docs.bluetooth-samples.page-80
title: TMAP中心设备
kind: reference
status: maintained
domains: [zephyr, bluetooth, samples]
source_url: https://docs.zephyrproject.org/latest/samples/bluetooth/audio/tmap_central/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="ble_peripheral_tmap_central"></a>

# 第80章\_电话与媒体音频配置文件（Telephone and Media Audio Profile，TMAP）中心设备（Central）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/bluetooth/audio/tmap_central/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/audio/tmap_central/README.rst/..)

<a id="overview"></a>

## 80.1 概述（Overview）

本应用演示 TMAP 中心设备功能，实现 CG 和 UMS 角色。

> 译注——复合角色：此处 CG 是呼叫网关，UMS 是单播媒体发送器，它们是 TMAP 角色；GAP Central 则是连接角色。本例组合了这些角色，并与[TMAP 外设](P081_TMAP外设.md)配合。安全建立、角色发现、媒体／呼叫控制和音频流配置应分别检查。

<a id="requirements"></a>

## 80.2 前提条件（Requirements）

- 一块支持 Bluetooth Low Energy 5.2 的开发板。

<a id="building-and-running"></a>

## 80.3 构建与运行（Building and Running）

> 译注——执行环境与前提：以下命令从读者自己的 Zephyr 源码根目录执行，实际开发板构建可使用 UCRT64 Bash 或 Linux Bash；模拟板的 Linux 可执行程序应在具备相应模拟环境的 Linux 中构建／运行。先按[入门指南](../getting_started/大纲.md)准备工具链、west 工作区和板支持，并核对所选控制器实际支持的角色及 ISO 等功能；“Bluetooth 5.2”名称本身不能代替功能核验。`samples/...` 是官方目录，`<board>` 替换为实际板目标，构建输出由工具生成。构建、烧录、发现对端、流／服务配置和收发分别检查；失败时先回查当前阶段的配置、板文档及配套角色。本次未执行固件构建、烧录或蓝牙通信。

按以下方式构建并烧录示例，将 `<board>` 替换为目标开发板，例如 [nRF5340 DK](https://docs.zephyrproject.org/latest/boards/nordic/nrf5340dk/doc/index.html#nrf5340dk)：

```text
west build -b <board> samples/bluetooth/audio/tmap_central
west flash
```

烧录后，示例初始化 TMAP 呼叫网关（Call Gateway，CG）和单播媒体发送器（Unicast Media Sender，UMS）角色，然后扫描在广播中声明支持 UMR 的 TMAP 外设。连接后，它执行安全交互并配置单播音频流。

在另一块开发板上运行[电话与媒体音频配置文件（Telephone and Media Audio Profile，TMAP）外设（Peripheral）](P081_TMAP外设.md#ble_peripheral_tmap_peripheral)示例，充当 TMAP 外设，承担 CT 和 UMR 角色。

详情参见[蓝牙示例（Bluetooth samples）](https://docs.zephyrproject.org/latest/samples/bluetooth/bluetooth.html#bluetooth)。

<a id="see-also"></a>

## 80.4 另请参阅（See also）

[蓝牙 API（Bluetooth APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__bluetooth.html)

[蓝牙音频（Bluetooth Audio）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html)

[蓝牙基本音频配置文件（Bluetooth Basic Audio Profile）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html)

[通用音频配置文件（Common Audio Profile，CAP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html)

[连接管理（Connection management）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html)

[电话承载服务（Telephone Bearer Service，TBS）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html)

[电话与媒体音频配置文件（Telephone and Media Audio Profile，TMAP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tmap.html)

[音量控制配置文件（Volume Control Profile，VCP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html)

> 译注——源码入口：[samples/bluetooth/audio/tmap_central/src/main.c](../../../samples/bluetooth/audio/tmap_central/src/main.c)；[samples/bluetooth/audio/tmap_central/prj.conf](../../../samples/bluetooth/audio/tmap_central/prj.conf)。均按所在译文解析相对链接，仓库移动后仍可跟踪；本地源码版本可能与官方快照不同。

对应官方文档源码：[samples/bluetooth/audio/tmap_central/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/bluetooth/audio/tmap_central/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/bluetooth/audio/tmap_central/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录、运行无线通信或连接设备。

[上一章](P079_TMAP广播媒体发送器.md) · [返回大纲](大纲.md) · [下一章](P081_TMAP外设.md)
