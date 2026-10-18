---
id: learning.zephyr-docs.peripheral-bus-storage-header-reference.page-5
title: zephyr__drivers__espi_saf.h_头文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/espi__saf_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_zephyr\_\_drivers\_\_espi\_saf.h\_头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/espi__saf_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

eSPI驱动的公共API。

<a id="details"></a>

```c
#include <zephyr/sys/__assert.h>
#include <zephyr/types.h>
#include <zephyr/device.h>
#include <zephyr/syscalls/espi_saf.h>
```

查看此文件的源码。

eSPI驱动的公共API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 5.1\_数据结构（Data Structures）

<a id="r_espi_5Fsaf_5Fcfg"></a>

```c
struct espi_saf_cfg
```

相关声明：[espi_saf_cfg](../peripheral_bus_storage_model_reference/P015_espi_saf_cfg_结构体.md)。

eSPI从设备附属闪存（SAF）的配置参数。

<a id="r_espi_5Fsaf_5Fpacket"></a>

```c
struct espi_saf_packet
```

相关声明：[espi_saf_packet](../peripheral_bus_storage_model_reference/P017_espi_saf_packet_结构体.md)。

eSPI从设备附属闪存（SAF）事务的数据包格式。

<a id="r_espi_5Fsaf_5Fdriver_5Fapi"></a>

```c
struct espi_saf_driver_api
```

相关声明：[espi_saf_driver_api](../peripheral_bus_storage_model_reference/P016_espi_saf_driver_api_结构体.md)。

驱动操作（Driver Operations）：eSPI SAF驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 5.2\_类型定义（Typedefs）

<a id="r_ga5f422a48cf008d7a737ec6a3fd0f0400"></a>

```c
typedef int(* espi_saf_api_config) (const struct device *dev, const struct espi_saf_cfg *cfg)
```

相关声明：[espi_saf_api_config](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface__backend.html#ga5f422a48cf008d7a737ec6a3fd0f0400)、[device](../device_reference/P002_设备对象结构.md)、[espi_saf_cfg](../peripheral_bus_storage_model_reference/P015_espi_saf_cfg_结构体.md)。

配置 eSPI 从设备附接 Flash（SAF）控制器的回调 API。

<a id="r_gaeb3c1ee73f50fd05737f28a75013c2a8"></a>

```c
typedef int(* espi_saf_api_set_protection_regions) (const struct device *dev, const struct espi_saf_protection *pr)
```

相关声明：[espi_saf_api_set_protection_regions](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface__backend.html#gaeb3c1ee73f50fd05737f28a75013c2a8)、[device](../device_reference/P002_设备对象结构.md)。

设置一个或多个 SAF 保护区域的回调 API。

<a id="r_ga03a72ef8a19738d90681114f478ff068"></a>

```c
typedef int(* espi_saf_api_activate) (const struct device *dev)
```

相关声明：[espi_saf_api_activate](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface__backend.html#ga03a72ef8a19738d90681114f478ff068)、[device](../device_reference/P002_设备对象结构.md)。

激活 SAF 模块的回调 API。

<a id="r_ga6ac9186c5b022f79dd8671594450efff"></a>

```c
typedef bool(* espi_saf_api_get_channel_status) (const struct device *dev)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[espi_saf_api_get_channel_status](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface__backend.html#ga6ac9186c5b022f79dd8671594450efff)、[device](../device_reference/P002_设备对象结构.md)。

查询 SAF 是否就绪的回调 API。

<a id="r_ga6154711885b4edc54db016ba9826c176"></a>

```c
typedef int(* espi_saf_api_flash_read) (const struct device *dev, struct espi_saf_packet *pckt)
```

相关声明：[espi_saf_api_flash_read](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface__backend.html#ga6154711885b4edc54db016ba9826c176)、[device](../device_reference/P002_设备对象结构.md)、[espi_saf_packet](../peripheral_bus_storage_model_reference/P017_espi_saf_packet_结构体.md)。

发送从设备附接 Flash 读取请求的回调 API。

<a id="r_ga24498afe1639bd7c5192215dc8bbbed9"></a>

```c
typedef int(* espi_saf_api_flash_write) (const struct device *dev, struct espi_saf_packet *pckt)
```

相关声明：[espi_saf_api_flash_write](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface__backend.html#ga24498afe1639bd7c5192215dc8bbbed9)、[device](../device_reference/P002_设备对象结构.md)、[espi_saf_packet](../peripheral_bus_storage_model_reference/P017_espi_saf_packet_结构体.md)。

发送从设备附接 Flash 写入请求的回调 API。

<a id="r_ga4e8a12a1311d6604a61d1a9e57573e17"></a>

```c
typedef int(* espi_saf_api_flash_erase) (const struct device *dev, struct espi_saf_packet *pckt)
```

相关声明：[espi_saf_api_flash_erase](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface__backend.html#ga4e8a12a1311d6604a61d1a9e57573e17)、[device](../device_reference/P002_设备对象结构.md)、[espi_saf_packet](../peripheral_bus_storage_model_reference/P017_espi_saf_packet_结构体.md)。

发送从设备附接 Flash 擦除请求的回调 API。

<a id="r_ga7c1aef03f238ced4e64c6e3be7ad643c"></a>

```c
typedef int(* espi_saf_api_flash_unsuccess) (const struct device *dev, struct espi_saf_packet *pckt)
```

相关声明：[espi_saf_api_flash_unsuccess](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface__backend.html#ga7c1aef03f238ced4e64c6e3be7ad643c)、[device](../device_reference/P002_设备对象结构.md)、[espi_saf_packet](../peripheral_bus_storage_model_reference/P017_espi_saf_packet_结构体.md)。

针对从设备附接 Flash 返回未成功完成（Unsuccessful completion）响应的回调 API。

<a id="r_ga20ae708179a104c9334fe8fd554e5e05"></a>

```c
typedef int(* espi_saf_api_manage_callback) (const struct device *dev, struct espi_callback *callback, bool set)
```

相关声明：[espi_saf_api_manage_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface__backend.html#ga20ae708179a104c9334fe8fd554e5e05)、[device](../device_reference/P002_设备对象结构.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

管理应用程序回调的回调 API，包括添加和移除。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 5.3\_枚举（Enumerations）

<a id="r_ga66bd7ad63051eefa407df554d5241d9e"></a>

```c
enum espi_taf_event { ESPI_TAF_EVENT_NO_REQUEST = 0 , ESPI_TAF_EVENT_HOST_REQUEST , ESPI_TAF_EVENT_EC0_REQUEST , ESPI_TAF_EVENT_MAX_REQUEST }
```

相关声明：[espi_taf_event](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#ga66bd7ad63051eefa407df554d5241d9e)、[ESPI_TAF_EVENT_NO_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#gga66bd7ad63051eefa407df554d5241d9ea7bbb878224b80bfa133655879bcb8607)、[ESPI_TAF_EVENT_HOST_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#gga66bd7ad63051eefa407df554d5241d9ea79df8d5856d2f0d818cb511d9ae41b74)、[ESPI_TAF_EVENT_EC0_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#gga66bd7ad63051eefa407df554d5241d9ea875a93d6e2f4ed68b0355d71d68674b2)、[ESPI_TAF_EVENT_MAX_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#gga66bd7ad63051eefa407df554d5241d9ea9041f596e78d9443c7368b46527f49f1)。

eSPI TAF 通知类型。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.4\_函数（Functions）

<a id="r_ga34b0f6336aec45016d97528767b09434"></a>

```c
int espi_saf_config (const struct device *dev, const struct espi_saf_cfg *cfg)
```

相关声明：[espi_saf_config](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#ga34b0f6336aec45016d97528767b09434)、[device](../device_reference/P002_设备对象结构.md)、[espi_saf_cfg](../peripheral_bus_storage_model_reference/P015_espi_saf_cfg_结构体.md)。

配置 eSPI 控制器的运行方式。

<a id="r_ga273a9707f3ca501ed2dd3019cdeaa363"></a>

```c
int espi_saf_set_protection_regions (const struct device *dev, const struct espi_saf_protection *pr)
```

相关声明：[espi_saf_set_protection_regions](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#ga273a9707f3ca501ed2dd3019cdeaa363)、[device](../device_reference/P002_设备对象结构.md)。

设置一个或多个从设备附接 Flash（Slave Attached Flash，SAF）保护区域。

<a id="r_gaafe30738c18a16b056ed8dcf8638eb84"></a>

```c
int espi_saf_activate (const struct device *dev)
```

相关声明：[espi_saf_activate](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#gaafe30738c18a16b056ed8dcf8638eb84)、[device](../device_reference/P002_设备对象结构.md)。

激活 SAF 模块。

<a id="r_ga8b53a93559f0c67953e283f59107aa22"></a>

```c
bool espi_saf_get_channel_status (const struct device *dev)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[espi_saf_get_channel_status](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#ga8b53a93559f0c67953e283f59107aa22)、[device](../device_reference/P002_设备对象结构.md)。

查询 SAF 是否就绪。

<a id="r_ga0f5017eac05f928e635fec8e5f877c7d"></a>

```c
int espi_saf_flash_read (const struct device *dev, struct espi_saf_packet *pckt)
```

相关声明：[espi_saf_flash_read](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#ga0f5017eac05f928e635fec8e5f877c7d)、[device](../device_reference/P002_设备对象结构.md)、[espi_saf_packet](../peripheral_bus_storage_model_reference/P017_espi_saf_packet_结构体.md)。

发送从设备附接 Flash 的读取请求包。

<a id="r_ga104175f74019e58b8b7901f3dae245db"></a>

```c
int espi_saf_flash_write (const struct device *dev, struct espi_saf_packet *pckt)
```

相关声明：[espi_saf_flash_write](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#ga104175f74019e58b8b7901f3dae245db)、[device](../device_reference/P002_设备对象结构.md)、[espi_saf_packet](../peripheral_bus_storage_model_reference/P017_espi_saf_packet_结构体.md)。

发送从设备附接 Flash 的写入请求包。

<a id="r_ga15855a2ac593b97dc1a3e83ac9eda300"></a>

```c
int espi_saf_flash_erase (const struct device *dev, struct espi_saf_packet *pckt)
```

相关声明：[espi_saf_flash_erase](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#ga15855a2ac593b97dc1a3e83ac9eda300)、[device](../device_reference/P002_设备对象结构.md)、[espi_saf_packet](../peripheral_bus_storage_model_reference/P017_espi_saf_packet_结构体.md)。

发送从设备附接 Flash 的擦除请求包。

<a id="r_ga6c54d9274b1a8e883484bd892f606fd5"></a>

```c
int espi_saf_flash_unsuccess (const struct device *dev, struct espi_saf_packet *pckt)
```

相关声明：[espi_saf_flash_unsuccess](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#ga6c54d9274b1a8e883484bd892f606fd5)、[device](../device_reference/P002_设备对象结构.md)、[espi_saf_packet](../peripheral_bus_storage_model_reference/P017_espi_saf_packet_结构体.md)。

针对从设备附接 Flash 返回未成功完成（Unsuccessful completion）响应。

<a id="r_ga324283c28e6a33be112571621d1568e8"></a>

```c
static void espi_saf_init_callback (struct espi_callback *callback, espi_callback_handler_t handler, enum espi_bus_event evt_type)
```

相关声明：[espi_saf_init_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#ga324283c28e6a33be112571621d1568e8)、[espi_callback_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga9d848c7e367cf277230f365f73c15c46)、[espi_bus_event](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga36ac3fbf9813f78bad90f047e1eb1128)。

回调模型（Callback model）。

<a id="r_gadb881f847082f713bb0159d1e474980a"></a>

```c
static int espi_saf_add_callback (const struct device *dev, struct espi_callback *callback)
```

相关声明：[espi_saf_add_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#gadb881f847082f713bb0159d1e474980a)、[device](../device_reference/P002_设备对象结构.md)。

添加应用回调。

<a id="r_gaf987842bc7dad310c7270aed50086af9"></a>

```c
static int espi_saf_remove_callback (const struct device *dev, struct espi_callback *callback)
```

相关声明：[espi_saf_remove_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#gaf987842bc7dad310c7270aed50086af9)、[device](../device_reference/P002_设备对象结构.md)。

移除应用回调。


## 5.5\_原页交叉引用（Cross References）

- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码](https://docs.zephyrproject.org/latest/doxygen/html/espi__saf_8h_source.html)
- [espi_saf_cfg](../peripheral_bus_storage_model_reference/P015_espi_saf_cfg_结构体.md)
- [espi_saf_packet](../peripheral_bus_storage_model_reference/P017_espi_saf_packet_结构体.md)
- [espi_saf_driver_api](../peripheral_bus_storage_model_reference/P016_espi_saf_driver_api_结构体.md)
- [espi_saf_api_config](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface__backend.html#ga5f422a48cf008d7a737ec6a3fd0f0400)
- [device](../device_reference/P002_设备对象结构.md)
- [espi_saf_api_set_protection_regions](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface__backend.html#gaeb3c1ee73f50fd05737f28a75013c2a8)
- [espi_saf_api_activate](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface__backend.html#ga03a72ef8a19738d90681114f478ff068)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [espi_saf_api_get_channel_status](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface__backend.html#ga6ac9186c5b022f79dd8671594450efff)
- [espi_saf_api_flash_read](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface__backend.html#ga6154711885b4edc54db016ba9826c176)
- [espi_saf_api_flash_write](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface__backend.html#ga24498afe1639bd7c5192215dc8bbbed9)
- [espi_saf_api_flash_erase](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface__backend.html#ga4e8a12a1311d6604a61d1a9e57573e17)
- [espi_saf_api_flash_unsuccess](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface__backend.html#ga7c1aef03f238ced4e64c6e3be7ad643c)
- [espi_saf_api_manage_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface__backend.html#ga20ae708179a104c9334fe8fd554e5e05)
- [espi_taf_event](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#ga66bd7ad63051eefa407df554d5241d9e)
- [ESPI_TAF_EVENT_NO_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#gga66bd7ad63051eefa407df554d5241d9ea7bbb878224b80bfa133655879bcb8607)
- [ESPI_TAF_EVENT_HOST_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#gga66bd7ad63051eefa407df554d5241d9ea79df8d5856d2f0d818cb511d9ae41b74)
- [ESPI_TAF_EVENT_EC0_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#gga66bd7ad63051eefa407df554d5241d9ea875a93d6e2f4ed68b0355d71d68674b2)
- [ESPI_TAF_EVENT_MAX_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#gga66bd7ad63051eefa407df554d5241d9ea9041f596e78d9443c7368b46527f49f1)
- [espi_saf_config](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#ga34b0f6336aec45016d97528767b09434)
- [espi_saf_set_protection_regions](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#ga273a9707f3ca501ed2dd3019cdeaa363)
- [espi_saf_activate](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#gaafe30738c18a16b056ed8dcf8638eb84)
- [espi_saf_get_channel_status](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#ga8b53a93559f0c67953e283f59107aa22)
- [espi_saf_flash_read](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#ga0f5017eac05f928e635fec8e5f877c7d)
- [espi_saf_flash_write](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#ga104175f74019e58b8b7901f3dae245db)
- [espi_saf_flash_erase](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#ga15855a2ac593b97dc1a3e83ac9eda300)
- [espi_saf_flash_unsuccess](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#ga6c54d9274b1a8e883484bd892f606fd5)
- [espi_saf_init_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#ga324283c28e6a33be112571621d1568e8)
- [espi_callback_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga9d848c7e367cf277230f365f73c15c46)
- [espi_bus_event](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#ga36ac3fbf9813f78bad90f047e1eb1128)
- [espi_saf_add_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#gadb881f847082f713bb0159d1e474980a)
- [espi_saf_remove_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#gaf987842bc7dad310c7270aed50086af9)

<a id="header-details"></a>

---

[上一章](P004_zephyr__drivers__espi.h_头文件参考.md) · [返回大纲](大纲.md) · [下一章](P006_zephyr__drivers__fpga.h_头文件参考.md)
