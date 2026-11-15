---
id: learning.zephyr-docs.audio-video-model-reference.page-50
title: uaol_ep_table_entry_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structuaol__ep__table__entry.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第50章\_uaol\_ep\_table\_entry\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structuaol__ep__table__entry.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

USB音频卸载链路（UAOL）的流端点表条目。

```c
#include <zephyr/drivers/uaol.h>
```

<a id="details"></a>

USB音频卸载链路（UAOL）的流端点表条目。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 50.1\_数据成员（Data Fields）

<a id="r_adcafe865df5890562a1bd91e3fd6117b"></a>

```c
uint32_t usb_ep_address: 5
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[usb_ep_address](#adcafe865df5890562a1bd91e3fd6117b)。

USB 端点编号。

<a id="r_af78fdd9cf09d756cfecfe5527b84d7ff"></a>

```c
uint32_t device_slot_number: 8
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[device_slot_number](#af78fdd9cf09d756cfecfe5527b84d7ff)。

槽位编号（Slot number）。

<a id="r_a3bc142e34d341ae58cbe87a9d2eaf614"></a>

```c
uint32_t split_ep: 1
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[split_ep](#a3bc142e34d341ae58cbe87a9d2eaf614)。

拆分端点（Split endpoint）标志。

## 50.2\_详细说明（Detailed Documentation）

<a id="af78fdd9cf09d756cfecfe5527b84d7ff"></a>

### `device_slot_number`

```c
uint32_t uaol_ep_table_entry::device_slot_number
```

槽位编号（Slot number）。

<a id="a3bc142e34d341ae58cbe87a9d2eaf614"></a>

### `split_ep`

```c
uint32_t uaol_ep_table_entry::split_ep
```

拆分端点（Split endpoint）标志。

<a id="adcafe865df5890562a1bd91e3fd6117b"></a>

### `usb_ep_address`

```c
uint32_t uaol_ep_table_entry::usb_ep_address
```

USB 端点编号。

本数据类型文档由以下文件生成：

- `zephyr/drivers/uaol.h`

## 50.3\_原页交叉引用（Cross References）

- [zephyr/drivers/uaol.h](https://docs.zephyrproject.org/latest/doxygen/html/uaol_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P049_uaol_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P051_video_buffer_结构体.md)
