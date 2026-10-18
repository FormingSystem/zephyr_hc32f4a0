---
id: learning.zephyr-docs.api-file-usb-network-reference.page-6
title: zephyr__bluetooth__direction.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_zephyr\_\_bluetooth\_\_direction.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/direction_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stdint.h>
#include <zephyr/bluetooth/bluetooth.h>
#include <zephyr/sys/util_macro.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 6.1\_数据结构（Data Structures）

<a id="r_bt_5Fdf_5Fadv_5Fcte_5Ftx_5Fparam"></a>

```c
struct bt_df_adv_cte_tx_param
```

相关声明：[bt_df_adv_cte_tx_param](../bluetooth_connection_model_reference/P042_bt_df_adv_cte_tx_param_结构体.md)。

无连接传输（Connectionless Transmission）的恒定音调扩展（Constant Tone Extension，CTE）参数。

<a id="r_bt_5Fdf_5Fper_5Fadv_5Fsync_5Fcte_5Frx_5Fparam"></a>

```c
struct bt_df_per_adv_sync_cte_rx_param
```

相关声明：[bt_df_per_adv_sync_cte_rx_param](../bluetooth_connection_model_reference/P047_bt_df_per_adv_sync_cte_rx_param_结构体.md)。

无连接接收（Connectionless Reception）的恒定音调扩展参数。

<a id="r_bt_5Fdf_5Fper_5Fadv_5Fsync_5Fiq_5Fsamples_5Freport"></a>

```c
struct bt_df_per_adv_sync_iq_samples_report
```

相关声明：[bt_df_per_adv_sync_iq_samples_report](../bluetooth_connection_model_reference/P048_bt_df_per_adv_sync_iq_samples_report_结构体.md)。

<a id="r_bt_5Fdf_5Fconn_5Fcte_5Frx_5Fparam"></a>

```c
struct bt_df_conn_cte_rx_param
```

相关声明：[bt_df_conn_cte_rx_param](../bluetooth_connection_model_reference/P044_bt_df_conn_cte_rx_param_结构体.md)。

<a id="r_bt_5Fdf_5Fconn_5Fiq_5Fsamples_5Freport"></a>

```c
struct bt_df_conn_iq_samples_report
```

相关声明：[bt_df_conn_iq_samples_report](../bluetooth_connection_model_reference/P046_bt_df_conn_iq_samples_report_结构体.md)。

<a id="r_bt_5Fdf_5Fconn_5Fcte_5Ftx_5Fparam"></a>

```c
struct bt_df_conn_cte_tx_param
```

相关声明：[bt_df_conn_cte_tx_param](../bluetooth_connection_model_reference/P045_bt_df_conn_cte_tx_param_结构体.md)。

连接模式下传输 CTE 的恒定音调扩展参数。

<a id="r_bt_5Fdf_5Fconn_5Fcte_5Freq_5Fparams"></a>

```c
struct bt_df_conn_cte_req_params
```

相关声明：[bt_df_conn_cte_req_params](../bluetooth_connection_model_reference/P043_bt_df_conn_cte_req_params_结构体.md)。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 6.2\_枚举（Enumerations）

<a id="r_a64bf01dee8bc4bbc62e0dbc356726a05"></a>

```c
enum bt_df_cte_type { BT_DF_CTE_TYPE_NONE = 0 , BT_DF_CTE_TYPE_AOA = (1UL << (0)) , BT_DF_CTE_TYPE_AOD_1US = (1UL << (1)) , BT_DF_CTE_TYPE_AOD_2US = (1UL << (2)) , BT_DF_CTE_TYPE_ALL = (BT_DF_CTE_TYPE_AOA | BT_DF_CTE_TYPE_AOD_1US | BT_DF_CTE_TYPE_AOD_2US) }
```

相关声明：[bt_df_cte_type](#a64bf01dee8bc4bbc62e0dbc356726a05)、[BT_DF_CTE_TYPE_NONE](#a64bf01dee8bc4bbc62e0dbc356726a05a1f24630a9b6afc19e1f671a4b5906dd1)、[BT_DF_CTE_TYPE_AOA](#a64bf01dee8bc4bbc62e0dbc356726a05a6c91466a8e8dfe73665749b263b26207)、[BT_DF_CTE_TYPE_AOD_1US](#a64bf01dee8bc4bbc62e0dbc356726a05a331e4cc8da9f583ad18422cd260018da)、[BT_DF_CTE_TYPE_AOD_2US](#a64bf01dee8bc4bbc62e0dbc356726a05aeeb9304adba4363faaa8e3d299abfdb8)、[BT_DF_CTE_TYPE_ALL](#a64bf01dee8bc4bbc62e0dbc356726a05a3e1c5452412a00c994ad005858e03ac7)。

恒定音调扩展类型（Constant Tone Extension Types，CTE Types）。

<a id="r_a546598ce9a81161ad1ba098a7b1a8df4"></a>

```c
enum bt_df_antenna_switching_slot { BT_DF_ANTENNA_SWITCHING_SLOT_1US = 0x1 , BT_DF_ANTENNA_SWITCHING_SLOT_2US = 0x2 }
```

相关声明：[bt_df_antenna_switching_slot](#a546598ce9a81161ad1ba098a7b1a8df4)、[BT_DF_ANTENNA_SWITCHING_SLOT_1US](#a546598ce9a81161ad1ba098a7b1a8df4a68c89c394d7a1d92560a1e51fa1b069a)、[BT_DF_ANTENNA_SWITCHING_SLOT_2US](#a546598ce9a81161ad1ba098a7b1a8df4ad59a9caab9aeced1f95dd1fe8778fe38)。

允许的天线切换时隙（Antenna Switching Slot）：1 μs 或 2 μs。

<a id="r_ab9acadbaf03dd976a2ee185574effb4c"></a>

```c
enum bt_df_packet_status { BT_DF_CTE_CRC_OK = 0x0 , BT_DF_CTE_CRC_ERR_CTE_BASED_TIME = 0x1 , BT_DF_CTE_CRC_ERR_CTE_BASED_OTHER = 0x2 , BT_DF_CTE_INSUFFICIENT_RESOURCES = 0xFF }
```

相关声明：[bt_df_packet_status](#ab9acadbaf03dd976a2ee185574effb4c)、[BT_DF_CTE_CRC_OK](#ab9acadbaf03dd976a2ee185574effb4ca10328e978a6641f5f787f4f4e9b50d6c)、[BT_DF_CTE_CRC_ERR_CTE_BASED_TIME](#ab9acadbaf03dd976a2ee185574effb4cadf830cbbe3043423eff237b983bf1c92)、[BT_DF_CTE_CRC_ERR_CTE_BASED_OTHER](#ab9acadbaf03dd976a2ee185574effb4cacdc558d9892228b4403cb782ed2260f9)、[BT_DF_CTE_INSUFFICIENT_RESOURCES](#ab9acadbaf03dd976a2ee185574effb4ca70ea13abb5e1626304f8ef4e22564a8b)。

包含所报告 CTE 的协议数据单元（PDU）可能具有的状态。

<a id="r_a53df7da4b178b4a6e4dd68e9266c0771"></a>

```c
enum bt_df_iq_sample { BT_DF_IQ_SAMPLE_8_BITS_INT , BT_DF_IQ_SAMPLE_16_BITS_INT }
```

相关声明：[bt_df_iq_sample](#a53df7da4b178b4a6e4dd68e9266c0771)、[BT_DF_IQ_SAMPLE_8_BITS_INT](#a53df7da4b178b4a6e4dd68e9266c0771a82ee06924dbf1fd3f9c68891b1ccdef4)、[BT_DF_IQ_SAMPLE_16_BITS_INT](#a53df7da4b178b4a6e4dd68e9266c0771a25db2bd4a02678b2ea026ec47b6c2b1b)。

<a id="r_a953634e6a88617a8729541d6b5bd0dd6"></a>

```c
enum bt_df_conn_iq_report_err { BT_DF_IQ_REPORT_ERR_SUCCESS , BT_DF_IQ_REPORT_ERR_NO_CTE , BT_DF_IQ_REPORT_ERR_PEER_REJECTED }
```

相关声明：[bt_df_conn_iq_report_err](#a953634e6a88617a8729541d6b5bd0dd6)、[BT_DF_IQ_REPORT_ERR_SUCCESS](#a953634e6a88617a8729541d6b5bd0dd6acd6f87bd43540cc1b44e5e023a4d0519)、[BT_DF_IQ_REPORT_ERR_NO_CTE](#a953634e6a88617a8729541d6b5bd0dd6a53596e4aa9a96006cee3c899150d7a0e)、[BT_DF_IQ_REPORT_ERR_PEER_REJECTED](#a953634e6a88617a8729541d6b5bd0dd6a7f3f42ede92bafd169620bebddc75512)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 6.3\_函数（Functions）

<a id="r_ae98248377f111deb6aa0565db1d3f690"></a>

```c
int bt_df_set_adv_cte_tx_param (struct bt_le_ext_adv *adv, const struct bt_df_adv_cte_tx_param *params)
```

相关声明：[bt_df_set_adv_cte_tx_param](#ae98248377f111deb6aa0565db1d3f690)、[bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)、[bt_df_adv_cte_tx_param](../bluetooth_connection_model_reference/P042_bt_df_adv_cte_tx_param_结构体.md)。

为周期广播集（Periodic Advertising Set）设置或更新恒定音调扩展（CTE）参数。

<a id="r_ab03ec552192056eb8ddb9aae49029265"></a>

```c
int bt_df_adv_cte_tx_enable (struct bt_le_ext_adv *adv)
```

相关声明：[bt_df_adv_cte_tx_enable](#ab03ec552192056eb8ddb9aae49029265)、[bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)。

为给定广播集（Advertising Set）启用恒定音调扩展（CTE）的发送。

<a id="r_a248cd22ad9afe050e3d535f7124112d9"></a>

```c
int bt_df_adv_cte_tx_disable (struct bt_le_ext_adv *adv)
```

相关声明：[bt_df_adv_cte_tx_disable](#a248cd22ad9afe050e3d535f7124112d9)、[bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)。

为给定广播集（Advertising Set）禁用恒定音调扩展（CTE）的发送。

<a id="r_a26c40ea36de60266f029763551cd9d4e"></a>

```c
int bt_df_per_adv_sync_cte_rx_enable (struct bt_le_per_adv_sync *sync, const struct bt_df_per_adv_sync_cte_rx_param *params)
```

相关声明：[bt_df_per_adv_sync_cte_rx_enable](#a26c40ea36de60266f029763551cd9d4e)、[bt_le_per_adv_sync](../bluetooth_connection_model_reference/P117_bt_le_per_adv_sync_结构体.md)、[bt_df_per_adv_sync_cte_rx_param](../bluetooth_connection_model_reference/P047_bt_df_per_adv_sync_cte_rx_param_结构体.md)。

为给定同步集（Sync Set）启用恒定音调扩展（CTE）的接收与采样。

<a id="r_ac2064484bb3c4ea6ae5eb684f3ace008"></a>

```c
int bt_df_per_adv_sync_cte_rx_disable (struct bt_le_per_adv_sync *sync)
```

相关声明：[bt_df_per_adv_sync_cte_rx_disable](#ac2064484bb3c4ea6ae5eb684f3ace008)、[bt_le_per_adv_sync](../bluetooth_connection_model_reference/P117_bt_le_per_adv_sync_结构体.md)。

为给定同步集（Sync Set）禁用恒定音调扩展（CTE）的接收与采样。

<a id="r_a92d0b485a83a7395b3613b144b6e749f"></a>

```c
int bt_df_conn_cte_rx_enable (struct bt_conn *conn, const struct bt_df_conn_cte_rx_param *params)
```

相关声明：[bt_df_conn_cte_rx_enable](#a92d0b485a83a7395b3613b144b6e749f)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_df_conn_cte_rx_param](../bluetooth_connection_model_reference/P044_bt_df_conn_cte_rx_param_结构体.md)。

为连接对象（Connection Object）启用恒定音调扩展（CTE）的接收与采样。

<a id="r_a861696041baa770ef3968789afd4cbac"></a>

```c
int bt_df_conn_cte_rx_disable (struct bt_conn *conn)
```

相关声明：[bt_df_conn_cte_rx_disable](#a861696041baa770ef3968789afd4cbac)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

为连接对象（Connection Object）禁用恒定音调扩展（CTE）的接收与采样。

<a id="r_aa0eba41c1a810c9592e0097ee4fe7329"></a>

```c
int bt_df_set_conn_cte_tx_param (struct bt_conn *conn, const struct bt_df_conn_cte_tx_param *params)
```

相关声明：[bt_df_set_conn_cte_tx_param](#aa0eba41c1a810c9592e0097ee4fe7329)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_df_conn_cte_tx_param](../bluetooth_connection_model_reference/P045_bt_df_conn_cte_tx_param_结构体.md)。

为连接设置恒定音调扩展（CTE）发送参数。

<a id="r_a84fee1f1ac25af73bb7a8f91ed912c67"></a>

```c
int bt_df_conn_cte_req_enable (struct bt_conn *conn, const struct bt_df_conn_cte_req_params *params)
```

相关声明：[bt_df_conn_cte_req_enable](#a84fee1f1ac25af73bb7a8f91ed912c67)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_df_conn_cte_req_params](../bluetooth_connection_model_reference/P043_bt_df_conn_cte_req_params_结构体.md)。

为连接启用恒定音调扩展请求过程（CTE Request Procedure）。

<a id="r_ade1a048c3fdf11e979fa9a74f33bc375"></a>

```c
int bt_df_conn_cte_req_disable (struct bt_conn *conn)
```

相关声明：[bt_df_conn_cte_req_disable](#ade1a048c3fdf11e979fa9a74f33bc375)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

为连接禁用恒定音调扩展请求过程（CTE Request Procedure）。

<a id="r_a5e4a5168020d488561646beac48916f5"></a>

```c
int bt_df_conn_cte_rsp_enable (struct bt_conn *conn)
```

相关声明：[bt_df_conn_cte_rsp_enable](#a5e4a5168020d488561646beac48916f5)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

为连接启用恒定音调扩展响应过程（CTE Response Procedure）。

<a id="r_a856cfbe26fba92c80f4cf6012a0bbafe"></a>

```c
int bt_df_conn_cte_rsp_disable (struct bt_conn *conn)
```

相关声明：[bt_df_conn_cte_rsp_disable](#a856cfbe26fba92c80f4cf6012a0bbafe)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

为连接禁用恒定音调扩展响应过程（CTE Response Procedure）。

## 6.4\_详细说明（Detailed Documentation）

<a id="a546598ce9a81161ad1ba098a7b1a8df4"></a>

### `bt_df_antenna_switching_slot`

```c
enum bt_df_antenna_switching_slot
```

允许的天线切换时隙（Antenna Switching Slot）：1 μs 或 2 μs。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_DF_ANTENNA_SWITCHING_SLOT_1US` |  |
| `BT_DF_ANTENNA_SWITCHING_SLOT_2US` |  |

<a id="a953634e6a88617a8729541d6b5bd0dd6"></a>

### `bt_df_conn_iq_report_err`

```c
enum bt_df_conn_iq_report_err
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_DF_IQ_REPORT_ERR_SUCCESS` | 成功收到 IQ 采样报告（IQ Samples Report）。 |
| `BT_DF_IQ_REPORT_ERR_NO_CTE` | 收到的 PDU 不含 CTE。报告（Report）中没有有效数据。 |
| `BT_DF_IQ_REPORT_ERR_PEER_REJECTED` | 对端拒绝了 CTE 请求（CTE Request）。报告中没有有效数据。 |

<a id="a64bf01dee8bc4bbc62e0dbc356726a05"></a>

### `bt_df_cte_type`

```c
enum bt_df_cte_type
```

恒定音调扩展类型（Constant Tone Extension Types，CTE Types）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_DF_CTE_TYPE_NONE` | 便捷取值（Convenience Value），用于不允许任何 CTE 类型的情况。 |
| `BT_DF_CTE_TYPE_AOA` | 到达角模式（Angle of Arrival Mode，AoA）。在接收端进行天线切换（Antenna Switching）。 |
| `BT_DF_CTE_TYPE_AOD_1US` | 采用 1 μs 天线切换时隙（Antenna Switching Slot）的出发角模式（Angle of Departure Mode，AoD）。在发送端进行天线切换。 |
| `BT_DF_CTE_TYPE_AOD_2US` | 采用 2 μs 天线切换时隙（Antenna Switching Slot）的出发角模式（Angle of Departure Mode，AoD）。在发送端进行天线切换。 |
| `BT_DF_CTE_TYPE_ALL` | 便捷取值（Convenience Value），将所有可能的 CTE 类型汇集在一个条目中。 |

<a id="a53df7da4b178b4a6e4dd68e9266c0771"></a>

### `bt_df_iq_sample`

```c
enum bt_df_iq_sample
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_DF_IQ_SAMPLE_8_BITS_INT` | 报告的 IQ 样本（IQ Sample）采用 8 位有符号整数格式。大小在蓝牙核心规范（Bluetooth Core）5.3 第 4 卷 E 部分第 7.7.65.21 节和第 7.7.65.22 节中定义。 |
| `BT_DF_IQ_SAMPLE_16_BITS_INT` | 报告的 IQ 样本（IQ Sample）采用 16 位有符号整数格式。这是厂商特定扩展（Vendor-specific Extension）。 |

<a id="ab9acadbaf03dd976a2ee185574effb4c"></a>

### `bt_df_packet_status`

```c
enum bt_df_packet_status
```

包含所报告 CTE 的协议数据单元（PDU）可能具有的状态。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_DF_CTE_CRC_OK` | 收到的 PDU 的循环冗余校验（CRC）正确。 |
| `BT_DF_CTE_CRC_ERR_CTE_BASED_TIME` | 收到的 PDU 的循环冗余校验（CRC）不正确，但无线电外设（Radio Peripheral）能够解析 PDU 的 `CTEInfo` 字段并对 CTE 进行采样。 |
| `BT_DF_CTE_CRC_ERR_CTE_BASED_OTHER` | 收到的 PDU 的循环冗余校验（CRC）不正确，但无线电外设（Radio Peripheral）能够通过其他方式对 CTE 进行采样。 |
| `BT_DF_CTE_INSUFFICIENT_RESOURCES` | 没有足够的资源对 CTE 进行采样（Sampling）。 |

<a id="a248cd22ad9afe050e3d535f7124112d9"></a>

### `bt_df_adv_cte_tx_disable()`

```c
int bt_df_adv_cte_tx_disable ( struct bt_le_ext_adv * adv)
```

为给定广播集（Advertising Set）禁用恒定音调扩展（CTE）的发送。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] adv` | 广播集对象（Advertising Set Object）。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="ab03ec552192056eb8ddb9aae49029265"></a>

### `bt_df_adv_cte_tx_enable()`

```c
int bt_df_adv_cte_tx_enable ( struct bt_le_ext_adv * adv)
```

为给定广播集（Advertising Set）启用恒定音调扩展（CTE）的发送。

只有在设置周期广播参数（`bt_le_per_adv_set_param`）和恒定音调扩展参数（`bt_df_set_adv_cte_tx_param`）之后，才能启用恒定音调扩展（CTE）的发送。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] adv` | 广播集对象（Advertising Set Object）。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="ade1a048c3fdf11e979fa9a74f33bc375"></a>

### `bt_df_conn_cte_req_disable()`

```c
int bt_df_conn_cte_req_disable ( struct bt_conn * conn)
```

为连接禁用恒定音调扩展请求过程（CTE Request Procedure）。

启用 `CONFIG_BT_DF_CONNECTION_CTE_REQ` 时，本函数可用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |

**返回（Returns）**：返回值（Returns）：成功时为零，失败时为其他值。

<a id="a84fee1f1ac25af73bb7a8f91ed912c67"></a>

### `bt_df_conn_cte_req_enable()`

```c
int bt_df_conn_cte_req_enable ( struct bt_conn * conn, const struct bt_df_conn_cte_req_params * params )
```

为连接启用恒定音调扩展请求过程（CTE Request Procedure）。

启用 `CONFIG_BT_DF_CONNECTION_CTE_REQ` 时，本函数可用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `params` | CTE 接收与采样参数（Receive and Sampling Parameters）。 |

**返回（Returns）**：返回值（Returns）：成功时为零，失败时为其他值。

<a id="a856cfbe26fba92c80f4cf6012a0bbafe"></a>

### `bt_df_conn_cte_rsp_disable()`

```c
int bt_df_conn_cte_rsp_disable ( struct bt_conn * conn)
```

为连接禁用恒定音调扩展响应过程（CTE Response Procedure）。

启用 `CONFIG_BT_DF_CONNECTION_CTE_RSP` 时，本函数可用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |

**返回（Returns）**：返回值（Returns）：成功时为零，失败时为其他值。

<a id="a5e4a5168020d488561646beac48916f5"></a>

### `bt_df_conn_cte_rsp_enable()`

```c
int bt_df_conn_cte_rsp_enable ( struct bt_conn * conn)
```

为连接启用恒定音调扩展响应过程（CTE Response Procedure）。

启用 `CONFIG_BT_DF_CONNECTION_CTE_RSP` 时，本函数可用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |

**返回（Returns）**：返回值（Returns）：成功时为零，失败时为其他值。

<a id="a861696041baa770ef3968789afd4cbac"></a>

### `bt_df_conn_cte_rx_disable()`

```c
int bt_df_conn_cte_rx_disable ( struct bt_conn * conn)
```

为连接对象（Connection Object）禁用恒定音调扩展（CTE）的接收与采样。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |

**返回（Returns）**：返回值（Returns）：成功时为零，失败时为其他值。

<a id="a92d0b485a83a7395b3613b144b6e749f"></a>

### `bt_df_conn_cte_rx_enable()`

```c
int bt_df_conn_cte_rx_enable ( struct bt_conn * conn, const struct bt_df_conn_cte_rx_param * params )
```

为连接对象（Connection Object）启用恒定音调扩展（CTE）的接收与采样。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `params` | CTE 接收与采样参数（Receive and Sampling Parameters）。 |

**返回（Returns）**：返回值（Returns）：成功时为零，失败时为其他值。

<a id="ac2064484bb3c4ea6ae5eb684f3ace008"></a>

### `bt_df_per_adv_sync_cte_rx_disable()`

```c
int bt_df_per_adv_sync_cte_rx_disable ( struct bt_le_per_adv_sync * sync)
```

为给定同步集（Sync Set）禁用恒定音调扩展（CTE）的接收与采样。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sync` | 周期广播同步对象（Periodic Advertising Sync Object）。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="a26c40ea36de60266f029763551cd9d4e"></a>

### `bt_df_per_adv_sync_cte_rx_enable()`

```c
int bt_df_per_adv_sync_cte_rx_enable ( struct bt_le_per_adv_sync * sync, const struct bt_df_per_adv_sync_cte_rx_param * params )
```

为给定同步集（Sync Set）启用恒定音调扩展（CTE）的接收与采样。

只有在建立周期广播同步（Periodic Advertising Sync）之后，才能启用恒定音调扩展（CTE）的接收与采样。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sync` | 周期广播同步对象（Periodic Advertising Sync Object）。 |
| `params` | CTE 接收与采样参数（Receive and Sampling Parameters）。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="ae98248377f111deb6aa0565db1d3f690"></a>

### `bt_df_set_adv_cte_tx_param()`

```c
int bt_df_set_adv_cte_tx_param ( struct bt_le_ext_adv * adv, const struct bt_df_adv_cte_tx_param * params )
```

为周期广播集（Periodic Advertising Set）设置或更新恒定音调扩展（CTE）参数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] adv` | 广播集对象（Advertising Set Object）。 |
| `[in] params` | 恒定音调扩展参数（Constant Tone Extension Parameters）。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="aa0eba41c1a810c9592e0097ee4fe7329"></a>

### `bt_df_set_conn_cte_tx_param()`

```c
int bt_df_set_conn_cte_tx_param ( struct bt_conn * conn, const struct bt_df_conn_cte_tx_param * params )
```

为连接设置恒定音调扩展（CTE）发送参数。

启用 `CONFIG_BT_DF_CONNECTION_CTE_TX` 时，本函数可用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `params` | CTE 发送参数（Transmission Parameters）。 |

**说明（Note）**：注意（Note）：如果位字段（Bitfield）中既未设置 `BT_DF_CTE_TYPE_AOD_1US`，也未设置 `BT_DF_CTE_TYPE_AOD_2US`，则忽略 `bt_df_conn_cte_tx_param.num_ant_ids` 和 `bt_df_conn_cte_tx_param.ant_ids` 参数。

**返回（Returns）**：返回值（Returns）：成功时为零，失败时为其他值。


## 6.5\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/bluetooth/bluetooth.h](../api_source_system_reference/P003_bluetooth.h_源码浏览.md)
- [zephyr/sys/util_macro.h](../util_reference/P005_宏工具头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P132_direction.h_源码浏览.md)
- [bt_df_adv_cte_tx_param](../bluetooth_connection_model_reference/P042_bt_df_adv_cte_tx_param_结构体.md)
- [bt_df_per_adv_sync_cte_rx_param](../bluetooth_connection_model_reference/P047_bt_df_per_adv_sync_cte_rx_param_结构体.md)
- [bt_df_per_adv_sync_iq_samples_report](../bluetooth_connection_model_reference/P048_bt_df_per_adv_sync_iq_samples_report_结构体.md)
- [bt_df_conn_cte_rx_param](../bluetooth_connection_model_reference/P044_bt_df_conn_cte_rx_param_结构体.md)
- [bt_df_conn_iq_samples_report](../bluetooth_connection_model_reference/P046_bt_df_conn_iq_samples_report_结构体.md)
- [bt_df_conn_cte_tx_param](../bluetooth_connection_model_reference/P045_bt_df_conn_cte_tx_param_结构体.md)
- [bt_df_conn_cte_req_params](../bluetooth_connection_model_reference/P043_bt_df_conn_cte_req_params_结构体.md)
- [bt_le_ext_adv](../bluetooth_connection_model_reference/P102_bt_le_ext_adv_结构体.md)
- [bt_le_per_adv_sync](../bluetooth_connection_model_reference/P117_bt_le_per_adv_sync_结构体.md)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_le_per_adv_set_param](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaa72029a2759123ec776061d2e80bf3a1)
- [CONFIG_BT_DF_CONNECTION_CTE_REQ](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_DF_CONNECTION_CTE_REQ)
- [CONFIG_BT_DF_CONNECTION_CTE_RSP](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_DF_CONNECTION_CTE_RSP)
- [CONFIG_BT_DF_CONNECTION_CTE_TX](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_DF_CONNECTION_CTE_TX)
- [bt_df_conn_cte_tx_param.num_ant_ids](../bluetooth_connection_model_reference/P045_bt_df_conn_cte_tx_param_结构体.md#ad49bc64170e8ee4741aa01393284e7de)
- [bt_df_conn_cte_tx_param.ant_ids](../bluetooth_connection_model_reference/P045_bt_df_conn_cte_tx_param_结构体.md#a9df1dac6180e77a4c7abc80890346c4a)

<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a546598ce9a81161ad1ba098a7b1a8df4a68c89c394d7a1d92560a1e51fa1b069a"></a>
<a id="a546598ce9a81161ad1ba098a7b1a8df4ad59a9caab9aeced1f95dd1fe8778fe38"></a>
<a id="a953634e6a88617a8729541d6b5bd0dd6acd6f87bd43540cc1b44e5e023a4d0519"></a>
<a id="a953634e6a88617a8729541d6b5bd0dd6a53596e4aa9a96006cee3c899150d7a0e"></a>
<a id="a953634e6a88617a8729541d6b5bd0dd6a7f3f42ede92bafd169620bebddc75512"></a>
<a id="a64bf01dee8bc4bbc62e0dbc356726a05a1f24630a9b6afc19e1f671a4b5906dd1"></a>
<a id="a64bf01dee8bc4bbc62e0dbc356726a05a6c91466a8e8dfe73665749b263b26207"></a>
<a id="a64bf01dee8bc4bbc62e0dbc356726a05a331e4cc8da9f583ad18422cd260018da"></a>
<a id="a64bf01dee8bc4bbc62e0dbc356726a05aeeb9304adba4363faaa8e3d299abfdb8"></a>
<a id="a64bf01dee8bc4bbc62e0dbc356726a05a3e1c5452412a00c994ad005858e03ac7"></a>
<a id="a53df7da4b178b4a6e4dd68e9266c0771a82ee06924dbf1fd3f9c68891b1ccdef4"></a>
<a id="a53df7da4b178b4a6e4dd68e9266c0771a25db2bd4a02678b2ea026ec47b6c2b1b"></a>
<a id="ab9acadbaf03dd976a2ee185574effb4ca10328e978a6641f5f787f4f4e9b50d6c"></a>
<a id="ab9acadbaf03dd976a2ee185574effb4cadf830cbbe3043423eff237b983bf1c92"></a>
<a id="ab9acadbaf03dd976a2ee185574effb4cacdc558d9892228b4403cb782ed2260f9"></a>
<a id="ab9acadbaf03dd976a2ee185574effb4ca70ea13abb5e1626304f8ef4e22564a8b"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P005_zephyr__video__controls.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P007_zephyr__dt-bindings__sensor__tmag5273.h_文件参考.md)
