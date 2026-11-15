---
id: learning.zephyr-docs.peripheral-bus-storage-header-reference.page-6
title: zephyr__drivers__fpga.h_头文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/fpga_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_zephyr\_\_drivers\_\_fpga.h\_头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/fpga_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

现场可编程门阵列（FPGA）驱动API的主头文件。

<a id="details"></a>

```c
#include <errno.h>
#include <zephyr/types.h>
#include <zephyr/sys/util.h>
#include <zephyr/device.h>
```

查看此文件的源码。

现场可编程门阵列（FPGA）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 6.1\_数据结构（Data Structures）

<a id="r_fpga_5Fdriver_5Fapi"></a>

```c
struct fpga_driver_api
```

相关声明：[fpga_driver_api](../peripheral_bus_storage_model_reference/P018_fpga_driver_api_结构体.md)。

驱动操作（Driver Operations）：现场可编程门阵列（FPGA）驱动操作。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.2\_宏定义（Macros）

<a id="r_gab41c04907be508f62e8df813d633b34b"></a>

```c
#define FPGA_GET_INFO_DEFAULT "n/a"
```

相关声明：[FPGA_GET_INFO_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface.html#gab41c04907be508f62e8df813d633b34b)。

无可用信息时，`fpga_get_info()` 返回的默认字符串。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 6.3\_类型定义（Typedefs）

<a id="r_ga02d71e7a82f446220d67664d4cc7a5c9"></a>

```c
typedef enum FPGA_status(* fpga_api_get_status) (const struct device *dev)
```

相关声明：[FPGA_status](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface.html#ga0bbacdfdac79bace1786bb2a1627bb1e)、[fpga_api_get_status](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface__backend.html#ga02d71e7a82f446220d67664d4cc7a5c9)、[device](../device_reference/P002_设备对象结构.md)。

读取 FPGA 状态的回调 API。

<a id="r_ga9860c64bbc2cfb89df9b51da655691b6"></a>

```c
typedef int(* fpga_api_load) (const struct device *dev, uint32_t *image_ptr, uint32_t img_size)
```

相关声明：[fpga_api_load](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface__backend.html#ga9860c64bbc2cfb89df9b51da655691b6)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

加载位流（Bitstream）并配置 FPGA 的回调 API。

<a id="r_ga3c53b90b9d0b50c44c01a534c61e9212"></a>

```c
typedef int(* fpga_api_reset) (const struct device *dev)
```

相关声明：[fpga_api_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface__backend.html#ga3c53b90b9d0b50c44c01a534c61e9212)、[device](../device_reference/P002_设备对象结构.md)。

复位 FPGA 的回调 API。

<a id="r_gaf3e8ea5d443fd09352e2b63f82a459be"></a>

```c
typedef int(* fpga_api_on) (const struct device *dev)
```

相关声明：[fpga_api_on](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface__backend.html#gaf3e8ea5d443fd09352e2b63f82a459be)、[device](../device_reference/P002_设备对象结构.md)。

开启 FPGA 的回调 API。

<a id="r_ga872a8d75bb46de50a41b56170804ed27"></a>

```c
typedef int(* fpga_api_off) (const struct device *dev)
```

相关声明：[fpga_api_off](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface__backend.html#ga872a8d75bb46de50a41b56170804ed27)、[device](../device_reference/P002_设备对象结构.md)。

关闭 FPGA 的回调 API。

<a id="r_ga24fd6ce4832b960b79914f42010774aa"></a>

```c
typedef const char *(* fpga_api_get_info) (const struct device *dev)
```

相关声明：[fpga_api_get_info](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface__backend.html#ga24fd6ce4832b960b79914f42010774aa)、[device](../device_reference/P002_设备对象结构.md)。

返回 FPGA 信息的回调 API。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 6.4\_枚举（Enumerations）

<a id="r_ga0bbacdfdac79bace1786bb2a1627bb1e"></a>

```c
enum FPGA_status { FPGA_STATUS_INACTIVE , FPGA_STATUS_ACTIVE }
```

相关声明：[FPGA_status](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface.html#ga0bbacdfdac79bace1786bb2a1627bb1e)、[FPGA_STATUS_INACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface.html#gga0bbacdfdac79bace1786bb2a1627bb1ea46571663477ca2df50b24cf93a5e2441)、[FPGA_STATUS_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface.html#gga0bbacdfdac79bace1786bb2a1627bb1eac1b036277b07dfdef1dd1c3e1a299131)。

FPGA 配置状态（Programming status）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 6.5\_函数（Functions）

<a id="r_ga1a1e78a46df9f4bd374cf5ecc2449360"></a>

```c
static enum FPGA_status fpga_get_status (const struct device *dev)
```

相关声明：[FPGA_status](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface.html#ga0bbacdfdac79bace1786bb2a1627bb1e)、[fpga_get_status](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface.html#ga1a1e78a46df9f4bd374cf5ecc2449360)、[device](../device_reference/P002_设备对象结构.md)。

读取现场可编程门阵列（FPGA）的状态。

<a id="r_gadfc8d6c24cb1b1640393017a462011c9"></a>

```c
static int fpga_reset (const struct device *dev)
```

相关声明：[fpga_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface.html#gadfc8d6c24cb1b1640393017a462011c9)、[device](../device_reference/P002_设备对象结构.md)。

复位 FPGA。

<a id="r_ga1cace6c7cc44705bf861d7aa5e863e16"></a>

```c
static int fpga_load (const struct device *dev, uint32_t *image_ptr, uint32_t img_size)
```

相关声明：[fpga_load](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface.html#ga1cace6c7cc44705bf861d7aa5e863e16)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

加载位流（Bitstream）并配置 FPGA。

<a id="r_gad9093bd96c6a62cd958718d1e01e3f37"></a>

```c
static int fpga_on (const struct device *dev)
```

相关声明：[fpga_on](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface.html#gad9093bd96c6a62cd958718d1e01e3f37)、[device](../device_reference/P002_设备对象结构.md)。

开启 FPGA。

<a id="r_gab887999e8728bcc335a784afbdbbee8f"></a>

```c
static const char * fpga_get_info (const struct device *dev)
```

相关声明：[fpga_get_info](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface.html#gab887999e8728bcc335a784afbdbbee8f)、[device](../device_reference/P002_设备对象结构.md)。

返回 FPGA 的相关信息。

<a id="r_gaa161c7a7006db24793c1a1ecdea25b5c"></a>

```c
static int fpga_off (const struct device *dev)
```

相关声明：[fpga_off](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface.html#gaa161c7a7006db24793c1a1ecdea25b5c)、[device](../device_reference/P002_设备对象结构.md)。

关闭 FPGA。


## 6.6\_原页交叉引用（Cross References）

- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码](https://docs.zephyrproject.org/latest/doxygen/html/fpga_8h_source.html)
- [fpga_driver_api](../peripheral_bus_storage_model_reference/P018_fpga_driver_api_结构体.md)
- [FPGA_GET_INFO_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface.html#gab41c04907be508f62e8df813d633b34b)
- [fpga_get_info()](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface.html#gab887999e8728bcc335a784afbdbbee8f)
- [FPGA_status](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface.html#ga0bbacdfdac79bace1786bb2a1627bb1e)
- [fpga_api_get_status](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface__backend.html#ga02d71e7a82f446220d67664d4cc7a5c9)
- [device](../device_reference/P002_设备对象结构.md)
- [fpga_api_load](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface__backend.html#ga9860c64bbc2cfb89df9b51da655691b6)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [fpga_api_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface__backend.html#ga3c53b90b9d0b50c44c01a534c61e9212)
- [fpga_api_on](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface__backend.html#gaf3e8ea5d443fd09352e2b63f82a459be)
- [fpga_api_off](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface__backend.html#ga872a8d75bb46de50a41b56170804ed27)
- [fpga_api_get_info](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface__backend.html#ga24fd6ce4832b960b79914f42010774aa)
- [FPGA_STATUS_INACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface.html#gga0bbacdfdac79bace1786bb2a1627bb1ea46571663477ca2df50b24cf93a5e2441)
- [FPGA_STATUS_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface.html#gga0bbacdfdac79bace1786bb2a1627bb1eac1b036277b07dfdef1dd1c3e1a299131)
- [fpga_get_status](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface.html#ga1a1e78a46df9f4bd374cf5ecc2449360)
- [fpga_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface.html#gadfc8d6c24cb1b1640393017a462011c9)
- [fpga_load](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface.html#ga1cace6c7cc44705bf861d7aa5e863e16)
- [fpga_on](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface.html#gad9093bd96c6a62cd958718d1e01e3f37)
- [fpga_off](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface.html#gaa161c7a7006db24793c1a1ecdea25b5c)

<a id="header-details"></a>

---

[上一章](P005_zephyr__drivers__espi_saf.h_头文件参考.md) · [返回大纲](大纲.md) · [下一章](P007_zephyr__drivers__lin.h_头文件参考.md)
