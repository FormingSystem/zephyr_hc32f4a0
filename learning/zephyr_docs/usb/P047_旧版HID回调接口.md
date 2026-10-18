---
id: learning.zephyr-docs.usb.api-47
title: 旧版HID回调接口
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structhid__ops.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第47章\_旧版HID回调接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structhid__ops.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 47.1\_阅读说明与来源

译注：本页属于[HID通用说明](P040_HID通用说明.md)及其设备接口参考，说明报告描述符、设备回调和报告传输。声明和原注释按官方页面保留，补充解释明确标为源码译注。

[本册大纲](大纲.md)提供本组第40至50章的全部字段参考。

USB HID 设备接口。

```c
#include <zephyr/usb/class/usb_hid.h>
```

USB HID 设备接口。

## 47.2\_数据成员（Data Fields）

<a id="r_a4ec029d8a0bc2acb1dd89a4ccdc4d652"></a>

```c
hid_cb_t get_report
```



相关声明：[hid_cb_t](P046_旧版HID设备接口API.md#ga04ec088255198d1597df8d70db6257ee)、[get_report](P047_旧版HID回调接口.md#a4ec029d8a0bc2acb1dd89a4ccdc4d652)。

<a id="r_a5ab9c3bbb1d42b7557682ce4f9fc5de5"></a>

```c
hid_cb_t set_report
```



相关声明：[hid_cb_t](P046_旧版HID设备接口API.md#ga04ec088255198d1597df8d70db6257ee)、[set_report](P047_旧版HID回调接口.md#a5ab9c3bbb1d42b7557682ce4f9fc5de5)。

<a id="r_acc04ebec1deb335ef60bd3a01c6058d6"></a>

```c
hid_protocol_cb_t protocol_change
```



相关声明：[hid_protocol_cb_t](P046_旧版HID设备接口API.md#gae3d308c55f5594cc0c926b52aaa28fc7)、[protocol_change](P047_旧版HID回调接口.md#acc04ebec1deb335ef60bd3a01c6058d6)。

<a id="r_a1acc7f77f6896d2925e63402f1b9ffdd"></a>

```c
hid_idle_cb_t on_idle
```



相关声明：[hid_idle_cb_t](P046_旧版HID设备接口API.md#ga61b4facfbfb729159135f5c7534ca593)、[on_idle](P047_旧版HID回调接口.md#a1acc7f77f6896d2925e63402f1b9ffdd)。

<a id="r_af1eda81d93e935f9560a26344076f65e"></a>

```c
hid_int_ready_callback int_in_ready
```



相关声明：[hid_int_ready_callback](P046_旧版HID设备接口API.md#gaed433e24f8487d4e451d9f9daa08c5b0)、[int_in_ready](P047_旧版HID回调接口.md#af1eda81d93e935f9560a26344076f65e)。

<a id="r_a42f454cc1ea1e7ae75e6fa4073111f48"></a>

```c
hid_int_ready_callback int_out_ready
```



相关声明：[hid_int_ready_callback](P046_旧版HID设备接口API.md#gaed433e24f8487d4e451d9f9daa08c5b0)、[int_out_ready](P047_旧版HID回调接口.md#a42f454cc1ea1e7ae75e6fa4073111f48)。

## 47.3\_详细说明（Detailed Documentation）

<a id="a4ec029d8a0bc2acb1dd89a4ccdc4d652"></a>

### `get_report`

```c
hid_cb_t hid_ops::get_report
```

<a id="af1eda81d93e935f9560a26344076f65e"></a>

### `int_in_ready`

```c
hid_int_ready_callback hid_ops::int_in_ready
```

> 译注（源码核对）：官方头文件的普通注释说明它是可选回调，在当前中断IN传输结束时调用，可用于等待端点空闲或触发下一次传输。该普通注释未出现在Doxygen字段正文中，这里作为源码译注补充。

<a id="a42f454cc1ea1e7ae75e6fa4073111f48"></a>

### `int_out_ready`

```c
hid_int_ready_callback hid_ops::int_out_ready
```

<a id="a1acc7f77f6896d2925e63402f1b9ffdd"></a>

### `on_idle`

```c
hid_idle_cb_t hid_ops::on_idle
```

> 译注（源码核对）：新版兼容层没有把报告ID对应的 Set Idle 时长完整转发给旧接口，非零ID会记录无法传播的错误日志；旧回调表与新版 hid_device_ops 不能机械一一替换。

<a id="acc04ebec1deb335ef60bd3a01c6058d6"></a>

### `protocol_change`

```c
hid_protocol_cb_t hid_ops::protocol_change
```

<a id="a5ab9c3bbb1d42b7557682ce4f9fc5de5"></a>

### `set_report`

```c
hid_cb_t hid_ops::set_report
```

> 译注：本页保留已弃用接口用于迁移和源码对照；新实现参阅[新版HID设备API](P042_新版HID设备API.md)。

## 47.4\_源码跟踪与使用边界

通用项目及描述符见[hid.h](../../../include/zephyr/usb/class/hid.h)，新版接口见[usbd_hid.h](../../../include/zephyr/usb/class/usbd_hid.h)和[新版实现](../../../subsys/usb/device_next/class/usbd_hid.c)，旧接口见[usb_hid.h](../../../include/zephyr/usb/class/usb_hid.h)、[旧版实现](../../../subsys/usb/device/class/hid/core.c)及[新版兼容包装](../../../subsys/usb/device_next/class/usbd_hid_api.c)。本仓库版本可能与官方 latest 不同；译注依据保存的[官方通用头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/hid.h)、[新版头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/usbd_hid.h)、[新版实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_hid.c)、[兼容包装](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_hid_api.c)和[旧版实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device/class/hid/core.c)，摘要见[来源记录](../SOURCES.md)。本批未编译、运行或操作USB硬件。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P046_旧版HID设备接口API.md) · [返回大纲](大纲.md) · [下一章](P048_HID通用定义.md)
