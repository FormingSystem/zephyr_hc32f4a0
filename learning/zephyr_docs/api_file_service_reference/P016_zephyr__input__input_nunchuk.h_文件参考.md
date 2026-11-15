---
id: learning.zephyr-docs.api-file-service-reference.page-16
title: zephyr__input__input_nunchuk.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/input__nunchuk_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_zephyr\_\_input\_\_input\_nunchuk.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/input__nunchuk_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Nunchuk输入驱动同步读取（Synchronous Reading）的头文件。

<a id="details"></a>

```c
#include <zephyr/device.h>
```

查看此文件的源码。

Nunchuk输入驱动同步读取（Synchronous Reading）的头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 16.1\_宏定义（Macros）

<a id="r_gad05cb505dd3599859f7bdee239d11150"></a>

```c
#define INPUT_NUNCHUK_ACCEL_X 0
```

相关声明：[INPUT_NUNCHUK_ACCEL_X](https://docs.zephyrproject.org/latest/doxygen/html/group__nunchuk__interface.html#gad05cb505dd3599859f7bdee239d11150)。

Nunchuk 报告的 X 轴加速度（Acceleration）。

<a id="r_gae057e51e128873212a8d368db80128c8"></a>

```c
#define INPUT_NUNCHUK_ACCEL_Y 1
```

相关声明：[INPUT_NUNCHUK_ACCEL_Y](https://docs.zephyrproject.org/latest/doxygen/html/group__nunchuk__interface.html#gae057e51e128873212a8d368db80128c8)。

Nunchuk 报告的 Y 轴加速度（Acceleration）。

<a id="r_ga73c30a58e1819ab501aa6c31a9a76c7c"></a>

```c
#define INPUT_NUNCHUK_ACCEL_Z 2
```

相关声明：[INPUT_NUNCHUK_ACCEL_Z](https://docs.zephyrproject.org/latest/doxygen/html/group__nunchuk__interface.html#ga73c30a58e1819ab501aa6c31a9a76c7c)。

Nunchuk 报告的 Z 轴加速度（Acceleration）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 16.2\_函数（Functions）

<a id="r_ga481650458998947e79ee89fbf1402435"></a>

```c
int nunchuk_read (const struct device *dev)
```

相关声明：[nunchuk_read](https://docs.zephyrproject.org/latest/doxygen/html/group__nunchuk__interface.html#ga481650458998947e79ee89fbf1402435)、[device](../device_reference/P002_设备对象结构.md)。

开始从 Nunchuk 读取当前按键状态（Button States）、摇杆位置（Joystick Position），以及可选的加速度（Acceleration）；加速度读取需要启用 `CONFIG_INPUT_NUNCHUK_ACCELERATION`。


## 16.3\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P382_input_nunchuk.h_源码浏览.md)
- [INPUT_NUNCHUK_ACCEL_X](https://docs.zephyrproject.org/latest/doxygen/html/group__nunchuk__interface.html#gad05cb505dd3599859f7bdee239d11150)
- [INPUT_NUNCHUK_ACCEL_Y](https://docs.zephyrproject.org/latest/doxygen/html/group__nunchuk__interface.html#gae057e51e128873212a8d368db80128c8)
- [INPUT_NUNCHUK_ACCEL_Z](https://docs.zephyrproject.org/latest/doxygen/html/group__nunchuk__interface.html#ga73c30a58e1819ab501aa6c31a9a76c7c)
- [nunchuk_read](https://docs.zephyrproject.org/latest/doxygen/html/group__nunchuk__interface.html#ga481650458998947e79ee89fbf1402435)
- [device](../device_reference/P002_设备对象结构.md)

<a id="header-details"></a>

---

[上一章](P015_zephyr__bluetooth__services__hrs.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P017_zephyr__llext__inspect.h_文件参考.md)
