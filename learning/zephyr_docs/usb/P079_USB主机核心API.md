---
id: learning.zephyr-docs.usb.api-79
title: USB主机核心API
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__usb__host__core__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第79章\_USB主机核心API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__host__core__api.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 79.1\_阅读说明与来源

译注：本页说明USB主机栈（USB Host Stack）的接口与数据对象。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

USB主机核心层API（USB Host Core Layer API）。

USB主机核心层API（USB Host Core Layer API）。

引入版本（Since）：3.3。

接口版本（Version）：0.1.0。

## 79.2\_数据结构（Data Structures）

<a id="r_usbh_5Fstatus"></a>

```c
struct usbh_status
```

USB主机支持状态。

相关声明：[usbh_status](P084_USB主机状态.md)。

<a id="r_usbh_5Fcontext"></a>

```c
struct usbh_context
```

USB主机支持的运行时上下文（Runtime Context）。

相关声明：[usbh_context](P083_USB主机上下文.md)。

<a id="r_usbh_5Fclass_5Ffilter"></a>

```c
struct usbh_class_filter
```

与匹配特定类有关的设备信息。

相关声明：[usbh_class_filter](P087_USB主机类匹配条件.md)。

<a id="r_usbh_5Fclass_5Fapi"></a>

```c
struct usbh_class_api
```

USB主机类实例API。

相关声明：[usbh_class_api](P085_USB主机类驱动接口.md)。

<a id="r_usbh_5Fclass_5Fdata"></a>

```c
struct usbh_class_data
```

USB主机类实例数据。

相关声明：[usbh_class_data](P086_USB主机类驱动数据.md)。

## 79.3\_宏定义（Macros）

<a id="r_ga0a8885f9c6e8371ccc02ce191d010010"></a>

```c
#define USBH_CONTROLLER_DEFINE(device_name, uhc_dev)
```



相关声明：[USBH_CONTROLLER_DEFINE](P079_USB主机核心API.md#ga0a8885f9c6e8371ccc02ce191d010010)。

<a id="r_gac517efa196831699a3fc261453dfe16f"></a>

```c
#define USBH_DEFINE_CLASS(class_name, class_api, class_priv, filt)
```

定义USB主机支持的类数据。

相关声明：[USBH_DEFINE_CLASS](P079_USB主机核心API.md#gac517efa196831699a3fc261453dfe16f)。

## 79.4\_函数（Functions）

<a id="r_ga9a0b6b3d13573de570a95985450fa869"></a>

```c
int usbh_init (struct usbh_context *uhs_ctx)
```

初始化USB主机支持。

相关声明：[usbh_init](P079_USB主机核心API.md#ga9a0b6b3d13573de570a95985450fa869)、[usbh_context](P083_USB主机上下文.md)。

<a id="r_ga799fa25976930bb2ec39f351f91321ff"></a>

```c
int usbh_enable (struct usbh_context *uhs_ctx)
```

启用USB主机支持及类实例。

相关声明：[usbh_enable](P079_USB主机核心API.md#ga799fa25976930bb2ec39f351f91321ff)、[usbh_context](P083_USB主机上下文.md)。

<a id="r_ga9f5874fb7d02f323f389b079a677372f"></a>

```c
int usbh_disable (struct usbh_context *uhs_ctx)
```

停用USB主机支持。

相关声明：[usbh_disable](P079_USB主机核心API.md#ga9f5874fb7d02f323f389b079a677372f)、[usbh_context](P083_USB主机上下文.md)。

<a id="r_gafa107bce1b2c0af5618f5cc6345a17e2"></a>

```c
int usbh_shutdown (struct usbh_context *const uhs_ctx)
```

关闭USB主机支持。

相关声明：[usbh_shutdown](P079_USB主机核心API.md#gafa107bce1b2c0af5618f5cc6345a17e2)、[usbh_context](P083_USB主机上下文.md)。

## 79.5\_详细说明（Detailed Documentation）

<a id="ga0a8885f9c6e8371ccc02ce191d010010"></a>

### 79.5.1\_`USBH\_CONTROLLER\_DEFINE`

```c
#define USBH_CONTROLLER_DEFINE ( device_name, uhc_dev )
```

```c
#include <zephyr/usb/usbh.h>
```

**宏展开值（Value）**

```c
SYS_BITARRAY_DEFINE_STATIC(ba_##device_name, 128);              \
static STRUCT_SECTION_ITERABLE(usbh_context, device_name) = {   \
        .name = STRINGIFY(device_name),                         \
        .mutex = Z_MUTEX_INITIALIZER(device_name.mutex),        \
        .dev = uhc_dev,                                         \
        .addr_ba = &ba_##device_name,                           \
}
```

> 译注（源码核对）：宏建立128位设备地址位数组，并将静态usbh_context放入可迭代段（Iterable Section），设置名称、互斥锁、UHC设备及地址表；它不自动执行usbh_init或usbh_enable。运行时设备地址分配使用1至127，地址0不从该循环分配。

<a id="gac517efa196831699a3fc261453dfe16f"></a>

### 79.5.2\_`USBH\_DEFINE\_CLASS`

```c
#define USBH_DEFINE_CLASS ( class_name, class_api, class_priv, filt )
```

```c
#include <zephyr/usb/usbh.h>
```

**宏展开值（Value）**

```c
static struct usbh_class_data UTIL_CAT(class_data_, class_name) = {     \
        .name = STRINGIFY(class_name),                                  \
        .api = class_api,                                               \
        .priv = class_priv,                                             \
};                                                                      \
static STRUCT_SECTION_ITERABLE(usbh_class_node, class_name) = {         \
        .c_data = &UTIL_CAT(class_data_, class_name),                   \
        .filters = filt,                                                \
};
```

定义USB主机支持的类数据。

此宏定义类（功能）数据，以及栈内部使用的对应节点结构。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] class_name` | 类名称 |
| `[in] class_api` | 指向usbh_class_api结构的指针 |
| `[in] class_priv` | 类私有数据 |
| `[in] filt` | 用于匹配此类的usbh_class_filter数组；传入NULL表示匹配所有对象。非NULL时，数组必须以flags为0的条目结束。 |

> 译注（源码核对）：宏保存回调表、私有数据与过滤器指针，并创建栈内部节点，不复制这些指针所指对象。过滤器为NULL时不做字段筛选，但仍须通过probe；非NULL数组以flags=0结束，该结束项不表示匹配所有对象。每个类实例一次绑定一个设备功能，需要并发服务多个功能时须考虑实例数量。

<a id="ga9f5874fb7d02f323f389b079a677372f"></a>

### 79.5.3\_`usbh\_disable()`

```c
int usbh_disable ( struct usbh_context * uhs_ctx)
```

```c
#include <zephyr/usb/usbh.h>
```

停用USB主机支持。

此函数停用USB主机支持。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] uhs_ctx` | 指向USB主机支持上下文的指针 |

**返回（Returns）**：成功为0，失败为其他值。

> 译注（源码核对）：当前实现发现控制器已停用时直接返回0；调用uhc_disable失败时只记录错误日志，最后仍返回0。不能把此函数的返回0单独当作底层硬件已成功停用的证据。

<a id="ga799fa25976930bb2ec39f351f91321ff"></a>

### 79.5.4\_`usbh\_enable()`

```c
int usbh_enable ( struct usbh_context * uhs_ctx)
```

```c
#include <zephyr/usb/usbh.h>
```

启用USB主机支持及类实例。

此函数启用USB主机支持。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] uhs_ctx` | 指向USB主机支持上下文的指针 |

**返回（Returns）**：成功为0，失败为其他值。

> 译注（源码核对）：当前实现检查UHC是否初始化和是否已启用，分别可能返回-EPERM或-EALREADY，然后转发uhc_enable。函数返回不表示设备枚举、配置选择或类匹配已经完成。

<a id="ga9a0b6b3d13573de570a95985450fa869"></a>

### 79.5.5\_`usbh\_init()`

```c
int usbh_init ( struct usbh_context * uhs_ctx)
```

```c
#include <zephyr/usb/usbh.h>
```

初始化USB主机支持。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] uhs_ctx` | 指向USB主机支持上下文的指针 |

**返回（Returns）**：成功为0，失败为其他值。

> 译注（源码核对）：当前实现先检查UHC设备是否就绪，未就绪返回-ENODEV；控制器已初始化返回-EALREADY。成功时通过内部入口注册事件载体并初始化设备链表。类实例的init由主机子系统预初始化阶段调用，不是在每次usbh_init时重复初始化。

<a id="gafa107bce1b2c0af5618f5cc6345a17e2"></a>

### 79.5.6\_`usbh\_shutdown()`

```c
int usbh_shutdown ( struct usbh_context *const uhs_ctx)
```

```c
#include <zephyr/usb/usbh.h>
```

关闭USB主机支持。

此函数完全停用USB主机支持。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] uhs_ctx` | 指向USB主机支持上下文的指针 |

**返回（Returns）**：成功为0，失败为其他值。

> 译注（源码核对）：当前实现调用并返回uhc_shutdown结果，不先调用disable；控制器仍启用时底层会返回-EBUSY。关闭主机支持不等于已通过此函数完成每个设备的移除回调和资源释放，须按实际连接与清理流程核对。

## 79.6\_源码跟踪与使用边界

译注依据保存的[官方主机头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/usbh.h)、[UHC头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/drivers/usb/uhc.h)、[生命周期实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_api.c)、[类匹配实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_class.c)、[类回调包装](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_class_api.h)、[设备管理](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_device.c)及[事件处理](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_core.c)，摘要见[来源记录](../SOURCES.md)。本仓库的[主机头文件](../../../include/zephyr/usb/usbh.h)、[UHC头文件](../../../include/zephyr/drivers/usb/uhc.h)与[主机栈目录](../../../subsys/usb/host)可用于源码跟踪，版本可能与网页不同。本批未构建、运行或操作USB硬件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>
<a id="header-define-members"></a>
<a id="define-members"></a>
<a id="header-func-members"></a>
<a id="func-members"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__bitarray__apis_html_ga2c55680355b67fc25125299a35f604d1"></a>
<a id="agroup__iterable__section__apis_html_ga9104f42cbe4a67a931bed7f7cc8f600f"></a>
<a id="astructusbh__context_html"></a>
<a id="astructusbh__class__data_html"></a>
<a id="autil__internal_8h_html_a7e7766e792d1638bfbbc9d0f328d3d0d"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

[上一章](P078_USB主机栈头文件接口.md) · [返回大纲](大纲.md) · [下一章](P080_USB主机设备对象.md)
