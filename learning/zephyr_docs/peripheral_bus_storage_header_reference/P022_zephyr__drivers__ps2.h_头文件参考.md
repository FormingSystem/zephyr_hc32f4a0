---
id: learning.zephyr-docs.peripheral-bus-storage-header-reference.page-22
title: zephyr__drivers__ps2.h_头文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ps2_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_zephyr\_\_drivers\_\_ps2.h\_头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ps2_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

个人系统/2（Personal System/2，PS/2）驱动API的主头文件。

<a id="details"></a>

```c
#include <errno.h>
#include <zephyr/types.h>
#include <stddef.h>
#include <zephyr/device.h>
#include <zephyr/syscalls/ps2.h>
```

查看此文件的源码。

个人系统/2（Personal System/2，PS/2）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 22.1\_数据结构（Data Structures）

<a id="r_ps2_5Fdriver_5Fapi"></a>

```c
struct ps2_driver_api
```

相关声明：[ps2_driver_api](../peripheral_bus_storage_model_reference/P069_ps2_driver_api_结构体.md)。

驱动操作（Driver Operations）：PS/2驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 22.2\_类型定义（Typedefs）

<a id="r_gad7cf29301681fac0d2a359d425a13b5f"></a>

```c
typedef void(* ps2_callback_t) (const struct device *dev, uint8_t data)
```

相关声明：[ps2_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface.html#gad7cf29301681fac0d2a359d425a13b5f)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

用户键入或点击鼠标时调用的 PS/2 回调。

<a id="r_ga7fb2edbebe2523efde6c7f73bffb850a"></a>

```c
typedef int(* ps2_config_t) (const struct device *dev, ps2_callback_t callback_isr)
```

相关声明：[ps2_config_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface__backend.html#ga7fb2edbebe2523efde6c7f73bffb850a)、[device](../device_reference/P002_设备对象结构.md)、[ps2_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface.html#gad7cf29301681fac0d2a359d425a13b5f)。

配置 PS/2 设备的回调 API。

<a id="r_ga3d5a1b7e613e0e2b1a28689b9ab52ca5"></a>

```c
typedef int(* ps2_read_t) (const struct device *dev, uint8_t *value)
```

相关声明：[ps2_read_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface__backend.html#ga3d5a1b7e613e0e2b1a28689b9ab52ca5)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从 PS/2 设备读取的回调 API。

<a id="r_gaf7a935b2e1debd819792dbb02bd84ee2"></a>

```c
typedef int(* ps2_write_t) (const struct device *dev, uint8_t value)
```

相关声明：[ps2_write_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface__backend.html#gaf7a935b2e1debd819792dbb02bd84ee2)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向 PS/2 设备写入的回调 API。

<a id="r_gaaa51cb5cf5f5d7560c35374561746f6d"></a>

```c
typedef int(* ps2_disable_callback_t) (const struct device *dev)
```

相关声明：[ps2_disable_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface__backend.html#gaaa51cb5cf5f5d7560c35374561746f6d)、[device](../device_reference/P002_设备对象结构.md)。

禁用 PS/2 设备回调的回调 API。

<a id="r_gaad5d2a31e2f4768953b6d611364e748c"></a>

```c
typedef int(* ps2_enable_callback_t) (const struct device *dev)
```

相关声明：[ps2_enable_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface__backend.html#gaad5d2a31e2f4768953b6d611364e748c)、[device](../device_reference/P002_设备对象结构.md)。

启用 PS/2 设备回调的回调 API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 22.3\_函数（Functions）

<a id="r_ga8d6da9b966432defb0cd482003c11f15"></a>

```c
int ps2_config (const struct device *dev, ps2_callback_t callback_isr)
```

相关声明：[ps2_config](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface.html#ga8d6da9b966432defb0cd482003c11f15)、[device](../device_reference/P002_设备对象结构.md)、[ps2_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface.html#gad7cf29301681fac0d2a359d425a13b5f)。

配置 PS/2 设备实例。

<a id="r_gae291cb991ae9525552fdb52c2fa4ac5e"></a>

```c
int ps2_write (const struct device *dev, uint8_t value)
```

相关声明：[ps2_write](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface.html#gae291cb991ae9525552fdb52c2fa4ac5e)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向 PS/2 设备写入。

<a id="r_gab91b1efe1f07d409607922f4eb87b221"></a>

```c
int ps2_read (const struct device *dev, uint8_t *value)
```

相关声明：[ps2_read](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface.html#gab91b1efe1f07d409607922f4eb87b221)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从 PS/2 设备读取从设备到主机方向的数据值。

<a id="r_ga9568487018f4ef972eb463ea2098e254"></a>

```c
int ps2_enable_callback (const struct device *dev)
```

相关声明：[ps2_enable_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface.html#ga9568487018f4ef972eb463ea2098e254)、[device](../device_reference/P002_设备对象结构.md)。

启用回调。

<a id="r_gade1a470c3583e465d6a8f24a28611397"></a>

```c
int ps2_disable_callback (const struct device *dev)
```

相关声明：[ps2_disable_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface.html#gade1a470c3583e465d6a8f24a28611397)、[device](../device_reference/P002_设备对象结构.md)。

禁用回调。


## 22.4\_原页交叉引用（Cross References）

- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码](https://docs.zephyrproject.org/latest/doxygen/html/ps2_8h_source.html)
- [ps2_driver_api](../peripheral_bus_storage_model_reference/P069_ps2_driver_api_结构体.md)
- [ps2_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface.html#gad7cf29301681fac0d2a359d425a13b5f)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [ps2_config_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface__backend.html#ga7fb2edbebe2523efde6c7f73bffb850a)
- [ps2_read_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface__backend.html#ga3d5a1b7e613e0e2b1a28689b9ab52ca5)
- [ps2_write_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface__backend.html#gaf7a935b2e1debd819792dbb02bd84ee2)
- [ps2_disable_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface__backend.html#gaaa51cb5cf5f5d7560c35374561746f6d)
- [ps2_enable_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface__backend.html#gaad5d2a31e2f4768953b6d611364e748c)
- [ps2_config](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface.html#ga8d6da9b966432defb0cd482003c11f15)
- [ps2_write](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface.html#gae291cb991ae9525552fdb52c2fa4ac5e)
- [ps2_read](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface.html#gab91b1efe1f07d409607922f4eb87b221)
- [ps2_enable_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface.html#ga9568487018f4ef972eb463ea2098e254)
- [ps2_disable_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface.html#gade1a470c3583e465d6a8f24a28611397)

<a id="header-details"></a>

---

[上一章](P021_zephyr__drivers__peci.h_头文件参考.md) · [返回大纲](大纲.md) · [下一章](P023_zephyr__drivers__psi5__psi5.h_头文件参考.md)
