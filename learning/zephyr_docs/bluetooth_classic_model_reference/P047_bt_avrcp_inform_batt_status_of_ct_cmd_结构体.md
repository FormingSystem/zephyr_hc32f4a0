---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-47
title: bt_avrcp_inform_batt_status_of_ct_cmd_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__inform__batt__status__of__ct__cmd.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第47章\_bt\_avrcp\_inform\_batt\_status\_of\_ct\_cmd\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__inform__batt__status__of__ct__cmd.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

通知控制端电池状态（InformBatteryStatusOfCT）命令请求。

```c
#include <zephyr/bluetooth/classic/avrcp.h>
```

<a id="details"></a>

通知控制端电池状态（InformBatteryStatusOfCT）命令请求。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 47.1\_数据成员（Data Fields）

<a id="r_ae79067d210d7484c18adc3570ec20af1"></a>

```c
uint8_t battery_status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[battery_status](#ae79067d210d7484c18adc3570ec20af1)。

电池状态值，类型为 `bt_avrcp_battery_status_t`。

## 47.2\_详细说明（Detailed Documentation）

<a id="ae79067d210d7484c18adc3570ec20af1"></a>

### `battery_status`

```c
uint8_t bt_avrcp_inform_batt_status_of_ct_cmd::battery_status
```

电池状态值，类型为 `bt_avrcp_battery_status_t`。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp.h`

## 47.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_avrcp_battery_status_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html#ga33825b183b12a2b29d5148a7366c0e77)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P046_bt_avrcp_get_total_number_of_items_rsp_结构体.md) · [返回大纲](大纲.md) · [下一章](P048_bt_avrcp_inform_displayable_char_set_cmd_结构体.md)
