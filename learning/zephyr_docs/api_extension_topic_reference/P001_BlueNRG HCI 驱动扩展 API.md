---
id: learning.zephyr-docs.api-extension-topic-reference.page-1
title: BlueNRG HCI 驱动扩展 API
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bluenrg__hci__driver.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_BlueNRG HCI 驱动扩展 API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bluenrg__hci__driver.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

BlueNRG HCI 驱动专用 API

<a id="details"></a>

BlueNRG HCI 驱动专用 API

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.1\_函数（Functions）

<a id="r_gaa76b4af2fc2076deaeeb845514475483"></a>

```c
int bluenrg_bt_reset (bool updater_mode)
```

相关声明：[bluenrg_bt_reset](#gaa76b4af2fc2076deaeeb845514475483)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

对 BlueNRG 网络协处理器（Network Coprocessor）执行硬件复位（Hardware Reset）。

## 1.2\_详细说明（Detailed Documentation）

<a id="gaa76b4af2fc2076deaeeb845514475483"></a>

### `bluenrg_bt_reset()`

```c
int bluenrg_bt_reset ( bool updater_mode)
```

```c
#include <zephyr/drivers/bluetooth/hci_driver_bluenrg.h>
```

对 BlueNRG 网络协处理器（Network Coprocessor）执行硬件复位（Hardware Reset）。

对低功耗蓝牙网络协处理器（BLE Network Coprocessor）执行硬件复位（Hardware Reset），还可以强制进入固件更新器模式（Firmware Updater Mode）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `updater_mode` | 表示是否需要进入更新器模式（Updater Mode）的标志（Flag）。 |

返回（Returns）：非负值表示成功；负错误码（Negative Error Code）表示失败。


## 1.3\_原页交叉引用（Cross References）

- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [zephyr/drivers/bluetooth/hci_driver_bluenrg.h](../api_file_supplement_reference/P042_zephyr__drivers__bluetooth__hci_driver_bluenrg.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_蓝牙控制器（Bluetooth Controller）.md)
