---
id: learning.zephyr-docs.system-service-model-reference.page-15
title: ec_host_cmd_tx_buf_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structec__host__cmd__tx__buf.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_ec\_host\_cmd\_tx\_buf\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structec__host__cmd__tx__buf.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

主机命令后端与处理程序用于传递发送（TX）数据的上下文。

```c
#include <zephyr/mgmt/ec_host_cmd/backend.h>
```

<a id="details"></a>

主机命令后端与处理程序用于传递发送（TX）数据的上下文。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 15.1\_数据成员（Data Fields）

<a id="r_a6444723bccc196fb9792e95957bd98a5"></a>

```c
void * buf
```

相关声明：[buf](#a6444723bccc196fb9792e95957bd98a5)。

要写给主机的数据。

<a id="r_afaff8fbcb798a0445b029db1cedb6fd1"></a>

```c
size_t len
```

相关声明：[len](#afaff8fbcb798a0445b029db1cedb6fd1)。

要从 `buf` 写出的字节数。

<a id="r_a0f115f85bd271fa0defec1a2fc461d4c"></a>

```c
size_t len_max
```

相关声明：[len_max](#a0f115f85bd271fa0defec1a2fc461d4c)。

单个响应包可发送的最大字节数。

## 15.2\_详细说明（Detailed Documentation）

<a id="a6444723bccc196fb9792e95957bd98a5"></a>

### `buf`

```c
void* ec_host_cmd_tx_buf::buf
```

要写给主机的数据。

当 `CONFIG_EC_HOST_CMD_HANDLER_TX_BUFFER_SIZE > 0` 时，由处理器提供缓冲区。否则，后端应自行提供缓冲区，并在初始化函数中覆盖 `buf` 指针和 `len_max`。

<a id="afaff8fbcb798a0445b029db1cedb6fd1"></a>

### `len`

```c
size_t ec_host_cmd_tx_buf::len
```

要从 `buf` 写出的字节数。

<a id="a0f115f85bd271fa0defec1a2fc461d4c"></a>

### `len_max`

```c
size_t ec_host_cmd_tx_buf::len_max
```

单个响应包可发送的最大字节数。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/ec_host_cmd/backend.h`

## 15.3\_原页交叉引用（Cross References）

- [zephyr/mgmt/ec_host_cmd/backend.h](https://docs.zephyrproject.org/latest/doxygen/html/backend_8h_source.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P014_ec_host_cmd_rx_ctx_结构体.md) · [返回大纲](大纲.md) · [下一章](P016_elf32_ehdr_结构体.md)
