---
id: learning.zephyr-docs.platform-security-model-reference.page-57
title: sip_svc_response_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsip__svc__response.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第57章\_sip\_svc\_response\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsip__svc__response.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

SiP服务（SiP Services）通信协议的响应格式。

```c
#include <zephyr/drivers/sip_svc/sip_svc_proto.h>
```

<a id="details"></a>

SiP 服务通信协议的响应格式（Response format）。

响应头（Response header）：位 `[15:0]` 为错误码；位 `[23:16]` 为事务 ID；位 `[29:24]` 未使用，保留；位 `[31:30]` 为 Arm SiP 服务通信协议版本。

`a0 - a3`：SMC/HVC 的返回值。

`resp_data_addr`：仅用于异步命令。该动态分配的内存地址用于存放异步响应数据，由客户端在请求期间提供。客户端收到异步命令事务的回调后，负责释放这块内存。内存必须动态分配；如果通道处于 `ABORT` 状态，框架将释放已分配的内存。

`resp_data_size`：仅用于异步命令。`resp_data_addr` 中有效数据的大小，单位为字节。

`priv_data`：在请求期间提供的客户端上下文内存地址。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 57.1\_数据成员（Data Fields）

<a id="r_ab2a3ed6ec283ef83a2ad8ea8eea421be"></a>

```c
uint32_t header
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[header](#ab2a3ed6ec283ef83a2ad8ea8eea421be)。

<a id="r_a4f413e152dc2ef463140499164c3e410"></a>

```c
unsigned long a0
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[a0](#a4f413e152dc2ef463140499164c3e410)。

<a id="r_abfb0f411524209388f79f35a82031e79"></a>

```c
unsigned long a1
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[a1](#abfb0f411524209388f79f35a82031e79)。

<a id="r_af973d08da13a7dcecf344f3f9d6f118e"></a>

```c
unsigned long a2
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[a2](#af973d08da13a7dcecf344f3f9d6f118e)。

<a id="r_aac8bb11e4661e59cbce0d6b5d50a0820"></a>

```c
unsigned long a3
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[a3](#aac8bb11e4661e59cbce0d6b5d50a0820)。

<a id="r_a5b8a49d292e45ecdd81920c30b650c10"></a>

```c
uint64_t resp_data_addr
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[resp_data_addr](#a5b8a49d292e45ecdd81920c30b650c10)。

<a id="r_a2e8373be61b16ac4f4d013103539cceb"></a>

```c
uint32_t resp_data_size
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[resp_data_size](#a2e8373be61b16ac4f4d013103539cceb)。

<a id="r_a992b3f936866852633569f9c8d37d6a0"></a>

```c
void * priv_data
```

相关声明：[priv_data](#a992b3f936866852633569f9c8d37d6a0)。

## 57.2\_详细说明（Detailed Documentation）

<a id="a4f413e152dc2ef463140499164c3e410"></a>

### `a0`

```c
unsigned long sip_svc_response::a0
```

<a id="abfb0f411524209388f79f35a82031e79"></a>

### `a1`

```c
unsigned long sip_svc_response::a1
```

<a id="af973d08da13a7dcecf344f3f9d6f118e"></a>

### `a2`

```c
unsigned long sip_svc_response::a2
```

<a id="aac8bb11e4661e59cbce0d6b5d50a0820"></a>

### `a3`

```c
unsigned long sip_svc_response::a3
```

<a id="ab2a3ed6ec283ef83a2ad8ea8eea421be"></a>

### `header`

```c
uint32_t sip_svc_response::header
```

<a id="a992b3f936866852633569f9c8d37d6a0"></a>

### `priv_data`

```c
void* sip_svc_response::priv_data
```

<a id="a5b8a49d292e45ecdd81920c30b650c10"></a>

### `resp_data_addr`

```c
uint64_t sip_svc_response::resp_data_addr
```

<a id="a2e8373be61b16ac4f4d013103539cceb"></a>

### `resp_data_size`

```c
uint32_t sip_svc_response::resp_data_size
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/sip_svc/sip_svc_proto.h`

## 57.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sip_svc/sip_svc_proto.h](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__proto_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P056_sip_svc_request_结构体.md) · [返回大纲](大纲.md) · [下一章](P058_tee_driver_api_结构体.md)
