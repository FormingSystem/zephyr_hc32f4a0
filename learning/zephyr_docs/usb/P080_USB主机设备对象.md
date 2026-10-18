---
id: learning.zephyr-docs.usb.api-80
title: USB主机设备对象
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusb__device.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第80章\_USB主机设备对象

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusb__device.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 80.1\_阅读说明与来源

译注：本页说明USB主机栈（USB Host Stack）的接口与数据对象。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

USB设备在主机侧的表示。

```c
#include <zephyr/drivers/usb/uhc.h>
```

USB设备在主机侧的表示。

## 80.2\_数据成员（Data Fields）

<a id="r_a0215608e40123de4a3a79ca440c6c593"></a>

```c
sys_dnode_t node
```

双向链表（Doubly Linked List，dlist）节点

相关声明：[sys_dnode_t](../dlist_reference/P001_双向链表公共接口.md#ga57fdb936802a617d16c00ab08cd2ad98)、[node](P080_USB主机设备对象.md#a0215608e40123de4a3a79ca440c6c593)。

<a id="r_a72ee0e53efd86c91e0cea6c7e873d5ce"></a>

```c
void * ctx
```

指向此设备所属主机上下文的不透明指针（Opaque Pointer）。

相关声明：[ctx](P080_USB主机设备对象.md#a72ee0e53efd86c91e0cea6c7e873d5ce)。

<a id="r_a4203b2cfd65f70096a43a20c7c37de27"></a>

```c
struct k_mutex mutex
```

设备互斥锁（Mutex）。

相关声明：[k_mutex](../synchronization_reference/P007_内核互斥量结构.md)、[mutex](P080_USB主机设备对象.md#a4203b2cfd65f70096a43a20c7c37de27)。

<a id="r_a24be9609d416d3a184fdedbefa298490"></a>

```c
struct usb_device_descriptor dev_desc
```

USB设备描述符（Device Descriptor）。

相关声明：[usb_device_descriptor](P163_USB设备描述符.md)、[dev_desc](P080_USB主机设备对象.md#a24be9609d416d3a184fdedbefa298490)。

<a id="r_aa75bbea6a879460b39216453323d177f"></a>

```c
enum usb_device_state state
```

设备状态。

相关声明：[usb_device_state](P073_USB主机控制器API.md#ga7127ac2a46b577f2aa1bb9a650e62a3f)、[state](P080_USB主机设备对象.md#aa75bbea6a879460b39216453323d177f)。

<a id="r_a1b3f4becfd9fbfae80074fc2e76ea6a8"></a>

```c
enum usb_device_speed speed
```

设备速率。

相关声明：[usb_device_speed](P073_USB主机控制器API.md#ga59ba7bbb99177a622f3c073fc48b7bc5)、[speed](P080_USB主机设备对象.md#a1b3f4becfd9fbfae80074fc2e76ea6a8)。

<a id="r_a101d30facb781bd410581fc6c2d3fa59"></a>

```c
uint8_t actual_cfg
```

当前活动的设备配置（Configuration）。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[actual_cfg](P080_USB主机设备对象.md#a101d30facb781bd410581fc6c2d3fa59)。

<a id="r_aa9062a5b9da663863e6d51ef2e04197b"></a>

```c
uint8_t addr
```

设备地址。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[addr](P080_USB主机设备对象.md#aa9062a5b9da663863e6d51ef2e04197b)。

<a id="r_ac98af9fb0d5bba21bc8037a8fcfb3126"></a>

```c
void * cfg_desc
```

指向当前设备配置描述符（Configuration Descriptor）的指针。

相关声明：[cfg_desc](P080_USB主机设备对象.md#ac98af9fb0d5bba21bc8037a8fcfb3126)。

<a id="r_a5cccbb483d91032f4a7f25f88270747f"></a>

```c
struct usb_host_interface ifaces [32+1]
```

指向设备接口的指针。

相关声明：[usb_host_interface](P081_USB主机接口对象.md)、[ifaces](P080_USB主机设备对象.md#a5cccbb483d91032f4a7f25f88270747f)。

<a id="r_a658b9992a472574b1d88e49b7fea478d"></a>

```c
struct usb_host_ep ep_out [16]
```

指向设备输出（OUT）端点的指针。

相关声明：[usb_host_ep](P082_USB主机端点对象.md)、[ep_out](P080_USB主机设备对象.md#a658b9992a472574b1d88e49b7fea478d)。

<a id="r_ad3091acb2a713b9e66c595bbf4a736a5"></a>

```c
struct usb_host_ep ep_in [16]
```

指向设备输入（IN）端点的指针。

相关声明：[usb_host_ep](P082_USB主机端点对象.md)、[ep_in](P080_USB主机设备对象.md#ad3091acb2a713b9e66c595bbf4a736a5)。

<a id="r_a475090912a408eaa2f04d582a1367114"></a>

```c
struct usb_device * hub
```

指向此设备所连接集线器（Hub）的指针。

相关声明：[usb_device](P080_USB主机设备对象.md)、[hub](P080_USB主机设备对象.md#a475090912a408eaa2f04d582a1367114)。

<a id="r_ae0c9c3454eea32432ddb4f8da7361182"></a>

```c
uint16_t tt
```

设备所连接集线器的处理等待时间（Think Time）。

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[tt](P080_USB主机设备对象.md#ae0c9c3454eea32432ddb4f8da7361182)。

<a id="r_a4a66403ece2f186d59ff29e39dc78839"></a>

```c
uint8_t hub_port
```

设备所在的集线器端口。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[hub_port](P080_USB主机设备对象.md#a4a66403ece2f186d59ff29e39dc78839)。

<a id="r_ada9943f1917010381116cd778d6bc47c"></a>

```c
uint8_t level
```

设备层级，根设备的层级为1。

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[level](P080_USB主机设备对象.md#ada9943f1917010381116cd778d6bc47c)。

## 80.3\_详细说明（Detailed Documentation）

<a id="a101d30facb781bd410581fc6c2d3fa59"></a>

### 80.3.1\_`actual\_cfg`

```c
uint8_t usb_device::actual_cfg
```

当前活动的设备配置（Configuration）。

> 译注（源码核对）：保存当前选中的配置值，不是描述符数组的索引。当前设置配置成功后才写入该字段并将state置为USB_STATE_CONFIGURED。

<a id="aa9062a5b9da663863e6d51ef2e04197b"></a>

### 80.3.2\_`addr`

```c
uint8_t usb_device::addr
```

设备地址。

<a id="ac98af9fb0d5bba21bc8037a8fcfb3126"></a>

### 80.3.3\_`cfg\_desc`

```c
void* usb_device::cfg_desc
```

指向当前设备配置描述符（Configuration Descriptor）的指针。

> 译注（源码核对）：当前实现为活动配置描述符及其后续描述符分配一块内存，接口与端点描述符指针会指向其中。切换配置或移除设备时会释放该内存；类驱动不能跨这些生命周期继续使用旧指针。

<a id="a72ee0e53efd86c91e0cea6c7e873d5ce"></a>

### 80.3.4\_`ctx`

```c
void* usb_device::ctx
```

指向此设备所属主机上下文的不透明指针（Opaque Pointer）。

<a id="a24be9609d416d3a184fdedbefa298490"></a>

### 80.3.5\_`dev\_desc`

```c
struct usb_device_descriptor usb_device::dev_desc
```

USB设备描述符（Device Descriptor）。

<a id="ad3091acb2a713b9e66c595bbf4a736a5"></a>

### 80.3.6\_`ep\_in`

```c
struct usb_host_ep usb_device::ep_in[16]
```

指向设备输入（IN）端点的指针。

> 译注（源码核对）：实际声明是16个usb_host_ep元素，各元素的desc才是描述符指针；按端点地址的低4位索引，方向位决定选择ep_in或ep_out。

<a id="a658b9992a472574b1d88e49b7fea478d"></a>

### 80.3.7\_`ep\_out`

```c
struct usb_host_ep usb_device::ep_out[16]
```

指向设备输出（OUT）端点的指针。

> 译注（源码核对）：与ep_in分别保存两个方向的端点信息。OUT是主机向设备发送，IN是设备向主机发送，不应从设备应用的局部读写方向反推。

<a id="a475090912a408eaa2f04d582a1367114"></a>

### 80.3.8\_`hub`

```c
struct usb_device* usb_device::hub
```

指向此设备所连接集线器（Hub）的指针。

> 译注（源码核对）：这些集线器关系字段描述设备拓扑，不表示当前启用的控制器和类驱动已实现全部Hub功能。实际支持须核对所用主机栈与Hub驱动。

<a id="a4a66403ece2f186d59ff29e39dc78839"></a>

### 80.3.9\_`hub\_port`

```c
uint8_t usb_device::hub_port
```

设备所在的集线器端口。

<a id="a5cccbb483d91032f4a7f25f88270747f"></a>

### 80.3.10\_`ifaces`

```c
struct usb_host_interface usb_device::ifaces[32+1]
```

指向设备接口的指针。

> 译注（源码核对）：原注释称“指针”，实际声明是usb_host_interface结构体数组，各元素再保存描述符指针。数组有UHC_INTERFACES_MAX+1个元素不等于支持这么多接口；当前配置解析入口还拒绝bNumInterfaces大于等于UHC_INTERFACES_MAX的配置。

<a id="ada9943f1917010381116cd778d6bc47c"></a>

### 80.3.11\_`level`

```c
uint8_t usb_device::level
```

设备层级，根设备的层级为1。

<a id="a4203b2cfd65f70096a43a20c7c37de27"></a>

### 80.3.12\_`mutex`

```c
struct k_mutex usb_device::mutex
```

设备互斥锁（Mutex）。

<a id="a0215608e40123de4a3a79ca440c6c593"></a>

### 80.3.13\_`node`

```c
sys_dnode_t usb_device::node
```

双向链表（Doubly Linked List，dlist）节点

<a id="a1b3f4becfd9fbfae80074fc2e76ea6a8"></a>

### 80.3.14\_`speed`

```c
enum usb_device_speed usb_device::speed
```

设备速率。

> 译注（源码核对）：该枚举存在SuperSpeed值，但当前设备初始化的最大包长检查明确对USB_SPEED_SPEED_SS返回-ENOTSUP；枚举存在不代表主机栈已支持该速率。

<a id="aa75bbea6a879460b39216453323d177f"></a>

### 80.3.15\_`state`

```c
enum usb_device_state usb_device::state
```

设备状态。

<a id="ae0c9c3454eea32432ddb4f8da7361182"></a>

### 80.3.16\_`tt`

```c
uint16_t usb_device::tt
```

设备所连接集线器的处理等待时间（Think Time）。

## 80.4\_源码跟踪与使用边界

译注依据保存的[官方主机头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/usbh.h)、[UHC头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/drivers/usb/uhc.h)、[生命周期实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_api.c)、[类匹配实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_class.c)、[类回调包装](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_class_api.h)、[设备管理](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_device.c)及[事件处理](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_core.c)，摘要见[来源记录](../SOURCES.md)。本仓库的[主机头文件](../../../include/zephyr/usb/usbh.h)、[UHC头文件](../../../include/zephyr/drivers/usb/uhc.h)与[主机栈目录](../../../subsys/usb/host)可用于源码跟踪，版本可能与网页不同。本批未构建、运行或操作USB硬件。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P079_USB主机核心API.md) · [返回大纲](大纲.md) · [下一章](P081_USB主机接口对象.md)
