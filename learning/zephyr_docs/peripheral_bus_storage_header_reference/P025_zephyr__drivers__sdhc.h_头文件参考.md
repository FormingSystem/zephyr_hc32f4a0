---
id: learning.zephyr-docs.peripheral-bus-storage-header-reference.page-25
title: zephyr__drivers__sdhc.h_头文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sdhc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第25章\_zephyr\_\_drivers\_\_sdhc.h\_头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/sdhc_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

安全数字主控制器（Secure Digital Host Controller，SDHC）驱动API的主头文件。

<a id="details"></a>

```c
#include <errno.h>
#include <zephyr/device.h>
#include <zephyr/net_buf.h>
#include <zephyr/sd/sd_spec.h>
#include <zephyr/syscalls/sdhc.h>
```

查看此文件的源码。

安全数字主控制器（Secure Digital Host Controller，SDHC）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 25.1\_数据结构（Data Structures）

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

<a id="r_sdhc_5Fdriver_5Fapi"></a>

```c
struct sdhc_driver_api
```

相关声明：[sdhc_driver_api](../peripheral_bus_storage_model_reference/P081_sdhc_driver_api_结构体.md)。

驱动操作（Driver Operations）：SD主控制器（SDHC）驱动操作。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 25.2\_宏定义（Macros）

<a id="r_gaff462431ff5c38c74c24772cfbccc1fd"></a>

```c
#define SDHC_NATIVE_RESPONSE_MASK 0xF
```

相关声明：[SDHC_NATIVE_RESPONSE_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gaff462431ff5c38c74c24772cfbccc1fd)。

<a id="r_ga48071d79eddd5178f4b36756a19a21b2"></a>

```c
#define SDHC_SPI_RESPONSE_TYPE_MASK 0xF0
```

相关声明：[SDHC_SPI_RESPONSE_TYPE_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ga48071d79eddd5178f4b36756a19a21b2)。

<a id="define-members-0"></a>

### SD 命令超时（Command timeouts）

<a id="r_gaacc4249f628bcd8967f16713a7def8ae"></a>

```c
#define SDHC_TIMEOUT_FOREVER (-1)
```

相关声明：[SDHC_TIMEOUT_FOREVER](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gaacc4249f628bcd8967f16713a7def8ae)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 25.3\_类型定义（Typedefs）

<a id="r_ga5d207e3b3d76ed9dbfa7d68a92755cbe"></a>

```c
typedef void(* sdhc_interrupt_cb_t) (const struct device *dev, int reason, const void *user_data)
```

相关声明：[sdhc_interrupt_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ga5d207e3b3d76ed9dbfa7d68a92755cbe)、[device](../device_reference/P002_设备对象结构.md)。

SDHC 卡中断回调原型（Callback prototype）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 25.4\_枚举（Enumerations）

<a id="r_gaf26909ae9fffdc6ac02abd8094d16dc8"></a>

```c
enum sdhc_bus_mode { SDHC_BUSMODE_OPENDRAIN = 1 , SDHC_BUSMODE_PUSHPULL = 2 }
```

相关声明：[sdhc_bus_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gaf26909ae9fffdc6ac02abd8094d16dc8)、[SDHC_BUSMODE_OPENDRAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ggaf26909ae9fffdc6ac02abd8094d16dc8a5408bfd39f7ab8c79735d8a956dc9b1a)、[SDHC_BUSMODE_PUSHPULL](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ggaf26909ae9fffdc6ac02abd8094d16dc8ae47425099c55e2191de84a8cbfa17959)。

SD 总线模式。

<a id="r_gad63742820bb18ca18cd2f96547e12eb9"></a>

```c
enum sdhc_power { SDHC_POWER_OFF = 1 , SDHC_POWER_ON = 2 }
```

相关声明：[sdhc_power](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gad63742820bb18ca18cd2f96547e12eb9)、[SDHC_POWER_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ggad63742820bb18ca18cd2f96547e12eb9a621f9456dbce2647567e2e2d049a4c07)、[SDHC_POWER_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ggad63742820bb18ca18cd2f96547e12eb9a9442e1400bdfa373a6874cd1434ab604)。

SD 主机控制器电源。

<a id="r_gad8bab66ec505c8356fac7785a8955448"></a>

```c
enum sdhc_bus_width { SDHC_BUS_WIDTH1BIT = 1U , SDHC_BUS_WIDTH4BIT = 4U , SDHC_BUS_WIDTH8BIT = 8U }
```

相关声明：[sdhc_bus_width](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gad8bab66ec505c8356fac7785a8955448)、[SDHC_BUS_WIDTH1BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ggad8bab66ec505c8356fac7785a8955448a875995b349ed5c81e6f34569c35079a0)、[SDHC_BUS_WIDTH4BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ggad8bab66ec505c8356fac7785a8955448a4e679800f8863d5650827a0330ef22b6)、[SDHC_BUS_WIDTH8BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ggad8bab66ec505c8356fac7785a8955448a2b28e7702abe63e03d2b77994d30e156)。

SD 主机控制器总线宽度。

<a id="r_ga6f006ca8fd9ff8a68ac46a0bb7d4bc90"></a>

```c
enum sdhc_timing_mode { SDHC_TIMING_LEGACY = 1U , SDHC_TIMING_HS = 2U , SDHC_TIMING_SDR12 = 3U , SDHC_TIMING_SDR25 = 4U , SDHC_TIMING_SDR50 = 5U , SDHC_TIMING_SDR104 = 6U , SDHC_TIMING_DDR50 = 7U , SDHC_TIMING_DDR52 = 8U , SDHC_TIMING_HS200 = 9U , SDHC_TIMING_HS400 = 10U }
```

相关声明：[sdhc_timing_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ga6f006ca8fd9ff8a68ac46a0bb7d4bc90)、[SDHC_TIMING_LEGACY](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a8c5c11b75f76771dfedebc6d4a844e55)、[SDHC_TIMING_HS](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90af5f82fc8f4b281e44b5e78f229d9564b)、[SDHC_TIMING_SDR12](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90aa48069d7a8a43308d308c9fe67543d86)、[SDHC_TIMING_SDR25](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a8c77db56b6a006c1cff9f70e20f6d016)、[SDHC_TIMING_SDR50](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a836ffb1abaf681d2992c8c906f5e2c94)、[SDHC_TIMING_SDR104](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90ae2b69f73212e34bbbfb1c02c27740bd1)、[SDHC_TIMING_DDR50](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90afc9b5aa9339c4ffdea8d6452c10ba5fa)、[SDHC_TIMING_DDR52](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a80c5035dc9976f8ee4d7b1f20f21e692)、[SDHC_TIMING_HS200](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90ae892594e6a91a70ade2dc983bda2d145)、[SDHC_TIMING_HS400](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a56909869d92eb1c212051c8a23449ebc)。

SD 主机控制器时序模式。

<a id="r_ga34041edf280f125b8500809226b3de5d"></a>

```c
enum sd_voltage { SD_VOL_3_3_V = 1U , SD_VOL_3_0_V = 2U , SD_VOL_1_8_V = 3U , SD_VOL_1_2_V = 4U }
```

相关声明：[sd_voltage](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ga34041edf280f125b8500809226b3de5d)、[SD_VOL_3_3_V](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gga34041edf280f125b8500809226b3de5da186c3fbdedaf8840a8204d770de1e56d)、[SD_VOL_3_0_V](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gga34041edf280f125b8500809226b3de5daad6c30a3ea2280c9235ba538b52edf11)、[SD_VOL_1_8_V](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gga34041edf280f125b8500809226b3de5dafeed0c640efe6df6f13f76b95138373d)、[SD_VOL_1_2_V](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gga34041edf280f125b8500809226b3de5da6dd8c2d9590dfe38bb77a21c350d36af)。

SD 电压。

<a id="r_gab449b2f6b41e791d327f7d92b2b58c2d"></a>

```c
enum sdhc_interrupt_source { SDHC_INT_SDIO = BIT(0) , SDHC_INT_INSERTED = BIT(1) , SDHC_INT_REMOVED = BIT(2) }
```

相关声明：[sdhc_interrupt_source](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gab449b2f6b41e791d327f7d92b2b58c2d)、[SDHC_INT_SDIO](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ggab449b2f6b41e791d327f7d92b2b58c2dae3a741e98cdb1e8c0ddc8c3baaf64b59)、[SDHC_INT_INSERTED](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ggab449b2f6b41e791d327f7d92b2b58c2dab9df16a6ed1c7961bb9cab34ebe99f87)、[SDHC_INT_REMOVED](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ggab449b2f6b41e791d327f7d92b2b58c2da6e0a03105c6aba203daa53acb6b7c15c)。

SD 主机控制器中断源。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 25.5\_函数（Functions）

<a id="r_gad6b082a75f1272620b79a7d3a08862f7"></a>

```c
int sdhc_hw_reset (const struct device *dev)
```

相关声明：[sdhc_hw_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gad6b082a75f1272620b79a7d3a08862f7)、[device](../device_reference/P002_设备对象结构.md)。

复位 SDHC 控制器状态。

<a id="r_gac708d55e92a7705f92b90ee6baa65f74"></a>

```c
int sdhc_request (const struct device *dev, struct sdhc_command *cmd, struct sdhc_data *data)
```

相关声明：[sdhc_request](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gac708d55e92a7705f92b90ee6baa65f74)、[device](../device_reference/P002_设备对象结构.md)、[sdhc_command](../peripheral_bus_storage_model_reference/P079_sdhc_command_结构体.md)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)、[sdhc_data](../peripheral_bus_storage_model_reference/P080_sdhc_data_结构体.md)。

向 SDHC 发送命令。

<a id="r_ga0e6d8259cca442bd1356d00f668d35c4"></a>

```c
int sdhc_set_io (const struct device *dev, struct sdhc_io *io)
```

相关声明：[sdhc_set_io](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ga0e6d8259cca442bd1356d00f668d35c4)、[device](../device_reference/P002_设备对象结构.md)、[sdhc_io](../peripheral_bus_storage_model_reference/P084_sdhc_io_结构体.md)。

设置 SDHC 的 I/O 属性。

<a id="r_ga85184688da845759dbfb706aac5eac7d"></a>

```c
int sdhc_card_present (const struct device *dev)
```

相关声明：[sdhc_card_present](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ga85184688da845759dbfb706aac5eac7d)、[device](../device_reference/P002_设备对象结构.md)。

检查 SDHC 是否检测到卡。

<a id="r_gab5c2711c99573e031938faaa41862971"></a>

```c
int sdhc_execute_tuning (const struct device *dev)
```

相关声明：[sdhc_execute_tuning](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gab5c2711c99573e031938faaa41862971)、[device](../device_reference/P002_设备对象结构.md)。

执行 SDHC 调谐（Tuning）。

<a id="r_ga91acdc4a6bc2aecc988fdde6ee61ed46"></a>

```c
int sdhc_card_busy (const struct device *dev)
```

相关声明：[sdhc_card_busy](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ga91acdc4a6bc2aecc988fdde6ee61ed46)、[device](../device_reference/P002_设备对象结构.md)。

检查 SD 卡是否忙。

<a id="r_gab55cf88ae79e5aa9e2110b298048df8e"></a>

```c
int sdhc_get_host_props (const struct device *dev, struct sdhc_host_props *props)
```

相关声明：[sdhc_get_host_props](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gab55cf88ae79e5aa9e2110b298048df8e)、[device](../device_reference/P002_设备对象结构.md)、[sdhc_host_props](../peripheral_bus_storage_model_reference/P083_sdhc_host_props_结构体.md)。

获取 SD 主机控制器属性。

<a id="r_ga8e4beb1135aa5c0d32f999ca953224d2"></a>

```c
int sdhc_enable_interrupt (const struct device *dev, sdhc_interrupt_cb_t callback, int sources, void *user_data)
```

相关声明：[sdhc_enable_interrupt](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ga8e4beb1135aa5c0d32f999ca953224d2)、[device](../device_reference/P002_设备对象结构.md)、[sdhc_interrupt_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ga5d207e3b3d76ed9dbfa7d68a92755cbe)。

启用 SDHC 中断源。

<a id="r_ga6264f62c6427973749c8d49fb908f569"></a>

```c
int sdhc_disable_interrupt (const struct device *dev, int sources)
```

相关声明：[sdhc_disable_interrupt](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ga6264f62c6427973749c8d49fb908f569)、[device](../device_reference/P002_设备对象结构.md)。

禁用 SDHC 中断源。


## 25.6\_原页交叉引用（Cross References）

- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h_source.html)
- [zephyr/sd/sd_spec.h](https://docs.zephyrproject.org/latest/doxygen/html/sd__spec_8h_source.html)
- [查看此文件的源码](https://docs.zephyrproject.org/latest/doxygen/html/sdhc_8h_source.html)
- [sdhc_command](../peripheral_bus_storage_model_reference/P079_sdhc_command_结构体.md)
- [sdhc_data](../peripheral_bus_storage_model_reference/P080_sdhc_data_结构体.md)
- [sdhc_host_caps](../peripheral_bus_storage_model_reference/P082_sdhc_host_caps_结构体.md)
- [sdhc_io](../peripheral_bus_storage_model_reference/P084_sdhc_io_结构体.md)
- [sdhc_host_props](../peripheral_bus_storage_model_reference/P083_sdhc_host_props_结构体.md)
- [sdhc_driver_api](../peripheral_bus_storage_model_reference/P081_sdhc_driver_api_结构体.md)
- [SDHC_NATIVE_RESPONSE_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gaff462431ff5c38c74c24772cfbccc1fd)
- [SDHC_SPI_RESPONSE_TYPE_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ga48071d79eddd5178f4b36756a19a21b2)
- [SDHC_TIMEOUT_FOREVER](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gaacc4249f628bcd8967f16713a7def8ae)
- [sdhc_interrupt_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ga5d207e3b3d76ed9dbfa7d68a92755cbe)
- [device](../device_reference/P002_设备对象结构.md)
- [sdhc_bus_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gaf26909ae9fffdc6ac02abd8094d16dc8)
- [SDHC_BUSMODE_OPENDRAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ggaf26909ae9fffdc6ac02abd8094d16dc8a5408bfd39f7ab8c79735d8a956dc9b1a)
- [SDHC_BUSMODE_PUSHPULL](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ggaf26909ae9fffdc6ac02abd8094d16dc8ae47425099c55e2191de84a8cbfa17959)
- [sdhc_power](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gad63742820bb18ca18cd2f96547e12eb9)
- [SDHC_POWER_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ggad63742820bb18ca18cd2f96547e12eb9a621f9456dbce2647567e2e2d049a4c07)
- [SDHC_POWER_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ggad63742820bb18ca18cd2f96547e12eb9a9442e1400bdfa373a6874cd1434ab604)
- [sdhc_bus_width](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gad8bab66ec505c8356fac7785a8955448)
- [SDHC_BUS_WIDTH1BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ggad8bab66ec505c8356fac7785a8955448a875995b349ed5c81e6f34569c35079a0)
- [SDHC_BUS_WIDTH4BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ggad8bab66ec505c8356fac7785a8955448a4e679800f8863d5650827a0330ef22b6)
- [SDHC_BUS_WIDTH8BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ggad8bab66ec505c8356fac7785a8955448a2b28e7702abe63e03d2b77994d30e156)
- [sdhc_timing_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ga6f006ca8fd9ff8a68ac46a0bb7d4bc90)
- [SDHC_TIMING_LEGACY](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a8c5c11b75f76771dfedebc6d4a844e55)
- [SDHC_TIMING_HS](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90af5f82fc8f4b281e44b5e78f229d9564b)
- [SDHC_TIMING_SDR12](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90aa48069d7a8a43308d308c9fe67543d86)
- [SDHC_TIMING_SDR25](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a8c77db56b6a006c1cff9f70e20f6d016)
- [SDHC_TIMING_SDR50](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a836ffb1abaf681d2992c8c906f5e2c94)
- [SDHC_TIMING_SDR104](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90ae2b69f73212e34bbbfb1c02c27740bd1)
- [SDHC_TIMING_DDR50](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90afc9b5aa9339c4ffdea8d6452c10ba5fa)
- [SDHC_TIMING_DDR52](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a80c5035dc9976f8ee4d7b1f20f21e692)
- [SDHC_TIMING_HS200](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90ae892594e6a91a70ade2dc983bda2d145)
- [SDHC_TIMING_HS400](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gga6f006ca8fd9ff8a68ac46a0bb7d4bc90a56909869d92eb1c212051c8a23449ebc)
- [sd_voltage](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ga34041edf280f125b8500809226b3de5d)
- [SD_VOL_3_3_V](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gga34041edf280f125b8500809226b3de5da186c3fbdedaf8840a8204d770de1e56d)
- [SD_VOL_3_0_V](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gga34041edf280f125b8500809226b3de5daad6c30a3ea2280c9235ba538b52edf11)
- [SD_VOL_1_8_V](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gga34041edf280f125b8500809226b3de5dafeed0c640efe6df6f13f76b95138373d)
- [SD_VOL_1_2_V](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gga34041edf280f125b8500809226b3de5da6dd8c2d9590dfe38bb77a21c350d36af)
- [sdhc_interrupt_source](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gab449b2f6b41e791d327f7d92b2b58c2d)
- [SDHC_INT_SDIO](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ggab449b2f6b41e791d327f7d92b2b58c2dae3a741e98cdb1e8c0ddc8c3baaf64b59)
- [SDHC_INT_INSERTED](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ggab449b2f6b41e791d327f7d92b2b58c2dab9df16a6ed1c7961bb9cab34ebe99f87)
- [SDHC_INT_REMOVED](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ggab449b2f6b41e791d327f7d92b2b58c2da6e0a03105c6aba203daa53acb6b7c15c)
- [sdhc_hw_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gad6b082a75f1272620b79a7d3a08862f7)
- [sdhc_request](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gac708d55e92a7705f92b90ee6baa65f74)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)
- [sdhc_set_io](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ga0e6d8259cca442bd1356d00f668d35c4)
- [sdhc_card_present](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ga85184688da845759dbfb706aac5eac7d)
- [sdhc_execute_tuning](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gab5c2711c99573e031938faaa41862971)
- [sdhc_card_busy](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ga91acdc4a6bc2aecc988fdde6ee61ed46)
- [sdhc_get_host_props](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gab55cf88ae79e5aa9e2110b298048df8e)
- [sdhc_enable_interrupt](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ga8e4beb1135aa5c0d32f999ca953224d2)
- [sdhc_disable_interrupt](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ga6264f62c6427973749c8d49fb908f569)

<a id="header-details"></a>

---

[上一章](P024_zephyr__sd__sd.h_头文件参考.md) · [返回大纲](大纲.md) · [下一章](P026_zephyr__drivers__sent__sent.h_头文件参考.md)
