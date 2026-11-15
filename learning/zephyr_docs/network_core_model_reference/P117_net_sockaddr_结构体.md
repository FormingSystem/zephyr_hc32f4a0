---
id: learning.zephyr-docs.network-core-model-reference.page-117
title: net_sockaddr_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__sockaddr.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第117章\_net\_sockaddr\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__sockaddr.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

通用sockaddr结构。

```c
#include <zephyr/net/net_ip.h>
```

<a id="details"></a>

通用套接字地址结构（Generic sockaddr struct）。必须强制转换为适当类型。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 117.1\_数据成员（Data Fields）

<a id="r_a5cf76ac4582ea3c90fc871a44656490a"></a>

```c
net_sa_family_t sa_family
```

相关声明：[net_sa_family_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga8b4cfadf1b284e52d6905ca88657b48a)、[sa_family](#a5cf76ac4582ea3c90fc871a44656490a)。

地址族（Address family）。

## 117.2\_详细说明（Detailed Documentation）

<a id="a5cf76ac4582ea3c90fc871a44656490a"></a>

### `sa_family`

```c
net_sa_family_t net_sockaddr::sa_family
```

地址族（Address family）。

本数据类型文档由以下文件生成：

- `zephyr/net/net_ip.h`

## 117.3\_原页交叉引用（Cross References）

- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h_source.html)
- [net_sa_family_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga8b4cfadf1b284e52d6905ca88657b48a)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P116_net_ptp_time_结构体.md) · [返回大纲](大纲.md) · [下一章](P118_net_sockaddr_can_结构体.md)
