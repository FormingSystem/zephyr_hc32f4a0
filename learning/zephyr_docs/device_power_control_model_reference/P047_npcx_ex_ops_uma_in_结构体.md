---
id: learning.zephyr-docs.device-power-control-model-reference.page-47
title: npcx_ex_ops_uma_in_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnpcx__ex__ops__uma__in.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第47章\_npcx\_ex\_ops\_uma\_in\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnpcx__ex__ops__uma__in.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

FLASH_NPCX_EX_OP_EXEC_UMA操作的输入参数。

```c
#include <zephyr/drivers/flash/npcx_flash_api_ex.h>
```

<a id="details"></a>

`FLASH_NPCX_EX_OP_EXEC_UMA` 操作的输入参数，定义 UMA 事务（Transaction）的内容。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 47.1\_数据成员（Data Fields）

<a id="r_a891172574f487bcfbcbbed20cd340998"></a>

```c
uint8_t opcode
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[opcode](#a891172574f487bcfbcbbed20cd340998)。

SPI 操作码，即命令字节。

<a id="r_a67c765977abd17095e4589604dfe43b0"></a>

```c
uint8_t * tx_buf
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[tx_buf](#a67c765977abd17095e4589604dfe43b0)。

指向发送缓冲区的指针，可以为 `NULL`。

<a id="r_add76f25d7adf905d4d4ba3b6f4b977e6"></a>

```c
size_t tx_count
```

相关声明：[tx_count](#add76f25d7adf905d4d4ba3b6f4b977e6)。

要发送的字节数。

<a id="r_a4fe44cf0e3b09193700a72b62b78f544"></a>

```c
uint32_t addr
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[addr](#a4fe44cf0e3b09193700a72b62b78f544)。

地址阶段（Address phase）使用的地址。

<a id="r_a3c950c4208da78e2908a116ea3eedd5f"></a>

```c
size_t addr_count
```

相关声明：[addr_count](#a3c950c4208da78e2908a116ea3eedd5f)。

地址字节数，范围为 0–4。

<a id="r_a7c36c34ffe3f6c69e9229efdc41da87c"></a>

```c
size_t rx_count
```

相关声明：[rx_count](#a7c36c34ffe3f6c69e9229efdc41da87c)。

预期读取的字节数。

## 47.2\_详细说明（Detailed Documentation）

<a id="a4fe44cf0e3b09193700a72b62b78f544"></a>

### `addr`

```c
uint32_t npcx_ex_ops_uma_in::addr
```

地址阶段（Address phase）使用的地址。

<a id="a3c950c4208da78e2908a116ea3eedd5f"></a>

### `addr_count`

```c
size_t npcx_ex_ops_uma_in::addr_count
```

地址字节数，范围为 0–4。

<a id="a891172574f487bcfbcbbed20cd340998"></a>

### `opcode`

```c
uint8_t npcx_ex_ops_uma_in::opcode
```

SPI 操作码，即命令字节。

<a id="a7c36c34ffe3f6c69e9229efdc41da87c"></a>

### `rx_count`

```c
size_t npcx_ex_ops_uma_in::rx_count
```

预期读取的字节数。

<a id="a67c765977abd17095e4589604dfe43b0"></a>

### `tx_buf`

```c
uint8_t* npcx_ex_ops_uma_in::tx_buf
```

指向发送缓冲区的指针，可以为 `NULL`。

<a id="add76f25d7adf905d4d4ba3b6f4b977e6"></a>

### `tx_count`

```c
size_t npcx_ex_ops_uma_in::tx_count
```

要发送的字节数。

本数据类型文档由以下文件生成：

- `zephyr/drivers/flash/npcx_flash_api_ex.h`

## 47.3\_原页交叉引用（Cross References）

- [FLASH_NPCX_EX_OP_EXEC_UMA](https://docs.zephyrproject.org/latest/doxygen/html/group__npcx__flash__ex__op.html#ggad4f93f7272e825355875d0fb05351474ad1fde767b235165d178a13de61d5f007)
- [zephyr/drivers/flash/npcx_flash_api_ex.h](https://docs.zephyrproject.org/latest/doxygen/html/npcx__flash__api__ex_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P046_npcx_ex_ops_qspi_oper_out_结构体.md) · [返回大纲](大纲.md) · [下一章](P048_npcx_ex_ops_uma_out_结构体.md)
