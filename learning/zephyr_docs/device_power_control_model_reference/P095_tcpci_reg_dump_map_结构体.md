---
id: learning.zephyr-docs.device-power-control-model-reference.page-95
title: tcpci_reg_dump_map_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structtcpci__reg__dump__map.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第95章\_tcpci\_reg\_dump\_map\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structtcpci__reg__dump__map.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

在寄存器转储（Register Dump）中将寄存器地址绑定到名称的结构。

```c
#include <zephyr/drivers/usb_c/tcpci_priv.h>
```

<a id="details"></a>

在寄存器转储（Register Dump）中将寄存器地址绑定到名称的结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 95.1\_数据成员（Data Fields）

<a id="r_ad68dd201d76bfb2193567b8db2ec514a"></a>

```c
uint8_t addr
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[addr](#ad68dd201d76bfb2193567b8db2ec514a)。

I2C 设备寄存器的地址。

<a id="r_a316d7f2a6b4b5fd42eb6450a810b7dd8"></a>

```c
const char * name
```

相关声明：[name](#a316d7f2a6b4b5fd42eb6450a810b7dd8)。

便于阅读的寄存器名称。

<a id="r_a6e84093c1d027233230d8f27b0698756"></a>

```c
uint8_t size
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[size](#a6e84093c1d027233230d8f27b0698756)。

寄存器大小，单位为字节。

## 95.2\_详细说明（Detailed Documentation）

<a id="ad68dd201d76bfb2193567b8db2ec514a"></a>

### `addr`

```c
uint8_t tcpci_reg_dump_map::addr
```

I2C 设备寄存器的地址。

<a id="a316d7f2a6b4b5fd42eb6450a810b7dd8"></a>

### `name`

```c
const char* tcpci_reg_dump_map::name
```

便于阅读的寄存器名称。

<a id="a6e84093c1d027233230d8f27b0698756"></a>

### `size`

```c
uint8_t tcpci_reg_dump_map::size
```

寄存器大小，单位为字节。

本数据类型文档由以下文件生成：

- `zephyr/drivers/usb_c/tcpci_priv.h`

## 95.3\_原页交叉引用（Cross References）

- [zephyr/drivers/usb_c/tcpci_priv.h](https://docs.zephyrproject.org/latest/doxygen/html/tcpci__priv_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P094_tcpc_driver_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P096_tmc6460_field_结构体.md)
