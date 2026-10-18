---
id: learning.zephyr-docs.usb.api-32
title: USB设备控制器缓冲区信息
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structudc__buf__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第32章\_USB设备控制器缓冲区信息

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structudc__buf__info.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 32.1\_阅读说明与来源

译注：本页属于[USB设备控制器API说明](P029_USB设备控制器API说明.md)的底层接口参考，供理解控制器驱动、端点管理和请求生命周期。声明和原注释按官方页面保留，补充解释明确标为源码译注。

[本册大纲](大纲.md)提供本组第29至39章的全部字段参考。

UDC 端点缓冲区信息（Endpoint Buffer Info）。

```c
#include <zephyr/drivers/usb/udc.h>
```

UDC 端点缓冲区信息（Endpoint Buffer Info）。

所有 UDC 请求都必须具有此结构体。它包含请求的元数据，保存在各请求 net_buf 结构体的 user_data 数组中。

## 32.2\_数据成员（Data Fields）

<a id="r_a0a1c09f587d3f6847cb7ce77514a3321"></a>

```c
uint8_t ep
```

请求关联的端点。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ep](P032_USB设备控制器缓冲区信息.md#a0a1c09f587d3f6847cb7ce77514a3321)。

<a id="r_a9664e1f7cddd36dbc7d206b52da45170"></a>

```c
unsigned int setup: 1
```

标记设置阶段传输的标志。

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[setup](P032_USB设备控制器缓冲区信息.md#a9664e1f7cddd36dbc7d206b52da45170)。

<a id="r_ab500ff0bf12ecdbbd4f3cb48d0556ed2"></a>

```c
unsigned int data: 1
```

标记控制传输数据阶段的标志。

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[data](P032_USB设备控制器缓冲区信息.md#ab500ff0bf12ecdbbd4f3cb48d0556ed2)。

<a id="r_a84cf74496eddc4a69a47d23dcdbf753f"></a>

```c
unsigned int status: 1
```

标记控制传输状态阶段的标志。

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[status](P032_USB设备控制器缓冲区信息.md#a84cf74496eddc4a69a47d23dcdbf753f)。

<a id="r_afc2d0c391aca7f68a1ae5539a1fed8a0"></a>

```c
unsigned int zlp: 1
```

标记传输末尾 ZLP 的标志。

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[zlp](P032_USB设备控制器缓冲区信息.md#afc2d0c391aca7f68a1ae5539a1fed8a0)。

<a id="r_a9b03b6dd8418d4200733a612aac73daa"></a>

```c
unsigned int claimed: 1
```

标记请求缓冲区已被控制器占用的标志，原文标为待定（TBD）。

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[claimed](P032_USB设备控制器缓冲区信息.md#a9b03b6dd8418d4200733a612aac73daa)。

<a id="r_a4cd2e83000a0551d126bebe89552eab9"></a>

```c
unsigned int queued: 1
```

标记请求缓冲区已入队的标志，原文标为待定（TBD）。

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[queued](P032_USB设备控制器缓冲区信息.md#a4cd2e83000a0551d126bebe89552eab9)。

<a id="r_a33e927f23d227a4974915c65927284ec"></a>

```c
void * owner
```

传输所有者（Transfer Owner），通常是指向类实例的指针。

相关声明：[owner](P032_USB设备控制器缓冲区信息.md#a33e927f23d227a4974915c65927284ec)。

<a id="r_af1c92f1cdd6e0474a19f788140fdc573"></a>

```c
int err
```

传输结果，成功时为 0，其他值表示错误。

相关声明：[err](P032_USB设备控制器缓冲区信息.md#af1c92f1cdd6e0474a19f788140fdc573)。

## 32.3\_详细说明（Detailed Documentation）

<a id="a9b03b6dd8418d4200733a612aac73daa"></a>

### `claimed`

```c
unsigned int udc_buf_info::claimed
```

标记请求缓冲区已被控制器占用的标志，原文标为待定（TBD）。

<a id="ab500ff0bf12ecdbbd4f3cb48d0556ed2"></a>

### `data`

```c
unsigned int udc_buf_info::data
```

标记控制传输数据阶段的标志。

<a id="a0a1c09f587d3f6847cb7ce77514a3321"></a>

### `ep`

```c
uint8_t udc_buf_info::ep
```

请求关联的端点。

<a id="af1c92f1cdd6e0474a19f788140fdc573"></a>

### `err`

```c
int udc_buf_info::err
```

传输结果，成功时为 0，其他值表示错误。

> 译注（源码核对）：UDC_EVT_EP_REQUEST 使用事件的 buf 成员携带请求，传输结果由公共提交函数写入该缓冲区的 udc_buf_info.err。不能将事件联合体中的 status 当作同时有效的第二份传输结果。

<a id="a33e927f23d227a4974915c65927284ec"></a>

### `owner`

```c
void* udc_buf_info::owner
```

传输所有者（Transfer Owner），通常是指向类实例的指针。

<a id="a4cd2e83000a0551d126bebe89552eab9"></a>

### `queued`

```c
unsigned int udc_buf_info::queued
```

标记请求缓冲区已入队的标志，原文标为待定（TBD）。

<a id="a9664e1f7cddd36dbc7d206b52da45170"></a>

### `setup`

```c
unsigned int udc_buf_info::setup
```

标记设置阶段传输的标志。

<a id="a84cf74496eddc4a69a47d23dcdbf753f"></a>

### `status`

```c
unsigned int udc_buf_info::status
```

标记控制传输状态阶段的标志。

<a id="afc2d0c391aca7f68a1ae5539a1fed8a0"></a>

### `zlp`

```c
unsigned int udc_buf_info::zlp
```

标记传输末尾 ZLP 的标志。

## 32.4\_相关源码与使用边界

控制器接口与结构定义来自 `zephyr/drivers/usb/udc.h`，缓冲区宏来自 `zephyr/drivers/usb/usb_buf.h`。本仓库的[对应头文件](../../../include/zephyr/drivers/usb/udc.h)、[公共实现](../../../drivers/usb/udc/udc_common.c)、[内部辅助接口](../../../drivers/usb/udc/udc_common.h)和[驱动骨架](../../../drivers/usb/udc/udc_skeleton.c)可用于源码跟踪；版本可能与官方 latest 不同。译注依据保存的[官方头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/drivers/usb/udc.h)、[公共实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/usb/udc/udc_common.c)、[内部接口](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/usb/udc/udc_common.h)及[骨架实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/usb/udc/udc_skeleton.c)，摘要见[来源记录](../SOURCES.md)。本批没有编译、运行或操作USB设备。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P031_USB设备控制器驱动接口.md) · [返回大纲](大纲.md) · [下一章](P033_USB设备控制器驱动数据.md)
