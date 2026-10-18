---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-120
title: bt_le_per_adv_sync_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__per__adv__sync__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第120章\_bt\_le\_per\_adv\_sync\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__per__adv__sync__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

创建周期广播同步（Periodic Advertising Sync）对象的参数。

```c
#include <zephyr/bluetooth/bluetooth.h>
```

<a id="details"></a>

创建周期广播同步对象的参数（Periodic advertising sync object parameters）。此结构保存创建周期广播同步对象所需的参数，使系统能够同步接收广播器的周期广播报告。参数包括广播器地址、广播集标识符（SID）、同步选项、事件跳过数及同步超时。注意（Note）：`bt_le_per_adv_sync_param` 作为 `bt_le_per_adv_sync_create` 函数的参数，用于配置同步行为。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 120.1\_数据成员（Data Fields）

<a id="r_ac93adedad747f61a771ac5445e486b74"></a>

```c
bt_addr_le_t addr
```

相关声明：[bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)、[addr](#ac93adedad747f61a771ac5445e486b74)。

周期性广播者地址（Periodic Advertiser Address）。

<a id="r_a70795642ee94dd9e87f0cf251c095e7f"></a>

```c
uint8_t sid
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sid](#a70795642ee94dd9e87f0cf251c095e7f)。

广播集标识符（Advertising Set Identifier）。

<a id="r_a4252f2b3b453c2f9c8fbf8c35a618ff2"></a>

```c
uint32_t options
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[options](#a4252f2b3b453c2f9c8fbf8c35a618ff2)。

周期广播同步选项位域（Periodic advertising sync options bit-field），参见 `bt_le_adv_opt` 字段。

<a id="r_af9abb65547fb5bfea65f4c22963c7da0"></a>

```c
uint16_t skip
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[skip](#af9abb65547fb5bfea65f4c22963c7da0)。

最大事件跳过数（Maximum event skip）。

<a id="r_a301cfd3d6e5620d29c021ababe104754"></a>

```c
uint16_t timeout
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[timeout](#a301cfd3d6e5620d29c021ababe104754)。

同步超时（Synchronization timeout），为 N × 10 毫秒。

## 120.2\_详细说明（Detailed Documentation）

<a id="ac93adedad747f61a771ac5445e486b74"></a>

### `addr`

```c
bt_addr_le_t bt_le_per_adv_sync_param::addr
```

周期性广播者地址（Periodic Advertiser Address）。

仅在未使用周期广播列表（Periodic advertising list），即未使用 `BT_LE_PER_ADV_SYNC_OPT_USE_PER_ADV_LIST` 时有效。

<a id="a4252f2b3b453c2f9c8fbf8c35a618ff2"></a>

### `options`

```c
uint32_t bt_le_per_adv_sync_param::options
```

周期广播同步选项位域（Periodic advertising sync options bit-field），参见 `bt_le_adv_opt` 字段。

<a id="a70795642ee94dd9e87f0cf251c095e7f"></a>

### `sid`

```c
uint8_t bt_le_per_adv_sync_param::sid
```

广播集标识符（Advertising Set Identifier）。

有效范围为 `BT_GAP_SID_MIN` 至 `BT_GAP_SID_MAX`。

仅在未使用周期广播列表（Periodic advertising list），即未使用 `BT_LE_PER_ADV_SYNC_OPT_USE_PER_ADV_LIST` 时有效。

<a id="af9abb65547fb5bfea65f4c22963c7da0"></a>

### `skip`

```c
uint16_t bt_le_per_adv_sync_param::skip
```

最大事件跳过数（Maximum event skip）。

成功接收后最多可跳过的周期广播事件数量（Periodic advertising events），范围为 `0x0000`–`0x01F3`。

<a id="a301cfd3d6e5620d29c021ababe104754"></a>

### `timeout`

```c
uint16_t bt_le_per_adv_sync_param::timeout
```

同步超时（Synchronization timeout），为 N × 10 毫秒。

周期广播同步的同步超时（Synchronization timeout），范围为 `0x000A`–`0x4000`，即 100–163840 毫秒。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/bluetooth.h`

## 120.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h_source.html)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bt_le_adv_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gafbf81dab68b0e484d4742471c722fc28)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_le_per_adv_sync_param](P120_bt_le_per_adv_sync_param_结构体.md)
- [bt_le_per_adv_sync_create](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ga061bf84b989b2c96ab51d2ca0debb017)
- [BT_LE_PER_ADV_SYNC_OPT_USE_PER_ADV_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#ggac942d7e3cae8fca22080f93bf9528ee9ae9a88caa6a83da8b1697a6167629bf7e)
- [BT_GAP_SID_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gacf05b7660d2ae85f64e2a220abf8e57d)
- [BT_GAP_SID_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap__defines.html#gafa6f803fe3ada07030fb1f2f725940c4)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P119_bt_le_per_adv_sync_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P121_bt_le_per_adv_sync_recv_info_结构体.md)
