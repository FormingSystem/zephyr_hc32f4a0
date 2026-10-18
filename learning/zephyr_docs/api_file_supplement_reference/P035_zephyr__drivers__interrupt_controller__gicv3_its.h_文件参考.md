---
id: learning.zephyr-docs.api-file-supplement-reference.page-35
title: zephyr__drivers__interrupt_controller__gicv3_its.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gicv3__its_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第35章\_zephyr\_\_drivers\_\_interrupt\_controller\_\_gicv3\_its.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/gicv3__its_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

ARM通用中断控制器V3（GICv3）中断转换服务（Interrupt Translation Service）的驱动。

查看此文件的源码。

<a id="details"></a>

ARM 通用中断控制器第 3 版（Generic Interrupt Controller V3，GICv3）的中断转换服务（Interrupt Translation Service，ITS）驱动。通用中断控制器（GIC）的 ITS 接收由设备标识（DeviceID）确定的设备所发出的事件标识（EventID），将该输入转换为对应的中断标识（INTID），确定目标再分发器（Redistributor），并由此确定该 INTID 对应的目标处理单元（Processing Element，PE）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 35.1\_数据结构（Data Structures）

<a id="r_its_5Fdriver_5Fapi"></a>

```c
struct its_driver_api
```

相关声明：[its_driver_api](../platform_security_model_reference/P016_its_driver_api_结构体.md)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 35.2\_类型定义（Typedefs）

<a id="r_a49dff2553cbd48edc7057157d2ecb45d"></a>

```c
typedef unsigned int(* its_api_alloc_intid_t) (const struct device *dev)
```

相关声明：[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[its_api_alloc_intid_t](#a49dff2553cbd48edc7057157d2ecb45d)、[device](../device_reference/P002_设备对象结构.md)。

<a id="r_a39f4a213de953b77615b270f3ff13832"></a>

```c
typedef int(* its_api_setup_deviceid_t) (const struct device *dev, uint32_t device_id, unsigned int nites)
```

相关声明：[its_api_setup_deviceid_t](#a39f4a213de953b77615b270f3ff13832)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

<a id="r_a2642c1f7ecf45d404c17cdbcd824bb45"></a>

```c
typedef int(* its_api_map_intid_t) (const struct device *dev, uint32_t device_id, uint32_t event_id, unsigned int intid)
```

相关声明：[its_api_map_intid_t](#a2642c1f7ecf45d404c17cdbcd824bb45)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

<a id="r_a26bf8d071e3cb856fc81d8911e942f5a"></a>

```c
typedef int(* its_api_send_int_t) (const struct device *dev, uint32_t device_id, uint32_t event_id)
```

相关声明：[its_api_send_int_t](#a26bf8d071e3cb856fc81d8911e942f5a)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

<a id="r_add616700e3aeee952187ef96cb2d19c9"></a>

```c
typedef uint32_t(* its_api_get_msi_addr_t) (const struct device *dev)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[its_api_get_msi_addr_t](#add616700e3aeee952187ef96cb2d19c9)、[device](../device_reference/P002_设备对象结构.md)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 35.3\_函数（Functions）

<a id="r_a5c50167a84a3b7d8e3cf01d226deb3d3"></a>

```c
static int its_alloc_intid (const struct device *dev)
```

相关声明：[its_alloc_intid](#a5c50167a84a3b7d8e3cf01d226deb3d3)、[device](../device_reference/P002_设备对象结构.md)。

<a id="r_a05032faf2fdcde27760871345756d3e5"></a>

```c
static int its_setup_deviceid (const struct device *dev, uint32_t device_id, unsigned int nites)
```

相关声明：[its_setup_deviceid](#a05032faf2fdcde27760871345756d3e5)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

<a id="r_ac4899e33d0636465265a3072aa5510cc"></a>

```c
static int its_map_intid (const struct device *dev, uint32_t device_id, uint32_t event_id, unsigned int intid)
```

相关声明：[its_map_intid](#ac4899e33d0636465265a3072aa5510cc)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

<a id="r_a6139a7f275a6016ecadcb0ee2dfcc327"></a>

```c
static int its_send_int (const struct device *dev, uint32_t device_id, uint32_t event_id)
```

相关声明：[its_send_int](#a6139a7f275a6016ecadcb0ee2dfcc327)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

<a id="r_afcd0b4735367a10465e81b46d333b06b"></a>

```c
static uint32_t its_get_msi_addr (const struct device *dev)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[its_get_msi_addr](#afcd0b4735367a10465e81b46d333b06b)、[device](../device_reference/P002_设备对象结构.md)。

## 35.4\_详细说明（Detailed Documentation）

<a id="a49dff2553cbd48edc7057157d2ecb45d"></a>

### `its_api_alloc_intid_t`

```c
typedef unsigned int(* its_api_alloc_intid_t) (const struct device *dev)
```

<a id="add616700e3aeee952187ef96cb2d19c9"></a>

### `its_api_get_msi_addr_t`

```c
typedef uint32_t(* its_api_get_msi_addr_t) (const struct device *dev)
```

<a id="a2642c1f7ecf45d404c17cdbcd824bb45"></a>

### `its_api_map_intid_t`

```c
typedef int(* its_api_map_intid_t) (const struct device *dev, uint32_t device_id, uint32_t event_id, unsigned int intid)
```

<a id="a26bf8d071e3cb856fc81d8911e942f5a"></a>

### `its_api_send_int_t`

```c
typedef int(* its_api_send_int_t) (const struct device *dev, uint32_t device_id, uint32_t event_id)
```

<a id="a39f4a213de953b77615b270f3ff13832"></a>

### `its_api_setup_deviceid_t`

```c
typedef int(* its_api_setup_deviceid_t) (const struct device *dev, uint32_t device_id, unsigned int nites)
```

<a id="a5c50167a84a3b7d8e3cf01d226deb3d3"></a>

### `its_alloc_intid()`

```c
int its_alloc_intid ( const struct device * dev)
```

声明属性：`inline`、`static`。

<a id="afcd0b4735367a10465e81b46d333b06b"></a>

### `its_get_msi_addr()`

```c
uint32_t its_get_msi_addr ( const struct device * dev)
```

声明属性：`inline`、`static`。

<a id="ac4899e33d0636465265a3072aa5510cc"></a>

### `its_map_intid()`

```c
int its_map_intid ( const struct device * dev, uint32_t device_id, uint32_t event_id, unsigned int intid )
```

声明属性：`inline`、`static`。

<a id="a6139a7f275a6016ecadcb0ee2dfcc327"></a>

### `its_send_int()`

```c
int its_send_int ( const struct device * dev, uint32_t device_id, uint32_t event_id )
```

声明属性：`inline`、`static`。

<a id="a05032faf2fdcde27760871345756d3e5"></a>

### `its_setup_deviceid()`

```c
int its_setup_deviceid ( const struct device * dev, uint32_t device_id, unsigned int nites )
```

声明属性：`inline`、`static`。


## 35.5\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P290_gicv3_its.h_源码浏览.md)
- [its_driver_api](../platform_security_model_reference/P016_its_driver_api_结构体.md)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P034_zephyr__drivers__clock_control__gd32.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P036_zephyr__drivers__gpio__gpio_ambiq.h_文件参考.md)
