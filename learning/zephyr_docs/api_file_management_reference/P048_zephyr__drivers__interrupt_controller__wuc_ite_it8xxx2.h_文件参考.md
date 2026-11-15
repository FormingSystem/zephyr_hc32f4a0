---
id: learning.zephyr-docs.api-file-management-reference.page-48
title: zephyr__drivers__interrupt_controller__wuc_ite_it8xxx2.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/wuc__ite__it8xxx2_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第48章\_zephyr\_\_drivers\_\_interrupt\_controller\_\_wuc\_ite\_it8xxx2.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/wuc__ite__it8xxx2_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/device.h>
#include <stdint.h>
```

查看此文件的源码。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 48.1\_函数（Functions）

<a id="r_a12abd49530eee59cb3d9670c35c307b1"></a>

```c
void it8xxx2_wuc_enable (const struct device *dev, uint8_t mask)
```

相关声明：[it8xxx2_wuc_enable](#a12abd49530eee59cb3d9670c35c307b1)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

对应输入上的触发条件（trigger condition）向嵌入式控制器（EC）的电源管理控制模块产生唤醒信号（wake-up signal）。

<a id="r_af707d0b461010aea4fcfbfbeb82d0b2b"></a>

```c
void it8xxx2_wuc_disable (const struct device *dev, uint8_t mask)
```

相关声明：[it8xxx2_wuc_disable](#af707d0b461010aea4fcfbfbeb82d0b2b)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

对应输入上的触发条件不会置位唤醒信号，信号已取消而非处于挂起状态（canceled, not pending）。

<a id="r_ad48382e2c3fd0d12c3a1334d863a9065"></a>

```c
void it8xxx2_wuc_clear_status (const struct device *dev, uint8_t mask)
```

相关声明：[it8xxx2_wuc_clear_status](#ad48382e2c3fd0d12c3a1334d863a9065)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

通过写 1 清零（write-1-clear）清除对应输入上出现的触发条件。

<a id="r_ab589f992436176f288056e219ead7972"></a>

```c
void it8xxx2_wuc_set_polarity (const struct device *dev, uint8_t mask, uint32_t flags)
```

相关声明：[it8xxx2_wuc_set_polarity](#ab589f992436176f288056e219ead7972)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

选择对应输入的触发边沿模式（trigger edge mode）。

## 48.2\_详细说明（Detailed Documentation）

<a id="ad48382e2c3fd0d12c3a1334d863a9065"></a>

### `it8xxx2_wuc_clear_status()`

```c
void it8xxx2_wuc_clear_status ( const struct device * dev, uint8_t mask )
```

通过写 1 清零（write-1-clear）清除对应输入上出现的触发条件。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `mask` | 唤醒控制器（WUC）组的引脚掩码（pin mask）。 |

<a id="af707d0b461010aea4fcfbfbeb82d0b2b"></a>

### `it8xxx2_wuc_disable()`

```c
void it8xxx2_wuc_disable ( const struct device * dev, uint8_t mask )
```

对应输入上的触发条件不会置位唤醒信号，信号已取消而非处于挂起状态（canceled, not pending）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `mask` | 唤醒控制器（WUC）组的引脚掩码（pin mask）。 |

<a id="a12abd49530eee59cb3d9670c35c307b1"></a>

### `it8xxx2_wuc_enable()`

```c
void it8xxx2_wuc_enable ( const struct device * dev, uint8_t mask )
```

对应输入上的触发条件（trigger condition）向嵌入式控制器（EC）的电源管理控制模块产生唤醒信号（wake-up signal）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `mask` | 唤醒控制器（WUC）组的引脚掩码（pin mask）。 |

<a id="ab589f992436176f288056e219ead7972"></a>

### `it8xxx2_wuc_set_polarity()`

```c
void it8xxx2_wuc_set_polarity ( const struct device * dev, uint8_t mask, uint32_t flags )
```

选择对应输入的触发边沿模式（trigger edge mode）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `mask` | 唤醒控制器（WUC）组的引脚掩码（pin mask）。 |
| `flags` | 选择触发边沿模式。 |


## 48.3\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P929_wuc_ite_it8xxx2.h_源码浏览.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P047_zephyr__dt-bindings__video__video-interfaces.h_文件参考.md) · [返回大纲](大纲.md)
