---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-8
title: bt_conn_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_bt\_conn\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

连接回调结构体（Connection Callback Structure）。

```c
#include <zephyr/bluetooth/conn.h>
```

<a id="details"></a>

连接回调结构（Connection callback structure）。此结构用于跟踪连接状态，通过 `bt_conn_cb_register()` API 注册。如果应用中的不同模块都希望跟踪连接状态，可以注册多个 `bt_conn_cb` 实例。某个实例不关心的回调可以设为 `NULL`，该实例就不会使用此回调。注意（Note）：回调在线程上下文（Thread context）中执行，绝不会从中断服务程序（ISR）调用。回调是在协议栈内部上下文中调用，还是在触发它的 API 调用中同步执行，以及具体使用哪个上下文，都不是 API 契约的一部分，可能随版本变化。有关在回调中阻塞的风险及缓解方法，参见回调执行上下文（Callback execution contexts）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 8.1\_数据成员（Data Fields）

<a id="r_ab3618150bfeea9492095ba27ce978c69"></a>

```c
void(* connected )(struct bt_conn *conn, uint8_t err)
```

相关声明：[connected](#ab3618150bfeea9492095ba27ce978c69)、[bt_conn](P002_bt_conn_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

已建立新连接（New connection）。

<a id="r_a8b8983b5b5b05c9e2dae242485b6c914"></a>

```c
void(* disconnected )(struct bt_conn *conn, uint8_t reason)
```

相关声明：[disconnected](#a8b8983b5b5b05c9e2dae242485b6c914)、[bt_conn](P002_bt_conn_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

连接已断开（Disconnected）。

<a id="r_a1bd8d99988ad0ae3f79aad3d03fcbd8b"></a>

```c
void(* recycled )(void)
```

相关声明：[recycled](#a1bd8d99988ad0ae3f79aad3d03fcbd8b)。

连接对象（Connection object）已归还对象池（Pool）。

<a id="r_a2c52c2e2798062708c373fae9610fadd"></a>

```c
bool(* le_param_req )(struct bt_conn *conn, struct bt_le_conn_param *param)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[le_param_req](#a2c52c2e2798062708c373fae9610fadd)、[bt_conn](P002_bt_conn_结构体.md)、[bt_le_conn_param](P093_bt_le_conn_param_结构体.md)。

低功耗连接参数更新请求（LE connection parameter update request）。

<a id="r_a01582ed3e3801e10c665534eaa991454"></a>

```c
void(* le_param_updated )(struct bt_conn *conn, uint16_t interval, uint16_t latency, uint16_t timeout)
```

相关声明：[le_param_updated](#a01582ed3e3801e10c665534eaa991454)、[bt_conn](P002_bt_conn_结构体.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

低功耗连接参数（LE connection parameters）已更新。

<a id="r_a2179943b5f64302e38c64f075a5b6a9e"></a>

```c
void(* le_param_update_rejected )(struct bt_conn *conn, uint8_t hci_err)
```

相关声明：[le_param_update_rejected](#a2179943b5f64302e38c64f075a5b6a9e)、[bt_conn](P002_bt_conn_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

低功耗连接参数更新（LE connection parameter update）被对等设备拒绝。

<a id="r_aea9b62ab1a1469be97a207a8e07d2f14"></a>

```c
void(* identity_resolved )(struct bt_conn *conn, const bt_addr_le_t *rpa, const bt_addr_le_t *identity)
```

相关声明：[identity_resolved](#aea9b62ab1a1469be97a207a8e07d2f14)、[bt_conn](P002_bt_conn_结构体.md)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)。

已解析远端身份地址（Remote Identity Address）。

<a id="r_ae454d5bc2664e90ba2b1e0c867db374e"></a>

```c
void(* security_changed )(struct bt_conn *conn, bt_security_t level, enum bt_security_err err)
```

相关声明：[security_changed](#ae454d5bc2664e90ba2b1e0c867db374e)、[bt_conn](P002_bt_conn_结构体.md)、[bt_security_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf0c56cd26c4147f6c9f0faa11fa01783)、[bt_security_err](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaa9420ff489fd5857ff076406442679ff)。

连接安全等级（Security level）已变化。

<a id="r_af726f004c06b86f770ece263ed6c9ca4"></a>

```c
void(* remote_info_available )(struct bt_conn *conn, struct bt_conn_remote_info *remote_info)
```

相关声明：[remote_info_available](#af726f004c06b86f770ece263ed6c9ca4)、[bt_conn](P002_bt_conn_结构体.md)、[bt_conn_remote_info](P039_bt_conn_remote_info_结构体.md)。

远端信息获取过程（Remote information procedures）已完成。

<a id="r_abc6a0c4846d52d040b671b4f9f505755"></a>

```c
struct bt_conn_br_cb br
```

相关声明：[bt_conn_br_cb](P005_bt_conn_br_cb_结构体.md)、[br](#abc6a0c4846d52d040b671b4f9f505755)。

基本速率／增强数据率专用回调（BR/EDR specific callbacks）。

<a id="r_ae02a23d823954a747f8f474fb19276d7"></a>

```c
void(* le_phy_updated )(struct bt_conn *conn, struct bt_conn_le_phy_info *param)
```

相关声明：[le_phy_updated](#ae02a23d823954a747f8f474fb19276d7)、[bt_conn](P002_bt_conn_结构体.md)、[bt_conn_le_phy_info](P028_bt_conn_le_phy_info_结构体.md)。

连接的物理层（PHY）已变化。

<a id="r_a1142d1861cc0b0058f68ecf537d0cec3"></a>

```c
void(* le_data_len_updated )(struct bt_conn *conn, struct bt_conn_le_data_len_info *info)
```

相关声明：[le_data_len_updated](#a1142d1861cc0b0058f68ecf537d0cec3)、[bt_conn](P002_bt_conn_结构体.md)、[bt_conn_le_data_len_info](P019_bt_conn_le_data_len_info_结构体.md)。

连接的数据长度参数（Data length parameters）已变化。

<a id="r_a8bde5cae151fa9ba79a7bf91c8901f5f"></a>

```c
void(* cte_report_cb )(struct bt_conn *conn, const struct bt_df_conn_iq_samples_report *iq_report)
```

相关声明：[cte_report_cb](#a8bde5cae151fa9ba79a7bf91c8901f5f)、[bt_conn](P002_bt_conn_结构体.md)、[bt_df_conn_iq_samples_report](P046_bt_df_conn_iq_samples_report_结构体.md)。

接收数据通道协议数据单元（PDU）中的恒定音调扩展（CTE）并采样时，报告所采集同相／正交样本（IQ samples）的回调。

<a id="r_a73d18565f1510a0adaa2b1f4d2278f2f"></a>

```c
void(* tx_power_report )(struct bt_conn *conn, const struct bt_conn_le_tx_power_report *report)
```

相关声明：[tx_power_report](#a73d18565f1510a0adaa2b1f4d2278f2f)、[bt_conn](P002_bt_conn_结构体.md)、[bt_conn_le_tx_power_report](P036_bt_conn_le_tx_power_report_结构体.md)。

低功耗读取远端发射功率等级过程（LE Read Remote Transmit Power Level）已完成，或发生低功耗发射功率报告事件（LE Transmit Power Reporting）。

<a id="r_a274d375b999d46854a691990fb58d90b"></a>

```c
void(* path_loss_threshold_report )(struct bt_conn *conn, const struct bt_conn_le_path_loss_threshold_report *report)
```

相关声明：[path_loss_threshold_report](#a274d375b999d46854a691990fb58d90b)、[bt_conn](P002_bt_conn_结构体.md)、[bt_conn_le_path_loss_threshold_report](P027_bt_conn_le_path_loss_threshold_report_结构体.md)。

低功耗路径损耗阈值事件（LE Path Loss Threshold）。

<a id="r_a32949bf4b5d8cc44f0887c3022df0023"></a>

```c
void(* subrate_changed )(struct bt_conn *conn, const struct bt_conn_le_subrate_changed *params)
```

相关声明：[subrate_changed](#a32949bf4b5d8cc44f0887c3022df0023)、[bt_conn](P002_bt_conn_结构体.md)、[bt_conn_le_subrate_changed](P032_bt_conn_le_subrate_changed_结构体.md)。

低功耗子速率变化事件（LE Subrate Changed）。

<a id="r_a9cbc0e6b91fc2742c59815b676875235"></a>

```c
void(* conn_rate_changed )(struct bt_conn *conn, uint8_t status, const struct bt_conn_le_conn_rate_changed *params)
```

相关声明：[conn_rate_changed](#a9cbc0e6b91fc2742c59815b676875235)、[bt_conn](P002_bt_conn_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_conn_le_conn_rate_changed](P010_bt_conn_le_conn_rate_changed_结构体.md)。

低功耗连接速率变化事件（LE Connection Rate Changed）。

<a id="r_aff02fd2cc1fd90640d0b9ce2e7440202"></a>

```c
void(* read_all_remote_feat_complete )(struct bt_conn *conn, const struct bt_conn_le_read_all_remote_feat_complete *params)
```

相关声明：[read_all_remote_feat_complete](#aff02fd2cc1fd90640d0b9ce2e7440202)、[bt_conn](P002_bt_conn_结构体.md)、[bt_conn_le_read_all_remote_feat_complete](P030_bt_conn_le_read_all_remote_feat_complete_结构体.md)。

读取所有远端特性完成事件（Read All Remote Features Complete）。

<a id="r_a1818aa00a45e807872e732e1fdfddc2c"></a>

```c
void(* frame_space_updated )(struct bt_conn *conn, const struct bt_conn_le_frame_space_updated *params)
```

相关声明：[frame_space_updated](#a1818aa00a45e807872e732e1fdfddc2c)、[bt_conn](P002_bt_conn_结构体.md)、[bt_conn_le_frame_space_updated](P022_bt_conn_le_frame_space_updated_结构体.md)。

帧间隔更新完成事件（Frame Space Update Complete）。

<a id="r_a11b357037d6e3bdf99be7d3649a876d4"></a>

```c
void(* le_cs_read_remote_capabilities_complete )(struct bt_conn *conn, uint8_t status, struct bt_conn_le_cs_capabilities *params)
```

相关声明：[le_cs_read_remote_capabilities_complete](#a11b357037d6e3bdf99be7d3649a876d4)、[bt_conn](P002_bt_conn_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_conn_le_cs_capabilities](P014_bt_conn_le_cs_capabilities_结构体.md)。

低功耗信道探测读取远端支持能力完成事件（LE CS Read Remote Supported Capabilities Complete）。

<a id="r_a016b5f28c5d7187991905abc71d09656"></a>

```c
void(* le_cs_read_remote_fae_table_complete )(struct bt_conn *conn, uint8_t status, struct bt_conn_le_cs_fae_table *params)
```

相关声明：[le_cs_read_remote_fae_table_complete](#a016b5f28c5d7187991905abc71d09656)、[bt_conn](P002_bt_conn_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_conn_le_cs_fae_table](P016_bt_conn_le_cs_fae_table_结构体.md)。

低功耗信道探测读取远端频率驱动误差表完成事件（LE CS Read Remote FAE Table Complete）。

<a id="r_ac20a741bc56068addc9fad442281a493"></a>

```c
void(* le_cs_config_complete )(struct bt_conn *conn, uint8_t status, struct bt_conn_le_cs_config *config)
```

相关声明：[le_cs_config_complete](#ac20a741bc56068addc9fad442281a493)、[bt_conn](P002_bt_conn_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_conn_le_cs_config](P015_bt_conn_le_cs_config_结构体.md)。

已创建低功耗信道探测配置（LE CS Config）。

<a id="r_ae79d3b27e75e4c49575d70ff1a860589"></a>

```c
void(* le_cs_config_removed )(struct bt_conn *conn, uint8_t config_id)
```

相关声明：[le_cs_config_removed](#ae79d3b27e75e4c49575d70ff1a860589)、[bt_conn](P002_bt_conn_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

已移除低功耗信道探测配置（LE CS Config）。

<a id="r_a95af0f47a531b9ec02bb2ec4a26a2017"></a>

```c
void(* le_cs_subevent_data_available )(struct bt_conn *conn, struct bt_conn_le_cs_subevent_result *result)
```

相关声明：[le_cs_subevent_data_available](#a95af0f47a531b9ec02bb2ec4a26a2017)、[bt_conn](P002_bt_conn_结构体.md)、[bt_conn_le_cs_subevent_result](P018_bt_conn_le_cs_subevent_result_结构体.md)。

信道探测过程的子事件结果（CS Subevent Results）已可用。

<a id="r_a0dd4f406a0807014794470b2f33a0cea"></a>

```c
void(* le_cs_security_enable_complete )(struct bt_conn *conn, uint8_t status)
```

相关声明：[le_cs_security_enable_complete](#a0dd4f406a0807014794470b2f33a0cea)、[bt_conn](P002_bt_conn_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

低功耗信道探测安全（LE CS Security）已启用。

<a id="r_a39d8ed2cf68be3b029bd269be71b448a"></a>

```c
void(* le_cs_procedure_enable_complete )(struct bt_conn *conn, uint8_t status, struct bt_conn_le_cs_procedure_enable_complete *params)
```

相关声明：[le_cs_procedure_enable_complete](#a39d8ed2cf68be3b029bd269be71b448a)、[bt_conn](P002_bt_conn_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_conn_le_cs_procedure_enable_complete](P017_bt_conn_le_cs_procedure_enable_complete_结构体.md)。

低功耗信道探测过程（LE CS Procedure）已启用。

## 8.2\_详细说明（Detailed Documentation）

<a id="abc6a0c4846d52d040b671b4f9f505755"></a>

### `br`

```c
struct bt_conn_br_cb bt_conn_cb::br
```

基本速率／增强数据率专用回调（BR/EDR specific callbacks）。

<a id="a9cbc0e6b91fc2742c59815b676875235"></a>

### `conn_rate_changed`

```c
void(* bt_conn_cb::conn_rate_changed) (struct bt_conn *conn, uint8_t status, const struct bt_conn_le_conn_rate_changed *params)
```

低功耗连接速率变化事件（LE Connection Rate Changed）。

此回调通知应用，连接的连接速率参数（Connection rate parameters）可能发生变化，其中包含连接间隔（Connection interval）与子速率（Subrating）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `status` | 低功耗连接速率变化事件（LE Connection Rate Change）的主机控制器接口状态（HCI Status）。可能的状态码：成功（Success，`0x00`）；未知连接标识符（Unknown Connection Identifier，`0x02`）；命令不允许（Command Disallowed，`0x0C`）；不支持的特性或参数值（Unsupported Feature or Parameter Value，`0x11`）；无效 HCI 命令参数（Invalid HCI Command Parameters，`0x12`）；不支持的远端特性（Unsupported Remote Feature，`0x1A`）；不支持的链路层参数值（Unsupported LL Parameter Value，`0x20`）。 |
| `params` | 新的连接速率参数（Connection rate parameters）。若 `status` 不是 `BT_HCI_ERR_SUCCESS`，则此参数为 `NULL`。 |

<a id="ab3618150bfeea9492095ba27ce978c69"></a>

### `connected`

```c
void(* bt_conn_cb::connected) (struct bt_conn *conn, uint8_t err)
```

已建立新连接（New connection）。

此回调通知应用有新连接（New connection）。若 `err` 参数非零，表示连接建立失败。

`err` 可能表示以下任一种情况：

- `BT_HCI_ERR_UNKNOWN_CONN_ID`：由 `bt_conn_le_create` 发起的连接创建已被取消。取消可能由用户通过 `bt_conn_disconnect` 触发，也可能由主机根据 `bt_conn_le_create_param` 的 `timeout` 参数超时触发；该参数默认值为 `CONFIG_BT_CREATE_CONN_TIMEOUT` 秒。
- `BT_HCI_ERR_ADV_TIMEOUT`：由 `bt_le_adv_start` 启动的高占空比定向可连接广播器（High duty cycle directed connectable advertiser）未能在超时内建立连接。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 新的连接对象（Connection object）。 |
| `err` | 主机控制器接口错误（HCI error）。成功时为零，否则为非零。 |

**说明（Note）**：注意（Note）：如果连接通过广播集（Advertising set）建立，则不能直接在此回调中重新启动该广播集。应改用广播集的 `connected` 回调。

<a id="a8bde5cae151fa9ba79a7bf91c8901f5f"></a>

### `cte_report_cb`

```c
void(* bt_conn_cb::cte_report_cb) (struct bt_conn *conn, const struct bt_df_conn_iq_samples_report *iq_report)
```

接收数据通道协议数据单元（PDU）中的恒定音调扩展（CTE）并采样时，报告所采集同相／正交样本（IQ samples）的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection object）。 |
| `iq_report` | 已采集同相／正交样本（IQ samples）的报告数据。 |

<a id="a8b8983b5b5b05c9e2dae242485b6c914"></a>

### `disconnected`

```c
void(* bt_conn_cb::disconnected) (struct bt_conn *conn, uint8_t reason)
```

连接已断开（Disconnected）。

此回调通知应用，连接已断开（Disconnected）。

调用此回调时，协议栈仍持有连接对象（Connection object）的一个引用。如果应用在回调中尝试启动可连接广播器（Connectable advertiser）或创建新连接，可能因没有可用的空闲连接对象而失败。为避免此问题，建议使用 `bt_conn_cb::recycled`；它会在连接对象确实释放后通知应用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `reason` | 表示断开原因的 `BT_HCI_ERR_*` 值。 |

<a id="a1818aa00a45e807872e732e1fdfddc2c"></a>

### `frame_space_updated`

```c
void(* bt_conn_cb::frame_space_updated) (struct bt_conn *conn, const struct bt_conn_le_frame_space_updated *params)
```

帧间隔更新完成事件（Frame Space Update Complete）。

此回调通知应用，连接的帧间隔（Frame space）可能发生变化。若 `status` 不是 `BT_HCI_ERR_SUCCESS`，帧间隔更新参数无效。

此回调可以由调用 `bt_conn_le_frame_space_update` 触发，也可以由控制器自主运行该过程或由对等设备触发。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `params` | 新的帧间隔更新参数（Frame space update parameters）。 |

<a id="aea9b62ab1a1469be97a207a8e07d2f14"></a>

### `identity_resolved`

```c
void(* bt_conn_cb::identity_resolved) (struct bt_conn *conn, const bt_addr_le_t *rpa, const bt_addr_le_t *identity)
```

已解析远端身份地址（Remote Identity Address）。

此回调通知应用，远端身份地址（Identity Address）已解析。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `rpa` | 可解析私有地址（Resolvable Private Address）。 |
| `identity` | 身份地址（Identity Address）。 |

<a id="ac20a741bc56068addc9fad442281a493"></a>

### `le_cs_config_complete`

```c
void(* bt_conn_cb::le_cs_config_complete) (struct bt_conn *conn, uint8_t status, struct bt_conn_le_cs_config *config)
```

已创建低功耗信道探测配置（LE CS Config）。

此回调通知应用，信道探测配置过程（Channel Sounding Configuration procedure）已完成。

若 `status` 为 `BT_HCI_ERR_SUCCESS`，则已创建新的信道探测配置（CS config）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `status` | 完成事件的主机控制器接口状态（HCI status）。 |
| `config` | 成功时为指向信道探测配置（CS configuration）的指针，否则为 `NULL`。 |

<a id="ae79d3b27e75e4c49575d70ff1a860589"></a>

### `le_cs_config_removed`

```c
void(* bt_conn_cb::le_cs_config_removed) (struct bt_conn *conn, uint8_t config_id)
```

已移除低功耗信道探测配置（LE CS Config）。

此回调通知应用，信道探测配置过程（Channel Sounding Configuration procedure）已完成，且已移除一个信道探测配置（CS config）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `config_id` | 被移除的信道探测配置标识符（CS configuration ID）。 |

<a id="a39d8ed2cf68be3b029bd269be71b448a"></a>

### `le_cs_procedure_enable_complete`

```c
void(* bt_conn_cb::le_cs_procedure_enable_complete) (struct bt_conn *conn, uint8_t status, struct bt_conn_le_cs_procedure_enable_complete *params)
```

低功耗信道探测过程（LE CS Procedure）已启用。

此回调通知应用，信道探测过程启用过程（Channel Sounding Procedure Enable procedure）已完成。

若 `status` 为 `BT_HCI_ERR_SUCCESS`，则信道探测过程（CS procedure）已启用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `status` | HCI 状态（Status）。 |
| `params` | 成功时为指向信道探测过程启用参数（CS Procedure Enable parameters）的指针，否则为 `NULL`。 |

<a id="a11b357037d6e3bdf99be7d3649a876d4"></a>

### `le_cs_read_remote_capabilities_complete`

```c
void(* bt_conn_cb::le_cs_read_remote_capabilities_complete) (struct bt_conn *conn, uint8_t status, struct bt_conn_le_cs_capabilities *params)
```

低功耗信道探测读取远端支持能力完成事件（LE CS Read Remote Supported Capabilities Complete）。

此回调通知应用，信道探测能力交换过程（Channel Sounding Capabilities Exchange procedure）已完成。

若 `status` 为 `BT_HCI_ERR_SUCCESS`，则已从对等设备收到远端信道探测能力（Channel sounding capabilities）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `status` | 完成事件的主机控制器接口状态（HCI status）。 |
| `params` | 成功时为指向信道探测能力（CS Capabilities）的指针，否则为 `NULL`。 |

<a id="a016b5f28c5d7187991905abc71d09656"></a>

### `le_cs_read_remote_fae_table_complete`

```c
void(* bt_conn_cb::le_cs_read_remote_fae_table_complete) (struct bt_conn *conn, uint8_t status, struct bt_conn_le_cs_fae_table *params)
```

低功耗信道探测读取远端频率驱动误差表完成事件（LE CS Read Remote FAE Table Complete）。

此回调通知应用，信道探测模式 0 频率驱动误差表请求过程（Channel Sounding Mode-0 FAE Table Request procedure）已完成。

若 `status` 为 `BT_HCI_ERR_SUCCESS`，则已从对等设备收到远端模式 0 频率驱动误差表（Mode-0 FAE Table）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `status` | 完成事件的主机控制器接口状态（HCI status）。 |
| `params` | 成功时为指向频率驱动误差表（FAE Table）的指针，否则为 `NULL`。 |

<a id="a0dd4f406a0807014794470b2f33a0cea"></a>

### `le_cs_security_enable_complete`

```c
void(* bt_conn_cb::le_cs_security_enable_complete) (struct bt_conn *conn, uint8_t status)
```

低功耗信道探测安全（LE CS Security）已启用。

此回调通知应用，信道探测安全启用过程（Channel Sounding Security Enable procedure）已完成。

若 `status` 为 `BT_HCI_ERR_SUCCESS`，则信道探测安全（CS Security）已启用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `status` | 完成事件的主机控制器接口状态（HCI status）。 |

<a id="a95af0f47a531b9ec02bb2ec4a26a2017"></a>

### `le_cs_subevent_data_available`

```c
void(* bt_conn_cb::le_cs_subevent_data_available) (struct bt_conn *conn, struct bt_conn_le_cs_subevent_result *result)
```

信道探测过程的子事件结果（CS Subevent Results）已可用。

此回调通知用户，给定连接对象的信道探测子事件结果（CS subevent results）已可用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection objects）。 |
| `result` | 子事件结果（Subevent results）。 |

<a id="a1142d1861cc0b0058f68ecf537d0cec3"></a>

### `le_data_len_updated`

```c
void(* bt_conn_cb::le_data_len_updated) (struct bt_conn *conn, struct bt_conn_le_data_len_info *info)
```

连接的数据长度参数（Data length parameters）已变化。

此回调通知应用，链路层（Link Layer）的最大载荷长度（Payload length）或传输时间（Transmission time）已变化。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `info` | 连接数据长度信息（Connection data length information）。 |

<a id="a2c52c2e2798062708c373fae9610fadd"></a>

### `le_param_req`

```c
bool(* bt_conn_cb::le_param_req) (struct bt_conn *conn, struct bt_le_conn_param *param)
```

低功耗连接参数更新请求（LE connection parameter update request）。

此回调通知应用，远端设备请求更新连接参数（Connection parameters）。应用返回 `true` 表示接受，返回 `false` 表示拒绝。接受之前，应用也可以调整参数，以更好地满足自身需求。

为简化处理，建议应用只注册一个此类回调。如果注册多个，则需要协调各回调可能不同的要求。每个回调收到的是前一个回调返回的参数，因此不一定与远端最初发送的参数相同。

如果应用未提供此回调，默认接受这些参数（Parameters）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `param` | 建议的连接参数（Proposed connection parameters）。 |

**返回（Returns）**：返回值（Returns）：`true` 表示接受参数，`false` 表示拒绝。

<a id="a2179943b5f64302e38c64f075a5b6a9e"></a>

### `le_param_update_rejected`

```c
void(* bt_conn_cb::le_param_update_rejected) (struct bt_conn *conn, uint8_t hci_err)
```

低功耗连接参数更新（LE connection parameter update）被对等设备拒绝。

此回调通知应用，由 `bt_conn_le_param_update` 发起的连接参数更新请求（Connection parameter update request）被对等设备拒绝。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `hci_err` | 连接参数请求（CPR）被拒绝时的 HCI 错误码 `BT_HCI_ERR_*`；若逻辑链路控制与适配协议回退过程（L2CAP fallback）被拒绝，则为 `BT_CONN_PARAM_REJECT_ERR_L2CAP_CPUP`。 |

**说明（Note）**：注意（Note）：仅在明确收到 HCI 拒绝，或逻辑链路控制与适配协议连接参数更新过程（L2CAP Connection Parameter Update Procedure，CPUP）被拒绝时调用。对于同一事件，此回调与 `le_param_updated` 互斥。如果远端不支持连接参数请求过程（Connection Parameter Request，CPR），且 L2CAP 回退过程也被拒绝，则 `hci_err` 为 `BT_CONN_PARAM_REJECT_ERR_L2CAP_CPUP`。

<a id="a01582ed3e3801e10c665534eaa991454"></a>

### `le_param_updated`

```c
void(* bt_conn_cb::le_param_updated) (struct bt_conn *conn, uint16_t interval, uint16_t latency, uint16_t timeout)
```

低功耗连接参数（LE connection parameters）已更新。

此回调通知应用，低功耗连接（LE connection）的连接参数已更新。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `interval` | 连接间隔（Connection interval）。 |
| `latency` | 连接延迟（Connection latency）。 |
| `timeout` | 连接监督超时（Connection supervision timeout）。 |

<a id="ae02a23d823954a747f8f474fb19276d7"></a>

### `le_phy_updated`

```c
void(* bt_conn_cb::le_phy_updated) (struct bt_conn *conn, struct bt_conn_le_phy_info *param)
```

连接的物理层（PHY）已变化。

此回调通知应用，连接的物理层（PHY）已变化。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `param` | 连接的低功耗物理层信息（LE PHY information）。 |

<a id="a274d375b999d46854a691990fb58d90b"></a>

### `path_loss_threshold_report`

```c
void(* bt_conn_cb::path_loss_threshold_report) (struct bt_conn *conn, const struct bt_conn_le_path_loss_threshold_report *report)
```

低功耗路径损耗阈值事件（LE Path Loss Threshold）。

此回调通知应用，路径损耗（Path loss）已跨越阈值，或者报告使用 `bt_conn_le_set_path_loss_mon_enable` 后的初始路径损耗阈值区域（Threshold zone）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `report` | 路径损耗阈值报告（Path loss threshold report）。 |

<a id="aff02fd2cc1fd90640d0b9ce2e7440202"></a>

### `read_all_remote_feat_complete`

```c
void(* bt_conn_cb::read_all_remote_feat_complete) (struct bt_conn *conn, const struct bt_conn_le_read_all_remote_feat_complete *params)
```

读取所有远端特性完成事件（Read All Remote Features Complete）。

此回调通知应用，连接的读取所有远端特性过程（Read all remote features）已完成。若 `status` 不是 `BT_HCI_ERR_SUCCESS`，则其他参数不会填充。

此回调可以由调用 `bt_conn_le_read_all_remote_features` 触发，也可以由控制器自主执行该过程触发。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `params` | 远端特性（Remote features）。 |

<a id="a1bd8d99988ad0ae3f79aad3d03fcbd8b"></a>

### `recycled`

```c
void(* bt_conn_cb::recycled) (void)
```

连接对象（Connection object）已归还对象池（Pool）。

此回调通知应用，现在可能可以分配一个连接对象（Connection object），但不作保证，遵循先到先得原则。只有通过 `CONFIG_BT_MAX_CONN` 配置数量的连接会触发此回调，即类型为 `BT_CONN_TYPE_LE` 或 `BT_CONN_TYPE_BR` 的连接。

同时存在的最大连接数（Maximum simultaneous connections）由 `CONFIG_BT_MAX_CONN` 配置。

需要开始新连接或启动可连接广播器（Connectable advertiser）时，应监听此事件。它既适用于等待系统完全结束处理旧连接后再启动的情况，也适用于应用因任何原因启动连接失败、正在等待合适重试时机的情况。

<a id="af726f004c06b86f770ece263ed6c9ca4"></a>

### `remote_info_available`

```c
void(* bt_conn_cb::remote_info_available) (struct bt_conn *conn, struct bt_conn_remote_info *remote_info)
```

远端信息获取过程（Remote information procedures）已完成。

此回调通知应用，已从远端对等设备（Remote peer）取得远端信息（Remote information）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `remote_info` | 远端设备的连接信息（Connection information）。 |

<a id="ae454d5bc2664e90ba2b1e0c867db374e"></a>

### `security_changed`

```c
void(* bt_conn_cb::security_changed) (struct bt_conn *conn, bt_security_t level, enum bt_security_err err)
```

连接安全等级（Security level）已变化。

此回调通知应用，连接的安全状态（Security）已变化。

连接的安全等级（Security level）可能提高，也可能保持不变。提高表示已执行配对过程，或已应用前一次连接保存的绑定信息（Bond information）。若安全等级不变，则表示连接的加密密钥（Encryption key）已刷新。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `level` | 连接的新安全等级（Security level）。 |
| `err` | 安全错误（Security error）。成功时为零，否则为非零。 |

<a id="a32949bf4b5d8cc44f0887c3022df0023"></a>

### `subrate_changed`

```c
void(* bt_conn_cb::subrate_changed) (struct bt_conn *conn, const struct bt_conn_le_subrate_changed *params)
```

低功耗子速率变化事件（LE Subrate Changed）。

此回调通知应用，连接的子速率参数（Subrating parameters）可能发生变化。若 `status` 不是 `BT_HCI_ERR_SUCCESS`，连接子速率参数保持不变。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `params` | 新的子速率参数（Subrating parameters）。 |

<a id="a73d18565f1510a0adaa2b1f4d2278f2f"></a>

### `tx_power_report`

```c
void(* bt_conn_cb::tx_power_report) (struct bt_conn *conn, const struct bt_conn_le_tx_power_report *report)
```

低功耗读取远端发射功率等级过程（LE Read Remote Transmit Power Level）已完成，或发生低功耗发射功率报告事件（LE Transmit Power Reporting）。

此回调通知应用，已从对等设备读取远端发射功率等级（Transmit power level）；或者在使用 `bt_conn_le_set_tx_power_report_enable` 为相应一侧启用发射功率报告之后，本地或远端控制器的发射功率等级已变化。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 连接对象（Connection Object）。 |
| `report` | 发射功率报告（Transmit power report）。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/conn.h`

## 8.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html)
- [bt_conn](P002_bt_conn_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [bt_le_conn_param](P093_bt_le_conn_param_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [bt_security_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf0c56cd26c4147f6c9f0faa11fa01783)
- [bt_security_err](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaa9420ff489fd5857ff076406442679ff)
- [bt_conn_remote_info](P039_bt_conn_remote_info_结构体.md)
- [bt_conn_br_cb](P005_bt_conn_br_cb_结构体.md)
- [bt_conn_le_phy_info](P028_bt_conn_le_phy_info_结构体.md)
- [bt_conn_le_data_len_info](P019_bt_conn_le_data_len_info_结构体.md)
- [bt_df_conn_iq_samples_report](P046_bt_df_conn_iq_samples_report_结构体.md)
- [bt_conn_le_tx_power_report](P036_bt_conn_le_tx_power_report_结构体.md)
- [bt_conn_le_path_loss_threshold_report](P027_bt_conn_le_path_loss_threshold_report_结构体.md)
- [bt_conn_le_subrate_changed](P032_bt_conn_le_subrate_changed_结构体.md)
- [bt_conn_le_conn_rate_changed](P010_bt_conn_le_conn_rate_changed_结构体.md)
- [bt_conn_le_read_all_remote_feat_complete](P030_bt_conn_le_read_all_remote_feat_complete_结构体.md)
- [bt_conn_le_frame_space_updated](P022_bt_conn_le_frame_space_updated_结构体.md)
- [bt_conn_le_cs_capabilities](P014_bt_conn_le_cs_capabilities_结构体.md)
- [bt_conn_le_cs_fae_table](P016_bt_conn_le_cs_fae_table_结构体.md)
- [bt_conn_le_cs_config](P015_bt_conn_le_cs_config_结构体.md)
- [bt_conn_le_cs_subevent_result](P018_bt_conn_le_cs_subevent_result_结构体.md)
- [bt_conn_le_cs_procedure_enable_complete](P017_bt_conn_le_cs_procedure_enable_complete_结构体.md)
- [bt_conn_cb_register()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaa9b79cd44734c1e560d6f30509be4d0b)
- [bt_conn_cb](P008_bt_conn_cb_结构体.md)
- [回调执行上下文（Callback execution contexts）](../bluetooth/P004_低功耗蓝牙主机.md#bluetooth-callback-contexts)
- [BT_HCI_ERR_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a27c890210eded48f159073cccef8582a)
- [BT_HCI_ERR_UNKNOWN_CONN_ID](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#afd68afeb0296e3af363d7d60eaf4e9a1)
- [bt_conn_le_create](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga8d66f3e0262a51279e9fa8b3139252e6)
- [bt_conn_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga14e7c852b0271781594e742ae509c5d3)
- [bt_conn_le_create_param](P012_bt_conn_le_create_param_结构体.md)
- [CONFIG_BT_CREATE_CONN_TIMEOUT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CREATE_CONN_TIMEOUT)
- [bt_le_adv_start](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gad2e3caef88d52d720e8e4d21df767b02)
- [bt_conn_le_frame_space_update](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gab734fbc307eff3c5bddf7c5e6ddd341b)
- [bt_conn_le_param_update](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gab44a964725f54ed2d37de17c6e2fd3eb)
- [bt_conn_le_set_path_loss_mon_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga90ae27bcc6f71f32be56efe8ecbc165d)
- [bt_conn_le_read_all_remote_features](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gac0dbbdb95ef868f35006622932dc8901)
- [CONFIG_BT_MAX_CONN](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MAX_CONN)
- [BT_CONN_TYPE_LE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggab8dde20ae75b51f1e28dbeed06001f20a052db9b0af1695a63097781c2179acb2)
- [BT_CONN_TYPE_BR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ggab8dde20ae75b51f1e28dbeed06001f20a57856dfae9c62f4bd92bd66c76421cb6)
- [bt_conn_le_set_tx_power_report_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaa1f38911acee0534a8a6e414018c6fb6)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P007_bt_conn_br_remote_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P009_bt_conn_info_结构体.md)
