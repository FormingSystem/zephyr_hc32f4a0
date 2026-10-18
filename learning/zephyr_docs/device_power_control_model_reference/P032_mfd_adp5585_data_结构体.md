---
id: learning.zephyr-docs.device-power-control-model-reference.page-32
title: mfd_adp5585_data_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmfd__adp5585__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第32章\_mfd\_adp5585\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmfd__adp5585__data.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/drivers/mfd/adp5585.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 32.1\_数据成员（Data Fields）

<a id="r_aad6ae38b0cfe0b216f9a965718ae92bf"></a>

```c
struct k_work work
```

相关声明：[k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)、[work](#aad6ae38b0cfe0b216f9a965718ae92bf)。

<a id="r_a87322b6acebc0c77b4d98ab8ee6b57e6"></a>

```c
struct k_sem lock
```

相关声明：[k_sem](../synchronization_reference/P009_内核信号量结构.md)、[lock](#a87322b6acebc0c77b4d98ab8ee6b57e6)。

<a id="r_aa517e16739c65b8468df3ef26c3b7c06"></a>

```c
const struct device * dev
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[dev](#aa517e16739c65b8468df3ef26c3b7c06)。

```c
struct {
```

<a id="r_ac890b9075851d9b9b3a102043ba522ac"></a>

```c
} child
```

相关声明：[child](#ac890b9075851d9b9b3a102043ba522ac)。

<a id="r_a22322bec62253aedbe8be191bf735e72"></a>

```c
struct gpio_callback int_gpio_cb
```

相关声明：[gpio_callback](../hardware/P270_GPIO回调结构.md)、[int_gpio_cb](#a22322bec62253aedbe8be191bf735e72)。

## 32.2\_详细说明（Detailed Documentation）

<a id="ac890b9075851d9b9b3a102043ba522ac"></a>

### `[struct]`

```c
struct { ... } mfd_adp5585_data::child
```

<a id="aa517e16739c65b8468df3ef26c3b7c06"></a>

### `dev`

```c
const struct device* mfd_adp5585_data::dev
```

<a id="a22322bec62253aedbe8be191bf735e72"></a>

### `int_gpio_cb`

```c
struct gpio_callback mfd_adp5585_data::int_gpio_cb
```

<a id="a87322b6acebc0c77b4d98ab8ee6b57e6"></a>

### `lock`

```c
struct k_sem mfd_adp5585_data::lock
```

<a id="aad6ae38b0cfe0b216f9a965718ae92bf"></a>

### `work`

```c
struct k_work mfd_adp5585_data::work
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/mfd/adp5585.h`

## 32.3\_原页交叉引用（Cross References）

- [zephyr/drivers/mfd/adp5585.h](https://docs.zephyrproject.org/latest/doxygen/html/adp5585_8h_source.html)
- [k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)
- [k_sem](../synchronization_reference/P009_内核信号量结构.md)
- [device](../device_reference/P002_设备对象结构.md)
- [gpio_callback](../hardware/P270_GPIO回调结构.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P031_mfd_adp5585_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P033_mfd_npm10xx_event_callback_结构体.md)
