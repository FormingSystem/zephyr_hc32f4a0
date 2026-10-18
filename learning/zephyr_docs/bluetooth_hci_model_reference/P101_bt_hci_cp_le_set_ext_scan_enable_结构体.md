---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-101
title: bt_hci_cp_le_set_ext_scan_enable_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__ext__scan__enable.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第101章\_bt\_hci\_cp\_le\_set\_ext\_scan\_enable\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__set__ext__scan__enable.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 101.1\_数据成员（Data Fields）

<a id="r_a922d0c5a7ccb6c1e1864f662227b8307"></a>

```c
uint8_t enable
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[enable](#a922d0c5a7ccb6c1e1864f662227b8307)。

<a id="r_aa5b0939838ab13eb8299f4a4b2fd3f14"></a>

```c
uint8_t filter_dup
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[filter_dup](#aa5b0939838ab13eb8299f4a4b2fd3f14)。

<a id="r_adcd5e00a240f3e7395d0d25994b4013a"></a>

```c
uint16_t duration
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[duration](#adcd5e00a240f3e7395d0d25994b4013a)。

<a id="r_aa60c8ade7047dcd202d83cfc3f18ada2"></a>

```c
uint16_t period
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[period](#aa60c8ade7047dcd202d83cfc3f18ada2)。

## 101.2\_详细说明（Detailed Documentation）

<a id="adcd5e00a240f3e7395d0d25994b4013a"></a>

### `duration`

```c
uint16_t bt_hci_cp_le_set_ext_scan_enable::duration
```

<a id="a922d0c5a7ccb6c1e1864f662227b8307"></a>

### `enable`

```c
uint8_t bt_hci_cp_le_set_ext_scan_enable::enable
```

<a id="aa5b0939838ab13eb8299f4a4b2fd3f14"></a>

### `filter_dup`

```c
uint8_t bt_hci_cp_le_set_ext_scan_enable::filter_dup
```

<a id="aa60c8ade7047dcd202d83cfc3f18ada2"></a>

### `period`

```c
uint16_t bt_hci_cp_le_set_ext_scan_enable::period
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 101.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P100_bt_hci_cp_le_set_ext_adv_param_v2_结构体.md) · [返回大纲](大纲.md) · [下一章](P102_bt_hci_cp_le_set_ext_scan_param_结构体.md)
