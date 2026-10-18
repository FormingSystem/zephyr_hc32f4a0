---
id: learning.zephyr-docs.network-service-model-reference.page-12
title: ethernet_qbv_param_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structethernet__qbv__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_ethernet\_qbv\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structethernet__qbv__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

以太网Qbv的专用参数。

```c
#include <zephyr/net/ethernet.h>
```

<a id="details"></a>

以太网Qbv的专用参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 12.1\_数据成员（Data Fields）

<a id="r_a037492458f47905b894a2269ff7365cd"></a>

```c
int port_id
```

相关声明：[port_id](#a037492458f47905b894a2269ff7365cd)。

端口 ID。

<a id="r_a2184250d397bd749764adc52ec3a1621"></a>

```c
enum ethernet_qbv_param_type type
```

相关声明：[type](#a2184250d397bd749764adc52ec3a1621)。

Qbv 参数类型。

<a id="r_a36702c57bea42c37c1341e144ced4f7d"></a>

```c
enum ethernet_qbv_state_type state
```

相关声明：[state](#a36702c57bea42c37c1341e144ced4f7d)。

这些参数所属的状态：管理态或运行态（Admin/Oper）。

```c
union {
```

<a id="r_aadfef84d408d1c13193922043688ba03"></a>

```c
bool enabled
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[enabled](#a0742dbe52f01addbb319e2fcb354d064)。

启用 Qbv 时为 `true`，否则为 `false`。

```c
struct {
```

<a id="r_a80ff892199aa40bd904179e3b77b1e9b"></a>

```c
bool gate_status [NET_TC_TX_COUNT]
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[gate_status](#a44b6ce52faeae761c5ebe49fad5338cd)。

`true` 表示打开，`false` 表示关闭。

<a id="r_a4cffe4ea79f06c87dfe69610f8d4f03d"></a>

```c
enum ethernet_gate_state_operation operation
```

相关声明：[operation](#a8471f7eb20a72bb16fe7abb0b2bb24f7)。

门状态（GateState）操作。

<a id="r_ada2515321ada05932b05ef6cb9a6c6a2"></a>

```c
uint32_t time_interval
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[time_interval](#aa6b2be0014988752e326bdc1fe6ef161)。

时间间隔刻度（ticks），单位为纳秒。

<a id="r_a3d2404175458089c0f915890519d2ae9"></a>

```c
uint16_t row
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[row](#a2c256aa3f65dfa75434752903daa809c)。

门控列表（gate control list）中的行。

<a id="r_a44dca4eeffbb3298046366b41c27c885"></a>

```c
} gate_control
```

相关声明：[gate_control](#a216046de6134584ae05b53609d368bb9)。

门控信息（Gate control information）。

<a id="r_a023f359725578a123ddf3430887b23b6"></a>

```c
uint32_t gate_control_list_len
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[gate_control_list_len](#afc0c26fcdeee1a921a2f549de4d1c33e)。

门控列表中的条目数量。

```c
struct {
```

<a id="r_a373d2df6b2b10d2c79da6be196433e59"></a>

```c
struct net_ptp_extended_time base_time
```

相关声明：[net_ptp_extended_time](../network_core_model_reference/P115_net_ptp_extended_time_结构体.md)、[base_time](#a53646a44e8b0e1f6588c357d49d97693)。

基准时间（Base time）。

<a id="r_ae93682b1c2012849db55991d219711f5"></a>

```c
struct net_ptp_time cycle_time
```

相关声明：[net_ptp_time](../network_core_model_reference/P116_net_ptp_time_结构体.md)、[cycle_time](#ad07589ae6802a9c3c4c3f809427129be)。

周期时间（Cycle time）。

<a id="r_aa27fdf0907f71e85c3c26786923dbf77"></a>

```c
uint32_t extension_time
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[extension_time](#a76220e58aa31ae6cfd92268277716c7a)。

扩展时间（Extension time），单位为纳秒。

<a id="r_a54917e6b9ba848df376d2112795fe68e"></a>

```c
}
```

当 `type` 设为 `ETHERNET_QBV_PARAM_TYPE_TIME` 时，一次性设置所有时间值。

<a id="r_a7da4918afb215f094b0676cef6cb6aa0"></a>

```c
};
```

所选 Qbv 参数类型对应的值。

## 12.2\_详细说明（Detailed Documentation）

<a id="a7da4918afb215f094b0676cef6cb6aa0"></a>

### `[union]`

```c
union { ... } ethernet_qbv_param
```

所选 Qbv 参数类型对应的值。

<a id="a53646a44e8b0e1f6588c357d49d97693"></a>

### `base_time`

```c
struct net_ptp_extended_time ethernet_qbv_param::base_time
```

基准时间（Base time）。

<a id="ad07589ae6802a9c3c4c3f809427129be"></a>

### `cycle_time`

```c
struct net_ptp_time ethernet_qbv_param::cycle_time
```

周期时间（Cycle time）。

<a id="a0742dbe52f01addbb319e2fcb354d064"></a>

### `enabled`

```c
bool ethernet_qbv_param::enabled
```

启用 Qbv 时为 `true`，否则为 `false`。

<a id="a76220e58aa31ae6cfd92268277716c7a"></a>

### `extension_time`

```c
uint32_t ethernet_qbv_param::extension_time
```

扩展时间（Extension time），单位为纳秒。

<a id="a216046de6134584ae05b53609d368bb9"></a>

### `[struct]`

```c
struct { ... } ethernet_qbv_param::gate_control
```

门控信息（Gate control information）。

<a id="afc0c26fcdeee1a921a2f549de4d1c33e"></a>

### `gate_control_list_len`

```c
uint32_t ethernet_qbv_param::gate_control_list_len
```

门控列表中的条目数量。

<a id="a44b6ce52faeae761c5ebe49fad5338cd"></a>

### `gate_status`

```c
bool ethernet_qbv_param::gate_status[NET_TC_TX_COUNT]
```

`true` 表示打开，`false` 表示关闭。

<a id="a8471f7eb20a72bb16fe7abb0b2bb24f7"></a>

### `operation`

```c
enum ethernet_gate_state_operation ethernet_qbv_param::operation
```

门状态（GateState）操作。

<a id="a037492458f47905b894a2269ff7365cd"></a>

### `port_id`

```c
int ethernet_qbv_param::port_id
```

端口 ID。

<a id="a2c256aa3f65dfa75434752903daa809c"></a>

### `row`

```c
uint16_t ethernet_qbv_param::row
```

门控列表（gate control list）中的行。

<a id="a36702c57bea42c37c1341e144ced4f7d"></a>

### `state`

```c
enum ethernet_qbv_state_type ethernet_qbv_param::state
```

这些参数所属的状态：管理态或运行态（Admin/Oper）。

<a id="aa6b2be0014988752e326bdc1fe6ef161"></a>

### `time_interval`

```c
uint32_t ethernet_qbv_param::time_interval
```

时间间隔刻度（ticks），单位为纳秒。

<a id="a2184250d397bd749764adc52ec3a1621"></a>

### `type`

```c
enum ethernet_qbv_param_type ethernet_qbv_param::type
```

Qbv 参数类型。

本数据类型文档由以下文件生成：

- `zephyr/net/ethernet.h`

## 12.3\_原页交叉引用（Cross References）

- [zephyr/net/ethernet.h](https://docs.zephyrproject.org/latest/doxygen/html/ethernet_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_ptp_extended_time](../network_core_model_reference/P115_net_ptp_extended_time_结构体.md)
- [net_ptp_time](../network_core_model_reference/P116_net_ptp_time_结构体.md)
- [ethernet_qbv_param](P012_ethernet_qbv_param_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P011_ethernet_qbu_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P013_ethernet_txtime_param_结构体.md)
