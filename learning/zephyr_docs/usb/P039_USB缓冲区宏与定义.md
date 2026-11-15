---
id: learning.zephyr-docs.usb.api-39
title: USB缓冲区宏与定义
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__usb__buf.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第39章\_USB缓冲区宏与定义

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__buf.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 39.1\_阅读说明与来源

译注：本页属于[USB设备控制器API说明](P029_USB设备控制器API说明.md)的底层接口参考，供理解控制器驱动、端点管理和请求生命周期。声明和原注释按官方页面保留，补充解释明确标为源码译注。

[本册大纲](大纲.md)提供本组第29至39章的全部字段参考。

USB 缓冲区宏与定义（USB Buffer Macros and Definitions）。

USB 缓冲区宏与定义（USB Buffer Macros and Definitions）。

引入版本（Since）：4.0。

接口版本（Version）：0.1.1。

## 39.2\_宏定义（Macros）

<a id="r_ga7c04001e0a2fba2d343d7d2eee6aff37"></a>

```c
#define USB_BUF_ALIGN USB_PRIV_BUFALIGN
```

UDC 驱动要求的缓冲区对齐（Alignment）。

相关声明：[USB_BUF_ALIGN](P039_USB缓冲区宏与定义.md#ga7c04001e0a2fba2d343d7d2eee6aff37)。

<a id="r_ga52954c29bc5f64f5e7b8fc3b881a11bf"></a>

```c
#define USB_BUF_GRANULARITY USB_PRIV_BUFGRANULARITY
```

UDC 驱动要求的缓冲区粒度（Granularity）。

相关声明：[USB_BUF_GRANULARITY](P039_USB缓冲区宏与定义.md#ga52954c29bc5f64f5e7b8fc3b881a11bf)。

<a id="r_ga5cfb8cab648a98fbc21ec1edbce057b7"></a>

```c
#define USB_BUF_ROUND_UP(size)
```

按 UDC 驱动要求的粒度向上取整。

相关声明：[USB_BUF_ROUND_UP](P039_USB缓冲区宏与定义.md#ga5cfb8cab648a98fbc21ec1edbce057b7)。

<a id="r_gac3e4ef96b046b995e0365bd3528cd32e"></a>

```c
#define USB_STATIC_BUF_DEFINE(name, size)
```

定义符合 UDC 驱动要求的静态缓冲区。

相关声明：[USB_STATIC_BUF_DEFINE](P039_USB缓冲区宏与定义.md#gac3e4ef96b046b995e0365bd3528cd32e)。

<a id="r_ga07b92466efcdf72a561f50f141f7b0b3"></a>

```c
#define IS_USB_BUF_ALIGNED(buf)
```

检查缓冲区是否满足 UDC 驱动要求的对齐。

相关声明：[IS_USB_BUF_ALIGNED](P039_USB缓冲区宏与定义.md#ga07b92466efcdf72a561f50f141f7b0b3)。

<a id="r_gadad8a14719e700eee228eff922ec6fbd"></a>

```c
#define USB_BUF_POOL_VAR_DEFINE(pname, count, size, ud_size, fdestroy)
```

定义一个采用可变大小载荷（Variable-size Payload）的 UDC 缓冲池。

相关声明：[USB_BUF_POOL_VAR_DEFINE](P039_USB缓冲区宏与定义.md#gadad8a14719e700eee228eff922ec6fbd)。

<a id="r_ga9dd362f9f98bda540c8bafa958345053"></a>

```c
#define USB_BUF_POOL_DEFINE(pname, count, size, ud_size, fdestroy)
```

定义一个采用固定大小数据（Fixed-size Data）的 UDC 缓冲池。

相关声明：[USB_BUF_POOL_DEFINE](P039_USB缓冲区宏与定义.md#ga9dd362f9f98bda540c8bafa958345053)。

<a id="r_gaf53404357b1184c1eda430e92cd696dc"></a>

```c
#define UDC_BUF_ALIGN USB_BUF_ALIGN
```

UDC 驱动要求的缓冲区对齐（Alignment）。

相关声明：[UDC_BUF_ALIGN](P039_USB缓冲区宏与定义.md#gaf53404357b1184c1eda430e92cd696dc)、[USB_BUF_ALIGN](P039_USB缓冲区宏与定义.md#ga7c04001e0a2fba2d343d7d2eee6aff37)。

<a id="r_ga87ea6bf98e8be1ca3378928fbf03bf8e"></a>

```c
#define UDC_BUF_GRANULARITY USB_BUF_GRANULARITY
```

UDC 驱动要求的缓冲区粒度（Granularity）。

相关声明：[UDC_BUF_GRANULARITY](P039_USB缓冲区宏与定义.md#ga87ea6bf98e8be1ca3378928fbf03bf8e)、[USB_BUF_GRANULARITY](P039_USB缓冲区宏与定义.md#ga52954c29bc5f64f5e7b8fc3b881a11bf)。

<a id="r_ga683a98bd402195fd5b57e6b3b9fe6e4a"></a>

```c
#define UDC_ROUND_UP(size)
```

按 UDC 驱动要求的粒度向上取整。

相关声明：[UDC_ROUND_UP](P039_USB缓冲区宏与定义.md#ga683a98bd402195fd5b57e6b3b9fe6e4a)。

<a id="r_gae5cb6affd574da5f4cd0c25e9178a0eb"></a>

```c
#define UDC_STATIC_BUF_DEFINE(name, size)
```

定义符合 UDC 驱动要求的静态缓冲区。

相关声明：[UDC_STATIC_BUF_DEFINE](P039_USB缓冲区宏与定义.md#gae5cb6affd574da5f4cd0c25e9178a0eb)。

<a id="r_ga4e77ceb9142c9d414966f0c4e0eb7710"></a>

```c
#define IS_UDC_ALIGNED(buf)
```

检查缓冲区是否满足 UDC 驱动要求的对齐。

相关声明：[IS_UDC_ALIGNED](P039_USB缓冲区宏与定义.md#ga4e77ceb9142c9d414966f0c4e0eb7710)。

<a id="r_ga064d3f73dbde0f98479ffdad5141e8c0"></a>

```c
#define UDC_BUF_POOL_VAR_DEFINE(pname, count, size, ud_size, fdestroy)
```

定义一个采用固定大小数据（Fixed-size Data）的 UDC 缓冲池。

相关声明：[UDC_BUF_POOL_VAR_DEFINE](P039_USB缓冲区宏与定义.md#ga064d3f73dbde0f98479ffdad5141e8c0)。

<a id="r_gac96f1518df5748927c3377cb3abc222d"></a>

```c
#define UDC_BUF_POOL_DEFINE(pname, count, size, ud_size, fdestroy)
```

定义一个采用固定大小数据（Fixed-size Data）的 UDC 缓冲池。

相关声明：[UDC_BUF_POOL_DEFINE](P039_USB缓冲区宏与定义.md#gac96f1518df5748927c3377cb3abc222d)。

## 39.3\_详细说明（Detailed Documentation）

<a id="ga4e77ceb9142c9d414966f0c4e0eb7710"></a>

### `IS_UDC_ALIGNED`

```c
#define IS_UDC_ALIGNED ( buf)
```

```c
#include <zephyr/drivers/usb/usb_buf.h>
```

**宏展开值（Value）**

```c
IS_USB_BUF_ALIGNED(buf)
```

检查缓冲区是否满足 UDC 驱动要求的对齐。

**参阅（See Also）**：IS_UDC_ALIGNED。

> 译注（源码核对）：原参阅条目指向本宏自身；实际展开转发到 IS_USB_BUF_ALIGNED，后者只检查地址对齐，不能据此推断缓冲容量、DMA可达性或缓存一致性均已满足。

<a id="ga07b92466efcdf72a561f50f141f7b0b3"></a>

### `IS_USB_BUF_ALIGNED`

```c
#define IS_USB_BUF_ALIGNED ( buf)
```

```c
#include <zephyr/drivers/usb/usb_buf.h>
```

**宏展开值（Value）**

```c
IS_ALIGNED(buf, USB_BUF_ALIGN)
```

检查缓冲区是否满足 UDC 驱动要求的对齐。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 缓冲区指针。 |

**参阅（See Also）**：IS_ALIGNED。

<a id="gaf53404357b1184c1eda430e92cd696dc"></a>

### `UDC_BUF_ALIGN`

```c
#define UDC_BUF_ALIGN USB_BUF_ALIGN
```

```c
#include <zephyr/drivers/usb/usb_buf.h>
```

UDC 驱动要求的缓冲区对齐（Alignment）。

**参阅（See Also）**：USB_BUF_ALIGN。

<a id="ga87ea6bf98e8be1ca3378928fbf03bf8e"></a>

### `UDC_BUF_GRANULARITY`

```c
#define UDC_BUF_GRANULARITY USB_BUF_GRANULARITY
```

```c
#include <zephyr/drivers/usb/usb_buf.h>
```

UDC 驱动要求的缓冲区粒度（Granularity）。

**参阅（See Also）**：USB_BUF_GRANULARITY。

<a id="gac96f1518df5748927c3377cb3abc222d"></a>

### `UDC_BUF_POOL_DEFINE`

```c
#define UDC_BUF_POOL_DEFINE ( pname, count, size, ud_size, fdestroy )
```

```c
#include <zephyr/drivers/usb/usb_buf.h>
```

**宏展开值（Value）**

```c
USB_BUF_POOL_DEFINE(pname, count, size, ud_size, fdestroy)
```

定义一个采用固定大小数据（Fixed-size Data）的 UDC 缓冲池。

**参阅（See Also）**：USB_BUF_POOL_DEFINE。

<a id="ga064d3f73dbde0f98479ffdad5141e8c0"></a>

### `UDC_BUF_POOL_VAR_DEFINE`

```c
#define UDC_BUF_POOL_VAR_DEFINE ( pname, count, size, ud_size, fdestroy )
```

```c
#include <zephyr/drivers/usb/usb_buf.h>
```

**宏展开值（Value）**

```c
USB_BUF_POOL_VAR_DEFINE(pname, count, size, ud_size, fdestroy)
```

定义一个采用固定大小数据（Fixed-size Data）的 UDC 缓冲池。

**参阅（See Also）**：USB_BUF_POOL_VAR_DEFINE。

> 译注（源码核对）：此别名原注释称“固定大小”，但实际展开到 USB_BUF_POOL_VAR_DEFINE，使用可变大小载荷。这里保留原注释并以展开式纠正分类。

<a id="ga683a98bd402195fd5b57e6b3b9fe6e4a"></a>

### `UDC_ROUND_UP`

```c
#define UDC_ROUND_UP ( size)
```

```c
#include <zephyr/drivers/usb/usb_buf.h>
```

**宏展开值（Value）**

```c
USB_BUF_ROUND_UP(size)
```

按 UDC 驱动要求的粒度向上取整。

**参阅（See Also）**：USB_BUF_ROUND_UP。

<a id="gae5cb6affd574da5f4cd0c25e9178a0eb"></a>

### `UDC_STATIC_BUF_DEFINE`

```c
#define UDC_STATIC_BUF_DEFINE ( name, size )
```

```c
#include <zephyr/drivers/usb/usb_buf.h>
```

**宏展开值（Value）**

```c
USB_STATIC_BUF_DEFINE(name, size)
```

定义符合 UDC 驱动要求的静态缓冲区。

**参阅（See Also）**：USB_STATIC_BUF_DEFINE。

<a id="ga7c04001e0a2fba2d343d7d2eee6aff37"></a>

### `USB_BUF_ALIGN`

```c
#define USB_BUF_ALIGN USB_PRIV_BUFALIGN
```

```c
#include <zephyr/drivers/usb/usb_buf.h>
```

UDC 驱动要求的缓冲区对齐（Alignment）。

> 译注（源码核对）：当前内部宏在定义 CONFIG_DCACHE_LINE_SIZE 且未强制放入非缓存区时，使用数据缓存行大小作为对齐与粒度；否则采用 sizeof(void *)。源码明确指出DMA可访问区域和缓存属性的信息仍不统一，这些宏并不证明任意地址都适合DMA。

<a id="ga52954c29bc5f64f5e7b8fc3b881a11bf"></a>

### `USB_BUF_GRANULARITY`

```c
#define USB_BUF_GRANULARITY USB_PRIV_BUFGRANULARITY
```

```c
#include <zephyr/drivers/usb/usb_buf.h>
```

UDC 驱动要求的缓冲区粒度（Granularity）。

<a id="ga9dd362f9f98bda540c8bafa958345053"></a>

### `USB_BUF_POOL_DEFINE`

```c
#define USB_BUF_POOL_DEFINE ( pname, count, size, ud_size, fdestroy )
```

```c
#include <zephyr/drivers/usb/usb_buf.h>
```

**宏展开值（Value）**

```c
_NET_BUF_ARRAY_DEFINE(pname, count, ud_size);                           \
BUILD_ASSERT((USB_BUF_GRANULARITY) % (USB_BUF_ALIGN) == 0,              \
             "Code assumes granurality is multiple of alignment");      \
static uint8_t USB_PRIV_BUFSECTION __aligned(USB_BUF_ALIGN)             \
        net_buf_data_##pname[count][USB_BUF_ROUND_UP(size)];            \
static const struct net_buf_pool_fixed net_buf_fixed_##pname = {        \
        .data_pool = (uint8_t *)net_buf_data_##pname,                   \
};                                                                      \
static const struct net_buf_data_alloc net_buf_fixed_alloc_##pname = {  \
        .cb = &net_buf_fixed_cb,                                        \
        .alloc_data = (void *)&net_buf_fixed_##pname,                   \
        .max_alloc_size = USB_BUF_ROUND_UP(size),                       \
};                                                                      \
static STRUCT_SECTION_ITERABLE(net_buf_pool, pname) =                   \
        NET_BUF_POOL_INITIALIZER(pname, &net_buf_fixed_alloc_##pname,   \
                                 _net_buf_##pname, count, ud_size,      \
                                 fdestroy)
```

定义一个采用固定大小数据（Fixed-size Data）的 UDC 缓冲池。

此宏类似于 NET_BUF_POOL_DEFINE，但提供适用于 UDC 驱动的缓冲区对齐和粒度。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pname` | 缓冲池变量名称。 |
| `count` | 池中缓冲区数量。 |
| `size` | 每个缓冲区的最大数据载荷。 |
| `ud_size` | 为每个缓冲区预留的用户数据空间。 |
| `fdestroy` | 可选的销毁回调（Destroy Callback），在缓冲区释放时调用。 |

**参阅（See Also）**：NET_BUF_POOL_DEFINE。

> 译注（源码核对）：当前固定大小宏按 count 创建数据槽，每槽容量为 USB_BUF_ROUND_UP(size)，并断言粒度是对齐的整数倍。ud_size 用于各 net_buf 的用户元数据区，不等于传输载荷长度。

<a id="gadad8a14719e700eee228eff922ec6fbd"></a>

### `USB_BUF_POOL_VAR_DEFINE`

```c
#define USB_BUF_POOL_VAR_DEFINE ( pname, count, size, ud_size, fdestroy )
```

```c
#include <zephyr/drivers/usb/usb_buf.h>
```

**宏展开值（Value）**

```c
_NET_BUF_ARRAY_DEFINE(pname, count, ud_size);                           \
USB_BUF_K_HEAP_DEFINE(net_buf_mem_pool_##pname, size);                  \
static const struct net_buf_data_alloc net_buf_data_alloc_##pname = {   \
        .cb = &net_buf_dma_cb,                                          \
        .alloc_data = &net_buf_mem_pool_##pname,                        \
        .max_alloc_size = 0,                                            \
};                                                                      \
static STRUCT_SECTION_ITERABLE(net_buf_pool, pname) =                   \
        NET_BUF_POOL_INITIALIZER(pname, &net_buf_data_alloc_##pname,    \
                                 _net_buf_##pname, count, ud_size,      \
                                 fdestroy)
```

定义一个采用可变大小载荷（Variable-size Payload）的 UDC 缓冲池。

此宏类似于 NET_BUF_POOL_VAR_DEFINE，但提供适用于 UDC 驱动的缓冲区对齐和粒度。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pname` | 缓冲池变量名称。 |
| `count` | 池中缓冲区数量。 |
| `size` | 每个缓冲区的最大数据载荷。 |
| `ud_size` | 为每个缓冲区预留的用户数据空间。 |
| `fdestroy` | 可选的销毁回调（Destroy Callback），在缓冲区释放时调用。 |

**参阅（See Also）**：NET_BUF_POOL_VAR_DEFINE。

> 译注（源码核对）：原参数说明把 size 称为每个缓冲区最大载荷，但当前宏将 size 传入 USB_BUF_K_HEAP_DEFINE，作为共享数据堆大小，而 count 控制 net_buf 对象数量；它不会为每个对象分别分配 size 字节的固定数据区。实际可分配容量还受堆元数据、对齐和同时在用的载荷影响。

<a id="ga5cfb8cab648a98fbc21ec1edbce057b7"></a>

### `USB_BUF_ROUND_UP`

```c
#define USB_BUF_ROUND_UP ( size)
```

```c
#include <zephyr/drivers/usb/usb_buf.h>
```

**宏展开值（Value）**

```c
ROUND_UP(size, USB_PRIV_BUFGRANULARITY)
```

按 UDC 驱动要求的粒度向上取整。

<a id="gac3e4ef96b046b995e0365bd3528cd32e"></a>

### `USB_STATIC_BUF_DEFINE`

```c
#define USB_STATIC_BUF_DEFINE ( name, size )
```

```c
#include <zephyr/drivers/usb/usb_buf.h>
```

**宏展开值（Value）**

```c
static uint8_t USB_PRIV_BUFSECTION __aligned(USB_BUF_ALIGN)             \
name[USB_BUF_ROUND_UP(size)];
```

定义符合 UDC 驱动要求的静态缓冲区。

如果应用自行定义用于 USB 传输的缓冲区，应使用此宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 缓冲区名称。 |
| `size` | 缓冲区大小。 |

> 译注（源码核对）：当前展开同时指定静态存储、对齐和向上取整后的数组容量；启用控制器的强制非缓存配置时还放入 __nocache 区段。使用该宏不能代替具体驱动的缓存同步与可访问内存检查。

## 39.4\_缓冲区源码

本页宏定义来自[本仓库 usb_buf.h](../../../include/zephyr/drivers/usb/usb_buf.h)，核对依据为保存的[官方 usb_buf.h](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/drivers/usb/usb_buf.h)。

## 39.5\_相关源码与使用边界

控制器接口与结构定义来自 `zephyr/drivers/usb/udc.h`，缓冲区宏来自 `zephyr/drivers/usb/usb_buf.h`。本仓库的[对应头文件](../../../include/zephyr/drivers/usb/udc.h)、[公共实现](../../../drivers/usb/udc/udc_common.c)、[内部辅助接口](../../../drivers/usb/udc/udc_common.h)和[驱动骨架](../../../drivers/usb/udc/udc_skeleton.c)可用于源码跟踪；版本可能与官方 latest 不同。译注依据保存的[官方头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/drivers/usb/udc.h)、[公共实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/usb/udc/udc_common.c)、[内部接口](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/usb/udc/udc_common.h)及[骨架实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/usb/udc/udc_skeleton.c)，摘要见[来源记录](../SOURCES.md)。本批没有编译、运行或操作USB设备。

<a id="header-define-members"></a>
<a id="define-members"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__usb__buf_html_ga07b92466efcdf72a561f50f141f7b0b3"></a>
<a id="agroup__sys-util_html_gabf601ce26a569512a4e422a074934660"></a>
<a id="agroup__usb__buf_html_ga7c04001e0a2fba2d343d7d2eee6aff37"></a>
<a id="agroup__usb__buf_html_ga9dd362f9f98bda540c8bafa958345053"></a>
<a id="agroup__usb__buf_html_gadad8a14719e700eee228eff922ec6fbd"></a>
<a id="agroup__usb__buf_html_ga5cfb8cab648a98fbc21ec1edbce057b7"></a>
<a id="agroup__usb__buf_html_gac3e4ef96b046b995e0365bd3528cd32e"></a>
<a id="agroup__iterable__section__apis_html_ga9104f42cbe4a67a931bed7f7cc8f600f"></a>
<a id="agroup__usb__buf_html_ga52954c29bc5f64f5e7b8fc3b881a11bf"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructnet__buf__pool_html"></a>
<a id="agroup__sys-util_html_gaada5610108b15d85c65d863b0c646ef3"></a>

[上一章](P038_USB设备控制器事件结构.md) · [返回大纲](大纲.md) · [下一章](P040_HID通用说明.md)
