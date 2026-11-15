---
id: learning.zephyr-docs.device-power-control-model-reference.page-48
title: npcx_ex_ops_uma_out_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnpcx__ex__ops__uma__out.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第48章\_npcx\_ex\_ops\_uma\_out\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnpcx__ex__ops__uma__out.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

FLASH_NPCX_EX_OP_EXEC_UMA操作的输出参数。

```c
#include <zephyr/drivers/flash/npcx_flash_api_ex.h>
```

<a id="details"></a>

`FLASH_NPCX_EX_OP_EXEC_UMA` 操作的输出参数，定义接收数据的存储位置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 48.1\_数据成员（Data Fields）

<a id="r_a9be2364b1328eedc07e0123d774dbba7"></a>

```c
uint8_t * rx_buf
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rx_buf](#a9be2364b1328eedc07e0123d774dbba7)。

指向接收缓冲区的指针，缓冲区必须足够大。

## 48.2\_详细说明（Detailed Documentation）

<a id="a9be2364b1328eedc07e0123d774dbba7"></a>

### `rx_buf`

```c
uint8_t* npcx_ex_ops_uma_out::rx_buf
```

指向接收缓冲区的指针，缓冲区必须足够大。

本数据类型文档由以下文件生成：

- `zephyr/drivers/flash/npcx_flash_api_ex.h`

## 48.3\_原页交叉引用（Cross References）

- [FLASH_NPCX_EX_OP_EXEC_UMA](https://docs.zephyrproject.org/latest/doxygen/html/group__npcx__flash__ex__op.html#ggad4f93f7272e825355875d0fb05351474ad1fde767b235165d178a13de61d5f007)
- [zephyr/drivers/flash/npcx_flash_api_ex.h](https://docs.zephyrproject.org/latest/doxygen/html/npcx__flash__api__ex_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P047_npcx_ex_ops_uma_in_结构体.md) · [返回大纲](大纲.md) · [下一章](P049_numaker_scc_subsys_结构体.md)
