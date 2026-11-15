---
id: learning.zephyr-docs.system-service-model-reference.page-10
title: ec_host_cmd_handler_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structec__host__cmd__handler.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_ec\_host\_cmd\_handler\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structec__host__cmd__handler.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于静态注册主机命令处理程序（Host Command Handler）的结构。

```c
#include <zephyr/mgmt/ec_host_cmd/ec_host_cmd.h>
```

<a id="details"></a>

用于静态注册主机命令处理程序（Host Command Handler）的结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 10.1\_数据成员（Data Fields）

<a id="r_aa87d559e625871f78023fcc015a02c82"></a>

```c
ec_host_cmd_handler_cb handler
```

相关声明：[ec_host_cmd_handler_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ga027ae23ea11a0ec7711725d1b28125d7)、[handler](#aa87d559e625871f78023fcc015a02c82)。

处理与 `id` 匹配的命令的回调例程。

<a id="r_ad0aea63728aa9254e2a14d8cf0352b87"></a>

```c
uint16_t id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[id](#ad0aea63728aa9254e2a14d8cf0352b87)。

数值形式的命令 ID，用于查找命令。

<a id="r_a2e4643dc7ca0ee4b8f7169b9156dadc6"></a>

```c
uint16_t version_mask
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[version_mask](#a2e4643dc7ca0ee4b8f7169b9156dadc6)。

处理器支持的所有版本组成的位域；每个位表示处理器是否支持对应版本。

<a id="r_aef233f030a30032e9dcde620c1953394"></a>

```c
uint16_t min_rqt_size
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[min_rqt_size](#aef233f030a30032e9dcde620c1953394)。

框架在将请求交给处理器之前强制要求的最小 `input_buf_size`。

<a id="r_a4777b0c23ddf568c36ca995886cf3248"></a>

```c
uint16_t min_rsp_size
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[min_rsp_size](#a4777b0c23ddf568c36ca995886cf3248)。

框架在将请求交给处理器之前强制要求的最小 `output_buf_size`。

## 10.2\_详细说明（Detailed Documentation）

<a id="aa87d559e625871f78023fcc015a02c82"></a>

### `handler`

```c
ec_host_cmd_handler_cb ec_host_cmd_handler::handler
```

处理与 `id` 匹配的命令的回调例程。

<a id="ad0aea63728aa9254e2a14d8cf0352b87"></a>

### `id`

```c
uint16_t ec_host_cmd_handler::id
```

数值形式的命令 ID，用于查找命令。

<a id="aef233f030a30032e9dcde620c1953394"></a>

### `min_rqt_size`

```c
uint16_t ec_host_cmd_handler::min_rqt_size
```

框架在将请求交给处理器之前强制要求的最小 `input_buf_size`。

<a id="a4777b0c23ddf568c36ca995886cf3248"></a>

### `min_rsp_size`

```c
uint16_t ec_host_cmd_handler::min_rsp_size
```

框架在将请求交给处理器之前强制要求的最小 `output_buf_size`。

<a id="a2e4643dc7ca0ee4b8f7169b9156dadc6"></a>

### `version_mask`

```c
uint16_t ec_host_cmd_handler::version_mask
```

处理器支持的所有版本组成的位域；每个位表示处理器是否支持对应版本。

例如，`BIT(0)` 对应版本 0。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/ec_host_cmd/ec_host_cmd.h`

## 10.3\_原页交叉引用（Cross References）

- [zephyr/mgmt/ec_host_cmd/ec_host_cmd.h](https://docs.zephyrproject.org/latest/doxygen/html/ec__host__cmd_8h_source.html)
- [ec_host_cmd_handler_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ga027ae23ea11a0ec7711725d1b28125d7)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [BIT(0)](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P009_ec_host_cmd_backend_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P011_ec_host_cmd_handler_args_结构体.md)
