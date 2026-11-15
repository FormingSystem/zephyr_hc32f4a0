---
id: learning.zephyr-docs.api-extension-topic-reference.page-31
title: MCUX 增强型正交解码器（EQDC MCUX）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__eqdc__mcux.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第31章\_MCUX 增强型正交解码器（EQDC MCUX）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__eqdc__mcux.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

NXP MCUX 增强型正交解码器（EQDC）传感器。

<a id="details"></a>

NXP MCUX 增强型正交解码器（EQDC）传感器。

<a id="header-files"></a>
<a id="files"></a>

## 31.1\_文件（Files）

<a id="r_eqdc_5Fmcux_2Eh"></a>

```c
file eqdc_mcux.h
```

相关声明：[eqdc_mcux.h](../api_file_supplement_reference/P026_zephyr__drivers__sensor__eqdc_mcux.h_文件参考.md)。

NXP MCUX EQDC传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 31.2\_枚举（Enumerations）

<a id="r_gadcc2ad717337d60cb4fc30950b098481"></a>

```c
enum sensor_attribute_eqdc_mcux { SENSOR_ATTR_EQDC_COUNTS_PER_REVOLUTION = SENSOR_ATTR_PRIV_START , SENSOR_ATTR_EQDC_PRESCALED_FREQUENCY }
```

相关声明：[sensor_attribute_eqdc_mcux](#gadcc2ad717337d60cb4fc30950b098481)、[SENSOR_ATTR_EQDC_COUNTS_PER_REVOLUTION](#ggadcc2ad717337d60cb4fc30950b098481ac90210723198bb8db0b0d5000bb3ce95)、[SENSOR_ATTR_EQDC_PRESCALED_FREQUENCY](#ggadcc2ad717337d60cb4fc30950b098481a38fef6ef89d7c82444be247744fa9a1d)。

NXP MCUX EQDC 的扩展传感器属性（Extended Sensor Attributes）。

## 31.3\_详细说明（Detailed Documentation）

<a id="gadcc2ad717337d60cb4fc30950b098481"></a>

### `sensor_attribute_eqdc_mcux`

```c
enum sensor_attribute_eqdc_mcux
```

```c
#include <zephyr/drivers/sensor/eqdc_mcux.h>
```

NXP MCUX EQDC 的扩展传感器属性（Extended Sensor Attributes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_ATTR_EQDC_COUNTS_PER_REVOLUTION` | 每转计数（Counts per Revolution），类型为 `uint32_t`。 |
| `SENSOR_ATTR_EQDC_PRESCALED_FREQUENCY` | 预分频后的 EQDC 模块时钟频率（Clock Frequency），类型为 `uint32_t`。 |


## 31.4\_原页交叉引用（Cross References）

- [eqdc_mcux.h](../api_file_supplement_reference/P026_zephyr__drivers__sensor__eqdc_mcux.h_文件参考.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggadcc2ad717337d60cb4fc30950b098481ac90210723198bb8db0b0d5000bb3ce95"></a>
<a id="ggadcc2ad717337d60cb4fc30950b098481a38fef6ef89d7c82444be247744fa9a1d"></a>

---

[上一章](P030_传输（Transport）.md) · [返回大纲](大纲.md) · [下一章](P032_SGP40 API主题.md)
