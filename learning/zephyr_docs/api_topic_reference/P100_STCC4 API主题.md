---
id: learning.zephyr-docs.api-topic-reference.page-100
title: STCC4 API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__stcc4__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第100章\_STCC4 API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__stcc4__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Sensirion STCC4 二氧化碳（CO2）传感器。

<a id="details"></a>

Sensirion STCC4 二氧化碳（CO2）传感器。

<a id="header-files"></a>
<a id="files"></a>

## 100.1\_文件（Files）

<a id="r_stcc4_2Eh"></a>

```c
file stcc4.h
```

相关声明：[stcc4.h](../api_file_runtime_reference/P064_zephyr__dt-bindings__sensor__stcc4.h_文件参考.md)。

the Sensirion STCC4 CO2 sensor的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 100.2\_测量模式（Measurement Mode）

设备树属性（Devicetree Property）`measurement-mode` 的取值。

<a id="r_ga7ea66c748fdf9063352690a70fd88d6f"></a>

```c
#define STCC4_DT_MODE_CONTINUOUS 0
```

相关声明：[STCC4_DT_MODE_CONTINUOUS](#ga7ea66c748fdf9063352690a70fd88d6f)。

连续测量（Continuous Measurement），频率约为 1 Hz。

<a id="r_ga95c5d1bae8d0cbfa3f4d4c5c37de03d7"></a>

```c
#define STCC4_DT_MODE_SINGLE_SHOT 1
```

相关声明：[STCC4_DT_MODE_SINGLE_SHOT](#ga95c5d1bae8d0cbfa3f4d4c5c37de03d7)。

单次测量（Single-Shot Measurement），每次 500 ms。

## 100.3\_详细说明（Detailed Documentation）

<a id="ga7ea66c748fdf9063352690a70fd88d6f"></a>

### `STCC4_DT_MODE_CONTINUOUS`

```c
#define STCC4_DT_MODE_CONTINUOUS 0
```

```c
#include <zephyr/dt-bindings/sensor/stcc4.h>
```

连续测量（Continuous Measurement），频率约为 1 Hz。

<a id="ga95c5d1bae8d0cbfa3f4d4c5c37de03d7"></a>

### `STCC4_DT_MODE_SINGLE_SHOT`

```c
#define STCC4_DT_MODE_SINGLE_SHOT 1
```

```c
#include <zephyr/dt-bindings/sensor/stcc4.h>
```

单次测量（Single-Shot Measurement），每次 500 ms。


## 100.4\_原页交叉引用（Cross References）

- [stcc4.h](../api_file_runtime_reference/P064_zephyr__dt-bindings__sensor__stcc4.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P099_Silicon Labs 引脚控制辅助工具（Pin control helpers）.md) · [返回大纲](大纲.md) · [下一章](P101_存储 API（Storage APIs）.md)
