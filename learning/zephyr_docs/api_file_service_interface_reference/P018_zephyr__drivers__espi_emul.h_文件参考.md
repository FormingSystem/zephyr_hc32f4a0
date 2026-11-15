---
id: learning.zephyr-docs.api-file-service-interface-reference.page-18
title: zephyr__drivers__espi_emul.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/espi__emul_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_zephyr\_\_drivers\_\_espi\_emul.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/espi__emul_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

eSPI仿真（Emulation）驱动API的主头文件。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/drivers/emul.h>
#include <zephyr/drivers/espi.h>
#include <zephyr/sys/slist.h>
#include <zephyr/types.h>
```

查看此文件的源码。

eSPI仿真（Emulation）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 18.1\_数据结构（Data Structures）

<a id="r_emul_5Fespi_5Fdevice_5Fapi"></a>

```c
struct emul_espi_device_api
```

相关声明：[emul_espi_device_api](../hardware/P481_eSPI仿真设备API结构.md)。

eSPI设备仿真器（Device Emulator）API的定义。

<a id="r_espi_5Femul"></a>

```c
struct espi_emul
```

相关声明：[espi_emul](../hardware/P488_eSPI仿真器链表节点.md)。

eSPI设备仿真器链表（Linked List）中的节点。

<a id="r_emul_5Fespi_5Fdriver_5Fapi"></a>

```c
struct emul_espi_driver_api
```

相关声明：[emul_espi_driver_api](../hardware/P482_eSPI仿真驱动API结构.md)。

eSPI控制器仿真器（Controller Emulator）API的定义。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 18.2\_宏定义（Macros）

<a id="r_ga18fb55455f95a7f7ba93fdc49de2b9c0"></a>

```c
#define EMUL_ESPI_HOST_CHIPSEL 0
```

相关声明：[EMUL_ESPI_HOST_CHIPSEL](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__emul__interface.html#ga18fb55455f95a7f7ba93fdc49de2b9c0)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 18.3\_类型定义（Typedefs）

<a id="r_gab1068f48bf931fbc86668fb9108e07c7"></a>

```c
typedef int(* emul_espi_api_set_vw) (const struct emul *target, enum espi_vwire_signal vw, uint8_t level)
```

相关声明：[emul_espi_api_set_vw](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__emul__interface.html#gab1068f48bf931fbc86668fb9108e07c7)、[emul](../hardware/P477_仿真器实例结构.md)、[espi_vwire_signal](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gab65a0951a8912d9de398cfec0aef7d35)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向仿真器（Emulator）传递 eSPI 虚拟线设置请求（Virtual Wire Packet）。

<a id="r_ga06c214788ceff221e776394318517f91"></a>

```c
typedef int(* emul_espi_api_get_vw) (const struct emul *target, enum espi_vwire_signal vw, uint8_t *level)
```

相关声明：[emul_espi_api_get_vw](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__emul__interface.html#ga06c214788ceff221e776394318517f91)、[emul](../hardware/P477_仿真器实例结构.md)、[espi_vwire_signal](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gab65a0951a8912d9de398cfec0aef7d35)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向仿真器（Emulator）传递 eSPI 虚拟线获取请求（Virtual Wire Packet）。

<a id="r_ga375d2f3d386a835b627cf26745bc77c3"></a>

```c
typedef uintptr_t(* emul_espi_api_get_acpi_shm) (const struct emul *target)
```

相关声明：[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[emul_espi_api_get_acpi_shm](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__emul__interface.html#ga375d2f3d386a835b627cf26745bc77c3)、[emul](../hardware/P477_仿真器实例结构.md)。

获取仿真器拥有的高级配置与电源接口（ACPI）共享内存地址。

<a id="r_gaa9e27e6a744a73a13415e01fa2c09bca"></a>

```c
typedef struct espi_emul *(* emul_find_emul) (const struct device *dev, unsigned int chipsel)
```

相关声明：[espi_emul](../hardware/P488_eSPI仿真器链表节点.md)、[emul_find_emul](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__emul__interface.html#gaa9e27e6a744a73a13415e01fa2c09bca)、[device](../device_reference/P002_设备对象结构.md)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

查找 eSPI 总线上的仿真器（Emulator）。

<a id="r_ga2abff7d857738254cc4a8a939264924f"></a>

```c
typedef int(* emul_trigger_event) (const struct device *dev, struct espi_event *evt)
```

相关声明：[emul_trigger_event](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__emul__interface.html#ga2abff7d857738254cc4a8a939264924f)、[device](../device_reference/P002_设备对象结构.md)、[espi_event](../peripheral_bus_storage_model_reference/P008_espi_event_结构体.md)。

在 eSPI 控制器侧的仿真器上触发事件，从而调用特定回调。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 18.4\_函数（Functions）

<a id="r_gaaccb8ef6060c0477151001af52310769"></a>

```c
int espi_emul_register (const struct device *dev, struct espi_emul *emul)
```

相关声明：[espi_emul_register](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__emul__interface.html#gaaccb8ef6060c0477151001af52310769)、[device](../device_reference/P002_设备对象结构.md)、[espi_emul](../hardware/P488_eSPI仿真器链表节点.md)、[emul](../hardware/P477_仿真器实例结构.md)。

在控制器（Controller）上注册仿真设备（Emulated Device）。

<a id="r_ga67deaf77a17682671ec28488ed3113fc"></a>

```c
int emul_espi_host_send_vw (const struct device *espi_dev, enum espi_vwire_signal vw, uint8_t level)
```

相关声明：[emul_espi_host_send_vw](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__emul__interface.html#ga67deaf77a17682671ec28488ed3113fc)、[device](../device_reference/P002_设备对象结构.md)、[espi_vwire_signal](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gab65a0951a8912d9de398cfec0aef7d35)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

在主机侧设置 eSPI 虚拟线（Virtual Wire），从而在仿真的 eSPI 控制器上触发相应事件及回调。

<a id="r_ga16c67d1d52f94b7062144e2c2f45d15a"></a>

```c
int emul_espi_host_port80_write (const struct device *espi_dev, uint32_t data)
```

相关声明：[emul_espi_host_port80_write](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__emul__interface.html#ga16c67d1d52f94b7062144e2c2f45d15a)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

在仿真主机侧执行端口 80（Port 80）写入，从而在仿真的 eSPI 控制器上触发相应事件及回调。

<a id="r_gaa9f83b27986b700d629188522850fab3"></a>

```c
uintptr_t emul_espi_host_get_acpi_shm (const struct device *espi_dev)
```

相关声明：[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[emul_espi_host_get_acpi_shm](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__emul__interface.html#gaa9f83b27986b700d629188522850fab3)、[device](../device_reference/P002_设备对象结构.md)。

获取主机设备的 ACPI 共享内存起始地址。


## 18.5\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/drivers/emul.h](../api_source_runtime_reference/P013_emul.h_源码浏览.md)
- [zephyr/drivers/espi.h](../peripheral_bus_storage_source_reference/P004_zephyr__drivers__espi.h_头文件源码.md)
- [zephyr/sys/slist.h](../slist_reference/P003_单向链表头文件源码.md)
- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [查看此文件的源码。](../api_source_configuration_reference/P026_espi_emul.h_源码浏览.md)
- [emul_espi_device_api](../hardware/P481_eSPI仿真设备API结构.md)
- [espi_emul](../hardware/P488_eSPI仿真器链表节点.md)
- [emul_espi_driver_api](../hardware/P482_eSPI仿真驱动API结构.md)
- [EMUL_ESPI_HOST_CHIPSEL](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__emul__interface.html#ga18fb55455f95a7f7ba93fdc49de2b9c0)
- [emul_espi_api_set_vw](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__emul__interface.html#gab1068f48bf931fbc86668fb9108e07c7)
- [emul](../hardware/P477_仿真器实例结构.md)
- [espi_vwire_signal](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gab65a0951a8912d9de398cfec0aef7d35)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [emul_espi_api_get_vw](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__emul__interface.html#ga06c214788ceff221e776394318517f91)
- [uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)
- [emul_espi_api_get_acpi_shm](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__emul__interface.html#ga375d2f3d386a835b627cf26745bc77c3)
- [emul_find_emul](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__emul__interface.html#gaa9e27e6a744a73a13415e01fa2c09bca)
- [device](../device_reference/P002_设备对象结构.md)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [emul_trigger_event](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__emul__interface.html#ga2abff7d857738254cc4a8a939264924f)
- [espi_event](../peripheral_bus_storage_model_reference/P008_espi_event_结构体.md)
- [espi_emul_register](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__emul__interface.html#gaaccb8ef6060c0477151001af52310769)
- [emul_espi_host_send_vw](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__emul__interface.html#ga67deaf77a17682671ec28488ed3113fc)
- [emul_espi_host_port80_write](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__emul__interface.html#ga16c67d1d52f94b7062144e2c2f45d15a)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [emul_espi_host_get_acpi_shm](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__emul__interface.html#gaa9f83b27986b700d629188522850fab3)

<a id="header-details"></a>

---

[上一章](P017_zephyr__bluetooth__ead.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P019_zephyr__xen__fdt.h_文件参考.md)
