---
id: learning.zephyr-docs.api-platform-topic-reference.page-65
title: Cadence MSPI 接口
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__cadence__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第65章\_Cadence MSPI 接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__cadence__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Cadence MSPI 控制器的配置接口。

<a id="details"></a>

Cadence MSPI 控制器的配置接口。

<a id="header-files"></a>
<a id="files"></a>

## 65.1\_文件（Files）

<a id="r_mspi_5Fcadence_2Eh"></a>

```c
file mspi_cadence.h
```

相关声明：[mspi_cadence.h](../peripheral_bus_storage_header_reference/P016_zephyr__drivers__mspi__mspi_cadence.h_头文件参考.md)。

Cadence MSPI控制器的专用定义（Controller Specific Definitions）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 65.2\_数据结构（Data Structures）

<a id="r_mspi_5Fcadence_5Ftiming_5Fcfg"></a>

```c
struct mspi_cadence_timing_cfg
```

相关声明：[mspi_cadence_timing_cfg](../peripheral_bus_storage_model_reference/P036_mspi_cadence_timing_cfg_结构体.md)。

TI K3 MSPI外设的时序配置（Timing Configuration）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 65.3\_枚举（Enumerations）

<a id="r_ga9437f27953847cd2c6e79e5252586d77"></a>

```c
enum mspi_cadence_timing_param { MSPI_CADENCE_TIMING_PARAM_RD_DELAY = BIT(0) }
```

相关声明：[mspi_cadence_timing_param](#ga9437f27953847cd2c6e79e5252586d77)、[MSPI_CADENCE_TIMING_PARAM_RD_DELAY](#gga9437f27953847cd2c6e79e5252586d77adf4828062b1fe820ec5ff5a2093a01ce)。

枚举，指定应修改哪些时序参数（Timing parameters）。

## 65.4\_详细说明（Detailed Documentation）

<a id="ga9437f27953847cd2c6e79e5252586d77"></a>

### `mspi_cadence_timing_param`

```c
enum mspi_cadence_timing_param
```

```c
#include <zephyr/drivers/mspi/mspi_cadence.h>
```

枚举，指定应修改哪些时序参数（Timing parameters）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MSPI_CADENCE_TIMING_PARAM_RD_DELAY` | 读取延迟时序参数（Read Delay Timing Parameter）。 |


## 65.5\_原页交叉引用（Cross References）

- [mspi_cadence.h](../peripheral_bus_storage_header_reference/P016_zephyr__drivers__mspi__mspi_cadence.h_头文件参考.md)
- [mspi_cadence_timing_cfg](../peripheral_bus_storage_model_reference/P036_mspi_cadence_timing_cfg_结构体.md)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga9437f27953847cd2c6e79e5252586d77adf4828062b1fe820ec5ff5a2093a01ce"></a>

---

[上一章](P064_插件（Plugins）.md) · [返回大纲](大纲.md) · [下一章](P066_网络命名空间兼容模式符号（Network namespace compatibility mode symbols）.md)
