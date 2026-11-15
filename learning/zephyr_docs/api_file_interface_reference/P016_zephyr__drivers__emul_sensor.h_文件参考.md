---
id: learning.zephyr-docs.api-file-interface-reference.page-16
title: zephyr__drivers__emul_sensor.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/emul__sensor_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_zephyr\_\_drivers\_\_emul\_sensor.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/emul__sensor_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

传感器仿真器（Sensor Emulators）的后端API。

<a id="details"></a>

```c
#include <zephyr/drivers/emul.h>
#include <zephyr/drivers/sensor.h>
#include <zephyr/drivers/sensor_attribute_types.h>
#include <stdint.h>
```

查看此文件的源码。

传感器仿真器（Sensor Emulators）的后端API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 16.1\_函数（Functions）

<a id="r_gadb7174783ab8466ab55aebb463fdfdd7"></a>

```c
static bool emul_sensor_backend_is_supported (const struct emul *target)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[emul_sensor_backend_is_supported](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__emulator__backend.html#gadb7174783ab8466ab55aebb463fdfdd7)、[emul](../hardware/P477_仿真器实例结构.md)。

检查指定传感器仿真器（sensor emulator）是否支持后端 API（backend API）。

<a id="r_gadfa5c6618361bb382e5b44dc1a03f735"></a>

```c
static int emul_sensor_backend_set_channel (const struct emul *target, struct sensor_chan_spec ch, const q31_t *value, int8_t shift)
```

相关声明：[emul_sensor_backend_set_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__emulator__backend.html#gadfa5c6618361bb382e5b44dc1a03f735)、[emul](../hardware/P477_仿真器实例结构.md)、[sensor_chan_spec](../sensor_navigation_model_reference/P035_sensor_chan_spec_结构体.md)、[q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)。

为指定传感器仿真器的指定通道设置期望值（expected value）。

<a id="r_ga271513cf5b2b5ee28d5f37e42449ee1e"></a>

```c
static int emul_sensor_backend_get_sample_range (const struct emul *target, struct sensor_chan_spec ch, q31_t *lower, q31_t *upper, q31_t *epsilon, int8_t *shift)
```

相关声明：[emul_sensor_backend_get_sample_range](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__emulator__backend.html#ga271513cf5b2b5ee28d5f37e42449ee1e)、[emul](../hardware/P477_仿真器实例结构.md)、[sensor_chan_spec](../sensor_navigation_model_reference/P035_sensor_chan_spec_结构体.md)、[q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)、[q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)、[q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)。

查询仿真器某通道所支持的样本值范围（sample value range）及容差（tolerance）。

<a id="r_gaec1ddd02bc6ff1c66c83ca3f3af98fa8"></a>

```c
static int emul_sensor_backend_set_attribute (const struct emul *target, struct sensor_chan_spec ch, enum sensor_attribute attribute, const void *value)
```

相关声明：[emul_sensor_backend_set_attribute](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__emulator__backend.html#gaec1ddd02bc6ff1c66c83ca3f3af98fa8)、[emul](../hardware/P477_仿真器实例结构.md)、[sensor_chan_spec](../sensor_navigation_model_reference/P035_sensor_chan_spec_结构体.md)、[sensor_attribute](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga0dcb6842bc969492bd1c9eb49708940b)。

设置仿真器的属性值（attribute values）。

<a id="r_ga3bf83e34c2218823386489cf4f1cd84c"></a>

```c
static int emul_sensor_backend_get_attribute_metadata (const struct emul *target, struct sensor_chan_spec ch, enum sensor_attribute attribute, q31_t *min, q31_t *max, q31_t *increment, int8_t *shift)
```

相关声明：[emul_sensor_backend_get_attribute_metadata](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__emulator__backend.html#ga3bf83e34c2218823386489cf4f1cd84c)、[emul](../hardware/P477_仿真器实例结构.md)、[sensor_chan_spec](../sensor_navigation_model_reference/P035_sensor_chan_spec_结构体.md)、[sensor_attribute](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga0dcb6842bc969492bd1c9eb49708940b)、[q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)、[min](../numeric_reference/P001_最小最大值与限幅宏参考.md#ac6afabdc09a49a433ee19d8a9486056d)、[q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)、[max](../numeric_reference/P001_最小最大值与限幅宏参考.md#affe776513b24d84b39af8ab0930fef7f)、[q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)。

获取属性的元数据（metadata）。


## 16.2\_原页交叉引用（Cross References）

- [zephyr/drivers/emul.h](../api_source_runtime_reference/P013_emul.h_源码浏览.md)
- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h_source.html)
- [zephyr/drivers/sensor_attribute_types.h](../api_source_reference/P765_sensor_attribute_types.h_源码浏览.md)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P226_emul_sensor.h_源码浏览.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [emul_sensor_backend_is_supported](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__emulator__backend.html#gadb7174783ab8466ab55aebb463fdfdd7)
- [emul](../hardware/P477_仿真器实例结构.md)
- [emul_sensor_backend_set_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__emulator__backend.html#gadfa5c6618361bb382e5b44dc1a03f735)
- [sensor_chan_spec](../sensor_navigation_model_reference/P035_sensor_chan_spec_结构体.md)
- [q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)
- [int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)
- [emul_sensor_backend_get_sample_range](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__emulator__backend.html#ga271513cf5b2b5ee28d5f37e42449ee1e)
- [emul_sensor_backend_set_attribute](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__emulator__backend.html#gaec1ddd02bc6ff1c66c83ca3f3af98fa8)
- [sensor_attribute](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga0dcb6842bc969492bd1c9eb49708940b)
- [emul_sensor_backend_get_attribute_metadata](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__emulator__backend.html#ga3bf83e34c2218823386489cf4f1cd84c)
- [min](../numeric_reference/P001_最小最大值与限幅宏参考.md#ac6afabdc09a49a433ee19d8a9486056d)
- [max](../numeric_reference/P001_最小最大值与限幅宏参考.md#affe776513b24d84b39af8ab0930fef7f)

<a id="header-details"></a>

---

[上一章](P015_zephyr__drivers__console__console.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P017_zephyr__mgmt__mcumgr__grp__enum_mgmt__enum_mgmt.h_文件参考.md)
