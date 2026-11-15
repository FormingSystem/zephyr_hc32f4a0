---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-4
title: crsf_payload_attitude_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcrsf__payload__attitude.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_crsf\_payload\_attitude\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structcrsf__payload__attitude.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

姿态遥测（Attitude Telemetry）载荷，类型为0x1E。

```c
#include <zephyr/input/input_crsf.h>
```

<a id="details"></a>

姿态遥测（Attitude Telemetry）载荷，类型为0x1E。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 4.1\_数据成员（Data Fields）

<a id="r_a72273cb8a6eed97f5656e0dee23aef14"></a>

```c
int16_t pitch_rad
```

相关声明：[int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)、[pitch_rad](#a72273cb8a6eed97f5656e0dee23aef14)。

俯仰角（Pitch angle），编码值为弧度值乘以 10,000。

<a id="r_adbc100ab349999d3b34d4934994f3c40"></a>

```c
int16_t roll_rad
```

相关声明：[int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)、[roll_rad](#adbc100ab349999d3b34d4934994f3c40)。

横滚角（Roll angle），编码值为弧度值乘以 10,000。

<a id="r_a7e745fcb15244c9619486d344436a6be"></a>

```c
int16_t yaw_rad
```

相关声明：[int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)、[yaw_rad](#a7e745fcb15244c9619486d344436a6be)。

偏航角（Yaw angle），编码值为弧度值乘以 10,000。

## 4.2\_详细说明（Detailed Documentation）

<a id="a72273cb8a6eed97f5656e0dee23aef14"></a>

### `pitch_rad`

```c
int16_t crsf_payload_attitude::pitch_rad
```

俯仰角（Pitch angle），编码值为弧度值乘以 10,000。

<a id="adbc100ab349999d3b34d4934994f3c40"></a>

### `roll_rad`

```c
int16_t crsf_payload_attitude::roll_rad
```

横滚角（Roll angle），编码值为弧度值乘以 10,000。

<a id="a7e745fcb15244c9619486d344436a6be"></a>

### `yaw_rad`

```c
int16_t crsf_payload_attitude::yaw_rad
```

偏航角（Yaw angle），编码值为弧度值乘以 10,000。

本数据类型文档由以下文件生成：

- `zephyr/input/input_crsf.h`

## 4.3\_原页交叉引用（Cross References）

- [zephyr/input/input_crsf.h](https://docs.zephyrproject.org/latest/doxygen/html/input__crsf_8h_source.html)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P003_crsf_link_stats_结构体.md) · [返回大纲](大纲.md) · [下一章](P005_crsf_payload_battery_结构体.md)
