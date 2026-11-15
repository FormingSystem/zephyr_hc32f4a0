---
id: learning.zephyr-docs.api-file-protocol-service-reference.page-11
title: zephyr__drivers__crc.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2crc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_zephyr\_\_drivers\_\_crc.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2crc_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

循环冗余校验（CRC）的公共API头文件。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/kernel.h>
#include <zephyr/sys/crc.h>
#include <zephyr/syscalls/crc.h>
```

查看此文件的源码。

循环冗余校验（CRC）的公共API头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 11.1\_数据结构（Data Structures）

<a id="r_crc_5Fctx"></a>

```c
struct crc_ctx
```

相关声明：[crc_ctx](../hardware/P046_CRC上下文结构.md)。

循环冗余校验（CRC）的上下文结构。

<a id="r_crc_5Fdriver_5Fapi"></a>

```c
struct crc_driver_api
```

相关声明：[crc_driver_api](../hardware/P052_CRC驱动操作结构.md)。

驱动操作（Driver Operations）：循环冗余校验（CRC）驱动操作。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 11.2\_宏定义（Macros）

<a id="define-members-0"></a>

### CRC 输入／输出字符串标志（Input/Output String Flags）



<a id="r_ga9686f52f45a6023d7e7c144732ab9202"></a>

```c
#define CRC_FLAG_REVERSE_INPUT BIT(0)
```

相关声明：[CRC_FLAG_REVERSE_INPUT](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#ga9686f52f45a6023d7e7c144732ab9202)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

反转输入字符串（Reverse Input String）。

<a id="r_gad2413454ab20a446fdc53f08ddd85a4e"></a>

```c
#define CRC_FLAG_REVERSE_OUTPUT BIT(1)
```

相关声明：[CRC_FLAG_REVERSE_OUTPUT](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#gad2413454ab20a446fdc53f08ddd85a4e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

反转输出字符串（Reverse Output String）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 11.3\_类型定义（Typedefs）

<a id="r_ga45ff64f03c4bfadd47ba66ce944c09bf"></a>

```c
typedef uint32_t crc_init_val_t
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[crc_init_val_t](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#ga45ff64f03c4bfadd47ba66ce944c09bf)。

提供保存 CRC 初始种子值（Initial Seed Value）的类型。

<a id="r_ga938a05769aa6a61c22217611fb375218"></a>

```c
typedef uint32_t crc_poly_t
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[crc_poly_t](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#ga938a05769aa6a61c22217611fb375218)。

提供保存 CRC 多项式值（Polynomial Value）的类型。

<a id="r_ga7c6663d361406882a73e8ba171840adc"></a>

```c
typedef uint32_t crc_result_t
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[crc_result_t](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#ga7c6663d361406882a73e8ba171840adc)。

提供保存 CRC 结果值（Result Value）的类型。

<a id="r_ga8babc96e0e656e3974c5e3df32f59107"></a>

```c
typedef int(* crc_api_begin) (const struct device *dev, struct crc_ctx *ctx)
```

相关声明：[crc_api_begin](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface__backend.html#ga8babc96e0e656e3974c5e3df32f59107)、[device](../device_reference/P002_设备对象结构.md)、[crc_ctx](../hardware/P046_CRC上下文结构.md)。

配置 CRC 单元以进行计算的回调 API。

<a id="r_ga7d6a2a6b119a8fb51d91e6f5f6269af7"></a>

```c
typedef int(* crc_api_update) (const struct device *dev, struct crc_ctx *ctx, const void *buffer, size_t bufsize)
```

相关声明：[crc_api_update](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface__backend.html#ga7d6a2a6b119a8fb51d91e6f5f6269af7)、[device](../device_reference/P002_设备对象结构.md)、[crc_ctx](../hardware/P046_CRC上下文结构.md)。

向正在进行的 CRC 计算（Calculation）提供数据的回调 API。

<a id="r_gadaec1299bbc8b5a03e4b724b32064abc"></a>

```c
typedef int(* crc_api_finish) (const struct device *dev, struct crc_ctx *ctx)
```

相关声明：[crc_api_finish](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface__backend.html#gadaec1299bbc8b5a03e4b724b32064abc)、[device](../device_reference/P002_设备对象结构.md)、[crc_ctx](../hardware/P046_CRC上下文结构.md)。

结束 CRC 计算（Finalize Calculation）的回调 API。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 11.4\_枚举（Enumerations）

<a id="r_gab463a891df58c677e5cafb160dfdb9a3"></a>

```c
enum crc_state { CRC_STATE_IDLE = 0 , CRC_STATE_IN_PROGRESS }
```

相关声明：[crc_state](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#gab463a891df58c677e5cafb160dfdb9a3)、[CRC_STATE_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#ggab463a891df58c677e5cafb160dfdb9a3ad3b521b0f1ec5fc7760f22f318b68c56)、[CRC_STATE_IN_PROGRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#ggab463a891df58c677e5cafb160dfdb9a3a2b46dc7210559c77073ad46d5757c7a2)。

CRC 状态枚举（State Enumeration）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 11.5\_函数（Functions）

<a id="r_gae6f2adfd858b18765b2e58d8135c28fa"></a>

```c
int crc_begin (const struct device *dev, struct crc_ctx *ctx)
```

相关声明：[crc_begin](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#gae6f2adfd858b18765b2e58d8135c28fa)、[device](../device_reference/P002_设备对象结构.md)、[crc_ctx](../hardware/P046_CRC上下文结构.md)。

配置 CRC 单元（Unit）以进行计算。

<a id="r_gaf5e71e99b5838e4b21f30e4b2fb4a684"></a>

```c
int crc_update (const struct device *dev, struct crc_ctx *ctx, const void *buffer, size_t bufsize)
```

相关声明：[crc_update](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#gaf5e71e99b5838e4b21f30e4b2fb4a684)、[device](../device_reference/P002_设备对象结构.md)、[crc_ctx](../hardware/P046_CRC上下文结构.md)。

对给定数据缓冲区（Data Buffer）执行 CRC 计算并获取结果。

<a id="r_gab144200cba95d6cc08c85cf9c5c1dd91"></a>

```c
int crc_finish (const struct device *dev, struct crc_ctx *ctx)
```

相关声明：[crc_finish](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#gab144200cba95d6cc08c85cf9c5c1dd91)、[device](../device_reference/P002_设备对象结构.md)、[crc_ctx](../hardware/P046_CRC上下文结构.md)。

结束 CRC 计算（Finalize Calculation）。

<a id="r_gaed8caf868b83c4ea1271a9f5ab6abd35"></a>

```c
static int crc_verify (struct crc_ctx *ctx, crc_result_t expected)
```

相关声明：[crc_verify](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#gaed8caf868b83c4ea1271a9f5ab6abd35)、[crc_ctx](../hardware/P046_CRC上下文结构.md)、[crc_result_t](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#ga7c6663d361406882a73e8ba171840adc)。

验证 CRC 结果（Verify Result）。


## 11.6\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/sys/crc.h](../data_utilities/P005_CRC系统头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P152_crc.h_源码浏览.md)
- [crc_ctx](../hardware/P046_CRC上下文结构.md)
- [crc_driver_api](../hardware/P052_CRC驱动操作结构.md)
- [CRC_FLAG_REVERSE_INPUT](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#ga9686f52f45a6023d7e7c144732ab9202)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [CRC_FLAG_REVERSE_OUTPUT](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#gad2413454ab20a446fdc53f08ddd85a4e)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [crc_init_val_t](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#ga45ff64f03c4bfadd47ba66ce944c09bf)
- [crc_poly_t](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#ga938a05769aa6a61c22217611fb375218)
- [crc_result_t](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#ga7c6663d361406882a73e8ba171840adc)
- [crc_api_begin](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface__backend.html#ga8babc96e0e656e3974c5e3df32f59107)
- [device](../device_reference/P002_设备对象结构.md)
- [crc_api_update](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface__backend.html#ga7d6a2a6b119a8fb51d91e6f5f6269af7)
- [crc_api_finish](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface__backend.html#gadaec1299bbc8b5a03e4b724b32064abc)
- [crc_state](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#gab463a891df58c677e5cafb160dfdb9a3)
- [CRC_STATE_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#ggab463a891df58c677e5cafb160dfdb9a3ad3b521b0f1ec5fc7760f22f318b68c56)
- [CRC_STATE_IN_PROGRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#ggab463a891df58c677e5cafb160dfdb9a3a2b46dc7210559c77073ad46d5757c7a2)
- [crc_begin](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#gae6f2adfd858b18765b2e58d8135c28fa)
- [crc_update](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#gaf5e71e99b5838e4b21f30e4b2fb4a684)
- [crc_finish](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#gab144200cba95d6cc08c85cf9c5c1dd91)
- [crc_verify](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#gaed8caf868b83c4ea1271a9f5ab6abd35)

<a id="CRC_FLAGS"></a>
<a id="header-details"></a>

---

[上一章](P010_zephyr__audio__dmic.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P012_zephyr__drivers__mspi__devicetree.h_文件参考.md)
