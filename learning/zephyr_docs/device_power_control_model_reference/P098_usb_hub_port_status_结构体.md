---
id: learning.zephyr-docs.device-power-control-model-reference.page-98
title: usb_hub_port_status_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusb__hub__port__status.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第98章\_usb\_hub\_port\_status\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusb__hub__port__status.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

USB集线器端口状态（Hub Port Status）。

```c
#include <zephyr/usb/class/usb_hub.h>
```

<a id="details"></a>

USB 集线器端口状态（Hub Port Status），参见规范表 11-21 和表 11-22。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 98.1\_数据成员（Data Fields）

<a id="r_a4e6e6bb6a2cc13c88456a4b391da3368"></a>

```c
uint16_t wPortStatus
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[wPortStatus](#a4e6e6bb6a2cc13c88456a4b391da3368)。

端口状态位图。

<a id="r_a0ce3b5e431b2153e9253c952ad49cfa1"></a>

```c
uint16_t wPortChange
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[wPortChange](#a0ce3b5e431b2153e9253c952ad49cfa1)。

端口状态变化位图。

## 98.2\_详细说明（Detailed Documentation）

<a id="a0ce3b5e431b2153e9253c952ad49cfa1"></a>

### `wPortChange`

```c
uint16_t usb_hub_port_status::wPortChange
```

端口状态变化位图。

<a id="a4e6e6bb6a2cc13c88456a4b391da3368"></a>

### `wPortStatus`

```c
uint16_t usb_hub_port_status::wPortStatus
```

端口状态位图。

本数据类型文档由以下文件生成：

- `zephyr/usb/class/usb_hub.h`

## 98.3\_原页交叉引用（Cross References）

- [zephyr/usb/class/usb_hub.h](https://docs.zephyrproject.org/latest/doxygen/html/usb__hub_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P097_usb_hub_descriptor_结构体.md) · [返回大纲](大纲.md) · [下一章](P099_usb_hub_status_结构体.md)
