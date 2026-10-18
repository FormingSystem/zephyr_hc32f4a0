---
id: learning.zephyr-docs.dma-reference.page-2
title: DMA驱动后端接口
kind: reference
status: maintained
domains: [zephyr, dma, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__dma__interface__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_DMA驱动后端接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__interface__backend.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：本页是直接内存访问（Direct Memory Access，DMA）应用程序接口（Application Programming Interface，API）参考。先读[DMA概述](../hardware/P011_DMA直接内存访问.md)，再按[本册大纲](大纲.md)区分通道配置（Channel Configuration）、传输块（Transfer Block）、运行状态（Runtime Status）与驱动后端（Driver Backend）。原始标识符、类型与常量保持不变；重复的接口摘要与详细说明均保留。

<a id="details"></a>

本组包含实现DMA驱动所需的API类型定义、回调函数签名及其他辅助项。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 2.1\_数据结构（Data Structures）

<a id="r_dma_5Fdriver_5Fapi"></a>

```c
struct dma_driver_api
```

相关声明：[dma_driver_api](P007_DMA驱动操作结构.md)。

驱动操作（Driver Operations）：DMA驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 2.2\_类型定义（Typedefs）

<a id="r_gab15e273c0f3b1978d17ad448d98f56bb"></a>

```c
typedef int(* dma_api_config) (const struct device *dev, uint32_t channel, struct dma_config *config)
```

相关声明：[dma_api_config](#gab15e273c0f3b1978d17ad448d98f56bb)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[dma_config](P004_DMA通道配置.md)。

为DMA传输配置单个通道（Channel）。

<a id="r_gab00e7199fa8dafa541e4ef5f63c391b4"></a>

```c
typedef int(* dma_api_reload) (const struct device *dev, uint32_t channel, uint32_t src, uint32_t dst, size_t size)
```

相关声明：[dma_api_reload](#gab00e7199fa8dafa541e4ef5f63c391b4)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

重新装载（Reload）DMA通道的缓冲区。

<a id="r_ga1cd1fc992eb0e95690a50e2696247da0"></a>

```c
typedef int(* dma_api_start) (const struct device *dev, uint32_t channel)
```

相关声明：[dma_api_start](#ga1cd1fc992eb0e95690a50e2696247da0)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

使能DMA通道并启动传输。

<a id="r_gad63e7dc2e41adc03f4a338bda760f2ff"></a>

```c
typedef int(* dma_api_stop) (const struct device *dev, uint32_t channel)
```

相关声明：[dma_api_stop](#gad63e7dc2e41adc03f4a338bda760f2ff)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

停止DMA传输并禁用通道。

<a id="r_gad3742f6c4218b6a648e9aa5734516818"></a>

```c
typedef int(* dma_api_suspend) (const struct device *dev, uint32_t channel)
```

相关声明：[dma_api_suspend](#gad3742f6c4218b6a648e9aa5734516818)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

挂起（Suspend）DMA通道传输。

<a id="r_ga5073bb15b75cbbbcdbd3f859f28e3473"></a>

```c
typedef int(* dma_api_resume) (const struct device *dev, uint32_t channel)
```

相关声明：[dma_api_resume](#ga5073bb15b75cbbbcdbd3f859f28e3473)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

恢复（Resume）DMA通道传输。

<a id="r_ga06781c37590c23e6df82471aac4923dc"></a>

```c
typedef int(* dma_api_get_status) (const struct device *dev, uint32_t channel, struct dma_status *status)
```

相关声明：[dma_api_get_status](#ga06781c37590c23e6df82471aac4923dc)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[dma_status](P005_DMA运行状态.md)。

取得DMA传输的当前运行时状态。

<a id="r_ga2cc72d829ce7f47eb2a326faaedf3fc5"></a>

```c
typedef int(* dma_api_get_attribute) (const struct device *dev, uint32_t type, uint32_t *value)
```

相关声明：[dma_api_get_attribute](#ga2cc72d829ce7f47eb2a326faaedf3fc5)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

取得DMA控制器的属性。

<a id="r_ga1c65fe109d52e477f3bafa56e4afefb7"></a>

```c
typedef bool(* dma_api_chan_filter) (const struct device *dev, int channel, void *filter_param)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[dma_api_chan_filter](#ga1c65fe109d52e477f3bafa56e4afefb7)、[device](../device_reference/P002_设备对象结构.md)。

通道筛选函数调用（Channel Filter）。

<a id="r_ga035b4982cae52df4ce1911ad007d3a64"></a>

```c
typedef void(* dma_api_chan_release) (const struct device *dev, uint32_t channel)
```

相关声明：[dma_api_chan_release](#ga035b4982cae52df4ce1911ad007d3a64)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

通道释放函数调用（Channel Release）。

## 2.3\_详细说明（Detailed Documentation）

<a id="ga1c65fe109d52e477f3bafa56e4afefb7"></a>

### `dma_api_chan_filter`

```c
typedef bool(* dma_api_chan_filter) (const struct device *dev, int channel, void *filter_param)
```

```c
#include <zephyr/drivers/dma.h>
```

通道筛选函数调用（Channel Filter）。

调用方提供的筛选函数，用于查找匹配的内部DMA通道。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向DMA设备实例。 |
| `channel` | 要使用的通道ID。 |
| `filter_param` | 筛选函数参数，可以为NULL。 |

**返回（Returns）**：筛选匹配时返回True，否则返回False。

<a id="ga035b4982cae52df4ce1911ad007d3a64"></a>

### `dma_api_chan_release`

```c
typedef void(* dma_api_chan_release) (const struct device *dev, uint32_t channel)
```

```c
#include <zephyr/drivers/dma.h>
```

通道释放函数调用（Channel Release）。

用于释放申请阶段“分配”的通道资源，例如已使能的电源域（Power Domain，PD）、中断请求（Interrupt Request，IRQ）等。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向DMA设备实例。 |
| `channel` | 要使用的通道ID。 |

<a id="gab15e273c0f3b1978d17ad448d98f56bb"></a>

### `dma_api_config`

```c
typedef int(* dma_api_config) (const struct device *dev, uint32_t channel, struct dma_config *config)
```

```c
#include <zephyr/drivers/dma.h>
```

为DMA传输配置单个通道（Channel）。

参数说明见dma_config()。

<a id="ga2cc72d829ce7f47eb2a326faaedf3fc5"></a>

### `dma_api_get_attribute`

```c
typedef int(* dma_api_get_attribute) (const struct device *dev, uint32_t type, uint32_t *value)
```

```c
#include <zephyr/drivers/dma.h>
```

取得DMA控制器的属性。

参数说明见dma_get_attribute()。

<a id="ga06781c37590c23e6df82471aac4923dc"></a>

### `dma_api_get_status`

```c
typedef int(* dma_api_get_status) (const struct device *dev, uint32_t channel, struct dma_status *status)
```

```c
#include <zephyr/drivers/dma.h>
```

取得DMA传输的当前运行时状态。

参数说明见dma_get_status()。

<a id="gab00e7199fa8dafa541e4ef5f63c391b4"></a>

### `dma_api_reload`

```c
typedef int(* dma_api_reload) (const struct device *dev, uint32_t channel, uint32_t src, uint32_t dst, size_t size)
```

```c
#include <zephyr/drivers/dma.h>
```

重新装载（Reload）DMA通道的缓冲区。

参数说明见dma_reload()。

> 译注——源码核对：该函数指针及公共dma_reload在CONFIG_DMA_64BIT下使用64位源／目标地址，默认分支为32位。本页保留官方网页展示的原型；实际编译以所用头文件和配置为准。

<a id="ga5073bb15b75cbbbcdbd3f859f28e3473"></a>

### `dma_api_resume`

```c
typedef int(* dma_api_resume) (const struct device *dev, uint32_t channel)
```

```c
#include <zephyr/drivers/dma.h>
```

恢复（Resume）DMA通道传输。

参数说明见dma_resume()。

<a id="ga1cd1fc992eb0e95690a50e2696247da0"></a>

### `dma_api_start`

```c
typedef int(* dma_api_start) (const struct device *dev, uint32_t channel)
```

```c
#include <zephyr/drivers/dma.h>
```

使能DMA通道并启动传输。

参数说明见dma_start()。

<a id="gad63e7dc2e41adc03f4a338bda760f2ff"></a>

### `dma_api_stop`

```c
typedef int(* dma_api_stop) (const struct device *dev, uint32_t channel)
```

```c
#include <zephyr/drivers/dma.h>
```

停止DMA传输并禁用通道。

参数说明见dma_stop()。

<a id="gad3742f6c4218b6a648e9aa5734516818"></a>

### `dma_api_suspend`

```c
typedef int(* dma_api_suspend) (const struct device *dev, uint32_t channel)
```

```c
#include <zephyr/drivers/dma.h>
```

挂起（Suspend）DMA通道传输。

参数说明见dma_suspend()。

## 2.4\_源码定位与版本边界

接口、配置结构和内联包装均可在仓库的[dma.h](../../../include/zephyr/drivers/dma.h)中相对定位。本次译注核对了[官方main头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/dma.h)，摘要见[来源记录](../SOURCES.md)；本地源码、滚动更新的main与latest网页不能自动视为同一版本。原始头文件法律署名为Copyright (c) 2016 Intel Corporation，许可证为Apache-2.0。

本批只翻译和核对官方源码，没有构建、执行DMA搬运、运行驱动测试或进行实板验证；这组参考也不声明本仓库已实现HC32 DMA驱动。

## 2.5\_原页交叉引用（Cross References）

- [dma_driver_api](P007_DMA驱动操作结构.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [dma_config](P004_DMA通道配置.md)
- [dma_status](P005_DMA运行状态.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [zephyr/drivers/dma.h](P009_DMA驱动头文件参考.md)
- [dma_config()](P001_DMA公共接口.md#ga6df1a6b89f271a0eae01c17b748bd2df)
- [dma_get_attribute()](P001_DMA公共接口.md#ga641f3fa492bfb17cf9f0a0361d429257)
- [dma_get_status()](P001_DMA公共接口.md#ga2cae500f1f9ed42ad338a40ec8655544)
- [dma_reload()](P001_DMA公共接口.md#ga55bd5d550349c11c63ef47c2ed861f36)
- [dma_resume()](P001_DMA公共接口.md#ga1b1eeef68f1aa4818c9baf95b83b9e1e)
- [dma_start()](P001_DMA公共接口.md#gaf1184de07811702ffe89737b79e4a338)
- [dma_stop()](P001_DMA公共接口.md#gafd602ee8386e10bb9ac7d386b3dc6a83)
- [dma_suspend()](P001_DMA公共接口.md#ga97bf9807b7fde7671a378333f01463d6)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P001_DMA公共接口.md) · [返回大纲](大纲.md) · [下一章](P003_DMA传输块配置.md)
