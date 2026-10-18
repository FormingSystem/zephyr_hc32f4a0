---
id: learning.zephyr-docs.api-file-protocol-service-reference.page-19
title: zephyr__drivers__sensor__htu31d.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/htu31d_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_zephyr\_\_drivers\_\_sensor\_\_htu31d.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/htu31d_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

HTU31D传感器的扩展API头文件（Extended Sensor API Header）。

<a id="details"></a>

```c
#include <zephyr/device.h>
```

查看此文件的源码。

HTU31D 传感器扩展 API 的头文件。它公开片上加热器（On-chip Heater）、诊断寄存器（Diagnostics Register）和工厂写入序列号（Factory-programmed Serial Number）的 API；这些功能超出通用 Zephyr 传感器驱动抽象层的范围。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 19.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 诊断寄存器位标志（Diagnostics Register Bit Flags）

`htu31d_read_diagnostics()` 返回的诊断字节（Diagnostics Byte）中的位位置。

<a id="r_ga67d7943b289a59c6150daef738e40ceb"></a>

```c
#define HTU31D_DIAG_HEATER_ON BIT(0)
```

相关声明：[HTU31D_DIAG_HEATER_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__htu31d__interface.html#ga67d7943b289a59c6150daef738e40ceb)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

加热器（Heater）当前已启用。

<a id="r_ga75b6d870de1388b42511d34bcc65b286"></a>

```c
#define HTU31D_DIAG_TEMP_LOW_ERR BIT(1)
```

相关声明：[HTU31D_DIAG_TEMP_LOW_ERR](https://docs.zephyrproject.org/latest/doxygen/html/group__htu31d__interface.html#ga75b6d870de1388b42511d34bcc65b286)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

温度（Temperature）低于最小值。

<a id="r_ga07ad22feb0fc89bcc1c16971bd74e1ff"></a>

```c
#define HTU31D_DIAG_TEMP_HIGH_ERR BIT(2)
```

相关声明：[HTU31D_DIAG_TEMP_HIGH_ERR](https://docs.zephyrproject.org/latest/doxygen/html/group__htu31d__interface.html#ga07ad22feb0fc89bcc1c16971bd74e1ff)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

温度（Temperature）高于最大值。

<a id="r_ga97027a00d1c4ea06db6a2d22236ccf09"></a>

```c
#define HTU31D_DIAG_TEMP_OVER_ERR BIT(3)
```

相关声明：[HTU31D_DIAG_TEMP_OVER_ERR](https://docs.zephyrproject.org/latest/doxygen/html/group__htu31d__interface.html#ga97027a00d1c4ea06db6a2d22236ccf09)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

温度下溢／上溢（Temperature Under/Over-run）。

<a id="r_gaa08ff4f3d320249213925f1fb220d29a"></a>

```c
#define HTU31D_DIAG_HUMI_LOW_ERR BIT(4)
```

相关声明：[HTU31D_DIAG_HUMI_LOW_ERR](https://docs.zephyrproject.org/latest/doxygen/html/group__htu31d__interface.html#gaa08ff4f3d320249213925f1fb220d29a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

湿度（Humidity）低于最小值。

<a id="r_gaa5d049d701095c976fb7a7f27d6a4878"></a>

```c
#define HTU31D_DIAG_HUMI_HIGH_ERR BIT(5)
```

相关声明：[HTU31D_DIAG_HUMI_HIGH_ERR](https://docs.zephyrproject.org/latest/doxygen/html/group__htu31d__interface.html#gaa5d049d701095c976fb7a7f27d6a4878)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

湿度（Humidity）高于最大值。

<a id="r_ga06035755bd7c270e481b2434022b1664"></a>

```c
#define HTU31D_DIAG_HUMI_OVER_ERR BIT(6)
```

相关声明：[HTU31D_DIAG_HUMI_OVER_ERR](https://docs.zephyrproject.org/latest/doxygen/html/group__htu31d__interface.html#ga06035755bd7c270e481b2434022b1664)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

湿度下溢／上溢（Humidity Under/Over-run）。

<a id="r_gad72c35292b8838b23fc7df3a102c6ba9"></a>

```c
#define HTU31D_DIAG_NVM_ERR BIT(7)
```

相关声明：[HTU31D_DIAG_NVM_ERR](https://docs.zephyrproject.org/latest/doxygen/html/group__htu31d__interface.html#gad72c35292b8838b23fc7df3a102c6ba9)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

非易失性存储器（NVM）校验和错误（Checksum Error）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 19.2\_函数（Functions）

<a id="r_ga607e81aff14b1638989d6f85f0fb661f"></a>

```c
int htu31d_heater_set (const struct device *dev, bool enable)
```

相关声明：[htu31d_heater_set](https://docs.zephyrproject.org/latest/doxygen/html/group__htu31d__interface.html#ga607e81aff14b1638989d6f85f0fb661f)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用或禁用片上加热器（On-chip Heater）。

<a id="r_gad20e48337c29bf96075c428f2c6f6549"></a>

```c
int htu31d_read_diagnostics (const struct device *dev, uint8_t *diag)
```

相关声明：[htu31d_read_diagnostics](https://docs.zephyrproject.org/latest/doxygen/html/group__htu31d__interface.html#gad20e48337c29bf96075c428f2c6f6549)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取传感器诊断寄存器（Diagnostics Register）。

<a id="r_ga18d4854388d8f53cf94c38b81b29ef2f"></a>

```c
int htu31d_read_serial (const struct device *dev, uint32_t *serial)
```

相关声明：[htu31d_read_serial](https://docs.zephyrproject.org/latest/doxygen/html/group__htu31d__interface.html#ga18d4854388d8f53cf94c38b81b29ef2f)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

读取工厂写入的 24 位序列号（Factory-programmed Serial Number）。


## 19.3\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P324_htu31d.h_源码浏览.md)
- [htu31d_read_diagnostics()](https://docs.zephyrproject.org/latest/doxygen/html/group__htu31d__interface.html#gad20e48337c29bf96075c428f2c6f6549)
- [HTU31D_DIAG_HEATER_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__htu31d__interface.html#ga67d7943b289a59c6150daef738e40ceb)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [HTU31D_DIAG_TEMP_LOW_ERR](https://docs.zephyrproject.org/latest/doxygen/html/group__htu31d__interface.html#ga75b6d870de1388b42511d34bcc65b286)
- [HTU31D_DIAG_TEMP_HIGH_ERR](https://docs.zephyrproject.org/latest/doxygen/html/group__htu31d__interface.html#ga07ad22feb0fc89bcc1c16971bd74e1ff)
- [HTU31D_DIAG_TEMP_OVER_ERR](https://docs.zephyrproject.org/latest/doxygen/html/group__htu31d__interface.html#ga97027a00d1c4ea06db6a2d22236ccf09)
- [HTU31D_DIAG_HUMI_LOW_ERR](https://docs.zephyrproject.org/latest/doxygen/html/group__htu31d__interface.html#gaa08ff4f3d320249213925f1fb220d29a)
- [HTU31D_DIAG_HUMI_HIGH_ERR](https://docs.zephyrproject.org/latest/doxygen/html/group__htu31d__interface.html#gaa5d049d701095c976fb7a7f27d6a4878)
- [HTU31D_DIAG_HUMI_OVER_ERR](https://docs.zephyrproject.org/latest/doxygen/html/group__htu31d__interface.html#ga06035755bd7c270e481b2434022b1664)
- [HTU31D_DIAG_NVM_ERR](https://docs.zephyrproject.org/latest/doxygen/html/group__htu31d__interface.html#gad72c35292b8838b23fc7df3a102c6ba9)
- [htu31d_heater_set](https://docs.zephyrproject.org/latest/doxygen/html/group__htu31d__interface.html#ga607e81aff14b1638989d6f85f0fb661f)
- [device](../device_reference/P002_设备对象结构.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [htu31d_read_serial](https://docs.zephyrproject.org/latest/doxygen/html/group__htu31d__interface.html#ga18d4854388d8f53cf94c38b81b29ef2f)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>

---

[上一章](P018_zephyr__drivers__sensor__grow_r502a.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P020_zephyr__net__icmp.h_文件参考.md)
