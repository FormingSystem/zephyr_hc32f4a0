---
id: learning.zephyr-docs.api-service-topic-reference.page-1
title: 电池 API（Battery APIs）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__battery__apis.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_电池 API（Battery APIs）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__battery__apis.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

电池 API（Battery API）

<a id="details"></a>

电池 API（Battery API）

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.1\_宏定义（Macros）

<a id="r_ga02de0e4f76b8e5804b82cd397c13ef86"></a>

```c
#define BATTERY_OCV_TABLE_LEN 11
```

相关声明：[BATTERY_OCV_TABLE_LEN](#ga02de0e4f76b8e5804b82cd397c13ef86)。

<a id="r_gae2c365581f7c8c71e1ec31b223545711"></a>

```c
#define BATTERY_CHEMISTRY_DT_GET(node_id)
```

相关声明：[BATTERY_CHEMISTRY_DT_GET](#gae2c365581f7c8c71e1ec31b223545711)。

获取电池化学体系枚举值（Battery Chemistry Enum Value）。

<a id="r_ga833bf8bf88136fd277a69fb41ad0fb7f"></a>

```c
#define BATTERY_OCV_TABLE_DT_GET(node_id, table)
```

相关声明：[BATTERY_OCV_TABLE_DT_GET](#ga833bf8bf88136fd277a69fb41ad0fb7f)。

获取给定表对应的开路电压曲线（Open-Circuit Voltage Curve，OCV Curve）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 1.2\_枚举（Enumerations）

<a id="r_gaf7ee6b6e85da9f31231cac577428de01"></a>

```c
enum battery_chemistry { BATTERY_CHEMISTRY_UNKNOWN = 0 , BATTERY_CHEMISTRY_NICKEL_CADMIUM , BATTERY_CHEMISTRY_NICKEL_METAL_HYDRIDE , BATTERY_CHEMISTRY_LITHIUM_ION , BATTERY_CHEMISTRY_LITHIUM_ION_POLYMER , BATTERY_CHEMISTRY_LITHIUM_ION_IRON_PHOSPHATE , BATTERY_CHEMISTRY_LITHIUM_ION_MANGANESE_OXIDE }
```

相关声明：[battery_chemistry](#gaf7ee6b6e85da9f31231cac577428de01)、[BATTERY_CHEMISTRY_UNKNOWN](#ggaf7ee6b6e85da9f31231cac577428de01a52bae762c2ef4ca140c1e7f89440b007)、[BATTERY_CHEMISTRY_NICKEL_CADMIUM](#ggaf7ee6b6e85da9f31231cac577428de01a00f07b177e6246e139b469386064698f)、[BATTERY_CHEMISTRY_NICKEL_METAL_HYDRIDE](#ggaf7ee6b6e85da9f31231cac577428de01a377834c71930068b6a822d4afd2112f4)、[BATTERY_CHEMISTRY_LITHIUM_ION](#ggaf7ee6b6e85da9f31231cac577428de01a450162d694da85864af48712cb05badd)、[BATTERY_CHEMISTRY_LITHIUM_ION_POLYMER](#ggaf7ee6b6e85da9f31231cac577428de01ab21f5e769426047924d83e5301b8a19f)、[BATTERY_CHEMISTRY_LITHIUM_ION_IRON_PHOSPHATE](#ggaf7ee6b6e85da9f31231cac577428de01a951b3bea1c503ce6f1d78e8cc1ed9e37)、[BATTERY_CHEMISTRY_LITHIUM_ION_MANGANESE_OXIDE](#ggaf7ee6b6e85da9f31231cac577428de01a30cd5d02bb416248b9380ab953836e96)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.3\_函数（Functions）

<a id="r_gaea81fb0c63b85654005b6f65521c3345"></a>

```c
static int32_t battery_soc_lookup (const int32_t ocv_table[11], uint32_t voltage_uv)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[battery_soc_lookup](#gaea81fb0c63b85654005b6f65521c3345)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

将开路电压表（OCV Table）和电池电压（Battery Voltage）转换为电量百分比（Charge Percentage）。

## 1.4\_详细说明（Detailed Documentation）

<a id="gae2c365581f7c8c71e1ec31b223545711"></a>

### `BATTERY_CHEMISTRY_DT_GET`

```c
#define BATTERY_CHEMISTRY_DT_GET ( node_id)
```

```c
#include <zephyr/drivers/sensor/battery.h>
```

展开值（Value）：

```c
UTIL_CAT(BATTERY_CHEMISTRY_, DT_STRING_UPPER_TOKEN_OR(node_id, device_chemistry, UNKNOWN))
```

获取电池化学体系枚举值（Battery Chemistry Enum Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 节点标识符。 |

<a id="ga833bf8bf88136fd277a69fb41ad0fb7f"></a>

### `BATTERY_OCV_TABLE_DT_GET`

```c
#define BATTERY_OCV_TABLE_DT_GET ( node_id, table )
```

```c
#include <zephyr/drivers/sensor/battery.h>
```

展开值（Value）：

```c
COND_CODE_1(DT_NODE_HAS_PROP(node_id, table),                                              \
            ({DT_FOREACH_PROP_ELEM_SEP(node_id, table, DT_PROP_BY_IDX, (,))}), ({-1}))
```

获取给定表对应的开路电压曲线（Open-Circuit Voltage Curve，OCV Curve）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 节点标识符。 |
| `table` | 要获取的表（Table）。 |

<a id="ga02de0e4f76b8e5804b82cd397c13ef86"></a>

### `BATTERY_OCV_TABLE_LEN`

```c
#define BATTERY_OCV_TABLE_LEN 11
```

```c
#include <zephyr/drivers/sensor/battery.h>
```

<a id="gaf7ee6b6e85da9f31231cac577428de01"></a>

### `battery_chemistry`

```c
enum battery_chemistry
```

```c
#include <zephyr/drivers/sensor/battery.h>
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BATTERY_CHEMISTRY_UNKNOWN` |  |
| `BATTERY_CHEMISTRY_NICKEL_CADMIUM` |  |
| `BATTERY_CHEMISTRY_NICKEL_METAL_HYDRIDE` |  |
| `BATTERY_CHEMISTRY_LITHIUM_ION` |  |
| `BATTERY_CHEMISTRY_LITHIUM_ION_POLYMER` |  |
| `BATTERY_CHEMISTRY_LITHIUM_ION_IRON_PHOSPHATE` |  |
| `BATTERY_CHEMISTRY_LITHIUM_ION_MANGANESE_OXIDE` |  |

<a id="gaea81fb0c63b85654005b6f65521c3345"></a>

### `battery_soc_lookup()`

```c
int32_t battery_soc_lookup ( const int32_t ocv_table[11], uint32_t voltage_uv )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/sensor/battery.h>
```

将开路电压表（OCV Table）和电池电压（Battery Voltage）转换为电量百分比（Charge Percentage）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ocv_table` | 开路电压曲线（Open Circuit Voltage Curve）。 |
| `voltage_uv` | 电池电压（Battery Voltage），单位为微伏（Microvolts）。 |

返回（Returns）：电池荷电状态（Battery State of Charge），单位为千分之一百分比（MilliPercent）。


## 1.5\_原页交叉引用（Cross References）

- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [zephyr/drivers/sensor/battery.h](../api_file_runtime_reference/P011_zephyr__drivers__sensor__battery.h_文件参考.md)
- [UTIL_CAT](../util_reference/P006_内部宏工具头文件参考.md#a7e7766e792d1638bfbbc9d0f328d3d0d)
- [DT_STRING_UPPER_TOKEN_OR](../dt_property_reference/P001_设备树属性读取宏.md#gab79f5274c82d025d805ec94d2935c9b9)
- [COND_CODE_1](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20)
- [DT_NODE_HAS_PROP](../dt_identity_reference/P002_设备树存在性与状态宏.md#gacce67bf20541cd2d07d8540058964692)
- [DT_FOREACH_PROP_ELEM_SEP](../dt_foreach_reference/P001_设备树遍历宏.md#ga72d0b6859b4fc61cde518aee118d9ed8)
- [DT_PROP_BY_IDX](../dt_property_reference/P001_设备树属性读取宏.md#ga52ad691ea4cae633ca702020e939d461)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__devicetree-generic-prop_html_gab79f5274c82d025d805ec94d2935c9b9"></a>
<a id="autil__internal_8h_html_a7e7766e792d1638bfbbc9d0f328d3d0d"></a>
<a id="agroup__devicetree-generic-exist_html_gacce67bf20541cd2d07d8540058964692"></a>
<a id="agroup__devicetree-generic-foreach_html_ga72d0b6859b4fc61cde518aee118d9ed8"></a>
<a id="agroup__devicetree-generic-prop_html_ga52ad691ea4cae633ca702020e939d461"></a>
<a id="agroup__sys-util_html_ga358bc3e7669c860a98839a51cd526b20"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggaf7ee6b6e85da9f31231cac577428de01a52bae762c2ef4ca140c1e7f89440b007"></a>
<a id="ggaf7ee6b6e85da9f31231cac577428de01a00f07b177e6246e139b469386064698f"></a>
<a id="ggaf7ee6b6e85da9f31231cac577428de01a377834c71930068b6a822d4afd2112f4"></a>
<a id="ggaf7ee6b6e85da9f31231cac577428de01a450162d694da85864af48712cb05badd"></a>
<a id="ggaf7ee6b6e85da9f31231cac577428de01ab21f5e769426047924d83e5301b8a19f"></a>
<a id="ggaf7ee6b6e85da9f31231cac577428de01a951b3bea1c503ce6f1d78e8cc1ed9e37"></a>
<a id="ggaf7ee6b6e85da9f31231cac577428de01a30cd5d02bb416248b9380ab953836e96"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_蓝牙 Mesh BLOB 闪存数据流（Flash stream）.md)
