---
id: learning.zephyr-docs.api-topic-reference.page-53
title: MSPI 工具（Mspi_util）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__util.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第53章\_MSPI 工具（Mspi\_util）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__util.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-define-members"></a>
<a id="define-members"></a>

## 53.1\_宏定义（Macros）

<a id="r_gadce17ebaa26cfd2b59fadab2a7b2a788"></a>

```c
#define MSPI_MEMMAP_CFG_STRUCT_DECLARE(_name)
```

相关声明：[MSPI_MEMMAP_CFG_STRUCT_DECLARE](#gadce17ebaa26cfd2b59fadab2a7b2a788)。

在外设驱动中声明可选的内存映射配置（Memory map configuration）。

<a id="r_gae9b12392a7cc1f6b746adddec56e0b85"></a>

```c
#define MSPI_MEMMAP_BASE_ADDR_DECLARE(_name)
```

相关声明：[MSPI_MEMMAP_BASE_ADDR_DECLARE](#gae9b12392a7cc1f6b746adddec56e0b85)。

在外设驱动中声明可选的内存映射基地址。

<a id="r_ga8c55eacfe36f484bb5b3f82f8918aa79"></a>

```c
#define MSPI_SCRAMBLE_CFG_STRUCT_DECLARE(_name)
```

相关声明：[MSPI_SCRAMBLE_CFG_STRUCT_DECLARE](#ga8c55eacfe36f484bb5b3f82f8918aa79)。

在外设驱动中声明可选的扰码配置（Scramble configuration）。

<a id="r_ga118cb8d67bde11040aa8369ff88e4b6b"></a>

```c
#define MSPI_TIMING_CFG_STRUCT_DECLARE(_name)
```

相关声明：[MSPI_TIMING_CFG_STRUCT_DECLARE](#ga118cb8d67bde11040aa8369ff88e4b6b)。

在外设驱动中声明可选的时序配置（Timing configuration）。

<a id="r_ga4c88adce60d915c85972fa2cfaf7177e"></a>

```c
#define MSPI_TIMING_PARAM_DECLARE(_name)
```

相关声明：[MSPI_TIMING_PARAM_DECLARE](#ga4c88adce60d915c85972fa2cfaf7177e)。

在外设驱动中声明可选的时序参数。

<a id="r_ga7b2c02a81ae6d670680b86088624dc17"></a>

```c
#define MSPI_OPTIONAL_CFG_STRUCT_INIT(code, _name, _object)
```

相关声明：[MSPI_OPTIONAL_CFG_STRUCT_INIT](#ga7b2c02a81ae6d670680b86088624dc17)。

初始化外设驱动中的可选配置结构体。

<a id="r_ga2da665f679f0c538e58ebff4005daec3"></a>

```c
#define MSPI_MEMMAP_BASE_ADDR_INIT(_name, _bus)
```

相关声明：[MSPI_MEMMAP_BASE_ADDR_INIT](#ga2da665f679f0c538e58ebff4005daec3)。

初始化外设驱动中的可选内存映射基地址。

## 53.2\_详细说明（Detailed Documentation）

<a id="gae9b12392a7cc1f6b746adddec56e0b85"></a>

### `MSPI_MEMMAP_BASE_ADDR_DECLARE`

```c
#define MSPI_MEMMAP_BASE_ADDR_DECLARE ( _name)
```

```c
#include <zephyr/drivers/mspi.h>
```

展开值（Value）：

```c
IF_ENABLED(CONFIG_MSPI_MEMMAP, (uint32_t _name;))
```

在外设驱动中声明可选的内存映射基地址。

<a id="ga2da665f679f0c538e58ebff4005daec3"></a>

### `MSPI_MEMMAP_BASE_ADDR_INIT`

```c
#define MSPI_MEMMAP_BASE_ADDR_INIT ( _name, _bus )
```

```c
#include <zephyr/drivers/mspi.h>
```

展开值（Value）：

```c
IF_ENABLED(CONFIG_MSPI_MEMMAP, (._name = DT_REG_ADDR_BY_IDX(_bus, 1),))
```

初始化外设驱动中的可选内存映射基地址。

<a id="gadce17ebaa26cfd2b59fadab2a7b2a788"></a>

### `MSPI_MEMMAP_CFG_STRUCT_DECLARE`

```c
#define MSPI_MEMMAP_CFG_STRUCT_DECLARE ( _name)
```

```c
#include <zephyr/drivers/mspi.h>
```

展开值（Value）：

```c
IF_ENABLED(CONFIG_MSPI_MEMMAP, (struct mspi_memmap_cfg _name;))
```

在外设驱动中声明可选的内存映射配置（Memory map configuration）。

<a id="ga7b2c02a81ae6d670680b86088624dc17"></a>

### `MSPI_OPTIONAL_CFG_STRUCT_INIT`

```c
#define MSPI_OPTIONAL_CFG_STRUCT_INIT ( code, _name, _object )
```

```c
#include <zephyr/drivers/mspi.h>
```

展开值（Value）：

```c
IF_ENABLED(code, (._name = _object,))
```

初始化外设驱动中的可选配置结构体。

<a id="ga8c55eacfe36f484bb5b3f82f8918aa79"></a>

### `MSPI_SCRAMBLE_CFG_STRUCT_DECLARE`

```c
#define MSPI_SCRAMBLE_CFG_STRUCT_DECLARE ( _name)
```

```c
#include <zephyr/drivers/mspi.h>
```

展开值（Value）：

```c
IF_ENABLED(CONFIG_MSPI_SCRAMBLE, (struct mspi_scramble_cfg _name;))
```

在外设驱动中声明可选的扰码配置（Scramble configuration）。

<a id="ga118cb8d67bde11040aa8369ff88e4b6b"></a>

### `MSPI_TIMING_CFG_STRUCT_DECLARE`

```c
#define MSPI_TIMING_CFG_STRUCT_DECLARE ( _name)
```

```c
#include <zephyr/drivers/mspi.h>
```

展开值（Value）：

```c
IF_ENABLED(CONFIG_MSPI_TIMING, (mspi_timing_cfg _name;))
```

在外设驱动中声明可选的时序配置（Timing configuration）。

<a id="ga4c88adce60d915c85972fa2cfaf7177e"></a>

### `MSPI_TIMING_PARAM_DECLARE`

```c
#define MSPI_TIMING_PARAM_DECLARE ( _name)
```

```c
#include <zephyr/drivers/mspi.h>
```

展开值（Value）：

```c
IF_ENABLED(CONFIG_MSPI_TIMING, (mspi_timing_param _name;))
```

在外设驱动中声明可选的时序参数。


## 53.3\_原页交叉引用（Cross References）

- [zephyr/drivers/mspi.h](../peripheral_bus_storage_header_reference/P017_zephyr__drivers__mspi.h_头文件参考.md)
- [IF_ENABLED](../util_reference/P001_通用工具公共接口.md#gae67ffe50e848951dbde309ed569ea925)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [DT_REG_ADDR_BY_IDX](../dt_reg_reference/P001_设备树寄存器属性宏.md#gac540b00bb12d0662f6aefe6ac0cff243)
- [mspi_memmap_cfg](../peripheral_bus_storage_model_reference/P047_mspi_memmap_cfg_结构体.md)
- [mspi_scramble_cfg](../peripheral_bus_storage_model_reference/P048_mspi_scramble_cfg_结构体.md)
- [mspi_timing_cfg](../peripheral_bus_storage_model_reference/P049_mspi_timing_cfg_结构体.md)
- [mspi_timing_param](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__configure__api.html#gaa25a7f97ab3437d4544832a0e7474f4a)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__sys-util_html_gae67ffe50e848951dbde309ed569ea925"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="agroup__devicetree-reg-prop_html_gac540b00bb12d0662f6aefe6ac0cff243"></a>
<a id="astructmspi__memmap__cfg_html"></a>
<a id="astructmspi__scramble__cfg_html"></a>
<a id="astructmspi__timing__cfg_html"></a>
<a id="agroup__mspi__configure__api_html_gaa25a7f97ab3437d4544832a0e7474f4a"></a>

---

[上一章](P052_其他设备（Miscellaneous Devices）.md) · [返回大纲](大纲.md) · [下一章](P054_多媒体（Multimedia）.md)
