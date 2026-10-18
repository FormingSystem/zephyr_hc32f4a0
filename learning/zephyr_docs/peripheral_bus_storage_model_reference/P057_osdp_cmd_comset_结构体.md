---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-57
title: osdp_cmd_comset_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structosdp__cmd__comset.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第57章\_osdp\_cmd\_comset\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structosdp__cmd__comset.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

作为对COMSET命令的响应发送。

```c
#include <zephyr/mgmt/osdp.h>
```

<a id="details"></a>

作为对 `COMSET` 命令的响应发送。设置外设（Peripheral Device，PD）的通信参数，必须将这些参数保存到 PD 的非易失性存储器（Non-volatile memory）中。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 57.1\_数据成员（Data Fields）

<a id="r_af318dc8d5c8148902a2f824d72120ddc"></a>

```c
uint8_t address
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[address](#af318dc8d5c8148902a2f824d72120ddc)。

变更生效后，此 PD 将响应的单元 ID。

<a id="r_a9de97b54c83b9643f1dd3413ec3b15e6"></a>

```c
uint32_t baud_rate
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[baud_rate](#a9de97b54c83b9643f1dd3413ec3b15e6)。

波特率（Baud rate）。

## 57.2\_详细说明（Detailed Documentation）

<a id="af318dc8d5c8148902a2f824d72120ddc"></a>

### `address`

```c
uint8_t osdp_cmd_comset::address
```

变更生效后，此 PD 将响应的单元 ID。

<a id="a9de97b54c83b9643f1dd3413ec3b15e6"></a>

### `baud_rate`

```c
uint32_t osdp_cmd_comset::baud_rate
```

波特率（Baud rate）。

有效值：`9600`、`19200`、`38400`、`115200`、`230400`。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/osdp.h`

## 57.3\_原页交叉引用（Cross References）

- [zephyr/mgmt/osdp.h](https://docs.zephyrproject.org/latest/doxygen/html/osdp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P056_osdp_cmd_buzzer_结构体.md) · [返回大纲](大纲.md) · [下一章](P058_osdp_cmd_keyset_结构体.md)
