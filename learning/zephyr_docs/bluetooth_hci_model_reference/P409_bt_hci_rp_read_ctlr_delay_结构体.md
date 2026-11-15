---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-409
title: bt_hci_rp_read_ctlr_delay_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__read__ctlr__delay.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第409章\_bt\_hci\_rp\_read\_ctlr\_delay\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__read__ctlr__delay.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 409.1\_数据成员（Data Fields）

<a id="r_a2f17081cf767643f3a9ad9d115ef5320"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a2f17081cf767643f3a9ad9d115ef5320)。

<a id="r_ab48d1d92cdf9470a93487434b3824d17"></a>

```c
uint8_t min_ctlr_delay [3]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[min_ctlr_delay](#ab48d1d92cdf9470a93487434b3824d17)。

<a id="r_a4c468053c4a86d1ab462c1e6f17f1013"></a>

```c
uint8_t max_ctlr_delay [3]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max_ctlr_delay](#a4c468053c4a86d1ab462c1e6f17f1013)。

## 409.2\_详细说明（Detailed Documentation）

<a id="a4c468053c4a86d1ab462c1e6f17f1013"></a>

### `max_ctlr_delay`

```c
uint8_t bt_hci_rp_read_ctlr_delay::max_ctlr_delay[3]
```

<a id="ab48d1d92cdf9470a93487434b3824d17"></a>

### `min_ctlr_delay`

```c
uint8_t bt_hci_rp_read_ctlr_delay::min_ctlr_delay[3]
```

<a id="a2f17081cf767643f3a9ad9d115ef5320"></a>

### `status`

```c
uint8_t bt_hci_rp_read_ctlr_delay::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 409.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P408_bt_hci_rp_read_conn_accept_timeout_结构体.md) · [返回大纲](大纲.md) · [下一章](P410_bt_hci_rp_read_default_link_policy_settings_结构体.md)
