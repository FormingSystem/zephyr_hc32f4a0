---
id: learning.zephyr-docs.device-power-control-model-reference.page-33
title: mfd_npm10xx_event_callback_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmfd__npm10xx__event__callback.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第33章\_mfd\_npm10xx\_event\_callback\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmfd__npm10xx__event__callback.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

NPM10xx多功能设备（MFD）的回调结构。

```c
#include <zephyr/drivers/mfd/npm10xx.h>
```

<a id="details"></a>

nPM10xx 多功能设备（MFD）回调结构体。用于在驱动实例的回调链表中注册回调。只要各回调使用不同的 `struct mfd_npm10xx_event_callback` 指针，就可以按需添加任意多个回调。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 33.1\_数据成员（Data Fields）

<a id="r_a7a94c66197c7339cbeff18e99106ff9d"></a>

```c
sys_snode_t node
```

相关声明：[sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)、[node](#a7a94c66197c7339cbeff18e99106ff9d)。

供驱动内部使用。

<a id="r_a778f6145e68bf2c371b1700c4586630b"></a>

```c
npm10xx_event_t event_mask
```

相关声明：[npm10xx_event_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gab2a9bae08f020392e33bfb98efff2f32)、[event_mask](#a778f6145e68bf2c371b1700c4586630b)。

回调所关注的一组事件。

<a id="r_a8056fcfbc6c04118502a67b90c301124"></a>

```c
npm10xx_callback_handler_t handler
```

相关声明：[npm10xx_callback_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga917abc6c5ed263f28a04bc96598d0009)、[handler](#a8056fcfbc6c04118502a67b90c301124)。

所指定的任意事件发生时调用的函数。

## 33.2\_详细说明（Detailed Documentation）

<a id="a778f6145e68bf2c371b1700c4586630b"></a>

### `event_mask`

```c
npm10xx_event_t mfd_npm10xx_event_callback::event_mask
```

回调所关注的一组事件。

可以将任意数量的 `NPM10XX_EVENT_*` 宏按位或（Bitwise OR）组合而成。

<a id="a8056fcfbc6c04118502a67b90c301124"></a>

### `handler`

```c
npm10xx_callback_handler_t mfd_npm10xx_event_callback::handler
```

所指定的任意事件发生时调用的函数。

<a id="a7a94c66197c7339cbeff18e99106ff9d"></a>

### `node`

```c
sys_snode_t mfd_npm10xx_event_callback::node
```

供驱动内部使用。

不要在应用程序中使用。

本数据类型文档由以下文件生成：

- `zephyr/drivers/mfd/npm10xx.h`

## 33.3\_原页交叉引用（Cross References）

- [zephyr/drivers/mfd/npm10xx.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mfd_2npm10xx_8h_source.html)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [npm10xx_event_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#gab2a9bae08f020392e33bfb98efff2f32)
- [npm10xx_callback_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__npm10xx.html#ga917abc6c5ed263f28a04bc96598d0009)
- [mfd_npm10xx_event_callback](P033_mfd_npm10xx_event_callback_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P032_mfd_adp5585_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P034_msosv2_ccgp_device_结构体.md)
