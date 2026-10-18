---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-43
title: bt_df_conn_cte_req_params_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__df__conn__cte__req__params.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第43章\_bt\_df\_conn\_cte\_req\_params\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__df__conn__cte__req__params.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/direction.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 43.1\_数据成员（Data Fields）

<a id="r_ab8148905943e0d87a37740ab891b9ef7"></a>

```c
uint16_t interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[interval](#ab8148905943e0d87a37740ab891b9ef7)。

请求的恒定音调扩展请求过程发起间隔（CTE Request procedure interval）。

<a id="r_a71340a450e573612a271467c51110166"></a>

```c
uint8_t cte_length
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cte_length](#a71340a450e573612a271467c51110166)。

请求的恒定音调扩展长度（CTE length），以 8 微秒为单位。

<a id="r_ae8232614ec9201e4572675d793b2292a"></a>

```c
uint8_t cte_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cte_type](#ae8232614ec9201e4572675d793b2292a)。

请求的恒定音调扩展类型（CTE type）。

## 43.2\_详细说明（Detailed Documentation）

<a id="a71340a450e573612a271467c51110166"></a>

### `cte_length`

```c
uint8_t bt_df_conn_cte_req_params::cte_length
```

请求的恒定音调扩展长度（CTE length），以 8 微秒为单位。

<a id="ae8232614ec9201e4572675d793b2292a"></a>

### `cte_type`

```c
uint8_t bt_df_conn_cte_req_params::cte_type
```

请求的恒定音调扩展类型（CTE type）。

允许值由 `bt_df_cte_type` 定义，但不包含 `BT_DF_CTE_TYPE_NONE` 和 `BT_DF_CTE_TYPE_ALL`。

<a id="ab8148905943e0d87a37740ab891b9ef7"></a>

### `interval`

```c
uint16_t bt_df_conn_cte_req_params::interval
```

请求的恒定音调扩展请求过程发起间隔（CTE Request procedure interval）。

值 `0x0` 表示仅执行该过程一次。其他值以连接事件数量（Connection events）为单位表示间隔，用于周期执行该命令。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/direction.h`

## 43.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/direction.h](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_df_cte_type](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#a64bf01dee8bc4bbc62e0dbc356726a05)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P042_bt_df_adv_cte_tx_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P044_bt_df_conn_cte_rx_param_结构体.md)
