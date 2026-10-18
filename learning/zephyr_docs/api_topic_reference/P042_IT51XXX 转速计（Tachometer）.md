---
id: learning.zephyr-docs.api-topic-reference.page-42
title: IT51XXX 转速计（Tachometer）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__tach__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第42章\_IT51XXX 转速计（Tachometer）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__it51xxx__tach__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

ITE IT51xxx 转速计（Tachometer）

<a id="details"></a>

ITE IT51xxx 转速计（Tachometer）

<a id="header-files"></a>
<a id="files"></a>

## 42.1\_文件（Files）

<a id="r_it51xxx_5Ftach_2Eh"></a>

```c
file it51xxx_tach.h
```

相关声明：[it51xxx_tach.h](../api_file_runtime_reference/P028_zephyr__dt-bindings__sensor__it51xxx_tach.h_文件参考.md)。

the ITE IT51xxx tachometer的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 42.2\_转速计输入引脚（Tachometer Input Pin）

设备树属性（Devicetree Property）`input-pin` 的取值。

<a id="r_ga7e5b163f187eb15ee5921248da735375"></a>

```c
#define IT51XXX_TACH_INPUT_PIN_A 0
```

相关声明：[IT51XXX_TACH_INPUT_PIN_A](#ga7e5b163f187eb15ee5921248da735375)。

来自引脚 A 的转速计输入（Tachometer Input）。

<a id="r_gaa17ff0e8486961f70888de6ff3d0eaea"></a>

```c
#define IT51XXX_TACH_INPUT_PIN_B 1
```

相关声明：[IT51XXX_TACH_INPUT_PIN_B](#gaa17ff0e8486961f70888de6ff3d0eaea)。

来自引脚 B 的转速计输入（Tachometer Input）。

## 42.3\_详细说明（Detailed Documentation）

<a id="ga7e5b163f187eb15ee5921248da735375"></a>

### `IT51XXX_TACH_INPUT_PIN_A`

```c
#define IT51XXX_TACH_INPUT_PIN_A 0
```

```c
#include <zephyr/dt-bindings/sensor/it51xxx_tach.h>
```

来自引脚 A 的转速计输入（Tachometer Input）。

<a id="gaa17ff0e8486961f70888de6ff3d0eaea"></a>

### `IT51XXX_TACH_INPUT_PIN_B`

```c
#define IT51XXX_TACH_INPUT_PIN_B 1
```

```c
#include <zephyr/dt-bindings/sensor/it51xxx_tach.h>
```

来自引脚 B 的转速计输入（Tachometer Input）。


## 42.4\_原页交叉引用（Cross References）

- [it51xxx_tach.h](../api_file_runtime_reference/P028_zephyr__dt-bindings__sensor__it51xxx_tach.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P041_内部与系统 API（Internal and System API）.md) · [返回大纲](大纲.md) · [下一章](P043_IT8XXX2 转速计（Tachometer）.md)
