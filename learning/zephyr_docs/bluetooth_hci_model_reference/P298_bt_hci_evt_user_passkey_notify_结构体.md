---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-298
title: bt_hci_evt_user_passkey_notify_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__user__passkey__notify.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第298章\_bt\_hci\_evt\_user\_passkey\_notify\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__user__passkey__notify.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 298.1\_数据成员（Data Fields）

<a id="r_af020e1cd131473fe06a193529a0499ac"></a>

```c
bt_addr_t bdaddr
```

相关声明：[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[bdaddr](#af020e1cd131473fe06a193529a0499ac)。

<a id="r_a7f6a367e50d41cb7d8897db05db826be"></a>

```c
uint32_t passkey
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[passkey](#a7f6a367e50d41cb7d8897db05db826be)。

## 298.2\_详细说明（Detailed Documentation）

<a id="af020e1cd131473fe06a193529a0499ac"></a>

### `bdaddr`

```c
bt_addr_t bt_hci_evt_user_passkey_notify::bdaddr
```

<a id="a7f6a367e50d41cb7d8897db05db826be"></a>

### `passkey`

```c
uint32_t bt_hci_evt_user_passkey_notify::passkey
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 298.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P297_bt_hci_evt_user_confirm_req_结构体.md) · [返回大纲](大纲.md) · [下一章](P299_bt_hci_evt_user_passkey_req_结构体.md)
