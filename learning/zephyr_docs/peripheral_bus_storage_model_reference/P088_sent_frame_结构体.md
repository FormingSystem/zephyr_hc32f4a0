---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-88
title: sent_frame_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsent__frame.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第88章\_sent\_frame\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsent__frame.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

单边沿半字节传输（SENT）的帧结构。

```c
#include <zephyr/drivers/sent/sent.h>
```

<a id="details"></a>

单边沿半字节传输（SENT）的帧结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 88.1\_数据成员（Data Fields）

<a id="r_aafd880b826c351481b384b5fef106068"></a>

```c
enum sent_frame_type type
```

相关声明：[sent_frame_type](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html#ga069232b79943be845df411539ef04993)、[type](#aafd880b826c351481b384b5fef106068)。

SENT 帧类型。

```c
union {
```

```c
struct {
```

<a id="r_a81db81552b432d03ce9975c2030c409a"></a>

```c
uint8_t id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[id](#a689cb24f6c8049e6282ca30939430c8f)。

串行消息（Serial message）ID。

<a id="r_a208d9e0005523aebd424a7b17d16e7e4"></a>

```c
uint16_t data
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[data](#a43d52380608b7683534dc31873a396af)。

串行消息数据。

<a id="r_ab5e1ddea7a4dec42a96177d5c1e718bb"></a>

```c
} serial
```

相关声明：[serial](#ab39f8ecf19e198ca4818fb13d522c6f4)。

串行消息。

```c
struct {
```

<a id="r_aebe35d533c5d6de5bbd33a153e3711ec"></a>

```c
uint8_t data_nibbles [8]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data_nibbles](#a4bef9a0871e8ecd86b6753e5bb46c6a0)。

快速消息（Fast message）数据的半字节（Nibble）数组。

<a id="r_aaca412303f4d02e27e25613f03503df4"></a>

```c
} fast
```

相关声明：[fast](#a1c02dabd2b0605b77683daf17fc7980b)。

快速消息。

<a id="r_aa3f6f64517db501bd3d83b817921b9d8"></a>

```c
};
```

帧载荷（Frame payload）。

<a id="r_aae185d5b024a3d9afc135ecc19c9410f"></a>

```c
uint32_t timestamp
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[timestamp](#aae185d5b024a3d9afc135ecc19c9410f)。

捕获该帧时的时间戳（Timestamp）。

<a id="r_a648203dab36ae27e874a171c71d92fe8"></a>

```c
uint8_t crc
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[crc](#a648203dab36ae27e874a171c71d92fe8)。

用于验证消息完整性的循环冗余校验（CRC）校验值。

## 88.2\_详细说明（Detailed Documentation）

<a id="aa3f6f64517db501bd3d83b817921b9d8"></a>

### `[union]`

```c
union { ... } sent_frame
```

帧载荷（Frame payload）。

有效成员取决于 `type`。

<a id="a648203dab36ae27e874a171c71d92fe8"></a>

### `crc`

```c
uint8_t sent_frame::crc
```

用于验证消息完整性的循环冗余校验（CRC）校验值。

<a id="a43d52380608b7683534dc31873a396af"></a>

### `data`

```c
uint16_t sent_frame::data
```

串行消息数据。

<a id="a4bef9a0871e8ecd86b6753e5bb46c6a0"></a>

### `data_nibbles`

```c
uint8_t sent_frame::data_nibbles[8]
```

快速消息（Fast message）数据的半字节（Nibble）数组。

<a id="a1c02dabd2b0605b77683daf17fc7980b"></a>

### `[struct]`

```c
struct { ... } sent_frame::fast
```

快速消息。

<a id="a689cb24f6c8049e6282ca30939430c8f"></a>

### `id`

```c
uint8_t sent_frame::id
```

串行消息（Serial message）ID。

<a id="ab39f8ecf19e198ca4818fb13d522c6f4"></a>

### `[struct]`

```c
struct { ... } sent_frame::serial
```

串行消息。

<a id="aae185d5b024a3d9afc135ecc19c9410f"></a>

### `timestamp`

```c
uint32_t sent_frame::timestamp
```

捕获该帧时的时间戳（Timestamp）。

<a id="aafd880b826c351481b384b5fef106068"></a>

### `type`

```c
enum sent_frame_type sent_frame::type
```

SENT 帧类型。

本数据类型文档由以下文件生成：

- `zephyr/drivers/sent/sent.h`

## 88.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sent/sent.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sent_2sent_8h_source.html)
- [sent_frame_type](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html#ga069232b79943be845df411539ef04993)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [sent_frame](P088_sent_frame_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P087_sent_driver_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P089_sent_rx_callback_config_结构体.md)
