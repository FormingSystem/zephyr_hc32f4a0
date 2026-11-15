---
id: learning.zephyr-docs.api-bridge-paging-topic-reference.page-13
title: MSPI 配置 API（MSPI Configure API）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__configure__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_MSPI 配置 API（MSPI Configure API）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__configure__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MSPI 配置 API（MSPI Configure API）

<a id="details"></a>

MSPI 配置 API（MSPI Configure API）

<a id="header-groups"></a>
<a id="groups"></a>

## 13.1\_主题（Topics）

<a id="r_mspi_5Fcadence_5Finterface"></a>

相关声明：[Cadence MSPI 接口](../api_platform_topic_reference/P065_Cadence MSPI 接口.md)。

Cadence MSPI 控制器的配置接口。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 13.2\_数据结构（Data Structures）

<a id="r_mspi_5Ftiming_5Fcfg"></a>

```c
struct mspi_timing_cfg
```

相关声明：[mspi_timing_cfg](../peripheral_bus_storage_model_reference/P049_mspi_timing_cfg_结构体.md)。

struct timing_cfg的占位结构（Stub）。

<a id="r_mspi_5Fdev_5Fid"></a>

```c
struct mspi_dev_id
```

相关声明：[mspi_dev_id](../peripheral_bus_storage_model_reference/P041_mspi_dev_id_结构体.md)。

MSPI设备标识（Device ID）。在多设备方案中，控制器可据此识别其设备，并判断是否允许访问。

<a id="r_mspi_5Fcfg"></a>

```c
struct mspi_cfg
```

相关声明：[mspi_cfg](../peripheral_bus_storage_model_reference/P039_mspi_cfg_结构体.md)。

MSPI控制器配置（Controller Configuration）。

<a id="r_mspi_5Fdt_5Fspec"></a>

```c
struct mspi_dt_spec
```

相关声明：[mspi_dt_spec](../peripheral_bus_storage_model_reference/P043_mspi_dt_spec_结构体.md)。

MSPI设备树（DT）信息。

<a id="r_mspi_5Fdev_5Fcfg"></a>

```c
struct mspi_dev_cfg
```

相关声明：[mspi_dev_cfg](../peripheral_bus_storage_model_reference/P040_mspi_dev_cfg_结构体.md)。

MSPI控制器设备专用配置（Device Specific Configuration）。

<a id="r_mspi_5Fmemmap_5Fcfg"></a>

```c
struct mspi_memmap_cfg
```

相关声明：[mspi_memmap_cfg](../peripheral_bus_storage_model_reference/P047_mspi_memmap_cfg_结构体.md)。

MSPI控制器的内存映射配置（Memory Map Configuration）。

<a id="r_mspi_5Fscramble_5Fcfg"></a>

```c
struct mspi_scramble_cfg
```

相关声明：[mspi_scramble_cfg](../peripheral_bus_storage_model_reference/P048_mspi_scramble_cfg_结构体.md)。

MSPI控制器的扰码配置（Scramble Configuration）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 13.3\_枚举（Enumerations）

<a id="r_gaa25a7f97ab3437d4544832a0e7474f4a"></a>

```c
enum mspi_timing_param { MSPI_TIMING_PARAM_DUMMY }
```

相关声明：[mspi_timing_param](#gaa25a7f97ab3437d4544832a0e7474f4a)、[MSPI_TIMING_PARAM_DUMMY](#ggaa25a7f97ab3437d4544832a0e7474f4aafae0ccedcd3b8f05e798037bf5414237)。

时序参数的占位项（Stub）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 13.4\_函数（Functions）

<a id="r_ga46c2b98e99ecea045c1ecac4bdf3f087"></a>

```c
int mspi_config (const struct mspi_dt_spec *spec)
```

相关声明：[mspi_config](#ga46c2b98e99ecea045c1ecac4bdf3f087)、[mspi_dt_spec](../peripheral_bus_storage_model_reference/P043_mspi_dt_spec_结构体.md)。

配置 MSPI 控制器。

<a id="r_gaa3c1eae8b3000c9bafcc26f14a8beb8b"></a>

```c
int mspi_dev_config (const struct device *controller, const struct mspi_dev_id *dev_id, const enum mspi_dev_cfg_mask param_mask, const struct mspi_dev_cfg *cfg)
```

相关声明：[mspi_dev_config](#gaa3c1eae8b3000c9bafcc26f14a8beb8b)、[device](../device_reference/P002_设备对象结构.md)、[mspi_dev_id](../peripheral_bus_storage_model_reference/P041_mspi_dev_id_结构体.md)、[mspi_dev_cfg_mask](../api_auxiliary_topic_reference/P014_多位串行外设接口（MSPI）.md#ga71c447d059acf7a8055c380243f3a647)、[mspi_dev_cfg](../peripheral_bus_storage_model_reference/P040_mspi_dev_cfg_结构体.md)。

使用设备特定参数配置 MSPI 控制器。

<a id="r_ga957b6ecd96c9f942f75bbe500898930d"></a>

```c
int mspi_get_channel_status (const struct device *controller, uint8_t ch)
```

相关声明：[mspi_get_channel_status](#ga957b6ecd96c9f942f75bbe500898930d)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

查询通道是否就绪。

<a id="r_gac025129882f814b59d5726c01f0138ce"></a>

```c
int mspi_memmap_config (const struct device *controller, const struct mspi_dev_id *dev_id, const struct mspi_memmap_cfg *cfg)
```

相关声明：[mspi_memmap_config](#gac025129882f814b59d5726c01f0138ce)、[device](../device_reference/P002_设备对象结构.md)、[mspi_dev_id](../peripheral_bus_storage_model_reference/P041_mspi_dev_id_结构体.md)、[mspi_memmap_cfg](../peripheral_bus_storage_model_reference/P047_mspi_memmap_cfg_结构体.md)。

配置 MSPI 内存映射（Memory map）设置。

<a id="r_gacf287e08b6ce4898524884e8de22b806"></a>

```c
int mspi_scramble_config (const struct device *controller, const struct mspi_dev_id *dev_id, const struct mspi_scramble_cfg *cfg)
```

相关声明：[mspi_scramble_config](#gacf287e08b6ce4898524884e8de22b806)、[device](../device_reference/P002_设备对象结构.md)、[mspi_dev_id](../peripheral_bus_storage_model_reference/P041_mspi_dev_id_结构体.md)、[mspi_scramble_cfg](../peripheral_bus_storage_model_reference/P048_mspi_scramble_cfg_结构体.md)。

配置 MSPI 扰码（Scrambling）设置。

<a id="r_gaff82af1cfc99b9e78cec17ea27f79ab6"></a>

```c
int mspi_timing_config (const struct device *controller, const struct mspi_dev_id *dev_id, const uint32_t param_mask, void *cfg)
```

相关声明：[mspi_timing_config](#gaff82af1cfc99b9e78cec17ea27f79ab6)、[device](../device_reference/P002_设备对象结构.md)、[mspi_dev_id](../peripheral_bus_storage_model_reference/P041_mspi_dev_id_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

配置 MSPI 时序（Timing）设置。

## 13.5\_详细说明（Detailed Documentation）

<a id="gaa25a7f97ab3437d4544832a0e7474f4a"></a>

### `mspi_timing_param`

```c
enum mspi_timing_param
```

```c
#include <zephyr/drivers/mspi.h>
```

时序参数的占位项（Stub）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MSPI_TIMING_PARAM_DUMMY` |  |

<a id="ga46c2b98e99ecea045c1ecac4bdf3f087"></a>

### `mspi_config()`

```c
int mspi_config ( const struct mspi_dt_spec * spec)
```

```c
#include <zephyr/drivers/mspi.h>
```

配置 MSPI 控制器。

此例程提供通用接口，用于覆盖 MSPI 控制器能力（Controller Capabilities）。

在控制器驱动中，可以实现此 API 来初始化或重新初始化控制器硬件。对于 `struct mspi_cfg` 未包含的其他 SoC 平台特定设置，可将其加入自定义绑定（Binding）`xxx,mspi-controller.yaml`，以便从设备树源码（DTS）提取设置并在此 API 中完成配置。通常这些设置不应在运行时变化。相关绑定请参见下述说明。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `spec` | 指向 MSPI 设备树（DT）信息的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EIO` | 一般输入／输出错误（General I/O Error），无法配置设备。 |
| `-EINVAL` | 能力（Capabilities）无效，无法配置设备。 |
| `-ENOTSUP` | MSPI 外设（Peripheral）不支持该能力。 |

**参阅（See Also）**：另请参见：`mspi_cfg` 的绑定位于 `mspi-controller.yaml`。

<a id="gaa3c1eae8b3000c9bafcc26f14a8beb8b"></a>

### `mspi_dev_config()`

```c
int mspi_dev_config ( const struct device * controller, const struct mspi_dev_id * dev_id, const enum mspi_dev_cfg_mask param_mask, const struct mspi_dev_cfg * cfg )
```

```c
#include <zephyr/drivers/mspi.h>
```

使用设备特定参数配置 MSPI 控制器。

此例程提供通用接口，用于覆盖 MSPI 控制器的设备专用设置（Device-specific Settings）；这些设置应从设备数据手册中获取。

结合下述标识使用（With）：

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `controller` | 指向驱动实例的设备结构（Device Structure）。 |
| `dev_id` | 指向设备的设备 ID 结构体的指针。 |
| `param_mask` | 指定要配置 `cfg` 中哪些内容的宏定义（Macro Definition）。 |
| `cfg` | MSPI 控制器的设备运行时配置（Device Runtime Configuration）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EIO` | 一般输入／输出错误（General I/O Error），无法配置设备。 |
| `-EINVAL` | 能力（Capabilities）无效，无法配置设备。 |
| `-ENOTSUP` | MSPI 外设（Peripheral）不支持该能力。 |

**参阅（See Also）**：另请参见：`mspi_dev_id` 由设备树中的设备索引（Device Index）和 CE GPIO 定义，因此此 API 支持在同一控制器实例上连接多个设备。是否通过软件或硬件支持设备切换（Device Switching），或者完全不支持切换，由控制器驱动实现决定。如果采用软件切换，应在此 API 的实现中执行。实现也可以支持通过 `mspi_dev_cfg_mask` 指定的单独参数配置。设备初始化并确定工作模式后，`mspi_dev_cfg` 中的设置通常不再改变。`mspi_dev_cfg` 的绑定位于 `mspi-device.yaml`。

<a id="ga957b6ecd96c9f942f75bbe500898930d"></a>

### `mspi_get_channel_status()`

```c
int mspi_get_channel_status ( const struct device * controller, uint8_t ch )
```

```c
#include <zephyr/drivers/mspi.h>
```

查询通道是否就绪。

此例程允许在使用逻辑通道（Logical Channel）前检查其是否就绪。注意：查询不受支持的通道时始终返回 `false`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `controller` | 指向驱动实例的设备结构（Device Structure）。 |
| `ch` | 要获取其状态的 MSPI 通道（Channel）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | MSPI 通道已就绪（Ready）时。 |

<a id="gac025129882f814b59d5726c01f0138ce"></a>

### `mspi_memmap_config()`

```c
int mspi_memmap_config ( const struct device * controller, const struct mspi_dev_id * dev_id, const struct mspi_memmap_cfg * cfg )
```

```c
#include <zephyr/drivers/mspi.h>
```

配置 MSPI 内存映射（Memory map）设置。

此例程提供通用接口，用于配置内存映射功能（Memory Map Feature）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `controller` | 指向驱动实例的设备结构（Device Structure）。 |
| `dev_id` | 指向设备的设备 ID 结构体的指针。 |
| `cfg` | MSPI 控制器的内存映射配置（Memory Map Configuration）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EIO` | 一般输入／输出错误（General I/O Error），无法配置设备。 |
| `-EINVAL` | 能力（Capabilities）无效，无法配置设备。 |
| `-ENOTSUP` | MSPI 外设（Peripheral）不支持该能力。 |

<a id="gacf287e08b6ce4898524884e8de22b806"></a>

### `mspi_scramble_config()`

```c
int mspi_scramble_config ( const struct device * controller, const struct mspi_dev_id * dev_id, const struct mspi_scramble_cfg * cfg )
```

```c
#include <zephyr/drivers/mspi.h>
```

配置 MSPI 扰码（Scrambling）设置。

此例程提供通用接口，用于配置扰码功能（Scrambling Feature）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `controller` | 指向驱动实例的设备结构（Device Structure）。 |
| `dev_id` | 指向设备的设备 ID 结构体的指针。 |
| `cfg` | MSPI 控制器的扰码配置（Scramble Configuration）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EIO` | 一般输入／输出错误（General I/O Error），无法配置设备。 |
| `-EINVAL` | 能力（Capabilities）无效，无法配置设备。 |
| `-ENOTSUP` | MSPI 外设（Peripheral）不支持该能力。 |

<a id="gaff82af1cfc99b9e78cec17ea27f79ab6"></a>

### `mspi_timing_config()`

```c
int mspi_timing_config ( const struct device * controller, const struct mspi_dev_id * dev_id, const uint32_t param_mask, void * cfg )
```

```c
#include <zephyr/drivers/mspi.h>
```

配置 MSPI 时序（Timing）设置。

此例程提供通用接口，用于在必要时配置 MSPI 控制器时序（Timing）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `controller` | 指向驱动实例的设备结构（Device Structure）。 |
| `dev_id` | 指向设备的设备 ID 结构体的指针。 |
| `param_mask` | 指定要配置 `cfg` 中哪些内容的宏定义（Macro Definition）。 |
| `cfg` | MSPI 控制器的时序配置（Timing Configuration）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EIO` | 一般输入／输出错误（General I/O Error），无法配置设备。 |
| `-EINVAL` | 能力（Capabilities）无效，无法配置设备。 |
| `-ENOTSUP` | MSPI 外设（Peripheral）不支持该能力。 |


## 13.6\_原页交叉引用（Cross References）

- [Cadence MSPI 接口](../api_platform_topic_reference/P065_Cadence MSPI 接口.md)
- [mspi_timing_cfg](../peripheral_bus_storage_model_reference/P049_mspi_timing_cfg_结构体.md)
- [mspi_dev_id](../peripheral_bus_storage_model_reference/P041_mspi_dev_id_结构体.md)
- [mspi_cfg](../peripheral_bus_storage_model_reference/P039_mspi_cfg_结构体.md)
- [mspi_dt_spec](../peripheral_bus_storage_model_reference/P043_mspi_dt_spec_结构体.md)
- [mspi_dev_cfg](../peripheral_bus_storage_model_reference/P040_mspi_dev_cfg_结构体.md)
- [mspi_memmap_cfg](../peripheral_bus_storage_model_reference/P047_mspi_memmap_cfg_结构体.md)
- [mspi_scramble_cfg](../peripheral_bus_storage_model_reference/P048_mspi_scramble_cfg_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [mspi_dev_cfg_mask](../api_auxiliary_topic_reference/P014_多位串行外设接口（MSPI）.md#ga71c447d059acf7a8055c380243f3a647)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [zephyr/drivers/mspi.h](../peripheral_bus_storage_header_reference/P017_zephyr__drivers__mspi.h_头文件参考.md)
- [设置（Settings）。](../storage/P063_设置子系统接口.md)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggaa25a7f97ab3437d4544832a0e7474f4aafae0ccedcd3b8f05e798037bf5414237"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P012_应用源（Application sources）.md) · [返回大纲](大纲.md) · [下一章](P014_唤醒控制器（WUC）.md)
