---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-201
title: bt_hci_driver_config_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__driver__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第201章\_bt\_hci\_driver\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__driver__config.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

蓝牙 HCI 驱动通用配置（Common Driver Configuration）。

```c
#include <zephyr/drivers/bluetooth.h>
```

<a id="details"></a>

蓝牙 HCI 驱动通用配置（Common Driver Configuration）。此结构体由所有蓝牙 HCI 驱动共用，必须是设备结构体中 `config` 字段所指对象的第一个成员。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 201.1\_数据成员（Data Fields）

<a id="r_a686f78df305033c3d093958e1c374a85"></a>

```c
uint32_t quirks
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[quirks](#a686f78df305033c3d093958e1c374a85)。

此 HCI 设备实例的特殊行为标记（Quirks）。

## 201.2\_详细说明（Detailed Documentation）

<a id="a686f78df305033c3d093958e1c374a85"></a>

### `quirks`

```c
uint32_t bt_hci_driver_config::quirks
```

此 HCI 设备实例的特殊行为标记（Quirks）。

本结构体文档由以下文件生成：

- `zephyr/drivers/bluetooth.h`

## 201.3\_原页交叉引用（Cross References）

- [zephyr/drivers/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2bluetooth_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P200_bt_hci_driver_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P202_bt_hci_driver_data_结构体.md)
