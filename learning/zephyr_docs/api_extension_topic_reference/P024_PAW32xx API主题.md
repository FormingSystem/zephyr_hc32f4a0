---
id: learning.zephyr-docs.api-extension-topic-reference.page-24
title: PAW32xx API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__paw32xx__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_PAW32xx API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__paw32xx__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

PAW32xx 超低功耗无线鼠标芯片（Ultra low power wireless mouse chip）。

<a id="details"></a>

PAW32xx 超低功耗无线鼠标芯片（Ultra low power wireless mouse chip）。

<a id="header-files"></a>
<a id="files"></a>

## 24.1\_文件（Files）

<a id="r_input_5Fpaw32xx_2Eh"></a>

```c
file input_paw32xx.h
```

相关声明：[input_paw32xx.h](../api_file_configuration_reference/P043_zephyr__input__input_paw32xx.h_文件参考.md)。

PAW32xx输入（Input）驱动的头文件。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 24.2\_函数（Functions）

<a id="r_ga7c15c20653486833cb07a43cd92c97cf"></a>

```c
int paw32xx_set_resolution (const struct device *dev, uint16_t res_cpi)
```

相关声明：[paw32xx_set_resolution](#ga7c15c20653486833cb07a43cd92c97cf)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置 paw32xx 设备的分辨率（Resolution）。

<a id="r_ga03c6aa7e9e7b370791c16292055b9fff"></a>

```c
int paw32xx_force_awake (const struct device *dev, bool enable)
```

相关声明：[paw32xx_force_awake](#ga03c6aa7e9e7b370791c16292055b9fff)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置 paw32xx 设备的强制唤醒模式（Force Awake Mode）。

## 24.3\_详细说明（Detailed Documentation）

<a id="ga03c6aa7e9e7b370791c16292055b9fff"></a>

### `paw32xx_force_awake()`

```c
int paw32xx_force_awake ( const struct device * dev, bool enable )
```

```c
#include <zephyr/input/input_paw32xx.h>
```

设置 paw32xx 设备的强制唤醒模式（Force Awake Mode）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | paw32xx 设备（Device）。 |
| `enable` | 是否启用或禁用强制唤醒模式（Force Awake Mode）。 |

<a id="ga7c15c20653486833cb07a43cd92c97cf"></a>

### `paw32xx_set_resolution()`

```c
int paw32xx_set_resolution ( const struct device * dev, uint16_t res_cpi )
```

```c
#include <zephyr/input/input_paw32xx.h>
```

设置 paw32xx 设备的分辨率（Resolution）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | paw32xx 设备（Device）。 |
| `res_cpi` | 每英寸计数分辨率（CPI Resolution）：200～3200。 |


## 24.4\_原页交叉引用（Cross References）

- [input_paw32xx.h](../api_file_configuration_reference/P043_zephyr__input__input_paw32xx.h_文件参考.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P023_PAT912x API主题.md) · [返回大纲](大纲.md) · [下一章](P025_PCIe 主机精确时间测量（PTM）接口.md)
