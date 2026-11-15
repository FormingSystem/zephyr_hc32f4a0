---
id: learning.zephyr-docs.api-auxiliary-topic-reference.page-3
title: 设备多路复用器（Devmux）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__demux__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_设备多路复用器（Devmux）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__demux__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

设备多路复用器（Device multiplexer）接口。

<a id="details"></a>

设备多路复用器接口（Interfaces for device multiplexers）。Devmux 充当设备多路复用器，转发所选设备的特性。下方保留原始示意图。

原页随示意图提供的符号说明：`select` 的声明为 `int select(int nfds, fd_set *readfds, fd_set *writefds, fd_set *errorfds, struct timeval *timeout)`。

```text
           +----------+                            +----------+
           |  devmux  |                            |  devmux  |
           |          |                            |          |
dev0       |          |                 dev0       |          |
+---------->   \      |                 +---------->          |
           |    \     |                            |          |
dev1       |     \    |       dev0      dev1       |          |       dev2
+---------->      O   +---------->      +---------->      O   +---------->
           |          |                            |     /    |
dev2       |          |                 dev2       |    /     |
+---------->          |                 +---------->   /      |
           |          |                            |          |
           |          |                            |          |
           |          |                            |          |
           +-----^----+                            +-----^----+
                 |                                       |
  select == 0    |                       select == 2     |
  +--------------+                       +---------------+
```

<a id="header-files"></a>
<a id="files"></a>

## 3.1\_文件（Files）

<a id="r_devmux_2Eh"></a>

```c
file devmux.h
```

相关声明：[devmux.h](../peripheral_bus_storage_header_reference/P002_zephyr__drivers__misc__devmux__devmux.h_头文件参考.md)。

设备多路复用器（Device Multiplexer）驱动的公共API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 3.2\_数据结构（Data Structures）

<a id="r_devmux_5Fdriver_5Fapi"></a>

```c
struct devmux_driver_api
```

相关声明：[devmux_driver_api](../peripheral_bus_storage_model_reference/P003_devmux_driver_api_结构体.md)。

驱动操作（Driver Operations）：设备多路复用（DEVMUX）驱动操作。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 3.3\_函数（Functions）

<a id="r_gafd3635aa5bd36c41832a4eb31cd122ca"></a>

```c
int devmux_select_get (const struct device *dev)
```

相关声明：[devmux_select_get](#gafd3635aa5bd36c41832a4eb31cd122ca)、[device](../device_reference/P002_设备对象结构.md)。

获取设备多路复用器（devmux）的当前选择项。

<a id="r_ga895dad09fcd98c8731f9ae784b018e0a"></a>

```c
int devmux_select_set (struct device *dev, size_t index)
```

相关声明：[devmux_select_set](#ga895dad09fcd98c8731f9ae784b018e0a)、[device](../device_reference/P002_设备对象结构.md)。

设置 devmux 设备的选择项。

## 3.4\_详细说明（Detailed Documentation）

<a id="gafd3635aa5bd36c41832a4eb31cd122ca"></a>

### `devmux_select_get()`

```c
int devmux_select_get ( const struct device * dev)
```

```c
#include <zephyr/drivers/misc/devmux/devmux.h>
```

获取设备多路复用器（devmux）的当前选择项。

返回当前所选设备的索引（index）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | devmux 设备。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | `dev` 无效时。 |

**返回（Returns）**：返回值：成功时返回当前活动的被复用设备的索引，索引不小于 0。

<a id="ga895dad09fcd98c8731f9ae784b018e0a"></a>

### `devmux_select_set()`

```c
int devmux_select_set ( struct device * dev, size_t index )
```

```c
#include <zephyr/drivers/misc/devmux/devmux.h>
```

设置 devmux 设备的选择项。

选择指定索引处的设备。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | devmux 设备。 |
| ` index` | 表示期望选择项的索引。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EINVAL` | `dev` 无效时。 |
| `-ENODEV` | 指定索引处的被复用设备尚未就绪时。 |


## 3.5\_原页交叉引用（Cross References）

- [devmux.h](../peripheral_bus_storage_header_reference/P002_zephyr__drivers__misc__devmux__devmux.h_头文件参考.md)
- [devmux_driver_api](../peripheral_bus_storage_model_reference/P003_devmux_driver_api_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [select](../api_file_reference/P380_zephyr__posix__sys__select.h_文件参考.md#a7ffa34f8c9a12e7fd43f5ef65bf889fa)

<a id="header-details"></a>
<a id="aselect_8h_html_a7ffa34f8c9a12e7fd43f5ef65bf889fa"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P002_代理（Proxy）.md) · [返回大纲](大纲.md) · [下一章](P004_Microchip XEC ECIA中断控制器（Interrupt Controller）.md)
