---
id: learning.zephyr-docs.usb.api-27
title: USB类回调接口
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusbd__class__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第27章\_USB类回调接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusbd__class__api.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 27.1\_阅读说明与来源

译注：本页是[USB设备核心API](P015_USB设备核心API.md)的数据结构参考，说明描述符、配置、上下文与类实例的成员。字段声明和原注释按官方页面保留；内部类型或回调约定的补充明确标为源码译注。

[本册大纲](大纲.md)提供本组第18至28章的全部字段参考。

USB 设备支持的类实例（Class Instance）API。

```c
#include <zephyr/usb/usbd.h>
```

USB 设备支持的类实例（Class Instance）API。

## 27.2\_数据成员（Data Fields）

<a id="r_a09475f1b29f482e548b6bc168dcd19e7"></a>

```c
void(* feature_halt )(struct usbd_class_data *const c_data, uint8_t ep, bool halted)
```

端点停止特性状态更新处理函数。

相关声明：[feature_halt](P027_USB类回调接口.md#a09475f1b29f482e548b6bc168dcd19e7)、[usbd_class_data](P028_USB类数据结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

<a id="r_a11d09e35f9d4c4d6b18e12bf4ea241b0"></a>

```c
void(* update )(struct usbd_class_data *const c_data, uint8_t iface, uint8_t alternate)
```

配置更新处理函数。

相关声明：[update](P027_USB类回调接口.md#a11d09e35f9d4c4d6b18e12bf4ea241b0)、[usbd_class_data](P028_USB类数据结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_ab37dd5f2bf4029f149e69046702626a1"></a>

```c
int(* control_to_dev )(struct usbd_class_data *const c_data, const struct usb_setup_packet *const setup, const struct net_buf *const buf)
```

主机到设备方向的 USB 控制请求处理函数。

相关声明：[control_to_dev](P027_USB类回调接口.md#ab37dd5f2bf4029f149e69046702626a1)、[usbd_class_data](P028_USB类数据结构.md)、[usb_setup_packet](P160_USB控制请求包.md)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

<a id="r_aec3b9914635baac7ef942e55ff28347f"></a>

```c
struct net_buf *(* control_to_host )(struct usbd_class_data *const c_data, const struct usb_setup_packet *const setup)
```

设备到主机方向的 USB 控制请求处理函数。

相关声明：[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)、[control_to_host](P027_USB类回调接口.md#aec3b9914635baac7ef942e55ff28347f)、[usbd_class_data](P028_USB类数据结构.md)、[usb_setup_packet](P160_USB控制请求包.md)。

<a id="r_a70425718fd34534fd976240340b4496d"></a>

```c
int(* request )(struct usbd_class_data *const c_data, struct net_buf *buf, int err)
```

端点请求完成事件处理函数。

相关声明：[request](P027_USB类回调接口.md#a70425718fd34534fd976240340b4496d)、[usbd_class_data](P028_USB类数据结构.md)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

<a id="r_a598afe76b5c2f9e75a049fe785393e04"></a>

```c
void(* suspended )(struct usbd_class_data *const c_data)
```

USB 电源管理的挂起处理函数。

相关声明：[suspended](P027_USB类回调接口.md#a598afe76b5c2f9e75a049fe785393e04)、[usbd_class_data](P028_USB类数据结构.md)。

<a id="r_ae6f3a658e5768f5d6672cd0e5f2d24a5"></a>

```c
void(* resumed )(struct usbd_class_data *const c_data)
```

USB 电源管理的恢复（Resumed）处理函数。

相关声明：[resumed](P027_USB类回调接口.md#ae6f3a658e5768f5d6672cd0e5f2d24a5)、[usbd_class_data](P028_USB类数据结构.md)。

<a id="r_a488b102936b5cd3e4095578119b71510"></a>

```c
void(* sof )(struct usbd_class_data *const c_data)
```

帧起始（Start of Frame，SOF）。

相关声明：[sof](P027_USB类回调接口.md#a488b102936b5cd3e4095578119b71510)、[usbd_class_data](P028_USB类数据结构.md)。

<a id="r_ab42f61db338471f0c5260576680409e9"></a>

```c
void(* enable )(struct usbd_class_data *const c_data)
```

类关联的配置已被选中。

相关声明：[enable](P027_USB类回调接口.md#ab42f61db338471f0c5260576680409e9)、[usbd_class_data](P028_USB类数据结构.md)。

<a id="r_afd43bfa4aab664c50648aa59a0c713de"></a>

```c
void(* disable )(struct usbd_class_data *const c_data)
```

类关联的配置已被停用。

相关声明：[disable](P027_USB类回调接口.md#afd43bfa4aab664c50648aa59a0c713de)、[usbd_class_data](P028_USB类数据结构.md)。

<a id="r_a7d749f007d70e30f76aa121067b7a5c6"></a>

```c
int(* init )(struct usbd_class_data *const c_data)
```

初始化类实现。

相关声明：[init](P027_USB类回调接口.md#a7d749f007d70e30f76aa121067b7a5c6)、[usbd_class_data](P028_USB类数据结构.md)。

<a id="r_a5ca5bc6d3f5220bd3658d9398e09016e"></a>

```c
void(* shutdown )(struct usbd_class_data *const c_data)
```

关闭类实现。

相关声明：[shutdown](P027_USB类回调接口.md#a5ca5bc6d3f5220bd3658d9398e09016e)、[usbd_class_data](P028_USB类数据结构.md)。

<a id="r_a193e2f7874ff86015ef2d07e5f2dbf08"></a>

```c
const void *(* get_desc )(struct usbd_class_data *const c_data, const enum usbd_speed speed)
```

根据速率参数取得功能描述符。

相关声明：[get_desc](P027_USB类回调接口.md#a193e2f7874ff86015ef2d07e5f2dbf08)、[usbd_class_data](P028_USB类数据结构.md)、[usbd_speed](P015_USB设备核心API.md#ga2f2da3d634530f08cd59d408c811ad71)。

## 27.3\_详细说明（Detailed Documentation）

<a id="ab37dd5f2bf4029f149e69046702626a1"></a>

### `control_to_dev`

```c
int(* usbd_class_api::control_to_dev) (struct usbd_class_data *const c_data, const struct usb_setup_packet *const setup, const struct net_buf *const buf)
```

主机到设备方向的 USB 控制请求处理函数。

> 译注（源码核对）：当前内部包装接口要求处理函数不得阻塞；有 OUT 数据阶段时，先用 NULL 缓冲区调用以检查是否接收，再用非空缓冲区调用处理数据。无数据阶段时只调用一次。成功返回0，其他值视为失败；未提供回调时包装层返回 -ENOTSUP。

<a id="aec3b9914635baac7ef942e55ff28347f"></a>

### `control_to_host`

```c
struct net_buf *(* usbd_class_api::control_to_host) (struct usbd_class_data *const c_data, const struct usb_setup_packet *const setup)
```

设备到主机方向的 USB 控制请求处理函数。

> 译注（源码核对）：当前包装接口要求处理函数不得阻塞。处理函数分配响应缓冲区，有效响应的所有权交给协议栈；若分配后决定用 STALL 握手拒绝请求，必须先释放缓冲区再返回 NULL。未提供回调时包装层返回 NULL。

<a id="afd43bfa4aab664c50648aa59a0c713de"></a>

### `disable`

```c
void(* usbd_class_api::disable) (struct usbd_class_data *const c_data)
```

类关联的配置已被停用。

> 译注（源码核对）：表示该类关联的配置被停用；当前内部接口要求此回调不得阻塞。

<a id="ab42f61db338471f0c5260576680409e9"></a>

### `enable`

```c
void(* usbd_class_api::enable) (struct usbd_class_data *const c_data)
```

类关联的配置已被选中。

> 译注（源码核对）：表示宿主选中了该类关联的配置，不等同于应用完成 usbd_init()。当前内部接口要求此回调不得阻塞。

<a id="a09475f1b29f482e548b6bc168dcd19e7"></a>

### `feature_halt`

```c
void(* usbd_class_api::feature_halt) (struct usbd_class_data *const c_data, uint8_t ep, bool halted)
```

端点停止特性状态更新处理函数。

> 译注（源码核对）：当前内部说明指出，所属接口端点被 Set Feature Endpoint Halt 或 Clear Feature Endpoint Halt 请求改变状态时调用此处理函数；halted 为 true 表示进入停止状态，为 false 表示清除停止状态。处理函数不得阻塞。

<a id="a193e2f7874ff86015ef2d07e5f2dbf08"></a>

### `get_desc`

```c
const void *(* usbd_class_api::get_desc) (struct usbd_class_data *const c_data, const enum usbd_speed speed)
```

根据速率参数取得功能描述符。

> 译注（源码核对）：当前包装接口约定，返回值指向 usb_desc_header 指针数组，最后一个元素指向 nil 描述符；不可用时返回 NULL。虽然公开原型为 const void *，也不能把结果当作单个普通描述符或任意字节块。

<a id="a7d749f007d70e30f76aa121067b7a5c6"></a>

### `init`

```c
int(* usbd_class_api::init) (struct usbd_class_data *const c_data)
```

初始化类实现。

> 译注（源码核对）：当前包装接口说明，此回调在初始化阶段、接口号和端点地址分配后执行，可初始化类专用描述符和底层系统；失败会终止栈初始化。没有提供 init 回调时包装层返回 -ENOTSUP，不能假定所有未填写的回调都被自动忽略。

<a id="a70425718fd34534fd976240340b4496d"></a>

### `request`

```c
int(* usbd_class_api::request) (struct usbd_class_data *const c_data, struct net_buf *buf, int err)
```

端点请求完成事件处理函数。

> 译注（源码核对）：这是端点传输完成通知，不是提交传输的接口。当前包装接口把传输结果通过 err 传入，0 表示成功；未提供 request 回调时返回 -ENOTSUP。具体缓冲区回收由对应类实现按传输生命周期处理。

<a id="ae6f3a658e5768f5d6672cd0e5f2d24a5"></a>

### `resumed`

```c
void(* usbd_class_api::resumed) (struct usbd_class_data *const c_data)
```

USB 电源管理的恢复（Resumed）处理函数。

<a id="a5ca5bc6d3f5220bd3658d9398e09016e"></a>

### `shutdown`

```c
void(* usbd_class_api::shutdown) (struct usbd_class_data *const c_data)
```

关闭类实现。

> 译注（源码核对）：当前内部接口在关闭阶段对每个实例调用此回调，并要求不得阻塞。没有提供回调时相应包装函数直接跳过。

<a id="a488b102936b5cd3e4095578119b71510"></a>

### `sof`

```c
void(* usbd_class_api::sof) (struct usbd_class_data *const c_data)
```

帧起始（Start of Frame，SOF）。

> 译注（源码核对）：当前内部说明要求帧起始处理函数不得阻塞；该通知与应用自行创建的周期定时器不同。

<a id="a598afe76b5c2f9e75a049fe785393e04"></a>

### `suspended`

```c
void(* usbd_class_api::suspended) (struct usbd_class_data *const c_data)
```

USB 电源管理的挂起处理函数。

<a id="a11d09e35f9d4c4d6b18e12bf4ea241b0"></a>

### `update`

```c
void(* usbd_class_api::update) (struct usbd_class_data *const c_data, uint8_t iface, uint8_t alternate)
```

配置更新处理函数。

> 译注（源码核对）：此处理函数响应 Set Configuration 或 Set Interface 引起的接口配置变化，iface 为接口号，alternate 为替代设置。当前内部接口明确要求不得阻塞。

## 27.4\_相关源码与使用边界

本页结构定义来自 `zephyr/usb/usbd.h`；本仓库的[对应头文件](../../../include/zephyr/usb/usbd.h)、[类回调包装接口](../../../subsys/usb/device_next/usbd_class_api.h)、[第9章控制请求处理](../../../subsys/usb/device_next/usbd_ch9.c)及[初始化实现](../../../subsys/usb/device_next/usbd_init.c)可用于源码跟踪，版本可能与官网 latest 不同。译注依据保存的[官方头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/usbd.h)、[回调接口](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_class_api.h)、[控制请求实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_ch9.c)、[描述符管理](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_desc.c)和[初始化实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/usbd_init.c)，摘要见[来源记录](../SOURCES.md)。本批没有编译、运行或操作USB设备。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P026_USB类厂商请求表.md) · [返回大纲](大纲.md) · [下一章](P028_USB类数据结构.md)
