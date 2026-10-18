---
id: learning.zephyr-docs.bluetooth-samples.page-75
title: HAP助听器
kind: reference
status: maintained
domains: [zephyr, bluetooth, samples]
source_url: https://docs.zephyrproject.org/latest/samples/bluetooth/audio/hap_ha/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="bluetooth_hap_ha"></a>

# 第75章\_助听访问配置文件（Hearing Access Profile，HAP）助听器（Hearing Aid，HA）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/bluetooth/audio/hap_ha/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/audio/hap_ha/README.rst/..)

<a id="overview"></a>

## 75.1 概述（Overview）

本应用演示 LE Audio 助听器示例功能。

> 译注——角色辨认：HAUC 是助听器单播客户端，HARC 是远程控制器，两者用途不同。能发现 HAS 或建立连接，并不单独证明音频已传输、解码和播放；检查预设控制与音频流时应分别选择具备相应功能的对端。

<a id="requirements"></a>

## 75.2 前提条件（Requirements）

- 主机上运行 BlueZ，或者

- 一块支持 Bluetooth Low Energy 5.2 的开发板。

<a id="building-and-running"></a>

## 75.3 构建与运行（Building and Running）

> 译注——执行环境与前提：以下命令从读者自己的 Zephyr 源码根目录执行，实际开发板构建可使用 UCRT64 Bash 或 Linux Bash；模拟板的 Linux 可执行程序应在具备相应模拟环境的 Linux 中构建／运行。先按[入门指南](../getting_started/大纲.md)准备工具链、west 工作区和板支持，并核对所选控制器实际支持的角色及 ISO 等功能；“Bluetooth 5.2”名称本身不能代替功能核验。`samples/...` 是官方目录，`<board>` 替换为实际板目标，构建输出由工具生成。构建、烧录、发现对端、流／服务配置和收发分别检查；失败时先回查当前阶段的配置、板文档及配套角色。本次未执行固件构建、烧录或蓝牙通信。

按以下方式构建并烧录示例，将 `<board>` 替换为目标开发板，例如 [nRF5340 DK](https://docs.zephyrproject.org/latest/boards/nordic/nrf5340dk/doc/index.html#nrf5340dk)：

```text
west build -b <board> samples/bluetooth/audio/hap_ha
west flash
```

烧录后，示例以 `Hearing Aid sample` 名称开始广播，并等待助听器单播客户端（Hearing Aid Unicast Client，HAUC）或助听器远程控制器（Hearing Aid Remote Controller，HARC）连接。

详情参见[蓝牙示例（Bluetooth samples）](https://docs.zephyrproject.org/latest/samples/bluetooth/bluetooth.html#bluetooth)。

<a id="see-also"></a>

## 75.4 另请参阅（See also）

[助听访问服务（Hearing Access Service，HAS）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html)

> 译注——源码入口：[samples/bluetooth/audio/hap_ha/src/main.c](../../../samples/bluetooth/audio/hap_ha/src/main.c)；[samples/bluetooth/audio/hap_ha/prj.conf](../../../samples/bluetooth/audio/hap_ha/prj.conf)。均按所在译文解析相对链接，仓库移动后仍可跟踪；本地源码版本可能与官方快照不同。

对应官方文档源码：[samples/bluetooth/audio/hap_ha/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/bluetooth/audio/hap_ha/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/bluetooth/audio/hap_ha/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录、运行无线通信或连接设备。

[上一章](P074_CCP呼叫控制服务端.md) · [返回大纲](大纲.md) · [下一章](P076_PBP公共广播接收端.md)
