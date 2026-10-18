---
id: learning.zephyr-docs.api-topic-reference.page-43
title: IT8XXX2 转速计（Tachometer）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__it8xxx2__tach__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第43章\_IT8XXX2 转速计（Tachometer）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__it8xxx2__tach__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

ITE IT8xxx2 转速计（Tachometer）

<a id="details"></a>

ITE IT8xxx2 转速计（Tachometer）

<a id="header-files"></a>
<a id="files"></a>

## 43.1\_文件（Files）

<a id="r_it8xxx2_5Ftach_2Eh"></a>

```c
file it8xxx2_tach.h
```

相关声明：[it8xxx2_tach.h](../api_file_runtime_reference/P030_zephyr__dt-bindings__sensor__it8xxx2_tach.h_文件参考.md)。

the ITE IT8xxx2 tachometer的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 43.2\_转速计通道（Tachometer Channels）

设备树属性（Devicetree Property）`channel` 的取值。

<a id="r_ga06251760a77cfe0d80731adbda14d82e"></a>

```c
#define IT8XXX2_TACH_CHANNEL_A 0
```

相关声明：[IT8XXX2_TACH_CHANNEL_A](#ga06251760a77cfe0d80731adbda14d82e)。

转速计通道 A（Tachometer Channel A）。

<a id="r_ga3730fcda8c14a9e177122fee9579d6f2"></a>

```c
#define IT8XXX2_TACH_CHANNEL_B 1
```

相关声明：[IT8XXX2_TACH_CHANNEL_B](#ga3730fcda8c14a9e177122fee9579d6f2)。

转速计通道 B（Tachometer Channel B）。

## 43.3\_详细说明（Detailed Documentation）

<a id="ga06251760a77cfe0d80731adbda14d82e"></a>

### `IT8XXX2_TACH_CHANNEL_A`

```c
#define IT8XXX2_TACH_CHANNEL_A 0
```

```c
#include <zephyr/dt-bindings/sensor/it8xxx2_tach.h>
```

转速计通道 A（Tachometer Channel A）。

<a id="ga3730fcda8c14a9e177122fee9579d6f2"></a>

### `IT8XXX2_TACH_CHANNEL_B`

```c
#define IT8XXX2_TACH_CHANNEL_B 1
```

```c
#include <zephyr/dt-bindings/sensor/it8xxx2_tach.h>
```

转速计通道 B（Tachometer Channel B）。


## 43.4\_原页交叉引用（Cross References）

- [it8xxx2_tach.h](../api_file_runtime_reference/P030_zephyr__dt-bindings__sensor__it8xxx2_tach.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P042_IT51XXX 转速计（Tachometer）.md) · [返回大纲](大纲.md) · [下一章](P044_局部互连网络（LIN）.md)
