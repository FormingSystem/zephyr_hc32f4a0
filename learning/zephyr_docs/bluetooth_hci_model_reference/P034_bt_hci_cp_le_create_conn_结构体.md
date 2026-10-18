---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-34
title: bt_hci_cp_le_create_conn_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__create__conn.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第34章\_bt\_hci\_cp\_le\_create\_conn\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__le__create__conn.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 34.1\_数据成员（Data Fields）

<a id="r_a1a830a0f6cd961d534c338031b2b691b"></a>

```c
uint16_t scan_interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[scan_interval](#a1a830a0f6cd961d534c338031b2b691b)。

<a id="r_abf61e67f5e20adc44b5b9314ed43bccc"></a>

```c
uint16_t scan_window
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[scan_window](#abf61e67f5e20adc44b5b9314ed43bccc)。

<a id="r_a2ca5063f5082a0f330676e56253a21c7"></a>

```c
uint8_t filter_policy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[filter_policy](#a2ca5063f5082a0f330676e56253a21c7)。

<a id="r_aa51da7602eb2b44528964c8b706bb043"></a>

```c
bt_addr_le_t peer_addr
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[peer_addr](#aa51da7602eb2b44528964c8b706bb043)。

<a id="r_a63c7f9e89528105e484a60e41eeb8a30"></a>

```c
uint8_t own_addr_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[own_addr_type](#a63c7f9e89528105e484a60e41eeb8a30)。

<a id="r_a988cf154b0df1ff9af8d34ce73a920dd"></a>

```c
uint16_t conn_interval_min
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[conn_interval_min](#a988cf154b0df1ff9af8d34ce73a920dd)。

<a id="r_aa009d54866d9c675c2785412bdbd182f"></a>

```c
uint16_t conn_interval_max
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[conn_interval_max](#aa009d54866d9c675c2785412bdbd182f)。

<a id="r_a5a9d5c1d44adac876680a517b1fad63f"></a>

```c
uint16_t conn_latency
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[conn_latency](#a5a9d5c1d44adac876680a517b1fad63f)。

<a id="r_ae8e0ad70a3b23ac035c237db0d57adc4"></a>

```c
uint16_t supervision_timeout
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[supervision_timeout](#ae8e0ad70a3b23ac035c237db0d57adc4)。

<a id="r_a476501ccd209f3a52082decf906ca8f0"></a>

```c
uint16_t min_ce_len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[min_ce_len](#a476501ccd209f3a52082decf906ca8f0)。

<a id="r_a5b329aa8b48e03998e969b2436d35ab5"></a>

```c
uint16_t max_ce_len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_ce_len](#a5b329aa8b48e03998e969b2436d35ab5)。

## 34.2\_详细说明（Detailed Documentation）

<a id="aa009d54866d9c675c2785412bdbd182f"></a>

### `conn_interval_max`

```c
uint16_t bt_hci_cp_le_create_conn::conn_interval_max
```

<a id="a988cf154b0df1ff9af8d34ce73a920dd"></a>

### `conn_interval_min`

```c
uint16_t bt_hci_cp_le_create_conn::conn_interval_min
```

<a id="a5a9d5c1d44adac876680a517b1fad63f"></a>

### `conn_latency`

```c
uint16_t bt_hci_cp_le_create_conn::conn_latency
```

<a id="a2ca5063f5082a0f330676e56253a21c7"></a>

### `filter_policy`

```c
uint8_t bt_hci_cp_le_create_conn::filter_policy
```

<a id="a5b329aa8b48e03998e969b2436d35ab5"></a>

### `max_ce_len`

```c
uint16_t bt_hci_cp_le_create_conn::max_ce_len
```

<a id="a476501ccd209f3a52082decf906ca8f0"></a>

### `min_ce_len`

```c
uint16_t bt_hci_cp_le_create_conn::min_ce_len
```

<a id="a63c7f9e89528105e484a60e41eeb8a30"></a>

### `own_addr_type`

```c
uint8_t bt_hci_cp_le_create_conn::own_addr_type
```

<a id="aa51da7602eb2b44528964c8b706bb043"></a>

### `peer_addr`

```c
bt_addr_le_t bt_hci_cp_le_create_conn::peer_addr
```

<a id="a1a830a0f6cd961d534c338031b2b691b"></a>

### `scan_interval`

```c
uint16_t bt_hci_cp_le_create_conn::scan_interval
```

<a id="abf61e67f5e20adc44b5b9314ed43bccc"></a>

### `scan_window`

```c
uint16_t bt_hci_cp_le_create_conn::scan_window
```

<a id="ae8e0ad70a3b23ac035c237db0d57adc4"></a>

### `supervision_timeout`

```c
uint16_t bt_hci_cp_le_create_conn::supervision_timeout
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 34.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P033_bt_hci_cp_le_create_cis_结构体.md) · [返回大纲](大纲.md) · [下一章](P035_bt_hci_cp_le_cs_create_config_结构体.md)
