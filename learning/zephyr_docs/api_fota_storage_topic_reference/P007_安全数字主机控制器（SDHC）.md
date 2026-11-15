---
id: learning.zephyr-docs.api-fota-storage-topic-reference.page-7
title: 安全数字主机控制器（SDHC）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_安全数字主机控制器（SDHC）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

安全数字主机控制器（Secure Digital Host Controller，SDHC）接口。

<a id="details"></a>

安全数字卡主机控制器（Secure Digital Host Controller，SDHC）接口。自（Since）3.1 起提供，版本（Version）0.8.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 7.1\_主题（Topics）

<a id="r_sdhc_5Finterface_5Fbackend"></a>

相关声明：[SDHC 驱动后端 API](../api_platform_topic_reference/P120_SDHC 驱动后端 API.md)。

<a id="header-files"></a>
<a id="files"></a>

## 7.2\_文件（Files）

<a id="r_sdhc_2Eh"></a>

```c
file sdhc.h
```

相关声明：[sdhc.h](../peripheral_bus_storage_header_reference/P025_zephyr__drivers__sdhc.h_头文件参考.md)。

安全数字主控制器（Secure Digital Host Controller，SDHC）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 7.3\_数据结构（Data Structures）

<a id="r_sdhc_5Fcommand"></a>

```c
struct sdhc_command
```

相关声明：[sdhc_command](../peripheral_bus_storage_model_reference/P079_sdhc_command_结构体.md)。

SD主控制器（Host Controller）的命令结构。

<a id="r_sdhc_5Fdata"></a>

```c
struct sdhc_data
```

相关声明：[sdhc_data](../peripheral_bus_storage_model_reference/P080_sdhc_data_结构体.md)。

SD主控制器（Host Controller）的数据结构。

<a id="r_sdhc_5Fhost_5Fcaps"></a>

```c
struct sdhc_host_caps
```

相关声明：[sdhc_host_caps](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md)。

SD主控制器（Host Controller）的能力。

<a id="r_sdhc_5Fio"></a>

```c
struct sdhc_io
```

相关声明：[sdhc_io](../peripheral_bus_storage_model_reference/P084_sdhc_io_结构体.md)。

SD主控制器（Host Controller）的输入输出控制结构。

<a id="r_sdhc_5Fhost_5Fprops"></a>

```c
struct sdhc_host_props
```

相关声明：[sdhc_host_props](../peripheral_bus_storage_model_reference/P083_sdhc_host_props_结构体.md)。

SD主控制器（Host Controller）的属性。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 7.4\_宏定义（Macros）

<a id="r_gaff462431ff5c38c74c24772cfbccc1fd"></a>

```c
#define SDHC_NATIVE_RESPONSE_MASK 0xF
```

相关声明：[SDHC_NATIVE_RESPONSE_MASK](#gaff462431ff5c38c74c24772cfbccc1fd)。

<a id="r_ga48071d79eddd5178f4b36756a19a21b2"></a>

```c
#define SDHC_SPI_RESPONSE_TYPE_MASK 0xF0
```

相关声明：[SDHC_SPI_RESPONSE_TYPE_MASK](#ga48071d79eddd5178f4b36756a19a21b2)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 7.5\_类型定义（Typedefs）

<a id="r_ga5d207e3b3d76ed9dbfa7d68a92755cbe"></a>

```c
typedef void(* sdhc_interrupt_cb_t) (const struct device *dev, int reason, const void *user_data)
```

相关声明：[sdhc_interrupt_cb_t](#ga5d207e3b3d76ed9dbfa7d68a92755cbe)、[device](../device_reference/P002_设备对象结构.md)。

SDHC 卡中断回调原型（Callback prototype）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 7.6\_枚举（Enumerations）

<a id="r_gaf26909ae9fffdc6ac02abd8094d16dc8"></a>

```c
enum sdhc_bus_mode { SDHC_BUSMODE_OPENDRAIN = 1 , SDHC_BUSMODE_PUSHPULL = 2 }
```

相关声明：[sdhc_bus_mode](#gaf26909ae9fffdc6ac02abd8094d16dc8)、[SDHC_BUSMODE_OPENDRAIN](#ggaf26909ae9fffdc6ac02abd8094d16dc8a5408bfd39f7ab8c79735d8a956dc9b1a)、[SDHC_BUSMODE_PUSHPULL](#ggaf26909ae9fffdc6ac02abd8094d16dc8ae47425099c55e2191de84a8cbfa17959)。

SD 总线模式。

<a id="r_gad63742820bb18ca18cd2f96547e12eb9"></a>

```c
enum sdhc_power { SDHC_POWER_OFF = 1 , SDHC_POWER_ON = 2 }
```

相关声明：[sdhc_power](#gad63742820bb18ca18cd2f96547e12eb9)、[SDHC_POWER_OFF](#ggad63742820bb18ca18cd2f96547e12eb9a621f9456dbce2647567e2e2d049a4c07)、[SDHC_POWER_ON](#ggad63742820bb18ca18cd2f96547e12eb9a9442e1400bdfa373a6874cd1434ab604)。

SD 主机控制器电源。

<a id="r_gad8bab66ec505c8356fac7785a8955448"></a>

```c
enum sdhc_bus_width { SDHC_BUS_WIDTH1BIT = 1U , SDHC_BUS_WIDTH4BIT = 4U , SDHC_BUS_WIDTH8BIT = 8U }
```

相关声明：[sdhc_bus_width](#gad8bab66ec505c8356fac7785a8955448)、[SDHC_BUS_WIDTH1BIT](#ggad8bab66ec505c8356fac7785a8955448a875995b349ed5c81e6f34569c35079a0)、[SDHC_BUS_WIDTH4BIT](#ggad8bab66ec505c8356fac7785a8955448a4e679800f8863d5650827a0330ef22b6)、[SDHC_BUS_WIDTH8BIT](#ggad8bab66ec505c8356fac7785a8955448a2b28e7702abe63e03d2b77994d30e156)。

SD 主机控制器总线宽度。

<a id="r_ga6f006ca8fd9ff8a68ac46a0bb7d4bc90"></a>

```c
enum sdhc_timing_mode { SDHC_TIMING_LEGACY = 1U , SDHC_TIMING_HS = 2U , SDHC_TIMING_SDR12 = 3U , SDHC_TIMING_SDR25 = 4U , SDHC_TIMING_SDR50 = 5U , SDHC_TIMING_SDR104 = 6U , SDHC_TIMING_DDR50 = 7U , SDHC_TIMING_DDR52 = 8U , SDHC_TIMING_HS200 = 9U , SDHC_TIMING_HS400 = 10U }
```

相关声明：[sdhc_timing_mode](#ga6f006ca8fd9ff8a68ac46a0bb7d4bc90)、[SDHC_TIMING_LEGACY](#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a8c5c11b75f76771dfedebc6d4a844e55)、[SDHC_TIMING_HS](#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90af5f82fc8f4b281e44b5e78f229d9564b)、[SDHC_TIMING_SDR12](#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90aa48069d7a8a43308d308c9fe67543d86)、[SDHC_TIMING_SDR25](#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a8c77db56b6a006c1cff9f70e20f6d016)、[SDHC_TIMING_SDR50](#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a836ffb1abaf681d2992c8c906f5e2c94)、[SDHC_TIMING_SDR104](#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90ae2b69f73212e34bbbfb1c02c27740bd1)、[SDHC_TIMING_DDR50](#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90afc9b5aa9339c4ffdea8d6452c10ba5fa)、[SDHC_TIMING_DDR52](#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a80c5035dc9976f8ee4d7b1f20f21e692)、[SDHC_TIMING_HS200](#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90ae892594e6a91a70ade2dc983bda2d145)、[SDHC_TIMING_HS400](#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a56909869d92eb1c212051c8a23449ebc)。

SD 主机控制器时序模式。

<a id="r_ga34041edf280f125b8500809226b3de5d"></a>

```c
enum sd_voltage { SD_VOL_3_3_V = 1U , SD_VOL_3_0_V = 2U , SD_VOL_1_8_V = 3U , SD_VOL_1_2_V = 4U }
```

相关声明：[sd_voltage](#ga34041edf280f125b8500809226b3de5d)、[SD_VOL_3_3_V](#gga34041edf280f125b8500809226b3de5da186c3fbdedaf8840a8204d770de1e56d)、[SD_VOL_3_0_V](#gga34041edf280f125b8500809226b3de5daad6c30a3ea2280c9235ba538b52edf11)、[SD_VOL_1_8_V](#gga34041edf280f125b8500809226b3de5dafeed0c640efe6df6f13f76b95138373d)、[SD_VOL_1_2_V](#gga34041edf280f125b8500809226b3de5da6dd8c2d9590dfe38bb77a21c350d36af)。

SD 电压。

<a id="r_gab449b2f6b41e791d327f7d92b2b58c2d"></a>

```c
enum sdhc_interrupt_source { SDHC_INT_SDIO = BIT(0) , SDHC_INT_INSERTED = BIT(1) , SDHC_INT_REMOVED = BIT(2) }
```

相关声明：[sdhc_interrupt_source](#gab449b2f6b41e791d327f7d92b2b58c2d)、[SDHC_INT_SDIO](#ggab449b2f6b41e791d327f7d92b2b58c2dae3a741e98cdb1e8c0ddc8c3baaf64b59)、[SDHC_INT_INSERTED](#ggab449b2f6b41e791d327f7d92b2b58c2dab9df16a6ed1c7961bb9cab34ebe99f87)、[SDHC_INT_REMOVED](#ggab449b2f6b41e791d327f7d92b2b58c2da6e0a03105c6aba203daa53acb6b7c15c)。

SD 主机控制器中断源。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 7.7\_函数（Functions）

<a id="r_gad6b082a75f1272620b79a7d3a08862f7"></a>

```c
int sdhc_hw_reset (const struct device *dev)
```

相关声明：[sdhc_hw_reset](#gad6b082a75f1272620b79a7d3a08862f7)、[device](../device_reference/P002_设备对象结构.md)。

复位 SDHC 控制器状态。

<a id="r_gac708d55e92a7705f92b90ee6baa65f74"></a>

```c
int sdhc_request (const struct device *dev, struct sdhc_command *cmd, struct sdhc_data *data)
```

相关声明：[sdhc_request](#gac708d55e92a7705f92b90ee6baa65f74)、[device](../device_reference/P002_设备对象结构.md)、[sdhc_command](../peripheral_bus_storage_model_reference/P079_sdhc_command_结构体.md)、[cmd](../api_scoped_clock_topic_reference/P012_FT8xx 参考 API.md#gacde1ca3945cbe6c828f65051c5c3a615)、[sdhc_data](../peripheral_bus_storage_model_reference/P080_sdhc_data_结构体.md)。

向 SDHC 发送命令。

<a id="r_ga0e6d8259cca442bd1356d00f668d35c4"></a>

```c
int sdhc_set_io (const struct device *dev, struct sdhc_io *io)
```

相关声明：[sdhc_set_io](#ga0e6d8259cca442bd1356d00f668d35c4)、[device](../device_reference/P002_设备对象结构.md)、[sdhc_io](../peripheral_bus_storage_model_reference/P084_sdhc_io_结构体.md)。

设置 SDHC 的 I/O 属性。

<a id="r_ga85184688da845759dbfb706aac5eac7d"></a>

```c
int sdhc_card_present (const struct device *dev)
```

相关声明：[sdhc_card_present](#ga85184688da845759dbfb706aac5eac7d)、[device](../device_reference/P002_设备对象结构.md)。

检查 SDHC 是否检测到卡。

<a id="r_gab5c2711c99573e031938faaa41862971"></a>

```c
int sdhc_execute_tuning (const struct device *dev)
```

相关声明：[sdhc_execute_tuning](#gab5c2711c99573e031938faaa41862971)、[device](../device_reference/P002_设备对象结构.md)。

执行 SDHC 调谐（Tuning）。

<a id="r_ga91acdc4a6bc2aecc988fdde6ee61ed46"></a>

```c
int sdhc_card_busy (const struct device *dev)
```

相关声明：[sdhc_card_busy](#ga91acdc4a6bc2aecc988fdde6ee61ed46)、[device](../device_reference/P002_设备对象结构.md)。

检查 SD 卡是否忙。

<a id="r_gab55cf88ae79e5aa9e2110b298048df8e"></a>

```c
int sdhc_get_host_props (const struct device *dev, struct sdhc_host_props *props)
```

相关声明：[sdhc_get_host_props](#gab55cf88ae79e5aa9e2110b298048df8e)、[device](../device_reference/P002_设备对象结构.md)、[sdhc_host_props](../peripheral_bus_storage_model_reference/P083_sdhc_host_props_结构体.md)。

获取 SD 主机控制器属性。

<a id="r_ga8e4beb1135aa5c0d32f999ca953224d2"></a>

```c
int sdhc_enable_interrupt (const struct device *dev, sdhc_interrupt_cb_t callback, int sources, void *user_data)
```

相关声明：[sdhc_enable_interrupt](#ga8e4beb1135aa5c0d32f999ca953224d2)、[device](../device_reference/P002_设备对象结构.md)、[sdhc_interrupt_cb_t](#ga5d207e3b3d76ed9dbfa7d68a92755cbe)。

启用 SDHC 中断源。

<a id="r_ga6264f62c6427973749c8d49fb908f569"></a>

```c
int sdhc_disable_interrupt (const struct device *dev, int sources)
```

相关声明：[sdhc_disable_interrupt](#ga6264f62c6427973749c8d49fb908f569)、[device](../device_reference/P002_设备对象结构.md)。

禁用 SDHC 中断源。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 7.8\_SD 命令超时（Command timeouts）

<a id="r_gaacc4249f628bcd8967f16713a7def8ae"></a>

```c
#define SDHC_TIMEOUT_FOREVER (-1)
```

相关声明：[SDHC_TIMEOUT_FOREVER](#gaacc4249f628bcd8967f16713a7def8ae)。

## 7.9\_详细说明（Detailed Documentation）

<a id="gaff462431ff5c38c74c24772cfbccc1fd"></a>

### `SDHC_NATIVE_RESPONSE_MASK`

```c
#define SDHC_NATIVE_RESPONSE_MASK 0xF
```

```c
#include <zephyr/drivers/sdhc.h>
```

<a id="ga48071d79eddd5178f4b36756a19a21b2"></a>

### `SDHC_SPI_RESPONSE_TYPE_MASK`

```c
#define SDHC_SPI_RESPONSE_TYPE_MASK 0xF0
```

```c
#include <zephyr/drivers/sdhc.h>
```

<a id="gaacc4249f628bcd8967f16713a7def8ae"></a>

### `SDHC_TIMEOUT_FOREVER`

```c
#define SDHC_TIMEOUT_FOREVER (-1)
```

```c
#include <zephyr/drivers/sdhc.h>
```

<a id="ga5d207e3b3d76ed9dbfa7d68a92755cbe"></a>

### `sdhc_interrupt_cb_t`

```c
typedef void(* sdhc_interrupt_cb_t) (const struct device *dev, int reason, const void *user_data)
```

```c
#include <zephyr/drivers/sdhc.h>
```

SDHC 卡中断回调原型（Callback prototype）。

SDHC 卡中断回调（Card Interrupt Callback）的函数原型。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 产生中断的 SDHC 设备。 |
| `reason` | `sdhc_interrupt_source` 中的一个值。 |
| `user_data` | 通过 `sdhc_enable_interrupt` 设置的用户数据（User Data）。 |

<a id="ga34041edf280f125b8500809226b3de5d"></a>

### `sd_voltage`

```c
enum sd_voltage
```

```c
#include <zephyr/drivers/sdhc.h>
```

SD 电压。

超高速卡（Ultra High Speed，UHS）可使用 1.8 V 信号电平以降低功耗。传统卡可能支持 3.0 V 信号电平，所有卡均从 3.3 V 开始。此项仅与 SD 控制器相关，不适用于 SPI 控制器。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SD_VOL_3_3_V` | 卡工作电压约为 3.3 V。 |
| `SD_VOL_3_0_V` | 卡工作电压约为 3.0 V。 |
| `SD_VOL_1_8_V` | 卡工作电压约为 1.8 V。 |
| `SD_VOL_1_2_V` | 卡工作电压约为 1.2 V。 |

<a id="gaf26909ae9fffdc6ac02abd8094d16dc8"></a>

### `sdhc_bus_mode`

```c
enum sdhc_bus_mode
```

```c
#include <zephyr/drivers/sdhc.h>
```

SD 总线模式。

大多数控制器（包括 SPI）使用推挽（Push-Pull）模式，但实现 SD 主机规范的 SDHC 控制器可以支持开漏（Open-Drain）模式。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SDHC_BUSMODE_OPENDRAIN` |  |
| `SDHC_BUSMODE_PUSHPULL` |  |

<a id="gad8bab66ec505c8356fac7785a8955448"></a>

### `sdhc_bus_width`

```c
enum sdhc_bus_width
```

```c
#include <zephyr/drivers/sdhc.h>
```

SD 主机控制器总线宽度。

仅与 SD 模式相关，SPI 不支持总线宽度（Bus Width）设置。UHS 卡使用 4 位数据总线；所有卡均从 1 位模式开始。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SDHC_BUS_WIDTH1BIT` |  |
| `SDHC_BUS_WIDTH4BIT` |  |
| `SDHC_BUS_WIDTH8BIT` |  |

<a id="gab449b2f6b41e791d327f7d92b2b58c2d"></a>

### `sdhc_interrupt_source`

```c
enum sdhc_interrupt_source
```

```c
#include <zephyr/drivers/sdhc.h>
```

SD 主机控制器中断源。

SD 主机控制器的中断源（Interrupt Sources）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SDHC_INT_SDIO` | 卡中断（Card Interrupt），由 SDIO 卡使用。 |
| `SDHC_INT_INSERTED` | 卡已插入插槽。 |
| `SDHC_INT_REMOVED` | 卡已从插槽中拔出。 |

<a id="gad63742820bb18ca18cd2f96547e12eb9"></a>

### `sdhc_power`

```c
enum sdhc_power
```

```c
#include <zephyr/drivers/sdhc.h>
```

SD 主机控制器电源。

许多主机控制器可控制所连接 SD 卡的电源。此枚举允许应用请求主机控制器关闭 SD 卡电源。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SDHC_POWER_OFF` |  |
| `SDHC_POWER_ON` |  |

<a id="ga6f006ca8fd9ff8a68ac46a0bb7d4bc90"></a>

### `sdhc_timing_mode`

```c
enum sdhc_timing_mode
```

```c
#include <zephyr/drivers/sdhc.h>
```

SD 主机控制器时序模式。

供 SD 主机控制器确定总线上所连接卡的时序（Timing）。卡以传统时序启动，但 UHS-II 卡最高可达到 SDR104（原文如此）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SDHC_TIMING_LEGACY` | 传统 3.3 V 模式（Legacy Mode）。 |
| `SDHC_TIMING_HS` | 传统高速模式（Legacy High Speed Mode，3.3 V）。 |
| `SDHC_TIMING_SDR12` | 识别模式（Identification Mode）与 SDR12。 |
| `SDHC_TIMING_SDR25` | 高速模式（High Speed Mode）与 SDR25。 |
| `SDHC_TIMING_SDR50` | SDR50 模式。 |
| `SDHC_TIMING_SDR104` | SDR104 模式。 |
| `SDHC_TIMING_DDR50` | DDR50 模式。 |
| `SDHC_TIMING_DDR52` | DDR52 模式。 |
| `SDHC_TIMING_HS200` | HS200 模式。 |
| `SDHC_TIMING_HS400` | HS400 模式。 |

<a id="ga91acdc4a6bc2aecc988fdde6ee61ed46"></a>

### `sdhc_card_busy()`

```c
int sdhc_card_busy ( const struct device * dev)
```

```c
#include <zephyr/drivers/sdhc.h>
```

检查 SD 卡是否忙。

通常应通过检查 SD 总线 `DAT[0:3]` 信号线的电平来实现此检查。无需发送 SD 命令，控制器只需报告 SD 总线状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | SDHC 设备。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 卡不忙（Not Busy）。 |
| `1` | 卡忙。 |
| `-EIO` | 输入／输出错误（I/O Error）。 |

<a id="ga85184688da845759dbfb706aac5eac7d"></a>

### `sdhc_card_present()`

```c
int sdhc_card_present ( const struct device * dev)
```

```c
#include <zephyr/drivers/sdhc.h>
```

检查 SDHC 是否检测到卡。

检查 SD 总线上是否有卡。注意，如果控制器需要给卡上电才能检测其是否在位，则应在此函数中上电。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | SDHC 设备。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `1` | 存在卡。 |
| `0` | 不存在卡。 |
| `-EIO` | 输入／输出错误（I/O Error）。 |

<a id="ga6264f62c6427973749c8d49fb908f569"></a>

### `sdhc_disable_interrupt()`

```c
int sdhc_disable_interrupt ( const struct device * dev, int sources )
```

```c
#include <zephyr/drivers/sdhc.h>
```

禁用 SDHC 中断源。

禁用 SDHC 中断源（Interrupt Sources）。若启用了多个中断源，仅屏蔽 `sources` 指定的中断源。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | SDHC 设备。 |
| `sources` | 由 `sdhc_interrupt_source` 值组成的位掩码（Bitmask），指示要禁用哪些中断。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 中断已禁用。 |
| `-ENOSYS` | 控制器不支持此函数。 |
| `-EIO` | 输入／输出错误（I/O Error）。 |

<a id="ga8e4beb1135aa5c0d32f999ca953224d2"></a>

### `sdhc_enable_interrupt()`

```c
int sdhc_enable_interrupt ( const struct device * dev, sdhc_interrupt_cb_t callback, int sources, void * user_data )
```

```c
#include <zephyr/drivers/sdhc.h>
```

启用 SDHC 中断源。

启用 SDHC 中断源（Interrupt Sources）。每次后续调用都应替换之前设置的回调，并仅保留 `sources` 参数指定的中断处于启用状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | SDHC 设备。 |
| `callback` | 发生中断时调用的回调（Callback）。 |
| `sources` | 由 `sdhc_interrupt_source` 值组成的位掩码（Bitmask），指示哪些中断应触发回调。 |
| `user_data` | 将传给回调函数的参数。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 中断已启用，且回调已安装。 |
| `-ENOSYS` | 控制器不支持中断（Interrupts）。 |
| `-EINVAL` | 指定了无效的中断源（Interrupt Source）。 |
| `-EIO` | 输入／输出错误（I/O Error）。 |

<a id="gab5c2711c99573e031938faaa41862971"></a>

### `sdhc_execute_tuning()`

```c
int sdhc_execute_tuning ( const struct device * dev)
```

```c
#include <zephyr/drivers/sdhc.h>
```

执行 SDHC 调谐（Tuning）。

SD 卡在 UHS 的 SDR104 和 SDR50 模式下需要信号调谐（Signal Tuning）。此函数允许应用请求 SD 主机控制器对卡进行调谐。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | SDHC 设备。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 调谐（Tuning）成功，卡已准备好接收命令。 |
| `-ETIMEDOUT` | 调谐（Tuning）超时失败。 |
| `-ENOSYS` | 控制器不支持调谐（Tuning）。 |
| `-EIO` | 调谐（Tuning）期间发生 I/O 错误。 |

<a id="gab55cf88ae79e5aa9e2110b298048df8e"></a>

### `sdhc_get_host_props()`

```c
int sdhc_get_host_props ( const struct device * dev, struct sdhc_host_props * props )
```

```c
#include <zephyr/drivers/sdhc.h>
```

获取 SD 主机控制器属性。

从主机控制器获取主机属性（Host Properties）。主机控制器应初始化所提供 `sdhc_host_props` 结构体中的全部值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | SDHC 设备。 |
| `props` | 由 SDHC 驱动填充的属性结构体。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 函数执行成功。 |
| `-EIO` | 输入／输出错误（I/O Error）。 |

<a id="gad6b082a75f1272620b79a7d3a08862f7"></a>

### `sdhc_hw_reset()`

```c
int sdhc_hw_reset ( const struct device * dev)
```

```c
#include <zephyr/drivers/sdhc.h>
```

复位 SDHC 控制器状态。

在 SDHC 遇到错误时使用。复位 SDHC 控制器应清除其所有错误，但不一定会把 I/O 设置恢复至启动状态（可通过 `sdhc_set_io` 完成恢复）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | SD 主机控制器设备（SD Host Controller Device）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 复位成功（Reset Succeeded）。 |
| `-ETIMEDOUT` | 控制器复位超时（Reset Timed Out）。 |
| `-ENOSYS` | 控制器不支持复位（Reset）。 |
| `-EIO` | 复位失败（Reset Failed）。 |

<a id="gac708d55e92a7705f92b90ee6baa65f74"></a>

### `sdhc_request()`

```c
int sdhc_request ( const struct device * dev, struct sdhc_command * cmd, struct sdhc_data * data )
```

```c
#include <zephyr/drivers/sdhc.h>
```

向 SDHC 发送命令。

向 SD 主机控制器发送命令；控制器会将该命令发送给连接的 SD 卡。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | SDHC 设备。 |
| `cmd` | SDHC 命令（Command）。 |
| `data` | SDHC 数据（Data）。设为 `NULL` 可发送不带数据的 SD 命令。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 命令发送成功。 |
| `-ETIMEDOUT` | 发送命令时超时。 |
| `-EIO` | 输入／输出错误（I/O Error）。 |

<a id="ga0e6d8259cca442bd1356d00f668d35c4"></a>

### `sdhc_set_io()`

```c
int sdhc_set_io ( const struct device * dev, struct sdhc_io * io )
```

```c
#include <zephyr/drivers/sdhc.h>
```

设置 SDHC 的 I/O 属性。

向卡发送命令以修改其自身 SD 设置后，应重新配置 I/O 属性。此函数也可用于开关 SD 卡电源。支持 eMMC HS400 增强选通（Enhanced Strobe）的主机还应应用 `io` 中的 `enhanced_strobe` 状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | SDHC 设备。 |
| `io` | I/O 属性（I/O Properties）。 |

**返回（Returns）**：返回值（Returns）：0 表示 I/O 已正确配置；`-ENOTSUP` 表示控制器不支持这些 I/O 设置；`-EIO` 表示控制器无法配置 I/O 设置。


## 7.10\_原页交叉引用（Cross References）

- [SDHC 驱动后端 API](../api_platform_topic_reference/P120_SDHC 驱动后端 API.md)
- [sdhc.h](../peripheral_bus_storage_header_reference/P025_zephyr__drivers__sdhc.h_头文件参考.md)
- [sdhc_command](../peripheral_bus_storage_model_reference/P079_sdhc_command_结构体.md)
- [sdhc_data](../peripheral_bus_storage_model_reference/P080_sdhc_data_结构体.md)
- [sdhc_host_caps](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md)
- [sdhc_io](../peripheral_bus_storage_model_reference/P084_sdhc_io_结构体.md)
- [sdhc_host_props](../peripheral_bus_storage_model_reference/P083_sdhc_host_props_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [cmd](../api_scoped_clock_topic_reference/P012_FT8xx 参考 API.md#gacde1ca3945cbe6c828f65051c5c3a615)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga34041edf280f125b8500809226b3de5da186c3fbdedaf8840a8204d770de1e56d"></a>
<a id="gga34041edf280f125b8500809226b3de5daad6c30a3ea2280c9235ba538b52edf11"></a>
<a id="gga34041edf280f125b8500809226b3de5dafeed0c640efe6df6f13f76b95138373d"></a>
<a id="gga34041edf280f125b8500809226b3de5da6dd8c2d9590dfe38bb77a21c350d36af"></a>
<a id="ggaf26909ae9fffdc6ac02abd8094d16dc8a5408bfd39f7ab8c79735d8a956dc9b1a"></a>
<a id="ggaf26909ae9fffdc6ac02abd8094d16dc8ae47425099c55e2191de84a8cbfa17959"></a>
<a id="ggad8bab66ec505c8356fac7785a8955448a875995b349ed5c81e6f34569c35079a0"></a>
<a id="ggad8bab66ec505c8356fac7785a8955448a4e679800f8863d5650827a0330ef22b6"></a>
<a id="ggad8bab66ec505c8356fac7785a8955448a2b28e7702abe63e03d2b77994d30e156"></a>
<a id="ggab449b2f6b41e791d327f7d92b2b58c2dae3a741e98cdb1e8c0ddc8c3baaf64b59"></a>
<a id="ggab449b2f6b41e791d327f7d92b2b58c2dab9df16a6ed1c7961bb9cab34ebe99f87"></a>
<a id="ggab449b2f6b41e791d327f7d92b2b58c2da6e0a03105c6aba203daa53acb6b7c15c"></a>
<a id="ggad63742820bb18ca18cd2f96547e12eb9a621f9456dbce2647567e2e2d049a4c07"></a>
<a id="ggad63742820bb18ca18cd2f96547e12eb9a9442e1400bdfa373a6874cd1434ab604"></a>
<a id="gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a8c5c11b75f76771dfedebc6d4a844e55"></a>
<a id="gga6f006ca8fd9ff8a68ac46a0bb7d4bc90af5f82fc8f4b281e44b5e78f229d9564b"></a>
<a id="gga6f006ca8fd9ff8a68ac46a0bb7d4bc90aa48069d7a8a43308d308c9fe67543d86"></a>
<a id="gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a8c77db56b6a006c1cff9f70e20f6d016"></a>
<a id="gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a836ffb1abaf681d2992c8c906f5e2c94"></a>
<a id="gga6f006ca8fd9ff8a68ac46a0bb7d4bc90ae2b69f73212e34bbbfb1c02c27740bd1"></a>
<a id="gga6f006ca8fd9ff8a68ac46a0bb7d4bc90afc9b5aa9339c4ffdea8d6452c10ba5fa"></a>
<a id="gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a80c5035dc9976f8ee4d7b1f20f21e692"></a>
<a id="gga6f006ca8fd9ff8a68ac46a0bb7d4bc90ae892594e6a91a70ade2dc983bda2d145"></a>
<a id="gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a56909869d92eb1c212051c8a23449ebc"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P006_PCIe能力（Capabilities）。.md) · [返回大纲](大纲.md) · [下一章](P008_系统管理总线（SMBus）.md)
