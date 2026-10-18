---
id: learning.zephyr-docs.network-core-model-reference.page-105
title: net_linkaddr_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__linkaddr.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第105章\_net\_linkaddr\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__linkaddr.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

硬件链路地址（Hardware Link Address）结构。

```c
#include <zephyr/net/net_linkaddr.h>
```

<a id="details"></a>

硬件链路地址结构（Hardware link address structure）。用于保存链路地址信息。需要存储链路层地址（Link layer address）时，使用此变体。注意，不能将其强制转换为 `net_linkaddr`：`uint8_t *` 与 `uint8_t addr[]` 的处理方式不同，而且这里有意采用了不同的字段顺序。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 105.1\_数据成员（Data Fields）

<a id="r_a5f5b4c3d353261d0fab8011aa09f00d7"></a>

```c
uint8_t type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[type](#a5f5b4c3d353261d0fab8011aa09f00d7)。

此地址的类型（Address kind）。

<a id="r_a7b2f8ebe68b557eb9cbb4c2f2ecd70e0"></a>

```c
uint8_t len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[len](#a7b2f8ebe68b557eb9cbb4c2f2ecd70e0)。

链路层地址（LL address）的实际长度。

<a id="r_a58de2645f8c7d31c97026f0bd5262881"></a>

```c
uint8_t addr [6]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[addr](#a58de2645f8c7d31c97026f0bd5262881)。

表示该地址的字节数组（Byte array）。

## 105.2\_详细说明（Detailed Documentation）

<a id="a58de2645f8c7d31c97026f0bd5262881"></a>

### `addr`

```c
uint8_t net_linkaddr::addr[6]
```

表示该地址的字节数组（Byte array）。

<a id="a7b2f8ebe68b557eb9cbb4c2f2ecd70e0"></a>

### `len`

```c
uint8_t net_linkaddr::len
```

链路层地址（LL address）的实际长度。

<a id="a5f5b4c3d353261d0fab8011aa09f00d7"></a>

### `type`

```c
uint8_t net_linkaddr::type
```

此地址的类型（Address kind）。

本数据类型文档由以下文件生成：

- `zephyr/net/net_linkaddr.h`

## 105.3\_原页交叉引用（Cross References）

- [zephyr/net/net_linkaddr.h](https://docs.zephyrproject.org/latest/doxygen/html/net__linkaddr_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_linkaddr](P105_net_linkaddr_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P104_net_linger_结构体.md) · [返回大纲](大纲.md) · [下一章](P106_net_lldp_chassis_tlv_结构体.md)
