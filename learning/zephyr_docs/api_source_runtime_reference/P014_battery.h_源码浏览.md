---
id: learning.zephyr-docs.api-source-runtime-reference.page-14
title: battery.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2battery_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_battery.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2battery_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2battery_8h.html)。

## 14.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="foldopen00031"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="foldopen00049"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="foldopen00058"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="foldopen00070"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="adevicetree_8h_html"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__battery__apis_html_ga02de0e4f76b8e5804b82cd397c13ef86"></a>
<a id="agroup__battery__apis_html_gaea81fb0c63b85654005b6f65521c3345"></a>
<a id="agroup__battery__apis_html_gaf7ee6b6e85da9f31231cac577428de01"></a>
<a id="agroup__battery__apis_html_ggaf7ee6b6e85da9f31231cac577428de01a00f07b177e6246e139b469386064698f"></a>
<a id="agroup__battery__apis_html_ggaf7ee6b6e85da9f31231cac577428de01a30cd5d02bb416248b9380ab953836e96"></a>
<a id="agroup__battery__apis_html_ggaf7ee6b6e85da9f31231cac577428de01a377834c71930068b6a822d4afd2112f4"></a>
<a id="agroup__battery__apis_html_ggaf7ee6b6e85da9f31231cac577428de01a450162d694da85864af48712cb05badd"></a>
<a id="agroup__battery__apis_html_ggaf7ee6b6e85da9f31231cac577428de01a52bae762c2ef4ca140c1e7f89440b007"></a>
<a id="agroup__battery__apis_html_ggaf7ee6b6e85da9f31231cac577428de01a951b3bea1c503ce6f1d78e8cc1ed9e37"></a>
<a id="agroup__battery__apis_html_ggaf7ee6b6e85da9f31231cac577428de01ab21f5e769426047924d83e5301b8a19f"></a>
<a id="agroup__math__interpolation_html_ga8abbb1799796222b39a051819bd19a2a"></a>
<a id="ainterpolation_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="autil__macro_8h_html"></a>

```c
/*
 * Copyright 2024 Embeint Inc
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_SENSOR_BATTERY_H_
#define ZEPHYR_INCLUDE_DRIVERS_SENSOR_BATTERY_H_

#include <stdint.h>
#include <errno.h>

#include <zephyr/devicetree.h>
#include <zephyr/math/interpolation.h>
#include <zephyr/sys/util_macro.h>

#ifdef __cplusplus
extern "C" {
#endif


/* Battery chemistry enumeration.
 * Value names must match those from dts/bindings/battery.yaml
 */
enum battery_chemistry {
        BATTERY_CHEMISTRY_UNKNOWN = 0,
        BATTERY_CHEMISTRY_NICKEL_CADMIUM,
        BATTERY_CHEMISTRY_NICKEL_METAL_HYDRIDE,
        BATTERY_CHEMISTRY_LITHIUM_ION,
        BATTERY_CHEMISTRY_LITHIUM_ION_POLYMER,
        BATTERY_CHEMISTRY_LITHIUM_ION_IRON_PHOSPHATE,
        BATTERY_CHEMISTRY_LITHIUM_ION_MANGANESE_OXIDE,
};

/* Length of open circuit voltage table */
#define BATTERY_OCV_TABLE_LEN 11

#define BATTERY_CHEMISTRY_DT_GET(node_id)                                                          \
        UTIL_CAT(BATTERY_CHEMISTRY_, DT_STRING_UPPER_TOKEN_OR(node_id, device_chemistry, UNKNOWN))

#define BATTERY_OCV_TABLE_DT_GET(node_id, table)                                                   \
        COND_CODE_1(DT_NODE_HAS_PROP(node_id, table),                                              \
                    ({DT_FOREACH_PROP_ELEM_SEP(node_id, table, DT_PROP_BY_IDX, (,))}), ({-1}))

static inline int32_t battery_soc_lookup(const int32_t ocv_table[BATTERY_OCV_TABLE_LEN],
                                         uint32_t voltage_uv)
{
        static const int32_t soc_axis[BATTERY_OCV_TABLE_LEN] = {
                0, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000};

        /* Convert voltage to SoC */
        return linear_interpolate(ocv_table, soc_axis, BATTERY_OCV_TABLE_LEN, voltage_uv);
}


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_SENSOR_BATTERY_H_ */
```

## 14.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2024 Embeint Inc。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 28 行

电池化学体系枚举（Battery chemistry enumeration）。各值名称必须与 `dts/bindings/battery.yaml` 中的一致。

### 注释 3：原第 41 行

开路电压表（Open circuit voltage table）的长度。

### 注释 4：原第 76 行

将电压转换为荷电状态（State of Charge，SoC）。

### 注释 5：原第 88 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_SENSOR_BATTERY_H_`。

## 14.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2battery_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [zephyr/devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [zephyr/math/interpolation.h](../interpolation_reference/P002_插值头文件参考.md)
- [zephyr/sys/util_macro.h](../util_reference/P004_宏工具头文件参考.md)
- [battery_chemistry](https://docs.zephyrproject.org/latest/doxygen/html/group__battery__apis.html#gaf7ee6b6e85da9f31231cac577428de01)
- [BATTERY_CHEMISTRY_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__battery__apis.html#ggaf7ee6b6e85da9f31231cac577428de01a52bae762c2ef4ca140c1e7f89440b007)
- [BATTERY_CHEMISTRY_NICKEL_CADMIUM](https://docs.zephyrproject.org/latest/doxygen/html/group__battery__apis.html#ggaf7ee6b6e85da9f31231cac577428de01a00f07b177e6246e139b469386064698f)
- [BATTERY_CHEMISTRY_NICKEL_METAL_HYDRIDE](https://docs.zephyrproject.org/latest/doxygen/html/group__battery__apis.html#ggaf7ee6b6e85da9f31231cac577428de01a377834c71930068b6a822d4afd2112f4)
- [BATTERY_CHEMISTRY_LITHIUM_ION](https://docs.zephyrproject.org/latest/doxygen/html/group__battery__apis.html#ggaf7ee6b6e85da9f31231cac577428de01a450162d694da85864af48712cb05badd)
- [BATTERY_CHEMISTRY_LITHIUM_ION_POLYMER](https://docs.zephyrproject.org/latest/doxygen/html/group__battery__apis.html#ggaf7ee6b6e85da9f31231cac577428de01ab21f5e769426047924d83e5301b8a19f)
- [BATTERY_CHEMISTRY_LITHIUM_ION_IRON_PHOSPHATE](https://docs.zephyrproject.org/latest/doxygen/html/group__battery__apis.html#ggaf7ee6b6e85da9f31231cac577428de01a951b3bea1c503ce6f1d78e8cc1ed9e37)
- [BATTERY_CHEMISTRY_LITHIUM_ION_MANGANESE_OXIDE](https://docs.zephyrproject.org/latest/doxygen/html/group__battery__apis.html#ggaf7ee6b6e85da9f31231cac577428de01a30cd5d02bb416248b9380ab953836e96)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [battery_soc_lookup](https://docs.zephyrproject.org/latest/doxygen/html/group__battery__apis.html#gaea81fb0c63b85654005b6f65521c3345)
- [BATTERY_OCV_TABLE_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__battery__apis.html#ga02de0e4f76b8e5804b82cd397c13ef86)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [linear_interpolate](../interpolation_reference/P001_插值公共接口.md#ga8abbb1799796222b39a051819bd19a2a)
- [devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [interpolation.h](../interpolation_reference/P002_插值头文件参考.md)
- [util_macro.h](../util_reference/P004_宏工具头文件参考.md)

---

[上一章](P013_emul.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P015_dsa_tag.h_源码浏览.md)
