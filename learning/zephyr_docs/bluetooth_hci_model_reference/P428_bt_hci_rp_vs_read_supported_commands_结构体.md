---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-428
title: bt_hci_rp_vs_read_supported_commands_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__vs__read__supported__commands.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第428章\_bt\_hci\_rp\_vs\_read\_supported\_commands\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__vs__read__supported__commands.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_vs.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 428.1\_数据成员（Data Fields）

<a id="r_afe9e5d1647b0cea192fa281367dc6c85"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#afe9e5d1647b0cea192fa281367dc6c85)。

<a id="r_a699129590cb1f5a3418d8e0eab3868e4"></a>

```c
uint8_t commands [64]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[commands](#a699129590cb1f5a3418d8e0eab3868e4)。

## 428.2\_详细说明（Detailed Documentation）

<a id="a699129590cb1f5a3418d8e0eab3868e4"></a>

### `commands`

```c
uint8_t bt_hci_rp_vs_read_supported_commands::commands[64]
```

<a id="afe9e5d1647b0cea192fa281367dc6c85"></a>

### `status`

```c
uint8_t bt_hci_rp_vs_read_supported_commands::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_vs.h`

## 428.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_vs.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__vs_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P427_bt_hci_rp_vs_read_static_addrs_结构体.md) · [返回大纲](大纲.md) · [下一章](P429_bt_hci_rp_vs_read_supported_features_结构体.md)
