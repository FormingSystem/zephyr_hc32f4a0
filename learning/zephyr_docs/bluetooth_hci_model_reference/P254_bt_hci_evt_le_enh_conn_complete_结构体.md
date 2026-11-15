---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-254
title: bt_hci_evt_le_enh_conn_complete_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__enh__conn__complete.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第254章\_bt\_hci\_evt\_le\_enh\_conn\_complete\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__evt__le__enh__conn__complete.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 254.1\_数据成员（Data Fields）

<a id="r_ae26575416658bf285c45f57ddf426eb2"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#ae26575416658bf285c45f57ddf426eb2)。

<a id="r_a13ceff445de6a89f6ea0e832e8b3fba9"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a13ceff445de6a89f6ea0e832e8b3fba9)。

<a id="r_af24298f8c1d58882b4962a14086fc5c7"></a>

```c
uint8_t role
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[role](#af24298f8c1d58882b4962a14086fc5c7)。

<a id="r_a4906d6991489e95f8c74aacf5ad8c22e"></a>

```c
bt_addr_le_t peer_addr
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[peer_addr](#a4906d6991489e95f8c74aacf5ad8c22e)。

<a id="r_ab275bcb4a3dd09525b446c01e4e5fdad"></a>

```c
bt_addr_t local_rpa
```

相关声明：[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[local_rpa](#ab275bcb4a3dd09525b446c01e4e5fdad)。

<a id="r_a4ece4379733f1ab404fa03f4794192a4"></a>

```c
bt_addr_t peer_rpa
```

相关声明：[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[peer_rpa](#a4ece4379733f1ab404fa03f4794192a4)。

<a id="r_ac0565ecf0c459275d147933bbdaa9fbc"></a>

```c
uint16_t interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[interval](#ac0565ecf0c459275d147933bbdaa9fbc)。

<a id="r_a7276bf433c21ffcd3582463492af107b"></a>

```c
uint16_t latency
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[latency](#a7276bf433c21ffcd3582463492af107b)。

<a id="r_aa99df131f3fb0330ff8051015d2b78dc"></a>

```c
uint16_t supv_timeout
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[supv_timeout](#aa99df131f3fb0330ff8051015d2b78dc)。

<a id="r_a5641e5cb17df4613cd85f5ad3ba8541c"></a>

```c
uint8_t clock_accuracy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[clock_accuracy](#a5641e5cb17df4613cd85f5ad3ba8541c)。

## 254.2\_详细说明（Detailed Documentation）

<a id="a5641e5cb17df4613cd85f5ad3ba8541c"></a>

### `clock_accuracy`

```c
uint8_t bt_hci_evt_le_enh_conn_complete::clock_accuracy
```

<a id="a13ceff445de6a89f6ea0e832e8b3fba9"></a>

### `handle`

```c
uint16_t bt_hci_evt_le_enh_conn_complete::handle
```

<a id="ac0565ecf0c459275d147933bbdaa9fbc"></a>

### `interval`

```c
uint16_t bt_hci_evt_le_enh_conn_complete::interval
```

<a id="a7276bf433c21ffcd3582463492af107b"></a>

### `latency`

```c
uint16_t bt_hci_evt_le_enh_conn_complete::latency
```

<a id="ab275bcb4a3dd09525b446c01e4e5fdad"></a>

### `local_rpa`

```c
bt_addr_t bt_hci_evt_le_enh_conn_complete::local_rpa
```

<a id="a4906d6991489e95f8c74aacf5ad8c22e"></a>

### `peer_addr`

```c
bt_addr_le_t bt_hci_evt_le_enh_conn_complete::peer_addr
```

<a id="a4ece4379733f1ab404fa03f4794192a4"></a>

### `peer_rpa`

```c
bt_addr_t bt_hci_evt_le_enh_conn_complete::peer_rpa
```

<a id="af24298f8c1d58882b4962a14086fc5c7"></a>

### `role`

```c
uint8_t bt_hci_evt_le_enh_conn_complete::role
```

<a id="ae26575416658bf285c45f57ddf426eb2"></a>

### `status`

```c
uint8_t bt_hci_evt_le_enh_conn_complete::status
```

<a id="aa99df131f3fb0330ff8051015d2b78dc"></a>

### `supv_timeout`

```c
uint16_t bt_hci_evt_le_enh_conn_complete::supv_timeout
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 254.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P253_bt_hci_evt_le_direct_adv_report_结构体.md) · [返回大纲](大纲.md) · [下一章](P255_bt_hci_evt_le_enh_conn_complete_v2_结构体.md)
