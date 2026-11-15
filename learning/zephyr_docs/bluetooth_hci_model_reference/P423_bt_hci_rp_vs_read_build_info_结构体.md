---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-423
title: bt_hci_rp_vs_read_build_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__vs__read__build__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第423章\_bt\_hci\_rp\_vs\_read\_build\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__vs__read__build__info.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_vs.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 423.1\_数据成员（Data Fields）

<a id="r_acdebc0d6f8d713075c6e5e69cf136ea3"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#acdebc0d6f8d713075c6e5e69cf136ea3)。

<a id="r_aba2aaa3916221768412eed39cc85ab5f"></a>

```c
uint8_t info [0]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[info](#aba2aaa3916221768412eed39cc85ab5f)。

## 423.2\_详细说明（Detailed Documentation）

<a id="aba2aaa3916221768412eed39cc85ab5f"></a>

### `info`

```c
uint8_t bt_hci_rp_vs_read_build_info::info[0]
```

<a id="acdebc0d6f8d713075c6e5e69cf136ea3"></a>

### `status`

```c
uint8_t bt_hci_rp_vs_read_build_info::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_vs.h`

## 423.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_vs.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__vs_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P422_bt_hci_rp_user_confirm_reply_结构体.md) · [返回大纲](大纲.md) · [下一章](P424_bt_hci_rp_vs_read_chip_temp_结构体.md)
