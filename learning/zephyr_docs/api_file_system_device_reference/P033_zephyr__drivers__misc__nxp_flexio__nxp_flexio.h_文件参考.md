---
id: learning.zephyr-docs.api-file-system-device-reference.page-33
title: zephyr__drivers__misc__nxp_flexio__nxp_flexio.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nxp__flexio_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第33章\_zephyr\_\_drivers\_\_misc\_\_nxp\_flexio\_\_nxp\_flexio.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/nxp__flexio_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

NXP FlexIO驱动的头文件。

<a id="details"></a>

```c
#include <zephyr/device.h>
```

查看此文件的源码。

NXP FlexIO驱动的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 33.1\_数据结构（Data Structures）

<a id="r_nxp_5Fflexio_5Fchild_5Fres"></a>

```c
struct nxp_flexio_child_res
```

相关声明：[nxp_flexio_child_res](../platform_security_model_reference/P021_nxp_flexio_child_res_结构体.md)。

包含FlexIO子设备所需资源信息的结构。

<a id="r_nxp_5Fflexio_5Fchild"></a>

```c
struct nxp_flexio_child
```

相关声明：[nxp_flexio_child](../platform_security_model_reference/P020_nxp_flexio_child_结构体.md)。

包含FlexIO所需子设备数据（Child Data）的结构。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 33.2\_类型定义（Typedefs）

<a id="r_gaf11959c4e7c7a5ef56b082fcf0b7f42c"></a>

```c
typedef int(* nxp_flexio_child_isr_t) (void *user_data)
```

相关声明：[nxp_flexio_child_isr_t](https://docs.zephyrproject.org/latest/doxygen/html/group__nxp__flexio__interface.html#gaf11959c4e7c7a5ef56b082fcf0b7f42c)。

用于通知 API 用户 FlexIO 已触发中断的回调 API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 33.3\_函数（Functions）

<a id="r_ga7e84a09852b713337d6e124eb2b8df7d"></a>

```c
void nxp_flexio_irq_enable (const struct device *dev)
```

相关声明：[nxp_flexio_irq_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__nxp__flexio__interface.html#ga7e84a09852b713337d6e124eb2b8df7d)、[device](../device_reference/P002_设备对象结构.md)。

启用 FlexIO 中断请求（IRQ）。

<a id="r_ga39b6b8b2eda354b4d3a40da48f41e3d2"></a>

```c
void nxp_flexio_irq_disable (const struct device *dev)
```

相关声明：[nxp_flexio_irq_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__nxp__flexio__interface.html#ga39b6b8b2eda354b4d3a40da48f41e3d2)、[device](../device_reference/P002_设备对象结构.md)。

禁用 FlexIO IRQ。

<a id="r_ga3be561d6ee29eb0e23f67ddcf234d22e"></a>

```c
void nxp_flexio_lock (const struct device *dev)
```

相关声明：[nxp_flexio_lock](https://docs.zephyrproject.org/latest/doxygen/html/group__nxp__flexio__interface.html#ga3be561d6ee29eb0e23f67ddcf234d22e)、[device](../device_reference/P002_设备对象结构.md)。

锁定 FlexIO 互斥锁（mutex）。

<a id="r_gab5ff53d4ac41321fe4726e2ede175ac2"></a>

```c
void nxp_flexio_unlock (const struct device *dev)
```

相关声明：[nxp_flexio_unlock](https://docs.zephyrproject.org/latest/doxygen/html/group__nxp__flexio__interface.html#gab5ff53d4ac41321fe4726e2ede175ac2)、[device](../device_reference/P002_设备对象结构.md)。

解锁 FlexIO 互斥锁。

<a id="r_ga9c5fdb0b5b11dcc04d42c2c7b98b3ffb"></a>

```c
int nxp_flexio_get_rate (const struct device *dev, uint32_t *rate)
```

相关声明：[nxp_flexio_get_rate](https://docs.zephyrproject.org/latest/doxygen/html/group__nxp__flexio__interface.html#ga9c5fdb0b5b11dcc04d42c2c7b98b3ffb)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取 FlexIO 所用子系统的时钟频率（clock rate）。

<a id="r_ga1208ad4ef70419ff61a87b8b1ff8d446"></a>

```c
int nxp_flexio_child_attach (const struct device *dev, const struct nxp_flexio_child *child)
```

相关声明：[nxp_flexio_child_attach](https://docs.zephyrproject.org/latest/doxygen/html/group__nxp__flexio__interface.html#ga1208ad4ef70419ff61a87b8b1ff8d446)、[device](../device_reference/P002_设备对象结构.md)、[nxp_flexio_child](../platform_security_model_reference/P020_nxp_flexio_child_结构体.md)。

将 FlexIO 子设备附接到 FlexIO 控制器。


## 33.4\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P619_nxp_flexio.h_源码浏览.md)
- [nxp_flexio_child_res](../platform_security_model_reference/P021_nxp_flexio_child_res_结构体.md)
- [nxp_flexio_child](../platform_security_model_reference/P020_nxp_flexio_child_结构体.md)
- [nxp_flexio_child_isr_t](https://docs.zephyrproject.org/latest/doxygen/html/group__nxp__flexio__interface.html#gaf11959c4e7c7a5ef56b082fcf0b7f42c)
- [nxp_flexio_irq_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__nxp__flexio__interface.html#ga7e84a09852b713337d6e124eb2b8df7d)
- [device](../device_reference/P002_设备对象结构.md)
- [nxp_flexio_irq_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__nxp__flexio__interface.html#ga39b6b8b2eda354b4d3a40da48f41e3d2)
- [nxp_flexio_lock](https://docs.zephyrproject.org/latest/doxygen/html/group__nxp__flexio__interface.html#ga3be561d6ee29eb0e23f67ddcf234d22e)
- [nxp_flexio_unlock](https://docs.zephyrproject.org/latest/doxygen/html/group__nxp__flexio__interface.html#gab5ff53d4ac41321fe4726e2ede175ac2)
- [nxp_flexio_get_rate](https://docs.zephyrproject.org/latest/doxygen/html/group__nxp__flexio__interface.html#ga9c5fdb0b5b11dcc04d42c2c7b98b3ffb)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [nxp_flexio_child_attach](https://docs.zephyrproject.org/latest/doxygen/html/group__nxp__flexio__interface.html#ga1208ad4ef70419ff61a87b8b1ff8d446)

<a id="header-details"></a>

---

[上一章](P032_zephyr__drivers__firmware__scmi__nxp__system.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P034_zephyr__bluetooth__mesh__op_agg_cli.h_文件参考.md)
