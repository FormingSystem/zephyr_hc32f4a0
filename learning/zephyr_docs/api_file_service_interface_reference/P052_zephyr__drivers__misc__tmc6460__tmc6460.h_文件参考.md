---
id: learning.zephyr-docs.api-file-service-interface-reference.page-52
title: zephyr__drivers__misc__tmc6460__tmc6460.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/tmc6460_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第52章\_zephyr\_\_drivers\_\_misc\_\_tmc6460\_\_tmc6460.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/tmc6460_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

TMC6460磁场定向控制（FOC）栅极驱动器的公共API。

<a id="details"></a>

```c
#include <zephyr/types.h>
#include <zephyr/device.h>
#include <zephyr/sys/util.h>
```

查看此文件的源码。

TMC6460磁场定向控制（FOC）栅极驱动器的公共API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 52.1\_数据结构（Data Structures）

<a id="r_tmc6460_5Ffield"></a>

```c
struct tmc6460_field
```

相关声明：[tmc6460_field](../device_power_control_model_reference/P096_tmc6460_field_结构体.md)。

描述TMC6460寄存器中的位域（Bitfield）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 52.2\_函数（Functions）

<a id="r_ga59b012bb5bced0ce523f73ee1386e84e"></a>

```c
int tmc6460_write (const struct device *dev, uint16_t reg_addr, uint32_t reg_val)
```

相关声明：[tmc6460_write](https://docs.zephyrproject.org/latest/doxygen/html/group__tmc6460__interface.html#ga59b012bb5bced0ce523f73ee1386e84e)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向 TMC6460 寄存器写入一个值。

<a id="r_gac5859fa6261be5e1b887ba76731b8423"></a>

```c
int tmc6460_read (const struct device *dev, uint16_t reg_addr, uint32_t *reg_val)
```

相关声明：[tmc6460_read](https://docs.zephyrproject.org/latest/doxygen/html/group__tmc6460__interface.html#gac5859fa6261be5e1b887ba76731b8423)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

从 TMC6460 寄存器读取一个值。

<a id="r_ga86cd8bceebe0ebcfd038c1eaea9d275e"></a>

```c
int tmc6460_rtmi_stream_write (const struct device *dev, uint8_t rtmi_index, uint32_t value)
```

相关声明：[tmc6460_rtmi_stream_write](https://docs.zephyrproject.org/latest/doxygen/html/group__tmc6460__interface.html#ga86cd8bceebe0ebcfd038c1eaea9d275e)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向RTMI 流式寄存器槽（Streamed Register Slot）写入一个值，仅适用于 UART。

<a id="r_ga65e91ddd2249dfefc8261ca2a806c491"></a>

```c
int tmc6460_enable (const struct device *dev)
```

相关声明：[tmc6460_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__tmc6460__interface.html#ga65e91ddd2249dfefc8261ca2a806c491)、[device](../device_reference/P002_设备对象结构.md)。

启用 TMC6460 栅极驱动器（Gate Driver）。

<a id="r_ga1d7408f27b645db9718d17163921f9a8"></a>

```c
int tmc6460_disable (const struct device *dev)
```

相关声明：[tmc6460_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__tmc6460__interface.html#ga1d7408f27b645db9718d17163921f9a8)、[device](../device_reference/P002_设备对象结构.md)。

禁用 TMC6460 栅极驱动器（Gate Driver）。

<a id="r_ga52909d4e6831887c5d4e8835ab93c164"></a>

```c
int tmc6460_poll_flag (const struct device *dev, uint16_t reg_addr, uint32_t flag_mask, uint32_t poll_interval_ms, uint32_t timeout_ms)
```

相关声明：[tmc6460_poll_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__tmc6460__interface.html#ga52909d4e6831887c5d4e8835ab93c164)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

轮询寄存器，直到指定标志位（Flag Bits）全部置位或超时。

<a id="r_ga00038972be11ffdaa324845f79f85387"></a>

```c
static uint32_t tmc6460_field_update (uint32_t reg_val, struct tmc6460_field field, uint32_t field_val)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[tmc6460_field_update](https://docs.zephyrproject.org/latest/doxygen/html/group__tmc6460__interface.html#ga00038972be11ffdaa324845f79f85387)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[tmc6460_field](../device_power_control_model_reference/P096_tmc6460_field_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

更新寄存器值中的位域（Bitfield），仅操作内存中的值。

<a id="r_ga65fdd1bbdc1cc88a341c63fc1894c748"></a>

```c
static int tmc6460_field_write (const struct device *dev, struct tmc6460_field field, uint32_t field_val)
```

相关声明：[tmc6460_field_write](https://docs.zephyrproject.org/latest/doxygen/html/group__tmc6460__interface.html#ga65fdd1bbdc1cc88a341c63fc1894c748)、[device](../device_reference/P002_设备对象结构.md)、[tmc6460_field](../device_power_control_model_reference/P096_tmc6460_field_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

对设备上的位域（Bitfield）执行读－改－写（Read-modify-write）。


## 52.3\_原页交叉引用（Cross References）

- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/tmc6460_8h_source.html)
- [tmc6460_field](../device_power_control_model_reference/P096_tmc6460_field_结构体.md)
- [tmc6460_write](https://docs.zephyrproject.org/latest/doxygen/html/group__tmc6460__interface.html#ga59b012bb5bced0ce523f73ee1386e84e)
- [device](../device_reference/P002_设备对象结构.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [tmc6460_read](https://docs.zephyrproject.org/latest/doxygen/html/group__tmc6460__interface.html#gac5859fa6261be5e1b887ba76731b8423)
- [tmc6460_rtmi_stream_write](https://docs.zephyrproject.org/latest/doxygen/html/group__tmc6460__interface.html#ga86cd8bceebe0ebcfd038c1eaea9d275e)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [tmc6460_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__tmc6460__interface.html#ga65e91ddd2249dfefc8261ca2a806c491)
- [tmc6460_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__tmc6460__interface.html#ga1d7408f27b645db9718d17163921f9a8)
- [tmc6460_poll_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__tmc6460__interface.html#ga52909d4e6831887c5d4e8835ab93c164)
- [tmc6460_field_update](https://docs.zephyrproject.org/latest/doxygen/html/group__tmc6460__interface.html#ga00038972be11ffdaa324845f79f85387)
- [tmc6460_field_write](https://docs.zephyrproject.org/latest/doxygen/html/group__tmc6460__interface.html#ga65fdd1bbdc1cc88a341c63fc1894c748)

<a id="header-details"></a>

---

[上一章](P051_zephyr__net__tls_credentials.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P053_zephyr__net__trickle.h_文件参考.md)
