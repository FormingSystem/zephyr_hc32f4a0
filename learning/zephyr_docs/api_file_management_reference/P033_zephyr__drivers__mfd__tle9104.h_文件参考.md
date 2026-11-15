---
id: learning.zephyr-docs.api-file-management-reference.page-33
title: zephyr__drivers__mfd__tle9104.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mfd_2tle9104_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第33章\_zephyr\_\_drivers\_\_mfd\_\_tle9104.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mfd_2tle9104_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stdbool.h>
#include <zephyr/device.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 33.1\_数据结构（Data Structures）

<a id="r_gpio_5Ftle9104_5Fchannel_5Fdiagnostics"></a>

```c
struct gpio_tle9104_channel_diagnostics
```

相关声明：[gpio_tle9104_channel_diagnostics](../device_power_control_model_reference/P016_gpio_tle9104_channel_diagnostics_结构体.md)。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 33.2\_宏定义（Macros）

<a id="r_a3f6f8709aa1b46781268154e34c298a9"></a>

```c
#define TLE9104_GPIO_COUNT 4
```

相关声明：[TLE9104_GPIO_COUNT](#a3f6f8709aa1b46781268154e34c298a9)。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 33.3\_枚举（Enumerations）

<a id="r_aa40748ba46d1bc413f8bf3caa5d7b4b0"></a>

```c
enum tle9104_on_state_diagnostics { TLE9104_ONDIAG_OT = 5 , TLE9104_ONDIAG_OCTIME = 4 , TLE9104_ONDIAG_OCOT = 3 , TLE9104_ONDIAG_SCB = 2 , TLE9104_ONDIAG_NOFAIL = 1 , TLE9104_ONDIAG_UNKNOWN = 0 }
```

相关声明：[tle9104_on_state_diagnostics](#aa40748ba46d1bc413f8bf3caa5d7b4b0)、[TLE9104_ONDIAG_OT](#aa40748ba46d1bc413f8bf3caa5d7b4b0a359b0a412ecb9de36e12a50946dc2173)、[TLE9104_ONDIAG_OCTIME](#aa40748ba46d1bc413f8bf3caa5d7b4b0a36e248aad4b5b47c338589d86f4e2925)、[TLE9104_ONDIAG_OCOT](#aa40748ba46d1bc413f8bf3caa5d7b4b0a7cea6cba428b062f1951809d12e15685)、[TLE9104_ONDIAG_SCB](#aa40748ba46d1bc413f8bf3caa5d7b4b0a9d82a99fcc6ea7017e38959d5e299f4c)、[TLE9104_ONDIAG_NOFAIL](#aa40748ba46d1bc413f8bf3caa5d7b4b0a7aace824362e7c51841585b9f3a64ca4)、[TLE9104_ONDIAG_UNKNOWN](#aa40748ba46d1bc413f8bf3caa5d7b4b0addb7f997401544e59dc6a181c1341679)。

<a id="r_acd342488b1a9b0e2b4a0e79a1441d8e3"></a>

```c
enum tle9104_off_state_diagnostics { TLE9104_OFFDIAG_SCG = 3 , TLE9104_OFFDIAG_OL = 2 , TLE9104_OFFDIAG_NOFAIL = 1 , TLE9104_OFFDIAG_UNKNOWN = 0 }
```

相关声明：[tle9104_off_state_diagnostics](#acd342488b1a9b0e2b4a0e79a1441d8e3)、[TLE9104_OFFDIAG_SCG](#acd342488b1a9b0e2b4a0e79a1441d8e3abc547081143f840a6261d807fa72284e)、[TLE9104_OFFDIAG_OL](#acd342488b1a9b0e2b4a0e79a1441d8e3ac37a0b72b862d7279572eaf960e5507d)、[TLE9104_OFFDIAG_NOFAIL](#acd342488b1a9b0e2b4a0e79a1441d8e3a2dfab15a18c96bcbe413a4ed94da6af7)、[TLE9104_OFFDIAG_UNKNOWN](#acd342488b1a9b0e2b4a0e79a1441d8e3ad16bbd2e028e21957316609bda7f8393)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 33.4\_函数（Functions）

<a id="r_a3fbd8b8e3cdf6998990d055a6e503361"></a>

```c
int tle9104_get_diagnostics (const struct device *dev, struct gpio_tle9104_channel_diagnostics diag[4])
```

相关声明：[tle9104_get_diagnostics](#a3fbd8b8e3cdf6998990d055a6e503361)、[device](../device_reference/P002_设备对象结构.md)、[gpio_tle9104_channel_diagnostics](../device_power_control_model_reference/P016_gpio_tle9104_channel_diagnostics_结构体.md)。

获取各输出的诊断信息（diagnostics）。

<a id="r_a1c4925c222bbdd94c0fe1eb295244ec3"></a>

```c
int tle9104_clear_diagnostics (const struct device *dev)
```

相关声明：[tle9104_clear_diagnostics](#a1c4925c222bbdd94c0fe1eb295244ec3)、[device](../device_reference/P002_设备对象结构.md)。

清除各输出的诊断信息。

<a id="r_a5febfb7f1b4fd5859bf503e9ff4c2ed4"></a>

```c
int tle9104_write_state (const struct device *dev, uint8_t state)
```

相关声明：[tle9104_write_state](#a5febfb7f1b4fd5859bf503e9ff4c2ed4)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

写入输出状态（output state）。

## 33.5\_详细说明（Detailed Documentation）

<a id="a3f6f8709aa1b46781268154e34c298a9"></a>

### `TLE9104_GPIO_COUNT`

```c
#define TLE9104_GPIO_COUNT 4
```

<a id="acd342488b1a9b0e2b4a0e79a1441d8e3"></a>

### `tle9104_off_state_diagnostics`

```c
enum tle9104_off_state_diagnostics
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `TLE9104_OFFDIAG_SCG` |  |
| `TLE9104_OFFDIAG_OL` |  |
| `TLE9104_OFFDIAG_NOFAIL` |  |
| `TLE9104_OFFDIAG_UNKNOWN` |  |

<a id="aa40748ba46d1bc413f8bf3caa5d7b4b0"></a>

### `tle9104_on_state_diagnostics`

```c
enum tle9104_on_state_diagnostics
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `TLE9104_ONDIAG_OT` |  |
| `TLE9104_ONDIAG_OCTIME` |  |
| `TLE9104_ONDIAG_OCOT` |  |
| `TLE9104_ONDIAG_SCB` |  |
| `TLE9104_ONDIAG_NOFAIL` |  |
| `TLE9104_ONDIAG_UNKNOWN` |  |

<a id="a1c4925c222bbdd94c0fe1eb295244ec3"></a>

### `tle9104_clear_diagnostics()`

```c
int tle9104_clear_diagnostics ( const struct device * dev)
```

清除各输出的诊断信息。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | TLE9104 实例。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |

<a id="a3fbd8b8e3cdf6998990d055a6e503361"></a>

### `tle9104_get_diagnostics()`

```c
int tle9104_get_diagnostics ( const struct device * dev, struct gpio_tle9104_channel_diagnostics diag[4] )
```

获取各输出的诊断信息（diagnostics）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | TLE9104 实例。 |
| `diag` | 写入结果的目标位置。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |

<a id="a5febfb7f1b4fd5859bf503e9ff4c2ed4"></a>

### `tle9104_write_state()`

```c
int tle9104_write_state ( const struct device * dev, uint8_t state )
```

写入输出状态（output state）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | TLE9104 实例。 |
| `state` | 输出状态，每一位代表一个输出。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |


## 33.6\_原页交叉引用（Cross References）

- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_compiler_device_reference/P017_tle9104.h_源码浏览.md)
- [gpio_tle9104_channel_diagnostics](../device_power_control_model_reference/P016_gpio_tle9104_channel_diagnostics_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="acd342488b1a9b0e2b4a0e79a1441d8e3abc547081143f840a6261d807fa72284e"></a>
<a id="acd342488b1a9b0e2b4a0e79a1441d8e3ac37a0b72b862d7279572eaf960e5507d"></a>
<a id="acd342488b1a9b0e2b4a0e79a1441d8e3a2dfab15a18c96bcbe413a4ed94da6af7"></a>
<a id="acd342488b1a9b0e2b4a0e79a1441d8e3ad16bbd2e028e21957316609bda7f8393"></a>
<a id="aa40748ba46d1bc413f8bf3caa5d7b4b0a359b0a412ecb9de36e12a50946dc2173"></a>
<a id="aa40748ba46d1bc413f8bf3caa5d7b4b0a36e248aad4b5b47c338589d86f4e2925"></a>
<a id="aa40748ba46d1bc413f8bf3caa5d7b4b0a7cea6cba428b062f1951809d12e15685"></a>
<a id="aa40748ba46d1bc413f8bf3caa5d7b4b0a9d82a99fcc6ea7017e38959d5e299f4c"></a>
<a id="aa40748ba46d1bc413f8bf3caa5d7b4b0a7aace824362e7c51841585b9f3a64ca4"></a>
<a id="aa40748ba46d1bc413f8bf3caa5d7b4b0addb7f997401544e59dc6a181c1341679"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P032_zephyr__drivers__clock_control__mchp_clock_sam_d5x_e5x.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P034_zephyr__drivers__mm__mm_drv_bank.h_文件参考.md)
