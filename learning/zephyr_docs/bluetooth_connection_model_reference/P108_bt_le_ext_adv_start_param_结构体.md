---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-108
title: bt_le_ext_adv_start_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__ext__adv__start__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第108章\_bt\_le\_ext\_adv\_start\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__ext__adv__start__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

启动扩展广播会话（Extended Advertising Session）的参数。

```c
#include <zephyr/bluetooth/bluetooth.h>
```

<a id="details"></a>

启动扩展广播会话的参数（Extended advertising session parameters）。此结构用于控制扩展广播会话行为，包括超时和要发送的广播事件数量。超时以 10 毫秒为单位；事件数量决定广播在停止前发送多少次。达到超时或事件数量限制时，会停止广播会话，并通过广播器发送完成回调（Advertiser sent callback）通知应用。如果两个参数都提供，则达到任一限制即停止。注意（Note）：用于 `bt_le_ext_adv_start` 函数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 108.1\_数据成员（Data Fields）

<a id="r_a80bb1ef4316dd75ea1268241333f4346"></a>

```c
uint16_t timeout
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[timeout](#a80bb1ef4316dd75ea1268241333f4346)。

广播集的最长持续时间（Maximum advertising set duration），为 N × 10 毫秒。

<a id="r_ab45ae0bfdb144071efcc64c30648388f"></a>

```c
uint8_t num_events
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_events](#ab45ae0bfdb144071efcc64c30648388f)。

要发送的扩展广播事件最大数量（Extended advertising events）。

## 108.2\_详细说明（Detailed Documentation）

<a id="ab45ae0bfdb144071efcc64c30648388f"></a>

### `num_events`

```c
uint8_t bt_le_ext_adv_start_param::num_events
```

要发送的扩展广播事件最大数量（Extended advertising events）。

完整广播，即扩展广播事件（Extended advertising event），发送达到指定次数后，可自动禁用广播器。已发送广播协议数据单元（Advertising PDUs）的数量可能更大，与此计数无关。

设为零表示无限制（No limit）。

因达到此限制而自动禁用广播集时，将调用 `bt_le_ext_adv_cb::sent`。

背景说明参见蓝牙核心规范（Bluetooth Core Specification）6.0 版第 4 卷 E 部分第 7.8.56 节中的 `Max_Extended_Advertising_Events` 参数。

<a id="a80bb1ef4316dd75ea1268241333f4346"></a>

### `timeout`

```c
uint16_t bt_le_ext_adv_start_param::timeout
```

广播集的最长持续时间（Maximum advertising set duration），为 N × 10 毫秒。

广播集首次在空中发送后，经过指定时间，可以自动禁用该广播集（Advertising set）。

设为零表示无限制（No limit）；以 10 毫秒为单位设置。

因达到此限制而自动禁用广播集时，将调用 `bt_le_ext_adv_cb::sent`。

使用高占空比定向可连接广播（High duty cycle directed connectable advertising）时，此参数必须设为非零，且不超过最大值 `BT_GAP_ADV_HIGH_DUTY_CYCLE_MAX_TIMEOUT`。

若启用了隐私配置 `CONFIG_BT_PRIVACY`，则超时必须小于 `CONFIG_BT_RPA_TIMEOUT`。

背景说明参见蓝牙核心规范（Bluetooth Core Specification）6.0 版第 4 卷 E 部分第 7.8.56 节中的 `Duration` 参数。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/bluetooth.h`

## 108.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_le_ext_adv_start](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gaf0f436c55482d9429f674303ae3aa815)
- [bt_le_ext_adv_cb::sent](P103_bt_le_ext_adv_cb_结构体.md#a85b8887c9ef443d18b71e9561e7dde60)
- [BT_GAP_ADV_HIGH_DUTY_CYCLE_MAX_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gabe483d4dd601b11ac3eea570c962b1ec)
- [CONFIG_BT_PRIVACY](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PRIVACY)
- [CONFIG_BT_RPA_TIMEOUT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_RPA_TIMEOUT)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P107_bt_le_ext_adv_sent_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P109_bt_le_local_features_结构体.md)
