---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-84
title: sdhc_io_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsdhc__io.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第84章\_sdhc\_io\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsdhc__io.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

SD主控制器（Host Controller）的输入输出控制结构。

```c
#include <zephyr/drivers/sdhc.h>
```

<a id="details"></a>

SD 主机控制器 I/O 控制结构体。控制 SDHC 的 I/O 设置。注意，对于处于 SPI 模式的主机控制器，只有其中一部分设置适用。填充此结构体后，调用 `sdhc_set_io` 应用 I/O 设置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 84.1\_数据成员（Data Fields）

<a id="r_aaa15197b8f1947a67dcd8522aa62afc5"></a>

```c
enum sdhc_clock_speed clock
```

相关声明：[sdhc_clock_speed](https://docs.zephyrproject.org/latest/doxygen/html/sd__spec_8h.html#a9660a61775e481ae4093e11ce9336539)、[clock](#aaa15197b8f1947a67dcd8522aa62afc5)。

时钟频率（Clock rate）。

<a id="r_a2b4456b108778aada0d42b8c8107b3e9"></a>

```c
enum sdhc_bus_mode bus_mode
```

相关声明：[sdhc_bus_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gaf26909ae9fffdc6ac02abd8094d16dc8)、[bus_mode](#a2b4456b108778aada0d42b8c8107b3e9)。

命令输出模式。

<a id="r_ac503fb9fba7ffdb01695a77780972930"></a>

```c
enum sdhc_power power_mode
```

相关声明：[sdhc_power](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gad63742820bb18ca18cd2f96547e12eb9)、[power_mode](#ac503fb9fba7ffdb01695a77780972930)。

SD 供电模式（Power supply mode）。

<a id="r_a904b05c7e73e80bb7326b0bfcb6b7103"></a>

```c
enum sdhc_bus_width bus_width
```

相关声明：[sdhc_bus_width](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gad8bab66ec505c8356fac7785a8955448)、[bus_width](#a904b05c7e73e80bb7326b0bfcb6b7103)。

SD 总线宽度。

<a id="r_a85c50f625d8606bb4c07a228c0de24e4"></a>

```c
enum sdhc_timing_mode timing
```

相关声明：[sdhc_timing_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ga6f006ca8fd9ff8a68ac46a0bb7d4bc90)、[timing](#a85c50f625d8606bb4c07a228c0de24e4)。

SD 总线时序（Bus timing）。

<a id="r_afa9a07a8734e9d39b29da0697cf60289"></a>

```c
bool enhanced_strobe
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[enhanced_strobe](#afa9a07a8734e9d39b29da0697cf60289)。

eMMC HS400 增强选通状态。

<a id="r_a0c62aaa1a8a7700ebb00a38ce2e57d11"></a>

```c
enum sd_driver_type driver_type
```

相关声明：[sd_driver_type](https://docs.zephyrproject.org/latest/doxygen/html/sd__spec_8h.html#a314c38b1b0603c003e67b5dec2228d4b)、[driver_type](#a0c62aaa1a8a7700ebb00a38ce2e57d11)。

SD 驱动类型（Driver type）。

<a id="r_ade8b8cd4e4f4b21f5fa8e3fb2661917e"></a>

```c
enum sd_voltage signal_voltage
```

相关声明：[sd_voltage](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ga34041edf280f125b8500809226b3de5d)、[signal_voltage](#ade8b8cd4e4f4b21f5fa8e3fb2661917e)。

I/O 信号电压，通常为 1.8 V 或 3.3 V。

## 84.2\_详细说明（Detailed Documentation）

<a id="a2b4456b108778aada0d42b8c8107b3e9"></a>

### `bus_mode`

```c
enum sdhc_bus_mode sdhc_io::bus_mode
```

命令输出模式。

<a id="a904b05c7e73e80bb7326b0bfcb6b7103"></a>

### `bus_width`

```c
enum sdhc_bus_width sdhc_io::bus_width
```

SD 总线宽度。

<a id="aaa15197b8f1947a67dcd8522aa62afc5"></a>

### `clock`

```c
enum sdhc_clock_speed sdhc_io::clock
```

时钟频率（Clock rate）。

<a id="a0c62aaa1a8a7700ebb00a38ce2e57d11"></a>

### `driver_type`

```c
enum sd_driver_type sdhc_io::driver_type
```

SD 驱动类型（Driver type）。

<a id="afa9a07a8734e9d39b29da0697cf60289"></a>

### `enhanced_strobe`

```c
bool sdhc_io::enhanced_strobe
```

eMMC HS400 增强选通状态。

<a id="ac503fb9fba7ffdb01695a77780972930"></a>

### `power_mode`

```c
enum sdhc_power sdhc_io::power_mode
```

SD 供电模式（Power supply mode）。

<a id="ade8b8cd4e4f4b21f5fa8e3fb2661917e"></a>

### `signal_voltage`

```c
enum sd_voltage sdhc_io::signal_voltage
```

I/O 信号电压，通常为 1.8 V 或 3.3 V。

<a id="a85c50f625d8606bb4c07a228c0de24e4"></a>

### `timing`

```c
enum sdhc_timing_mode sdhc_io::timing
```

SD 总线时序（Bus timing）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/sdhc.h`

## 84.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sdhc.h](https://docs.zephyrproject.org/latest/doxygen/html/sdhc_8h_source.html)
- [sdhc_clock_speed](https://docs.zephyrproject.org/latest/doxygen/html/sd__spec_8h.html#a9660a61775e481ae4093e11ce9336539)
- [sdhc_bus_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gaf26909ae9fffdc6ac02abd8094d16dc8)
- [sdhc_power](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gad63742820bb18ca18cd2f96547e12eb9)
- [sdhc_bus_width](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gad8bab66ec505c8356fac7785a8955448)
- [sdhc_timing_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ga6f006ca8fd9ff8a68ac46a0bb7d4bc90)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [sd_driver_type](https://docs.zephyrproject.org/latest/doxygen/html/sd__spec_8h.html#a314c38b1b0603c003e67b5dec2228d4b)
- [sd_voltage](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ga34041edf280f125b8500809226b3de5d)
- [sdhc_set_io](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ga0e6d8259cca442bd1356d00f668d35c4)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P083_sdhc_host_props_结构体.md) · [返回大纲](大纲.md) · [下一章](P085_sdio_cis_结构体.md)
