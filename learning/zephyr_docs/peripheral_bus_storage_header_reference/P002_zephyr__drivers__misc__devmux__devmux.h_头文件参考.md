---
id: learning.zephyr-docs.peripheral-bus-storage-header-reference.page-2
title: zephyr__drivers__misc__devmux__devmux.h_头文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/devmux_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_zephyr\_\_drivers\_\_misc\_\_devmux\_\_devmux.h\_头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/devmux_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

设备多路复用器（Device Multiplexer）驱动的公共API。

<a id="details"></a>

```c
#include <stdint.h>
#include <zephyr/device.h>
#include <zephyr/kernel.h>
#include <zephyr/syscalls/devmux.h>
```

查看此文件的源码。

设备多路复用器（Device Multiplexer）驱动的公共API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 2.1\_数据结构（Data Structures）

<a id="r_devmux_5Fdriver_5Fapi"></a>

```c
struct devmux_driver_api
```

相关声明：[devmux_driver_api](../peripheral_bus_storage_model_reference/P003_devmux_driver_api_结构体.md)。

驱动操作（Driver Operations）：设备多路复用（DEVMUX）驱动操作。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.2\_函数（Functions）

<a id="r_gafd3635aa5bd36c41832a4eb31cd122ca"></a>

```c
int devmux_select_get (const struct device *dev)
```

相关声明：[devmux_select_get](https://docs.zephyrproject.org/latest/doxygen/html/group__demux__interface.html#gafd3635aa5bd36c41832a4eb31cd122ca)、[device](../device_reference/P002_设备对象结构.md)。

获取设备多路复用器（devmux）的当前选择项。

<a id="r_ga895dad09fcd98c8731f9ae784b018e0a"></a>

```c
int devmux_select_set (struct device *dev, size_t index)
```

相关声明：[devmux_select_set](https://docs.zephyrproject.org/latest/doxygen/html/group__demux__interface.html#ga895dad09fcd98c8731f9ae784b018e0a)、[device](../device_reference/P002_设备对象结构.md)。

设置 devmux 设备的选择项。


## 2.3\_原页交叉引用（Cross References）

- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [查看此文件的源码](https://docs.zephyrproject.org/latest/doxygen/html/devmux_8h_source.html)
- [devmux_driver_api](../peripheral_bus_storage_model_reference/P003_devmux_driver_api_结构体.md)
- [devmux_select_get](https://docs.zephyrproject.org/latest/doxygen/html/group__demux__interface.html#gafd3635aa5bd36c41832a4eb31cd122ca)
- [device](../device_reference/P002_设备对象结构.md)
- [devmux_select_set](https://docs.zephyrproject.org/latest/doxygen/html/group__demux__interface.html#ga895dad09fcd98c8731f9ae784b018e0a)

<a id="header-details"></a>

---

[上一章](P001_zephyr__drivers__dali.h_头文件参考.md) · [返回大纲](大纲.md) · [下一章](P003_zephyr__drivers__disk.h_头文件参考.md)
