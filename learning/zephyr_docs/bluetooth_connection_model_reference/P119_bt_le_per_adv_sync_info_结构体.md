---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-119
title: bt_le_per_adv_sync_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__per__adv__sync__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第119章\_bt\_le\_per\_adv\_sync\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__per__adv__sync__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

周期广播集（Periodic Advertising Set）的信息结构。

```c
#include <zephyr/bluetooth/bluetooth.h>
```

<a id="details"></a>

周期广播集（Periodic Advertising Set）的信息结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 119.1\_数据成员（Data Fields）

<a id="r_ac10fc2e2d3ec2160db8c2aac148d18a2"></a>

```c
bt_addr_le_t addr
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[addr](#ac10fc2e2d3ec2160db8c2aac148d18a2)。

周期性广播者地址（Periodic Advertiser Address）。

<a id="r_acc0ef26c38279c9a67f8992005c2e58a"></a>

```c
uint8_t sid
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sid](#acc0ef26c38279c9a67f8992005c2e58a)。

广播集标识符（Advertising Set Identifier），有效范围为 `BT_GAP_SID_MIN` 至 `BT_GAP_SID_MAX`。

<a id="r_a365a0d8577429e4ee96e977071c9a906"></a>

```c
uint16_t interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[interval](#a365a0d8577429e4ee96e977071c9a906)。

周期广播间隔（Periodic advertising interval），为 N × 1.25 毫秒。

<a id="r_a4d9520ea6a803f8fe4f41190f55c26e5"></a>

```c
uint8_t phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[phy](#a4d9520ea6a803f8fe4f41190f55c26e5)。

广播器物理层（Advertiser PHY），参见 `bt_gap_le_phy`。

## 119.2\_详细说明（Detailed Documentation）

<a id="ac10fc2e2d3ec2160db8c2aac148d18a2"></a>

### `addr`

```c
bt_addr_le_t bt_le_per_adv_sync_info::addr
```

周期性广播者地址（Periodic Advertiser Address）。

<a id="a365a0d8577429e4ee96e977071c9a906"></a>

### `interval`

```c
uint16_t bt_le_per_adv_sync_info::interval
```

周期广播间隔（Periodic advertising interval），为 N × 1.25 毫秒。

<a id="a4d9520ea6a803f8fe4f41190f55c26e5"></a>

### `phy`

```c
uint8_t bt_le_per_adv_sync_info::phy
```

广播器物理层（Advertiser PHY），参见 `bt_gap_le_phy`。

<a id="acc0ef26c38279c9a67f8992005c2e58a"></a>

### `sid`

```c
uint8_t bt_le_per_adv_sync_info::sid
```

广播集标识符（Advertising Set Identifier），有效范围为 `BT_GAP_SID_MIN` 至 `BT_GAP_SID_MAX`。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/bluetooth.h`

## 119.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h_source.html)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [BT_GAP_SID_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gacf05b7660d2ae85f64e2a220abf8e57d)
- [BT_GAP_SID_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gafa6f803fe3ada07030fb1f2f725940c4)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_gap_le_phy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#ga691d9793fd21c41b2c192d65cc2bf6c4)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P118_bt_le_per_adv_sync_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P120_bt_le_per_adv_sync_param_结构体.md)
