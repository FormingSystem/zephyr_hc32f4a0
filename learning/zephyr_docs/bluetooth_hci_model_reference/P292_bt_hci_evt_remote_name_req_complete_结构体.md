---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-292
title: bt_hci_evt_remote_name_req_complete_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__remote__name__req__complete.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第292章\_bt\_hci\_evt\_remote\_name\_req\_complete\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__remote__name__req__complete.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 292.1\_数据成员（Data Fields）

<a id="r_ab43d4a3c19d829b829cc7b40a67959f3"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#ab43d4a3c19d829b829cc7b40a67959f3)。

<a id="r_a380121873bf059b7c8a4abdf212f4235"></a>

```c
bt_addr_t bdaddr
```

相关声明：[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[bdaddr](#a380121873bf059b7c8a4abdf212f4235)。

<a id="r_a3e54674692f7fc1670fa389e293714c7"></a>

```c
uint8_t name [248]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[name](#a3e54674692f7fc1670fa389e293714c7)。

## 292.2\_详细说明（Detailed Documentation）

<a id="a380121873bf059b7c8a4abdf212f4235"></a>

### `bdaddr`

```c
bt_addr_t bt_hci_evt_remote_name_req_complete::bdaddr
```

<a id="a3e54674692f7fc1670fa389e293714c7"></a>

### `name`

```c
uint8_t bt_hci_evt_remote_name_req_complete::name[248]
```

<a id="ab43d4a3c19d829b829cc7b40a67959f3"></a>

### `status`

```c
uint8_t bt_hci_evt_remote_name_req_complete::status
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 292.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P291_bt_hci_evt_remote_features_结构体.md) · [返回大纲](大纲.md) · [下一章](P293_bt_hci_evt_remote_version_info_结构体.md)
