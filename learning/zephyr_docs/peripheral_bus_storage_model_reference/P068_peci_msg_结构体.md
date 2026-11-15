---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-68
title: peci_msg_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structpeci__msg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第68章\_peci\_msg\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structpeci__msg.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

平台环境控制接口（PECI）的事务数据包格式。

```c
#include <zephyr/drivers/peci.h>
```

<a id="details"></a>

平台环境控制接口（PECI）的事务数据包格式。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 68.1\_数据成员（Data Fields）

<a id="r_aa4d6785fc79059dc7e8574010bc29e4c"></a>

```c
uint8_t addr
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[addr](#aa4d6785fc79059dc7e8574010bc29e4c)。

客户端地址（Client Address）。

<a id="r_a10b270f4669c85a85c6e8f1bef7671e8"></a>

```c
enum peci_command_code cmd_code
```

相关声明：[peci_command_code](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gacd243f64973f7bdcc8c999dc14ed2bd6)、[cmd_code](#a10b270f4669c85a85c6e8f1bef7671e8)。

命令码（Command code）。

<a id="r_a22e435e110d261b8ecd5180d118ffd2d"></a>

```c
struct peci_buf tx_buffer
```

相关声明：[peci_buf](P066_peci_buf_结构体.md)、[tx_buffer](#a22e435e110d261b8ecd5180d118ffd2d)。

指向待写入数据缓冲区的指针。

<a id="r_abea62e39ca0ac59fca47c2f08a72f1e8"></a>

```c
struct peci_buf rx_buffer
```

相关声明：[peci_buf](P066_peci_buf_结构体.md)、[rx_buffer](#abea62e39ca0ac59fca47c2f08a72f1e8)。

指向读取数据缓冲区的指针。

<a id="r_a2990d5a2ae318020ed9301dd2de37070"></a>

```c
uint8_t oob_addr
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[oob_addr](#a2990d5a2ae318020ed9301dd2de37070)。

eSPI 带外（OOB）客户端地址。

<a id="r_a0449f151c62e672553d7d60480e1b995"></a>

```c
uint8_t flags
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[flags](#a0449f151c62e672553d7d60480e1b995)。

PECI 消息标志。

## 68.2\_详细说明（Detailed Documentation）

<a id="aa4d6785fc79059dc7e8574010bc29e4c"></a>

### `addr`

```c
uint8_t peci_msg::addr
```

客户端地址（Client Address）。

<a id="a10b270f4669c85a85c6e8f1bef7671e8"></a>

### `cmd_code`

```c
enum peci_command_code peci_msg::cmd_code
```

命令码（Command code）。

<a id="a0449f151c62e672553d7d60480e1b995"></a>

### `flags`

```c
uint8_t peci_msg::flags
```

PECI 消息标志。

<a id="a2990d5a2ae318020ed9301dd2de37070"></a>

### `oob_addr`

```c
uint8_t peci_msg::oob_addr
```

eSPI 带外（OOB）客户端地址。

<a id="abea62e39ca0ac59fca47c2f08a72f1e8"></a>

### `rx_buffer`

```c
struct peci_buf peci_msg::rx_buffer
```

指向读取数据缓冲区的指针。

<a id="a22e435e110d261b8ecd5180d118ffd2d"></a>

### `tx_buffer`

```c
struct peci_buf peci_msg::tx_buffer
```

指向待写入数据缓冲区的指针。

本数据类型文档由以下文件生成：

- `zephyr/drivers/peci.h`

## 68.3\_原页交叉引用（Cross References）

- [zephyr/drivers/peci.h](https://docs.zephyrproject.org/latest/doxygen/html/peci_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [peci_command_code](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gacd243f64973f7bdcc8c999dc14ed2bd6)
- [peci_buf](P066_peci_buf_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P067_peci_driver_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P069_ps2_driver_api_结构体.md)
