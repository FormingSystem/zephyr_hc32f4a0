---
id: learning.zephyr-docs.api-extension-topic-reference.page-23
title: PAT912x API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__pat912x__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第23章\_PAT912x API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__pat912x__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

PAT912x 微型光学导航芯片（Miniature Optical Navigation Chip）。

<a id="details"></a>

PAT912x 微型光学导航芯片（Miniature Optical Navigation Chip）。

<a id="header-files"></a>
<a id="files"></a>

## 23.1\_文件（Files）

<a id="r_input_5Fpat912x_2Eh"></a>

```c
file input_pat912x.h
```

相关声明：[input_pat912x.h](../api_file_supplement_reference/P048_zephyr__input__input_pat912x.h_文件参考.md)。

PAT912x输入（Input）驱动的头文件。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 23.2\_函数（Functions）

<a id="r_ga1c9f11b31312dbaf5cf24ddaaad7eada"></a>

```c
int pat912x_set_resolution (const struct device *dev, int16_t res_x_cpi, int16_t res_y_cpi)
```

相关声明：[pat912x_set_resolution](#ga1c9f11b31312dbaf5cf24ddaaad7eada)、[device](../device_reference/P002_设备对象结构.md)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

设置 pat912x 设备的分辨率（Resolution）。

## 23.3\_详细说明（Detailed Documentation）

<a id="ga1c9f11b31312dbaf5cf24ddaaad7eada"></a>

### `pat912x_set_resolution()`

```c
int pat912x_set_resolution ( const struct device * dev, int16_t res_x_cpi, int16_t res_y_cpi )
```

```c
#include <zephyr/input/input_pat912x.h>
```

设置 pat912x 设备的分辨率（Resolution）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | pat912x 设备（Device）。 |
| `res_x_cpi` | X 轴每英寸计数分辨率（CPI Resolution）：0～1275；`-1` 表示保持当前值。 |
| `res_y_cpi` | Y 轴每英寸计数分辨率（CPI Resolution）：0～1275；`-1` 表示保持当前值。 |


## 23.4\_原页交叉引用（Cross References）

- [input_pat912x.h](../api_file_supplement_reference/P048_zephyr__input__input_pat912x.h_文件参考.md)
- [device](../device_reference/P002_设备对象结构.md)
- [int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P022_分组套接字的套接字选项（Socket options for packet socket）.md) · [返回大纲](大纲.md) · [下一章](P024_PAW32xx API主题.md)
