---
id: learning.zephyr-docs.peripheral-bus-storage-source-reference.page-2
title: zephyr__drivers__misc__devmux__devmux.h_头文件源码
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/devmux_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_zephyr__drivers__misc__devmux__devmux.h_头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/devmux_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应头文件参考](../peripheral_bus_storage_header_reference/P002_zephyr__drivers__misc__devmux__devmux.h_头文件参考.md)。

## 2.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00056"></a>
<a id="foldopen00060"></a>
<a id="l00060"></a>
<a id="l00064"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__demux__interface_html_ga895dad09fcd98c8731f9ae784b018e0a"></a>
<a id="agroup__demux__interface_html_gafd3635aa5bd36c41832a4eb31cd122ca"></a>
<a id="akernel_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astructdevice_html"></a>
<a id="astructdevmux__driver__api_html"></a>
<a id="astructdevmux__driver__api_html_a883b6973a6109c189f7f82f38aace760"></a>
<a id="astructdevmux__driver__api_html_a9e9453dbb5639b6df48f75905b539583"></a>

```c
/*
 * Copyright (c) 2023, Meta
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_MISC_DEVMUX_DEVMUX_H_
#define ZEPHYR_INCLUDE_DRIVERS_MISC_DEVMUX_DEVMUX_H_

#include <stdint.h>

#include <zephyr/device.h>
#include <zephyr/kernel.h>

#ifdef __cplusplus
extern "C" {
#endif


__subsystem struct devmux_driver_api {
        int (*select_get)(const struct device *dev);
        int (*select_set)(struct device *dev, size_t index);
};

__syscall int devmux_select_get(const struct device *dev);

__syscall int devmux_select_set(struct device *dev, size_t index);


#ifdef __cplusplus
}
#endif

#include <zephyr/syscalls/devmux.h>

#endif /* ZEPHYR_INCLUDE_DRIVERS_MISC_DEVMUX_DEVMUX_H_ */
```

## 2.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023, Meta。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 105 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_MISC_DEVMUX_DEVMUX_H_`。

## 2.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../peripheral_bus_storage_header_reference/P002_zephyr__drivers__misc__devmux__devmux.h_头文件参考.md)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [devmux_driver_api](../peripheral_bus_storage_model_reference/P003_devmux_driver_api_结构体.md)
- [select_get](../peripheral_bus_storage_model_reference/P003_devmux_driver_api_结构体.md#a883b6973a6109c189f7f82f38aace760)
- [device](../device_reference/P002_设备对象结构.md)
- [select_set](../peripheral_bus_storage_model_reference/P003_devmux_driver_api_结构体.md#a9e9453dbb5639b6df48f75905b539583)
- [devmux_select_get](https://docs.zephyrproject.org/latest/doxygen/html/group__demux__interface.html#gafd3635aa5bd36c41832a4eb31cd122ca)
- [devmux_select_set](https://docs.zephyrproject.org/latest/doxygen/html/group__demux__interface.html#ga895dad09fcd98c8731f9ae784b018e0a)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [devmux_driver_api::select_get](../peripheral_bus_storage_model_reference/P003_devmux_driver_api_结构体.md#a883b6973a6109c189f7f82f38aace760)
- [devmux_driver_api::select_set](../peripheral_bus_storage_model_reference/P003_devmux_driver_api_结构体.md#a9e9453dbb5639b6df48f75905b539583)

---

[上一章](P001_zephyr__drivers__dali.h_头文件源码.md) · [返回大纲](大纲.md) · [下一章](P003_zephyr__drivers__disk.h_头文件源码.md)
