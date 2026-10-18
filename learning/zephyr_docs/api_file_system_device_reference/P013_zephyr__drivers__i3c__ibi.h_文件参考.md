---
id: learning.zephyr-docs.api-file-system-device-reference.page-13
title: zephyr__drivers__i3c__ibi.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ibi_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_zephyr\_\_drivers\_\_i3c\_\_ibi.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ibi_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stdint.h>
#include <zephyr/device.h>
#include <zephyr/kernel.h>
#include <zephyr/sys/slist.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 13.1\_数据结构（Data Structures）

<a id="r_i3c_5Fibi"></a>

```c
struct i3c_ibi
```

相关声明：[i3c_ibi](../hardware/P397_I3C带内中断请求.md)。

带内中断（IBI）请求的结构。

<a id="r_i3c_5Fibi_5Fpayload"></a>

```c
struct i3c_ibi_payload
```

相关声明：[i3c_ibi_payload](../hardware/P398_I3C带内中断载荷.md)。

带内中断（IBI）载荷缓冲区的结构。

<a id="r_i3c_5Fibi_5Fwork"></a>

```c
struct i3c_ibi_work
```

相关声明：[i3c_ibi_work](../hardware/P399_I3C带内中断工作项.md)。

已排队的带内中断（IBI）的节点。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 13.2\_宏定义（Macros）

<a id="r_ga7bbbff351dc33d1c00abf6c22bbd50d4"></a>

```c
#define CONFIG_I3C_IBI_MAX_PAYLOAD_SIZE 0
```

相关声明：[CONFIG_I3C_IBI_MAX_PAYLOAD_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#ga7bbbff351dc33d1c00abf6c22bbd50d4)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 13.3\_类型定义（Typedefs）

<a id="r_ga814cf622b240808216ce4e87802e965c"></a>

```c
typedef int(* i3c_target_ibi_cb_t) (struct i3c_device_desc *target, struct i3c_ibi_payload *payload)
```

相关声明：[i3c_target_ibi_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#ga814cf622b240808216ce4e87802e965c)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[i3c_ibi_payload](../hardware/P398_I3C带内中断载荷.md)。

收到目标设备的带内中断（In-Band Interrupt，IBI）时调用的函数。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 13.4\_枚举（Enumerations）

<a id="r_gaf4be72fc9c862d996d860c0b7fbc862b"></a>

```c
enum i3c_ibi_type { I3C_IBI_TARGET_INTR , I3C_IBI_CONTROLLER_ROLE_REQUEST , I3C_IBI_HOTJOIN , I3C_IBI_TYPE_MAX = I3C_IBI_HOTJOIN , I3C_IBI_WORKQUEUE_CB }
```

相关声明：[i3c_ibi_type](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#gaf4be72fc9c862d996d860c0b7fbc862b)、[I3C_IBI_TARGET_INTR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#ggaf4be72fc9c862d996d860c0b7fbc862ba368e8ad08a003ebf197add6d73ffd43d)、[I3C_IBI_CONTROLLER_ROLE_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#ggaf4be72fc9c862d996d860c0b7fbc862ba00235d326559f945d54638b0c0558815)、[I3C_IBI_HOTJOIN](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#ggaf4be72fc9c862d996d860c0b7fbc862ba493d3b1e9669434c3d62f16aa3d6f92f)、[I3C_IBI_TYPE_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#ggaf4be72fc9c862d996d860c0b7fbc862baab12781f76c743cec6b72ffa7d8c27ee)、[I3C_IBI_WORKQUEUE_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#ggaf4be72fc9c862d996d860c0b7fbc862ba39d8f6a9b69d092eabf9ca9726deec8c)。

带内中断（IBI）类型。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 13.5\_函数（Functions）

<a id="r_gaafc2fdf9f2402691c3ebe11d06106840"></a>

```c
int i3c_ibi_work_enqueue (struct i3c_ibi_work *ibi_work)
```

相关声明：[i3c_ibi_work_enqueue](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#gaafc2fdf9f2402691c3ebe11d06106840)、[i3c_ibi_work](../hardware/P399_I3C带内中断工作项.md)。

将 IBI 工作项（work item）加入队列，以便稍后处理。

<a id="r_ga7fbf838ea07516849dc1296d48af65d1"></a>

```c
int i3c_ibi_work_enqueue_target_irq (struct i3c_device_desc *target, uint8_t *payload, size_t payload_len)
```

相关声明：[i3c_ibi_work_enqueue_target_irq](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#ga7fbf838ea07516849dc1296d48af65d1)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将目标中断（target interrupt）IBI 加入队列，以便稍后处理。

<a id="r_gad643c7f0512e1e6dcddbe5821e70fc0d"></a>

```c
int i3c_ibi_work_enqueue_controller_request (struct i3c_device_desc *target)
```

相关声明：[i3c_ibi_work_enqueue_controller_request](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#gad643c7f0512e1e6dcddbe5821e70fc0d)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)。

将控制器角色请求（controllership request）IBI 加入队列，以便稍后处理。

<a id="r_gab135cb893efd50c7db16c1734b6a0bab"></a>

```c
int i3c_ibi_work_enqueue_hotjoin (const struct device *dev)
```

相关声明：[i3c_ibi_work_enqueue_hotjoin](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#gab135cb893efd50c7db16c1734b6a0bab)、[device](../device_reference/P002_设备对象结构.md)。

将热加入（hot join）IBI 加入队列，以便稍后处理。

<a id="r_ga4c6f4516e55d0ab6c539fb800d7ec45a"></a>

```c
int i3c_ibi_work_enqueue_cb (const struct device *dev, k_work_handler_t work_cb)
```

相关声明：[i3c_ibi_work_enqueue_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#ga4c6f4516e55d0ab6c539fb800d7ec45a)、[device](../device_reference/P002_设备对象结构.md)、[k_work_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga5add9ef0dce306a08413c4140fc0bdda)。

将通用回调加入队列，以便稍后处理。


## 13.6\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/sys/slist.h](../slist_reference/P003_单向链表头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P332_ibi.h_源码浏览.md)
- [i3c_ibi](../hardware/P397_I3C带内中断请求.md)
- [i3c_ibi_payload](../hardware/P398_I3C带内中断载荷.md)
- [i3c_ibi_work](../hardware/P399_I3C带内中断工作项.md)
- [CONFIG_I3C_IBI_MAX_PAYLOAD_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#ga7bbbff351dc33d1c00abf6c22bbd50d4)
- [i3c_target_ibi_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#ga814cf622b240808216ce4e87802e965c)
- [i3c_device_desc](../hardware/P401_I3C设备描述符.md)
- [i3c_ibi_type](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#gaf4be72fc9c862d996d860c0b7fbc862b)
- [I3C_IBI_TARGET_INTR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#ggaf4be72fc9c862d996d860c0b7fbc862ba368e8ad08a003ebf197add6d73ffd43d)
- [I3C_IBI_CONTROLLER_ROLE_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#ggaf4be72fc9c862d996d860c0b7fbc862ba00235d326559f945d54638b0c0558815)
- [I3C_IBI_HOTJOIN](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#ggaf4be72fc9c862d996d860c0b7fbc862ba493d3b1e9669434c3d62f16aa3d6f92f)
- [I3C_IBI_TYPE_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#ggaf4be72fc9c862d996d860c0b7fbc862baab12781f76c743cec6b72ffa7d8c27ee)
- [I3C_IBI_WORKQUEUE_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#ggaf4be72fc9c862d996d860c0b7fbc862ba39d8f6a9b69d092eabf9ca9726deec8c)
- [i3c_ibi_work_enqueue](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#gaafc2fdf9f2402691c3ebe11d06106840)
- [i3c_ibi_work_enqueue_target_irq](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#ga7fbf838ea07516849dc1296d48af65d1)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [i3c_ibi_work_enqueue_controller_request](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#gad643c7f0512e1e6dcddbe5821e70fc0d)
- [i3c_ibi_work_enqueue_hotjoin](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#gab135cb893efd50c7db16c1734b6a0bab)
- [device](../device_reference/P002_设备对象结构.md)
- [i3c_ibi_work_enqueue_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#ga4c6f4516e55d0ab6c539fb800d7ec45a)
- [k_work_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga5add9ef0dce306a08413c4140fc0bdda)

---

[上一章](P012_zephyr__net__ethernet_bridge_fdb.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P014_zephyr__dt-bindings__clock__ifx_clock_source_psc3xx.h_文件参考.md)
