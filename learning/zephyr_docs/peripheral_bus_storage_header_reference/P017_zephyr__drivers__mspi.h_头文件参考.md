---
id: learning.zephyr-docs.peripheral-bus-storage-header-reference.page-17
title: zephyr__drivers__mspi.h_头文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mspi_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_zephyr\_\_drivers\_\_mspi.h\_头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mspi_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

多位串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）驱动API的主头文件。

<a id="details"></a>

```c
#include <errno.h>
#include <zephyr/sys/__assert.h>
#include <zephyr/types.h>
#include <zephyr/kernel.h>
#include <zephyr/device.h>
#include <zephyr/drivers/gpio.h>
#include <zephyr/drivers/mspi/devicetree.h>
#include <zephyr/sys/util_macro.h>
#include <zephyr/syscalls/mspi.h>
```

查看此文件的源码。

多位串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 17.1\_数据结构（Data Structures）

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

<a id="r_mspi_5Fce_5Fcontrol"></a>

```c
struct mspi_ce_control
```

相关声明：[mspi_ce_control](../peripheral_bus_storage_model_reference/P038_mspi_ce_control_结构体.md)。

MSPI片选（Chip Select）的控制结构。

<a id="r_mspi_5Fxfer_5Fpacket"></a>

```c
struct mspi_xfer_packet
```

相关声明：[mspi_xfer_packet](../peripheral_bus_storage_model_reference/P051_mspi_xfer_packet_结构体.md)。

MSPI外设传输数据包格式（Xfer Packet Format）。

<a id="r_mspi_5Fxfer"></a>

```c
struct mspi_xfer
```

相关声明：[mspi_xfer](../peripheral_bus_storage_model_reference/P050_mspi_xfer_结构体.md)。

MSPI外设传输格式（Xfer Format），包括可能需要配置硬件的传输相关设置。

<a id="r_mspi_5Fevent_5Fdata"></a>

```c
struct mspi_event_data
```

相关声明：[mspi_event_data](../peripheral_bus_storage_model_reference/P046_mspi_event_data_结构体.md)。

MSPI事件数据（Event Data）。

<a id="r_mspi_5Fevent"></a>

```c
struct mspi_event
```

相关声明：[mspi_event](../peripheral_bus_storage_model_reference/P045_mspi_event_结构体.md)。

MSPI事件（Event）。

<a id="r_mspi_5Fcallback_5Fcontext"></a>

```c
struct mspi_callback_context
```

相关声明：[mspi_callback_context](../peripheral_bus_storage_model_reference/P037_mspi_callback_context_结构体.md)。

MSPI回调上下文（Callback Context）。

<a id="r_mspi_5Fdriver_5Fapi"></a>

```c
struct mspi_driver_api
```

相关声明：[mspi_driver_api](../peripheral_bus_storage_model_reference/P042_mspi_driver_api_结构体.md)。

驱动操作（Driver Operations）：MSPI驱动操作。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 17.2\_宏定义（Macros）

<a id="r_gadce17ebaa26cfd2b59fadab2a7b2a788"></a>

```c
#define MSPI_MEMMAP_CFG_STRUCT_DECLARE(_name)
```

相关声明：[MSPI_MEMMAP_CFG_STRUCT_DECLARE](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__util.html#gadce17ebaa26cfd2b59fadab2a7b2a788)。

在外设驱动中声明可选的内存映射配置（Memory map configuration）。

<a id="r_gae9b12392a7cc1f6b746adddec56e0b85"></a>

```c
#define MSPI_MEMMAP_BASE_ADDR_DECLARE(_name)
```

相关声明：[MSPI_MEMMAP_BASE_ADDR_DECLARE](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__util.html#gae9b12392a7cc1f6b746adddec56e0b85)。

在外设驱动中声明可选的内存映射基地址。

<a id="r_ga8c55eacfe36f484bb5b3f82f8918aa79"></a>

```c
#define MSPI_SCRAMBLE_CFG_STRUCT_DECLARE(_name)
```

相关声明：[MSPI_SCRAMBLE_CFG_STRUCT_DECLARE](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__util.html#ga8c55eacfe36f484bb5b3f82f8918aa79)。

在外设驱动中声明可选的扰码配置（Scramble configuration）。

<a id="r_ga118cb8d67bde11040aa8369ff88e4b6b"></a>

```c
#define MSPI_TIMING_CFG_STRUCT_DECLARE(_name)
```

相关声明：[MSPI_TIMING_CFG_STRUCT_DECLARE](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__util.html#ga118cb8d67bde11040aa8369ff88e4b6b)。

在外设驱动中声明可选的时序配置（Timing configuration）。

<a id="r_ga4c88adce60d915c85972fa2cfaf7177e"></a>

```c
#define MSPI_TIMING_PARAM_DECLARE(_name)
```

相关声明：[MSPI_TIMING_PARAM_DECLARE](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__util.html#ga4c88adce60d915c85972fa2cfaf7177e)。

在外设驱动中声明可选的时序参数。

<a id="r_ga7b2c02a81ae6d670680b86088624dc17"></a>

```c
#define MSPI_OPTIONAL_CFG_STRUCT_INIT(code, _name, _object)
```

相关声明：[MSPI_OPTIONAL_CFG_STRUCT_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__util.html#ga7b2c02a81ae6d670680b86088624dc17)。

初始化外设驱动中的可选配置结构体。

<a id="r_ga2da665f679f0c538e58ebff4005daec3"></a>

```c
#define MSPI_MEMMAP_BASE_ADDR_INIT(_name, _bus)
```

相关声明：[MSPI_MEMMAP_BASE_ADDR_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__util.html#ga2da665f679f0c538e58ebff4005daec3)。

初始化外设驱动中的可选内存映射基地址。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 17.3\_类型定义（Typedefs）

<a id="r_ga29421f748fdb89c823e1a48ff69cf0f4"></a>

```c
typedef void(* mspi_callback_handler_t) (struct mspi_callback_context *mspi_cb_ctx,...)
```

相关声明：[mspi_callback_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__callback__api.html#ga29421f748fdb89c823e1a48ff69cf0f4)、[mspi_callback_context](../peripheral_bus_storage_model_reference/P037_mspi_callback_context_结构体.md)。

定义应用程序回调处理函数的签名（Function Signature）。

<a id="r_ga2ff9209634fb241e2f7323e749df612e"></a>

```c
typedef int(* mspi_api_config) (const struct mspi_dt_spec *spec)
```

相关声明：[mspi_api_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface__backend.html#ga2ff9209634fb241e2f7323e749df612e)、[mspi_dt_spec](../peripheral_bus_storage_model_reference/P043_mspi_dt_spec_结构体.md)。

配置 MSPI 控制器。

<a id="r_ga7e3bae501067b045e9ed8d0efbe6e61d"></a>

```c
typedef int(* mspi_api_dev_config) (const struct device *controller, const struct mspi_dev_id *dev_id, const enum mspi_dev_cfg_mask param_mask, const struct mspi_dev_cfg *cfg)
```

相关声明：[mspi_api_dev_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface__backend.html#ga7e3bae501067b045e9ed8d0efbe6e61d)、[device](../device_reference/P002_设备对象结构.md)、[mspi_dev_id](../peripheral_bus_storage_model_reference/P041_mspi_dev_id_结构体.md)、[mspi_dev_cfg_mask](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga71c447d059acf7a8055c380243f3a647)、[mspi_dev_cfg](../peripheral_bus_storage_model_reference/P040_mspi_dev_cfg_结构体.md)。

使用设备特定参数配置 MSPI 控制器。

<a id="r_gadd66b118b76a4ee7ef252afc6b830bfa"></a>

```c
typedef int(* mspi_api_get_channel_status) (const struct device *controller, uint8_t ch)
```

相关声明：[mspi_api_get_channel_status](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface__backend.html#gadd66b118b76a4ee7ef252afc6b830bfa)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

查询通道是否就绪。

<a id="r_ga17b551f4d9f980fde8eabcaae3318617"></a>

```c
typedef int(* mspi_api_transceive) (const struct device *controller, const struct mspi_dev_id *dev_id, const struct mspi_xfer *req)
```

相关声明：[mspi_api_transceive](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface__backend.html#ga17b551f4d9f980fde8eabcaae3318617)、[device](../device_reference/P002_设备对象结构.md)、[mspi_dev_id](../peripheral_bus_storage_model_reference/P041_mspi_dev_id_结构体.md)、[mspi_xfer](../peripheral_bus_storage_model_reference/P050_mspi_xfer_结构体.md)。

通过 MSPI 执行传输请求。

<a id="r_gad6d65ef0d523f22592ff17c04698f663"></a>

```c
typedef int(* mspi_api_register_callback) (const struct device *controller, const struct mspi_dev_id *dev_id, const enum mspi_bus_event evt_type, mspi_callback_handler_t cb, struct mspi_callback_context *ctx)
```

相关声明：[mspi_api_register_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface__backend.html#gad6d65ef0d523f22592ff17c04698f663)、[device](../device_reference/P002_设备对象结构.md)、[mspi_dev_id](../peripheral_bus_storage_model_reference/P041_mspi_dev_id_结构体.md)、[mspi_bus_event](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga4cd05950729893e08ef0d4a12e2242d5)、[mspi_callback_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__callback__api.html#ga29421f748fdb89c823e1a48ff69cf0f4)、[mspi_callback_context](../peripheral_bus_storage_model_reference/P037_mspi_callback_context_结构体.md)。

注册 MSPI 回调函数。

<a id="r_ga002c5d3cc7d6691130dee0f42b928894"></a>

```c
typedef int(* mspi_api_memmap_config) (const struct device *controller, const struct mspi_dev_id *dev_id, const struct mspi_memmap_cfg *memmap_cfg)
```

相关声明：[mspi_api_memmap_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface__backend.html#ga002c5d3cc7d6691130dee0f42b928894)、[device](../device_reference/P002_设备对象结构.md)、[mspi_dev_id](../peripheral_bus_storage_model_reference/P041_mspi_dev_id_结构体.md)、[mspi_memmap_cfg](../peripheral_bus_storage_model_reference/P047_mspi_memmap_cfg_结构体.md)。

配置 MSPI 内存映射（Memory map）设置。

<a id="r_ga092c8bb0879977a8cc8eea5d1662c34b"></a>

```c
typedef int(* mspi_api_scramble_config) (const struct device *controller, const struct mspi_dev_id *dev_id, const struct mspi_scramble_cfg *scramble_cfg)
```

相关声明：[mspi_api_scramble_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface__backend.html#ga092c8bb0879977a8cc8eea5d1662c34b)、[device](../device_reference/P002_设备对象结构.md)、[mspi_dev_id](../peripheral_bus_storage_model_reference/P041_mspi_dev_id_结构体.md)、[mspi_scramble_cfg](../peripheral_bus_storage_model_reference/P048_mspi_scramble_cfg_结构体.md)。

配置 MSPI 扰码（Scrambling）设置。

<a id="r_ga407713e07f23756564814402342c9c97"></a>

```c
typedef int(* mspi_api_timing_config) (const struct device *controller, const struct mspi_dev_id *dev_id, const uint32_t param_mask, void *timing_cfg)
```

相关声明：[mspi_api_timing_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface__backend.html#ga407713e07f23756564814402342c9c97)、[device](../device_reference/P002_设备对象结构.md)、[mspi_dev_id](../peripheral_bus_storage_model_reference/P041_mspi_dev_id_结构体.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

配置 MSPI 时序（Timing）设置。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 17.4\_枚举（Enumerations）

<a id="r_ga3f211cd81e05cb9ee073a2722f6b22d8"></a>

```c
enum mspi_op_mode { MSPI_OP_MODE_CONTROLLER = 0 , MSPI_OP_MODE_PERIPHERAL = 1 }
```

相关声明：[mspi_op_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga3f211cd81e05cb9ee073a2722f6b22d8)、[MSPI_OP_MODE_CONTROLLER](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga3f211cd81e05cb9ee073a2722f6b22d8a6a862f1d9931725be7789bd982d2937a)、[MSPI_OP_MODE_PERIPHERAL](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga3f211cd81e05cb9ee073a2722f6b22d8a11af11e286399c7e2f1fbcadca44ea83)。

MSPI 工作模式（Operational mode）。

<a id="r_ga20e348d7a9f1f9b32078a3bf6c4e82b9"></a>

```c
enum mspi_duplex { MSPI_HALF_DUPLEX = 0 , MSPI_FULL_DUPLEX = 1 }
```

相关声明：[mspi_duplex](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga20e348d7a9f1f9b32078a3bf6c4e82b9)、[MSPI_HALF_DUPLEX](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga20e348d7a9f1f9b32078a3bf6c4e82b9ac05ddc8ca44f1c70d3c3748e21fe80d3)、[MSPI_FULL_DUPLEX](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga20e348d7a9f1f9b32078a3bf6c4e82b9a13a3f16c4273ca6f28671663d0ecf33c)。

MSPI 双工模式（Duplex mode）。

<a id="r_ga904dfc1c800fb9832f7c6200f767f9a5"></a>

```c
enum mspi_io_mode { MSPI_IO_MODE_SINGLE = 0 , MSPI_IO_MODE_DUAL = 1 , MSPI_IO_MODE_DUAL_1_1_2 = 2 , MSPI_IO_MODE_DUAL_1_2_2 = 3 , MSPI_IO_MODE_QUAD = 4 , MSPI_IO_MODE_QUAD_1_1_4 = 5 , MSPI_IO_MODE_QUAD_1_4_4 = 6 , MSPI_IO_MODE_OCTAL = 7 , MSPI_IO_MODE_OCTAL_1_1_8 = 8 , MSPI_IO_MODE_OCTAL_1_8_8 = 9 , MSPI_IO_MODE_HEX = 10 , MSPI_IO_MODE_HEX_8_8_16 = 11 , MSPI_IO_MODE_HEX_8_16_16 = 12 , MSPI_IO_MODE_MAX }
```

相关声明：[mspi_io_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga904dfc1c800fb9832f7c6200f767f9a5)、[MSPI_IO_MODE_SINGLE](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga904dfc1c800fb9832f7c6200f767f9a5a63cf9def8dea959ebfb0f5f19c9235bd)、[MSPI_IO_MODE_DUAL](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga904dfc1c800fb9832f7c6200f767f9a5a9826a30dc94c734cdad9f91148cb8673)、[MSPI_IO_MODE_DUAL_1_1_2](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga904dfc1c800fb9832f7c6200f767f9a5a8225b99a3943f35b1c713af462a2d5da)、[MSPI_IO_MODE_DUAL_1_2_2](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga904dfc1c800fb9832f7c6200f767f9a5aaee80ab69881b09ec6b85dbaaa9e8663)、[MSPI_IO_MODE_QUAD](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga904dfc1c800fb9832f7c6200f767f9a5af65a413ec9c72d6c7acf5154a618870a)、[MSPI_IO_MODE_QUAD_1_1_4](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga904dfc1c800fb9832f7c6200f767f9a5abe9925279cee8433d2b11cc3614c5a5a)、[MSPI_IO_MODE_QUAD_1_4_4](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga904dfc1c800fb9832f7c6200f767f9a5a1b3112af8589ef5e2493fc6545c4945a)、[MSPI_IO_MODE_OCTAL](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga904dfc1c800fb9832f7c6200f767f9a5ac79eb0c07038226a74411ca211d9b725)、[MSPI_IO_MODE_OCTAL_1_1_8](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga904dfc1c800fb9832f7c6200f767f9a5ac70792100fe11a07c020c9825c1cdfbf)、[MSPI_IO_MODE_OCTAL_1_8_8](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga904dfc1c800fb9832f7c6200f767f9a5a1d6b2be620bf17c4daecad66ba011573)、[MSPI_IO_MODE_HEX](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga904dfc1c800fb9832f7c6200f767f9a5a1882d6c9772a1fa1e9e255fe3883d86b)、[MSPI_IO_MODE_HEX_8_8_16](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga904dfc1c800fb9832f7c6200f767f9a5ade6a4a01f3281e5331b3e16f1222eb02)、[MSPI_IO_MODE_HEX_8_16_16](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga904dfc1c800fb9832f7c6200f767f9a5a49283124787af5787d64c71bf38e3caa)、[MSPI_IO_MODE_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga904dfc1c800fb9832f7c6200f767f9a5a9f726ce3043c03703d48bcdc45edcbdb)。

MSPI I/O 模式能力。`1_4_4` 等后缀表示命令、地址和数据阶段分别使用的线路数量。

<a id="r_gaa2131d9846bbfd74488a6ae1c2003e68"></a>

```c
enum mspi_data_rate { MSPI_DATA_RATE_SINGLE = 0 , MSPI_DATA_RATE_S_S_D = 1 , MSPI_DATA_RATE_S_D_D = 2 , MSPI_DATA_RATE_DUAL = 3 , MSPI_DATA_RATE_MAX }
```

相关声明：[mspi_data_rate](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gaa2131d9846bbfd74488a6ae1c2003e68)、[MSPI_DATA_RATE_SINGLE](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ggaa2131d9846bbfd74488a6ae1c2003e68a0e0a4b9bfda5f88df8a2fae13281e5e0)、[MSPI_DATA_RATE_S_S_D](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ggaa2131d9846bbfd74488a6ae1c2003e68a388bbd530a438507dbfa9208ec1ebf39)、[MSPI_DATA_RATE_S_D_D](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ggaa2131d9846bbfd74488a6ae1c2003e68a8cea9da4829a0769e3be8b8a32b79984)、[MSPI_DATA_RATE_DUAL](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ggaa2131d9846bbfd74488a6ae1c2003e68a96f82a24b684a7debe0ac32070fa53bc)、[MSPI_DATA_RATE_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ggaa2131d9846bbfd74488a6ae1c2003e68a51f3574f42456a11cc3fcd17c1195dd9)。

MSPI 数据速率能力。`SINGLE` 表示所有阶段均采用单数据速率（Single data rate）。

<a id="r_ga704e4d3759d3261b4468e9d9900e578c"></a>

```c
enum mspi_cpp_mode { MSPI_CPP_MODE_0 = 0 , MSPI_CPP_MODE_1 = 1 , MSPI_CPP_MODE_2 = 2 , MSPI_CPP_MODE_3 = 3 }
```

相关声明：[mspi_cpp_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga704e4d3759d3261b4468e9d9900e578c)、[MSPI_CPP_MODE_0](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga704e4d3759d3261b4468e9d9900e578cac1c3516819a027f50941e435f54fba90)、[MSPI_CPP_MODE_1](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga704e4d3759d3261b4468e9d9900e578ca8c93d56778ea1cbf901db1a4b9fee870)、[MSPI_CPP_MODE_2](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga704e4d3759d3261b4468e9d9900e578cabbde8c1ad9a5a8a9a3ca4ce33e2c0705)、[MSPI_CPP_MODE_3](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga704e4d3759d3261b4468e9d9900e578ca415e431b25ac4a12f35b139ccb77ba48)。

MSPI 极性与相位模式（Polarity & Phase Modes）。

<a id="r_ga3625cde1379e66cb66a8cb3803ab2e44"></a>

```c
enum mspi_endian { MSPI_XFER_LITTLE_ENDIAN = 0 , MSPI_XFER_BIG_ENDIAN = 1 }
```

相关声明：[mspi_endian](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga3625cde1379e66cb66a8cb3803ab2e44)、[MSPI_XFER_LITTLE_ENDIAN](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga3625cde1379e66cb66a8cb3803ab2e44acdde9f8c7517e287e2066c394593d345)、[MSPI_XFER_BIG_ENDIAN](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga3625cde1379e66cb66a8cb3803ab2e44a08e9349361779ce246bb7da6a1f3012d)。

MSPI 字节序（Endianness）。

<a id="r_ga283275f86fe186f4b5e30110ae0d506b"></a>

```c
enum mspi_ce_polarity { MSPI_CE_ACTIVE_LOW = 0 , MSPI_CE_ACTIVE_HIGH = 1 }
```

相关声明：[mspi_ce_polarity](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga283275f86fe186f4b5e30110ae0d506b)、[MSPI_CE_ACTIVE_LOW](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga283275f86fe186f4b5e30110ae0d506bab36e66d82b05449ed6ce5b6ebc8e2bae)、[MSPI_CE_ACTIVE_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga283275f86fe186f4b5e30110ae0d506ba375e0b870800e0982b3715417e109a22)。

MSPI 片选使能（Chip enable）极性。

<a id="r_ga4cd05950729893e08ef0d4a12e2242d5"></a>

```c
enum mspi_bus_event { MSPI_BUS_RESET = 0 , MSPI_BUS_ERROR = 1 , MSPI_BUS_XFER_COMPLETE = 2 , MSPI_BUS_TIMEOUT = 3 , MSPI_BUS_EVENT_MAX }
```

相关声明：[mspi_bus_event](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga4cd05950729893e08ef0d4a12e2242d5)、[MSPI_BUS_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga4cd05950729893e08ef0d4a12e2242d5afb1c2030d871cbbaa4341df7989a5a64)、[MSPI_BUS_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga4cd05950729893e08ef0d4a12e2242d5aeeaf87802ecc90ada4c39f65fc0e8af0)、[MSPI_BUS_XFER_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga4cd05950729893e08ef0d4a12e2242d5ad47099019f15f97d83bc6435e5e76a61)、[MSPI_BUS_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga4cd05950729893e08ef0d4a12e2242d5a9c538a902c3e5fa1086c0f0fcee4b7e6)、[MSPI_BUS_EVENT_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga4cd05950729893e08ef0d4a12e2242d5a325aa40170de5621e89aa2def557f85a)。

MSPI 总线事件。

<a id="r_gab33e9840b0937c944f4e1a2525534cb1"></a>

```c
enum mspi_bus_event_cb_mask { MSPI_BUS_NO_CB = 0 , MSPI_BUS_RESET_CB = BIT(0) , MSPI_BUS_ERROR_CB = BIT(1) , MSPI_BUS_XFER_COMPLETE_CB = BIT(2) , MSPI_BUS_TIMEOUT_CB = BIT(3) }
```

相关声明：[mspi_bus_event_cb_mask](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gab33e9840b0937c944f4e1a2525534cb1)、[MSPI_BUS_NO_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ggab33e9840b0937c944f4e1a2525534cb1aac3e8481082214c0d995ce3c3b452277)、[MSPI_BUS_RESET_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ggab33e9840b0937c944f4e1a2525534cb1a63fb981aab764d752c1166fc112094a1)、[MSPI_BUS_ERROR_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ggab33e9840b0937c944f4e1a2525534cb1a5cff8419a9236cc835a62b124debe498)、[MSPI_BUS_XFER_COMPLETE_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ggab33e9840b0937c944f4e1a2525534cb1aa315ad9c5ba56979914b21208920aad7)、[MSPI_BUS_TIMEOUT_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ggab33e9840b0937c944f4e1a2525534cb1af587e68d07441f3262ab164f48e783c0)。

MSPI 总线事件回调掩码。这是初步列表，与 `mspi_bus_event` 相同。

<a id="r_ga116259bbb1d12a10c2ba9e6051f2f000"></a>

```c
enum mspi_xfer_mode { MSPI_PIO , MSPI_DMA }
```

相关声明：[mspi_xfer_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga116259bbb1d12a10c2ba9e6051f2f000)、[MSPI_PIO](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga116259bbb1d12a10c2ba9e6051f2f000abea5c6920a3e81fe332c2a76e4d838a1)、[MSPI_DMA](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga116259bbb1d12a10c2ba9e6051f2f000a5a7235fe9c633206906d76d329f623a8)。

MSPI 传输模式。

<a id="r_ga632af162124ca2959a21ca3759e1cc9e"></a>

```c
enum mspi_xfer_priority { MSPI_XFER_PRIORITY_LOW , MSPI_XFER_PRIORITY_MEDIUM , MSPI_XFER_PRIORITY_HIGH }
```

相关声明：[mspi_xfer_priority](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga632af162124ca2959a21ca3759e1cc9e)、[MSPI_XFER_PRIORITY_LOW](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga632af162124ca2959a21ca3759e1cc9ea31222dc35adf9bed70571b9b640aca97)、[MSPI_XFER_PRIORITY_MEDIUM](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga632af162124ca2959a21ca3759e1cc9ea66753cdf13762a1dd995638ff71544e0)、[MSPI_XFER_PRIORITY_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga632af162124ca2959a21ca3759e1cc9ea3004e6ae8226294b669f2207e928f928)。

MSPI 传输优先级（Priority）。这是通常与 DMA 配合使用的初步优先级列表。

<a id="r_ga498f10591acf5dc7ec88e0aa98e537d6"></a>

```c
enum mspi_xfer_direction { MSPI_RX , MSPI_TX }
```

相关声明：[mspi_xfer_direction](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga498f10591acf5dc7ec88e0aa98e537d6)、[MSPI_RX](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga498f10591acf5dc7ec88e0aa98e537d6a044160eb569add203f06d963f57d3541)、[MSPI_TX](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga498f10591acf5dc7ec88e0aa98e537d6a213d4457305ab45d31b9c06ec85d2b8a)。

MSPI 传输方向。

<a id="r_ga71c447d059acf7a8055c380243f3a647"></a>

```c
enum mspi_dev_cfg_mask { MSPI_DEVICE_CONFIG_NONE = 0 , MSPI_DEVICE_CONFIG_CE_NUM = BIT(0) , MSPI_DEVICE_CONFIG_FREQUENCY = BIT(1) , MSPI_DEVICE_CONFIG_IO_MODE = BIT(2) , MSPI_DEVICE_CONFIG_DATA_RATE = BIT(3) , MSPI_DEVICE_CONFIG_CPP = BIT(4) , MSPI_DEVICE_CONFIG_ENDIAN = BIT(5) , MSPI_DEVICE_CONFIG_CE_POL = BIT(6) , MSPI_DEVICE_CONFIG_DQS = BIT(7) , MSPI_DEVICE_CONFIG_RX_DUMMY = BIT(8) , MSPI_DEVICE_CONFIG_TX_DUMMY = BIT(9) , MSPI_DEVICE_CONFIG_READ_CMD = BIT(10) , MSPI_DEVICE_CONFIG_WRITE_CMD = BIT(11) , MSPI_DEVICE_CONFIG_CMD_LEN = BIT(12) , MSPI_DEVICE_CONFIG_ADDR_LEN = BIT(13) , MSPI_DEVICE_CONFIG_MEM_BOUND = BIT(14) , MSPI_DEVICE_CONFIG_BREAK_TIME = BIT(15) , MSPI_DEVICE_CONFIG_ALL = BIT_MASK(16) }
```

相关声明：[mspi_dev_cfg_mask](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga71c447d059acf7a8055c380243f3a647)、[MSPI_DEVICE_CONFIG_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647acc1d59bd6682933d364f060f31f26878)、[MSPI_DEVICE_CONFIG_CE_NUM](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647a4a476e51f0d3613aab1bc9c1b335bab2)、[MSPI_DEVICE_CONFIG_FREQUENCY](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647a135b081210bd5aabf5b610fe90212809)、[MSPI_DEVICE_CONFIG_IO_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647a4aba5c75b43e1a87c66e940069b5b27f)、[MSPI_DEVICE_CONFIG_DATA_RATE](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647a0e954604ea419f6a4fdea59e620bdcd9)、[MSPI_DEVICE_CONFIG_CPP](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647a0d7032e045c80ca266e98f8c6684af65)、[MSPI_DEVICE_CONFIG_ENDIAN](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647aba8ef6308b3e06a2ace1cc0f225d66ca)、[MSPI_DEVICE_CONFIG_CE_POL](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647a51f46405fe8923a8b0c39bc2aad1ba0b)、[MSPI_DEVICE_CONFIG_DQS](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647a56ceb1ba2a93a626623a13f148282537)、[MSPI_DEVICE_CONFIG_RX_DUMMY](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647a13385127a309507ff01559122e03623a)、[MSPI_DEVICE_CONFIG_TX_DUMMY](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647a60b857bd38b0cced89462771edccd9f5)、[MSPI_DEVICE_CONFIG_READ_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647ae7c13ba10174e6f3f90161af69890872)、[MSPI_DEVICE_CONFIG_WRITE_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647a99f486fd1f01684ac232d503af1abf2b)、[MSPI_DEVICE_CONFIG_CMD_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647a1a2e21a3cbf0ee42977cc8a43efd3fac)、[MSPI_DEVICE_CONFIG_ADDR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647aa2ba135123fe9c89ce50fd86dfea759b)、[MSPI_DEVICE_CONFIG_MEM_BOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647ad07911eacaa2bde26a497c391e5c9946)、[MSPI_DEVICE_CONFIG_BREAK_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647acdea4576df8e6d7d48cc289305237120)、[MSPI_DEVICE_CONFIG_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647a67ae821a16a6280aca165ebf67bd2489)。

MSPI 控制器设备特定配置掩码。

<a id="r_gac127ef78c7b66c7eebe03782abf08c40"></a>

```c
enum mspi_memmap_permit { MSPI_MEMMAP_READ_WRITE = 0 , MSPI_MEMMAP_READ_ONLY = 1 }
```

相关声明：[mspi_memmap_permit](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gac127ef78c7b66c7eebe03782abf08c40)、[MSPI_MEMMAP_READ_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ggac127ef78c7b66c7eebe03782abf08c40a5e34cb52b8e8475f9457a9cab7a424ed)、[MSPI_MEMMAP_READ_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ggac127ef78c7b66c7eebe03782abf08c40aacecd5fab6e2ed50be75d882eaadadd6)。

MSPI 内存映射访问权限（Access permissions）。

<a id="r_gaa25a7f97ab3437d4544832a0e7474f4a"></a>

```c
enum mspi_timing_param { MSPI_TIMING_PARAM_DUMMY }
```

相关声明：[mspi_timing_param](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__configure__api.html#gaa25a7f97ab3437d4544832a0e7474f4a)、[MSPI_TIMING_PARAM_DUMMY](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__configure__api.html#ggaa25a7f97ab3437d4544832a0e7474f4aafae0ccedcd3b8f05e798037bf5414237)。

时序参数的占位项（Stub）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 17.5\_函数（Functions）

<a id="r_ga46c2b98e99ecea045c1ecac4bdf3f087"></a>

```c
int mspi_config (const struct mspi_dt_spec *spec)
```

相关声明：[mspi_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__configure__api.html#ga46c2b98e99ecea045c1ecac4bdf3f087)、[mspi_dt_spec](../peripheral_bus_storage_model_reference/P043_mspi_dt_spec_结构体.md)。

配置 MSPI 控制器。

<a id="r_gaa3c1eae8b3000c9bafcc26f14a8beb8b"></a>

```c
int mspi_dev_config (const struct device *controller, const struct mspi_dev_id *dev_id, const enum mspi_dev_cfg_mask param_mask, const struct mspi_dev_cfg *cfg)
```

相关声明：[mspi_dev_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__configure__api.html#gaa3c1eae8b3000c9bafcc26f14a8beb8b)、[device](../device_reference/P002_设备对象结构.md)、[mspi_dev_id](../peripheral_bus_storage_model_reference/P041_mspi_dev_id_结构体.md)、[mspi_dev_cfg_mask](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga71c447d059acf7a8055c380243f3a647)、[mspi_dev_cfg](../peripheral_bus_storage_model_reference/P040_mspi_dev_cfg_结构体.md)。

使用设备特定参数配置 MSPI 控制器。

<a id="r_ga957b6ecd96c9f942f75bbe500898930d"></a>

```c
int mspi_get_channel_status (const struct device *controller, uint8_t ch)
```

相关声明：[mspi_get_channel_status](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__configure__api.html#ga957b6ecd96c9f942f75bbe500898930d)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

查询通道是否就绪。

<a id="r_ga8c98c73e322c575b759ce911cc115129"></a>

```c
int mspi_transceive (const struct device *controller, const struct mspi_dev_id *dev_id, const struct mspi_xfer *req)
```

相关声明：[mspi_transceive](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__transfer__api.html#ga8c98c73e322c575b759ce911cc115129)、[device](../device_reference/P002_设备对象结构.md)、[mspi_dev_id](../peripheral_bus_storage_model_reference/P041_mspi_dev_id_结构体.md)、[mspi_xfer](../peripheral_bus_storage_model_reference/P050_mspi_xfer_结构体.md)。

通过 MSPI 执行传输请求。

<a id="r_gaa656820a834bcde0d06041cff8f0d5e1"></a>

```c
static int mspi_transceive_data_only (const struct device *controller, const struct mspi_dev_id *dev_id, const struct mspi_xfer_packet *packets, uint32_t num_packet, enum mspi_xfer_mode xfer_mode, bool async, uint32_t timeout)
```

相关声明：[mspi_transceive_data_only](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__transfer__api.html#gaa656820a834bcde0d06041cff8f0d5e1)、[device](../device_reference/P002_设备对象结构.md)、[mspi_dev_id](../peripheral_bus_storage_model_reference/P041_mspi_dev_id_结构体.md)、[mspi_xfer_packet](../peripheral_bus_storage_model_reference/P051_mspi_xfer_packet_结构体.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[mspi_xfer_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga116259bbb1d12a10c2ba9e6051f2f000)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

通过 MSPI 传输数据，不包含命令阶段和地址阶段。

<a id="r_gac025129882f814b59d5726c01f0138ce"></a>

```c
int mspi_memmap_config (const struct device *controller, const struct mspi_dev_id *dev_id, const struct mspi_memmap_cfg *cfg)
```

相关声明：[mspi_memmap_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__configure__api.html#gac025129882f814b59d5726c01f0138ce)、[device](../device_reference/P002_设备对象结构.md)、[mspi_dev_id](../peripheral_bus_storage_model_reference/P041_mspi_dev_id_结构体.md)、[mspi_memmap_cfg](../peripheral_bus_storage_model_reference/P047_mspi_memmap_cfg_结构体.md)。

配置 MSPI 内存映射（Memory map）设置。

<a id="r_gacf287e08b6ce4898524884e8de22b806"></a>

```c
int mspi_scramble_config (const struct device *controller, const struct mspi_dev_id *dev_id, const struct mspi_scramble_cfg *cfg)
```

相关声明：[mspi_scramble_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__configure__api.html#gacf287e08b6ce4898524884e8de22b806)、[device](../device_reference/P002_设备对象结构.md)、[mspi_dev_id](../peripheral_bus_storage_model_reference/P041_mspi_dev_id_结构体.md)、[mspi_scramble_cfg](../peripheral_bus_storage_model_reference/P048_mspi_scramble_cfg_结构体.md)。

配置 MSPI 扰码（Scrambling）设置。

<a id="r_gaff82af1cfc99b9e78cec17ea27f79ab6"></a>

```c
int mspi_timing_config (const struct device *controller, const struct mspi_dev_id *dev_id, const uint32_t param_mask, void *cfg)
```

相关声明：[mspi_timing_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__configure__api.html#gaff82af1cfc99b9e78cec17ea27f79ab6)、[device](../device_reference/P002_设备对象结构.md)、[mspi_dev_id](../peripheral_bus_storage_model_reference/P041_mspi_dev_id_结构体.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

配置 MSPI 时序（Timing）设置。

<a id="r_ga967f5fed63f08ac2d5a88625b030cd14"></a>

```c
static int mspi_register_callback (const struct device *controller, const struct mspi_dev_id *dev_id, const enum mspi_bus_event evt_type, mspi_callback_handler_t cb, struct mspi_callback_context *ctx)
```

相关声明：[mspi_register_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__callback__api.html#ga967f5fed63f08ac2d5a88625b030cd14)、[device](../device_reference/P002_设备对象结构.md)、[mspi_dev_id](../peripheral_bus_storage_model_reference/P041_mspi_dev_id_结构体.md)、[mspi_bus_event](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga4cd05950729893e08ef0d4a12e2242d5)、[mspi_callback_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__callback__api.html#ga29421f748fdb89c823e1a48ff69cf0f4)、[mspi_callback_context](../peripheral_bus_storage_model_reference/P037_mspi_callback_context_结构体.md)。

注册 MSPI 回调函数。


## 17.6\_原页交叉引用（Cross References）

- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/drivers/gpio.h](../gpio_driver_reference/P002_GPIO驱动头文件源码.md)
- [zephyr/drivers/mspi/devicetree.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mspi_2devicetree_8h_source.html)
- [zephyr/sys/util_macro.h](../util_reference/P005_宏工具头文件源码.md)
- [查看此文件的源码](https://docs.zephyrproject.org/latest/doxygen/html/mspi_8h_source.html)
- [mspi_timing_cfg](../peripheral_bus_storage_model_reference/P049_mspi_timing_cfg_结构体.md)
- [mspi_dev_id](../peripheral_bus_storage_model_reference/P041_mspi_dev_id_结构体.md)
- [mspi_cfg](../peripheral_bus_storage_model_reference/P039_mspi_cfg_结构体.md)
- [mspi_dt_spec](../peripheral_bus_storage_model_reference/P043_mspi_dt_spec_结构体.md)
- [mspi_dev_cfg](../peripheral_bus_storage_model_reference/P040_mspi_dev_cfg_结构体.md)
- [mspi_memmap_cfg](../peripheral_bus_storage_model_reference/P047_mspi_memmap_cfg_结构体.md)
- [mspi_scramble_cfg](../peripheral_bus_storage_model_reference/P048_mspi_scramble_cfg_结构体.md)
- [mspi_ce_control](../peripheral_bus_storage_model_reference/P038_mspi_ce_control_结构体.md)
- [mspi_xfer_packet](../peripheral_bus_storage_model_reference/P051_mspi_xfer_packet_结构体.md)
- [mspi_xfer](../peripheral_bus_storage_model_reference/P050_mspi_xfer_结构体.md)
- [mspi_event_data](../peripheral_bus_storage_model_reference/P046_mspi_event_data_结构体.md)
- [mspi_event](../peripheral_bus_storage_model_reference/P045_mspi_event_结构体.md)
- [mspi_callback_context](../peripheral_bus_storage_model_reference/P037_mspi_callback_context_结构体.md)
- [mspi_driver_api](../peripheral_bus_storage_model_reference/P042_mspi_driver_api_结构体.md)
- [MSPI_MEMMAP_CFG_STRUCT_DECLARE](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__util.html#gadce17ebaa26cfd2b59fadab2a7b2a788)
- [MSPI_MEMMAP_BASE_ADDR_DECLARE](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__util.html#gae9b12392a7cc1f6b746adddec56e0b85)
- [MSPI_SCRAMBLE_CFG_STRUCT_DECLARE](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__util.html#ga8c55eacfe36f484bb5b3f82f8918aa79)
- [MSPI_TIMING_CFG_STRUCT_DECLARE](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__util.html#ga118cb8d67bde11040aa8369ff88e4b6b)
- [MSPI_TIMING_PARAM_DECLARE](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__util.html#ga4c88adce60d915c85972fa2cfaf7177e)
- [MSPI_OPTIONAL_CFG_STRUCT_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__util.html#ga7b2c02a81ae6d670680b86088624dc17)
- [MSPI_MEMMAP_BASE_ADDR_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__util.html#ga2da665f679f0c538e58ebff4005daec3)
- [mspi_callback_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__callback__api.html#ga29421f748fdb89c823e1a48ff69cf0f4)
- [mspi_api_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface__backend.html#ga2ff9209634fb241e2f7323e749df612e)
- [mspi_api_dev_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface__backend.html#ga7e3bae501067b045e9ed8d0efbe6e61d)
- [device](../device_reference/P002_设备对象结构.md)
- [mspi_dev_cfg_mask](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga71c447d059acf7a8055c380243f3a647)
- [mspi_api_get_channel_status](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface__backend.html#gadd66b118b76a4ee7ef252afc6b830bfa)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mspi_api_transceive](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface__backend.html#ga17b551f4d9f980fde8eabcaae3318617)
- [mspi_api_register_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface__backend.html#gad6d65ef0d523f22592ff17c04698f663)
- [mspi_bus_event](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga4cd05950729893e08ef0d4a12e2242d5)
- [mspi_api_memmap_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface__backend.html#ga002c5d3cc7d6691130dee0f42b928894)
- [mspi_api_scramble_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface__backend.html#ga092c8bb0879977a8cc8eea5d1662c34b)
- [mspi_api_timing_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface__backend.html#ga407713e07f23756564814402342c9c97)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [mspi_op_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga3f211cd81e05cb9ee073a2722f6b22d8)
- [MSPI_OP_MODE_CONTROLLER](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga3f211cd81e05cb9ee073a2722f6b22d8a6a862f1d9931725be7789bd982d2937a)
- [MSPI_OP_MODE_PERIPHERAL](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga3f211cd81e05cb9ee073a2722f6b22d8a11af11e286399c7e2f1fbcadca44ea83)
- [mspi_duplex](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga20e348d7a9f1f9b32078a3bf6c4e82b9)
- [MSPI_HALF_DUPLEX](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga20e348d7a9f1f9b32078a3bf6c4e82b9ac05ddc8ca44f1c70d3c3748e21fe80d3)
- [MSPI_FULL_DUPLEX](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga20e348d7a9f1f9b32078a3bf6c4e82b9a13a3f16c4273ca6f28671663d0ecf33c)
- [mspi_io_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga904dfc1c800fb9832f7c6200f767f9a5)
- [MSPI_IO_MODE_SINGLE](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga904dfc1c800fb9832f7c6200f767f9a5a63cf9def8dea959ebfb0f5f19c9235bd)
- [MSPI_IO_MODE_DUAL](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga904dfc1c800fb9832f7c6200f767f9a5a9826a30dc94c734cdad9f91148cb8673)
- [MSPI_IO_MODE_DUAL_1_1_2](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga904dfc1c800fb9832f7c6200f767f9a5a8225b99a3943f35b1c713af462a2d5da)
- [MSPI_IO_MODE_DUAL_1_2_2](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga904dfc1c800fb9832f7c6200f767f9a5aaee80ab69881b09ec6b85dbaaa9e8663)
- [MSPI_IO_MODE_QUAD](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga904dfc1c800fb9832f7c6200f767f9a5af65a413ec9c72d6c7acf5154a618870a)
- [MSPI_IO_MODE_QUAD_1_1_4](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga904dfc1c800fb9832f7c6200f767f9a5abe9925279cee8433d2b11cc3614c5a5a)
- [MSPI_IO_MODE_QUAD_1_4_4](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga904dfc1c800fb9832f7c6200f767f9a5a1b3112af8589ef5e2493fc6545c4945a)
- [MSPI_IO_MODE_OCTAL](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga904dfc1c800fb9832f7c6200f767f9a5ac79eb0c07038226a74411ca211d9b725)
- [MSPI_IO_MODE_OCTAL_1_1_8](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga904dfc1c800fb9832f7c6200f767f9a5ac70792100fe11a07c020c9825c1cdfbf)
- [MSPI_IO_MODE_OCTAL_1_8_8](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga904dfc1c800fb9832f7c6200f767f9a5a1d6b2be620bf17c4daecad66ba011573)
- [MSPI_IO_MODE_HEX](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga904dfc1c800fb9832f7c6200f767f9a5a1882d6c9772a1fa1e9e255fe3883d86b)
- [MSPI_IO_MODE_HEX_8_8_16](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga904dfc1c800fb9832f7c6200f767f9a5ade6a4a01f3281e5331b3e16f1222eb02)
- [MSPI_IO_MODE_HEX_8_16_16](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga904dfc1c800fb9832f7c6200f767f9a5a49283124787af5787d64c71bf38e3caa)
- [MSPI_IO_MODE_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga904dfc1c800fb9832f7c6200f767f9a5a9f726ce3043c03703d48bcdc45edcbdb)
- [mspi_data_rate](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gaa2131d9846bbfd74488a6ae1c2003e68)
- [MSPI_DATA_RATE_SINGLE](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ggaa2131d9846bbfd74488a6ae1c2003e68a0e0a4b9bfda5f88df8a2fae13281e5e0)
- [MSPI_DATA_RATE_S_S_D](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ggaa2131d9846bbfd74488a6ae1c2003e68a388bbd530a438507dbfa9208ec1ebf39)
- [MSPI_DATA_RATE_S_D_D](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ggaa2131d9846bbfd74488a6ae1c2003e68a8cea9da4829a0769e3be8b8a32b79984)
- [MSPI_DATA_RATE_DUAL](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ggaa2131d9846bbfd74488a6ae1c2003e68a96f82a24b684a7debe0ac32070fa53bc)
- [MSPI_DATA_RATE_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ggaa2131d9846bbfd74488a6ae1c2003e68a51f3574f42456a11cc3fcd17c1195dd9)
- [mspi_cpp_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga704e4d3759d3261b4468e9d9900e578c)
- [MSPI_CPP_MODE_0](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga704e4d3759d3261b4468e9d9900e578cac1c3516819a027f50941e435f54fba90)
- [MSPI_CPP_MODE_1](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga704e4d3759d3261b4468e9d9900e578ca8c93d56778ea1cbf901db1a4b9fee870)
- [MSPI_CPP_MODE_2](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga704e4d3759d3261b4468e9d9900e578cabbde8c1ad9a5a8a9a3ca4ce33e2c0705)
- [MSPI_CPP_MODE_3](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga704e4d3759d3261b4468e9d9900e578ca415e431b25ac4a12f35b139ccb77ba48)
- [mspi_endian](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga3625cde1379e66cb66a8cb3803ab2e44)
- [MSPI_XFER_LITTLE_ENDIAN](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga3625cde1379e66cb66a8cb3803ab2e44acdde9f8c7517e287e2066c394593d345)
- [MSPI_XFER_BIG_ENDIAN](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga3625cde1379e66cb66a8cb3803ab2e44a08e9349361779ce246bb7da6a1f3012d)
- [mspi_ce_polarity](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga283275f86fe186f4b5e30110ae0d506b)
- [MSPI_CE_ACTIVE_LOW](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga283275f86fe186f4b5e30110ae0d506bab36e66d82b05449ed6ce5b6ebc8e2bae)
- [MSPI_CE_ACTIVE_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga283275f86fe186f4b5e30110ae0d506ba375e0b870800e0982b3715417e109a22)
- [MSPI_BUS_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga4cd05950729893e08ef0d4a12e2242d5afb1c2030d871cbbaa4341df7989a5a64)
- [MSPI_BUS_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga4cd05950729893e08ef0d4a12e2242d5aeeaf87802ecc90ada4c39f65fc0e8af0)
- [MSPI_BUS_XFER_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga4cd05950729893e08ef0d4a12e2242d5ad47099019f15f97d83bc6435e5e76a61)
- [MSPI_BUS_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga4cd05950729893e08ef0d4a12e2242d5a9c538a902c3e5fa1086c0f0fcee4b7e6)
- [MSPI_BUS_EVENT_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga4cd05950729893e08ef0d4a12e2242d5a325aa40170de5621e89aa2def557f85a)
- [mspi_bus_event_cb_mask](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gab33e9840b0937c944f4e1a2525534cb1)
- [MSPI_BUS_NO_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ggab33e9840b0937c944f4e1a2525534cb1aac3e8481082214c0d995ce3c3b452277)
- [MSPI_BUS_RESET_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ggab33e9840b0937c944f4e1a2525534cb1a63fb981aab764d752c1166fc112094a1)
- [MSPI_BUS_ERROR_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ggab33e9840b0937c944f4e1a2525534cb1a5cff8419a9236cc835a62b124debe498)
- [MSPI_BUS_XFER_COMPLETE_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ggab33e9840b0937c944f4e1a2525534cb1aa315ad9c5ba56979914b21208920aad7)
- [MSPI_BUS_TIMEOUT_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ggab33e9840b0937c944f4e1a2525534cb1af587e68d07441f3262ab164f48e783c0)
- [mspi_xfer_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga116259bbb1d12a10c2ba9e6051f2f000)
- [MSPI_PIO](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga116259bbb1d12a10c2ba9e6051f2f000abea5c6920a3e81fe332c2a76e4d838a1)
- [MSPI_DMA](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga116259bbb1d12a10c2ba9e6051f2f000a5a7235fe9c633206906d76d329f623a8)
- [mspi_xfer_priority](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga632af162124ca2959a21ca3759e1cc9e)
- [MSPI_XFER_PRIORITY_LOW](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga632af162124ca2959a21ca3759e1cc9ea31222dc35adf9bed70571b9b640aca97)
- [MSPI_XFER_PRIORITY_MEDIUM](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga632af162124ca2959a21ca3759e1cc9ea66753cdf13762a1dd995638ff71544e0)
- [MSPI_XFER_PRIORITY_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga632af162124ca2959a21ca3759e1cc9ea3004e6ae8226294b669f2207e928f928)
- [mspi_xfer_direction](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga498f10591acf5dc7ec88e0aa98e537d6)
- [MSPI_RX](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga498f10591acf5dc7ec88e0aa98e537d6a044160eb569add203f06d963f57d3541)
- [MSPI_TX](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga498f10591acf5dc7ec88e0aa98e537d6a213d4457305ab45d31b9c06ec85d2b8a)
- [MSPI_DEVICE_CONFIG_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647acc1d59bd6682933d364f060f31f26878)
- [MSPI_DEVICE_CONFIG_CE_NUM](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647a4a476e51f0d3613aab1bc9c1b335bab2)
- [MSPI_DEVICE_CONFIG_FREQUENCY](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647a135b081210bd5aabf5b610fe90212809)
- [MSPI_DEVICE_CONFIG_IO_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647a4aba5c75b43e1a87c66e940069b5b27f)
- [MSPI_DEVICE_CONFIG_DATA_RATE](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647a0e954604ea419f6a4fdea59e620bdcd9)
- [MSPI_DEVICE_CONFIG_CPP](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647a0d7032e045c80ca266e98f8c6684af65)
- [MSPI_DEVICE_CONFIG_ENDIAN](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647aba8ef6308b3e06a2ace1cc0f225d66ca)
- [MSPI_DEVICE_CONFIG_CE_POL](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647a51f46405fe8923a8b0c39bc2aad1ba0b)
- [MSPI_DEVICE_CONFIG_DQS](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647a56ceb1ba2a93a626623a13f148282537)
- [MSPI_DEVICE_CONFIG_RX_DUMMY](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647a13385127a309507ff01559122e03623a)
- [MSPI_DEVICE_CONFIG_TX_DUMMY](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647a60b857bd38b0cced89462771edccd9f5)
- [MSPI_DEVICE_CONFIG_READ_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647ae7c13ba10174e6f3f90161af69890872)
- [MSPI_DEVICE_CONFIG_WRITE_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647a99f486fd1f01684ac232d503af1abf2b)
- [MSPI_DEVICE_CONFIG_CMD_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647a1a2e21a3cbf0ee42977cc8a43efd3fac)
- [MSPI_DEVICE_CONFIG_ADDR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647aa2ba135123fe9c89ce50fd86dfea759b)
- [MSPI_DEVICE_CONFIG_MEM_BOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647ad07911eacaa2bde26a497c391e5c9946)
- [MSPI_DEVICE_CONFIG_BREAK_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647acdea4576df8e6d7d48cc289305237120)
- [MSPI_DEVICE_CONFIG_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gga71c447d059acf7a8055c380243f3a647a67ae821a16a6280aca165ebf67bd2489)
- [mspi_memmap_permit](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gac127ef78c7b66c7eebe03782abf08c40)
- [MSPI_MEMMAP_READ_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ggac127ef78c7b66c7eebe03782abf08c40a5e34cb52b8e8475f9457a9cab7a424ed)
- [MSPI_MEMMAP_READ_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ggac127ef78c7b66c7eebe03782abf08c40aacecd5fab6e2ed50be75d882eaadadd6)
- [mspi_timing_param](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__configure__api.html#gaa25a7f97ab3437d4544832a0e7474f4a)
- [MSPI_TIMING_PARAM_DUMMY](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__configure__api.html#ggaa25a7f97ab3437d4544832a0e7474f4aafae0ccedcd3b8f05e798037bf5414237)
- [mspi_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__configure__api.html#ga46c2b98e99ecea045c1ecac4bdf3f087)
- [mspi_dev_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__configure__api.html#gaa3c1eae8b3000c9bafcc26f14a8beb8b)
- [mspi_get_channel_status](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__configure__api.html#ga957b6ecd96c9f942f75bbe500898930d)
- [mspi_transceive](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__transfer__api.html#ga8c98c73e322c575b759ce911cc115129)
- [mspi_transceive_data_only](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__transfer__api.html#gaa656820a834bcde0d06041cff8f0d5e1)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [mspi_memmap_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__configure__api.html#gac025129882f814b59d5726c01f0138ce)
- [mspi_scramble_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__configure__api.html#gacf287e08b6ce4898524884e8de22b806)
- [mspi_timing_config](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__configure__api.html#gaff82af1cfc99b9e78cec17ea27f79ab6)
- [mspi_register_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__callback__api.html#ga967f5fed63f08ac2d5a88625b030cd14)

<a id="header-details"></a>

---

[上一章](P016_zephyr__drivers__mspi__mspi_cadence.h_头文件参考.md) · [返回大纲](大纲.md) · [下一章](P018_zephyr__drivers__mspi__mspi_dw.h_头文件参考.md)
