---
id: learning.zephyr-docs.api-file-network-device-reference.page-3
title: zephyr__drivers__buzzer.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/buzzer_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_zephyr\_\_drivers\_\_buzzer.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/buzzer_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蜂鸣器（Buzzer）驱动API的主头文件。

<a id="details"></a>

```c
#include <errno.h>
#include <stdint.h>
#include <zephyr/device.h>
```

查看此文件的源码。

蜂鸣器（Buzzer）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 3.1\_数据结构（Data Structures）

<a id="r_buzzer_5Fdriver_5Fapi"></a>

```c
struct buzzer_driver_api
```

相关声明：[buzzer_driver_api](../hardware/P146_蜂鸣器驱动操作表.md)。

驱动操作（Driver Operations）：蜂鸣器（Buzzer）驱动操作。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.2\_宏定义（Macros）

<a id="r_ga8f59503d35269e3535cafeb5140f2ed9"></a>

```c
#define BUZZER_FREQ_REST 0U
```

相关声明：[BUZZER_FREQ_REST](https://docs.zephyrproject.org/latest/doxygen/html/group__buzzer__interface.html#ga8f59503d35269e3535cafeb5140f2ed9)。

表示静音（Silence）的特殊频率值。

<a id="r_ga536d8f9b36f89636ab3e1ce090ce9de4"></a>

```c
#define BUZZER_VOLUME_MAX 100U
```

相关声明：[BUZZER_VOLUME_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__buzzer__interface.html#ga536d8f9b36f89636ab3e1ce090ce9de4)。

最大音量级别（Volume Level），范围为 0 到 `BUZZER_VOLUME_MAX`。

<a id="r_ga7a6fa0c0251b4b673cf89b019ddad9c2"></a>

```c
#define BUZZER_DURATION_FOREVER UINT32_MAX
```

相关声明：[BUZZER_DURATION_FOREVER](https://docs.zephyrproject.org/latest/doxygen/html/group__buzzer__interface.html#ga7a6fa0c0251b4b673cf89b019ddad9c2)、[UINT32_MAX](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ab5eb23180f7cc12b7d6c04a8ec067fdd)。

表示“持续播放直到显式停止”的特殊时长（Duration）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 3.3\_类型定义（Typedefs）

<a id="r_gac6ae53a4674a3c1ca96a7e41735f9ff3"></a>

```c
typedef int(* buzzer_tone_t) (const struct device *dev, uint32_t freq_hz, uint32_t duration_ms)
```

相关声明：[buzzer_tone_t](https://docs.zephyrproject.org/latest/doxygen/html/group__buzzer__interface__backend.html#gac6ae53a4674a3c1ca96a7e41735f9ff3)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

在指定时长内播放单音（Single Tone）。

<a id="r_ga19d504c3b6dc816706d5cdd9dec37e3f"></a>

```c
typedef int(* buzzer_set_volume_t) (const struct device *dev, uint8_t percent)
```

相关声明：[buzzer_set_volume_t](https://docs.zephyrproject.org/latest/doxygen/html/group__buzzer__interface__backend.html#ga19d504c3b6dc816706d5cdd9dec37e3f)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置蜂鸣器音量（Buzzer Volume）。

<a id="r_gae36ee5133f2877ee6bd119214744b362"></a>

```c
typedef int(* buzzer_beep_t) (const struct device *dev, uint32_t duration_ms)
```

相关声明：[buzzer_beep_t](https://docs.zephyrproject.org/latest/doxygen/html/group__buzzer__interface__backend.html#gae36ee5133f2877ee6bd119214744b362)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

播放蜂鸣器的默认音调（Default Tone）。

<a id="r_gad6e97a02e02eaf1f127203a856018cf3"></a>

```c
typedef int(* buzzer_stop_t) (const struct device *dev)
```

相关声明：[buzzer_stop_t](https://docs.zephyrproject.org/latest/doxygen/html/group__buzzer__interface__backend.html#gad6e97a02e02eaf1f127203a856018cf3)、[device](../device_reference/P002_设备对象结构.md)。

停止当前正在播放的任何音调（Tone）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 3.4\_函数（Functions）

<a id="r_ga11d8fa4f540452ee487164a4af200868"></a>

```c
static int buzzer_tone (const struct device *dev, uint32_t freq_hz, uint32_t duration_ms)
```

相关声明：[buzzer_tone](https://docs.zephyrproject.org/latest/doxygen/html/group__buzzer__interface.html#ga11d8fa4f540452ee487164a4af200868)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

以 `freq_hz` 频率播放单音，持续 `duration_ms`。

<a id="r_ga6ad479424be12d83cab59656cf94cde0"></a>

```c
static int buzzer_set_volume (const struct device *dev, uint8_t percent)
```

相关声明：[buzzer_set_volume](https://docs.zephyrproject.org/latest/doxygen/html/group__buzzer__interface.html#ga6ad479424be12d83cab59656cf94cde0)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置蜂鸣器音量（Buzzer Volume）。

<a id="r_gad22c8c78d97814b849d87e42b1363ea9"></a>

```c
static int buzzer_beep (const struct device *dev, uint32_t duration_ms)
```

相关声明：[buzzer_beep](https://docs.zephyrproject.org/latest/doxygen/html/group__buzzer__interface.html#gad22c8c78d97814b849d87e42b1363ea9)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

播放蜂鸣器的默认音调，持续 `duration_ms`。

<a id="r_ga8990f4ef56d763b59a59e9fc69782106"></a>

```c
static int buzzer_stop (const struct device *dev)
```

相关声明：[buzzer_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__buzzer__interface.html#ga8990f4ef56d763b59a59e9fc69782106)、[device](../device_reference/P002_设备对象结构.md)。

停止当前正在播放的任何音调（Tone）。


## 3.5\_原页交叉引用（Cross References）

- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P081_buzzer.h_源码浏览.md)
- [buzzer_driver_api](../hardware/P146_蜂鸣器驱动操作表.md)
- [BUZZER_FREQ_REST](https://docs.zephyrproject.org/latest/doxygen/html/group__buzzer__interface.html#ga8f59503d35269e3535cafeb5140f2ed9)
- [BUZZER_VOLUME_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__buzzer__interface.html#ga536d8f9b36f89636ab3e1ce090ce9de4)
- [BUZZER_DURATION_FOREVER](https://docs.zephyrproject.org/latest/doxygen/html/group__buzzer__interface.html#ga7a6fa0c0251b4b673cf89b019ddad9c2)
- [UINT32_MAX](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ab5eb23180f7cc12b7d6c04a8ec067fdd)
- [buzzer_tone_t](https://docs.zephyrproject.org/latest/doxygen/html/group__buzzer__interface__backend.html#gac6ae53a4674a3c1ca96a7e41735f9ff3)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [buzzer_set_volume_t](https://docs.zephyrproject.org/latest/doxygen/html/group__buzzer__interface__backend.html#ga19d504c3b6dc816706d5cdd9dec37e3f)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [buzzer_beep_t](https://docs.zephyrproject.org/latest/doxygen/html/group__buzzer__interface__backend.html#gae36ee5133f2877ee6bd119214744b362)
- [buzzer_stop_t](https://docs.zephyrproject.org/latest/doxygen/html/group__buzzer__interface__backend.html#gad6e97a02e02eaf1f127203a856018cf3)
- [buzzer_tone](https://docs.zephyrproject.org/latest/doxygen/html/group__buzzer__interface.html#ga11d8fa4f540452ee487164a4af200868)
- [buzzer_set_volume](https://docs.zephyrproject.org/latest/doxygen/html/group__buzzer__interface.html#ga6ad479424be12d83cab59656cf94cde0)
- [buzzer_beep](https://docs.zephyrproject.org/latest/doxygen/html/group__buzzer__interface.html#gad22c8c78d97814b849d87e42b1363ea9)
- [buzzer_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__buzzer__interface.html#ga8990f4ef56d763b59a59e9fc69782106)

<a id="header-details"></a>

---

[上一章](P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P004_zephyr__net__conn_mgr_connectivity_impl.h_文件参考.md)
