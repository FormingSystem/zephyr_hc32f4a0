---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-57
title: bt_csip_set_coordinator_set_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__csip__set__coordinator__set__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第57章\_bt\_csip\_set\_coordinator\_set\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__csip__set__coordinator__set__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

特定集合（Set）的信息。

```c
#include <zephyr/bluetooth/audio/csip.h>
```

<a id="details"></a>

特定集合（Set）的信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 57.1\_数据成员（Data Fields）

<a id="r_aa5e41081508a13948f4c899d1212e2bf"></a>

```c
uint8_t sirk [16U]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sirk](#aa5e41081508a13948f4c899d1212e2bf)。

16 个八位组的集合身份解析密钥（Set Identity Resolving Key，SIRK）。

<a id="r_ac969998670d04d6dea96ea6f666f3fc9"></a>

```c
uint8_t set_size
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[set_size](#ac969998670d04d6dea96ea6f666f3fc9)。

集合大小（Set size）。

<a id="r_a362fd6d8afbde9eb77d4f9a47aecb03c"></a>

```c
uint8_t rank
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rank](#a362fd6d8afbde9eb77d4f9a47aecb03c)。

远端设备上此集合的排序值（Rank）。

<a id="r_aa85b6a24ea8f020bb1312065e461c4b2"></a>

```c
bool lockable
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[lockable](#aa85b6a24ea8f020bb1312065e461c4b2)。

此设备上的集合是否可锁定（Lockable）。

## 57.2\_详细说明（Detailed Documentation）

<a id="aa85b6a24ea8f020bb1312065e461c4b2"></a>

### `lockable`

```c
bool bt_csip_set_coordinator_set_info::lockable
```

此设备上的集合是否可锁定（Lockable）。

<a id="a362fd6d8afbde9eb77d4f9a47aecb03c"></a>

### `rank`

```c
uint8_t bt_csip_set_coordinator_set_info::rank
```

远端设备上此集合的排序值（Rank）。

服务器未公开此项时为 `0`。

<a id="ac969998670d04d6dea96ea6f666f3fc9"></a>

### `set_size`

```c
uint8_t bt_csip_set_coordinator_set_info::set_size
```

集合大小（Set size）。

服务器未公开此项时为 `0`。

<a id="aa5e41081508a13948f4c899d1212e2bf"></a>

### `sirk`

```c
uint8_t bt_csip_set_coordinator_set_info::sirk[16U]
```

16 个八位组的集合身份解析密钥（Set Identity Resolving Key，SIRK）。

服务器可能不通过蓝牙公开集合身份解析密钥（SIRK），此时可能需要带外方式（Out-of-band solution）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/csip.h`

## 57.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/csip.h](https://docs.zephyrproject.org/latest/doxygen/html/csip_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P056_bt_csip_set_coordinator_csis_inst_结构体.md) · [返回大纲](大纲.md) · [下一章](P058_bt_csip_set_coordinator_set_member_结构体.md)
