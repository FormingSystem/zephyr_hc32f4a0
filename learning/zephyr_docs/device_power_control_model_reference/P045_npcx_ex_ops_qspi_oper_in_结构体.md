---
id: learning.zephyr-docs.device-power-control-model-reference.page-45
title: npcx_ex_ops_qspi_oper_in_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnpcx__ex__ops__qspi__oper__in.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第45章\_npcx\_ex\_ops\_qspi\_oper\_in\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnpcx__ex__ops__qspi__oper__in.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

FLASH_NPCX_EX_OP_SET_QSPI_OPER操作的输入参数。

```c
#include <zephyr/drivers/flash/npcx_flash_api_ex.h>
```

<a id="details"></a>

`FLASH_NPCX_EX_OP_SET_QSPI_OPER` 操作的输入参数，用于启用或禁用指定的 NPCX 四线 SPI（Quad-SPI）操作。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 45.1\_数据成员（Data Fields）

<a id="r_afc12bebd886ba71fc9431cedf0765c24"></a>

```c
bool enable
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[enable](#afc12bebd886ba71fc9431cedf0765c24)。

`true` 表示启用，`false` 表示禁用。

<a id="r_a0b9c9407bb320396d73f30ae4a8b55f1"></a>

```c
uint32_t mask
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[mask](#a0b9c9407bb320396d73f30ae4a8b55f1)。

要配置的操作掩码（Mask）。

## 45.2\_详细说明（Detailed Documentation）

<a id="afc12bebd886ba71fc9431cedf0765c24"></a>

### `enable`

```c
bool npcx_ex_ops_qspi_oper_in::enable
```

`true` 表示启用，`false` 表示禁用。

<a id="a0b9c9407bb320396d73f30ae4a8b55f1"></a>

### `mask`

```c
uint32_t npcx_ex_ops_qspi_oper_in::mask
```

要配置的操作掩码（Mask）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/flash/npcx_flash_api_ex.h`

## 45.3\_原页交叉引用（Cross References）

- [FLASH_NPCX_EX_OP_SET_QSPI_OPER](https://docs.zephyrproject.org/latest/doxygen/html/group__npcx__flash__ex__op.html#ggad4f93f7272e825355875d0fb05351474abbf87cdc7e9c3cdc9e6afde3c0485ec9)
- [zephyr/drivers/flash/npcx_flash_api_ex.h](https://docs.zephyrproject.org/latest/doxygen/html/npcx__flash__api__ex_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P044_npcx_ex_ops_gdma_in_结构体.md) · [返回大纲](大纲.md) · [下一章](P046_npcx_ex_ops_qspi_oper_out_结构体.md)
