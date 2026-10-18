---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-332
title: bt_hci_op_le_set_default_rate_parameters_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__op__le__set__default__rate__parameters.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第332章\_bt\_hci\_op\_le\_set\_default\_rate\_parameters\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__op__le__set__default__rate__parameters.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 332.1\_数据成员（Data Fields）

<a id="r_af9afc0e463f068c113c0042f58dcc63d"></a>

```c
uint16_t conn_interval_min
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[conn_interval_min](#af9afc0e463f068c113c0042f58dcc63d)。

<a id="r_ad8051508f324d40bd95e9dbee97b1b2a"></a>

```c
uint16_t conn_interval_max
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[conn_interval_max](#ad8051508f324d40bd95e9dbee97b1b2a)。

<a id="r_a115579391f9fe7ec2536a21c3a42b3ab"></a>

```c
uint16_t subrate_min
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[subrate_min](#a115579391f9fe7ec2536a21c3a42b3ab)。

<a id="r_ad267cc8be963c1d16088a7c14bef19bf"></a>

```c
uint16_t subrate_max
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[subrate_max](#ad267cc8be963c1d16088a7c14bef19bf)。

<a id="r_a4efb8757f63f15e37070b3046490edcf"></a>

```c
uint16_t max_latency
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_latency](#a4efb8757f63f15e37070b3046490edcf)。

<a id="r_aaa9dd1a946c7440e0a985276137ae096"></a>

```c
uint16_t continuation_number
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[continuation_number](#aaa9dd1a946c7440e0a985276137ae096)。

<a id="r_af0fbd935b200c98b5ef6477d127ccdfe"></a>

```c
uint16_t supervision_timeout
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[supervision_timeout](#af0fbd935b200c98b5ef6477d127ccdfe)。

<a id="r_adb818d82c1c38f573a31f22b0ebc817b"></a>

```c
uint16_t min_ce_len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[min_ce_len](#adb818d82c1c38f573a31f22b0ebc817b)。

<a id="r_a630ae05aff2e511b37a522fadd831dd0"></a>

```c
uint16_t max_ce_len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_ce_len](#a630ae05aff2e511b37a522fadd831dd0)。

## 332.2\_详细说明（Detailed Documentation）

<a id="ad8051508f324d40bd95e9dbee97b1b2a"></a>

### `conn_interval_max`

```c
uint16_t bt_hci_op_le_set_default_rate_parameters::conn_interval_max
```

<a id="af9afc0e463f068c113c0042f58dcc63d"></a>

### `conn_interval_min`

```c
uint16_t bt_hci_op_le_set_default_rate_parameters::conn_interval_min
```

<a id="aaa9dd1a946c7440e0a985276137ae096"></a>

### `continuation_number`

```c
uint16_t bt_hci_op_le_set_default_rate_parameters::continuation_number
```

<a id="a630ae05aff2e511b37a522fadd831dd0"></a>

### `max_ce_len`

```c
uint16_t bt_hci_op_le_set_default_rate_parameters::max_ce_len
```

<a id="a4efb8757f63f15e37070b3046490edcf"></a>

### `max_latency`

```c
uint16_t bt_hci_op_le_set_default_rate_parameters::max_latency
```

<a id="adb818d82c1c38f573a31f22b0ebc817b"></a>

### `min_ce_len`

```c
uint16_t bt_hci_op_le_set_default_rate_parameters::min_ce_len
```

<a id="ad267cc8be963c1d16088a7c14bef19bf"></a>

### `subrate_max`

```c
uint16_t bt_hci_op_le_set_default_rate_parameters::subrate_max
```

<a id="a115579391f9fe7ec2536a21c3a42b3ab"></a>

### `subrate_min`

```c
uint16_t bt_hci_op_le_set_default_rate_parameters::subrate_min
```

<a id="af0fbd935b200c98b5ef6477d127ccdfe"></a>

### `supervision_timeout`

```c
uint16_t bt_hci_op_le_set_default_rate_parameters::supervision_timeout
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 332.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P331_bt_hci_op_le_read_min_supported_conn_interval_结构体.md) · [返回大纲](大纲.md) · [下一章](P333_bt_hci_pkt_cmd_rsp_结构体.md)
