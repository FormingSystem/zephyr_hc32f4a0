---
id: learning.zephyr-docs.api-file-signal-device-reference.page-9
title: zephyr__drivers__regulator__fake.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/fake_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_zephyr\_\_drivers\_\_regulator\_\_fake.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/fake_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

模拟稳压器（Fake Regulator）驱动的API函数。

<a id="details"></a>

```c
#include <zephyr/drivers/regulator.h>
#include <zephyr/fff.h>
```

查看此文件的源码。

模拟稳压器（Fake Regulator）驱动的API函数。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 9.1\_函数（Functions）

<a id="r_gae7b0b1f909b3bd6e82fdcd60436f2cb7"></a>

```c
int regulator_fake_enable (const struct device *)
```

相关声明：[regulator_fake_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#gae7b0b1f909b3bd6e82fdcd60436f2cb7)、[device](../device_reference/P002_设备对象结构.md)。

`regulator_driver_api::enable` 驱动操作（Driver Operation）的模拟实现（Fake Implementation）。

<a id="r_gaf60c59ae80d397943b589e89414f1af4"></a>

```c
int regulator_fake_disable (const struct device *)
```

相关声明：[regulator_fake_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#gaf60c59ae80d397943b589e89414f1af4)、[device](../device_reference/P002_设备对象结构.md)。

`regulator_driver_api::disable` 驱动操作（Driver Operation）的模拟实现（Fake Implementation）。

<a id="r_gaafc47ff2195727115be0e4e98f040611"></a>

```c
unsigned int regulator_fake_count_voltages (const struct device *)
```

相关声明：[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[regulator_fake_count_voltages](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#gaafc47ff2195727115be0e4e98f040611)、[device](../device_reference/P002_设备对象结构.md)。

`regulator_driver_api::count_voltages` 驱动操作（Driver Operation）的模拟实现（Fake Implementation）。

<a id="r_ga20e42c403dfbef4d77c6481c54b07a54"></a>

```c
int regulator_fake_list_voltage (const struct device *, unsigned int, int32_t *)
```

相关声明：[regulator_fake_list_voltage](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#ga20e42c403dfbef4d77c6481c54b07a54)、[device](../device_reference/P002_设备对象结构.md)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

`regulator_driver_api::list_voltage` 驱动操作（Driver Operation）的模拟实现（Fake Implementation）。

<a id="r_gaaf5093c4e28539c4ae5d253c90d1c7bb"></a>

```c
int regulator_fake_set_voltage (const struct device *, int32_t, int32_t)
```

相关声明：[regulator_fake_set_voltage](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#gaaf5093c4e28539c4ae5d253c90d1c7bb)、[device](../device_reference/P002_设备对象结构.md)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

`regulator_driver_api::set_voltage` 驱动操作（Driver Operation）的模拟实现（Fake Implementation）。

<a id="r_gab4d6cbe6fec13d6adc544c7695974e30"></a>

```c
int regulator_fake_get_voltage (const struct device *, int32_t *)
```

相关声明：[regulator_fake_get_voltage](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#gab4d6cbe6fec13d6adc544c7695974e30)、[device](../device_reference/P002_设备对象结构.md)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

`regulator_driver_api::get_voltage` 驱动操作（Driver Operation）的模拟实现（Fake Implementation）。

<a id="r_gacdb5dd0dde7c62c46dfeecc25e364821"></a>

```c
unsigned int regulator_fake_count_current_limits (const struct device *)
```

相关声明：[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[regulator_fake_count_current_limits](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#gacdb5dd0dde7c62c46dfeecc25e364821)、[device](../device_reference/P002_设备对象结构.md)。

`regulator_driver_api::count_current_limits` 驱动操作（Driver Operation）的模拟实现（Fake Implementation）。

<a id="r_ga46fa15902ea00714aa55339a6dfb0118"></a>

```c
int regulator_fake_list_current_limit (const struct device *, unsigned int, int32_t *)
```

相关声明：[regulator_fake_list_current_limit](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#ga46fa15902ea00714aa55339a6dfb0118)、[device](../device_reference/P002_设备对象结构.md)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

`regulator_driver_api::list_current_limit` 驱动操作（Driver Operation）的模拟实现（Fake Implementation）。

<a id="r_gaf76fea2e3aa81d36c102b2212e4f6f12"></a>

```c
int regulator_fake_set_current_limit (const struct device *, int32_t, int32_t)
```

相关声明：[regulator_fake_set_current_limit](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#gaf76fea2e3aa81d36c102b2212e4f6f12)、[device](../device_reference/P002_设备对象结构.md)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

`regulator_driver_api::set_current_limit` 驱动操作（Driver Operation）的模拟实现（Fake Implementation）。

<a id="r_gac06d00e3355efcc21ec639af071791de"></a>

```c
int regulator_fake_get_current_limit (const struct device *, int32_t *)
```

相关声明：[regulator_fake_get_current_limit](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#gac06d00e3355efcc21ec639af071791de)、[device](../device_reference/P002_设备对象结构.md)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

`regulator_driver_api::get_current_limit` 驱动操作（Driver Operation）的模拟实现（Fake Implementation）。

<a id="r_gadf5c7522be1d9654c9cbed62354d14f0"></a>

```c
int regulator_fake_set_mode (const struct device *, regulator_mode_t)
```

相关声明：[regulator_fake_set_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#gadf5c7522be1d9654c9cbed62354d14f0)、[device](../device_reference/P002_设备对象结构.md)、[regulator_mode_t](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface.html#ga1971bd21b504979a0cecab16048a0d03)。

`regulator_driver_api::set_mode` 驱动操作（Driver Operation）的模拟实现（Fake Implementation）。

<a id="r_ga440e1de9a526312b664ece361b69bb9c"></a>

```c
int regulator_fake_get_mode (const struct device *, regulator_mode_t *)
```

相关声明：[regulator_fake_get_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#ga440e1de9a526312b664ece361b69bb9c)、[device](../device_reference/P002_设备对象结构.md)、[regulator_mode_t](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface.html#ga1971bd21b504979a0cecab16048a0d03)。

`regulator_driver_api::get_mode` 驱动操作（Driver Operation）的模拟实现（Fake Implementation）。

<a id="r_ga48dff2682962072c8cd94ac86438e187"></a>

```c
int regulator_fake_set_active_discharge (const struct device *, bool)
```

相关声明：[regulator_fake_set_active_discharge](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#ga48dff2682962072c8cd94ac86438e187)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

`regulator_driver_api::set_active_discharge` 驱动操作（Driver Operation）的模拟实现（Fake Implementation）。

<a id="r_gad87508f8ea72f48f347dc417c212a3aa"></a>

```c
int regulator_fake_get_active_discharge (const struct device *, bool *)
```

相关声明：[regulator_fake_get_active_discharge](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#gad87508f8ea72f48f347dc417c212a3aa)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

`regulator_driver_api::get_active_discharge` 驱动操作（Driver Operation）的模拟实现（Fake Implementation）。

<a id="r_ga408d9f38ccfc124e37d493d7e28bc945"></a>

```c
int regulator_fake_get_error_flags (const struct device *, regulator_error_flags_t *)
```

相关声明：[regulator_fake_get_error_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#ga408d9f38ccfc124e37d493d7e28bc945)、[device](../device_reference/P002_设备对象结构.md)、[regulator_error_flags_t](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface.html#ga31dae130509d28ee41602ab16ab31a90)。

`regulator_driver_api::get_error_flags` 驱动操作（Driver Operation）的模拟实现（Fake Implementation）。

<a id="r_ga3698eca47d504ade69bdf83c701790a3"></a>

```c
int regulator_parent_fake_dvs_state_set (const struct device *, regulator_dvs_state_t)
```

相关声明：[regulator_parent_fake_dvs_state_set](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#ga3698eca47d504ade69bdf83c701790a3)、[device](../device_reference/P002_设备对象结构.md)、[regulator_dvs_state_t](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface.html#ga9a15a21a532e497713724f42052b1dbd)。

`regulator_parent_driver_api::dvs_state_set` 驱动操作（Driver Operation）的模拟实现（Fake Implementation）。

<a id="r_ga4cb6eb2be56aa8068ef2ae9535f10865"></a>

```c
int regulator_parent_fake_ship_mode (const struct device *)
```

相关声明：[regulator_parent_fake_ship_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#ga4cb6eb2be56aa8068ef2ae9535f10865)、[device](../device_reference/P002_设备对象结构.md)。

`regulator_parent_driver_api::ship_mode` 驱动操作（Driver Operation）的模拟实现（Fake Implementation）。


## 9.2\_原页交叉引用（Cross References）

- [zephyr/drivers/regulator.h](../api_source_reference/P701_regulator.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P253_fake.h_源码浏览.md)
- [regulator_fake_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#gae7b0b1f909b3bd6e82fdcd60436f2cb7)
- [device](../device_reference/P002_设备对象结构.md)
- [regulator_driver_api::enable](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__driver__api.html#a518274ecff0d8721a3b883bc344151e6)
- [regulator_fake_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#gaf60c59ae80d397943b589e89414f1af4)
- [regulator_driver_api::disable](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__driver__api.html#ace034f3b7b9fe74dbcbb5d9ead0497d0)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [regulator_fake_count_voltages](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#gaafc47ff2195727115be0e4e98f040611)
- [regulator_driver_api::count_voltages](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__driver__api.html#a7daeba7b79bc27d99bf30fb05ef056a0)
- [regulator_fake_list_voltage](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#ga20e42c403dfbef4d77c6481c54b07a54)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [regulator_driver_api::list_voltage](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__driver__api.html#a89613fef0b8adb6de371e8edc178442a)
- [regulator_fake_set_voltage](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#gaaf5093c4e28539c4ae5d253c90d1c7bb)
- [regulator_driver_api::set_voltage](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__driver__api.html#a67b1aeea6bfb4301972e87564a8656f6)
- [regulator_fake_get_voltage](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#gab4d6cbe6fec13d6adc544c7695974e30)
- [regulator_driver_api::get_voltage](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__driver__api.html#abb3f66fa87c23a9508e1b7f693c2fd97)
- [regulator_fake_count_current_limits](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#gacdb5dd0dde7c62c46dfeecc25e364821)
- [regulator_driver_api::count_current_limits](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__driver__api.html#afcc032c8173f75f789c65ccf517fdb28)
- [regulator_fake_list_current_limit](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#ga46fa15902ea00714aa55339a6dfb0118)
- [regulator_driver_api::list_current_limit](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__driver__api.html#a4e4cd7fef63c83a705941109e63b67d0)
- [regulator_fake_set_current_limit](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#gaf76fea2e3aa81d36c102b2212e4f6f12)
- [regulator_driver_api::set_current_limit](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__driver__api.html#a109db0dcdd1a68eaa134e721229e2056)
- [regulator_fake_get_current_limit](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#gac06d00e3355efcc21ec639af071791de)
- [regulator_driver_api::get_current_limit](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__driver__api.html#adcb93913bceff8c766355a7d79217597)
- [regulator_fake_set_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#gadf5c7522be1d9654c9cbed62354d14f0)
- [regulator_mode_t](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface.html#ga1971bd21b504979a0cecab16048a0d03)
- [regulator_driver_api::set_mode](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__driver__api.html#a98796a09c441bf201e333452de21662f)
- [regulator_fake_get_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#ga440e1de9a526312b664ece361b69bb9c)
- [regulator_driver_api::get_mode](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__driver__api.html#a9146d14c422bf5b6406b0e6b87b8df01)
- [regulator_fake_set_active_discharge](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#ga48dff2682962072c8cd94ac86438e187)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [regulator_driver_api::set_active_discharge](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__driver__api.html#a8a79e7f2e12e0b4d2da3511367f8aa30)
- [regulator_fake_get_active_discharge](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#gad87508f8ea72f48f347dc417c212a3aa)
- [regulator_driver_api::get_active_discharge](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__driver__api.html#a9b696b7edb797460b7b3de1e9319c4e3)
- [regulator_fake_get_error_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#ga408d9f38ccfc124e37d493d7e28bc945)
- [regulator_error_flags_t](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface.html#ga31dae130509d28ee41602ab16ab31a90)
- [regulator_driver_api::get_error_flags](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__driver__api.html#a85efb04e9271af38d8ed23a83202fccc)
- [regulator_parent_fake_dvs_state_set](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#ga3698eca47d504ade69bdf83c701790a3)
- [regulator_dvs_state_t](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface.html#ga9a15a21a532e497713724f42052b1dbd)
- [regulator_parent_driver_api::dvs_state_set](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__parent__driver__api.html#a52f314a95ce64485240b1d3cc46dac05)
- [regulator_parent_fake_ship_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__fake.html#ga4cb6eb2be56aa8068ef2ae9535f10865)
- [regulator_parent_driver_api::ship_mode](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__parent__driver__api.html#aa0d54ca393956b0c6213217c678308a4)

<a id="header-details"></a>

---

[上一章](P008_zephyr__drivers__edac.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P010_zephyr__net__http__frame.h_文件参考.md)
