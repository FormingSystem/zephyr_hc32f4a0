---
id: learning.zephyr-docs.api-file-reference.page-72
title: zephyr__drivers__interrupt_controller__dw_ace.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dw__ace_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第72章\_zephyr\_\_drivers\_\_interrupt\_controller\_\_dw\_ace.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dw__ace_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/device.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 72.1\_数据结构（Data Structures）

<a id="r_dw_5Face_5Fv1_5Fictl_5Fdriver_5Fapi"></a>

```c
struct dw_ace_v1_ictl_driver_api
```

相关声明：[dw_ace_v1_ictl_driver_api](../platform_security_model_reference/P002_dw_ace_v1_ictl_driver_api_结构体.md)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 72.2\_类型定义（Typedefs）

<a id="r_a99f66a0736502ea18deb13e0a5d9958e"></a>

```c
typedef void(* irq_enable_t) (const struct device *dev, uint32_t irq)
```

相关声明：[irq_enable_t](#a99f66a0736502ea18deb13e0a5d9958e)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

<a id="r_a1e71aa00761ed1a478f92de8a1342564"></a>

```c
typedef void(* irq_disable_t) (const struct device *dev, uint32_t irq)
```

相关声明：[irq_disable_t](#a1e71aa00761ed1a478f92de8a1342564)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

<a id="r_af94ebd4f440b084d94d42eed62e159cc"></a>

```c
typedef int(* irq_is_enabled_t) (const struct device *dev, unsigned int irq)
```

相关声明：[irq_is_enabled_t](#af94ebd4f440b084d94d42eed62e159cc)、[device](../device_reference/P002_设备对象结构.md)、[unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

<a id="r_a5b6d1259c32080069df86d5e4fd506cb"></a>

```c
typedef int(* irq_connect_dynamic_t) (const struct device *dev, unsigned int irq, unsigned int priority, void(*routine) (const void *parameter), const void *parameter, uint32_t flags)
```

相关声明：[irq_connect_dynamic_t](#a5b6d1259c32080069df86d5e4fd506cb)、[device](../device_reference/P002_设备对象结构.md)、[unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[uint32_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[flags](P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

## 72.3\_详细说明（Detailed Documentation）

<a id="a5b6d1259c32080069df86d5e4fd506cb"></a>

### `irq_connect_dynamic_t`

```c
typedef int(* irq_connect_dynamic_t) (const struct device *dev, unsigned int irq, unsigned int priority, void(*routine)(const void *parameter), const void *parameter, uint32_t flags)
```

<a id="a1e71aa00761ed1a478f92de8a1342564"></a>

### `irq_disable_t`

```c
typedef void(* irq_disable_t) (const struct device *dev, uint32_t irq)
```

<a id="a99f66a0736502ea18deb13e0a5d9958e"></a>

### `irq_enable_t`

```c
typedef void(* irq_enable_t) (const struct device *dev, uint32_t irq)
```

<a id="af94ebd4f440b084d94d42eed62e159cc"></a>

### `irq_is_enabled_t`

```c
typedef int(* irq_is_enabled_t) (const struct device *dev, unsigned int irq)
```


## 72.4\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P216_dw_ace.h_源码浏览.md)
- [dw_ace_v1_ictl_driver_api](../platform_security_model_reference/P002_dw_ace_v1_ictl_driver_api_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [flags](P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P071_zephyr__dt-bindings__usb__audio.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P073_zephyr__drivers__edac__edac_mcux_erm.h_文件参考.md)
