---
id: learning.zephyr-docs.device-power-control-model-reference.page-46
title: npcx_ex_ops_qspi_oper_out_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnpcx__ex__ops__qspi__oper__out.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第46章\_npcx\_ex\_ops\_qspi\_oper\_out\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnpcx__ex__ops__qspi__oper__out.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

FLASH_NPCX_EX_OP_GET_QSPI_OPER操作的输出参数。

```c
#include <zephyr/drivers/flash/npcx_flash_api_ex.h>
```

<a id="details"></a>

`FLASH_NPCX_EX_OP_GET_QSPI_OPER` 操作的输出参数，用于报告当前 QSPI 操作状态。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 46.1\_数据成员（Data Fields）

<a id="r_aa77f1bdcc00e1f3cc7a66cc150ab5686"></a>

```c
uint32_t oper
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[oper](#aa77f1bdcc00e1f3cc7a66cc150ab5686)。

当前已激活操作的位域（Bitfield）。

## 46.2\_详细说明（Detailed Documentation）

<a id="aa77f1bdcc00e1f3cc7a66cc150ab5686"></a>

### `oper`

```c
uint32_t npcx_ex_ops_qspi_oper_out::oper
```

当前已激活操作的位域（Bitfield）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/flash/npcx_flash_api_ex.h`

## 46.3\_原页交叉引用（Cross References）

- [FLASH_NPCX_EX_OP_GET_QSPI_OPER](https://docs.zephyrproject.org/latest/doxygen/html/group__npcx__flash__ex__op.html#ggad4f93f7272e825355875d0fb05351474a46c5fff8b0ffbc480c01fed93ff8fd57)
- [zephyr/drivers/flash/npcx_flash_api_ex.h](https://docs.zephyrproject.org/latest/doxygen/html/npcx__flash__api__ex_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P045_npcx_ex_ops_qspi_oper_in_结构体.md) · [返回大纲](大纲.md) · [下一章](P047_npcx_ex_ops_uma_in_结构体.md)
