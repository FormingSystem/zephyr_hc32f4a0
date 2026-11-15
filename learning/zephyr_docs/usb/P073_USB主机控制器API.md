---
id: learning.zephyr-docs.usb.api-73
title: USB主机控制器API
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__uhc__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第73章\_USB主机控制器API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__uhc__api.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 73.1\_阅读说明与来源

译注：本页说明USB主机控制器（USB Host Controller，UHC）的公开声明。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

USB主机控制器（USB Host Controller，UHC）驱动API。

USB主机控制器（USB Host Controller，UHC）驱动API。

引入版本（Since）：3.3。

接口版本（Version）：0.1.1。

## 73.2\_数据结构（Data Structures）

<a id="r_usb_5Fhost_5Finterface"></a>

```c
struct usb_host_interface
```



相关声明：[usb_host_interface](P081_USB主机接口对象.md)。

<a id="r_usb_5Fhost_5Fep"></a>

```c
struct usb_host_ep
```



相关声明：[usb_host_ep](P082_USB主机端点对象.md)。

<a id="r_usb_5Fdevice"></a>

```c
struct usb_device
```

USB设备在主机侧的表示。

相关声明：[usb_device](P080_USB主机设备对象.md)。

<a id="r_uhc_5Ftransfer"></a>

```c
struct uhc_transfer
```

UHC端点缓冲区信息。

相关声明：[uhc_transfer](P077_USB主机传输结构.md)。

<a id="r_uhc_5Fevent"></a>

```c
struct uhc_event
```

USB主机控制器事件。

相关声明：[uhc_event](P076_USB主机控制器事件.md)。

<a id="r_uhc_5Fdevice_5Fcaps"></a>

```c
struct uhc_device_caps
```

USB主机控制器能力。

相关声明：[uhc_device_caps](P075_USB主机控制器能力.md)。

<a id="r_uhc_5Fdata"></a>

```c
struct uhc_data
```

UHC驱动公共数据结构。

相关声明：[uhc_data](P074_USB主机控制器数据.md)。

## 73.3\_宏定义（Macros）

<a id="r_ga1b1ec49cb7649ece6ec5a31dac3e2537"></a>

```c
#define UHC_INTERFACES_MAX 32
```



相关声明：[UHC_INTERFACES_MAX](P073_USB主机控制器API.md#ga1b1ec49cb7649ece6ec5a31dac3e2537)。

<a id="r_ga09ad6fc9251212fa0dffececb767ff9e"></a>

```c
#define UHC_STATUS_INITIALIZED 0
```

控制器已通过uhc_init()初始化。

相关声明：[UHC_STATUS_INITIALIZED](P073_USB主机控制器API.md#ga09ad6fc9251212fa0dffececb767ff9e)。

<a id="r_ga230e104bd7be1d4b83b2d31ee72ac3c4"></a>

```c
#define UHC_STATUS_ENABLED 1
```

控制器已启用，全部API函数可用。

相关声明：[UHC_STATUS_ENABLED](P073_USB主机控制器API.md#ga230e104bd7be1d4b83b2d31ee72ac3c4)。

## 73.4\_类型定义（Typedefs）

<a id="r_ga3cda056094ceef79dd62ad9c6852daf9"></a>

```c
typedef int(* uhc_event_cb_t) (const struct device *dev, const struct uhc_event *const event)
```

将UHC事件提交到上层的回调函数（Callback）。

相关声明：[uhc_event_cb_t](P073_USB主机控制器API.md#ga3cda056094ceef79dd62ad9c6852daf9)、[device](../device_reference/P002_设备对象结构.md)、[uhc_event](P076_USB主机控制器事件.md)。

## 73.5\_枚举（Enumerations）

<a id="r_ga7127ac2a46b577f2aa1bb9a650e62a3f"></a>

```c
enum usb_device_state {
    USB_STATE_NOTCONNECTED,
    USB_STATE_DEFAULT,
    USB_STATE_ADDRESSED,
    USB_STATE_CONFIGURED
}
```

USB设备状态（Device State）。

相关声明：[usb_device_state](P073_USB主机控制器API.md#ga7127ac2a46b577f2aa1bb9a650e62a3f)、[USB_STATE_NOTCONNECTED](P073_USB主机控制器API.md#gga7127ac2a46b577f2aa1bb9a650e62a3fa70367cdc7b5d7d1f3ab046391f50df9d)、[USB_STATE_DEFAULT](P073_USB主机控制器API.md#gga7127ac2a46b577f2aa1bb9a650e62a3fabb0f4a1c2f62f028bec1d0b55b5d5554)、[USB_STATE_ADDRESSED](P073_USB主机控制器API.md#gga7127ac2a46b577f2aa1bb9a650e62a3fad7f0841a21d3179c13f19d3ae8a8e3b6)、[USB_STATE_CONFIGURED](P073_USB主机控制器API.md#gga7127ac2a46b577f2aa1bb9a650e62a3fa6566e87fb6d54f2da5b7564743df7a47)。

<a id="r_ga59ba7bbb99177a622f3c073fc48b7bc5"></a>

```c
enum usb_device_speed {
    USB_SPEED_UNKNOWN,
    USB_SPEED_SPEED_LS,
    USB_SPEED_SPEED_FS,
    USB_SPEED_SPEED_HS,
    USB_SPEED_SPEED_SS
}
```

USB设备工作速率（Operating Speed）。

相关声明：[usb_device_speed](P073_USB主机控制器API.md#ga59ba7bbb99177a622f3c073fc48b7bc5)、[USB_SPEED_UNKNOWN](P073_USB主机控制器API.md#gga59ba7bbb99177a622f3c073fc48b7bc5ac9755ae6b86f8148054fd6a342c74acc)、[USB_SPEED_SPEED_LS](P073_USB主机控制器API.md#gga59ba7bbb99177a622f3c073fc48b7bc5a46c4232a37347ac22ac14b240abddbdc)、[USB_SPEED_SPEED_FS](P073_USB主机控制器API.md#gga59ba7bbb99177a622f3c073fc48b7bc5a8cd687699d8afb4d818595d70b189e27)、[USB_SPEED_SPEED_HS](P073_USB主机控制器API.md#gga59ba7bbb99177a622f3c073fc48b7bc5aab0ef8e9a798d70fd3c93e68785c0968)、[USB_SPEED_SPEED_SS](P073_USB主机控制器API.md#gga59ba7bbb99177a622f3c073fc48b7bc5a36e25f2ed5532d6a281abaf521583fcc)。

<a id="r_gaef9b0703714676c1f7bd1cad57f49bc8"></a>

```c
enum uhc_control_stage {
    UHC_CONTROL_STAGE_SETUP = 0,
    UHC_CONTROL_STAGE_DATA,
    UHC_CONTROL_STAGE_STATUS
}
```

USB控制传输阶段（Control Transfer Stage）。

相关声明：[uhc_control_stage](P073_USB主机控制器API.md#gaef9b0703714676c1f7bd1cad57f49bc8)、[UHC_CONTROL_STAGE_SETUP](P073_USB主机控制器API.md#ggaef9b0703714676c1f7bd1cad57f49bc8a3f3c131b3a97a552d2917bbddcd9afc8)、[UHC_CONTROL_STAGE_DATA](P073_USB主机控制器API.md#ggaef9b0703714676c1f7bd1cad57f49bc8a2179067786eb86aad804d0aead9d71a5)、[UHC_CONTROL_STAGE_STATUS](P073_USB主机控制器API.md#ggaef9b0703714676c1f7bd1cad57f49bc8a7bd9f0423e9f50266905c3736e12468f)。

<a id="r_gabaf69c1e69fe0fb3d912b92daf8754eb"></a>

```c
enum uhc_event_type {
    UHC_EVT_DEV_CONNECTED_LS,
    UHC_EVT_DEV_CONNECTED_FS,
    UHC_EVT_DEV_CONNECTED_HS,
    UHC_EVT_DEV_REMOVED,
    UHC_EVT_RESETED,
    UHC_EVT_SUSPENDED,
    UHC_EVT_RESUMED,
    UHC_EVT_RWUP,
    UHC_EVT_EP_REQUEST,
    UHC_EVT_ERROR
}
```

USB主机控制器事件类型。

相关声明：[uhc_event_type](P073_USB主机控制器API.md#gabaf69c1e69fe0fb3d912b92daf8754eb)、[UHC_EVT_DEV_CONNECTED_LS](P073_USB主机控制器API.md#ggabaf69c1e69fe0fb3d912b92daf8754ebae0a316b8f60df97f30f54630f6847f70)、[UHC_EVT_DEV_CONNECTED_FS](P073_USB主机控制器API.md#ggabaf69c1e69fe0fb3d912b92daf8754eba98d87b3c737c234918fed0ce4589f4ce)、[UHC_EVT_DEV_CONNECTED_HS](P073_USB主机控制器API.md#ggabaf69c1e69fe0fb3d912b92daf8754eba923b6cfe57c254e22b57eab88c84b67f)、[UHC_EVT_DEV_REMOVED](P073_USB主机控制器API.md#ggabaf69c1e69fe0fb3d912b92daf8754ebab7c4181ad631b127cc50605f7864bc30)、[UHC_EVT_RESETED](P073_USB主机控制器API.md#ggabaf69c1e69fe0fb3d912b92daf8754ebafb131548cc66e748e562ee88df274ab3)、[UHC_EVT_SUSPENDED](P073_USB主机控制器API.md#ggabaf69c1e69fe0fb3d912b92daf8754ebab28885b8210133d4f0c2b532561c9c7a)、[UHC_EVT_RESUMED](P073_USB主机控制器API.md#ggabaf69c1e69fe0fb3d912b92daf8754ebad874caf1d7338081d185634e12f69848)、[UHC_EVT_RWUP](P073_USB主机控制器API.md#ggabaf69c1e69fe0fb3d912b92daf8754ebaa616f846752aacb8029f9b21747c656e)、[UHC_EVT_EP_REQUEST](P073_USB主机控制器API.md#ggabaf69c1e69fe0fb3d912b92daf8754eba5cdc8afb59f760c4dc9b2de314d05483)、[UHC_EVT_ERROR](P073_USB主机控制器API.md#ggabaf69c1e69fe0fb3d912b92daf8754ebae5970877eb9b6426132d8955cdeb26d7)。

## 73.6\_函数（Functions）

<a id="r_ga3251967d36b67169d7892a615323c14e"></a>

```c
static bool uhc_is_initialized (const struct device *dev)
```

检查控制器是否已初始化。

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[uhc_is_initialized](P073_USB主机控制器API.md#ga3251967d36b67169d7892a615323c14e)、[device](../device_reference/P002_设备对象结构.md)。

<a id="r_ga09b71dc5c334f09fb92cf37e2ecf51eb"></a>

```c
static bool uhc_is_enabled (const struct device *dev)
```

检查控制器是否已启用。

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[uhc_is_enabled](P073_USB主机控制器API.md#ga09b71dc5c334f09fb92cf37e2ecf51eb)、[device](../device_reference/P002_设备对象结构.md)。

<a id="r_ga4ceb0400168cd53201f0dde5f596452f"></a>

```c
static int uhc_bus_reset (const struct device *dev)
```

复位USB总线。

相关声明：[uhc_bus_reset](P073_USB主机控制器API.md#ga4ceb0400168cd53201f0dde5f596452f)、[device](../device_reference/P002_设备对象结构.md)。

<a id="r_gafe55e97cbf31d163b10616c03da39414"></a>

```c
static int uhc_sof_enable (const struct device *dev)
```

启用帧起始（Start of Frame，SOF）生成器。

相关声明：[uhc_sof_enable](P073_USB主机控制器API.md#gafe55e97cbf31d163b10616c03da39414)、[device](../device_reference/P002_设备对象结构.md)。

<a id="r_ga897081ff02dab4377c68bcba343f492c"></a>

```c
static int uhc_bus_suspend (const struct device *dev)
```

挂起USB总线。

相关声明：[uhc_bus_suspend](P073_USB主机控制器API.md#ga897081ff02dab4377c68bcba343f492c)、[device](../device_reference/P002_设备对象结构.md)。

<a id="r_ga6669bc2ac56395b38292fa796b99bfd9"></a>

```c
static int uhc_bus_resume (const struct device *dev)
```

恢复USB总线。

相关声明：[uhc_bus_resume](P073_USB主机控制器API.md#ga6669bc2ac56395b38292fa796b99bfd9)、[device](../device_reference/P002_设备对象结构.md)。

<a id="r_gab5a2df4d176d4c85751c3158b63e366b"></a>

```c
struct uhc_transfer * uhc_xfer_alloc (const struct device *dev, const uint8_t ep, struct usb_device *const udev, void *const cb, void *const cb_priv)
```

分配UHC传输对象（Transfer）。

相关声明：[uhc_transfer](P077_USB主机传输结构.md)、[uhc_xfer_alloc](P073_USB主机控制器API.md#gab5a2df4d176d4c85751c3158b63e366b)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[usb_device](P080_USB主机设备对象.md)。

<a id="r_ga75c2142698a15c547ab76ab76c89c177"></a>

```c
struct uhc_transfer * uhc_xfer_alloc_with_buf (const struct device *dev, const uint8_t ep, struct usb_device *const udev, void *const cb, void *const cb_priv, size_t size)
```

分配带缓冲区的UHC传输对象。

相关声明：[uhc_transfer](P077_USB主机传输结构.md)、[uhc_xfer_alloc_with_buf](P073_USB主机控制器API.md#ga75c2142698a15c547ab76ab76c89c177)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[usb_device](P080_USB主机设备对象.md)。

<a id="r_ga69748d0650399a51672b98b475ab8437"></a>

```c
void uhc_xfer_ref (struct uhc_transfer *const xfer)
```

增加UHC传输对象的引用计数。

相关声明：[uhc_xfer_ref](P073_USB主机控制器API.md#ga69748d0650399a51672b98b475ab8437)、[uhc_transfer](P077_USB主机传输结构.md)。

<a id="r_gab399b0ad7f6d856251af56cd92240351"></a>

```c
bool uhc_xfer_unref (struct uhc_transfer *const xfer)
```

减少UHC传输对象的引用计数。

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[uhc_xfer_unref](P073_USB主机控制器API.md#gab399b0ad7f6d856251af56cd92240351)、[uhc_transfer](P077_USB主机传输结构.md)。

<a id="r_gab2f6328e8051559edccc05ae3552f4f9"></a>

```c
int uhc_xfer_free (const struct device *dev, struct uhc_transfer *const xfer)
```

释放UHC传输对象及其全部缓冲区。

相关声明：[uhc_xfer_free](P073_USB主机控制器API.md#gab2f6328e8051559edccc05ae3552f4f9)、[device](../device_reference/P002_设备对象结构.md)、[uhc_transfer](P077_USB主机传输结构.md)。

<a id="r_ga779dbd7ee8ac5fce487e087706791ea7"></a>

```c
int uhc_xfer_buf_add (const struct device *dev, struct uhc_transfer *const xfer, struct net_buf *buf)
```

添加UHC传输缓冲区。

相关声明：[uhc_xfer_buf_add](P073_USB主机控制器API.md#ga779dbd7ee8ac5fce487e087706791ea7)、[device](../device_reference/P002_设备对象结构.md)、[uhc_transfer](P077_USB主机传输结构.md)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

<a id="r_gab4f7439fab8c57e203862bc408a6e46b"></a>

```c
struct net_buf * uhc_xfer_buf_alloc (const struct device *dev, const size_t size)
```

分配UHC传输缓冲区。

相关声明：[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)、[uhc_xfer_buf_alloc](P073_USB主机控制器API.md#gab4f7439fab8c57e203862bc408a6e46b)、[device](../device_reference/P002_设备对象结构.md)。

<a id="r_gac4bd26a85f8abc2006ecf2622669d615"></a>

```c
void uhc_xfer_buf_free (const struct device *dev, struct net_buf *const buf)
```

释放UHC请求缓冲区。

相关声明：[uhc_xfer_buf_free](P073_USB主机控制器API.md#gac4bd26a85f8abc2006ecf2622669d615)、[device](../device_reference/P002_设备对象结构.md)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

<a id="r_ga7a07b598c00d53393e15f6dae5cf1c4a"></a>

```c
int uhc_ep_enqueue (const struct device *dev, struct uhc_transfer *const xfer)
```

将USB主机控制器传输加入队列。

相关声明：[uhc_ep_enqueue](P073_USB主机控制器API.md#ga7a07b598c00d53393e15f6dae5cf1c4a)、[device](../device_reference/P002_设备对象结构.md)、[uhc_transfer](P077_USB主机传输结构.md)。

<a id="r_ga7c362cba29e0181ffcc8f70060100e62"></a>

```c
int uhc_ep_dequeue (const struct device *dev, struct uhc_transfer *const xfer)
```

从队列移除USB主机控制器传输。

相关声明：[uhc_ep_dequeue](P073_USB主机控制器API.md#ga7c362cba29e0181ffcc8f70060100e62)、[device](../device_reference/P002_设备对象结构.md)、[uhc_transfer](P077_USB主机传输结构.md)。

<a id="r_ga97beb6e3b3d4ad1b0b7664eae473e1be"></a>

```c
int uhc_init (const struct device *dev, uhc_event_cb_t event_cb, const void *const event_ctx)
```

初始化USB主机控制器。

相关声明：[uhc_init](P073_USB主机控制器API.md#ga97beb6e3b3d4ad1b0b7664eae473e1be)、[device](../device_reference/P002_设备对象结构.md)、[uhc_event_cb_t](P073_USB主机控制器API.md#ga3cda056094ceef79dd62ad9c6852daf9)。

<a id="r_gafe94b7f9e32aada9634166ebb2115c2f"></a>

```c
int uhc_enable (const struct device *dev)
```

启用USB主机控制器。

相关声明：[uhc_enable](P073_USB主机控制器API.md#gafe94b7f9e32aada9634166ebb2115c2f)、[device](../device_reference/P002_设备对象结构.md)。

<a id="r_ga9ec92df4497588adbf8da6f0777a4afd"></a>

```c
int uhc_disable (const struct device *dev)
```

停用USB主机控制器。

相关声明：[uhc_disable](P073_USB主机控制器API.md#ga9ec92df4497588adbf8da6f0777a4afd)、[device](../device_reference/P002_设备对象结构.md)。

<a id="r_gac6d1feb9481882a711e58c3e55e915cb"></a>

```c
int uhc_shutdown (const struct device *dev)
```

关闭USB主机控制器电源。

相关声明：[uhc_shutdown](P073_USB主机控制器API.md#gac6d1feb9481882a711e58c3e55e915cb)、[device](../device_reference/P002_设备对象结构.md)。

<a id="r_ga8796569eba96260ce332e611fb520033"></a>

```c
static struct uhc_device_caps uhc_caps (const struct device *dev)
```

获取USB主机控制器能力。

相关声明：[uhc_device_caps](P075_USB主机控制器能力.md)、[uhc_caps](P073_USB主机控制器API.md#ga8796569eba96260ce332e611fb520033)、[device](../device_reference/P002_设备对象结构.md)。

<a id="r_ga4468d1460d79dc30b2605e36ba478e40"></a>

```c
static const void * uhc_get_event_ctx (const struct device *dev)
```

获取指向上层上下文（Context）的指针。

相关声明：[uhc_get_event_ctx](P073_USB主机控制器API.md#ga4468d1460d79dc30b2605e36ba478e40)、[device](../device_reference/P002_设备对象结构.md)。

## 73.7\_详细说明（Detailed Documentation）

<a id="ga1b1ec49cb7649ece6ec5a31dac3e2537"></a>

### 73.7.1\_`UHC\_INTERFACES\_MAX`

```c
#define UHC_INTERFACES_MAX 32
```

```c
#include <zephyr/drivers/usb/uhc.h>
```

<a id="ga230e104bd7be1d4b83b2d31ee72ac3c4"></a>

### 73.7.2\_`UHC\_STATUS\_ENABLED`

```c
#define UHC_STATUS_ENABLED 1
```

```c
#include <zephyr/drivers/usb/uhc.h>
```

控制器已启用，全部API函数可用。

> 译注（源码核对）：这是状态位号1。已启用并不取消各API的调用前提，也不表示已有设备枚举完成；总线操作与传输结果仍需单独检查。

<a id="ga09ad6fc9251212fa0dffececb767ff9e"></a>

### 73.7.3\_`UHC\_STATUS\_INITIALIZED`

```c
#define UHC_STATUS_INITIALIZED 0
```

```c
#include <zephyr/drivers/usb/uhc.h>
```

控制器已通过uhc_init()初始化。

> 译注（源码核对）：这是atomic状态位的位号0，不是“未初始化”的状态值；启用位对应位号1。应使用查询接口，而不是把宏当作整个状态字比较。

<a id="ga3cda056094ceef79dd62ad9c6852daf9"></a>

### 73.7.4\_`uhc\_event\_cb\_t`

```c
typedef int(* uhc_event_cb_t) (const struct device *dev, const struct uhc_event *const event)
```

```c
#include <zephyr/drivers/usb/uhc.h>
```

将UHC事件提交到上层的回调函数（Callback）。

上层应将事件放入消息队列（Message Queue）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例device结构体的指针 |
| `[in] event` | 指向事件结构体的指针 |

**返回（Returns）**：成功时为0，其他值均应视为错误。

> 译注（源码核对）：当前公共实现把事件结构建立在调用栈上，再同步调用event_cb；上层必须在回调返回前复制事件内容，不能仅保存该临时指针。当前主机栈用K_NO_WAIT将事件副本放入消息队列，队列满可能失败；传输完成路径调用回调后不检查返回值，也不自动重投事件。

<a id="gaef9b0703714676c1f7bd1cad57f49bc8"></a>

### 73.7.5\_`uhc\_control\_stage`

```c
enum uhc_control_stage
```

```c
#include <zephyr/drivers/usb/uhc.h>
```

USB控制传输阶段（Control Transfer Stage）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `UHC_CONTROL_STAGE_SETUP` |  |
| `UHC_CONTROL_STAGE_DATA` |  |
| `UHC_CONTROL_STAGE_STATUS` |  |

<a id="gabaf69c1e69fe0fb3d912b92daf8754eb"></a>

### 73.7.6\_`uhc\_event\_type`

```c
enum uhc_event_type
```

```c
#include <zephyr/drivers/usb/uhc.h>
```

USB主机控制器事件类型。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `UHC_EVT_DEV_CONNECTED_LS` | 低速（Low Speed）设备已连接。 |
| `UHC_EVT_DEV_CONNECTED_FS` | 全速（Full Speed）设备已连接。 |
| `UHC_EVT_DEV_CONNECTED_HS` | 高速（High Speed）设备已连接。 |
| `UHC_EVT_DEV_REMOVED` | 设备（外设）已移除。 |
| `UHC_EVT_RESETED` | 总线复位操作已完成。 |
| `UHC_EVT_SUSPENDED` | 总线挂起操作已完成。 |
| `UHC_EVT_RESUMED` | 总线恢复操作已完成。 |
| `UHC_EVT_RWUP` | 远程唤醒（Remote Wakeup）信号。 |
| `UHC_EVT_EP_REQUEST` | 端点请求结果事件。 |
| `UHC_EVT_ERROR` | 不可纠正的错误事件，需要上层或应用关注。 |

<a id="ga59ba7bbb99177a622f3c073fc48b7bc5"></a>

### 73.7.7\_`usb\_device\_speed`

```c
enum usb_device_speed
```

```c
#include <zephyr/drivers/usb/uhc.h>
```

USB设备工作速率（Operating Speed）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `USB_SPEED_UNKNOWN` | 设备可能未连接。 |
| `USB_SPEED_SPEED_LS` | 低速（Low Speed）。 |
| `USB_SPEED_SPEED_FS` | 全速（Full Speed）。 |
| `USB_SPEED_SPEED_HS` | 高速（High Speed）。 |
| `USB_SPEED_SPEED_SS` | 超速（SuperSpeed）。 |

<a id="ga7127ac2a46b577f2aa1bb9a650e62a3f"></a>

### 73.7.8\_`usb\_device\_state`

```c
enum usb_device_state
```

```c
#include <zephyr/drivers/usb/uhc.h>
```

USB设备状态（Device State）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `USB_STATE_NOTCONNECTED` |  |
| `USB_STATE_DEFAULT` |  |
| `USB_STATE_ADDRESSED` |  |
| `USB_STATE_CONFIGURED` |  |

<a id="ga4ceb0400168cd53201f0dde5f596452f"></a>

### 73.7.9\_`uhc\_bus\_reset()`

```c
static inline int uhc_bus_reset ( const struct device * dev)
```

```c
#include <zephyr/drivers/usb/uhc.h>
```

复位USB总线。

执行USB总线复位；复位信号结束时，控制器可能发出UHC_EVT_RESETED事件。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例device结构体的指针 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EBUSY` | 控制器已在执行总线操作 |

**返回（Returns）**：成功时为0，其他值均应视为错误。

> 译注（源码核对）：公共包装不单独检查初始化／启用位或总线忙状态，直接在驱动锁内转发bus_reset。原文列出的错误和事件描述需结合具体驱动实现理解。

<a id="ga6669bc2ac56395b38292fa796b99bfd9"></a>

### 73.7.10\_`uhc\_bus\_resume()`

```c
static inline int uhc_bus_resume ( const struct device * dev)
```

```c
#include <zephyr/drivers/usb/uhc.h>
```

恢复USB总线。

发出至少20毫秒的恢复信号，并在USB总线恢复信号结束时发出UHC_EVT_RESUMED事件；SOF生成器随后应在3毫秒内启动。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例device结构体的指针 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EBUSY` | 控制器已在执行总线操作 |

**返回（Returns）**：成功时为0，其他值均应视为错误。

> 译注（源码核对）：公共内联包装只加锁并调用驱动bus_resume，不自行执行20毫秒／3毫秒定时；时序与事件实现需要核对具体控制器驱动。虚拟控制器用于模型交互，不能作为物理信号时序的实测证据。

<a id="ga897081ff02dab4377c68bcba343f492c"></a>

### 73.7.11\_`uhc\_bus\_suspend()`

```c
static inline int uhc_bus_suspend ( const struct device * dev)
```

```c
#include <zephyr/drivers/usb/uhc.h>
```

挂起USB总线。

停用SOF生成器，并在USB总线挂起时发出UHC_EVT_SUSPENDED事件。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例device结构体的指针 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EALREADY` | 已经挂起 |

**返回（Returns）**：成功时为0，其他值均应视为错误。

<a id="ga8796569eba96260ce332e611fb520033"></a>

### 73.7.12\_`uhc\_caps()`

```c
static inline struct uhc_device_caps uhc_caps ( const struct device * dev)
```

```c
#include <zephyr/drivers/usb/uhc.h>
```

获取USB主机控制器能力。

获取控制器能力，例如高速（High Speed，HS）能力等。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例device结构体的指针 |

**返回（Returns）**：USB主机控制器能力。

<a id="ga9ec92df4497588adbf8da6f0777a4afd"></a>

### 73.7.13\_`uhc\_disable()`

```c
int uhc_disable ( const struct device * dev)
```

```c
#include <zephyr/drivers/usb/uhc.h>
```

停用USB主机控制器。

停用已启用的USB主机控制器。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例device结构体的指针 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EALREADY` | 已经停用 |

**返回（Returns）**：成功时为0，其他值均应视为错误。

> 译注（源码核对）：当前公共实现调用驱动disable后，即使驱动返回错误也清除ENABLED位。因此查询结果为false不能单独证明硬件已成功停用，必须同时处理返回码。

<a id="gafe94b7f9e32aada9634166ebb2115c2f"></a>

### 73.7.14\_`uhc\_enable()`

```c
int uhc_enable ( const struct device * dev)
```

```c
#include <zephyr/drivers/usb/uhc.h>
```

启用USB主机控制器。

启用已供电的USB主机控制器，使主机栈能够识别和枚举设备。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例device结构体的指针 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EPERM` | 控制器尚未初始化 |
| `-EALREADY` | 已经启用 |

**返回（Returns）**：成功时为0，其他值均应视为错误。

<a id="ga7c362cba29e0181ffcc8f70060100e62"></a>

### 73.7.15\_`uhc\_ep\_dequeue()`

```c
int uhc_ep_dequeue ( const struct device * dev, struct uhc_transfer *const xfer )
```

```c
#include <zephyr/drivers/usb/uhc.h>
```

从队列移除USB主机控制器传输。

尚未实现。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例device结构体的指针 |
| `[in] xfer` | 指向UHC传输对象的指针 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EPERM` | 控制器尚未初始化 |

**返回（Returns）**：成功时为0，其他值均应视为错误。

> 译注（源码核对）：原文“尚未实现”已不符合当前公共实现：它调用驱动ep_dequeue，并在返回后清除queued，即使驱动返回错误也会清除。具体取消方式仍由驱动决定；虚拟驱动将对象标记为-ECONNRESET，稍后清理并报告完成。不能仅以queued变0认定取消和回调均已完成。

<a id="ga7a07b598c00d53393e15f6dae5cf1c4a"></a>

### 73.7.16\_`uhc\_ep\_enqueue()`

```c
int uhc_ep_enqueue ( const struct device * dev, struct uhc_transfer *const xfer )
```

```c
#include <zephyr/drivers/usb/uhc.h>
```

将USB主机控制器传输加入队列。

将传输加入队列；若队列为空，控制器可立即接手该传输。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例device结构体的指针 |
| `[in] xfer` | 指向UHC传输对象的指针 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EPERM` | 控制器尚未初始化 |

**返回（Returns）**：成功时为0，其他值均应视为错误。

> 译注（源码核对）：公共层检查INITIALIZED后设置queued、增加一次传输对象引用，再调用驱动；驱动入队失败则清除queued并撤销该引用。它没有在公共层检查ENABLED，也没有拦截重复提交同一对象；调用者必须按栈／驱动的状态和所有权约定提交。

<a id="ga4468d1460d79dc30b2605e36ba478e40"></a>

### 73.7.17\_`uhc\_get\_event\_ctx()`

```c
static inline const void * uhc_get_event_ctx ( const struct device * dev)
```

```c
#include <zephyr/drivers/usb/uhc.h>
```

获取指向上层上下文（Context）的指针。

上下文地址作为参数传给uhc_init()，并保存在UHC数据中。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例device结构体的指针 |

**返回（Returns）**：指向上层上下文的不透明指针（Opaque Pointer）。

<a id="ga97beb6e3b3d4ad1b0b7664eae473e1be"></a>

### 73.7.18\_`uhc\_init()`

```c
int uhc_init ( const struct device * dev, uhc_event_cb_t event_cb, const void *const event_ctx )
```

```c
#include <zephyr/drivers/usb/uhc.h>
```

初始化USB主机控制器。

初始化USB主机控制器。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例device结构体的指针 |
| `[in] event_cb` | 来自上层（USB主机栈）的事件回调 |
| `[in] event_ctx` | 指向上层上下文的不透明指针 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | 参数错误，未传入回调函数 |
| `-EALREADY` | 已经初始化 |

**返回（Returns）**：成功时为0，其他值均应视为错误。

> 译注（源码核对）：公共实现只要求event_cb非NULL，允许event_ctx为NULL；当前主机栈自身传入有效上下文以供事件线程使用。初始化驱动成功才设置INITIALIZED位，初始化不自动启用控制器。

<a id="ga09b71dc5c334f09fb92cf37e2ecf51eb"></a>

### 73.7.19\_`uhc\_is\_enabled()`

```c
static inline bool uhc_is_enabled ( const struct device * dev)
```

```c
#include <zephyr/drivers/usb/uhc.h>
```

检查控制器是否已启用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例device结构体的指针 |

**返回（Returns）**：控制器已启用时为true，否则为false。

<a id="ga3251967d36b67169d7892a615323c14e"></a>

### 73.7.20\_`uhc\_is\_initialized()`

```c
static inline bool uhc_is_initialized ( const struct device * dev)
```

```c
#include <zephyr/drivers/usb/uhc.h>
```

检查控制器是否已初始化。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例device结构体的指针 |

**返回（Returns）**：控制器已初始化时为true，否则为false。

<a id="gac6d1feb9481882a711e58c3e55e915cb"></a>

### 73.7.21\_`uhc\_shutdown()`

```c
int uhc_shutdown ( const struct device * dev)
```

```c
#include <zephyr/drivers/usb/uhc.h>
```

关闭USB主机控制器电源。

完全关闭控制器，以降低能耗或改变控制器角色。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例device结构体的指针 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EALREADY` | 控制器已经处于未初始化状态 |

**返回（Returns）**：成功时为0，其他值均应视为错误。

> 译注（源码核对）：当前公共实现先检查控制器是否仍启用，是则返回-EBUSY；应先完成停用。调用驱动shutdown后，无论驱动返回值如何都会清除INITIALIZED位。

<a id="gafe55e97cbf31d163b10616c03da39414"></a>

### 73.7.22\_`uhc\_sof\_enable()`

```c
static inline int uhc_sof_enable ( const struct device * dev)
```

```c
#include <zephyr/drivers/usb/uhc.h>
```

启用帧起始（Start of Frame，SOF）生成器。

启用SOF生成器。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例device结构体的指针 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EALREADY` | 已经启用 |

**返回（Returns）**：成功时为0，其他值均应视为错误。

> 译注（源码核对）：公共层只是加锁转发；并非所有驱动都用相同方式报告重复启用。例如当前虚拟驱动重启SOF定时器并返回0。

<a id="gab5a2df4d176d4c85751c3158b63e366b"></a>

### 73.7.23\_`uhc\_xfer\_alloc()`

```c
struct uhc_transfer * uhc_xfer_alloc ( const struct device * dev, const uint8_t ep, struct usb_device *const udev, void *const cb, void *const cb_priv )
```

```c
#include <zephyr/drivers/usb/uhc.h>
```

分配UHC传输对象（Transfer）。

从公共传输对象池（Transfer Pool）分配新传输对象。分配后不带缓冲区，但可以从不同缓冲区池中分配并添加缓冲区。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例device结构体的指针 |
| `[in] ep` | 端点地址（Endpoint Address） |
| `[in] udev` | 指向USB设备的指针 |
| `[in] cb` | 传输完成回调 |
| `[in] cb_priv` | 完成回调的私有数据 |

**返回（Returns）**：指向已分配传输对象的指针，错误时为NULL。

> 译注（源码核对）：当前实现先检查控制器已初始化，并从有效udev及端点描述符提取类型、最大包长和间隔。非零端点尚未配置，或对象池不足时，都可能返回NULL；不能只把NULL解释为内存不足。分配使用K_NO_WAIT，新对象的buf为NULL，cb与私有数据指针只保存而不复制指向对象。

<a id="ga75c2142698a15c547ab76ab76c89c177"></a>

### 73.7.24\_`uhc\_xfer\_alloc\_with\_buf()`

```c
struct uhc_transfer * uhc_xfer_alloc_with_buf ( const struct device * dev, const uint8_t ep, struct usb_device *const udev, void *const cb, void *const cb_priv, size_t size )
```

```c
#include <zephyr/drivers/usb/uhc.h>
```

分配带缓冲区的UHC传输对象。

从公共传输对象池分配带缓冲区的新传输对象。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例device结构体的指针 |
| `[in] ep` | 端点地址（Endpoint Address） |
| `[in] udev` | 指向USB设备的指针 |
| `[in] cb` | 传输完成回调 |
| `[in] cb_priv` | 完成回调的私有数据 |
| `[in] size` | 缓冲区大小 |

**返回（Returns）**：指向已分配传输对象的指针，错误时为NULL。

> 译注（源码核对）：当前实现先分配net_buf，再分配传输对象；传输对象分配失败时释放先前取得的缓冲区，成功后把缓冲区指针放入xfer->buf。后续释放责任须结合下方free／unref说明判断。

<a id="ga779dbd7ee8ac5fce487e087706791ea7"></a>

### 73.7.25\_`uhc\_xfer\_buf\_add()`

```c
int uhc_xfer_buf_add ( const struct device * dev, struct uhc_transfer *const xfer, struct net_buf * buf )
```

```c
#include <zephyr/drivers/usb/uhc.h>
```

添加UHC传输缓冲区。

向传输对象添加先前分配的缓冲区。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例device结构体的指针 |
| `[in] xfer` | 指向UHC传输对象的指针 |
| `[in] buf` | 指向UHC请求缓冲区的指针 |

**返回（Returns）**：指向已分配请求的指针，错误时为NULL。

> 译注（源码核对）：原文“返回已分配请求指针或NULL”与int原型不符。当前实现返回0，或在xfer已入队时返回-EBUSY；成功时仅赋值xfer->buf，不增加buf引用，也不释放此前指向的缓冲区。替换前应先处理原缓冲区的所有权。

<a id="gab4f7439fab8c57e203862bc408a6e46b"></a>

### 73.7.26\_`uhc\_xfer\_buf\_alloc()`

```c
struct net_buf * uhc_xfer_buf_alloc ( const struct device * dev, const size_t size )
```

```c
#include <zephyr/drivers/usb/uhc.h>
```

分配UHC传输缓冲区。

从公共请求缓冲区池分配新缓冲区；如果xfer参数不为NULL，则将其赋给传输对象。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例device结构体的指针 |
| `[in] size` | 请求缓冲区大小 |

**返回（Returns）**：指向已分配请求的指针，错误时为NULL。

> 译注（源码核对）：当前原型只有dev和size，没有xfer参数；原文“xfer不为NULL时自动赋给传输对象”是遗留说明。实现只从公共池以K_NO_WAIT分配并返回net_buf，需要另行添加到传输对象或使用带缓冲区的分配接口。

<a id="gac4bd26a85f8abc2006ecf2622669d615"></a>

### 73.7.27\_`uhc\_xfer\_buf\_free()`

```c
void uhc_xfer_buf_free ( const struct device * dev, struct net_buf *const buf )
```

```c
#include <zephyr/drivers/usb/uhc.h>
```

释放UHC请求缓冲区。

将缓冲区归还到请求缓冲区池。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例device结构体的指针 |
| `[in] buf` | 指向UHC请求缓冲区的指针 |

<a id="gab2f6328e8051559edccc05ae3552f4f9"></a>

### 73.7.28\_`uhc\_xfer\_free()`

```c
int uhc_xfer_free ( const struct device * dev, struct uhc_transfer *const xfer )
```

```c
#include <zephyr/drivers/usb/uhc.h>
```

释放UHC传输对象及其全部缓冲区。

释放全部缓冲区，并将传输对象归还到传输对象池。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例device结构体的指针 |
| `[in] xfer` | 指向UHC传输对象的指针 |

**返回（Returns）**：成功时为0，其他值均应视为错误。

> 译注（源码核对）：当前实现仅调用uhc_xfer_unref()并返回0；最后一个引用释放时只归还传输对象内存，没有释放xfer->buf。原文“释放全部缓冲区”与此不符。当前主机栈的丢弃路径显式先调用uhc_xfer_buf_free()再unref传输对象，不能依赖本函数自动释放缓冲区。

<a id="ga69748d0650399a51672b98b475ab8437"></a>

### 73.7.29\_`uhc\_xfer\_ref()`

```c
void uhc_xfer_ref ( struct uhc_transfer *const xfer)
```

```c
#include <zephyr/drivers/usb/uhc.h>
```

增加UHC传输对象的引用计数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] xfer` | 指向有效UHC传输对象的指针 |

<a id="gab399b0ad7f6d856251af56cd92240351"></a>

### 73.7.30\_`uhc\_xfer\_unref()`

```c
bool uhc_xfer_unref ( struct uhc_transfer *const xfer)
```

```c
#include <zephyr/drivers/usb/uhc.h>
```

减少UHC传输对象的引用计数。

减少引用计数，最后一个引用消失时释放对象。可从任意上下文安全调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] xfer` | 指向有效UHC传输对象的指针 |

**返回（Returns）**：传输对象已释放时为true，否则为false。

> 译注（源码核对）：引用计数降到0后释放的是传输对象本身，当前释放回调不处理buf。传输对象引用和net_buf引用是两套计数；操作前须仍持有有效引用，不能在对象已释放后再次访问。

## 73.8\_源码跟踪与使用边界

译注依据保存的[官方头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/drivers/usb/uhc.h)、[公共实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/usb/uhc/uhc_common.c)、[虚拟控制器](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/usb/uhc/uhc_virtual.c)和[主机栈事件处理](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/usbh_core.c)，摘要见[来源记录](../SOURCES.md)。本仓库的[头文件](../../../include/zephyr/drivers/usb/uhc.h)、[公共实现](../../../drivers/usb/uhc/uhc_common.c)与[主机栈](../../../subsys/usb/host/usbh_core.c)可用于跟踪，版本可能与网页不同。此API仍为实验性接口，本批未编译或运行USB主机固件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>
<a id="header-define-members"></a>
<a id="define-members"></a>
<a id="header-typedef-members"></a>
<a id="typedef-members"></a>
<a id="header-enum-members"></a>
<a id="enum-members"></a>
<a id="header-func-members"></a>
<a id="func-members"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggaef9b0703714676c1f7bd1cad57f49bc8a3f3c131b3a97a552d2917bbddcd9afc8"></a>
<a id="ggaef9b0703714676c1f7bd1cad57f49bc8a2179067786eb86aad804d0aead9d71a5"></a>
<a id="ggaef9b0703714676c1f7bd1cad57f49bc8a7bd9f0423e9f50266905c3736e12468f"></a>
<a id="ggabaf69c1e69fe0fb3d912b92daf8754ebae0a316b8f60df97f30f54630f6847f70"></a>
<a id="ggabaf69c1e69fe0fb3d912b92daf8754eba98d87b3c737c234918fed0ce4589f4ce"></a>
<a id="ggabaf69c1e69fe0fb3d912b92daf8754eba923b6cfe57c254e22b57eab88c84b67f"></a>
<a id="ggabaf69c1e69fe0fb3d912b92daf8754ebab7c4181ad631b127cc50605f7864bc30"></a>
<a id="ggabaf69c1e69fe0fb3d912b92daf8754ebafb131548cc66e748e562ee88df274ab3"></a>
<a id="ggabaf69c1e69fe0fb3d912b92daf8754ebab28885b8210133d4f0c2b532561c9c7a"></a>
<a id="ggabaf69c1e69fe0fb3d912b92daf8754ebad874caf1d7338081d185634e12f69848"></a>
<a id="ggabaf69c1e69fe0fb3d912b92daf8754ebaa616f846752aacb8029f9b21747c656e"></a>
<a id="ggabaf69c1e69fe0fb3d912b92daf8754eba5cdc8afb59f760c4dc9b2de314d05483"></a>
<a id="ggabaf69c1e69fe0fb3d912b92daf8754ebae5970877eb9b6426132d8955cdeb26d7"></a>
<a id="gga59ba7bbb99177a622f3c073fc48b7bc5ac9755ae6b86f8148054fd6a342c74acc"></a>
<a id="gga59ba7bbb99177a622f3c073fc48b7bc5a46c4232a37347ac22ac14b240abddbdc"></a>
<a id="gga59ba7bbb99177a622f3c073fc48b7bc5a8cd687699d8afb4d818595d70b189e27"></a>
<a id="gga59ba7bbb99177a622f3c073fc48b7bc5aab0ef8e9a798d70fd3c93e68785c0968"></a>
<a id="gga59ba7bbb99177a622f3c073fc48b7bc5a36e25f2ed5532d6a281abaf521583fcc"></a>
<a id="gga7127ac2a46b577f2aa1bb9a650e62a3fa70367cdc7b5d7d1f3ab046391f50df9d"></a>
<a id="gga7127ac2a46b577f2aa1bb9a650e62a3fabb0f4a1c2f62f028bec1d0b55b5d5554"></a>
<a id="gga7127ac2a46b577f2aa1bb9a650e62a3fad7f0841a21d3179c13f19d3ae8a8e3b6"></a>
<a id="gga7127ac2a46b577f2aa1bb9a650e62a3fa6566e87fb6d54f2da5b7564743df7a47"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

[上一章](P072_USB主机控制器API说明.md) · [返回大纲](大纲.md) · [下一章](P074_USB主机控制器数据.md)
