---
id: learning.zephyr-docs.modem-wireless-model-reference.page-59
title: modem_cmux_dlci_config_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmodem__cmux__dlci__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第59章\_modem\_cmux\_dlci\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmodem__cmux__dlci__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

CMUX数据链路连接标识符（DLCI）的配置。

```c
#include <zephyr/modem/cmux.h>
```

<a id="details"></a>

CMUX数据链路连接标识符（DLCI）的配置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 59.1\_数据成员（Data Fields）

<a id="r_ad0b1fe93bbee6343c8446da5a0ad88c9"></a>

```c
uint8_t dlci_address
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[dlci_address](#ad0b1fe93bbee6343c8446da5a0ad88c9)。

数据链路连接标识符（DLCI）通道地址。

<a id="r_ad3d6c1e0adce243aa536e52e5e4c4374"></a>

```c
uint8_t * receive_buf
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[receive_buf](#ad3d6c1e0adce243aa536e52e5e4c4374)。

管道使用的接收缓冲区。

<a id="r_af7715440c78d87466f91464000db1fef"></a>

```c
uint16_t receive_buf_size
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[receive_buf_size](#af7715440c78d87466f91464000db1fef)。

管道使用的接收缓冲区大小，单位为字节，范围从 127 开始。

## 59.2\_详细说明（Detailed Documentation）

<a id="ad0b1fe93bbee6343c8446da5a0ad88c9"></a>

### `dlci_address`

```c
uint8_t modem_cmux_dlci_config::dlci_address
```

数据链路连接标识符（DLCI）通道地址。

<a id="ad3d6c1e0adce243aa536e52e5e4c4374"></a>

### `receive_buf`

```c
uint8_t* modem_cmux_dlci_config::receive_buf
```

管道使用的接收缓冲区。

<a id="af7715440c78d87466f91464000db1fef"></a>

### `receive_buf_size`

```c
uint16_t modem_cmux_dlci_config::receive_buf_size
```

管道使用的接收缓冲区大小，单位为字节，范围从 127 开始。

本数据类型文档由以下文件生成：

- `zephyr/modem/cmux.h`

## 59.3\_原页交叉引用（Cross References）

- [zephyr/modem/cmux.h](https://docs.zephyrproject.org/latest/doxygen/html/cmux_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P058_modem_cmux_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P060_modem_pipe_data_fragment_结构体.md)
