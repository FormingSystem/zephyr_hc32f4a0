---
id: learning.zephyr-docs.api-file-management-reference.page-9
title: zephyr__drivers__biometrics__emul.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2biometrics_2emul_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_zephyr\_\_drivers\_\_biometrics\_\_emul.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2biometrics_2emul_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

生物识别仿真器（Biometrics Emulator）的测试辅助API。

<a id="details"></a>

```c
#include <stdbool.h>
#include <zephyr/drivers/biometrics.h>
#include <zephyr/device.h>
```

查看此文件的源码。

生物识别仿真器（Biometrics Emulator）的测试辅助API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 9.1\_函数（Functions）

<a id="r_gac3678eaa27b193eb1a50458a657bb79c"></a>

```c
void biometrics_emul_set_match_score (const struct device *dev, int score)
```

相关声明：[biometrics_emul_set_match_score](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__emulator.html#gac3678eaa27b193eb1a50458a657bb79c)、[device](../device_reference/P002_设备对象结构.md)。

设置生物特征识别仿真器（biometrics emulator）的匹配分数（match score）。

<a id="r_gac7f189217091ebabf3c797edc8510f79"></a>

```c
void biometrics_emul_set_match_id (const struct device *dev, int id)
```

相关声明：[biometrics_emul_set_match_id](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__emulator.html#gac7f189217091ebabf3c797edc8510f79)、[device](../device_reference/P002_设备对象结构.md)。

设置身份识别匹配所用的模板标识符（template ID）。

<a id="r_ga1d019c8b87edc683164eb4fe50dbcecd"></a>

```c
void biometrics_emul_set_match_fail (const struct device *dev, bool fail)
```

相关声明：[biometrics_emul_set_match_fail](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__emulator.html#ga1d019c8b87edc683164eb4fe50dbcecd)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置匹配操作（match operations）是否应失败。

<a id="r_ga5263531d01ea35ffbc8c7f012f508ab0"></a>

```c
void biometrics_emul_set_capture_timeout (const struct device *dev, bool timeout)
```

相关声明：[biometrics_emul_set_capture_timeout](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__emulator.html#ga5263531d01ea35ffbc8c7f012f508ab0)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置采集操作（capture operations）是否应超时。

<a id="r_gac4373b9736267d218e54373fe5a170e7"></a>

```c
void biometrics_emul_set_image_quality (const struct device *dev, int quality)
```

相关声明：[biometrics_emul_set_image_quality](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__emulator.html#gac4373b9736267d218e54373fe5a170e7)、[device](../device_reference/P002_设备对象结构.md)。

设置图像质量分数（image quality score）。

<a id="r_ga93a3ca46b71f86b6a61078fb0377f684"></a>

```c
enum biometric_led_state biometrics_emul_get_led_state (const struct device *dev)
```

相关声明：[biometric_led_state](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga83c3fbd41de6c4f3739880fceadea96f)、[biometrics_emul_get_led_state](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__emulator.html#ga93a3ca46b71f86b6a61078fb0377f684)、[device](../device_reference/P002_设备对象结构.md)。

获取当前 LED 状态。


## 9.2\_原页交叉引用（Cross References）

- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [zephyr/drivers/biometrics.h](../api_source_reference/P066_biometrics.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P147_emul.h_源码浏览.md)
- [biometrics_emul_set_match_score](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__emulator.html#gac3678eaa27b193eb1a50458a657bb79c)
- [device](../device_reference/P002_设备对象结构.md)
- [biometrics_emul_set_match_id](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__emulator.html#gac7f189217091ebabf3c797edc8510f79)
- [biometrics_emul_set_match_fail](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__emulator.html#ga1d019c8b87edc683164eb4fe50dbcecd)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [biometrics_emul_set_capture_timeout](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__emulator.html#ga5263531d01ea35ffbc8c7f012f508ab0)
- [biometrics_emul_set_image_quality](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__emulator.html#gac4373b9736267d218e54373fe5a170e7)
- [biometric_led_state](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga83c3fbd41de6c4f3739880fceadea96f)
- [biometrics_emul_get_led_state](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__emulator.html#ga93a3ca46b71f86b6a61078fb0377f684)

<a id="header-details"></a>

---

[上一章](P008_zephyr__gnss__rtk__decoder.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P010_zephyr__drivers__mfd__npm2100.h_文件参考.md)
