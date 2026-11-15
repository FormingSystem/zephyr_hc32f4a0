---
id: learning.zephyr-docs.api-file-system-power-reference.page-1
title: zephyr__drivers__i3c__addresses.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/addresses_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_zephyr\_\_drivers\_\_i3c\_\_addresses.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/addresses_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stdint.h>
#include <zephyr/device.h>
#include <zephyr/sys/util.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.1\_数据结构（Data Structures）

<a id="r_i3c_5Faddr_5Fslots"></a>

```c
struct i3c_addr_slots
```

相关声明：[i3c_addr_slots](../hardware/P384_I3C地址槽结构.md)。

用于跟踪I3C总线地址的结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.2\_宏定义（Macros）

<a id="r_gad516c48319d08db1886719645a682787"></a>

```c
#define I3C_BROADCAST_ADDR 0x7E
```

相关声明：[I3C_BROADCAST_ADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#gad516c48319d08db1886719645a682787)。

I3C 总线上的广播地址（Broadcast Address）。

<a id="r_ga85a120abff94213b57ce4912f58d5ed8"></a>

```c
#define I3C_MAX_ADDR 0x7F
```

相关声明：[I3C_MAX_ADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#ga85a120abff94213b57ce4912f58d5ed8)。

设备地址（Device Address）的最大值。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 1.3\_枚举（Enumerations）

<a id="r_gaacbed5bbaae3b36d6f3ba175074aecd0"></a>

```c
enum i3c_addr_slot_status { I3C_ADDR_SLOT_STATUS_FREE = 0U , I3C_ADDR_SLOT_STATUS_RSVD , I3C_ADDR_SLOT_STATUS_I3C_DEV , I3C_ADDR_SLOT_STATUS_I2C_DEV , I3C_ADDR_SLOT_STATUS_MASK = 0x03U }
```

相关声明：[i3c_addr_slot_status](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#gaacbed5bbaae3b36d6f3ba175074aecd0)、[I3C_ADDR_SLOT_STATUS_FREE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#ggaacbed5bbaae3b36d6f3ba175074aecd0a847927f32a28341e0d356c9ec1ccfb2e)、[I3C_ADDR_SLOT_STATUS_RSVD](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#ggaacbed5bbaae3b36d6f3ba175074aecd0a0af543ae2b67f2e8055d496689437d45)、[I3C_ADDR_SLOT_STATUS_I3C_DEV](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#ggaacbed5bbaae3b36d6f3ba175074aecd0a38b0fd286477bcc936132c25d787749a)、[I3C_ADDR_SLOT_STATUS_I2C_DEV](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#ggaacbed5bbaae3b36d6f3ba175074aecd0ac8d91073cf590626b58bbf5f5b8d9c55)、[I3C_ADDR_SLOT_STATUS_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#ggaacbed5bbaae3b36d6f3ba175074aecd0a2093cda582c682b292deb065956ca280)。

表示地址状态的枚举（Enum）：保留（Reserved）、连接有 I2C/I3C 设备，或未连接设备。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.4\_函数（Functions）

<a id="r_gaf2be07d40d885f60997b5eb5edcf910f"></a>

```c
int i3c_addr_slots_init (const struct device *dev)
```

相关声明：[i3c_addr_slots_init](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#gaf2be07d40d885f60997b5eb5edcf910f)、[device](../device_reference/P002_设备对象结构.md)。

初始化 I3C 地址槽结构体（Address Slots Struct）。

<a id="r_gae4eb7e22abde57c9bcfdc8407c0da68d"></a>

```c
void i3c_addr_slots_set (struct i3c_addr_slots *slots, uint8_t dev_addr, enum i3c_addr_slot_status status)
```

相关声明：[i3c_addr_slots_set](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#gae4eb7e22abde57c9bcfdc8407c0da68d)、[i3c_addr_slots](../hardware/P384_I3C地址槽结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[i3c_addr_slot_status](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#gaacbed5bbaae3b36d6f3ba175074aecd0)。

设置设备的地址状态（Address Status）。

<a id="r_ga3dc021699fc489995b0bbe299753a33e"></a>

```c
enum i3c_addr_slot_status i3c_addr_slots_status (struct i3c_addr_slots *slots, uint8_t dev_addr)
```

相关声明：[i3c_addr_slot_status](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#gaacbed5bbaae3b36d6f3ba175074aecd0)、[i3c_addr_slots_status](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#ga3dc021699fc489995b0bbe299753a33e)、[i3c_addr_slots](../hardware/P384_I3C地址槽结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取设备的地址状态（Address Status）。

<a id="r_gadc2539a0b8793ec5b5ff34e57e68fb60"></a>

```c
bool i3c_addr_slots_is_free (struct i3c_addr_slots *slots, uint8_t dev_addr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[i3c_addr_slots_is_free](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#gadc2539a0b8793ec5b5ff34e57e68fb60)、[i3c_addr_slots](../hardware/P384_I3C地址槽结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

检查地址是否空闲（Free）。

<a id="r_gad7eddb7aebf337a31f336ccf3f78cad1"></a>

```c
uint8_t i3c_addr_slots_next_free_find (struct i3c_addr_slots *slots, uint8_t start_addr)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[i3c_addr_slots_next_free_find](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#gad7eddb7aebf337a31f336ccf3f78cad1)、[i3c_addr_slots](../hardware/P384_I3C地址槽结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

查找下一个空闲地址（Free Address）。

<a id="r_gaf384836871625543aaa3f087e688f1b4"></a>

```c
static void i3c_addr_slots_mark_free (struct i3c_addr_slots *addr_slots, uint8_t addr)
```

相关声明：[i3c_addr_slots_mark_free](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#gaf384836871625543aaa3f087e688f1b4)、[i3c_addr_slots](../hardware/P384_I3C地址槽结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

在设备列表中将地址标为空闲（Free，即未使用）。

<a id="r_gac976f542afb29d2360fc2c8d797dbac5"></a>

```c
static void i3c_addr_slots_mark_rsvd (struct i3c_addr_slots *addr_slots, uint8_t addr)
```

相关声明：[i3c_addr_slots_mark_rsvd](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#gac976f542afb29d2360fc2c8d797dbac5)、[i3c_addr_slots](../hardware/P384_I3C地址槽结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

在设备列表中将地址标为保留（Reserved）。

<a id="r_gae10e6aba3335b78a2be728a5f495b436"></a>

```c
static void i3c_addr_slots_mark_i3c (struct i3c_addr_slots *addr_slots, uint8_t addr)
```

相关声明：[i3c_addr_slots_mark_i3c](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#gae10e6aba3335b78a2be728a5f495b436)、[i3c_addr_slots](../hardware/P384_I3C地址槽结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

在设备列表中将地址标为 I3C 设备（Device）。

<a id="r_gad5fc6b00171a4fdf76de20e6da3fbb32"></a>

```c
static void i3c_addr_slots_mark_i2c (struct i3c_addr_slots *addr_slots, uint8_t addr)
```

相关声明：[i3c_addr_slots_mark_i2c](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#gad5fc6b00171a4fdf76de20e6da3fbb32)、[i3c_addr_slots](../hardware/P384_I3C地址槽结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

在设备列表中将地址标为 I2C 设备（Device）。


## 1.5\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [查看此文件的源码。](../api_source_supplement_reference/P003_addresses.h_源码浏览.md)
- [i3c_addr_slots](../hardware/P384_I3C地址槽结构.md)
- [I3C_BROADCAST_ADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#gad516c48319d08db1886719645a682787)
- [I3C_MAX_ADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#ga85a120abff94213b57ce4912f58d5ed8)
- [i3c_addr_slot_status](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#gaacbed5bbaae3b36d6f3ba175074aecd0)
- [I3C_ADDR_SLOT_STATUS_FREE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#ggaacbed5bbaae3b36d6f3ba175074aecd0a847927f32a28341e0d356c9ec1ccfb2e)
- [I3C_ADDR_SLOT_STATUS_RSVD](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#ggaacbed5bbaae3b36d6f3ba175074aecd0a0af543ae2b67f2e8055d496689437d45)
- [I3C_ADDR_SLOT_STATUS_I3C_DEV](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#ggaacbed5bbaae3b36d6f3ba175074aecd0a38b0fd286477bcc936132c25d787749a)
- [I3C_ADDR_SLOT_STATUS_I2C_DEV](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#ggaacbed5bbaae3b36d6f3ba175074aecd0ac8d91073cf590626b58bbf5f5b8d9c55)
- [I3C_ADDR_SLOT_STATUS_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#ggaacbed5bbaae3b36d6f3ba175074aecd0a2093cda582c682b292deb065956ca280)
- [i3c_addr_slots_init](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#gaf2be07d40d885f60997b5eb5edcf910f)
- [device](../device_reference/P002_设备对象结构.md)
- [i3c_addr_slots_set](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#gae4eb7e22abde57c9bcfdc8407c0da68d)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [i3c_addr_slots_status](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#ga3dc021699fc489995b0bbe299753a33e)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [i3c_addr_slots_is_free](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#gadc2539a0b8793ec5b5ff34e57e68fb60)
- [i3c_addr_slots_next_free_find](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#gad7eddb7aebf337a31f336ccf3f78cad1)
- [i3c_addr_slots_mark_free](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#gaf384836871625543aaa3f087e688f1b4)
- [i3c_addr_slots_mark_rsvd](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#gac976f542afb29d2360fc2c8d797dbac5)
- [i3c_addr_slots_mark_i3c](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#gae10e6aba3335b78a2be728a5f495b436)
- [i3c_addr_slots_mark_i2c](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#gad5fc6b00171a4fdf76de20e6da3fbb32)

---

[返回大纲](大纲.md) · [下一章](P002_zephyr__dt-bindings__clock__bflb_bl70x_clock.h_文件参考.md)
