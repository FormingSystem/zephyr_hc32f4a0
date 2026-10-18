---
id: learning.zephyr-docs.system-service-model-reference.page-14
title: ec_host_cmd_rx_ctx_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structec__host__cmd__rx__ctx.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_ec\_host\_cmd\_rx\_ctx\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structec__host__cmd__rx__ctx.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

主机命令后端与处理程序用于传递接收（RX）数据的上下文。

```c
#include <zephyr/mgmt/ec_host_cmd/backend.h>
```

<a id="details"></a>

主机命令后端与处理程序用于传递接收（RX）数据的上下文。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 14.1\_数据成员（Data Fields）

<a id="r_afcae3b7881f1c8634bb3ac1315111294"></a>

```c
uint8_t * buf
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[buf](#afcae3b7881f1c8634bb3ac1315111294)。

保存接收数据的缓冲区。

<a id="r_ae9f1c0c78d27dd5aa9bf47c56452a75a"></a>

```c
size_t len
```

相关声明：[len](#ae9f1c0c78d27dd5aa9bf47c56452a75a)。

后端写入 `buf` 的字节数。

<a id="r_a2db5dc5740436c8e0e232b959472ed0f"></a>

```c
size_t len_max
```

相关声明：[len_max](#a2db5dc5740436c8e0e232b959472ed0f)。

单个请求包可接收的最大字节数。

## 14.2\_详细说明（Detailed Documentation）

<a id="afcae3b7881f1c8634bb3ac1315111294"></a>

### `buf`

```c
uint8_t* ec_host_cmd_rx_ctx::buf
```

保存接收数据的缓冲区。

当 `CONFIG_EC_HOST_CMD_HANDLER_RX_BUFFER_SIZE > 0` 时，由处理器提供缓冲区。否则，后端应自行提供缓冲区，并在初始化函数中覆盖 `buf` 指针和 `len_max`。

<a id="ae9f1c0c78d27dd5aa9bf47c56452a75a"></a>

### `len`

```c
size_t ec_host_cmd_rx_ctx::len
```

后端写入 `buf` 的字节数。

<a id="a2db5dc5740436c8e0e232b959472ed0f"></a>

### `len_max`

```c
size_t ec_host_cmd_rx_ctx::len_max
```

单个请求包可接收的最大字节数。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/ec_host_cmd/backend.h`

## 14.3\_原页交叉引用（Cross References）

- [zephyr/mgmt/ec_host_cmd/backend.h](https://docs.zephyrproject.org/latest/doxygen/html/backend_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P013_ec_host_cmd_response_header_结构体.md) · [返回大纲](大纲.md) · [下一章](P015_ec_host_cmd_tx_buf_结构体.md)
