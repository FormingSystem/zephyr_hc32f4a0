---
id: learning.zephyr-docs.api-protocol-topic-reference.page-42
title: Nunchuk API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__nunchuk__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第42章\_Nunchuk API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__nunchuk__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

任天堂 Nunchuk 操纵杆（Nintendo Nunchuk joystick）。

<a id="details"></a>

任天堂 Nunchuk 操纵杆（Nintendo Nunchuk joystick）。

<a id="header-files"></a>
<a id="files"></a>

## 42.1\_文件（Files）

<a id="r_input_5Fnunchuk_2Eh"></a>

```c
file input_nunchuk.h
```

相关声明：[input_nunchuk.h](../api_file_service_reference/P016_zephyr__input__input_nunchuk.h_文件参考.md)。

Nunchuk输入驱动同步读取（Synchronous Reading）的头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 42.2\_宏定义（Macros）

<a id="r_gad05cb505dd3599859f7bdee239d11150"></a>

```c
#define INPUT_NUNCHUK_ACCEL_X 0
```

相关声明：[INPUT_NUNCHUK_ACCEL_X](#gad05cb505dd3599859f7bdee239d11150)。

Nunchuk 报告的 X 轴加速度（Acceleration）。

<a id="r_gae057e51e128873212a8d368db80128c8"></a>

```c
#define INPUT_NUNCHUK_ACCEL_Y 1
```

相关声明：[INPUT_NUNCHUK_ACCEL_Y](#gae057e51e128873212a8d368db80128c8)。

Nunchuk 报告的 Y 轴加速度（Acceleration）。

<a id="r_ga73c30a58e1819ab501aa6c31a9a76c7c"></a>

```c
#define INPUT_NUNCHUK_ACCEL_Z 2
```

相关声明：[INPUT_NUNCHUK_ACCEL_Z](#ga73c30a58e1819ab501aa6c31a9a76c7c)。

Nunchuk 报告的 Z 轴加速度（Acceleration）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 42.3\_函数（Functions）

<a id="r_ga481650458998947e79ee89fbf1402435"></a>

```c
int nunchuk_read (const struct device *dev)
```

相关声明：[nunchuk_read](#ga481650458998947e79ee89fbf1402435)、[device](../device_reference/P002_设备对象结构.md)。

开始从 Nunchuk 读取当前按键状态（Button States）、摇杆位置（Joystick Position），以及可选的加速度（Acceleration）；加速度读取需要启用 `CONFIG_INPUT_NUNCHUK_ACCELERATION`。

## 42.4\_详细说明（Detailed Documentation）

<a id="gad05cb505dd3599859f7bdee239d11150"></a>

### `INPUT_NUNCHUK_ACCEL_X`

```c
#define INPUT_NUNCHUK_ACCEL_X 0
```

```c
#include <zephyr/input/input_nunchuk.h>
```

Nunchuk 报告的 X 轴加速度（Acceleration）。

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_INPUT_NUNCHUK_ACCELERATION` 时可用。

<a id="gae057e51e128873212a8d368db80128c8"></a>

### `INPUT_NUNCHUK_ACCEL_Y`

```c
#define INPUT_NUNCHUK_ACCEL_Y 1
```

```c
#include <zephyr/input/input_nunchuk.h>
```

Nunchuk 报告的 Y 轴加速度（Acceleration）。

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_INPUT_NUNCHUK_ACCELERATION` 时可用。

<a id="ga73c30a58e1819ab501aa6c31a9a76c7c"></a>

### `INPUT_NUNCHUK_ACCEL_Z`

```c
#define INPUT_NUNCHUK_ACCEL_Z 2
```

```c
#include <zephyr/input/input_nunchuk.h>
```

Nunchuk 报告的 Z 轴加速度（Acceleration）。

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_INPUT_NUNCHUK_ACCELERATION` 时可用。

<a id="ga481650458998947e79ee89fbf1402435"></a>

### `nunchuk_read()`

```c
int nunchuk_read ( const struct device * dev)
```

```c
#include <zephyr/input/input_nunchuk.h>
```

开始从 Nunchuk 读取当前按键状态（Button States）、摇杆位置（Joystick Position），以及可选的加速度（Acceleration）；加速度读取需要启用 `CONFIG_INPUT_NUNCHUK_ACCELERATION`。

只有在 Nunchuk 输入驱动的 DTS 定义中将 `polling-interval-ms` 属性设为 0，从而禁用后台轮询（background polling）时，此函数才能正常工作。

注意，此函数会立即返回；随后在后台从 Nunchuk 读取数据，并通过标准输入事件接口（input event interface）上报。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 Nunchuk 设备的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `SUCCESS` | 已能启动数据读取过程。 |
| `-errno` | 发生任何错误时。 |


## 42.5\_原页交叉引用（Cross References）

- [input_nunchuk.h](../api_file_service_reference/P016_zephyr__input__input_nunchuk.h_文件参考.md)
- [device](../device_reference/P002_设备对象结构.md)
- [CONFIG_INPUT_NUNCHUK_ACCELERATION](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT_NUNCHUK_ACCELERATION)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P041_NPCX 转速计（Tachometer）.md) · [返回大纲](大纲.md) · [下一章](P043_PAT9136 API主题.md)
