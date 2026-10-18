---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-114
title: bt_le_per_adv_response_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__per__adv__response__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第114章\_bt\_le\_per\_adv\_response\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__per__adv__response__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

已接收的带响应周期广播（PAwR）响应的信息。

```c
#include <zephyr/bluetooth/bluetooth.h>
```

<a id="details"></a>

已接收的带响应周期广播响应信息（PAwR response information）。控制器表示一个或多个已同步设备已响应周期广播子事件指示时，`bt_le_per_adv_response_info` 保存相关子事件、状态、响应发射功率（TX power）、响应接收信号强度指示（RSSI）、广播恒定音调扩展（CTE），以及收到响应的时隙等信息。注意（Note）：用于 `bt_le_ext_adv_cb`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 114.1\_数据成员（Data Fields）

<a id="r_a1b87ab77f5c7d4ee0c1c612bcfb424d5"></a>

```c
uint8_t subevent
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[subevent](#a1b87ab77f5c7d4ee0c1c612bcfb424d5)。

接收到响应的子事件（Subevent）。

<a id="r_ab17f33cb713d258bf6c863a64e5aba07"></a>

```c
uint8_t tx_status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[tx_status](#ab17f33cb713d258bf6c863a64e5aba07)。

子事件指示的状态（Subevent indication status）。

<a id="r_a7ed20f695e0d696eaab7cddc4e3c11fb"></a>

```c
int8_t tx_power
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[tx_power](#a7ed20f695e0d696eaab7cddc4e3c11fb)。

响应的发射功率（TX power），单位为 dBm。

<a id="r_a2db58fb452a07290ab4a50892c682837"></a>

```c
int8_t rssi
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[rssi](#a2db58fb452a07290ab4a50892c682837)。

响应的接收信号强度指示（RSSI），单位为 dBm。

<a id="r_a52b0c612b09cfcb3eb2ea475614c34b8"></a>

```c
uint8_t cte_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cte_type](#a52b0c612b09cfcb3eb2ea475614c34b8)。

广播中的恒定音调扩展（Constant Tone Extension，CTE），参见 `bt_df_cte_type`。

<a id="r_a83cc642c9f22c767421644e7d8233001"></a>

```c
uint8_t response_slot
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[response_slot](#a83cc642c9f22c767421644e7d8233001)。

接收到响应的时隙（Slot）。

## 114.2\_详细说明（Detailed Documentation）

<a id="a52b0c612b09cfcb3eb2ea475614c34b8"></a>

### `cte_type`

```c
uint8_t bt_le_per_adv_response_info::cte_type
```

广播中的恒定音调扩展（Constant Tone Extension，CTE），参见 `bt_df_cte_type`。

<a id="a83cc642c9f22c767421644e7d8233001"></a>

### `response_slot`

```c
uint8_t bt_le_per_adv_response_info::response_slot
```

接收到响应的时隙（Slot）。

<a id="a2db58fb452a07290ab4a50892c682837"></a>

### `rssi`

```c
int8_t bt_le_per_adv_response_info::rssi
```

响应的接收信号强度指示（RSSI），单位为 dBm。

<a id="a1b87ab77f5c7d4ee0c1c612bcfb424d5"></a>

### `subevent`

```c
uint8_t bt_le_per_adv_response_info::subevent
```

接收到响应的子事件（Subevent）。

<a id="a7ed20f695e0d696eaab7cddc4e3c11fb"></a>

### `tx_power`

```c
int8_t bt_le_per_adv_response_info::tx_power
```

响应的发射功率（TX power），单位为 dBm。

<a id="ab17f33cb713d258bf6c863a64e5aba07"></a>

### `tx_status`

```c
uint8_t bt_le_per_adv_response_info::tx_status
```

子事件指示的状态（Subevent indication status）。

`0` 表示已发送子事件指示（Subevent indication）；`1` 表示未发送；其余值保留供将来使用（RFU）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/bluetooth.h`

## 114.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [bt_df_cte_type](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html#a64bf01dee8bc4bbc62e0dbc356726a05)
- [bt_le_per_adv_response_info](P114_bt_le_per_adv_response_info_结构体.md)
- [bt_le_ext_adv_cb](P103_bt_le_ext_adv_cb_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P113_bt_le_per_adv_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P115_bt_le_per_adv_response_params_结构体.md)
