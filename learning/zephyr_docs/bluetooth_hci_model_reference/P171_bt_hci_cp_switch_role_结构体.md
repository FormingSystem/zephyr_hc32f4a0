---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-171
title: bt_hci_cp_switch_role_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__switch__role.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第171章\_bt\_hci\_cp\_switch\_role\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__switch__role.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 171.1\_数据成员（Data Fields）

<a id="r_afed76d83e552fa3666f8c84df4279938"></a>

```c
bt_addr_t bdaddr
```

相关声明：[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[bdaddr](#afed76d83e552fa3666f8c84df4279938)。

<a id="r_ac6b6acdaf5993384eb3029c9e78407b6"></a>

```c
uint8_t role
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[role](#ac6b6acdaf5993384eb3029c9e78407b6)。

## 171.2\_详细说明（Detailed Documentation）

<a id="afed76d83e552fa3666f8c84df4279938"></a>

### `bdaddr`

```c
bt_addr_t bt_hci_cp_switch_role::bdaddr
```

<a id="ac6b6acdaf5993384eb3029c9e78407b6"></a>

### `role`

```c
uint8_t bt_hci_cp_switch_role::role
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 171.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P170_bt_hci_cp_sniff_subrating_结构体.md) · [返回大纲](大纲.md) · [下一章](P172_bt_hci_cp_user_confirm_reply_结构体.md)
