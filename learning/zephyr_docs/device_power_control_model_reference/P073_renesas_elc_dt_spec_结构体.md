---
id: learning.zephyr-docs.device-power-control-model-reference.page-73
title: renesas_elc_dt_spec_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structrenesas__elc__dt__spec.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第73章\_renesas\_elc\_dt\_spec\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structrenesas__elc__dt__spec.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

设备树（Devicetree）所指定Renesas事件链路控制器（ELC）信息的容器。

```c
#include <zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h>
```

<a id="details"></a>

保存设备树中指定的 Renesas 事件链接控制器（Event Link Controller，ELC）信息。此类型包含 Renesas ELC 设备指针，以及用于通过 ELC 配置外设间链接的外设 ID 和事件 ID。通常通过设备树宏初始化该结构体，这些宏解析引用 ELC 实例的 `phandle-array` 属性。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 73.1\_数据成员（Data Fields）

<a id="r_ae759c1c19bd7c69d14165a12331f3df4"></a>

```c
const struct device * dev
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[dev](#ae759c1c19bd7c69d14165a12331f3df4)。

Renesas ELC 设备实例。

<a id="r_a7b20982a91e3bb944c7aaf94b6fd33dd"></a>

```c
uint32_t peripheral
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[peripheral](#a7b20982a91e3bb944c7aaf94b6fd33dd)。

Renesas ELC 外设 ID。

<a id="r_a9004b468890e2901b4316e9f2fa648ea"></a>

```c
uint32_t event
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[event](#a9004b468890e2901b4316e9f2fa648ea)。

Renesas ELC 事件 ID。

## 73.2\_详细说明（Detailed Documentation）

<a id="ae759c1c19bd7c69d14165a12331f3df4"></a>

### `dev`

```c
const struct device* renesas_elc_dt_spec::dev
```

Renesas ELC 设备实例。

<a id="a9004b468890e2901b4316e9f2fa648ea"></a>

### `event`

```c
uint32_t renesas_elc_dt_spec::event
```

Renesas ELC 事件 ID。

<a id="a7b20982a91e3bb944c7aaf94b6fd33dd"></a>

### `peripheral`

```c
uint32_t renesas_elc_dt_spec::peripheral
```

Renesas ELC 外设 ID。

本数据类型文档由以下文件生成：

- `zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h`

## 73.3\_原页交叉引用（Cross References）

- [zephyr/drivers/misc/interconn/renesas_elc/renesas_elc.h](https://docs.zephyrproject.org/latest/doxygen/html/renesas__elc_8h_source.html)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P072_rcar_pin_func_结构体.md) · [返回大纲](大纲.md) · [下一章](P074_renesas_ra_ctsu_touch_cfg_结构体.md)
