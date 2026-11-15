---
id: learning.zephyr-docs.network-service-model-reference.page-28
title: lcp_options_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structlcp__options.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第28章\_lcp\_options\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structlcp__options.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

链路控制协议（Link Control Protocol）的选项。

```c
#include <zephyr/net/ppp.h>
```

<a id="details"></a>

链路控制协议（Link Control Protocol）的选项。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 28.1\_数据成员（Data Fields）

<a id="r_a68d9f004596bfac6dea9b14bd22e9dda"></a>

```c
uint32_t magic
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[magic](#a68d9f004596bfac6dea9b14bd22e9dda)。

魔数（Magic number）。

<a id="r_a2672e1374c25aac1571adccadda5283e"></a>

```c
uint32_t async_map
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[async_map](#a2672e1374c25aac1571adccadda5283e)。

异步字符映射（Async character map）。

<a id="r_a028da648c4b8cdd9330d9195a161e847"></a>

```c
uint16_t mru
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[mru](#a028da648c4b8cdd9330d9195a161e847)。

最大接收单元（Maximum Receive Unit，MRU）值。

<a id="r_a560d009cb642fff99ef83a9e6c056c6b"></a>

```c
uint16_t auth_proto
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[auth_proto](#a560d009cb642fff99ef83a9e6c056c6b)。

协商采用的身份验证协议（authentication protocol）；0 表示不使用。

<a id="r_ae176ccd3d5c747f28023c0621714f340"></a>

```c
bool pfc
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[pfc](#ae176ccd3d5c747f28023c0621714f340)。

已协商启用协议字段压缩（Protocol-Field-Compression）。

<a id="r_a3479abfcee498aca22ec2ca461e985d5"></a>

```c
bool acfc
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[acfc](#a3479abfcee498aca22ec2ca461e985d5)。

已协商启用地址与控制字段压缩（Address-and-Control-Field-Compression）。

## 28.2\_详细说明（Detailed Documentation）

<a id="a3479abfcee498aca22ec2ca461e985d5"></a>

### `acfc`

```c
bool lcp_options::acfc
```

已协商启用地址与控制字段压缩（Address-and-Control-Field-Compression）。

<a id="a2672e1374c25aac1571adccadda5283e"></a>

### `async_map`

```c
uint32_t lcp_options::async_map
```

异步字符映射（Async character map）。

<a id="a560d009cb642fff99ef83a9e6c056c6b"></a>

### `auth_proto`

```c
uint16_t lcp_options::auth_proto
```

协商采用的身份验证协议（authentication protocol）；0 表示不使用。

<a id="a68d9f004596bfac6dea9b14bd22e9dda"></a>

### `magic`

```c
uint32_t lcp_options::magic
```

魔数（Magic number）。

<a id="a028da648c4b8cdd9330d9195a161e847"></a>

### `mru`

```c
uint16_t lcp_options::mru
```

最大接收单元（Maximum Receive Unit，MRU）值。

<a id="ae176ccd3d5c747f28023c0621714f340"></a>

### `pfc`

```c
bool lcp_options::pfc
```

已协商启用协议字段压缩（Protocol-Field-Compression）。

本数据类型文档由以下文件生成：

- `zephyr/net/ppp.h`

## 28.3\_原页交叉引用（Cross References）

- [zephyr/net/ppp.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2ppp_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P027_ipv6cp_options_结构体.md) · [返回大纲](大纲.md) · [下一章](P029_loopback_disk_access_结构体.md)
