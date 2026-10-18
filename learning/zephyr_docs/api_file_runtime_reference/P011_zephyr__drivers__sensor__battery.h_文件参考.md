---
id: learning.zephyr-docs.api-file-runtime-reference.page-11
title: zephyr__drivers__sensor__battery.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2battery_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_zephyr\_\_drivers\_\_sensor\_\_battery.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2battery_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stdint.h>
#include <errno.h>
#include <zephyr/devicetree.h>
#include <zephyr/math/interpolation.h>
#include <zephyr/sys/util_macro.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 11.1\_宏定义（Macros）

<a id="r_ga02de0e4f76b8e5804b82cd397c13ef86"></a>

```c
#define BATTERY_OCV_TABLE_LEN 11
```

相关声明：[BATTERY_OCV_TABLE_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__battery__apis.html#ga02de0e4f76b8e5804b82cd397c13ef86)。

<a id="r_gae2c365581f7c8c71e1ec31b223545711"></a>

```c
#define BATTERY_CHEMISTRY_DT_GET(node_id)
```

相关声明：[BATTERY_CHEMISTRY_DT_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__battery__apis.html#gae2c365581f7c8c71e1ec31b223545711)。

获取电池化学体系枚举值（Battery Chemistry Enum Value）。

<a id="r_ga833bf8bf88136fd277a69fb41ad0fb7f"></a>

```c
#define BATTERY_OCV_TABLE_DT_GET(node_id, table)
```

相关声明：[BATTERY_OCV_TABLE_DT_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__battery__apis.html#ga833bf8bf88136fd277a69fb41ad0fb7f)。

获取给定表对应的开路电压曲线（Open-Circuit Voltage Curve，OCV Curve）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 11.2\_枚举（Enumerations）

<a id="r_gaf7ee6b6e85da9f31231cac577428de01"></a>

```c
enum battery_chemistry { BATTERY_CHEMISTRY_UNKNOWN = 0 , BATTERY_CHEMISTRY_NICKEL_CADMIUM , BATTERY_CHEMISTRY_NICKEL_METAL_HYDRIDE , BATTERY_CHEMISTRY_LITHIUM_ION , BATTERY_CHEMISTRY_LITHIUM_ION_POLYMER , BATTERY_CHEMISTRY_LITHIUM_ION_IRON_PHOSPHATE , BATTERY_CHEMISTRY_LITHIUM_ION_MANGANESE_OXIDE }
```

相关声明：[battery_chemistry](https://docs.zephyrproject.org/latest/doxygen/html/group__battery__apis.html#gaf7ee6b6e85da9f31231cac577428de01)、[BATTERY_CHEMISTRY_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__battery__apis.html#ggaf7ee6b6e85da9f31231cac577428de01a52bae762c2ef4ca140c1e7f89440b007)、[BATTERY_CHEMISTRY_NICKEL_CADMIUM](https://docs.zephyrproject.org/latest/doxygen/html/group__battery__apis.html#ggaf7ee6b6e85da9f31231cac577428de01a00f07b177e6246e139b469386064698f)、[BATTERY_CHEMISTRY_NICKEL_METAL_HYDRIDE](https://docs.zephyrproject.org/latest/doxygen/html/group__battery__apis.html#ggaf7ee6b6e85da9f31231cac577428de01a377834c71930068b6a822d4afd2112f4)、[BATTERY_CHEMISTRY_LITHIUM_ION](https://docs.zephyrproject.org/latest/doxygen/html/group__battery__apis.html#ggaf7ee6b6e85da9f31231cac577428de01a450162d694da85864af48712cb05badd)、[BATTERY_CHEMISTRY_LITHIUM_ION_POLYMER](https://docs.zephyrproject.org/latest/doxygen/html/group__battery__apis.html#ggaf7ee6b6e85da9f31231cac577428de01ab21f5e769426047924d83e5301b8a19f)、[BATTERY_CHEMISTRY_LITHIUM_ION_IRON_PHOSPHATE](https://docs.zephyrproject.org/latest/doxygen/html/group__battery__apis.html#ggaf7ee6b6e85da9f31231cac577428de01a951b3bea1c503ce6f1d78e8cc1ed9e37)、[BATTERY_CHEMISTRY_LITHIUM_ION_MANGANESE_OXIDE](https://docs.zephyrproject.org/latest/doxygen/html/group__battery__apis.html#ggaf7ee6b6e85da9f31231cac577428de01a30cd5d02bb416248b9380ab953836e96)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 11.3\_函数（Functions）

<a id="r_gaea81fb0c63b85654005b6f65521c3345"></a>

```c
static int32_t battery_soc_lookup (const int32_t ocv_table[11], uint32_t voltage_uv)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[battery_soc_lookup](https://docs.zephyrproject.org/latest/doxygen/html/group__battery__apis.html#gaea81fb0c63b85654005b6f65521c3345)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

将开路电压表（OCV Table）和电池电压（Battery Voltage）转换为电量百分比（Charge Percentage）。


## 11.4\_原页交叉引用（Cross References）

- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [zephyr/devicetree.h](../dt_main_reference/P002_设备树主头文件源码.md)
- [zephyr/math/interpolation.h](../interpolation_reference/P003_插值头文件源码.md)
- [zephyr/sys/util_macro.h](../util_reference/P005_宏工具头文件源码.md)
- [查看此文件的源码。](../api_source_runtime_reference/P014_battery.h_源码浏览.md)
- [BATTERY_OCV_TABLE_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__battery__apis.html#ga02de0e4f76b8e5804b82cd397c13ef86)
- [BATTERY_CHEMISTRY_DT_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__battery__apis.html#gae2c365581f7c8c71e1ec31b223545711)
- [BATTERY_OCV_TABLE_DT_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__battery__apis.html#ga833bf8bf88136fd277a69fb41ad0fb7f)
- [battery_chemistry](https://docs.zephyrproject.org/latest/doxygen/html/group__battery__apis.html#gaf7ee6b6e85da9f31231cac577428de01)
- [BATTERY_CHEMISTRY_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__battery__apis.html#ggaf7ee6b6e85da9f31231cac577428de01a52bae762c2ef4ca140c1e7f89440b007)
- [BATTERY_CHEMISTRY_NICKEL_CADMIUM](https://docs.zephyrproject.org/latest/doxygen/html/group__battery__apis.html#ggaf7ee6b6e85da9f31231cac577428de01a00f07b177e6246e139b469386064698f)
- [BATTERY_CHEMISTRY_NICKEL_METAL_HYDRIDE](https://docs.zephyrproject.org/latest/doxygen/html/group__battery__apis.html#ggaf7ee6b6e85da9f31231cac577428de01a377834c71930068b6a822d4afd2112f4)
- [BATTERY_CHEMISTRY_LITHIUM_ION](https://docs.zephyrproject.org/latest/doxygen/html/group__battery__apis.html#ggaf7ee6b6e85da9f31231cac577428de01a450162d694da85864af48712cb05badd)
- [BATTERY_CHEMISTRY_LITHIUM_ION_POLYMER](https://docs.zephyrproject.org/latest/doxygen/html/group__battery__apis.html#ggaf7ee6b6e85da9f31231cac577428de01ab21f5e769426047924d83e5301b8a19f)
- [BATTERY_CHEMISTRY_LITHIUM_ION_IRON_PHOSPHATE](https://docs.zephyrproject.org/latest/doxygen/html/group__battery__apis.html#ggaf7ee6b6e85da9f31231cac577428de01a951b3bea1c503ce6f1d78e8cc1ed9e37)
- [BATTERY_CHEMISTRY_LITHIUM_ION_MANGANESE_OXIDE](https://docs.zephyrproject.org/latest/doxygen/html/group__battery__apis.html#ggaf7ee6b6e85da9f31231cac577428de01a30cd5d02bb416248b9380ab953836e96)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [battery_soc_lookup](https://docs.zephyrproject.org/latest/doxygen/html/group__battery__apis.html#gaea81fb0c63b85654005b6f65521c3345)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)

---

[上一章](P010_zephyr__drivers__otp__npm10xx.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P012_zephyr__drivers__sensor__icm4268x.h_文件参考.md)
