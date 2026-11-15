---
id: learning.zephyr-docs.api-file-usb-network-reference.page-15
title: zephyr__drivers__usb__udc.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/udc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_zephyr\_\_drivers\_\_usb\_\_udc.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/udc_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

新的USB设备控制器（UDC）驱动API。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <zephyr/device.h>
#include <zephyr/drivers/usb/usb_buf.h>
#include <zephyr/sys/atomic.h>
#include <zephyr/usb/usb_ch9.h>
```

查看此文件的源码。

新的USB设备控制器（UDC）驱动API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 15.1\_数据结构（Data Structures）

<a id="r_udc_5Fdevice_5Fcaps"></a>

```c
struct udc_device_caps
```

相关声明：[udc_device_caps](../usb/P034_USB设备控制器设备能力.md)。

USB设备控制器（Device Controller）的能力。

<a id="r_udc_5Fep_5Fcaps"></a>

```c
struct udc_ep_caps
```

相关声明：[udc_ep_caps](../usb/P035_USB设备控制器端点能力.md)。

USB设备控制器（Device Controller）的端点能力。

<a id="r_udc_5Fep_5Fstat"></a>

```c
struct udc_ep_stat
```

相关声明：[udc_ep_stat](../usb/P037_USB设备控制器端点状态.md)。

USB设备控制器（Device Controller）的端点状态。

<a id="r_udc_5Fep_5Fconfig"></a>

```c
struct udc_ep_config
```

相关声明：[udc_ep_config](../usb/P036_USB设备控制器端点配置.md)。

USB设备控制器（Device Controller）的端点配置。

<a id="r_udc_5Fevent"></a>

```c
struct udc_event
```

相关声明：[udc_event](../usb/P038_USB设备控制器事件结构.md)。

USB设备控制器（Device Controller）的事件。

<a id="r_udc_5Fbuf_5Finfo"></a>

```c
struct udc_buf_info
```

相关声明：[udc_buf_info](../usb/P032_USB设备控制器缓冲区信息.md)。

USB设备控制器（UDC）的端点缓冲区信息。

<a id="r_udc_5Fapi"></a>

```c
struct udc_api
```

相关声明：[udc_api](../usb/P031_USB设备控制器驱动接口.md)。

USB设备控制器（UDC）驱动API。任何USB设备控制器驱动都必须提供此API，但device_speed()和test_mode()仅高速（HS）控制器需要提供。

<a id="r_udc_5Fdata"></a>

```c
struct udc_data
```

相关声明：[udc_data](../usb/P033_USB设备控制器驱动数据.md)。

通用USB设备控制器（UDC）驱动数据结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 15.2\_宏定义（Macros）

<a id="r_a8c96946734085924e2afc591ac502551"></a>

```c
#define UDC_STATUS_INITIALIZED 0
```

相关声明：[UDC_STATUS_INITIALIZED](#a8c96946734085924e2afc591ac502551)。

控制器已由 `udc_init()` 初始化；若具备相应能力，可以生成 VBUS 事件（VBUS Event），但主机不得识别到该控制器。

<a id="r_ad10596af54465c3cb10cc59ae9a507d2"></a>

```c
#define UDC_STATUS_ENABLED 1
```

相关声明：[UDC_STATUS_ENABLED](#ad10596af54465c3cb10cc59ae9a507d2)。

控制器已启用，所有 API 函数均可用，且主机能够识别该控制器（Controller）。

<a id="r_ac3a36aa8cb3aab95d7931cb602631c36"></a>

```c
#define UDC_STATUS_SUSPENDED 2
```

相关声明：[UDC_STATUS_SUSPENDED](#ac3a36aa8cb3aab95d7931cb602631c36)。

控制器已被主机挂起（Suspended）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 15.3\_类型定义（Typedefs）

<a id="r_aa3ff247fd5234f65d91f84ebc38e384a"></a>

```c
typedef int(* udc_event_cb_t) (const struct device *dev, const struct udc_event *const event)
```

相关声明：[udc_event_cb_t](#aa3ff247fd5234f65d91f84ebc38e384a)、[device](../device_reference/P002_设备对象结构.md)、[udc_event](../usb/P038_USB设备控制器事件结构.md)。

向上层提交 USB 设备控制器事件（UDC Event）的回调（Callback）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 15.4\_枚举（Enumerations）

<a id="r_ac254f8a970f890d14e35c43474c915fd"></a>

```c
enum udc_mps0 { UDC_MPS0_8 , UDC_MPS0_16 , UDC_MPS0_32 , UDC_MPS0_64 }
```

相关声明：[udc_mps0](#ac254f8a970f890d14e35c43474c915fd)、[UDC_MPS0_8](#ac254f8a970f890d14e35c43474c915fdad961e13d52b708c9e6b8d951affd31bb)、[UDC_MPS0_16](#ac254f8a970f890d14e35c43474c915fda4a8ba94e9dced296d0e269390931e85a)、[UDC_MPS0_32](#ac254f8a970f890d14e35c43474c915fda1930322c1c7b053f3b9da2e319ed11e7)、[UDC_MPS0_64](#ac254f8a970f890d14e35c43474c915fdab481546bd71839266d4d881d6610633a)。

控制器所支持的控制端点最大包大小（Control Endpoint Maximum Packet Size）。

<a id="r_a32d61ab6dbb734009102b5239a834d1b"></a>

```c
enum udc_bus_speed { UDC_BUS_UNKNOWN , UDC_BUS_SPEED_FS , UDC_BUS_SPEED_HS , UDC_BUS_SPEED_SS }
```

相关声明：[udc_bus_speed](#a32d61ab6dbb734009102b5239a834d1b)、[UDC_BUS_UNKNOWN](#a32d61ab6dbb734009102b5239a834d1ba872aa49861a213ad970012f43db7d35d)、[UDC_BUS_SPEED_FS](#a32d61ab6dbb734009102b5239a834d1ba8177d4c8e8cb0456f9c2a553c76dc0d5)、[UDC_BUS_SPEED_HS](#a32d61ab6dbb734009102b5239a834d1ba9fc26a4b4ba8db446731274b67182599)、[UDC_BUS_SPEED_SS](#a32d61ab6dbb734009102b5239a834d1ba71b0e0a870859cf1f0c11380833f790a)。

USB 设备实际速度（USB Device Actual Speed）。

<a id="r_a03749f5acb64ff8cfddc3c0b6b81a040"></a>

```c
enum udc_event_type { UDC_EVT_VBUS_READY , UDC_EVT_VBUS_REMOVED , UDC_EVT_RESUME , UDC_EVT_SUSPEND , UDC_EVT_RESET , UDC_EVT_SOF , UDC_EVT_EP_REQUEST , UDC_EVT_ERROR }
```

相关声明：[udc_event_type](#a03749f5acb64ff8cfddc3c0b6b81a040)、[UDC_EVT_VBUS_READY](#a03749f5acb64ff8cfddc3c0b6b81a040a010cfc9f43a6faf68323201ae02fa00d)、[UDC_EVT_VBUS_REMOVED](#a03749f5acb64ff8cfddc3c0b6b81a040a4bdf374daa2aeb4f7b6b6c5fe2a46432)、[UDC_EVT_RESUME](#a03749f5acb64ff8cfddc3c0b6b81a040a0e0da320fe601eb1de24c142fc60f332)、[UDC_EVT_SUSPEND](#a03749f5acb64ff8cfddc3c0b6b81a040a120dc649618040f41da7542bf639159f)、[UDC_EVT_RESET](#a03749f5acb64ff8cfddc3c0b6b81a040aa174f33c3802cec8d6c37606bc5ba9bb)、[UDC_EVT_SOF](#a03749f5acb64ff8cfddc3c0b6b81a040af20153f2fde8ea2bb1a985f2e17a2f78)、[UDC_EVT_EP_REQUEST](#a03749f5acb64ff8cfddc3c0b6b81a040a52bb5ea941db9a025ccb73de3fc6d55b)、[UDC_EVT_ERROR](#a03749f5acb64ff8cfddc3c0b6b81a040a8ff69c0bc684eb113f1d4e0ec02dd70d)。

USB 设备控制器事件类型（USB Device Controller Event Types）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 15.5\_函数（Functions）

<a id="r_ga40e50cf79b40d3792513e8fea3347f59"></a>

```c
static bool udc_is_initialized (const struct device *dev)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[udc_is_initialized](../usb/P030_USB设备控制器API.md#ga40e50cf79b40d3792513e8fea3347f59)、[device](../device_reference/P002_设备对象结构.md)。

检查控制器是否已初始化（Initialized）。

<a id="r_ga2c09f2a1e89c91527a8492019089d13f"></a>

```c
static bool udc_is_enabled (const struct device *dev)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[udc_is_enabled](../usb/P030_USB设备控制器API.md#ga2c09f2a1e89c91527a8492019089d13f)、[device](../device_reference/P002_设备对象结构.md)。

检查控制器是否已启用（Enabled）。

<a id="r_ga88786eda763fce5c2a51521650ccc9f4"></a>

```c
static bool udc_is_suspended (const struct device *dev)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[udc_is_suspended](../usb/P030_USB设备控制器API.md#ga88786eda763fce5c2a51521650ccc9f4)、[device](../device_reference/P002_设备对象结构.md)。

检查控制器是否已挂起（Suspended）。

<a id="r_ga0670bec8b55c013fb607ba53a8634ad4"></a>

```c
int udc_init (const struct device *dev, udc_event_cb_t event_cb, const void *const event_ctx)
```

相关声明：[udc_init](../usb/P030_USB设备控制器API.md#ga0670bec8b55c013fb607ba53a8634ad4)、[device](../device_reference/P002_设备对象结构.md)、[udc_event_cb_t](#aa3ff247fd5234f65d91f84ebc38e384a)。

初始化 USB 设备控制器（USB Device Controller）。

<a id="r_gafbb0dec089f83fd674bd19670a882c65"></a>

```c
int udc_enable (const struct device *dev)
```

相关声明：[udc_enable](../usb/P030_USB设备控制器API.md#gafbb0dec089f83fd674bd19670a882c65)、[device](../device_reference/P002_设备对象结构.md)。

启用 USB 设备控制器（USB Device Controller）。

<a id="r_gaa7c2eaa52bdbe1d763b2961124570e8a"></a>

```c
int udc_disable (const struct device *dev)
```

相关声明：[udc_disable](../usb/P030_USB设备控制器API.md#gaa7c2eaa52bdbe1d763b2961124570e8a)、[device](../device_reference/P002_设备对象结构.md)。

禁用 USB 设备控制器（USB Device Controller）。

<a id="r_ga59a92eb60575ca80d205cc29b4fb4f21"></a>

```c
int udc_shutdown (const struct device *dev)
```

相关声明：[udc_shutdown](../usb/P030_USB设备控制器API.md#ga59a92eb60575ca80d205cc29b4fb4f21)、[device](../device_reference/P002_设备对象结构.md)。

将 USB 设备控制器（USB Device Controller）断电。

<a id="r_ga3ee738bad8e1ee3928d32f57f82bef70"></a>

```c
static struct udc_device_caps udc_caps (const struct device *dev)
```

相关声明：[udc_device_caps](../usb/P034_USB设备控制器设备能力.md)、[udc_caps](../usb/P030_USB设备控制器API.md#ga3ee738bad8e1ee3928d32f57f82bef70)、[device](../device_reference/P002_设备对象结构.md)。

获取 USB 设备控制器能力（USB Device Controller Capabilities）。

<a id="r_gab936f04015b0fee584756bcdf40d2f50"></a>

```c
enum udc_bus_speed udc_device_speed (const struct device *dev)
```

相关声明：[udc_bus_speed](#a32d61ab6dbb734009102b5239a834d1b)、[udc_device_speed](../usb/P030_USB设备控制器API.md#gab936f04015b0fee584756bcdf40d2f50)、[device](../device_reference/P002_设备对象结构.md)。

获取 USB 设备实际速度（USB Device Actual Speed）。

<a id="r_ga6feb32a2263307bdde9acc63d3c2ebb1"></a>

```c
static int udc_set_address (const struct device *dev, const uint8_t addr)
```

相关声明：[udc_set_address](../usb/P030_USB设备控制器API.md#ga6feb32a2263307bdde9acc63d3c2ebb1)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置 USB 设备地址（USB Device Address）。

<a id="r_ga7f575b548833cc1e5109e0d919630b3f"></a>

```c
static int udc_test_mode (const struct device *dev, const uint8_t mode, const bool dryrun)
```

相关声明：[udc_test_mode](../usb/P030_USB设备控制器API.md#ga7f575b548833cc1e5109e0d919630b3f)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用测试模式（Test Mode）。

<a id="r_ga075edc81fb3e39c2b377fc56c8c0915c"></a>

```c
static int udc_host_wakeup (const struct device *dev)
```

相关声明：[udc_host_wakeup](../usb/P030_USB设备控制器API.md#ga075edc81fb3e39c2b377fc56c8c0915c)、[device](../device_reference/P002_设备对象结构.md)。

启动主机唤醒过程（Host Wakeup Procedure）。

<a id="r_ga81307ae4ab17ccd86be64bdf1653df0e"></a>

```c
int udc_ep_try_config (const struct device *dev, const uint8_t ep, const uint8_t attributes, uint16_t *const mps, const uint8_t interval)
```

相关声明：[udc_ep_try_config](../usb/P030_USB设备控制器API.md#ga81307ae4ab17ccd86be64bdf1653df0e)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

尝试一种端点配置（Endpoint Configuration）。

<a id="r_gacc4b5c127532c994406df30bacab5684"></a>

```c
int udc_ep_enable (const struct device *dev, const uint8_t ep, const uint8_t attributes, const uint16_t mps, const uint8_t interval)
```

相关声明：[udc_ep_enable](../usb/P030_USB设备控制器API.md#gacc4b5c127532c994406df30bacab5684)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

配置并启用端点（Endpoint）。

<a id="r_ga52da2366ac5da1a695caa8826b342cbc"></a>

```c
int udc_ep_disable (const struct device *dev, const uint8_t ep)
```

相关声明：[udc_ep_disable](../usb/P030_USB设备控制器API.md#ga52da2366ac5da1a695caa8826b342cbc)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

禁用端点（Endpoint）。

<a id="r_ga19488ec4c93d81592bb5ffccfc1eadc4"></a>

```c
int udc_ep_set_halt (const struct device *dev, const uint8_t ep)
```

相关声明：[udc_ep_set_halt](../usb/P030_USB设备控制器API.md#ga19488ec4c93d81592bb5ffccfc1eadc4)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

使端点进入停滞状态（Halt Endpoint）。

<a id="r_gadec9c8af89b28984028fd8e0b1a8c776"></a>

```c
int udc_ep_clear_halt (const struct device *dev, const uint8_t ep)
```

相关声明：[udc_ep_clear_halt](../usb/P030_USB设备控制器API.md#gadec9c8af89b28984028fd8e0b1a8c776)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

清除端点停滞（Endpoint Halt）。

<a id="r_gacb2dc96353f1cffcc3d5e9710133fc0d"></a>

```c
int udc_ep_enqueue (const struct device *dev, struct net_buf *const buf)
```

相关声明：[udc_ep_enqueue](../usb/P030_USB设备控制器API.md#gacb2dc96353f1cffcc3d5e9710133fc0d)、[device](../device_reference/P002_设备对象结构.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

将 USB 设备控制器请求（USB Device Controller Request）加入队列。

<a id="r_ga409efee6a62a656a1349c07ba3a42bad"></a>

```c
int udc_purge_queues (const struct device *dev)
```

相关声明：[udc_purge_queues](../usb/P030_USB设备控制器API.md#ga409efee6a62a656a1349c07ba3a42bad)、[device](../device_reference/P002_设备对象结构.md)。

控制器关闭后，清空控制端点队列（Control Endpoint Queue）。

<a id="r_ga352ad356c5ec38dc5d18f076b97867b9"></a>

```c
bool udc_ep_queue_is_empty (const struct device *dev, const uint8_t ep)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[udc_ep_queue_is_empty](../usb/P030_USB设备控制器API.md#ga352ad356c5ec38dc5d18f076b97867b9)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

判断端点队列（Endpoint Queue）是否为空。

<a id="r_ga6e6fb62fb8ebceca7e8e6b590c32efc2"></a>

```c
int udc_ep_dequeue (const struct device *dev, const uint8_t ep)
```

相关声明：[udc_ep_dequeue](../usb/P030_USB设备控制器API.md#ga6e6fb62fb8ebceca7e8e6b590c32efc2)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从端点队列（Endpoint Queue）移除全部 USB 设备控制器请求（USB Device Controller Request）。

<a id="r_gad3fb1d64b6e0cf051627011ce673bb1e"></a>

```c
struct net_buf * udc_ep_buf_alloc (const struct device *dev, const uint8_t ep, const size_t size)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[udc_ep_buf_alloc](../usb/P030_USB设备控制器API.md#gad3fb1d64b6e0cf051627011ce673bb1e)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

分配 UDC 请求缓冲区（UDC Request Buffer）。

<a id="r_gaaf80c4d3b09686e8956cf121bfeb5e6c"></a>

```c
struct net_buf * udc_ctrl_setup_alloc (const struct device *dev)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[udc_ctrl_setup_alloc](../usb/P030_USB设备控制器API.md#gaaf80c4d3b09686e8956cf121bfeb5e6c)、[device](../device_reference/P002_设备对象结构.md)。

分配 UDC 控制传输的建立阶段缓冲区（Control Transfer SETUP Buffer）。

<a id="r_ga68791ba18df95c8caf5f62c25a275baa"></a>

```c
struct net_buf * udc_ctrl_data_alloc (const struct device *dev, const uint8_t ep, const size_t size)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[udc_ctrl_data_alloc](../usb/P030_USB设备控制器API.md#ga68791ba18df95c8caf5f62c25a275baa)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

分配 UDC 控制传输的数据阶段缓冲区（Control Transfer Data Stage Buffer）。

<a id="r_gaca5f39f41358237966c37b280d92a0a5"></a>

```c
struct net_buf * udc_ctrl_status_alloc (const struct device *dev, const uint8_t ep)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[udc_ctrl_status_alloc](../usb/P030_USB设备控制器API.md#gaca5f39f41358237966c37b280d92a0a5)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

分配 UDC 控制传输的状态阶段缓冲区（Control Transfer Status Stage Buffer）。

<a id="r_gaedd615defad234b001e74448f89488e1"></a>

```c
int udc_ep_buf_free (const struct device *dev, struct net_buf *const buf)
```

相关声明：[udc_ep_buf_free](../usb/P030_USB设备控制器API.md#gaedd615defad234b001e74448f89488e1)、[device](../device_reference/P002_设备对象结构.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

释放 UDC 请求缓冲区（UDC Request Buffer）。

<a id="r_ga50f6bde28b6a5fcab6b685107570e081"></a>

```c
static void udc_ep_buf_set_zlp (struct net_buf *const buf)
```

相关声明：[udc_ep_buf_set_zlp](../usb/P030_USB设备控制器API.md#ga50f6bde28b6a5fcab6b685107570e081)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

在请求元数据（Request Metadata）中设置零长度包标志（ZLP Flag）。

<a id="r_ga073a51222ac639d3c70af7b57970b42a"></a>

```c
static struct udc_buf_info * udc_get_buf_info (const struct net_buf *const buf)
```

相关声明：[udc_buf_info](../usb/P032_USB设备控制器缓冲区信息.md)、[udc_get_buf_info](../usb/P030_USB设备控制器API.md#ga073a51222ac639d3c70af7b57970b42a)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

获取请求元数据（Request Metadata）。

<a id="r_ga2d89f013b2e1279d1ec4cbd869e0cae6"></a>

```c
static const void * udc_get_event_ctx (const struct device *dev)
```

相关声明：[udc_get_event_ctx](../usb/P030_USB设备控制器API.md#ga2d89f013b2e1279d1ec4cbd869e0cae6)、[device](../device_reference/P002_设备对象结构.md)。

获取高层上下文（Higher Layer Context）的指针。

<a id="r_ga6da3d836e868f2d09fe24854c2d76aeb"></a>

```c
static uint16_t udc_mps_ep_size (const struct udc_ep_config *const cfg)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[udc_mps_ep_size](../usb/P030_USB设备控制器API.md#ga6da3d836e868f2d09fe24854c2d76aeb)、[udc_ep_config](../usb/P036_USB设备控制器端点配置.md)。

从 UDC 端点配置（Endpoint Configuration）中获取端点大小。

## 15.6\_详细说明（Detailed Documentation）

<a id="ad10596af54465c3cb10cc59ae9a507d2"></a>

### `UDC_STATUS_ENABLED`

```c
#define UDC_STATUS_ENABLED 1
```

控制器已启用，所有 API 函数均可用，且主机能够识别该控制器（Controller）。

<a id="a8c96946734085924e2afc591ac502551"></a>

### `UDC_STATUS_INITIALIZED`

```c
#define UDC_STATUS_INITIALIZED 0
```

控制器已由 `udc_init()` 初始化；若具备相应能力，可以生成 VBUS 事件（VBUS Event），但主机不得识别到该控制器。

<a id="ac3a36aa8cb3aab95d7931cb602631c36"></a>

### `UDC_STATUS_SUSPENDED`

```c
#define UDC_STATUS_SUSPENDED 2
```

控制器已被主机挂起（Suspended）。

<a id="aa3ff247fd5234f65d91f84ebc38e384a"></a>

### `udc_event_cb_t`

```c
typedef int(* udc_event_cb_t) (const struct device *dev, const struct udc_event *const event)
```

向上层提交 USB 设备控制器事件（UDC Event）的回调（Callback）。

在上层，需要将事件（Event）插入消息队列（Message Queue）。待定（TBD）：也许更适合提供一个指向初始化时所传入 `k_msgq` 的指针。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例设备结构体（Device Struct of the Driver Instance）的指针（Pointer）。 |
| `[in] event` | 指向事件结构体（Event Structure）。 |

**返回（Returns）**：返回值：成功返回 0，其他所有值均应视为错误。

<a id="a32d61ab6dbb734009102b5239a834d1b"></a>

### `udc_bus_speed`

```c
enum udc_bus_speed
```

USB 设备实际速度（USB Device Actual Speed）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `UDC_BUS_UNKNOWN` | 设备可能未连接（Not Connected）。 |
| `UDC_BUS_SPEED_FS` | 设备已连接到全速总线（Full Speed Bus）。 |
| `UDC_BUS_SPEED_HS` | 设备已连接到高速总线（High Speed Bus）。 |
| `UDC_BUS_SPEED_SS` | 设备已连接到超高速总线（SuperSpeed Bus）。 |

<a id="a03749f5acb64ff8cfddc3c0b6b81a040"></a>

### `udc_event_type`

```c
enum udc_event_type
```

USB 设备控制器事件类型（USB Device Controller Event Types）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `UDC_EVT_VBUS_READY` | VBUS 就绪事件（VBUS Ready Event），表示 VBUS 处于稳定状态（Stable Condition）。 |
| `UDC_EVT_VBUS_REMOVED` | VBUS 移除事件（VBUS Removed Event），表示 VBUS 低于有效范围（Valid Range）。 |
| `UDC_EVT_RESUME` | 设备恢复事件（Device Resume Event）。 |
| `UDC_EVT_SUSPEND` | 设备挂起事件（Device Suspended Event）。 |
| `UDC_EVT_RESET` | 检测到端口复位（Port Reset）。 |
| `UDC_EVT_SOF` | 帧开始事件（Start of Frame Event）。 |
| `UDC_EVT_EP_REQUEST` | 端点请求结果事件（Endpoint Request Result Event）。 |
| `UDC_EVT_ERROR` | 不可纠正错误事件（Non-correctable Error Event），需要上层或应用关注。 |

<a id="ac254f8a970f890d14e35c43474c915fd"></a>

### `udc_mps0`

```c
enum udc_mps0
```

控制器所支持的控制端点最大包大小（Control Endpoint Maximum Packet Size）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `UDC_MPS0_8` |  |
| `UDC_MPS0_16` |  |
| `UDC_MPS0_32` |  |
| `UDC_MPS0_64` |  |


## 15.7\_原页交叉引用（Cross References）

- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/drivers/usb/usb_buf.h](../api_source_runtime_reference/P066_usb_buf.h_源码浏览.md)
- [zephyr/sys/atomic.h](../atomic_reference/P003_原子操作公共头文件源码.md)
- [zephyr/usb/usb_ch9.h](../usb/P173_USB第9章头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P884_udc.h_源码浏览.md)
- [udc_device_caps](../usb/P034_USB设备控制器设备能力.md)
- [udc_ep_caps](../usb/P035_USB设备控制器端点能力.md)
- [udc_ep_stat](../usb/P037_USB设备控制器端点状态.md)
- [udc_ep_config](../usb/P036_USB设备控制器端点配置.md)
- [udc_event](../usb/P038_USB设备控制器事件结构.md)
- [udc_buf_info](../usb/P032_USB设备控制器缓冲区信息.md)
- [udc_api](../usb/P031_USB设备控制器驱动接口.md)
- [device_speed()](../usb/P031_USB设备控制器驱动接口.md#adf2b8f76158d7bd2d3918628c8a9fc22)
- [test_mode()](../usb/P031_USB设备控制器驱动接口.md#ab06839ded48cbc671b2b915fe0010959)
- [udc_data](../usb/P033_USB设备控制器驱动数据.md)
- [udc_init()](../usb/P030_USB设备控制器API.md#ga0670bec8b55c013fb607ba53a8634ad4)
- [device](../device_reference/P002_设备对象结构.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [udc_is_initialized](../usb/P030_USB设备控制器API.md#ga40e50cf79b40d3792513e8fea3347f59)
- [udc_is_enabled](../usb/P030_USB设备控制器API.md#ga2c09f2a1e89c91527a8492019089d13f)
- [udc_is_suspended](../usb/P030_USB设备控制器API.md#ga88786eda763fce5c2a51521650ccc9f4)
- [udc_enable](../usb/P030_USB设备控制器API.md#gafbb0dec089f83fd674bd19670a882c65)
- [udc_disable](../usb/P030_USB设备控制器API.md#gaa7c2eaa52bdbe1d763b2961124570e8a)
- [udc_shutdown](../usb/P030_USB设备控制器API.md#ga59a92eb60575ca80d205cc29b4fb4f21)
- [udc_caps](../usb/P030_USB设备控制器API.md#ga3ee738bad8e1ee3928d32f57f82bef70)
- [udc_device_speed](../usb/P030_USB设备控制器API.md#gab936f04015b0fee584756bcdf40d2f50)
- [udc_set_address](../usb/P030_USB设备控制器API.md#ga6feb32a2263307bdde9acc63d3c2ebb1)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [udc_test_mode](../usb/P030_USB设备控制器API.md#ga7f575b548833cc1e5109e0d919630b3f)
- [udc_host_wakeup](../usb/P030_USB设备控制器API.md#ga075edc81fb3e39c2b377fc56c8c0915c)
- [udc_ep_try_config](../usb/P030_USB设备控制器API.md#ga81307ae4ab17ccd86be64bdf1653df0e)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [udc_ep_enable](../usb/P030_USB设备控制器API.md#gacc4b5c127532c994406df30bacab5684)
- [udc_ep_disable](../usb/P030_USB设备控制器API.md#ga52da2366ac5da1a695caa8826b342cbc)
- [udc_ep_set_halt](../usb/P030_USB设备控制器API.md#ga19488ec4c93d81592bb5ffccfc1eadc4)
- [udc_ep_clear_halt](../usb/P030_USB设备控制器API.md#gadec9c8af89b28984028fd8e0b1a8c776)
- [udc_ep_enqueue](../usb/P030_USB设备控制器API.md#gacb2dc96353f1cffcc3d5e9710133fc0d)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [udc_purge_queues](../usb/P030_USB设备控制器API.md#ga409efee6a62a656a1349c07ba3a42bad)
- [udc_ep_queue_is_empty](../usb/P030_USB设备控制器API.md#ga352ad356c5ec38dc5d18f076b97867b9)
- [udc_ep_dequeue](../usb/P030_USB设备控制器API.md#ga6e6fb62fb8ebceca7e8e6b590c32efc2)
- [udc_ep_buf_alloc](../usb/P030_USB设备控制器API.md#gad3fb1d64b6e0cf051627011ce673bb1e)
- [udc_ctrl_setup_alloc](../usb/P030_USB设备控制器API.md#gaaf80c4d3b09686e8956cf121bfeb5e6c)
- [udc_ctrl_data_alloc](../usb/P030_USB设备控制器API.md#ga68791ba18df95c8caf5f62c25a275baa)
- [udc_ctrl_status_alloc](../usb/P030_USB设备控制器API.md#gaca5f39f41358237966c37b280d92a0a5)
- [udc_ep_buf_free](../usb/P030_USB设备控制器API.md#gaedd615defad234b001e74448f89488e1)
- [udc_ep_buf_set_zlp](../usb/P030_USB设备控制器API.md#ga50f6bde28b6a5fcab6b685107570e081)
- [udc_get_buf_info](../usb/P030_USB设备控制器API.md#ga073a51222ac639d3c70af7b57970b42a)
- [udc_get_event_ctx](../usb/P030_USB设备控制器API.md#ga2d89f013b2e1279d1ec4cbd869e0cae6)
- [udc_mps_ep_size](../usb/P030_USB设备控制器API.md#ga6da3d836e868f2d09fe24854c2d76aeb)
- [k_msgq](../msgstack_reference/P002_内核消息队列结构.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a32d61ab6dbb734009102b5239a834d1ba872aa49861a213ad970012f43db7d35d"></a>
<a id="a32d61ab6dbb734009102b5239a834d1ba8177d4c8e8cb0456f9c2a553c76dc0d5"></a>
<a id="a32d61ab6dbb734009102b5239a834d1ba9fc26a4b4ba8db446731274b67182599"></a>
<a id="a32d61ab6dbb734009102b5239a834d1ba71b0e0a870859cf1f0c11380833f790a"></a>
<a id="a03749f5acb64ff8cfddc3c0b6b81a040a010cfc9f43a6faf68323201ae02fa00d"></a>
<a id="a03749f5acb64ff8cfddc3c0b6b81a040a4bdf374daa2aeb4f7b6b6c5fe2a46432"></a>
<a id="a03749f5acb64ff8cfddc3c0b6b81a040a0e0da320fe601eb1de24c142fc60f332"></a>
<a id="a03749f5acb64ff8cfddc3c0b6b81a040a120dc649618040f41da7542bf639159f"></a>
<a id="a03749f5acb64ff8cfddc3c0b6b81a040aa174f33c3802cec8d6c37606bc5ba9bb"></a>
<a id="a03749f5acb64ff8cfddc3c0b6b81a040af20153f2fde8ea2bb1a985f2e17a2f78"></a>
<a id="a03749f5acb64ff8cfddc3c0b6b81a040a52bb5ea941db9a025ccb73de3fc6d55b"></a>
<a id="a03749f5acb64ff8cfddc3c0b6b81a040a8ff69c0bc684eb113f1d4e0ec02dd70d"></a>
<a id="ac254f8a970f890d14e35c43474c915fdad961e13d52b708c9e6b8d951affd31bb"></a>
<a id="ac254f8a970f890d14e35c43474c915fda4a8ba94e9dced296d0e269390931e85a"></a>
<a id="ac254f8a970f890d14e35c43474c915fda1930322c1c7b053f3b9da2e319ed11e7"></a>
<a id="ac254f8a970f890d14e35c43474c915fdab481546bd71839266d4d881d6610633a"></a>

---

[上一章](P014_zephyr__drivers__sip_svc__sip_svc_driver.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P016_zephyr__drivers__usb_c__usbc_tc.h_文件参考.md)
