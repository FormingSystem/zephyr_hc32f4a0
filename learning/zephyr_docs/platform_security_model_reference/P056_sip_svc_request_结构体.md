---
id: learning.zephyr-docs.platform-security-model-reference.page-56
title: sip_svc_request_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsip__svc__request.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第56章\_sip\_svc\_request\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsip__svc__request.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

SiP服务（SiP Service）通信协议的请求格式。

```c
#include <zephyr/drivers/sip_svc/sip_svc_proto.h>
```

<a id="details"></a>

SiP 服务通信协议的请求格式（Request format）。

请求头（Request header）：位 `[15:0]` 为 Arm SiP 服务命令码；位 `[23:16]` 为事务 ID，由 `sip_svc` 服务填写；位 `[29:24]` 未使用，保留；位 `[31:30]` 为 Arm SiP 服务通信协议版本。

`a0 - a7`：用户输入数据，在触发安全监控调用/超级调用（SMC/HVC）时填入 `a0-a7` 寄存器。

`resp_data_addr`：仅用于异步命令。该动态分配的内存地址供服务写入异步响应数据。如果客户端取消事务，服务将释放这块内存。

`resp_data_size`：仅用于异步命令。`resp_data_addr` 所指内存的最大大小，单位为字节。

`priv_data`：客户端上下文的内存地址。服务通过回调，以响应格式将此地址返回给客户端。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 56.1\_数据成员（Data Fields）

<a id="r_aa8c71f7af00dd3195d49c04df5cb3509"></a>

```c
uint32_t header
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[header](#aa8c71f7af00dd3195d49c04df5cb3509)。

<a id="r_a95e4d0bb03bfca90ea78fc19c581ef7f"></a>

```c
unsigned long a0
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[a0](#a95e4d0bb03bfca90ea78fc19c581ef7f)。

<a id="r_a3b41176de28f042510d5ca5fc9c4678e"></a>

```c
unsigned long a1
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[a1](#a3b41176de28f042510d5ca5fc9c4678e)。

<a id="r_aa20d78ab299064e8d4b304f4165bfdf2"></a>

```c
unsigned long a2
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[a2](#aa20d78ab299064e8d4b304f4165bfdf2)。

<a id="r_a6cd5c3cf895daad0c600544a903f2eb8"></a>

```c
unsigned long a3
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[a3](#a6cd5c3cf895daad0c600544a903f2eb8)。

<a id="r_a8d827ae174a2b8f11b50c7e6f31c3708"></a>

```c
unsigned long a4
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[a4](#a8d827ae174a2b8f11b50c7e6f31c3708)。

<a id="r_a67c7626f24035b9cdfef24193e2442c6"></a>

```c
unsigned long a5
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[a5](#a67c7626f24035b9cdfef24193e2442c6)。

<a id="r_a35198a51b070fb2acf76458568204ec1"></a>

```c
unsigned long a6
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[a6](#a35198a51b070fb2acf76458568204ec1)。

<a id="r_af20b0881ec14973d7a6b79f3b146dc7a"></a>

```c
unsigned long a7
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[a7](#af20b0881ec14973d7a6b79f3b146dc7a)。

<a id="r_a9b4cc837fbb958e93a900b58b2ea3a75"></a>

```c
uint64_t resp_data_addr
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[resp_data_addr](#a9b4cc837fbb958e93a900b58b2ea3a75)。

<a id="r_aff7c782bc6690ef134db4e4d999189a7"></a>

```c
uint32_t resp_data_size
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[resp_data_size](#aff7c782bc6690ef134db4e4d999189a7)。

<a id="r_a0b70942fc037346bb5ee051484c21745"></a>

```c
void * priv_data
```

相关声明：[priv_data](#a0b70942fc037346bb5ee051484c21745)。

## 56.2\_详细说明（Detailed Documentation）

<a id="a95e4d0bb03bfca90ea78fc19c581ef7f"></a>

### `a0`

```c
unsigned long sip_svc_request::a0
```

<a id="a3b41176de28f042510d5ca5fc9c4678e"></a>

### `a1`

```c
unsigned long sip_svc_request::a1
```

<a id="aa20d78ab299064e8d4b304f4165bfdf2"></a>

### `a2`

```c
unsigned long sip_svc_request::a2
```

<a id="a6cd5c3cf895daad0c600544a903f2eb8"></a>

### `a3`

```c
unsigned long sip_svc_request::a3
```

<a id="a8d827ae174a2b8f11b50c7e6f31c3708"></a>

### `a4`

```c
unsigned long sip_svc_request::a4
```

<a id="a67c7626f24035b9cdfef24193e2442c6"></a>

### `a5`

```c
unsigned long sip_svc_request::a5
```

<a id="a35198a51b070fb2acf76458568204ec1"></a>

### `a6`

```c
unsigned long sip_svc_request::a6
```

<a id="af20b0881ec14973d7a6b79f3b146dc7a"></a>

### `a7`

```c
unsigned long sip_svc_request::a7
```

<a id="aa8c71f7af00dd3195d49c04df5cb3509"></a>

### `header`

```c
uint32_t sip_svc_request::header
```

<a id="a0b70942fc037346bb5ee051484c21745"></a>

### `priv_data`

```c
void* sip_svc_request::priv_data
```

<a id="a9b4cc837fbb958e93a900b58b2ea3a75"></a>

### `resp_data_addr`

```c
uint64_t sip_svc_request::resp_data_addr
```

<a id="aff7c782bc6690ef134db4e4d999189a7"></a>

### `resp_data_size`

```c
uint32_t sip_svc_request::resp_data_size
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/sip_svc/sip_svc_proto.h`

## 56.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sip_svc/sip_svc_proto.h](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__proto_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P055_shared_vector_desc_t_结构体.md) · [返回大纲](大纲.md) · [下一章](P057_sip_svc_response_结构体.md)
