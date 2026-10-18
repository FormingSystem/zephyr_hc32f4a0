---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-415
title: bt_hci_rp_read_local_features_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__read__local__features.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第415章\_bt\_hci\_rp\_read\_local\_features\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__rp__read__local__features.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 415.1\_数据成员（Data Fields）

<a id="r_a0ff73da5704ada47f8f79c113254820d"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a0ff73da5704ada47f8f79c113254820d)。

<a id="r_ae660b4a772f96bf72bd08124bf26b352"></a>

```c
uint8_t features [8]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[features](#ae660b4a772f96bf72bd08124bf26b352)。

## 415.2\_详细说明（Detailed Documentation）

<a id="ae660b4a772f96bf72bd08124bf26b352"></a>

### `features`

```c
uint8_t bt_hci_rp_read_local_features::features[8]
```

<a id="a0ff73da5704ada47f8f79c113254820d"></a>

### `status`

```c
uint8_t bt_hci_rp_read_local_features::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 415.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P414_bt_hci_rp_read_local_ext_features_结构体.md) · [返回大纲](大纲.md) · [下一章](P416_bt_hci_rp_read_local_version_info_结构体.md)
