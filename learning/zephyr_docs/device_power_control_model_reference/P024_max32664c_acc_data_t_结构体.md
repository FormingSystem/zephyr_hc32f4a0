---
id: learning.zephyr-docs.device-power-control-model-reference.page-24
title: max32664c_acc_data_t_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmax32664c__acc__data__t.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_max32664c\_acc\_data\_t\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmax32664c__acc__data__t.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

外部加速度计（External Accelerometer）数据的数据结构。

```c
#include <zephyr/drivers/sensor/max32664c.h>
```

<a id="details"></a>

外部加速度计（Accelerometer）数据结构。此结构体表示从外部加速度计采集并送入 MAX32664C 传感器集线器（Sensor hub）的数据，包含 x、y、z 三轴加速度值。仅在启用外部加速度计时使用。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 24.1\_数据成员（Data Fields）

<a id="r_a8e95a8eaa70345cfe213995a041f70b8"></a>

```c
int16_t x
```

相关声明：[int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)、[x](#a8e95a8eaa70345cfe213995a041f70b8)。

X 轴加速度。

<a id="r_a597ae57e9ff4879f0410b3bf0bb87377"></a>

```c
int16_t y
```

相关声明：[int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)、[y](#a597ae57e9ff4879f0410b3bf0bb87377)。

Y 轴加速度。

<a id="r_a9df29b0f8724792617f00e5aed49e7bb"></a>

```c
int16_t z
```

相关声明：[int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)、[z](#a9df29b0f8724792617f00e5aed49e7bb)。

Z 轴加速度。

## 24.2\_详细说明（Detailed Documentation）

<a id="a8e95a8eaa70345cfe213995a041f70b8"></a>

### `x`

```c
int16_t max32664c_acc_data_t::x
```

X 轴加速度。

<a id="a597ae57e9ff4879f0410b3bf0bb87377"></a>

### `y`

```c
int16_t max32664c_acc_data_t::y
```

Y 轴加速度。

<a id="a9df29b0f8724792617f00e5aed49e7bb"></a>

### `z`

```c
int16_t max32664c_acc_data_t::z
```

Z 轴加速度。

本数据类型文档由以下文件生成：

- `zephyr/drivers/sensor/max32664c.h`

## 24.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor/max32664c.h](https://docs.zephyrproject.org/latest/doxygen/html/max32664c_8h_source.html)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P023_max22017_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P025_max32_perclk_结构体.md)
