---
id: learning.zephyr-docs.api-file-clock-network-reference.page-26
title: zephyr__drivers__usb__uhc.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/uhc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第26章\_zephyr\_\_drivers\_\_usb\_\_uhc.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/uhc_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

USB主控制器（UHC）的驱动API。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <zephyr/device.h>
#include <zephyr/net_buf.h>
#include <zephyr/drivers/usb/usb_buf.h>
#include <zephyr/usb/usb_ch9.h>
#include <zephyr/sys/dlist.h>
#include <zephyr/sys/ref.h>
```

查看此文件的源码。

USB主控制器（UHC）的驱动API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 26.1\_数据结构（Data Structures）

<a id="r_usb_5Fhost_5Finterface"></a>

```c
struct usb_host_interface
```

相关声明：[usb_host_interface](../usb/P081_USB主机接口对象.md)。

<a id="r_usb_5Fhost_5Fep"></a>

```c
struct usb_host_ep
```

相关声明：[usb_host_ep](../usb/P082_USB主机端点对象.md)。

<a id="r_usb_5Fdevice"></a>

```c
struct usb_device
```

相关声明：[usb_device](../usb/P080_USB主机设备对象.md)。

USB设备在主机端的表示（Host Representation）。

<a id="r_uhc_5Ftransfer"></a>

```c
struct uhc_transfer
```

相关声明：[uhc_transfer](../usb/P077_USB主机传输结构.md)。

USB主控制器（UHC）的端点缓冲区信息。

<a id="r_uhc_5Fevent"></a>

```c
struct uhc_event
```

相关声明：[uhc_event](../usb/P076_USB主机控制器事件.md)。

USB主控制器（Host Controller）的事件。

<a id="r_uhc_5Fdevice_5Fcaps"></a>

```c
struct uhc_device_caps
```

相关声明：[uhc_device_caps](../usb/P075_USB主机控制器能力.md)。

USB主控制器（Host Controller）的能力。

<a id="r_uhc_5Fdata"></a>

```c
struct uhc_data
```

相关声明：[uhc_data](../usb/P074_USB主机控制器数据.md)。

通用USB主控制器（UHC）驱动数据结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 26.2\_宏定义（Macros）

<a id="r_ga1b1ec49cb7649ece6ec5a31dac3e2537"></a>

```c
#define UHC_INTERFACES_MAX 32
```

相关声明：[UHC_INTERFACES_MAX](../usb/P073_USB主机控制器API.md#ga1b1ec49cb7649ece6ec5a31dac3e2537)。

<a id="r_ga09ad6fc9251212fa0dffececb767ff9e"></a>

```c
#define UHC_STATUS_INITIALIZED 0
```

相关声明：[UHC_STATUS_INITIALIZED](../usb/P073_USB主机控制器API.md#ga09ad6fc9251212fa0dffececb767ff9e)。

控制器已通过 uhc_init() 初始化。

<a id="r_ga230e104bd7be1d4b83b2d31ee72ac3c4"></a>

```c
#define UHC_STATUS_ENABLED 1
```

相关声明：[UHC_STATUS_ENABLED](../usb/P073_USB主机控制器API.md#ga230e104bd7be1d4b83b2d31ee72ac3c4)。

控制器已启用，所有 API 函数均可用。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 26.3\_类型定义（Typedefs）

<a id="r_ga3cda056094ceef79dd62ad9c6852daf9"></a>

```c
typedef int(* uhc_event_cb_t) (const struct device *dev, const struct uhc_event *const event)
```

相关声明：[uhc_event_cb_t](../usb/P073_USB主机控制器API.md#ga3cda056094ceef79dd62ad9c6852daf9)、[device](../device_reference/P002_设备对象结构.md)、[uhc_event](../usb/P076_USB主机控制器事件.md)。

向高层提交 USB 主机控制器事件（UHC Event）的回调。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 26.4\_枚举（Enumerations）

<a id="r_ga7127ac2a46b577f2aa1bb9a650e62a3f"></a>

```c
enum usb_device_state { USB_STATE_NOTCONNECTED , USB_STATE_DEFAULT , USB_STATE_ADDRESSED , USB_STATE_CONFIGURED }
```

相关声明：[usb_device_state](../usb/P073_USB主机控制器API.md#ga7127ac2a46b577f2aa1bb9a650e62a3f)、[USB_STATE_NOTCONNECTED](../usb/P073_USB主机控制器API.md#gga7127ac2a46b577f2aa1bb9a650e62a3fa70367cdc7b5d7d1f3ab046391f50df9d)、[USB_STATE_DEFAULT](../usb/P073_USB主机控制器API.md#gga7127ac2a46b577f2aa1bb9a650e62a3fabb0f4a1c2f62f028bec1d0b55b5d5554)、[USB_STATE_ADDRESSED](../usb/P073_USB主机控制器API.md#gga7127ac2a46b577f2aa1bb9a650e62a3fad7f0841a21d3179c13f19d3ae8a8e3b6)、[USB_STATE_CONFIGURED](../usb/P073_USB主机控制器API.md#gga7127ac2a46b577f2aa1bb9a650e62a3fa6566e87fb6d54f2da5b7564743df7a47)。

USB 设备状态（Device State）。

<a id="r_ga59ba7bbb99177a622f3c073fc48b7bc5"></a>

```c
enum usb_device_speed { USB_SPEED_UNKNOWN , USB_SPEED_SPEED_LS , USB_SPEED_SPEED_FS , USB_SPEED_SPEED_HS , USB_SPEED_SPEED_SS }
```

相关声明：[usb_device_speed](../usb/P073_USB主机控制器API.md#ga59ba7bbb99177a622f3c073fc48b7bc5)、[USB_SPEED_UNKNOWN](../usb/P073_USB主机控制器API.md#gga59ba7bbb99177a622f3c073fc48b7bc5ac9755ae6b86f8148054fd6a342c74acc)、[USB_SPEED_SPEED_LS](../usb/P073_USB主机控制器API.md#gga59ba7bbb99177a622f3c073fc48b7bc5a46c4232a37347ac22ac14b240abddbdc)、[USB_SPEED_SPEED_FS](../usb/P073_USB主机控制器API.md#gga59ba7bbb99177a622f3c073fc48b7bc5a8cd687699d8afb4d818595d70b189e27)、[USB_SPEED_SPEED_HS](../usb/P073_USB主机控制器API.md#gga59ba7bbb99177a622f3c073fc48b7bc5aab0ef8e9a798d70fd3c93e68785c0968)、[USB_SPEED_SPEED_SS](../usb/P073_USB主机控制器API.md#gga59ba7bbb99177a622f3c073fc48b7bc5a36e25f2ed5532d6a281abaf521583fcc)。

USB 设备运行速度（Operating Speed）。

<a id="r_gaef9b0703714676c1f7bd1cad57f49bc8"></a>

```c
enum uhc_control_stage { UHC_CONTROL_STAGE_SETUP = 0 , UHC_CONTROL_STAGE_DATA , UHC_CONTROL_STAGE_STATUS }
```

相关声明：[uhc_control_stage](../usb/P073_USB主机控制器API.md#gaef9b0703714676c1f7bd1cad57f49bc8)、[UHC_CONTROL_STAGE_SETUP](../usb/P073_USB主机控制器API.md#ggaef9b0703714676c1f7bd1cad57f49bc8a3f3c131b3a97a552d2917bbddcd9afc8)、[UHC_CONTROL_STAGE_DATA](../usb/P073_USB主机控制器API.md#ggaef9b0703714676c1f7bd1cad57f49bc8a2179067786eb86aad804d0aead9d71a5)、[UHC_CONTROL_STAGE_STATUS](../usb/P073_USB主机控制器API.md#ggaef9b0703714676c1f7bd1cad57f49bc8a7bd9f0423e9f50266905c3736e12468f)。

USB 控制传输阶段（Control Transfer Stage）。

<a id="r_gabaf69c1e69fe0fb3d912b92daf8754eb"></a>

```c
enum uhc_event_type { UHC_EVT_DEV_CONNECTED_LS , UHC_EVT_DEV_CONNECTED_FS , UHC_EVT_DEV_CONNECTED_HS , UHC_EVT_DEV_REMOVED , UHC_EVT_RESETED , UHC_EVT_SUSPENDED , UHC_EVT_RESUMED , UHC_EVT_RWUP , UHC_EVT_EP_REQUEST , UHC_EVT_ERROR }
```

相关声明：[uhc_event_type](../usb/P073_USB主机控制器API.md#gabaf69c1e69fe0fb3d912b92daf8754eb)、[UHC_EVT_DEV_CONNECTED_LS](../usb/P073_USB主机控制器API.md#ggabaf69c1e69fe0fb3d912b92daf8754ebae0a316b8f60df97f30f54630f6847f70)、[UHC_EVT_DEV_CONNECTED_FS](../usb/P073_USB主机控制器API.md#ggabaf69c1e69fe0fb3d912b92daf8754eba98d87b3c737c234918fed0ce4589f4ce)、[UHC_EVT_DEV_CONNECTED_HS](../usb/P073_USB主机控制器API.md#ggabaf69c1e69fe0fb3d912b92daf8754eba923b6cfe57c254e22b57eab88c84b67f)、[UHC_EVT_DEV_REMOVED](../usb/P073_USB主机控制器API.md#ggabaf69c1e69fe0fb3d912b92daf8754ebab7c4181ad631b127cc50605f7864bc30)、[UHC_EVT_RESETED](../usb/P073_USB主机控制器API.md#ggabaf69c1e69fe0fb3d912b92daf8754ebafb131548cc66e748e562ee88df274ab3)、[UHC_EVT_SUSPENDED](../usb/P073_USB主机控制器API.md#ggabaf69c1e69fe0fb3d912b92daf8754ebab28885b8210133d4f0c2b532561c9c7a)、[UHC_EVT_RESUMED](../usb/P073_USB主机控制器API.md#ggabaf69c1e69fe0fb3d912b92daf8754ebad874caf1d7338081d185634e12f69848)、[UHC_EVT_RWUP](../usb/P073_USB主机控制器API.md#ggabaf69c1e69fe0fb3d912b92daf8754ebaa616f846752aacb8029f9b21747c656e)、[UHC_EVT_EP_REQUEST](../usb/P073_USB主机控制器API.md#ggabaf69c1e69fe0fb3d912b92daf8754eba5cdc8afb59f760c4dc9b2de314d05483)、[UHC_EVT_ERROR](../usb/P073_USB主机控制器API.md#ggabaf69c1e69fe0fb3d912b92daf8754ebae5970877eb9b6426132d8955cdeb26d7)。

USB 主机控制器事件类型（Host Controller Event Types）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 26.5\_函数（Functions）

<a id="r_ga3251967d36b67169d7892a615323c14e"></a>

```c
static bool uhc_is_initialized (const struct device *dev)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[uhc_is_initialized](../usb/P073_USB主机控制器API.md#ga3251967d36b67169d7892a615323c14e)、[device](../device_reference/P002_设备对象结构.md)。

检查控制器是否已初始化（Initialized）。

<a id="r_ga09b71dc5c334f09fb92cf37e2ecf51eb"></a>

```c
static bool uhc_is_enabled (const struct device *dev)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[uhc_is_enabled](../usb/P073_USB主机控制器API.md#ga09b71dc5c334f09fb92cf37e2ecf51eb)、[device](../device_reference/P002_设备对象结构.md)。

检查控制器是否已启用（Enabled）。

<a id="r_ga4ceb0400168cd53201f0dde5f596452f"></a>

```c
static int uhc_bus_reset (const struct device *dev)
```

相关声明：[uhc_bus_reset](../usb/P073_USB主机控制器API.md#ga4ceb0400168cd53201f0dde5f596452f)、[device](../device_reference/P002_设备对象结构.md)。

复位 USB 总线（Bus）。

<a id="r_gafe55e97cbf31d163b10616c03da39414"></a>

```c
static int uhc_sof_enable (const struct device *dev)
```

相关声明：[uhc_sof_enable](../usb/P073_USB主机控制器API.md#gafe55e97cbf31d163b10616c03da39414)、[device](../device_reference/P002_设备对象结构.md)。

启用帧起始生成器（Start of Frame Generator）。

<a id="r_ga897081ff02dab4377c68bcba343f492c"></a>

```c
static int uhc_bus_suspend (const struct device *dev)
```

相关声明：[uhc_bus_suspend](../usb/P073_USB主机控制器API.md#ga897081ff02dab4377c68bcba343f492c)、[device](../device_reference/P002_设备对象结构.md)。

挂起 USB 总线（Suspend USB Bus）。

<a id="r_ga6669bc2ac56395b38292fa796b99bfd9"></a>

```c
static int uhc_bus_resume (const struct device *dev)
```

相关声明：[uhc_bus_resume](../usb/P073_USB主机控制器API.md#ga6669bc2ac56395b38292fa796b99bfd9)、[device](../device_reference/P002_设备对象结构.md)。

恢复 USB 总线（Resume USB Bus）。

<a id="r_gab5a2df4d176d4c85751c3158b63e366b"></a>

```c
struct uhc_transfer * uhc_xfer_alloc (const struct device *dev, const uint8_t ep, struct usb_device *const udev, void *const cb, void *const cb_priv)
```

相关声明：[uhc_transfer](../usb/P077_USB主机传输结构.md)、[uhc_xfer_alloc](../usb/P073_USB主机控制器API.md#gab5a2df4d176d4c85751c3158b63e366b)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[usb_device](../usb/P080_USB主机设备对象.md)。

分配 USB 主机控制器传输（UHC Transfer）。

<a id="r_ga75c2142698a15c547ab76ab76c89c177"></a>

```c
struct uhc_transfer * uhc_xfer_alloc_with_buf (const struct device *dev, const uint8_t ep, struct usb_device *const udev, void *const cb, void *const cb_priv, size_t size)
```

相关声明：[uhc_transfer](../usb/P077_USB主机传输结构.md)、[uhc_xfer_alloc_with_buf](../usb/P073_USB主机控制器API.md#ga75c2142698a15c547ab76ab76c89c177)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[usb_device](../usb/P080_USB主机设备对象.md)。

分配带缓冲区的 USB 主机控制器传输（UHC Transfer）。

<a id="r_ga69748d0650399a51672b98b475ab8437"></a>

```c
void uhc_xfer_ref (struct uhc_transfer *const xfer)
```

相关声明：[uhc_xfer_ref](../usb/P073_USB主机控制器API.md#ga69748d0650399a51672b98b475ab8437)、[uhc_transfer](../usb/P077_USB主机传输结构.md)。

增加 USB 主机控制器传输引用（UHC Transfer Reference）。

<a id="r_gab399b0ad7f6d856251af56cd92240351"></a>

```c
bool uhc_xfer_unref (struct uhc_transfer *const xfer)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[uhc_xfer_unref](../usb/P073_USB主机控制器API.md#gab399b0ad7f6d856251af56cd92240351)、[uhc_transfer](../usb/P077_USB主机传输结构.md)。

减少 USB 主机控制器传输引用（UHC Transfer Reference）。

<a id="r_gab2f6328e8051559edccc05ae3552f4f9"></a>

```c
int uhc_xfer_free (const struct device *dev, struct uhc_transfer *const xfer)
```

相关声明：[uhc_xfer_free](../usb/P073_USB主机控制器API.md#gab2f6328e8051559edccc05ae3552f4f9)、[device](../device_reference/P002_设备对象结构.md)、[uhc_transfer](../usb/P077_USB主机传输结构.md)。

释放 USB 主机控制器传输（UHC Transfer）及所有缓冲区。

<a id="r_ga779dbd7ee8ac5fce487e087706791ea7"></a>

```c
int uhc_xfer_buf_add (const struct device *dev, struct uhc_transfer *const xfer, struct net_buf *buf)
```

相关声明：[uhc_xfer_buf_add](../usb/P073_USB主机控制器API.md#ga779dbd7ee8ac5fce487e087706791ea7)、[device](../device_reference/P002_设备对象结构.md)、[uhc_transfer](../usb/P077_USB主机传输结构.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

添加 USB 主机控制器传输缓冲区（UHC Transfer Buffer）。

<a id="r_gab4f7439fab8c57e203862bc408a6e46b"></a>

```c
struct net_buf * uhc_xfer_buf_alloc (const struct device *dev, const size_t size)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uhc_xfer_buf_alloc](../usb/P073_USB主机控制器API.md#gab4f7439fab8c57e203862bc408a6e46b)、[device](../device_reference/P002_设备对象结构.md)。

分配 USB 主机控制器传输缓冲区（UHC Transfer Buffer）。

<a id="r_gac4bd26a85f8abc2006ecf2622669d615"></a>

```c
void uhc_xfer_buf_free (const struct device *dev, struct net_buf *const buf)
```

相关声明：[uhc_xfer_buf_free](../usb/P073_USB主机控制器API.md#gac4bd26a85f8abc2006ecf2622669d615)、[device](../device_reference/P002_设备对象结构.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

释放 USB 主机控制器请求缓冲区（UHC Request Buffer）。

<a id="r_ga7a07b598c00d53393e15f6dae5cf1c4a"></a>

```c
int uhc_ep_enqueue (const struct device *dev, struct uhc_transfer *const xfer)
```

相关声明：[uhc_ep_enqueue](../usb/P073_USB主机控制器API.md#ga7a07b598c00d53393e15f6dae5cf1c4a)、[device](../device_reference/P002_设备对象结构.md)、[uhc_transfer](../usb/P077_USB主机传输结构.md)。

将 USB 主机控制器传输（Host Controller Transfer）加入队列。

<a id="r_ga7c362cba29e0181ffcc8f70060100e62"></a>

```c
int uhc_ep_dequeue (const struct device *dev, struct uhc_transfer *const xfer)
```

相关声明：[uhc_ep_dequeue](../usb/P073_USB主机控制器API.md#ga7c362cba29e0181ffcc8f70060100e62)、[device](../device_reference/P002_设备对象结构.md)、[uhc_transfer](../usb/P077_USB主机传输结构.md)。

从队列移除 USB 主机控制器传输（Host Controller Transfers）。

<a id="r_ga97beb6e3b3d4ad1b0b7664eae473e1be"></a>

```c
int uhc_init (const struct device *dev, uhc_event_cb_t event_cb, const void *const event_ctx)
```

相关声明：[uhc_init](../usb/P073_USB主机控制器API.md#ga97beb6e3b3d4ad1b0b7664eae473e1be)、[device](../device_reference/P002_设备对象结构.md)、[uhc_event_cb_t](../usb/P073_USB主机控制器API.md#ga3cda056094ceef79dd62ad9c6852daf9)。

初始化 USB 主机控制器（Host Controller）。

<a id="r_gafe94b7f9e32aada9634166ebb2115c2f"></a>

```c
int uhc_enable (const struct device *dev)
```

相关声明：[uhc_enable](../usb/P073_USB主机控制器API.md#gafe94b7f9e32aada9634166ebb2115c2f)、[device](../device_reference/P002_设备对象结构.md)。

启用 USB 主机控制器（Host Controller）。

<a id="r_ga9ec92df4497588adbf8da6f0777a4afd"></a>

```c
int uhc_disable (const struct device *dev)
```

相关声明：[uhc_disable](../usb/P073_USB主机控制器API.md#ga9ec92df4497588adbf8da6f0777a4afd)、[device](../device_reference/P002_设备对象结构.md)。

禁用 USB 主机控制器（Host Controller）。

<a id="r_gac6d1feb9481882a711e58c3e55e915cb"></a>

```c
int uhc_shutdown (const struct device *dev)
```

相关声明：[uhc_shutdown](../usb/P073_USB主机控制器API.md#gac6d1feb9481882a711e58c3e55e915cb)、[device](../device_reference/P002_设备对象结构.md)。

关闭 USB 主机控制器（Host Controller）电源。

<a id="r_ga8796569eba96260ce332e611fb520033"></a>

```c
static struct uhc_device_caps uhc_caps (const struct device *dev)
```

相关声明：[uhc_device_caps](../usb/P075_USB主机控制器能力.md)、[uhc_caps](../usb/P073_USB主机控制器API.md#ga8796569eba96260ce332e611fb520033)、[device](../device_reference/P002_设备对象结构.md)。

获取 USB 主机控制器能力（Host Controller Capabilities）。

<a id="r_ga4468d1460d79dc30b2605e36ba478e40"></a>

```c
static const void * uhc_get_event_ctx (const struct device *dev)
```

相关声明：[uhc_get_event_ctx](../usb/P073_USB主机控制器API.md#ga4468d1460d79dc30b2605e36ba478e40)、[device](../device_reference/P002_设备对象结构.md)。

获取高层上下文（Higher Layer Context）的指针。


## 26.6\_原页交叉引用（Cross References）

- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/net_buf.h](../api_source_system_reference/P021_net_buf.h_源码浏览.md)
- [zephyr/drivers/usb/usb_buf.h](../api_source_runtime_reference/P066_usb_buf.h_源码浏览.md)
- [zephyr/usb/usb_ch9.h](../usb/P173_USB第9章头文件源码.md)
- [zephyr/sys/dlist.h](../dlist_reference/P003_双向链表头文件源码.md)
- [zephyr/sys/ref.h](../sysref_reference/P004_引用计数头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P885_uhc.h_源码浏览.md)
- [usb_host_interface](../usb/P081_USB主机接口对象.md)
- [usb_host_ep](../usb/P082_USB主机端点对象.md)
- [usb_device](../usb/P080_USB主机设备对象.md)
- [uhc_transfer](../usb/P077_USB主机传输结构.md)
- [uhc_event](../usb/P076_USB主机控制器事件.md)
- [uhc_device_caps](../usb/P075_USB主机控制器能力.md)
- [uhc_data](../usb/P074_USB主机控制器数据.md)
- [UHC_INTERFACES_MAX](../usb/P073_USB主机控制器API.md#ga1b1ec49cb7649ece6ec5a31dac3e2537)
- [UHC_STATUS_INITIALIZED](../usb/P073_USB主机控制器API.md#ga09ad6fc9251212fa0dffececb767ff9e)
- [uhc_init()](../usb/P073_USB主机控制器API.md#ga97beb6e3b3d4ad1b0b7664eae473e1be)
- [UHC_STATUS_ENABLED](../usb/P073_USB主机控制器API.md#ga230e104bd7be1d4b83b2d31ee72ac3c4)
- [uhc_event_cb_t](../usb/P073_USB主机控制器API.md#ga3cda056094ceef79dd62ad9c6852daf9)
- [device](../device_reference/P002_设备对象结构.md)
- [usb_device_state](../usb/P073_USB主机控制器API.md#ga7127ac2a46b577f2aa1bb9a650e62a3f)
- [USB_STATE_NOTCONNECTED](../usb/P073_USB主机控制器API.md#gga7127ac2a46b577f2aa1bb9a650e62a3fa70367cdc7b5d7d1f3ab046391f50df9d)
- [USB_STATE_DEFAULT](../usb/P073_USB主机控制器API.md#gga7127ac2a46b577f2aa1bb9a650e62a3fabb0f4a1c2f62f028bec1d0b55b5d5554)
- [USB_STATE_ADDRESSED](../usb/P073_USB主机控制器API.md#gga7127ac2a46b577f2aa1bb9a650e62a3fad7f0841a21d3179c13f19d3ae8a8e3b6)
- [USB_STATE_CONFIGURED](../usb/P073_USB主机控制器API.md#gga7127ac2a46b577f2aa1bb9a650e62a3fa6566e87fb6d54f2da5b7564743df7a47)
- [usb_device_speed](../usb/P073_USB主机控制器API.md#ga59ba7bbb99177a622f3c073fc48b7bc5)
- [USB_SPEED_UNKNOWN](../usb/P073_USB主机控制器API.md#gga59ba7bbb99177a622f3c073fc48b7bc5ac9755ae6b86f8148054fd6a342c74acc)
- [USB_SPEED_SPEED_LS](../usb/P073_USB主机控制器API.md#gga59ba7bbb99177a622f3c073fc48b7bc5a46c4232a37347ac22ac14b240abddbdc)
- [USB_SPEED_SPEED_FS](../usb/P073_USB主机控制器API.md#gga59ba7bbb99177a622f3c073fc48b7bc5a8cd687699d8afb4d818595d70b189e27)
- [USB_SPEED_SPEED_HS](../usb/P073_USB主机控制器API.md#gga59ba7bbb99177a622f3c073fc48b7bc5aab0ef8e9a798d70fd3c93e68785c0968)
- [USB_SPEED_SPEED_SS](../usb/P073_USB主机控制器API.md#gga59ba7bbb99177a622f3c073fc48b7bc5a36e25f2ed5532d6a281abaf521583fcc)
- [uhc_control_stage](../usb/P073_USB主机控制器API.md#gaef9b0703714676c1f7bd1cad57f49bc8)
- [UHC_CONTROL_STAGE_SETUP](../usb/P073_USB主机控制器API.md#ggaef9b0703714676c1f7bd1cad57f49bc8a3f3c131b3a97a552d2917bbddcd9afc8)
- [UHC_CONTROL_STAGE_DATA](../usb/P073_USB主机控制器API.md#ggaef9b0703714676c1f7bd1cad57f49bc8a2179067786eb86aad804d0aead9d71a5)
- [UHC_CONTROL_STAGE_STATUS](../usb/P073_USB主机控制器API.md#ggaef9b0703714676c1f7bd1cad57f49bc8a7bd9f0423e9f50266905c3736e12468f)
- [uhc_event_type](../usb/P073_USB主机控制器API.md#gabaf69c1e69fe0fb3d912b92daf8754eb)
- [UHC_EVT_DEV_CONNECTED_LS](../usb/P073_USB主机控制器API.md#ggabaf69c1e69fe0fb3d912b92daf8754ebae0a316b8f60df97f30f54630f6847f70)
- [UHC_EVT_DEV_CONNECTED_FS](../usb/P073_USB主机控制器API.md#ggabaf69c1e69fe0fb3d912b92daf8754eba98d87b3c737c234918fed0ce4589f4ce)
- [UHC_EVT_DEV_CONNECTED_HS](../usb/P073_USB主机控制器API.md#ggabaf69c1e69fe0fb3d912b92daf8754eba923b6cfe57c254e22b57eab88c84b67f)
- [UHC_EVT_DEV_REMOVED](../usb/P073_USB主机控制器API.md#ggabaf69c1e69fe0fb3d912b92daf8754ebab7c4181ad631b127cc50605f7864bc30)
- [UHC_EVT_RESETED](../usb/P073_USB主机控制器API.md#ggabaf69c1e69fe0fb3d912b92daf8754ebafb131548cc66e748e562ee88df274ab3)
- [UHC_EVT_SUSPENDED](../usb/P073_USB主机控制器API.md#ggabaf69c1e69fe0fb3d912b92daf8754ebab28885b8210133d4f0c2b532561c9c7a)
- [UHC_EVT_RESUMED](../usb/P073_USB主机控制器API.md#ggabaf69c1e69fe0fb3d912b92daf8754ebad874caf1d7338081d185634e12f69848)
- [UHC_EVT_RWUP](../usb/P073_USB主机控制器API.md#ggabaf69c1e69fe0fb3d912b92daf8754ebaa616f846752aacb8029f9b21747c656e)
- [UHC_EVT_EP_REQUEST](../usb/P073_USB主机控制器API.md#ggabaf69c1e69fe0fb3d912b92daf8754eba5cdc8afb59f760c4dc9b2de314d05483)
- [UHC_EVT_ERROR](../usb/P073_USB主机控制器API.md#ggabaf69c1e69fe0fb3d912b92daf8754ebae5970877eb9b6426132d8955cdeb26d7)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [uhc_is_initialized](../usb/P073_USB主机控制器API.md#ga3251967d36b67169d7892a615323c14e)
- [uhc_is_enabled](../usb/P073_USB主机控制器API.md#ga09b71dc5c334f09fb92cf37e2ecf51eb)
- [uhc_bus_reset](../usb/P073_USB主机控制器API.md#ga4ceb0400168cd53201f0dde5f596452f)
- [uhc_sof_enable](../usb/P073_USB主机控制器API.md#gafe55e97cbf31d163b10616c03da39414)
- [uhc_bus_suspend](../usb/P073_USB主机控制器API.md#ga897081ff02dab4377c68bcba343f492c)
- [uhc_bus_resume](../usb/P073_USB主机控制器API.md#ga6669bc2ac56395b38292fa796b99bfd9)
- [uhc_xfer_alloc](../usb/P073_USB主机控制器API.md#gab5a2df4d176d4c85751c3158b63e366b)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uhc_xfer_alloc_with_buf](../usb/P073_USB主机控制器API.md#ga75c2142698a15c547ab76ab76c89c177)
- [uhc_xfer_ref](../usb/P073_USB主机控制器API.md#ga69748d0650399a51672b98b475ab8437)
- [uhc_xfer_unref](../usb/P073_USB主机控制器API.md#gab399b0ad7f6d856251af56cd92240351)
- [uhc_xfer_free](../usb/P073_USB主机控制器API.md#gab2f6328e8051559edccc05ae3552f4f9)
- [uhc_xfer_buf_add](../usb/P073_USB主机控制器API.md#ga779dbd7ee8ac5fce487e087706791ea7)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [uhc_xfer_buf_alloc](../usb/P073_USB主机控制器API.md#gab4f7439fab8c57e203862bc408a6e46b)
- [uhc_xfer_buf_free](../usb/P073_USB主机控制器API.md#gac4bd26a85f8abc2006ecf2622669d615)
- [uhc_ep_enqueue](../usb/P073_USB主机控制器API.md#ga7a07b598c00d53393e15f6dae5cf1c4a)
- [uhc_ep_dequeue](../usb/P073_USB主机控制器API.md#ga7c362cba29e0181ffcc8f70060100e62)
- [uhc_enable](../usb/P073_USB主机控制器API.md#gafe94b7f9e32aada9634166ebb2115c2f)
- [uhc_disable](../usb/P073_USB主机控制器API.md#ga9ec92df4497588adbf8da6f0777a4afd)
- [uhc_shutdown](../usb/P073_USB主机控制器API.md#gac6d1feb9481882a711e58c3e55e915cb)
- [uhc_caps](../usb/P073_USB主机控制器API.md#ga8796569eba96260ce332e611fb520033)
- [uhc_get_event_ctx](../usb/P073_USB主机控制器API.md#ga4468d1460d79dc30b2605e36ba478e40)

<a id="header-details"></a>

---

[上一章](P025_zephyr__toolchain.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P027_zephyr__usb_c__usbc.h_文件参考.md)
