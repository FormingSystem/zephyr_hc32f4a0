---
id: learning.zephyr-docs.api-file-management-reference.page-43
title: zephyr__shared_irq.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/shared__irq_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第43章\_zephyr\_\_shared\_irq.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/shared__irq_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/device.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 43.1\_数据结构（Data Structures）

<a id="r_shared_5Firq_5Fdriver_5Fapi"></a>

```c
struct shared_irq_driver_api
```

相关声明：[shared_irq_driver_api](../platform_security_model_reference/P054_shared_irq_driver_api_结构体.md)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 43.2\_类型定义（Typedefs）

<a id="r_af6d98f7cd2cde7482b7276aa6e0b487c"></a>

```c
typedef int(* isr_t) (const struct device *dev, unsigned int irq_number)
```

相关声明：[isr_t](#af6d98f7cd2cde7482b7276aa6e0b487c)、[device](../device_reference/P002_设备对象结构.md)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

<a id="r_ae400920b45bedf3da66831597ebca841"></a>

```c
typedef int(* shared_irq_register_t) (const struct device *dev, isr_t isr_func, const struct device *isr_dev)
```

相关声明：[shared_irq_register_t](#ae400920b45bedf3da66831597ebca841)、[device](../device_reference/P002_设备对象结构.md)、[isr_t](#af6d98f7cd2cde7482b7276aa6e0b487c)、[device](../device_reference/P002_设备对象结构.md)。

<a id="r_a0ff7a6ee448eb3e889aa9a7bd63e49bc"></a>

```c
typedef int(* shared_irq_enable_t) (const struct device *dev, const struct device *isr_dev)
```

相关声明：[shared_irq_enable_t](#a0ff7a6ee448eb3e889aa9a7bd63e49bc)、[device](../device_reference/P002_设备对象结构.md)、[device](../device_reference/P002_设备对象结构.md)。

<a id="r_a22cf2ce082fea27f2087cd1abd74934c"></a>

```c
typedef int(* shared_irq_disable_t) (const struct device *dev, const struct device *isr_dev)
```

相关声明：[shared_irq_disable_t](#a22cf2ce082fea27f2087cd1abd74934c)、[device](../device_reference/P002_设备对象结构.md)、[device](../device_reference/P002_设备对象结构.md)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 43.3\_函数（Functions）

<a id="r_a6ef6d536da13ebd8aa75830516dc0696"></a>

```c
static int shared_irq_isr_register (const struct device *dev, isr_t isr_func, const struct device *isr_dev)
```

相关声明：[shared_irq_isr_register](#a6ef6d536da13ebd8aa75830516dc0696)、[device](../device_reference/P002_设备对象结构.md)、[isr_t](#af6d98f7cd2cde7482b7276aa6e0b487c)、[device](../device_reference/P002_设备对象结构.md)。

注册设备中断服务程序（ISR）。

<a id="r_af36534589858c1e02ea50ed3cc888d41"></a>

```c
static int shared_irq_enable (const struct device *dev, const struct device *isr_dev)
```

相关声明：[shared_irq_enable](#af36534589858c1e02ea50ed3cc888d41)、[device](../device_reference/P002_设备对象结构.md)、[device](../device_reference/P002_设备对象结构.md)。

为设备启用 ISR。

<a id="r_adcdb9702c30ca0911103fc8b9857abb4"></a>

```c
static int shared_irq_disable (const struct device *dev, const struct device *isr_dev)
```

相关声明：[shared_irq_disable](#adcdb9702c30ca0911103fc8b9857abb4)、[device](../device_reference/P002_设备对象结构.md)、[device](../device_reference/P002_设备对象结构.md)。

为设备禁用 ISR。

## 43.4\_详细说明（Detailed Documentation）

<a id="af6d98f7cd2cde7482b7276aa6e0b487c"></a>

### `isr_t`

```c
typedef int(* isr_t) (const struct device *dev, unsigned int irq_number)
```

<a id="a22cf2ce082fea27f2087cd1abd74934c"></a>

### `shared_irq_disable_t`

```c
typedef int(* shared_irq_disable_t) (const struct device *dev, const struct device *isr_dev)
```

<a id="a0ff7a6ee448eb3e889aa9a7bd63e49bc"></a>

### `shared_irq_enable_t`

```c
typedef int(* shared_irq_enable_t) (const struct device *dev, const struct device *isr_dev)
```

<a id="ae400920b45bedf3da66831597ebca841"></a>

### `shared_irq_register_t`

```c
typedef int(* shared_irq_register_t) (const struct device *dev, isr_t isr_func, const struct device *isr_dev)
```

<a id="adcdb9702c30ca0911103fc8b9857abb4"></a>

### `shared_irq_disable()`

```c
int shared_irq_disable ( const struct device * dev, const struct device * isr_dev )
```

声明属性：`inline`、`static`。

为设备禁用 ISR。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 `SHARED_IRQ` 驱动实例设备结构体的指针。 |
| `isr_dev` | 指向负责处理该中断的设备的指针。 |

<a id="af36534589858c1e02ea50ed3cc888d41"></a>

### `shared_irq_enable()`

```c
int shared_irq_enable ( const struct device * dev, const struct device * isr_dev )
```

声明属性：`inline`、`static`。

为设备启用 ISR。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 `SHARED_IRQ` 驱动实例设备结构体的指针。 |
| `isr_dev` | 指向负责处理该中断的设备的指针。 |

<a id="a6ef6d536da13ebd8aa75830516dc0696"></a>

### `shared_irq_isr_register()`

```c
int shared_irq_isr_register ( const struct device * dev, isr_t isr_func, const struct device * isr_dev )
```

声明属性：`inline`、`static`。

注册设备中断服务程序（ISR）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 `SHARED_IRQ` 驱动实例设备结构体的指针。 |
| `isr_func` | 指向该设备 ISR 函数的指针。 |
| `isr_dev` | 指向负责处理该中断的设备的指针。 |


## 43.5\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_configuration_reference/P100_shared_irq.h_源码浏览.md)
- [shared_irq_driver_api](../platform_security_model_reference/P054_shared_irq_driver_api_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)

<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P042_zephyr__bluetooth__mesh__sar_cfg_cli.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P044_zephyr__sys__speculation.h_文件参考.md)
