---
id: learning.zephyr-docs.device-power-control-model-reference.page-99
title: usb_hub_status_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusb__hub__status.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第99章\_usb\_hub\_status\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusb__hub__status.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

USB集线器状态（Hub Status）。

```c
#include <zephyr/usb/class/usb_hub.h>
```

<a id="details"></a>

USB 集线器状态（Hub Status），参见规范表 11-19 和表 11-20。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 99.1\_数据成员（Data Fields）

<a id="r_a9207edfd7adca1ab7339b3169595c96a"></a>

```c
uint16_t wHubStatus
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[wHubStatus](#a9207edfd7adca1ab7339b3169595c96a)。

集线器状态位图。

<a id="r_a69a3d6303815aef12358eb1f7da3d710"></a>

```c
uint16_t wHubChange
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[wHubChange](#a69a3d6303815aef12358eb1f7da3d710)。

集线器状态变化位图。

## 99.2\_详细说明（Detailed Documentation）

<a id="a69a3d6303815aef12358eb1f7da3d710"></a>

### `wHubChange`

```c
uint16_t usb_hub_status::wHubChange
```

集线器状态变化位图。

<a id="a9207edfd7adca1ab7339b3169595c96a"></a>

### `wHubStatus`

```c
uint16_t usb_hub_status::wHubStatus
```

集线器状态位图。

本数据类型文档由以下文件生成：

- `zephyr/usb/class/usb_hub.h`

## 99.3\_原页交叉引用（Cross References）

- [zephyr/usb/class/usb_hub.h](https://docs.zephyrproject.org/latest/doxygen/html/usb__hub_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P098_usb_hub_port_status_结构体.md) · [返回大纲](大纲.md) · [下一章](P100_usbc_ppc_driver_api_结构体.md)
