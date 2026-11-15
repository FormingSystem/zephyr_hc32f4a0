---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-118
title: bt_le_per_adv_sync_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__per__adv__sync__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第118章\_bt\_le\_per\_adv\_sync\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__per__adv__sync__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

周期广播同步（Periodic Advertising Sync）事件的回调结构。

```c
#include <zephyr/bluetooth/bluetooth.h>
```

<a id="details"></a>

周期广播同步事件回调结构（Periodic advertising sync event callback struct）。定义针对不同周期广播同步事件调用的回调函数，包括成功建立同步、终止同步、接收数据、状态变化、广播等时组信息报告（BIG info reports）以及周期广播的同相／正交样本（IQ samples）。注意（Note）：用于 `bt_le_per_adv_sync_cb_register` 函数。回调在线程上下文（Thread context）中执行，绝不会从中断服务程序（ISR）调用。回调是在协议栈内部上下文中调用，还是在触发它的 API 调用中同步执行，以及具体使用哪个上下文，都不是 API 契约的一部分，可能随版本变化。有关在回调中阻塞的风险及缓解方法，参见回调执行上下文（Callback execution contexts）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 118.1\_数据成员（Data Fields）

<a id="r_a815be4343ab589df433a551663c5f4a1"></a>

```c
void(* synced )(struct bt_le_per_adv_sync *sync, struct bt_le_per_adv_sync_synced_info *info)
```

相关声明：[synced](#a815be4343ab589df433a551663c5f4a1)、[bt_le_per_adv_sync](P117_bt_le_per_adv_sync_结构体.md)、[bt_le_per_adv_sync_synced_info](P124_bt_le_per_adv_sync_synced_info_结构体.md)。

周期广播（Periodic advertising）已成功同步。

<a id="r_acbd565a39918e5dfe7603a020e73daec"></a>

```c
void(* term )(struct bt_le_per_adv_sync *sync, const struct bt_le_per_adv_sync_term_info *info)
```

相关声明：[term](#acbd565a39918e5dfe7603a020e73daec)、[bt_le_per_adv_sync](P117_bt_le_per_adv_sync_结构体.md)、[bt_le_per_adv_sync_term_info](P125_bt_le_per_adv_sync_term_info_结构体.md)。

周期广播同步（Periodic advertising sync）已终止。

<a id="r_a5576248e2eaef2afebe606e05e55f05f"></a>

```c
void(* recv )(struct bt_le_per_adv_sync *sync, const struct bt_le_per_adv_sync_recv_info *info, struct net_buf_simple *buf)
```

相关声明：[recv](#a5576248e2eaef2afebe606e05e55f05f)、[bt_le_per_adv_sync](P117_bt_le_per_adv_sync_结构体.md)、[bt_le_per_adv_sync_recv_info](P121_bt_le_per_adv_sync_recv_info_结构体.md)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

已收到周期广播数据（Periodic advertising data）。

<a id="r_a656b4802f79d4a472c2367ade144d72e"></a>

```c
void(* state_changed )(struct bt_le_per_adv_sync *sync, const struct bt_le_per_adv_sync_state_info *info)
```

相关声明：[state_changed](#a656b4802f79d4a472c2367ade144d72e)、[bt_le_per_adv_sync](P117_bt_le_per_adv_sync_结构体.md)、[bt_le_per_adv_sync_state_info](P122_bt_le_per_adv_sync_state_info_结构体.md)。

周期广播同步状态（Periodic advertising sync state）已变化。

<a id="r_aa44efa17bc28da1952785063a9baf6a9"></a>

```c
void(* biginfo )(struct bt_le_per_adv_sync *sync, const struct bt_iso_biginfo *biginfo)
```

相关声明：[biginfo](#aa44efa17bc28da1952785063a9baf6a9)、[bt_le_per_adv_sync](P117_bt_le_per_adv_sync_结构体.md)、[bt_iso_biginfo](P075_bt_iso_biginfo_结构体.md)。

已收到广播等时组信息广播报告（BIGInfo advertising report）。

<a id="r_ad2dc168696fbd22f7e3a089ac56f62d7"></a>

```c
void(* cte_report_cb )(struct bt_le_per_adv_sync *sync, struct bt_df_per_adv_sync_iq_samples_report const *info)
```

相关声明：[cte_report_cb](#ad2dc168696fbd22f7e3a089ac56f62d7)、[bt_le_per_adv_sync](P117_bt_le_per_adv_sync_结构体.md)、[bt_df_per_adv_sync_iq_samples_report](P048_bt_df_per_adv_sync_iq_samples_report_结构体.md)。

接收周期广播协议数据单元（PDU）中的恒定音调扩展（CTE）并采样时，报告所采集同相／正交样本（IQ samples）的回调。

<a id="r_a1977d27941063773c953a5f1dfa9ca76"></a>

```c
sys_snode_t node
```

相关声明：[sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)、[node](#a1977d27941063773c953a5f1dfa9ca76)。

## 118.2\_详细说明（Detailed Documentation）

<a id="aa44efa17bc28da1952785063a9baf6a9"></a>

### `biginfo`

```c
void(* bt_le_per_adv_sync_cb::biginfo) (struct bt_le_per_adv_sync *sync, const struct bt_iso_biginfo *biginfo)
```

已收到广播等时组信息广播报告（BIGInfo advertising report）。

此回调向应用通知广播等时组信息广播报告（BIGInfo advertising report）。当广播器在一个广播等时组（BIG）中广播等时流时，会收到此报告。更多信息参见 `iso.h`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sync` | 广播集对象（Advertising set object）。 |
| `biginfo` | BIGInfo 报告。 |

<a id="ad2dc168696fbd22f7e3a089ac56f62d7"></a>

### `cte_report_cb`

```c
void(* bt_le_per_adv_sync_cb::cte_report_cb) (struct bt_le_per_adv_sync *sync, struct bt_df_per_adv_sync_iq_samples_report const *info)
```

接收周期广播协议数据单元（PDU）中的恒定音调扩展（CTE）并采样时，报告所采集同相／正交样本（IQ samples）的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sync` | 周期广播同步对象（Periodic advertising sync object）。 |
| `info` | 同步事件信息（Sync event information）。 |

<a id="a1977d27941063773c953a5f1dfa9ca76"></a>

### `node`

```c
sys_snode_t bt_le_per_adv_sync_cb::node
```

<a id="a5576248e2eaef2afebe606e05e55f05f"></a>

### `recv`

```c
void(* bt_le_per_adv_sync_cb::recv) (struct bt_le_per_adv_sync *sync, const struct bt_le_per_adv_sync_recv_info *info, struct net_buf_simple *buf)
```

已收到周期广播数据（Periodic advertising data）。

此回调向应用通知周期广播报告（Periodic advertising report）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sync` | 广播集对象（Advertising set object）。 |
| `info` | 周期广播事件信息（Periodic advertising event information）。 |
| `buf` | 包含周期广播数据（Periodic advertising data）的缓冲区。若控制器未能接收子事件指示（Subevent indication），则为 `NULL`；仅在启用 `CONFIG_BT_PER_ADV_SYNC_RSP` 时会发生这种情况。 |

<a id="a656b4802f79d4a472c2367ade144d72e"></a>

### `state_changed`

```c
void(* bt_le_per_adv_sync_cb::state_changed) (struct bt_le_per_adv_sync *sync, const struct bt_le_per_adv_sync_state_info *info)
```

周期广播同步状态（Periodic advertising sync state）已变化。

此回调通知应用同步状态（Sync state）的变化。同步初始化和终止由各自独立的回调处理，不在此处通知。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sync` | 周期广播同步对象（Periodic advertising sync object）。 |
| `info` | 状态变化信息（State change information）。 |

<a id="a815be4343ab589df433a551663c5f4a1"></a>

### `synced`

```c
void(* bt_le_per_adv_sync_cb::synced) (struct bt_le_per_adv_sync *sync, struct bt_le_per_adv_sync_synced_info *info)
```

周期广播（Periodic advertising）已成功同步。

此回调通知应用，周期广播集（Periodic advertising set）已成功同步，现将开始接收周期广播报告。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sync` | 周期广播同步对象（Periodic advertising sync object）。 |
| `info` | 同步事件信息（Sync event information）。 |

<a id="acbd565a39918e5dfe7603a020e73daec"></a>

### `term`

```c
void(* bt_le_per_adv_sync_cb::term) (struct bt_le_per_adv_sync *sync, const struct bt_le_per_adv_sync_term_info *info)
```

周期广播同步（Periodic advertising sync）已终止。

此回调通知应用，周期广播同步（Periodic advertising sync）已终止，原因可能是本地请求、远端请求，或数据缺失，例如超出范围或失去同步。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sync` | 周期广播同步对象（Periodic advertising sync object）。 |
| `info` | 终止事件信息（Termination event information）。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/bluetooth.h`

## 118.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h_source.html)
- [bt_le_per_adv_sync](P117_bt_le_per_adv_sync_结构体.md)
- [bt_le_per_adv_sync_synced_info](P124_bt_le_per_adv_sync_synced_info_结构体.md)
- [bt_le_per_adv_sync_term_info](P125_bt_le_per_adv_sync_term_info_结构体.md)
- [bt_le_per_adv_sync_recv_info](P121_bt_le_per_adv_sync_recv_info_结构体.md)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [bt_le_per_adv_sync_state_info](P122_bt_le_per_adv_sync_state_info_结构体.md)
- [bt_iso_biginfo](P075_bt_iso_biginfo_结构体.md)
- [bt_df_per_adv_sync_iq_samples_report](P048_bt_df_per_adv_sync_iq_samples_report_结构体.md)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [bt_le_per_adv_sync_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga4ee87bbf79e6ac844d14c3dafb2dadf4)
- [回调执行上下文（Callback execution contexts）](../bluetooth/P004_低功耗蓝牙主机.md#bluetooth-callback-contexts)
- [iso.h](https://docs.zephyrproject.org/latest/doxygen/html/iso_8h.html)
- [CONFIG_BT_PER_ADV_SYNC_RSP](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PER_ADV_SYNC_RSP)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P117_bt_le_per_adv_sync_结构体.md) · [返回大纲](大纲.md) · [下一章](P119_bt_le_per_adv_sync_info_结构体.md)
