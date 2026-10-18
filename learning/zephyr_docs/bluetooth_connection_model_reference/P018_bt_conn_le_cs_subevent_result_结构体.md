---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-18
title: bt_conn_le_cs_subevent_result_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__cs__subevent__result.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_bt\_conn\_le\_cs\_subevent\_result\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__cs__subevent__result.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

支持 CS 的 LE 连接的子事件（Subevent）数据。

```c
#include <zephyr/bluetooth/conn.h>
```

<a id="details"></a>

支持 CS 的 LE 连接的子事件（Subevent）数据。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 18.1\_数据成员（Data Fields）

```c
struct {
```

<a id="r_a61b4cccbfa699ee531a3e1defba51b52"></a>

```c
uint8_t config_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[config_id](#aa4c770ab2db8d4ab665ad50f7edd5bfa)。

信道探测配置标识符（CS configuration identifier）。

<a id="r_a4e77f673d958f3b88b9818b3477821b7"></a>

```c
uint16_t start_acl_conn_event
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[start_acl_conn_event](#a7706d0dfd7246d4cf193a8a9e7b6305d)。

起始异步面向连接链路连接事件计数器（ACL connection event counter）。

<a id="r_a5ffab1254bdac8d8b07b7444075d330b"></a>

```c
uint16_t procedure_counter
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[procedure_counter](#a0f8fc918f8eb31c47acf51885c7add08)。

与这些结果关联的信道探测过程计数（CS procedure count）。

<a id="r_a1ac2306f4c471da2ffbc6bd119bde8d0"></a>

```c
uint16_t frequency_compensation
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[frequency_compensation](#a967d37f37d0e1596984fdda34609a3b3)。

频率补偿值（Frequency compensation value），单位为 0.01 ppm。

<a id="r_a8bffa8da8f8c453ad0d37336b274a2c5"></a>

```c
int8_t reference_power_level
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[reference_power_level](#acbfc5e80a2fb82072d9376e996f7969f)。

参考功率等级（Reference power level），单位为 dBm。

<a id="r_ad09b12c19d4d2119425939d08578b7ff"></a>

```c
enum bt_conn_le_cs_procedure_done_status procedure_done_status
```

相关声明：[bt_conn_le_cs_procedure_done_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga9a1dc2010c5237466de87160944630d3)、[procedure_done_status](#adf60893d9229003d1eefc552a4957b65)。

过程状态（Procedure status）。

<a id="r_a54836644a8a6bded08c41cfada3608f6"></a>

```c
enum bt_conn_le_cs_subevent_done_status subevent_done_status
```

相关声明：[bt_conn_le_cs_subevent_done_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga8e54a191b889b1d5ed3e1fbb648d9bc7)、[subevent_done_status](#a45b22c6c2252e2afa28ee8b1bfed3ecf)。

子事件状态（Subevent status）。

<a id="r_af3dfde3d4a236568e954aa3bdaac2ca1"></a>

```c
enum bt_conn_le_cs_procedure_abort_reason procedure_abort_reason
```

相关声明：[bt_conn_le_cs_procedure_abort_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga3196a0eb1c7497e93d7c646713d2fc79)、[procedure_abort_reason](#a778c89f57ef50f612654243ba673ba3f)。

中止原因（Abort reason）。

<a id="r_a5009cbefc21176cd247ce60974bc38d8"></a>

```c
enum bt_conn_le_cs_subevent_abort_reason subevent_abort_reason
```

相关声明：[bt_conn_le_cs_subevent_abort_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga6394906c6da40c9bebfaeb05de9fd5be)、[subevent_abort_reason](#aef5ba53497c4d1576c9ecec1b5dea289)。

中止原因（Abort reason）。

<a id="r_ac5a4918d97959e532c78dc140a156711"></a>

```c
uint8_t num_antenna_paths
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_antenna_paths](#a3597697ae4acdd8f7c009bececab6a65)。

相位测量阶段（Phase measurement stage）使用的天线路径数量。

<a id="r_af551b76394472983090cf6a91c047fc5"></a>

```c
uint8_t num_steps_reported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_steps_reported](#a3bffc0935a5410d75d0050337e4fad27)。

子事件中的信道探测步骤数量（CS steps）。

<a id="r_a0b198d210246e0245e6277e2ba51eafc"></a>

```c
uint8_t abort_step
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[abort_step](#a9bfcc6dcaa191c7f56958ef88926b51e)。

子事件中止所在的步骤编号（Step number）。如果 `subevent_done_status` 为 `BT_CONN_LE_CS_SUBEVENT_COMPLETE`，则 `abort_step` 不使用，并设置为 `255`。

<a id="r_a1a90563a8c93f9b309e88fd771a7cec4"></a>

```c
} header
```

相关声明：[header](#a1a90563a8c93f9b309e88fd771a7cec4)。

<a id="r_a6948c4a8c5882cb1d1b04a2b390fda8c"></a>

```c
struct net_buf_simple * step_data_buf
```

相关声明：[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[step_data_buf](#a6948c4a8c5882cb1d1b04a2b390fda8c)。

指向包含步骤数据（Step data）的缓冲区的指针。

## 18.2\_详细说明（Detailed Documentation）

<a id="a9bfcc6dcaa191c7f56958ef88926b51e"></a>

### `abort_step`

```c
uint8_t bt_conn_le_cs_subevent_result::abort_step
```

子事件中止所在的步骤编号（Step number）。如果 `subevent_done_status` 为 `BT_CONN_LE_CS_SUBEVENT_COMPLETE`，则 `abort_step` 不使用，并设置为 `255`。

<a id="aa4c770ab2db8d4ab665ad50f7edd5bfa"></a>

### `config_id`

```c
uint8_t bt_conn_le_cs_subevent_result::config_id
```

信道探测配置标识符（CS configuration identifier）。

范围（Range）：0–3。

如果这些结果由信道探测测试（CS Test）生成，此值将设为 `0`，且无实际意义。

<a id="a967d37f37d0e1596984fdda34609a3b3"></a>

### `frequency_compensation`

```c
uint16_t bt_conn_le_cs_subevent_result::frequency_compensation
```

频率补偿值（Frequency compensation value），单位为 0.01 ppm。

这是一个 15 位有符号整数（Signed integer），范围为 [-100, 100] ppm。

值 `BT_HCI_LE_CS_SUBEVENT_RESULT_FREQ_COMPENSATION_NOT_AVAILABLE` 表示角色不是发起方（Initiator），或者频率补偿值不可用。

<a id="a1a90563a8c93f9b309e88fd771a7cec4"></a>

### `[struct]`

```c
struct { ... } bt_conn_le_cs_subevent_result::header
```

<a id="a3597697ae4acdd8f7c009bececab6a65"></a>

### `num_antenna_paths`

```c
uint8_t bt_conn_le_cs_subevent_result::num_antenna_paths
```

相位测量阶段（Phase measurement stage）使用的天线路径数量。

<a id="a3bffc0935a5410d75d0050337e4fad27"></a>

### `num_steps_reported`

```c
uint8_t bt_conn_le_cs_subevent_result::num_steps_reported
```

子事件中的信道探测步骤数量（CS steps）。

<a id="a778c89f57ef50f612654243ba673ba3f"></a>

### `procedure_abort_reason`

```c
enum bt_conn_le_cs_procedure_abort_reason bt_conn_le_cs_subevent_result::procedure_abort_reason
```

中止原因（Abort reason）。

若过程状态（Procedure status）为 `BT_CONN_LE_CS_PROCEDURE_ABORTED`，此字段指定中止原因。

<a id="a0f8fc918f8eb31c47acf51885c7add08"></a>

### `procedure_counter`

```c
uint16_t bt_conn_le_cs_subevent_result::procedure_counter
```

与这些结果关联的信道探测过程计数（CS procedure count）。

这是自信道探测安全启动过程（Channel Sounding Security Start procedure）完成以来的信道探测过程计数（CS procedure count）。

<a id="adf60893d9229003d1eefc552a4957b65"></a>

### `procedure_done_status`

```c
enum bt_conn_le_cs_procedure_done_status bt_conn_le_cs_subevent_result::procedure_done_status
```

过程状态（Procedure status）。

<a id="acbfc5e80a2fb82072d9376e996f7969f"></a>

### `reference_power_level`

```c
int8_t bt_conn_le_cs_subevent_result::reference_power_level
```

参考功率等级（Reference power level），单位为 dBm。

范围（Range）：-127–20。

值 `BT_HCI_LE_CS_REF_POWER_LEVEL_UNAVAILABLE` 表示子事件期间参考功率等级（Reference power level）不可用。

<a id="a7706d0dfd7246d4cf193a8a9e7b6305d"></a>

### `start_acl_conn_event`

```c
uint16_t bt_conn_le_cs_subevent_result::start_acl_conn_event
```

起始异步面向连接链路连接事件计数器（ACL connection event counter）。

如果这些结果由信道探测测试（CS Test）生成，此值将设为 `0`，且无实际意义。

<a id="a6948c4a8c5882cb1d1b04a2b390fda8c"></a>

### `step_data_buf`

```c
struct net_buf_simple* bt_conn_le_cs_subevent_result::step_data_buf
```

指向包含步骤数据（Step data）的缓冲区的指针。

`num_steps_reported` 为 `0` 时，此项为 `NULL`。

<a id="aef5ba53497c4d1576c9ecec1b5dea289"></a>

### `subevent_abort_reason`

```c
enum bt_conn_le_cs_subevent_abort_reason bt_conn_le_cs_subevent_result::subevent_abort_reason
```

中止原因（Abort reason）。

若子事件状态（Subevent status）为 `BT_CONN_LE_CS_SUBEVENT_ABORTED`，此字段指定中止原因。

<a id="a45b22c6c2252e2afa28ee8b1bfed3ecf"></a>

### `subevent_done_status`

```c
enum bt_conn_le_cs_subevent_done_status bt_conn_le_cs_subevent_result::subevent_done_status
```

子事件状态（Subevent status）。

对于已中止的子事件（Aborted subevents），此值设为 `BT_CONN_LE_CS_SUBEVENT_ABORTED`，`abort_step` 包含发生中止的步骤编号。请看以下示例：

示例参数（Example）：`subevent_done_status = BT_CONN_LE_CS_SUBEVENT_ABORTED`，`num_steps_reported = 160`，`abort_step = 100`。

这表示步骤 0–99 已完成，步骤 100–159 已中止（Aborted）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/conn.h`

## 18.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [bt_conn_le_cs_procedure_done_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga9a1dc2010c5237466de87160944630d3)
- [bt_conn_le_cs_subevent_done_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga8e54a191b889b1d5ed3e1fbb648d9bc7)
- [bt_conn_le_cs_procedure_abort_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga3196a0eb1c7497e93d7c646713d2fc79)
- [bt_conn_le_cs_subevent_abort_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga6394906c6da40c9bebfaeb05de9fd5be)
- [BT_CONN_LE_CS_SUBEVENT_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga8e54a191b889b1d5ed3e1fbb648d9bc7a900282c089ca30323171da1a0e0e0146)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [BT_HCI_LE_CS_SUBEVENT_RESULT_FREQ_COMPENSATION_NOT_AVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a385a401b373522160b1832b66838e02d)
- [BT_CONN_LE_CS_PROCEDURE_ABORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga9a1dc2010c5237466de87160944630d3a0ff236987e96f368c09944a9074f8f7b)
- [BT_HCI_LE_CS_REF_POWER_LEVEL_UNAVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#aa4345ca4225d3958968131ba7a5ff950)
- [BT_CONN_LE_CS_SUBEVENT_ABORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gga8e54a191b889b1d5ed3e1fbb648d9bc7a5943689e3233bc87054dbd9f54042202)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P017_bt_conn_le_cs_procedure_enable_complete_结构体.md) · [返回大纲](大纲.md) · [下一章](P019_bt_conn_le_data_len_info_结构体.md)
