---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-174
title: bt_hci_cp_user_passkey_reply_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__user__passkey__reply.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第174章\_bt\_hci\_cp\_user\_passkey\_reply\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__user__passkey__reply.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 174.1\_数据成员（Data Fields）

<a id="r_a56dbb4a858ecbf36eee61e24ed3742cf"></a>

```c
bt_addr_t bdaddr
```

相关声明：[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[bdaddr](#a56dbb4a858ecbf36eee61e24ed3742cf)。

<a id="r_a80483025a32f37e7f75b3a220d48148c"></a>

```c
uint32_t passkey
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[passkey](#a80483025a32f37e7f75b3a220d48148c)。

## 174.2\_详细说明（Detailed Documentation）

<a id="a56dbb4a858ecbf36eee61e24ed3742cf"></a>

### `bdaddr`

```c
bt_addr_t bt_hci_cp_user_passkey_reply::bdaddr
```

<a id="a80483025a32f37e7f75b3a220d48148c"></a>

### `passkey`

```c
uint32_t bt_hci_cp_user_passkey_reply::passkey
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 174.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P173_bt_hci_cp_user_passkey_neg_reply_结构体.md) · [返回大纲](大纲.md) · [下一章](P175_bt_hci_cp_vs_read_tx_power_level_结构体.md)
