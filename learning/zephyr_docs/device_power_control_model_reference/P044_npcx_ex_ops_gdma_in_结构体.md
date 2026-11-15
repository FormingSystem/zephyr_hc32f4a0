---
id: learning.zephyr-docs.device-power-control-model-reference.page-44
title: npcx_ex_ops_gdma_in_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnpcx__ex__ops__gdma__in.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第44章\_npcx\_ex\_ops\_gdma\_in\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnpcx__ex__ops__gdma__in.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

FLASH_NPCX_EX_OP_EXEC_GDMA操作的输入参数。

```c
#include <zephyr/drivers/flash/npcx_flash_api_ex.h>
```

<a id="details"></a>

`FLASH_NPCX_EX_OP_EXEC_GDMA` 操作的输入参数，定义通用 DMA（GDMA）内存传输的源地址、目的地址和大小。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 44.1\_数据成员（Data Fields）

<a id="r_a14eaa0c83b6f1234218e6d350405dbf3"></a>

```c
uint32_t src
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[src](#a14eaa0c83b6f1234218e6d350405dbf3)。

传输源地址。

<a id="r_a806cb6bab93a437093914cbffac07c62"></a>

```c
uint32_t dst
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[dst](#a806cb6bab93a437093914cbffac07c62)。

传输目的地址。

<a id="r_a2c7b04d7918257a0e4523822d4ccf07e"></a>

```c
uint16_t length
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[length](#a2c7b04d7918257a0e4523822d4ccf07e)。

要传输的字节数。

## 44.2\_详细说明（Detailed Documentation）

<a id="a806cb6bab93a437093914cbffac07c62"></a>

### `dst`

```c
uint32_t npcx_ex_ops_gdma_in::dst
```

传输目的地址。

<a id="a2c7b04d7918257a0e4523822d4ccf07e"></a>

### `length`

```c
uint16_t npcx_ex_ops_gdma_in::length
```

要传输的字节数。

<a id="a14eaa0c83b6f1234218e6d350405dbf3"></a>

### `src`

```c
uint32_t npcx_ex_ops_gdma_in::src
```

传输源地址。

本数据类型文档由以下文件生成：

- `zephyr/drivers/flash/npcx_flash_api_ex.h`

## 44.3\_原页交叉引用（Cross References）

- [FLASH_NPCX_EX_OP_EXEC_GDMA](https://docs.zephyrproject.org/latest/doxygen/html/group__npcx__flash__ex__op.html#ggad4f93f7272e825355875d0fb05351474ad675f28e2066d7d97be0ecdc7f3d34b9)
- [zephyr/drivers/flash/npcx_flash_api_ex.h](https://docs.zephyrproject.org/latest/doxygen/html/npcx__flash__api__ex_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P043_mspm0_sys_clock_结构体.md) · [返回大纲](大纲.md) · [下一章](P045_npcx_ex_ops_qspi_oper_in_结构体.md)
