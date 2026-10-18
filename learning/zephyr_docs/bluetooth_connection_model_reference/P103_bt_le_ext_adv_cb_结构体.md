---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-103
title: bt_le_ext_adv_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__ext__adv__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第103章\_bt\_le\_ext\_adv\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__ext__adv__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于通知广播者（Advertiser）活动的回调结构。

```c
#include <zephyr/bluetooth/bluetooth.h>
```

<a id="details"></a>

用于通知广播器活动的回调结构（Advertiser activity callback struct）。`bt_le_ext_adv_cb` 结构包含针对广播集（Advertising set）相关事件调用的回调函数，事件包括：广播数据发送完成、接受新连接、发送扫描响应数据；如果启用了隐私（Privacy），还包括广播集有效期到期；如果启用了带响应的周期广播（Periodic Advertising with Response，PAwR），还包括已准备好发送一个或多个 PAwR 子事件，即低功耗周期广播子事件数据请求事件（LE Periodic Advertising Subevent Data Request），以及已收到同步设备对周期广播子事件指示的响应，即低功耗周期广播响应报告事件（LE Periodic Advertising Response Report）。注意（Note）：在广播集的整个生命周期内，必须指向有效内存。此结构用于 `bt_le_ext_adv_create`。回调在线程上下文（Thread context）中执行，绝不会从中断服务程序（ISR）调用。回调是在协议栈内部上下文中调用，还是在触发它的 API 调用中同步执行，以及具体使用哪个上下文，都不是 API 契约的一部分，可能随版本变化。有关在回调中阻塞的风险及缓解方法，参见回调执行上下文（Callback execution contexts）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 103.1\_数据成员（Data Fields）

<a id="r_a85b8887c9ef443d18b71e9561e7dde60"></a>

```c
void(* sent )(struct bt_le_ext_adv *adv, struct bt_le_ext_adv_sent_info *info)
```

相关声明：[sent](#a85b8887c9ef443d18b71e9561e7dde60)、[bt_le_ext_adv](P102_bt_le_ext_adv_结构体.md)、[bt_le_ext_adv_sent_info](P107_bt_le_ext_adv_sent_info_结构体.md)。

广播集（Advertising set）达到限制后已禁用。

<a id="r_a7aad0fbd8e531e70f661500c338d870e"></a>

```c
void(* connected )(struct bt_le_ext_adv *adv, struct bt_le_ext_adv_connected_info *info)
```

相关声明：[connected](#a7aad0fbd8e531e70f661500c338d870e)、[bt_le_ext_adv](P102_bt_le_ext_adv_结构体.md)、[bt_le_ext_adv_connected_info](P104_bt_le_ext_adv_connected_info_结构体.md)。

广播集（Advertising set）已接受新连接。

<a id="r_a277dc3269741d40b644ae3c777198fab"></a>

```c
void(* scanned )(struct bt_le_ext_adv *adv, struct bt_le_ext_adv_scanned_info *info)
```

相关声明：[scanned](#a277dc3269741d40b644ae3c777198fab)、[bt_le_ext_adv](P102_bt_le_ext_adv_结构体.md)、[bt_le_ext_adv_scanned_info](P106_bt_le_ext_adv_scanned_info_结构体.md)。

广播集（Advertising set）已发送扫描响应数据（Scan response data）。

<a id="r_a251ea84adf8b6cc14bae051d74edc1fe"></a>

```c
bool(* rpa_expired )(struct bt_le_ext_adv *adv)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[rpa_expired](#a251ea84adf8b6cc14bae051d74edc1fe)、[bt_le_ext_adv](P102_bt_le_ext_adv_结构体.md)。

广播集的可解析私有地址（RPA）有效期已到期。

<a id="r_ab6452d9b3449847bf009c3d43c051922"></a>

```c
void(* pawr_data_request )(struct bt_le_ext_adv *adv, const struct bt_le_per_adv_data_request *request)
```

相关声明：[pawr_data_request](#ab6452d9b3449847bf009c3d43c051922)、[bt_le_ext_adv](P102_bt_le_ext_adv_结构体.md)、[bt_le_per_adv_data_request](P112_bt_le_per_adv_data_request_结构体.md)。

控制器表示已准备好发送一个或多个带响应的周期广播子事件（PAwR subevents）。

<a id="r_a6b26be418789c6e5087dab1100cb56a8"></a>

```c
void(* pawr_response )(struct bt_le_ext_adv *adv, struct bt_le_per_adv_response_info *info, struct net_buf_simple *buf)
```

相关声明：[pawr_response](#a6b26be418789c6e5087dab1100cb56a8)、[bt_le_ext_adv](P102_bt_le_ext_adv_结构体.md)、[bt_le_per_adv_response_info](P114_bt_le_per_adv_response_info_结构体.md)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

控制器表示，一个或多个已同步设备已响应周期广播子事件指示（Periodic advertising subevent indication）。

## 103.2\_详细说明（Detailed Documentation）

<a id="a7aad0fbd8e531e70f661500c338d870e"></a>

### `connected`

```c
void(* bt_le_ext_adv_cb::connected) (struct bt_le_ext_adv *adv, struct bt_le_ext_adv_connected_info *info)
```

广播集（Advertising set）已接受新连接。

此回调通知应用，广播集（Advertising set）已接受新连接。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `adv` | 广播集对象（Advertising set object）。 |
| `info` | 连接事件的信息（Connected event information）。 |

<a id="ab6452d9b3449847bf009c3d43c051922"></a>

### `pawr_data_request`

```c
void(* bt_le_ext_adv_cb::pawr_data_request) (struct bt_le_ext_adv *adv, const struct bt_le_per_adv_data_request *request)
```

控制器表示已准备好发送一个或多个带响应的周期广播子事件（PAwR subevents）。

此回调通知应用，控制器已请求即将到来的子事件（Subevents）所需的数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `adv` | 广播集对象（Advertising set object）。 |
| `request` | 即将到来的子事件信息（Subevent information）。 |

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 `CONFIG_BT_PER_ADV_RSP` 时可用。

<a id="a6b26be418789c6e5087dab1100cb56a8"></a>

### `pawr_response`

```c
void(* bt_le_ext_adv_cb::pawr_response) (struct bt_le_ext_adv *adv, struct bt_le_per_adv_response_info *info, struct net_buf_simple *buf)
```

控制器表示，一个或多个已同步设备已响应周期广播子事件指示（Periodic advertising subevent indication）。

一个响应可能被拆分到多份控制器报告（Controller reports）中。启用 `CONFIG_BT_PER_ADV_RSP_REASSEMBLY` 时，主机（Host）会重组片段，并在一次回调中交付完整响应。禁用时，丢弃不完整报告，只向应用转发控制器已标记为完整（Complete）的报告。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `adv` | 广播集对象（Advertising set object）。 |
| `info` | 已接收响应的信息（Response information）。 |
| `buf` | 接收到的数据（Received data）。若控制器报告未收到任何响应，则为 `NULL`。 |

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 `CONFIG_BT_PER_ADV_RSP` 时可用。

<a id="a251ea84adf8b6cc14bae051d74edc1fe"></a>

### `rpa_expired`

```c
bool(* bt_le_ext_adv_cb::rpa_expired) (struct bt_le_ext_adv *adv)
```

广播集的可解析私有地址（RPA）有效期已到期。

此回调通知应用，广播集的可解析私有地址（RPA）有效期已到期。用户可以利用此回调，使广播载荷更新（Advertising payload update）与 RPA 轮换（RPA rotation）同步，例如在回调中调用 `bt_le_ext_adv_set_data`。

如果启用了可解析私有地址共享（RPA sharing），参见 `CONFIG_BT_RPA_SHARING`，且属于同一广播身份（Adv ID）的任一广播集的此 RPA 到期回调返回 `false`，则这些广播集会在 RPA 轮换期间继续使用旧 RPA。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `adv` | 广播集对象（Advertising set object）。 |

**返回（Returns）**：返回值（Returns）：`true` 表示轮换当前可解析私有地址（RPA）；`false` 表示下一个轮换周期继续使用它。

<a id="a277dc3269741d40b644ae3c777198fab"></a>

### `scanned`

```c
void(* bt_le_ext_adv_cb::scanned) (struct bt_le_ext_adv *adv, struct bt_le_ext_adv_scanned_info *info)
```

广播集（Advertising set）已发送扫描响应数据（Scan response data）。

此回调通知应用，广播集已收到扫描请求数据包（Scan Request），并已发送扫描响应数据包（Scan Response）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `adv` | 广播集对象（Advertising set object）。 |
| `info` | 扫描事件信息（Scanned event information），即地址（Address）。 |

<a id="a85b8887c9ef443d18b71e9561e7dde60"></a>

### `sent`

```c
void(* bt_le_ext_adv_cb::sent) (struct bt_le_ext_adv *adv, struct bt_le_ext_adv_sent_info *info)
```

广播集（Advertising set）达到限制后已禁用。

达到 `bt_le_ext_adv_start_param::timeout` 或 `bt_le_ext_adv_start_param::num_events` 指定的限制时，调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `adv` | 广播集对象（Advertising set object）。 |
| `info` | 发送事件信息（Sent event information）。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/bluetooth.h`

## 103.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h_source.html)
- [bt_le_ext_adv](P102_bt_le_ext_adv_结构体.md)
- [bt_le_ext_adv_sent_info](P107_bt_le_ext_adv_sent_info_结构体.md)
- [bt_le_ext_adv_connected_info](P104_bt_le_ext_adv_connected_info_结构体.md)
- [bt_le_ext_adv_scanned_info](P106_bt_le_ext_adv_scanned_info_结构体.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [bt_le_per_adv_data_request](P112_bt_le_per_adv_data_request_结构体.md)
- [bt_le_per_adv_response_info](P114_bt_le_per_adv_response_info_结构体.md)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [bt_le_ext_adv_cb](P103_bt_le_ext_adv_cb_结构体.md)
- [bt_le_ext_adv_create](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gad02b855dd7a26e3910b247fa73f19297)
- [回调执行上下文（Callback execution contexts）](../bluetooth/P004_低功耗蓝牙主机.md#bluetooth-callback-contexts)
- [CONFIG_BT_PER_ADV_RSP](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PER_ADV_RSP)
- [CONFIG_BT_PER_ADV_RSP_REASSEMBLY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PER_ADV_RSP_REASSEMBLY)
- [bt_le_ext_adv_set_data](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gad731f829b3566be3e56485b2a64f80b1)
- [CONFIG_BT_RPA_SHARING](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_RPA_SHARING)
- [bt_le_ext_adv_start_param::timeout](P108_bt_le_ext_adv_start_param_结构体.md#a80bb1ef4316dd75ea1268241333f4346)
- [bt_le_ext_adv_start_param::num_events](P108_bt_le_ext_adv_start_param_结构体.md#ab45ae0bfdb144071efcc64c30648388f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P102_bt_le_ext_adv_结构体.md) · [返回大纲](大纲.md) · [下一章](P104_bt_le_ext_adv_connected_info_结构体.md)
