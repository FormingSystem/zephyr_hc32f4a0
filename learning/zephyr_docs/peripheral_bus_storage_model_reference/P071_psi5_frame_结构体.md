---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-71
title: psi5_frame_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structpsi5__frame.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第71章\_psi5\_frame\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structpsi5__frame.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

外设传感器接口5（PSI5）的帧结构。

```c
#include <zephyr/drivers/psi5/psi5.h>
```

<a id="details"></a>

外设传感器接口5（PSI5）的帧结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 71.1\_数据成员（Data Fields）

<a id="r_a975b56a545604103687679c2cb0561eb"></a>

```c
enum psi5_frame_type type
```

相关声明：[psi5_frame_type](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface.html#ga5cb0ef3be35e9ff2d05c39cc17f2659f)、[type](#a975b56a545604103687679c2cb0561eb)。

PSI5 帧类型。

```c
union {
```

<a id="r_a7f7e8e22280ee01c0e5cfdce2b962ff3"></a>

```c
uint32_t data
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[data](#a159d66a7eeee3ffc6714f5058ddeefe9)。

消息数据。

```c
struct {
```

<a id="r_a9f9f047a1ac6c6034292d7c803b548e9"></a>

```c
uint8_t id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[id](#ad32ba54088b03cbd4b91e77d9adadec8)。

串行消息（Serial message）ID。

<a id="r_a1f88fd62651e4a054cc687fa3290b613"></a>

```c
uint16_t data
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[data](#abdca8ada802a3352e2da439736f7f2aa)。

串行消息数据。

<a id="r_a2f51a019cf89410b35559de925049f66"></a>

```c
} serial
```

相关声明：[serial](#a04a7d9d8d1238c823d787543ba2188c3)。

串行消息。

<a id="r_ae445da12a7cecf3c30b73ae94efec38b"></a>

```c
};
```

帧载荷（Frame payload）。

<a id="r_a3b7f3b38ab831e2789c326a327a05e53"></a>

```c
uint32_t timestamp
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[timestamp](#a3b7f3b38ab831e2789c326a327a05e53)。

捕获该帧时的时间戳（Timestamp）。

<a id="r_abd146305031fa97378b96d46e3e6e97d"></a>

```c
uint8_t crc
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[crc](#abd146305031fa97378b96d46e3e6e97d)。

用于验证消息完整性的循环冗余校验（CRC）校验值。

<a id="r_aec97ec5f2ebef6903fd0b98d8fd2bec4"></a>

```c
uint8_t slot_number
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[slot_number](#aec97ec5f2ebef6903fd0b98d8fd2bec4)。

时隙编号（Slot number）。

## 71.2\_详细说明（Detailed Documentation）

<a id="ae445da12a7cecf3c30b73ae94efec38b"></a>

### `[union]`

```c
union { ... } psi5_frame
```

帧载荷（Frame payload）。

有效成员取决于 `type`。

<a id="abd146305031fa97378b96d46e3e6e97d"></a>

### `crc`

```c
uint8_t psi5_frame::crc
```

用于验证消息完整性的循环冗余校验（CRC）校验值。

<a id="abdca8ada802a3352e2da439736f7f2aa"></a>

### `data [1/2]`

```c
uint16_t psi5_frame::data
```

串行消息数据。

<a id="a159d66a7eeee3ffc6714f5058ddeefe9"></a>

### `data [2/2]`

```c
uint32_t psi5_frame::data
```

消息数据。

<a id="ad32ba54088b03cbd4b91e77d9adadec8"></a>

### `id`

```c
uint8_t psi5_frame::id
```

串行消息（Serial message）ID。

<a id="a04a7d9d8d1238c823d787543ba2188c3"></a>

### `[struct]`

```c
struct { ... } psi5_frame::serial
```

串行消息。

<a id="aec97ec5f2ebef6903fd0b98d8fd2bec4"></a>

### `slot_number`

```c
uint8_t psi5_frame::slot_number
```

时隙编号（Slot number）。

<a id="a3b7f3b38ab831e2789c326a327a05e53"></a>

### `timestamp`

```c
uint32_t psi5_frame::timestamp
```

捕获该帧时的时间戳（Timestamp）。

<a id="a975b56a545604103687679c2cb0561eb"></a>

### `type`

```c
enum psi5_frame_type psi5_frame::type
```

PSI5 帧类型。

本数据类型文档由以下文件生成：

- `zephyr/drivers/psi5/psi5.h`

## 71.3\_原页交叉引用（Cross References）

- [zephyr/drivers/psi5/psi5.h](https://docs.zephyrproject.org/latest/doxygen/html/psi5_8h_source.html)
- [psi5_frame_type](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface.html#ga5cb0ef3be35e9ff2d05c39cc17f2659f)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [psi5_frame](P071_psi5_frame_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P070_psi5_driver_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P072_psi5_rx_callback_config_结构体.md)
