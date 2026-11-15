---
id: learning.zephyr-docs.usb.api-37
title: USB设备控制器端点状态
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structudc__ep__stat.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第37章\_USB设备控制器端点状态

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structudc__ep__stat.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 37.1\_阅读说明与来源

译注：本页属于[USB设备控制器API说明](P029_USB设备控制器API说明.md)的底层接口参考，供理解控制器驱动、端点管理和请求生命周期。声明和原注释按官方页面保留，补充解释明确标为源码译注。

[本册大纲](大纲.md)提供本组第29至39章的全部字段参考。

USB 设备控制器端点状态。

```c
#include <zephyr/drivers/usb/udc.h>
```

USB 设备控制器端点状态。

## 37.2\_数据成员（Data Fields）

<a id="r_a250eed32f2945cb89df8033ae2781969"></a>

```c
bool enabled
```

端点已启用。

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[enabled](P037_USB设备控制器端点状态.md#a250eed32f2945cb89df8033ae2781969)。

<a id="r_a5273e8e99fb6943babcb573f10c90c76"></a>

```c
bool halted
```

端点已停止，返回 STALL 包标识符（Packet Identifier，PID）。

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[halted](P037_USB设备控制器端点状态.md#a5273e8e99fb6943babcb573f10c90c76)。

<a id="r_a2c9522c3f5e4f1a9cba90cd73092c07f"></a>

```c
bool data1
```

上次提交的 PID 为 DATA1。

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[data1](P037_USB设备控制器端点状态.md#a2c9522c3f5e4f1a9cba90cd73092c07f)。

<a id="r_a47a7b3247c2aee78c3b58835081aed0c"></a>

```c
bool busy
```

端点忙。

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[busy](P037_USB设备控制器端点状态.md#a47a7b3247c2aee78c3b58835081aed0c)。

## 37.3\_详细说明（Detailed Documentation）

<a id="a47a7b3247c2aee78c3b58835081aed0c"></a>

### `busy`

```c
bool udc_ep_stat::busy
```

端点忙。

<a id="a2c9522c3f5e4f1a9cba90cd73092c07f"></a>

### `data1`

```c
bool udc_ep_stat::data1
```

上次提交的 PID 为 DATA1。

<a id="a250eed32f2945cb89df8033ae2781969"></a>

### `enabled`

```c
bool udc_ep_stat::enabled
```

端点已启用。

<a id="a5273e8e99fb6943babcb573f10c90c76"></a>

### `halted`

```c
bool udc_ep_stat::halted
```

端点已停止，返回 STALL 包标识符（Packet Identifier，PID）。

## 37.4\_相关源码与使用边界

控制器接口与结构定义来自 `zephyr/drivers/usb/udc.h`，缓冲区宏来自 `zephyr/drivers/usb/usb_buf.h`。本仓库的[对应头文件](../../../include/zephyr/drivers/usb/udc.h)、[公共实现](../../../drivers/usb/udc/udc_common.c)、[内部辅助接口](../../../drivers/usb/udc/udc_common.h)和[驱动骨架](../../../drivers/usb/udc/udc_skeleton.c)可用于源码跟踪；版本可能与官方 latest 不同。译注依据保存的[官方头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/drivers/usb/udc.h)、[公共实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/usb/udc/udc_common.c)、[内部接口](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/usb/udc/udc_common.h)及[骨架实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/usb/udc/udc_skeleton.c)，摘要见[来源记录](../SOURCES.md)。本批没有编译、运行或操作USB设备。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P036_USB设备控制器端点配置.md) · [返回大纲](大纲.md) · [下一章](P038_USB设备控制器事件结构.md)
