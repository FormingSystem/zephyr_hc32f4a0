---
id: learning.zephyr-docs.api-file-network-device-reference.page-1
title: zephyr__drivers__bbram.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/bbram_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_zephyr\_\_drivers\_\_bbram.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/bbram_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

电池备份RAM（Battery-Backed RAM，BBRAM）驱动API的主头文件。

<a id="details"></a>

```c
#include <errno.h>
#include <zephyr/device.h>
#include <zephyr/syscalls/bbram.h>
```

查看此文件的源码。

电池备份RAM（Battery-Backed RAM，BBRAM）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.1\_数据结构（Data Structures）

<a id="r_bbram_5Fdriver_5Fapi"></a>

```c
struct bbram_driver_api
```

相关声明：[bbram_driver_api](../driver_model_reference/P024_电池备份RAM驱动接口.md)。

驱动操作（Driver Operations）：电池备份 RAM（Battery-backed RAM，BBRAM）驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 1.2\_类型定义（Typedefs）

<a id="r_gac23658302662587043f3587080f798fe"></a>

```c
typedef int(* bbram_api_check_invalid_t) (const struct device *dev)
```

相关声明：[bbram_api_check_invalid_t](../api_auxiliary_topic_reference/P001_BBRAM 驱动后端 API（Driver Backend API）.md#gac23658302662587043f3587080f798fe)、[device](../device_reference/P002_设备对象结构.md)。

用于检查 BBRAM 是否无效的回调 API。参数说明参见 `bbram_check_invalid()`。

<a id="r_ga99adefcb89ab80d8b5e24b8ffad8f43e"></a>

```c
typedef int(* bbram_api_check_standby_power_t) (const struct device *dev)
```

相关声明：[bbram_api_check_standby_power_t](../api_auxiliary_topic_reference/P001_BBRAM 驱动后端 API（Driver Backend API）.md#ga99adefcb89ab80d8b5e24b8ffad8f43e)、[device](../device_reference/P002_设备对象结构.md)。

用于检查待机电源故障（standby power failure）的回调 API。参数说明参见 `bbram_check_standby_power()`。

<a id="r_gaa6edc8a61529edad90de2e6fff619fdf"></a>

```c
typedef int(* bbram_api_check_power_t) (const struct device *dev)
```

相关声明：[bbram_api_check_power_t](../api_auxiliary_topic_reference/P001_BBRAM 驱动后端 API（Driver Backend API）.md#gaa6edc8a61529edad90de2e6fff619fdf)、[device](../device_reference/P002_设备对象结构.md)。

用于检查 VCC1 电源故障的回调 API。参数说明参见 `bbram_check_power()`。

<a id="r_gacfa586f705c520a6a05638a2e289fe50"></a>

```c
typedef int(* bbram_api_get_size_t) (const struct device *dev, size_t *size)
```

相关声明：[bbram_api_get_size_t](../api_auxiliary_topic_reference/P001_BBRAM 驱动后端 API（Driver Backend API）.md#gacfa586f705c520a6a05638a2e289fe50)、[device](../device_reference/P002_设备对象结构.md)。

用于获取 BBRAM 大小的回调 API。参数说明参见 `bbram_get_size()`。

<a id="r_ga8b06a1b3bb9b524597804dd268904881"></a>

```c
typedef int(* bbram_api_read_t) (const struct device *dev, size_t offset, size_t size, uint8_t *data)
```

相关声明：[bbram_api_read_t](../api_auxiliary_topic_reference/P001_BBRAM 驱动后端 API（Driver Backend API）.md#ga8b06a1b3bb9b524597804dd268904881)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

用于从 BBRAM 读取数据的回调 API。参数说明参见 `bbram_read()`。

<a id="r_ga1b111ae421791b9544777c1bab5e2a02"></a>

```c
typedef int(* bbram_api_write_t) (const struct device *dev, size_t offset, size_t size, const uint8_t *data)
```

相关声明：[bbram_api_write_t](../api_auxiliary_topic_reference/P001_BBRAM 驱动后端 API（Driver Backend API）.md#ga1b111ae421791b9544777c1bab5e2a02)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

用于向 BBRAM 写入数据的回调 API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.3\_函数（Functions）

<a id="r_ga7164969f308616696a9ab71a4d19b70b"></a>

```c
int bbram_check_invalid (const struct device *dev)
```

相关声明：[bbram_check_invalid](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface.html#ga7164969f308616696a9ab71a4d19b70b)、[device](../device_reference/P002_设备对象结构.md)。

检查电池备份 RAM（BBRAM）是否无效。

<a id="r_ga948ed0a7d3824f950ad46b99ba3d86f4"></a>

```c
int bbram_check_standby_power (const struct device *dev)
```

相关声明：[bbram_check_standby_power](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface.html#ga948ed0a7d3824f950ad46b99ba3d86f4)、[device](../device_reference/P002_设备对象结构.md)。

检查待机（Volt SBY）电源是否发生故障。

<a id="r_ga8fc2a647bda90e96f866514300180a96"></a>

```c
int bbram_check_power (const struct device *dev)
```

相关声明：[bbram_check_power](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface.html#ga8fc2a647bda90e96f866514300180a96)、[device](../device_reference/P002_设备对象结构.md)。

检查 V CC1 电源是否发生故障。

<a id="r_gab6bdb4a1cba88ca645c256366a696bdd"></a>

```c
int bbram_get_size (const struct device *dev, size_t *size)
```

相关声明：[bbram_get_size](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface.html#gab6bdb4a1cba88ca645c256366a696bdd)、[device](../device_reference/P002_设备对象结构.md)。

获取电池备份 RAM（BBRAM）的大小，单位为字节。

<a id="r_ga9ef786b0fbac3f8523be2bb87b7cff7b"></a>

```c
int bbram_read (const struct device *dev, size_t offset, size_t size, uint8_t *data)
```

相关声明：[bbram_read](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface.html#ga9ef786b0fbac3f8523be2bb87b7cff7b)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从电池备份 RAM（BBRAM）读取字节。

<a id="r_ga51007eed4820aed341d20e4562607564"></a>

```c
int bbram_write (const struct device *dev, size_t offset, size_t size, const uint8_t *data)
```

相关声明：[bbram_write](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface.html#ga51007eed4820aed341d20e4562607564)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向电池备份 RAM（BBRAM）写入字节。

<a id="r_gae2b89f8a44e38fe7df2219397bad139b"></a>

```c
int bbram_emul_set_invalid (const struct device *dev, bool is_invalid)
```

相关声明：[bbram_emul_set_invalid](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface.html#gae2b89f8a44e38fe7df2219397bad139b)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置仿真 BBRAM 驱动的无效状态（Invalid State）。

<a id="r_ga08a2c565ba0ec6ac5894a718a652eec2"></a>

```c
int bbram_emul_set_standby_power_state (const struct device *dev, bool failure)
```

相关声明：[bbram_emul_set_standby_power_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface.html#ga08a2c565ba0ec6ac5894a718a652eec2)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置仿真 BBRAM 驱动的待机电源状态（Standby Power State）。

<a id="r_gadc0243187b853832b08af36c9baf9cb0"></a>

```c
int bbram_emul_set_power_state (const struct device *dev, bool failure)
```

相关声明：[bbram_emul_set_power_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface.html#gadc0243187b853832b08af36c9baf9cb0)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置仿真 BBRAM 驱动的电源状态（Power State）。


## 1.4\_原页交叉引用（Cross References）

- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P055_bbram.h_源码浏览.md)
- [bbram_driver_api](../driver_model_reference/P024_电池备份RAM驱动接口.md)
- [bbram_api_check_invalid_t](../api_auxiliary_topic_reference/P001_BBRAM 驱动后端 API（Driver Backend API）.md#gac23658302662587043f3587080f798fe)
- [device](../device_reference/P002_设备对象结构.md)
- [bbram_check_invalid()](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface.html#ga7164969f308616696a9ab71a4d19b70b)
- [bbram_api_check_standby_power_t](../api_auxiliary_topic_reference/P001_BBRAM 驱动后端 API（Driver Backend API）.md#ga99adefcb89ab80d8b5e24b8ffad8f43e)
- [bbram_check_standby_power()](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface.html#ga948ed0a7d3824f950ad46b99ba3d86f4)
- [bbram_api_check_power_t](../api_auxiliary_topic_reference/P001_BBRAM 驱动后端 API（Driver Backend API）.md#gaa6edc8a61529edad90de2e6fff619fdf)
- [bbram_check_power()](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface.html#ga8fc2a647bda90e96f866514300180a96)
- [bbram_api_get_size_t](../api_auxiliary_topic_reference/P001_BBRAM 驱动后端 API（Driver Backend API）.md#gacfa586f705c520a6a05638a2e289fe50)
- [bbram_get_size()](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface.html#gab6bdb4a1cba88ca645c256366a696bdd)
- [bbram_api_read_t](../api_auxiliary_topic_reference/P001_BBRAM 驱动后端 API（Driver Backend API）.md#ga8b06a1b3bb9b524597804dd268904881)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bbram_read()](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface.html#ga9ef786b0fbac3f8523be2bb87b7cff7b)
- [bbram_api_write_t](../api_auxiliary_topic_reference/P001_BBRAM 驱动后端 API（Driver Backend API）.md#ga1b111ae421791b9544777c1bab5e2a02)
- [bbram_write](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface.html#ga51007eed4820aed341d20e4562607564)
- [bbram_emul_set_invalid](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface.html#gae2b89f8a44e38fe7df2219397bad139b)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bbram_emul_set_standby_power_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface.html#ga08a2c565ba0ec6ac5894a718a652eec2)
- [bbram_emul_set_power_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface.html#gadc0243187b853832b08af36c9baf9cb0)

<a id="header-details"></a>

---

[返回大纲](大纲.md) · [下一章](P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md)
