---
id: learning.zephyr-docs.device-power-control-model-reference.page-31
title: mfd_adp5585_config_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmfd__adp5585__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第31章\_mfd\_adp5585\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmfd__adp5585__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/drivers/mfd/adp5585.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 31.1\_数据成员（Data Fields）

<a id="r_af0c8d2113efb5fad7193c5969294660b"></a>

```c
struct gpio_dt_spec reset_gpio
```

相关声明：[gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)、[reset_gpio](#af0c8d2113efb5fad7193c5969294660b)。

<a id="r_a29c59990dea7c1e219f1f42baa699feb"></a>

```c
struct gpio_dt_spec nint_gpio
```

相关声明：[gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)、[nint_gpio](#a29c59990dea7c1e219f1f42baa699feb)。

<a id="r_ab27f8be0f4f2d29b0fe7e400cd475cd4"></a>

```c
struct i2c_dt_spec i2c_bus
```

相关声明：[i2c_dt_spec](../hardware/P306_I2C设备树描述.md)、[i2c_bus](#ab27f8be0f4f2d29b0fe7e400cd475cd4)。

## 31.2\_详细说明（Detailed Documentation）

<a id="ab27f8be0f4f2d29b0fe7e400cd475cd4"></a>

### `i2c_bus`

```c
struct i2c_dt_spec mfd_adp5585_config::i2c_bus
```

<a id="a29c59990dea7c1e219f1f42baa699feb"></a>

### `nint_gpio`

```c
struct gpio_dt_spec mfd_adp5585_config::nint_gpio
```

<a id="af0c8d2113efb5fad7193c5969294660b"></a>

### `reset_gpio`

```c
struct gpio_dt_spec mfd_adp5585_config::reset_gpio
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/mfd/adp5585.h`

## 31.3\_原页交叉引用（Cross References）

- [zephyr/drivers/mfd/adp5585.h](https://docs.zephyrproject.org/latest/doxygen/html/adp5585_8h_source.html)
- [gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)
- [i2c_dt_spec](../hardware/P306_I2C设备树描述.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P030_media_proxy_pl_calls_结构体.md) · [返回大纲](大纲.md) · [下一章](P032_mfd_adp5585_data_结构体.md)
