---
id: learning.zephyr-docs.api-network-time-topic-reference.page-23
title: NXP FlexIO API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__nxp__flexio__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第23章\_NXP FlexIO API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__nxp__flexio__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

NXP FlexIO 接口。

<a id="details"></a>

NXP FlexIO 接口。

<a id="header-files"></a>
<a id="files"></a>

## 23.1\_文件（Files）

<a id="r_nxp_5Fflexio_2Eh"></a>

```c
file nxp_flexio.h
```

相关声明：[nxp_flexio.h](../api_file_system_device_reference/P033_zephyr__drivers__misc__nxp_flexio__nxp_flexio.h_文件参考.md)。

NXP FlexIO驱动的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 23.2\_数据结构（Data Structures）

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

## 23.3\_类型定义（Typedefs）

<a id="r_gaf11959c4e7c7a5ef56b082fcf0b7f42c"></a>

```c
typedef int(* nxp_flexio_child_isr_t) (void *user_data)
```

相关声明：[nxp_flexio_child_isr_t](#gaf11959c4e7c7a5ef56b082fcf0b7f42c)。

用于通知 API 用户 FlexIO 已触发中断的回调 API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 23.4\_函数（Functions）

<a id="r_ga7e84a09852b713337d6e124eb2b8df7d"></a>

```c
void nxp_flexio_irq_enable (const struct device *dev)
```

相关声明：[nxp_flexio_irq_enable](#ga7e84a09852b713337d6e124eb2b8df7d)、[device](../device_reference/P002_设备对象结构.md)。

启用 FlexIO 中断请求（IRQ）。

<a id="r_ga39b6b8b2eda354b4d3a40da48f41e3d2"></a>

```c
void nxp_flexio_irq_disable (const struct device *dev)
```

相关声明：[nxp_flexio_irq_disable](#ga39b6b8b2eda354b4d3a40da48f41e3d2)、[device](../device_reference/P002_设备对象结构.md)。

禁用 FlexIO IRQ。

<a id="r_ga3be561d6ee29eb0e23f67ddcf234d22e"></a>

```c
void nxp_flexio_lock (const struct device *dev)
```

相关声明：[nxp_flexio_lock](#ga3be561d6ee29eb0e23f67ddcf234d22e)、[device](../device_reference/P002_设备对象结构.md)。

锁定 FlexIO 互斥锁（mutex）。

<a id="r_gab5ff53d4ac41321fe4726e2ede175ac2"></a>

```c
void nxp_flexio_unlock (const struct device *dev)
```

相关声明：[nxp_flexio_unlock](#gab5ff53d4ac41321fe4726e2ede175ac2)、[device](../device_reference/P002_设备对象结构.md)。

解锁 FlexIO 互斥锁。

<a id="r_ga9c5fdb0b5b11dcc04d42c2c7b98b3ffb"></a>

```c
int nxp_flexio_get_rate (const struct device *dev, uint32_t *rate)
```

相关声明：[nxp_flexio_get_rate](#ga9c5fdb0b5b11dcc04d42c2c7b98b3ffb)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取 FlexIO 所用子系统的时钟频率（clock rate）。

<a id="r_ga1208ad4ef70419ff61a87b8b1ff8d446"></a>

```c
int nxp_flexio_child_attach (const struct device *dev, const struct nxp_flexio_child *child)
```

相关声明：[nxp_flexio_child_attach](#ga1208ad4ef70419ff61a87b8b1ff8d446)、[device](../device_reference/P002_设备对象结构.md)、[nxp_flexio_child](../platform_security_model_reference/P020_nxp_flexio_child_结构体.md)。

将 FlexIO 子设备附接到 FlexIO 控制器。

## 23.5\_详细说明（Detailed Documentation）

<a id="gaf11959c4e7c7a5ef56b082fcf0b7f42c"></a>

### `nxp_flexio_child_isr_t`

```c
typedef int(* nxp_flexio_child_isr_t) (void *user_data)
```

```c
#include <zephyr/drivers/misc/nxp_flexio/nxp_flexio.h>
```

用于通知 API 用户 FlexIO 已触发中断的回调 API。

每当子设备映射的任一移位器（shifter）或定时器出现已使能且挂起的中断时，控制器都会从 IRQ 上下文调用此函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `user_data` | 附接（attachment）时提供的不透明指针（opaque pointer）。 |

<a id="ga1208ad4ef70419ff61a87b8b1ff8d446"></a>

### `nxp_flexio_child_attach()`

```c
int nxp_flexio_child_attach ( const struct device * dev, const struct nxp_flexio_child * child )
```

```c
#include <zephyr/drivers/misc/nxp_flexio/nxp_flexio.h>
```

将 FlexIO 子设备附接到 FlexIO 控制器。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 FlexIO 驱动实例设备结构体的指针。 |
| `child` | 指向 FlexIO 子设备的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-ENOBUFS` | 可用资源不足时。 |

<a id="ga9c5fdb0b5b11dcc04d42c2c7b98b3ffb"></a>

### `nxp_flexio_get_rate()`

```c
int nxp_flexio_get_rate ( const struct device * dev, uint32_t * rate )
```

```c
#include <zephyr/drivers/misc/nxp_flexio/nxp_flexio.h>
```

获取 FlexIO 所用子系统的时钟频率（clock rate）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` dev` | 指向 FlexIO 驱动实例设备结构体的指针。 |
| `[out] rate` | 子系统时钟频率（subsystem clock rate）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功读取频率时。 |
| `-EAGAIN` | 无法读取频率时。某些驱动在时钟关闭时不支持返回频率。 |
| `-ENOTSUP` | 不支持读取指定子系统的时钟频率时。 |
| `-ENOSYS` | 未实现此接口时。 |

<a id="ga39b6b8b2eda354b4d3a40da48f41e3d2"></a>

### `nxp_flexio_irq_disable()`

```c
void nxp_flexio_irq_disable ( const struct device * dev)
```

```c
#include <zephyr/drivers/misc/nxp_flexio/nxp_flexio.h>
```

禁用 FlexIO IRQ。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 FlexIO 驱动实例设备结构体的指针。 |

<a id="ga7e84a09852b713337d6e124eb2b8df7d"></a>

### `nxp_flexio_irq_enable()`

```c
void nxp_flexio_irq_enable ( const struct device * dev)
```

```c
#include <zephyr/drivers/misc/nxp_flexio/nxp_flexio.h>
```

启用 FlexIO 中断请求（IRQ）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 FlexIO 驱动实例设备结构体的指针。 |

<a id="ga3be561d6ee29eb0e23f67ddcf234d22e"></a>

### `nxp_flexio_lock()`

```c
void nxp_flexio_lock ( const struct device * dev)
```

```c
#include <zephyr/drivers/misc/nxp_flexio/nxp_flexio.h>
```

锁定 FlexIO 互斥锁（mutex）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 FlexIO 驱动实例设备结构体的指针。 |

<a id="gab5ff53d4ac41321fe4726e2ede175ac2"></a>

### `nxp_flexio_unlock()`

```c
void nxp_flexio_unlock ( const struct device * dev)
```

```c
#include <zephyr/drivers/misc/nxp_flexio/nxp_flexio.h>
```

解锁 FlexIO 互斥锁。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 FlexIO 驱动实例设备结构体的指针。 |


## 23.6\_原页交叉引用（Cross References）

- [nxp_flexio.h](../api_file_system_device_reference/P033_zephyr__drivers__misc__nxp_flexio__nxp_flexio.h_文件参考.md)
- [nxp_flexio_child_res](../platform_security_model_reference/P021_nxp_flexio_child_res_结构体.md)
- [nxp_flexio_child](../platform_security_model_reference/P020_nxp_flexio_child_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P022_网络时间表示（Network time representation）。.md) · [返回大纲](大纲.md) · [下一章](P024_基础协议（Base Protocol）.md)
