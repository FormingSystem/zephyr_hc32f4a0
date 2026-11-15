---
id: learning.zephyr-docs.bluetooth-samples.page-81
title: TMAP外设
kind: reference
status: maintained
domains: [zephyr, bluetooth, samples]
source_url: https://docs.zephyrproject.org/latest/samples/bluetooth/audio/tmap_peripheral/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="ble_peripheral_tmap_peripheral"></a>

# 第81章\_电话与媒体音频配置文件（Telephone and Media Audio Profile，TMAP）外设（Peripheral）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/bluetooth/audio/tmap_peripheral/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/bluetooth/audio/tmap_peripheral/README.rst/..)

<a id="overview"></a>

## 81.1 概述（Overview）

本应用演示 TMAP 外设功能，实现 CT 和 UMR 角色。

<a id="requirements"></a>

## 81.2 前提条件（Requirements）

- 一块支持 Bluetooth Low Energy 5.2 的开发板。

<a id="building-and-running"></a>

## 81.3 构建与运行（Building and Running）

> 译注——执行环境与前提：以下命令从读者自己的 Zephyr 源码根目录执行，实际开发板构建可使用 UCRT64 Bash 或 Linux Bash；模拟板的 Linux 可执行程序应在具备相应模拟环境的 Linux 中构建／运行。先按[入门指南](../getting_started/大纲.md)准备工具链、west 工作区和板支持，并核对所选控制器实际支持的角色及 ISO 等功能；“Bluetooth 5.2”名称本身不能代替功能核验。`samples/...` 是官方目录，`<board>` 替换为实际板目标，构建输出由工具生成。构建、烧录、发现对端、流／服务配置和收发分别检查；失败时先回查当前阶段的配置、板文档及配套角色。本次未执行固件构建、烧录或蓝牙通信。

按以下方式构建并烧录示例，将 `<board>` 替换为目标开发板，例如 [nRF5340 DK](https://docs.zephyrproject.org/latest/boards/nordic/nrf5340dk/doc/index.html#nrf5340dk)：

```text
west build -b <board> samples/bluetooth/audio/tmap_peripheral
west flash
```

烧录后，示例初始化 TMAP 呼叫终端（Call Terminal，CT）和单播媒体接收器（Unicast Media Receiver，UMR）角色，然后以 `TMAP Peripheral` 名称开始广播。TMAP 中心设备连接并建立安全关系后，示例发现对端的 TMAP 角色：若对端为呼叫网关（CG），则发送“发起呼叫”（originate call）请求，并在 2 秒后终止；若对端为单播媒体发送器（UMS），则发送“播放媒体”（play media）请求，并在 2 秒后暂停。

> 译注——条件触发与计时：本次源码在角色发现后分别检查 CG 和 UMS，二者同时存在时可分别触发呼叫与媒体控制。两秒通过延迟工作项调度终止／暂停请求，不能据此推断对端一定已执行成功；应核对请求返回及后续状态。这里的呼叫和媒体操作是本示例行为，不是 TMAP 对所有外设的固定启动动作。

在另一块开发板上运行[电话与媒体音频配置文件（Telephone and Media Audio Profile，TMAP）中心设备（Central）](P080_TMAP中心设备.md#ble_peripheral_tmap_central)示例，充当 TMAP 中心设备，承担 CG 和 UMS 角色。

详情参见[蓝牙示例（Bluetooth samples）](https://docs.zephyrproject.org/latest/samples/bluetooth/bluetooth.html#bluetooth)。

<a id="see-also"></a>

## 81.4 另请参阅（See also）

[蓝牙 API（Bluetooth APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__bluetooth.html)

[蓝牙音频（Bluetooth Audio）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html)

[蓝牙基本音频配置文件（Bluetooth Basic Audio Profile）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html)

[协调集识别配置文件（Coordinated Set Identification Profile，CSIP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html)

[媒体控制客户端（Media Control Client，MCC）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html)

[电话承载服务（Telephone Bearer Service，TBS）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html)

[电话与媒体音频配置文件（Telephone and Media Audio Profile，TMAP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tmap.html)

[音量控制配置文件（Volume Control Profile，VCP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html)

> 译注——源码入口：[samples/bluetooth/audio/tmap_peripheral/src/main.c](../../../samples/bluetooth/audio/tmap_peripheral/src/main.c)；[samples/bluetooth/audio/tmap_peripheral/prj.conf](../../../samples/bluetooth/audio/tmap_peripheral/prj.conf)。均按所在译文解析相对链接，仓库移动后仍可跟踪；本地源码版本可能与官方快照不同。

对应官方文档源码：[samples/bluetooth/audio/tmap_peripheral/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/bluetooth/audio/tmap_peripheral/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/bluetooth/audio/tmap_peripheral/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录、运行无线通信或连接设备。

[上一章](P080_TMAP中心设备.md) · [返回大纲](大纲.md) · [下一章](P082_蓝牙音频示例目录.md)
