---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-25
title: lin_msg_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structlin__msg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第25章\_lin\_msg\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structlin__msg.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

局部互连网络（LIN）的消息结构。

```c
#include <zephyr/drivers/lin.h>
```

<a id="details"></a>

局部互连网络（LIN）的消息结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 25.1\_数据成员（Data Fields）

<a id="r_a0bbd5b4c8d50c298372d6227674843df"></a>

```c
uint8_t id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[id](#a0bbd5b4c8d50c298372d6227674843df)。

LIN 消息 ID。

<a id="r_a785c43cefa7fd940bf45f7729a51fb95"></a>

```c
uint8_t flags
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[flags](#a785c43cefa7fd940bf45f7729a51fb95)。

消息的标志。

<a id="r_a8f9f0346d4f9f9a128150fbee2d2e3e6"></a>

```c
uint8_t data_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data_len](#a8f9f0346d4f9f9a128150fbee2d2e3e6)。

消息的数据长度。

```c
union {
```

<a id="r_a254bda40601ce0f49907ed65f2fdc8c2"></a>

```c
uint8_t data [LIN_MAX_DLEN]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#ae0a650e8bbd278259f59bec5337ff955)。

按字节访问的载荷数据。

<a id="r_af19b33bc85a65f175eb0b1fdbad364f0"></a>

```c
uint32_t data_32 [DIV_ROUND_UP(LIN_MAX_DLEN, sizeof(uint32_t))]
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[data_32](#aecea8811d33cfeb2c2d50a2d0cf92cbd)、[DIV_ROUND_UP](../util_reference/P001_通用工具公共接口.md#gae664e7492e37d324831caf2321ddda37)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

按 32 位字访问的载荷数据。

<a id="r_af19a9ad750ee1dd9f525127813229d0a"></a>

```c
};
```

消息载荷数据。

<a id="r_a3f139b75c8cd61fe2085b7eac4eb828b"></a>

```c
enum lin_checksum_type checksum_type
```

相关声明：[lin_checksum_type](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gaf97478fd971b8b6913386a225078a24f)、[checksum_type](#a3f139b75c8cd61fe2085b7eac4eb828b)。

消息的校验和类型。

## 25.2\_详细说明（Detailed Documentation）

<a id="af19a9ad750ee1dd9f525127813229d0a"></a>

### `[union]`

```c
union { ... } lin_msg
```

消息载荷数据。

<a id="a3f139b75c8cd61fe2085b7eac4eb828b"></a>

### `checksum_type`

```c
enum lin_checksum_type lin_msg::checksum_type
```

消息的校验和类型。

<a id="ae0a650e8bbd278259f59bec5337ff955"></a>

### `data`

```c
uint8_t lin_msg::data[LIN_MAX_DLEN]
```

按字节访问的载荷数据。

<a id="aecea8811d33cfeb2c2d50a2d0cf92cbd"></a>

### `data_32`

```c
uint32_t lin_msg::data_32[DIV_ROUND_UP(LIN_MAX_DLEN, sizeof(uint32_t))]
```

按 32 位字访问的载荷数据。

<a id="a8f9f0346d4f9f9a128150fbee2d2e3e6"></a>

### `data_len`

```c
uint8_t lin_msg::data_len
```

消息的数据长度。

<a id="a785c43cefa7fd940bf45f7729a51fb95"></a>

### `flags`

```c
uint8_t lin_msg::flags
```

消息的标志。

<a id="a0bbd5b4c8d50c298372d6227674843df"></a>

### `id`

```c
uint8_t lin_msg::id
```

LIN 消息 ID。

本数据类型文档由以下文件生成：

- `zephyr/drivers/lin.h`

## 25.3\_原页交叉引用（Cross References）

- [zephyr/drivers/lin.h](https://docs.zephyrproject.org/latest/doxygen/html/lin_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [DIV_ROUND_UP](../util_reference/P001_通用工具公共接口.md#gae664e7492e37d324831caf2321ddda37)
- [lin_checksum_type](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gaf97478fd971b8b6913386a225078a24f)
- [lin_msg](P025_lin_msg_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P024_lin_filter_结构体.md) · [返回大纲](大纲.md) · [下一章](P026_mctp_binding_i2c_gpio_controller_结构体.md)
