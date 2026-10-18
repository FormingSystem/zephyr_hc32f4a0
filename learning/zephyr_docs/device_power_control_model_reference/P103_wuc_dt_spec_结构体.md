---
id: learning.zephyr-docs.device-power-control-model-reference.page-103
title: wuc_dt_spec_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structwuc__dt__spec.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第103章\_wuc\_dt\_spec\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structwuc__dt__spec.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

唤醒控制器（Wakeup Controller）的设备配置。

```c
#include <zephyr/drivers/wuc.h>
```

<a id="details"></a>

唤醒控制器（Wakeup Controller）的设备配置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 103.1\_数据成员（Data Fields）

<a id="r_a7c0c301fad56d99ca1d35007b6da88fc"></a>

```c
const struct device * dev
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[dev](#a7c0c301fad56d99ca1d35007b6da88fc)。

唤醒控制器设备。

<a id="r_ab617463172da938eb1e7e97a4ec0bb67"></a>

```c
uint32_t id
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[id](#ab617463172da938eb1e7e97a4ec0bb67)。

唤醒源标识符。

## 103.2\_详细说明（Detailed Documentation）

<a id="a7c0c301fad56d99ca1d35007b6da88fc"></a>

### `dev`

```c
const struct device* wuc_dt_spec::dev
```

唤醒控制器设备。

<a id="ab617463172da938eb1e7e97a4ec0bb67"></a>

### `id`

```c
uint32_t wuc_dt_spec::id
```

唤醒源标识符。

本数据类型文档由以下文件生成：

- `zephyr/drivers/wuc.h`

## 103.3\_原页交叉引用（Cross References）

- [zephyr/drivers/wuc.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2wuc_8h_source.html)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P102_wuc_driver_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P104_charger_propval_联合体.md)
