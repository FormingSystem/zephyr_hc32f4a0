---
id: learning.zephyr-docs.api-protocol-topic-reference.page-29
title: MFD BD8LB600FS 接口
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__bd8lb600fs.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第29章\_MFD BD8LB600FS 接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__bd8lb600fs.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-func-members"></a>
<a id="func-members"></a>

## 29.1\_函数（Functions）

<a id="r_gaf155a458b77540f991d53c0827fad5cd"></a>

```c
int mfd_bd8lb600fs_set_outputs (const struct device *dev, uint32_t values)
```

相关声明：[mfd_bd8lb600fs_set_outputs](#gaf155a458b77540f991d53c0827fad5cd)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置输出（Outputs）。

<a id="r_ga478f99d83f78a0ec0fcabeb3103df015"></a>

```c
int mfd_bd8lb600fs_get_output_diagnostics (const struct device *dev, uint32_t *old, uint32_t *ocp_or_tsd)
```

相关声明：[mfd_bd8lb600fs_get_output_diagnostics](#ga478f99d83f78a0ec0fcabeb3103df015)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取输出诊断信息（Output Diagnostics）。

## 29.2\_详细说明（Detailed Documentation）

<a id="ga478f99d83f78a0ec0fcabeb3103df015"></a>

### `mfd_bd8lb600fs_get_output_diagnostics()`

```c
int mfd_bd8lb600fs_get_output_diagnostics ( const struct device * dev, uint32_t * old, uint32_t * ocp_or_tsd )
```

```c
#include <zephyr/drivers/mfd/bd8lb600fs.h>
```

获取输出诊断信息（Output Diagnostics）。

获取所有实例的当前诊断信息，因为多个实例可能采用菊花链（daisy chain）连接。`old` 和 `ocp_or_tsd` 中的每一位对应一个输出。位被置位表示相应功能处于活动状态，即存在负载开路、过流或温度过高。

`OLD`：负载开路（open load）；`OCP`：过流保护（over current protection）；`TSD`：过热关断（thermal shutdown）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | BD8LB600FS 多功能设备（MFD）实例。 |
| `[out] old` | 负载开路（open load）值。 |
| `[out] ocp_or_tsd` | 过流保护（over current protection）或过热关断（thermal shutdown）值。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |

<a id="gaf155a458b77540f991d53c0827fad5cd"></a>

### `mfd_bd8lb600fs_set_outputs()`

```c
int mfd_bd8lb600fs_set_outputs ( const struct device * dev, uint32_t values )
```

```c
#include <zephyr/drivers/mfd/bd8lb600fs.h>
```

设置输出（Outputs）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | BD8LB600FS 多功能设备（MFD）实例。 |
| `[in] values` | 各输出的值，每个输出对应一位。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |


## 29.3\_原页交叉引用（Cross References）

- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [zephyr/drivers/mfd/bd8lb600fs.h](../api_file_configuration_reference/P052_zephyr__drivers__mfd__bd8lb600fs.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P028_枚举管理（Enumeration Management）.md) · [返回大纲](大纲.md) · [下一章](P030_MEMC 驱动后端 API.md)
