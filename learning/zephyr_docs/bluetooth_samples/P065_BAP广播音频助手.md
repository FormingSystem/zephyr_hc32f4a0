---
id: learning.zephyr-docs.bluetooth-samples.page-65
title: BAP广播音频助手
kind: reference
status: maintained
domains: [zephyr, bluetooth, samples]
source_url: https://docs.zephyrproject.org/latest/samples/bluetooth/audio/bap_broadcast_assistant/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="bluetooth_bap_broadcast_assistant"></a>

# 第65章\_基本音频配置文件（Basic Audio Profile，BAP）广播音频助手（Broadcast Audio Assistant）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/bluetooth/audio/bap_broadcast_assistant/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/audio/bap_broadcast_assistant/README.rst/..)

<a id="overview"></a>

## 65.1 概述（Overview）

本应用演示 BAP 广播助手（Broadcast Assistant）功能。

> 译注——三个角色：广播助手通过 BASS 帮助扫描委托端选择广播源，本身不等同于转发音频的中继。完整演示还需要[广播音频接收端](P066_BAP广播音频接收端.md)和[广播音频源](P067_BAP广播音频源.md)；接收端声明 PACS／BASS 与源端声明广播 ID 是两类发现条件。

示例会自动尝试连接担任 BAP 扫描委托端（Scan Delegator）的设备，该设备在广播中声明支持广播音频扫描服务（Broadcast Audio Scan Service，BASS）。随后示例搜索广播源；若找到，就将广播 ID 添加到 BAP 扫描委托端。

实际使用本示例需要一个接收端，例如 BAP 广播音频接收端示例或支持 BAP 广播的耳塞，以及一个源端，例如 BAP 广播音频源示例。

通用信息请参阅[蓝牙示例（Bluetooth samples）](https://docs.zephyrproject.org/latest/samples/bluetooth/bluetooth.html#bluetooth)。

<a id="requirements"></a>

## 65.2 前提条件（Requirements）

- 主机上运行 BlueZ，或者

- 一块支持 Bluetooth Low Energy 5.2 的开发板。

- 广播音频源端和接收端设备。

<a id="building-and-running"></a>

## 65.3 构建与运行（Building and Running）

> 译注——执行环境与前提：以下命令从读者自己的 Zephyr 源码根目录执行，实际开发板构建可使用 UCRT64 Bash 或 Linux Bash；模拟板的 Linux 可执行程序应在具备相应模拟环境的 Linux 中构建／运行。先按[入门指南](../getting_started/大纲.md)准备工具链、west 工作区和板支持，并核对所选控制器实际支持的角色及 ISO 等功能；“Bluetooth 5.2”名称本身不能代替功能核验。`samples/...` 是官方目录，`<board>` 替换为实际板目标，构建输出由工具生成。构建、烧录、发现对端、流／服务配置和收发分别检查；失败时先回查当前阶段的配置、板文档及配套角色。本次未执行固件构建、烧录或蓝牙通信。

应用充当广播助手，可预先配置广播接收端和广播源的名称过滤条件。默认情况下，应用搜索并连接找到的第一个广播音频接收端，其广播包含 PACS 和 BASS 的 UUID；然后搜索并选择找到的第一个广播音频源，其广播包含广播 ID。

修改以下配置以进行过滤：

> 译注——过滤匹配：本次 main.c 用子字符串方式检查名称；源端可匹配蓝牙设备名或广播名，接收端检查蓝牙设备名。修改 Kconfig 字符串后须重新配置构建；名称过滤不能代替广播 ID、服务发现与实际连接状态的核对。

`CONFIG_SELECT_SINK_NAME`：接收端蓝牙名称中的子字符串。

以及

`CONFIG_SELECT_SOURCE_NAME`：源端蓝牙名称或广播名称中的子字符串。

<a id="building-for-an-nrf52840dk"></a>

### 65.3.1 为 nrf52840dk 构建（Building for an nrf52840dk）

```text
# From the root of the zephyr repository
west build -b nrf52840dk/nrf52840 samples/bluetooth/audio/bap_broadcast_assistant/
```

<a id="see-also"></a>

## 65.4 另请参阅（See also）

[蓝牙 API（Bluetooth APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__bluetooth.html)

[蓝牙音频（Bluetooth Audio）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html)

[蓝牙基本音频配置文件（Bluetooth Basic Audio Profile）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html)

[连接管理（Connection management）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html)

> 译注——源码入口：[samples/bluetooth/audio/bap_broadcast_assistant/src/main.c](../../../samples/bluetooth/audio/bap_broadcast_assistant/src/main.c)；[samples/bluetooth/audio/bap_broadcast_assistant/prj.conf](../../../samples/bluetooth/audio/bap_broadcast_assistant/prj.conf)。均按所在译文解析相对链接，仓库移动后仍可跟踪；本地源码版本可能与官方快照不同。

对应官方文档源码：[samples/bluetooth/audio/bap_broadcast_assistant/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/bluetooth/audio/bap_broadcast_assistant/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/bluetooth/audio/bap_broadcast_assistant/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录、运行无线通信或连接设备。

[上一章](P064_等时连接基准测试.md) · [返回大纲](大纲.md) · [下一章](P066_BAP广播音频接收端.md)
