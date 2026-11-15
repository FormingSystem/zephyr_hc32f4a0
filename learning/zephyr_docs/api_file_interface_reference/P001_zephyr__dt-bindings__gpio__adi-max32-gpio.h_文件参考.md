---
id: learning.zephyr-docs.api-file-interface-reference.page-1
title: zephyr__dt-bindings__gpio__adi-max32-gpio.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/adi-max32-gpio_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_zephyr\_\_dt-bindings\_\_gpio\_\_adi-max32-gpio.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/adi-max32-gpio_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.1\_宏定义（Macros）

<a id="define-members-0"></a>

### MAX32 GPIO 驱动标志（drive flags）。

MAX32 GPIO 驱动标志（drive flags）。

驱动标志（Drive Flags）编码在 `gpio_dt_flags_t` 的高 8 位，具体如下：

<a id="r_ga267d4548e80843b5b5678d2050cbef73"></a>

```c
#define MAX32_GPIO_VSEL_POS (8U)
```

相关声明：[MAX32_GPIO_VSEL_POS](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#ga267d4548e80843b5b5678d2050cbef73)。

GPIO 电压选择（Voltage Select）。

<a id="r_ga57b502aa34453a1af1eb5103221c5bde"></a>

```c
#define MAX32_GPIO_VSEL_MASK (0x01U << MAX32_GPIO_VSEL_POS)
```

相关声明：[MAX32_GPIO_VSEL_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#ga57b502aa34453a1af1eb5103221c5bde)、[MAX32_GPIO_VSEL_POS](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#ga267d4548e80843b5b5678d2050cbef73)。

<a id="r_ga476d2376c91da2a1cf1bdfd0a7a95198"></a>

```c
#define MAX32_GPIO_VSEL_VDDIO (0U << MAX32_GPIO_VSEL_POS)
```

相关声明：[MAX32_GPIO_VSEL_VDDIO](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#ga476d2376c91da2a1cf1bdfd0a7a95198)、[MAX32_GPIO_VSEL_POS](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#ga267d4548e80843b5b5678d2050cbef73)。

<a id="r_ga964594ce9114dc57a9e50e416e948147"></a>

```c
#define MAX32_GPIO_VSEL_VDDIOH (1U << MAX32_GPIO_VSEL_POS)
```

相关声明：[MAX32_GPIO_VSEL_VDDIOH](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#ga964594ce9114dc57a9e50e416e948147)、[MAX32_GPIO_VSEL_POS](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#ga267d4548e80843b5b5678d2050cbef73)。

<a id="r_ga8f42437e9d5cbc3bb2d9d58fee643bc5"></a>

```c
#define MAX32_GPIO_DRV_STRENGTH_POS (9U)
```

相关声明：[MAX32_GPIO_DRV_STRENGTH_POS](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#ga8f42437e9d5cbc3bb2d9d58fee643bc5)。

GPIO 驱动强度选择（Drive Strength Select）。

<a id="r_gaefce80e7ae44c9f9397e3b4f02a59893"></a>

```c
#define MAX32_GPIO_DRV_STRENGTH_MASK (0x03U << MAX32_GPIO_DRV_STRENGTH_POS)
```

相关声明：[MAX32_GPIO_DRV_STRENGTH_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#gaefce80e7ae44c9f9397e3b4f02a59893)、[MAX32_GPIO_DRV_STRENGTH_POS](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#ga8f42437e9d5cbc3bb2d9d58fee643bc5)。

<a id="r_gaf783f2b803f4772b5bf4c83f616b8a8a"></a>

```c
#define MAX32_GPIO_DRV_STRENGTH_0 (0U << MAX32_GPIO_DRV_STRENGTH_POS)
```

相关声明：[MAX32_GPIO_DRV_STRENGTH_0](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#gaf783f2b803f4772b5bf4c83f616b8a8a)、[MAX32_GPIO_DRV_STRENGTH_POS](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#ga8f42437e9d5cbc3bb2d9d58fee643bc5)。

<a id="r_ga2e0abcd63dbbef23c2368be433c1909d"></a>

```c
#define MAX32_GPIO_DRV_STRENGTH_1 (1U << MAX32_GPIO_DRV_STRENGTH_POS)
```

相关声明：[MAX32_GPIO_DRV_STRENGTH_1](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#ga2e0abcd63dbbef23c2368be433c1909d)、[MAX32_GPIO_DRV_STRENGTH_POS](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#ga8f42437e9d5cbc3bb2d9d58fee643bc5)。

<a id="r_gae7199008d9e034361d80355651128fdd"></a>

```c
#define MAX32_GPIO_DRV_STRENGTH_2 (2U << MAX32_GPIO_DRV_STRENGTH_POS)
```

相关声明：[MAX32_GPIO_DRV_STRENGTH_2](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#gae7199008d9e034361d80355651128fdd)、[MAX32_GPIO_DRV_STRENGTH_POS](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#ga8f42437e9d5cbc3bb2d9d58fee643bc5)。

<a id="r_gacf1c36bc17e552528ef20d4a8ae67f36"></a>

```c
#define MAX32_GPIO_DRV_STRENGTH_3 (3U << MAX32_GPIO_DRV_STRENGTH_POS)
```

相关声明：[MAX32_GPIO_DRV_STRENGTH_3](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#gacf1c36bc17e552528ef20d4a8ae67f36)、[MAX32_GPIO_DRV_STRENGTH_POS](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#ga8f42437e9d5cbc3bb2d9d58fee643bc5)。

<a id="r_gad20918791adf470f4421a2cbc1c7beaf"></a>

```c
#define MAX32_GPIO_WEAK_PULL_UP_POS (11U)
```

相关声明：[MAX32_GPIO_WEAK_PULL_UP_POS](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#gad20918791adf470f4421a2cbc1c7beaf)。

GPIO 偏置弱上拉（weak pull-up）选择，上拉至 VDDIO（1 MΩ）。

<a id="r_gac3a2881b03a0e130c0dc174a7aad5b04"></a>

```c
#define MAX32_GPIO_WEAK_PULL_UP (1U << MAX32_GPIO_WEAK_PULL_UP_POS)
```

相关声明：[MAX32_GPIO_WEAK_PULL_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#gac3a2881b03a0e130c0dc174a7aad5b04)、[MAX32_GPIO_WEAK_PULL_UP_POS](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#gad20918791adf470f4421a2cbc1c7beaf)。

<a id="r_ga81dd2d4a0dbd87b5346c65e608f5ea45"></a>

```c
#define MAX32_GPIO_WEAK_PULL_DOWN_POS (12U)
```

相关声明：[MAX32_GPIO_WEAK_PULL_DOWN_POS](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#ga81dd2d4a0dbd87b5346c65e608f5ea45)。

GPIO 偏置弱下拉（weak pull-down）选择，下拉至 VDDIOH（1 MΩ）。

<a id="r_gaa2a5bc76ccfd583c11ee5f18015871be"></a>

```c
#define MAX32_GPIO_WEAK_PULL_DOWN (1U << MAX32_GPIO_WEAK_PULL_DOWN_POS)
```

相关声明：[MAX32_GPIO_WEAK_PULL_DOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#gaa2a5bc76ccfd583c11ee5f18015871be)、[MAX32_GPIO_WEAK_PULL_DOWN_POS](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#ga81dd2d4a0dbd87b5346c65e608f5ea45)。


## 1.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P006_adi-max32-gpio.h_源码浏览.md)
- [gpio_dt_flags_t](../hardware/P266_GPIO公共接口.md#gad435719dccdc37c05852960a7218fbd2)
- [MAX32_GPIO_VSEL_POS](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#ga267d4548e80843b5b5678d2050cbef73)
- [MAX32_GPIO_VSEL_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#ga57b502aa34453a1af1eb5103221c5bde)
- [MAX32_GPIO_VSEL_VDDIO](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#ga476d2376c91da2a1cf1bdfd0a7a95198)
- [MAX32_GPIO_VSEL_VDDIOH](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#ga964594ce9114dc57a9e50e416e948147)
- [MAX32_GPIO_DRV_STRENGTH_POS](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#ga8f42437e9d5cbc3bb2d9d58fee643bc5)
- [MAX32_GPIO_DRV_STRENGTH_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#gaefce80e7ae44c9f9397e3b4f02a59893)
- [MAX32_GPIO_DRV_STRENGTH_0](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#gaf783f2b803f4772b5bf4c83f616b8a8a)
- [MAX32_GPIO_DRV_STRENGTH_1](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#ga2e0abcd63dbbef23c2368be433c1909d)
- [MAX32_GPIO_DRV_STRENGTH_2](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#gae7199008d9e034361d80355651128fdd)
- [MAX32_GPIO_DRV_STRENGTH_3](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#gacf1c36bc17e552528ef20d4a8ae67f36)
- [MAX32_GPIO_WEAK_PULL_UP_POS](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#gad20918791adf470f4421a2cbc1c7beaf)
- [MAX32_GPIO_WEAK_PULL_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#gac3a2881b03a0e130c0dc174a7aad5b04)
- [MAX32_GPIO_WEAK_PULL_DOWN_POS](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#ga81dd2d4a0dbd87b5346c65e608f5ea45)
- [MAX32_GPIO_WEAK_PULL_DOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#gaa2a5bc76ccfd583c11ee5f18015871be)

---

[返回大纲](大纲.md) · [下一章](P002_zephyr__dt-bindings__sensor__adxl362.h_文件参考.md)
