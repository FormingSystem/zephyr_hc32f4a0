---
id: learning.zephyr-docs.system-service-model-reference.page-11
title: ec_host_cmd_handler_args_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structec__host__cmd__handler__args.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_ec\_host\_cmd\_handler\_args\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structec__host__cmd__handler__args.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

传递给每个已安装主机命令处理程序（Host Command Handler）的参数。

```c
#include <zephyr/mgmt/ec_host_cmd/ec_host_cmd.h>
```

<a id="details"></a>

传递给每个已安装主机命令处理程序（Host Command Handler）的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 11.1\_数据成员（Data Fields）

<a id="r_a8c7fcd1d310b0622f45458388462c9ef"></a>

```c
void * reserved
```

相关声明：[reserved](#a8c7fcd1d310b0622f45458388462c9ef)。

为兼容性保留。

<a id="r_a059b20824ece1ada2d53c7e73f49972d"></a>

```c
uint16_t command
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[command](#a059b20824ece1ada2d53c7e73f49972d)。

命令标识符（Command identifier）。

<a id="r_ad346a4c196ee5e48c67640232a828745"></a>

```c
uint8_t version
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[version](#ad346a4c196ee5e48c67640232a828745)。

请求的主机命令版本。

<a id="r_a364bda288790f65205f26310148d2888"></a>

```c
const void * input_buf
```

相关声明：[input_buf](#a364bda288790f65205f26310148d2888)。

接收的数据，可强制转换为此处理器的请求类型。

<a id="r_a7d6d622f7dd9e3b8faf928befa72f36a"></a>

```c
uint16_t input_buf_size
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[input_buf_size](#a7d6d622f7dd9e3b8faf928befa72f36a)。

可从 `input_buf` 读取的有效字节数。

<a id="r_a1ac9d891b168b4db55a1829d72362ca5"></a>

```c
void * output_buf
```

相关声明：[output_buf](#a1ac9d891b168b4db55a1829d72362ca5)。

写入此缓冲区的数据将发送给主机。

<a id="r_ab3eaef25fd80d0ac38b8d2eb9e40ebd4"></a>

```c
uint16_t output_buf_max
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[output_buf_max](#ab3eaef25fd80d0ac38b8d2eb9e40ebd4)。

可写入 `output_buf` 的最大字节数。

<a id="r_a1a6f9a7ba7faf810f7095b4c053dd3b2"></a>

```c
uint16_t output_buf_size
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[output_buf_size](#a1a6f9a7ba7faf810f7095b4c053dd3b2)。

要从 `output_buf` 发送给主机的字节数。

## 11.2\_详细说明（Detailed Documentation）

<a id="a059b20824ece1ada2d53c7e73f49972d"></a>

### `command`

```c
uint16_t ec_host_cmd_handler_args::command
```

命令标识符（Command identifier）。

<a id="a364bda288790f65205f26310148d2888"></a>

### `input_buf`

```c
const void* ec_host_cmd_handler_args::input_buf
```

接收的数据，可强制转换为此处理器的请求类型。

<a id="a7d6d622f7dd9e3b8faf928befa72f36a"></a>

### `input_buf_size`

```c
uint16_t ec_host_cmd_handler_args::input_buf_size
```

可从 `input_buf` 读取的有效字节数。

<a id="a1ac9d891b168b4db55a1829d72362ca5"></a>

### `output_buf`

```c
void* ec_host_cmd_handler_args::output_buf
```

写入此缓冲区的数据将发送给主机。

<a id="ab3eaef25fd80d0ac38b8d2eb9e40ebd4"></a>

### `output_buf_max`

```c
uint16_t ec_host_cmd_handler_args::output_buf_max
```

可写入 `output_buf` 的最大字节数。

<a id="a1a6f9a7ba7faf810f7095b4c053dd3b2"></a>

### `output_buf_size`

```c
uint16_t ec_host_cmd_handler_args::output_buf_size
```

要从 `output_buf` 发送给主机的字节数。

<a id="a8c7fcd1d310b0622f45458388462c9ef"></a>

### `reserved`

```c
void* ec_host_cmd_handler_args::reserved
```

为兼容性保留。

<a id="ad346a4c196ee5e48c67640232a828745"></a>

### `version`

```c
uint8_t ec_host_cmd_handler_args::version
```

请求的主机命令版本。

此值是在静态注册时为该处理器登记的有效值之一。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/ec_host_cmd/ec_host_cmd.h`

## 11.3\_原页交叉引用（Cross References）

- [zephyr/mgmt/ec_host_cmd/ec_host_cmd.h](https://docs.zephyrproject.org/latest/doxygen/html/ec__host__cmd_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P010_ec_host_cmd_handler_结构体.md) · [返回大纲](大纲.md) · [下一章](P012_ec_host_cmd_request_header_结构体.md)
