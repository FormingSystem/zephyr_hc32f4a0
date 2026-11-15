---
id: learning.zephyr-docs.usb.api-30
title: USB设备控制器API
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__udc__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第30章\_USB设备控制器API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__udc__api.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 30.1\_阅读说明与来源

译注：本页属于[USB设备控制器API说明](P029_USB设备控制器API说明.md)的底层接口参考，供理解控制器驱动、端点管理和请求生命周期。声明和原注释按官方页面保留，补充解释明确标为源码译注。

[本册大纲](大纲.md)提供本组第29至39章的全部字段参考。

新版 USB 设备控制器（USB Device Controller，UDC）驱动 API。

新版 USB 设备控制器（USB Device Controller，UDC）驱动 API。

引入版本（Since）：3.3。

接口版本（Version）：0.1.1。

## 30.2\_函数（Functions）

<a id="r_ga40e50cf79b40d3792513e8fea3347f59"></a>

```c
static bool udc_is_initialized (const struct device *dev)
```

检查控制器是否已初始化（Initialized）。

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[udc_is_initialized](P030_USB设备控制器API.md#ga40e50cf79b40d3792513e8fea3347f59)、[device](../device_reference/P002_设备对象结构.md)。

<a id="r_ga2c09f2a1e89c91527a8492019089d13f"></a>

```c
static bool udc_is_enabled (const struct device *dev)
```

检查控制器是否已启用（Enabled）。

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[udc_is_enabled](P030_USB设备控制器API.md#ga2c09f2a1e89c91527a8492019089d13f)、[device](../device_reference/P002_设备对象结构.md)。

<a id="r_ga88786eda763fce5c2a51521650ccc9f4"></a>

```c
static bool udc_is_suspended (const struct device *dev)
```

检查控制器是否已挂起（Suspended）。

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[udc_is_suspended](P030_USB设备控制器API.md#ga88786eda763fce5c2a51521650ccc9f4)、[device](../device_reference/P002_设备对象结构.md)。

<a id="r_ga0670bec8b55c013fb607ba53a8634ad4"></a>

```c
int udc_init (const struct device *dev, udc_event_cb_t event_cb, const void *const event_ctx)
```

初始化 USB 设备控制器。

相关声明：[udc_init](P030_USB设备控制器API.md#ga0670bec8b55c013fb607ba53a8634ad4)、[device](../device_reference/P002_设备对象结构.md)、[udc_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/udc_8h.html#aa3ff247fd5234f65d91f84ebc38e384a)。

<a id="r_gafbb0dec089f83fd674bd19670a882c65"></a>

```c
int udc_enable (const struct device *dev)
```

启用 USB 设备控制器。

相关声明：[udc_enable](P030_USB设备控制器API.md#gafbb0dec089f83fd674bd19670a882c65)、[device](../device_reference/P002_设备对象结构.md)。

<a id="r_gaa7c2eaa52bdbe1d763b2961124570e8a"></a>

```c
int udc_disable (const struct device *dev)
```

停用 USB 设备控制器。

相关声明：[udc_disable](P030_USB设备控制器API.md#gaa7c2eaa52bdbe1d763b2961124570e8a)、[device](../device_reference/P002_设备对象结构.md)。

<a id="r_ga59a92eb60575ca80d205cc29b4fb4f21"></a>

```c
int udc_shutdown (const struct device *dev)
```

关闭 USB 设备控制器的电源。

相关声明：[udc_shutdown](P030_USB设备控制器API.md#ga59a92eb60575ca80d205cc29b4fb4f21)、[device](../device_reference/P002_设备对象结构.md)。

<a id="r_ga3ee738bad8e1ee3928d32f57f82bef70"></a>

```c
static struct udc_device_caps udc_caps (const struct device *dev)
```

获取 USB 设备控制器能力（Capabilities）。

相关声明：[udc_device_caps](P034_USB设备控制器设备能力.md)、[udc_caps](P030_USB设备控制器API.md#ga3ee738bad8e1ee3928d32f57f82bef70)、[device](../device_reference/P002_设备对象结构.md)。

<a id="r_gab936f04015b0fee584756bcdf40d2f50"></a>

```c
enum udc_bus_speed udc_device_speed (const struct device *dev)
```

获取 USB 设备的实际速率（Bus Speed）。

相关声明：[udc_bus_speed](https://docs.zephyrproject.org/latest/doxygen/html/udc_8h.html#a32d61ab6dbb734009102b5239a834d1b)、[udc_device_speed](P030_USB设备控制器API.md#gab936f04015b0fee584756bcdf40d2f50)、[device](../device_reference/P002_设备对象结构.md)。

<a id="r_ga6feb32a2263307bdde9acc63d3c2ebb1"></a>

```c
static int udc_set_address (const struct device *dev, const uint8_t addr)
```

设置 USB 设备地址。

相关声明：[udc_set_address](P030_USB设备控制器API.md#ga6feb32a2263307bdde9acc63d3c2ebb1)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_ga7f575b548833cc1e5109e0d919630b3f"></a>

```c
static int udc_test_mode (const struct device *dev, const uint8_t mode, const bool dryrun)
```

启用测试模式（Test Mode）。

相关声明：[udc_test_mode](P030_USB设备控制器API.md#ga7f575b548833cc1e5109e0d919630b3f)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

<a id="r_ga075edc81fb3e39c2b377fc56c8c0915c"></a>

```c
static int udc_host_wakeup (const struct device *dev)
```

发起主机唤醒过程（Host Wakeup）。

相关声明：[udc_host_wakeup](P030_USB设备控制器API.md#ga075edc81fb3e39c2b377fc56c8c0915c)、[device](../device_reference/P002_设备对象结构.md)。

<a id="r_ga81307ae4ab17ccd86be64bdf1653df0e"></a>

```c
int udc_ep_try_config (const struct device *dev, const uint8_t ep, const uint8_t attributes, uint16_t *const mps, const uint8_t interval)
```

尝试端点配置（Endpoint Configuration）。

相关声明：[udc_ep_try_config](P030_USB设备控制器API.md#ga81307ae4ab17ccd86be64bdf1653df0e)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

<a id="r_gacc4b5c127532c994406df30bacab5684"></a>

```c
int udc_ep_enable (const struct device *dev, const uint8_t ep, const uint8_t attributes, const uint16_t mps, const uint8_t interval)
```

配置并启用端点。

相关声明：[udc_ep_enable](P030_USB设备控制器API.md#gacc4b5c127532c994406df30bacab5684)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

<a id="r_ga52da2366ac5da1a695caa8826b342cbc"></a>

```c
int udc_ep_disable (const struct device *dev, const uint8_t ep)
```

停用端点。

相关声明：[udc_ep_disable](P030_USB设备控制器API.md#ga52da2366ac5da1a695caa8826b342cbc)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_ga19488ec4c93d81592bb5ffccfc1eadc4"></a>

```c
int udc_ep_set_halt (const struct device *dev, const uint8_t ep)
```

停止端点（Endpoint Halt）。

相关声明：[udc_ep_set_halt](P030_USB设备控制器API.md#ga19488ec4c93d81592bb5ffccfc1eadc4)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_gadec9c8af89b28984028fd8e0b1a8c776"></a>

```c
int udc_ep_clear_halt (const struct device *dev, const uint8_t ep)
```

清除端点停止状态。

相关声明：[udc_ep_clear_halt](P030_USB设备控制器API.md#gadec9c8af89b28984028fd8e0b1a8c776)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_gacb2dc96353f1cffcc3d5e9710133fc0d"></a>

```c
int udc_ep_enqueue (const struct device *dev, struct net_buf *const buf)
```

将 USB 设备控制器请求加入队列。

相关声明：[udc_ep_enqueue](P030_USB设备控制器API.md#gacb2dc96353f1cffcc3d5e9710133fc0d)、[device](../device_reference/P002_设备对象结构.md)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

<a id="r_ga409efee6a62a656a1349c07ba3a42bad"></a>

```c
int udc_purge_queues (const struct device *dev)
```

在控制器关闭后清空控制端点队列。

相关声明：[udc_purge_queues](P030_USB设备控制器API.md#ga409efee6a62a656a1349c07ba3a42bad)、[device](../device_reference/P002_设备对象结构.md)。

<a id="r_ga352ad356c5ec38dc5d18f076b97867b9"></a>

```c
bool udc_ep_queue_is_empty (const struct device *dev, const uint8_t ep)
```

判断端点队列是否为空。

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[udc_ep_queue_is_empty](P030_USB设备控制器API.md#ga352ad356c5ec38dc5d18f076b97867b9)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_ga6e6fb62fb8ebceca7e8e6b590c32efc2"></a>

```c
int udc_ep_dequeue (const struct device *dev, const uint8_t ep)
```

从端点队列移除所有 USB 设备控制器请求。

相关声明：[udc_ep_dequeue](P030_USB设备控制器API.md#ga6e6fb62fb8ebceca7e8e6b590c32efc2)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_gad3fb1d64b6e0cf051627011ce673bb1e"></a>

```c
struct net_buf * udc_ep_buf_alloc (const struct device *dev, const uint8_t ep, const size_t size)
```

分配 UDC 请求缓冲区（Request Buffer）。

相关声明：[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)、[udc_ep_buf_alloc](P030_USB设备控制器API.md#gad3fb1d64b6e0cf051627011ce673bb1e)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_gaaf80c4d3b09686e8956cf121bfeb5e6c"></a>

```c
struct net_buf * udc_ctrl_setup_alloc (const struct device *dev)
```

分配 UDC 控制传输的设置阶段（SETUP）缓冲区。

相关声明：[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)、[udc_ctrl_setup_alloc](P030_USB设备控制器API.md#gaaf80c4d3b09686e8956cf121bfeb5e6c)、[device](../device_reference/P002_设备对象结构.md)。

<a id="r_ga68791ba18df95c8caf5f62c25a275baa"></a>

```c
struct net_buf * udc_ctrl_data_alloc (const struct device *dev, const uint8_t ep, const size_t size)
```

分配 UDC 控制传输的数据阶段（Data Stage）缓冲区。

相关声明：[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)、[udc_ctrl_data_alloc](P030_USB设备控制器API.md#ga68791ba18df95c8caf5f62c25a275baa)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_gaca5f39f41358237966c37b280d92a0a5"></a>

```c
struct net_buf * udc_ctrl_status_alloc (const struct device *dev, const uint8_t ep)
```

分配 UDC 控制传输的状态阶段（Status Stage）缓冲区。

相关声明：[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)、[udc_ctrl_status_alloc](P030_USB设备控制器API.md#gaca5f39f41358237966c37b280d92a0a5)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_gaedd615defad234b001e74448f89488e1"></a>

```c
int udc_ep_buf_free (const struct device *dev, struct net_buf *const buf)
```

释放 UDC 请求缓冲区。

相关声明：[udc_ep_buf_free](P030_USB设备控制器API.md#gaedd615defad234b001e74448f89488e1)、[device](../device_reference/P002_设备对象结构.md)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

<a id="r_ga50f6bde28b6a5fcab6b685107570e081"></a>

```c
static void udc_ep_buf_set_zlp (struct net_buf *const buf)
```

在请求元数据中设置零长度包（Zero-Length Packet，ZLP）标志。

相关声明：[udc_ep_buf_set_zlp](P030_USB设备控制器API.md#ga50f6bde28b6a5fcab6b685107570e081)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

<a id="r_ga073a51222ac639d3c70af7b57970b42a"></a>

```c
static struct udc_buf_info * udc_get_buf_info (const struct net_buf *const buf)
```

获取请求元数据（Metadata）。

相关声明：[udc_buf_info](P032_USB设备控制器缓冲区信息.md)、[udc_get_buf_info](P030_USB设备控制器API.md#ga073a51222ac639d3c70af7b57970b42a)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

<a id="r_ga2d89f013b2e1279d1ec4cbd869e0cae6"></a>

```c
static const void * udc_get_event_ctx (const struct device *dev)
```

获取上层上下文（Higher Layer Context）的指针。

相关声明：[udc_get_event_ctx](P030_USB设备控制器API.md#ga2d89f013b2e1279d1ec4cbd869e0cae6)、[device](../device_reference/P002_设备对象结构.md)。

<a id="r_ga6da3d836e868f2d09fe24854c2d76aeb"></a>

```c
static uint16_t udc_mps_ep_size (const struct udc_ep_config *const cfg)
```

从 UDC 端点配置取得端点大小。

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[udc_mps_ep_size](P030_USB设备控制器API.md#ga6da3d836e868f2d09fe24854c2d76aeb)、[udc_ep_config](P036_USB设备控制器端点配置.md)。

## 30.3\_详细说明（Detailed Documentation）

<a id="ga3ee738bad8e1ee3928d32f57f82bef70"></a>

### `udc_caps()`

```c
static inline struct udc_device_caps udc_caps ( const struct device * dev)
```

```c
#include <zephyr/drivers/usb/udc.h>
```

获取 USB 设备控制器能力（Capabilities）。

获取控制器的全速（Full Speed，FS）、高速（High Speed，HS）等能力。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例的设备结构体的指针。 |

**返回（Returns）**：USB 设备控制器能力。

<a id="ga68791ba18df95c8caf5f62c25a275baa"></a>

### `udc_ctrl_data_alloc()`

```c
struct net_buf * udc_ctrl_data_alloc ( const struct device * dev, const uint8_t ep, const size_t size )
```

```c
#include <zephyr/drivers/usb/udc.h>
```

分配 UDC 控制传输的数据阶段（Data Stage）缓冲区。

从公共控制传输缓冲池分配一个新缓冲区。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例的设备结构体的指针。 |
| `[in] ep` | 控制端点地址。 |
| `[in] size` | 请求缓冲区大小。 |

**返回（Returns）**：指向已分配请求的指针；出错时返回 NULL。

> 译注（源码核对）：控制 OUT 方向按端点最大包长向上取整分配容量；IN 方向按请求大小分配。分配成功后设置 data 标志，清除 setup 和 status 标志。

<a id="gaaf80c4d3b09686e8956cf121bfeb5e6c"></a>

### `udc_ctrl_setup_alloc()`

```c
struct net_buf * udc_ctrl_setup_alloc ( const struct device * dev)
```

```c
#include <zephyr/drivers/usb/udc.h>
```

分配 UDC 控制传输的设置阶段（SETUP）缓冲区。

从公共控制传输缓冲池分配一个新缓冲区。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例的设备结构体的指针。 |

**返回（Returns）**：指向已分配请求的指针；出错时返回 NULL。

> 译注（源码核对）：SETUP 有效载荷为8字节，但当前实现按控制 OUT 端点的最大包长分配容量，并设置 setup 标志。缓冲容量不等于有效载荷长度。

<a id="gaca5f39f41358237966c37b280d92a0a5"></a>

### `udc_ctrl_status_alloc()`

```c
struct net_buf * udc_ctrl_status_alloc ( const struct device * dev, const uint8_t ep )
```

```c
#include <zephyr/drivers/usb/udc.h>
```

分配 UDC 控制传输的状态阶段（Status Stage）缓冲区。

从公共控制传输缓冲池分配一个新缓冲区。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例的设备结构体的指针。 |
| `[in] ep` | 控制端点地址。 |

**返回（Returns）**：指向已分配请求的指针；出错时返回 NULL。

> 译注（源码核对）：状态阶段传输零长度包，但当前实现仍为控制 OUT 分配一个最大包长的容量；IN 方向容量为0。传输长度和接收缓冲容量须分别理解。

<a id="gab936f04015b0fee584756bcdf40d2f50"></a>

### `udc_device_speed()`

```c
enum udc_bus_speed udc_device_speed ( const struct device * dev)
```

```c
#include <zephyr/drivers/usb/udc.h>
```

获取 USB 设备的实际速率（Bus Speed）。

应在复位事件之后调用此函数，以确定实际总线速率。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例的设备结构体的指针。 |

**返回（Returns）**：USB 设备控制器能力。

> 译注（源码核对）：原返回说明写“控制器能力”，但实际类型是 enum udc_bus_speed。当前实现对未启用控制器返回 UDC_BUS_UNKNOWN；已启用且未提供 device_speed 回调时回退为 UDC_BUS_SPEED_FS。能力字段 hs 与当前连接速率不是同一概念。

<a id="gaa7c2eaa52bdbe1d763b2961124570e8a"></a>

### `udc_disable()`

```c
int udc_disable ( const struct device * dev)
```

```c
#include <zephyr/drivers/usb/udc.h>
```

停用 USB 设备控制器。

停用已启用的 USB 设备控制器。驱动应继续检测电源状态变化。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例的设备结构体的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EALREADY` | 已经停用。 |

**返回（Returns）**：成功时为 0，其他所有值均应视为错误。

> 译注（源码核对）：停用不等于关闭。当前实现调用驱动的 disable 回调后即清除 enabled 位，即使驱动返回错误也会清除此位；应检查返回值，不能仅凭状态位推定硬件操作成功。

<a id="gafbb0dec089f83fd674bd19670a882c65"></a>

### `udc_enable()`

```c
int udc_enable ( const struct device * dev)
```

```c
#include <zephyr/drivers/usb/udc.h>
```

启用 USB 设备控制器。

启用已供电的 USB 设备控制器，使主机能够识别并枚举（Enumerate）设备。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例的设备结构体的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EPERM` | 控制器尚未初始化。 |
| `-EALREADY` | 已经启用。 |
| `-ETIMEDOUT` | 启用操作超时。 |

**返回（Returns）**：成功时为 0，其他所有值均应视为错误。

<a id="gad3fb1d64b6e0cf051627011ce673bb1e"></a>

### `udc_ep_buf_alloc()`

```c
struct net_buf * udc_ep_buf_alloc ( const struct device * dev, const uint8_t ep, const size_t size )
```

```c
#include <zephyr/drivers/usb/udc.h>
```

分配 UDC 请求缓冲区（Request Buffer）。

从公共请求缓冲池分配一个新缓冲区。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例的设备结构体的指针。 |
| `[in] ep` | 端点地址。 |
| `[in] size` | 请求缓冲区大小。 |

**返回（Returns）**：指向已分配请求的指针；出错时返回 NULL。

> 译注（源码核对）：当前公共实现以 K_NO_WAIT 分配，资源不足时可立即返回 NULL，使用前必须检查。控制传输分配目前也经 udc_ctrl_alloc() 转发到同一公共请求池，不能据原注释推定已存在独立的控制传输内存池。

<a id="gaedd615defad234b001e74448f89488e1"></a>

### `udc_ep_buf_free()`

```c
int udc_ep_buf_free ( const struct device * dev, struct net_buf *const buf )
```

```c
#include <zephyr/drivers/usb/udc.h>
```

释放 UDC 请求缓冲区。

将缓冲区放回请求缓冲池。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例的设备结构体的指针。 |
| `[in] buf` | 指向 UDC 请求缓冲区的指针。 |

**返回（Returns）**：成功时为 0，其他所有值均应视为错误。

> 译注（源码核对）：当前实现调用 net_buf_unref() 减少引用计数，随后返回0；有其他引用时不会立即销毁缓冲区。这不是脱离引用计数强制释放内存的接口。

<a id="ga50f6bde28b6a5fcab6b685107570e081"></a>

### `udc_ep_buf_set_zlp()`

```c
static inline void udc_ep_buf_set_zlp ( struct net_buf *const buf)
```

```c
#include <zephyr/drivers/usb/udc.h>
```

在请求元数据中设置零长度包（Zero-Length Packet，ZLP）标志。

控制器应在传输结束时发送一个 ZLP。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] buf` | 指向 UDC 请求缓冲区的指针。 |

<a id="gadec9c8af89b28984028fd8e0b1a8c776"></a>

### `udc_ep_clear_halt()`

```c
int udc_ep_clear_halt ( const struct device * dev, const uint8_t ep )
```

```c
#include <zephyr/drivers/usb/udc.h>
```

清除端点停止状态。

适用于所有端点。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例的设备结构体的指针。 |
| `[in] ep` | 端点地址。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENODEV` | 未找到端点配置。 |
| `-ENOTSUP` | 不支持，例如等时（Isochronous）端点。 |
| `-EPERM` | 控制器尚未启用。 |

**返回（Returns）**：成功时为 0，其他所有值均应视为错误。

<a id="ga6e6fb62fb8ebceca7e8e6b590c32efc2"></a>

### `udc_ep_dequeue()`

```c
int udc_ep_dequeue ( const struct device * dev, const uint8_t ep )
```

```c
#include <zephyr/drivers/usb/udc.h>
```

从端点队列移除所有 USB 设备控制器请求。

驱动释放其占用的缓冲区时，会产生 UDC_EVT_EP_REQUEST 事件；不再占用新请求，队列中的所有请求将以链表形式经事件的 buf 成员传递。此后端点队列为空。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例的设备结构体的指针。 |
| `[in] ep` | 端点地址。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENODEV` | 未找到端点配置。 |
| `-EACCES` | 端点尚未停用。 |
| `-EPERM` | 控制器尚未初始化。 |

**返回（Returns）**：成功时为 0，其他所有值均应视为错误。

> 译注（源码核对）：出队通过事件返回请求，不等于调用者可以立即释放仍由硬件占用的缓冲区。当前公共层在端点状态检查处仅写日志，不直接返回原表列出的 -EACCES；非空队列交给驱动的 ep_dequeue 处理，具体驱动仍可能返回错误。

<a id="ga52da2366ac5da1a695caa8826b342cbc"></a>

### `udc_ep_disable()`

```c
int udc_ep_disable ( const struct device * dev, const uint8_t ep )
```

```c
#include <zephyr/drivers/usb/udc.h>
```

停用端点。

适用于除控制 IN／OUT 端点外的所有端点。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例的设备结构体的指针。 |
| `[in] ep` | 端点地址。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | 参数错误，指定了控制 IN／OUT 端点。 |
| `-ENODEV` | 未找到端点配置。 |
| `-EALREADY` | 端点已经停用。 |
| `-EPERM` | 控制器尚未初始化。 |

**返回（Returns）**：成功时为 0，其他所有值均应视为错误。

<a id="gacc4b5c127532c994406df30bacab5684"></a>

### `udc_ep_enable()`

```c
int udc_ep_enable ( const struct device * dev, const uint8_t ep, const uint8_t attributes, const uint16_t mps, const uint8_t interval )
```

```c
#include <zephyr/drivers/usb/udc.h>
```

配置并启用端点。

配置端点，使其准备好供使用。适用于除控制 IN／OUT 端点外的所有端点。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例的设备结构体的指针。 |
| `[in] ep` | 端点地址，与 bEndpointAddress 相同。 |
| `[in] attributes` | 端点属性，与 bmAttributes 相同。 |
| `[in] mps` | 最大包长（Maximum Packet Size，MPS），与 wMaxPacketSize 相同。 |
| `[in] interval` | 轮询间隔（Polling Interval），与 bInterval 相同。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | 参数错误，指定了控制 IN／OUT 端点。 |
| `-EPERM` | 控制器尚未初始化。 |
| `-ENODEV` | 未找到端点配置。 |
| `-EALREADY` | 端点已经启用。 |

**返回（Returns）**：成功时为 0，其他所有值均应视为错误。

<a id="gacb2dc96353f1cffcc3d5e9710133fc0d"></a>

### `udc_ep_enqueue()`

```c
int udc_ep_enqueue ( const struct device * dev, struct net_buf *const buf )
```

```c
#include <zephyr/drivers/usb/udc.h>
```

将 USB 设备控制器请求加入队列。

将请求加入队列。如果队列为空，控制器可以立即占用该请求缓冲区。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例的设备结构体的指针。 |
| `[in] buf` | 指向 UDC 请求缓冲区的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENODEV` | 未找到端点配置。 |
| `-EACCES` | 端点尚未启用，原文标为待定（TBD）。 |
| `-EBUSY` | 请求无法加入队列。 |
| `-EPERM` | 控制器尚未初始化。 |

**返回（Returns）**：成功时为 0，其他所有值均应视为错误。

> 译注（源码核对）：当前公共实现要求控制器已启用，未启用返回 -EPERM；端点不存在或未启用均返回 -ENODEV。原表中“未启用端点返回 -EACCES”仍标为 TBD，这里保留原表并说明当前实现差异。

<a id="ga352ad356c5ec38dc5d18f076b97867b9"></a>

### `udc_ep_queue_is_empty()`

```c
bool udc_ep_queue_is_empty ( const struct device * dev, const uint8_t ep )
```

```c
#include <zephyr/drivers/usb/udc.h>
```

判断端点队列是否为空。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例的设备结构体的指针。 |
| `[in] ep` | 端点地址。 |

**返回（Returns）**：端点队列为空时为 true，否则为 false。

> 译注（源码核对）：当前实现未找到该端点配置时也返回 true；因此 true 不能单独证明端点存在，更不能证明硬件已完成所有传输。

<a id="ga19488ec4c93d81592bb5ffccfc1eadc4"></a>

### `udc_ep_set_halt()`

```c
int udc_ep_set_halt ( const struct device * dev, const uint8_t ep )
```

```c
#include <zephyr/drivers/usb/udc.h>
```

停止端点（Endpoint Halt）。

适用于所有端点。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例的设备结构体的指针。 |
| `[in] ep` | 端点地址。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENODEV` | 未找到端点配置。 |
| `-ENOTSUP` | 不支持，例如等时（Isochronous）端点。 |
| `-EPERM` | 控制器尚未启用。 |

**返回（Returns）**：成功时为 0，其他所有值均应视为错误。

<a id="ga81307ae4ab17ccd86be64bdf1653df0e"></a>

### `udc_ep_try_config()`

```c
int udc_ep_try_config ( const struct device * dev, const uint8_t ep, const uint8_t attributes, uint16_t *const mps, const uint8_t interval )
```

```c
#include <zephyr/drivers/usb/udc.h>
```

尝试端点配置（Endpoint Configuration）。

根据端点描述符尝试端点配置。此函数可能修改端点描述符的 wMaxPacketSize 字段。描述符的方向、传输类型等所有属性都应正确设置。如果 wMaxPacketSize 为零，则将其更新为该端点的最大缓冲区大小。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例的设备结构体的指针。 |
| `[in] ep` | 端点地址，与 bEndpointAddress 相同。 |
| `[in] attributes` | 端点属性，与 bmAttributes 相同。 |
| `[in] mps` | 最大包长（Maximum Packet Size，MPS），与 wMaxPacketSize 相同。 |
| `[in] interval` | 轮询间隔（Polling Interval），与 bInterval 相同。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | 参数错误。 |
| `-ENOTSUP` | 不支持该端点配置。 |
| `-ENODEV` | 没有可用端点。 |

**返回（Returns）**：成功时为 0，其他所有值均应视为错误。

> 译注（源码核对）：公开接口通过 mps 指针回写包长，参数不是描述符指针。当前公共实现仅为零包长的 bulk 和 interrupt 配置计算默认值；control 与 iso 不在该自动更新分支。实现按控制器 hs 能力选择上限，源码仍标注尚未结合复位后的实际总线速率，因此不能把原说明理解为任意传输类型都能自动得到正确包长。

<a id="ga073a51222ac639d3c70af7b57970b42a"></a>

### `udc_get_buf_info()`

```c
static inline struct udc_buf_info * udc_get_buf_info ( const struct net_buf *const buf)
```

```c
#include <zephyr/drivers/usb/udc.h>
```

获取请求元数据（Metadata）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] buf` | 指向 UDC 请求缓冲区的指针。 |

**返回（Returns）**：指向元数据结构体的指针。

<a id="ga2d89f013b2e1279d1ec4cbd869e0cae6"></a>

### `udc_get_event_ctx()`

```c
static inline const void * udc_get_event_ctx ( const struct device * dev)
```

```c
#include <zephyr/drivers/usb/udc.h>
```

获取上层上下文（Higher Layer Context）的指针。

上下文地址作为 udc_init() 的参数传入，并保存在 UDC 数据中。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例的设备结构体的指针。 |

**返回（Returns）**：指向上层上下文的不透明指针（Opaque Pointer）。

<a id="ga075edc81fb3e39c2b377fc56c8c0915c"></a>

### `udc_host_wakeup()`

```c
static inline int udc_host_wakeup ( const struct device * dev)
```

```c
#include <zephyr/drivers/usb/udc.h>
```

发起主机唤醒过程（Host Wakeup）。

发起主机唤醒。仅在总线挂起时才可进行。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例的设备结构体的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EPERM` | 控制器尚未启用，或尚未初始化。 |

**返回（Returns）**：成功时为 0，其他所有值均应视为错误。

> 译注（源码核对）：公共包装层检查 enabled 状态后调用驱动；原文要求的总线挂起前提不能据此省略。设备栈的远程唤醒策略与主机许可也不能由这个底层入口代替。

<a id="ga0670bec8b55c013fb607ba53a8634ad4"></a>

### `udc_init()`

```c
int udc_init ( const struct device * dev, udc_event_cb_t event_cb, const void *const event_ctx )
```

```c
#include <zephyr/drivers/usb/udc.h>
```

初始化 USB 设备控制器。

初始化 USB 设备控制器及控制 IN／OUT 端点。初始化后，控制器驱动应能检测总线供电状态，并报告供电状态变化。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例的设备结构体的指针。 |
| `[in] event_cb` | 由上层 USB 设备栈提供的事件回调（Event Callback）。 |
| `[in] event_ctx` | 指向上层上下文的不透明指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | 参数错误，未传入回调。 |
| `-EALREADY` | 已经初始化。 |

**返回（Returns）**：成功时为 0，其他所有值均应视为错误。

> 译注（源码核对）：当前公共实现同时要求 event_cb 和 event_ctx 非 NULL；原返回值说明只提到未传回调。初始化成功后仅设置 initialized 状态，设备可被主机识别还需要 udc_enable()。

<a id="ga2c09f2a1e89c91527a8492019089d13f"></a>

### `udc_is_enabled()`

```c
static inline bool udc_is_enabled ( const struct device * dev)
```

```c
#include <zephyr/drivers/usb/udc.h>
```

检查控制器是否已启用（Enabled）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例的设备结构体的指针。 |

**返回（Returns）**：控制器已启用时为 true，否则为 false。

<a id="ga40e50cf79b40d3792513e8fea3347f59"></a>

### `udc_is_initialized()`

```c
static inline bool udc_is_initialized ( const struct device * dev)
```

```c
#include <zephyr/drivers/usb/udc.h>
```

检查控制器是否已初始化（Initialized）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例的设备结构体的指针。 |

**返回（Returns）**：控制器已初始化时为 true，否则为 false。

<a id="ga88786eda763fce5c2a51521650ccc9f4"></a>

### `udc_is_suspended()`

```c
static inline bool udc_is_suspended ( const struct device * dev)
```

```c
#include <zephyr/drivers/usb/udc.h>
```

检查控制器是否已挂起（Suspended）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例的设备结构体的指针。 |

**返回（Returns）**：控制器已挂起时为 true，否则为 false。

<a id="ga6da3d836e868f2d09fe24854c2d76aeb"></a>

### `udc_mps_ep_size()`

```c
static inline uint16_t udc_mps_ep_size ( const struct udc_ep_config *const cfg)
```

```c
#include <zephyr/drivers/usb/udc.h>
```

从 UDC 端点配置取得端点大小。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] cfg` | 指向 UDC 端点配置的指针。 |

**返回（Returns）**：端点大小。

> 译注（源码核对）：此函数通过 USB_MPS_EP_SIZE(cfg->mps) 提取包长部分，不直接返回完整 wMaxPacketSize 编码。高带宽传输的附加事务位不属于此返回值。

<a id="ga409efee6a62a656a1349c07ba3a42bad"></a>

### `udc_purge_queues()`

```c
int udc_purge_queues ( const struct device * dev)
```

```c
#include <zephyr/drivers/usb/udc.h>
```

在控制器关闭后清空控制端点队列。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例的设备结构体的指针。 |

**返回（Returns）**：成功时为 0，其他所有值均应视为错误；-EBUSY 表示控制器尚未关闭。

> 译注（源码核对）：当前实现检查 initialized 位；只有关闭后才允许清理。它只遍历控制 IN 和控制 OUT 两个队列，并对缓冲区调用 net_buf_unref()，不是任意端点的统一取消接口。

<a id="ga6feb32a2263307bdde9acc63d3c2ebb1"></a>

### `udc_set_address()`

```c
static inline int udc_set_address ( const struct device * dev, const uint8_t addr )
```

```c
#include <zephyr/drivers/usb/udc.h>
```

设置 USB 设备地址。

设置已启用的 USB 设备的地址。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例的设备结构体的指针。 |
| `[in] addr` | USB 设备地址。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EPERM` | 控制器尚未启用，或尚未初始化。 |

**返回（Returns）**：成功时为 0，其他所有值均应视为错误。

<a id="ga59a92eb60575ca80d205cc29b4fb4f21"></a>

### `udc_shutdown()`

```c
int udc_shutdown ( const struct device * dev)
```

```c
#include <zephyr/drivers/usb/udc.h>
```

关闭 USB 设备控制器的电源。

完全关闭控制器，以降低能耗或改变控制器角色。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例的设备结构体的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EALREADY` | 控制器尚未初始化。 |

**返回（Returns）**：成功时为 0，其他所有值均应视为错误。

> 译注（源码核对）：当前公共实现要求先停用：仍处于 enabled 状态返回 -EBUSY，未初始化返回 -EALREADY。调用驱动 shutdown 后会清除 initialized 位，即使驱动返回错误也会清除此位。此过程与随后清空控制端点队列是不同动作。

<a id="ga7f575b548833cc1e5109e0d919630b3f"></a>

### `udc_test_mode()`

```c
static inline int udc_test_mode ( const struct device * dev, const uint8_t mode, const bool dryrun )
```

```c
#include <zephyr/drivers/usb/udc.h>
```

启用测试模式（Test Mode）。

为进行符合性测试（Compliance Testing），高速控制器必须支持测试模式。特定测试通过 SetFeature(TEST_MODE) 请求启用。要退出测试模式，需要对设备断电后重新上电。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 指向驱动实例的设备结构体的指针。 |
| `[in] mode` | 测试模式。 |
| `[in] dryrun` | 仅验证特定模式能否启用，不实际启用测试模式。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOTSUP` | 不支持该测试模式。 |

**返回（Returns）**：成功时为 0，其他所有值均应视为错误。

> 译注（源码核对）：当前实现还检查 enabled 状态，未启用返回 -EPERM；驱动未提供 test_mode 回调时返回 -ENOTSUP。dryrun 为 true 表示只验证。本页翻译没有启用测试模式或对设备断电。

## 30.4\_相关源码与使用边界

控制器接口与结构定义来自 `zephyr/drivers/usb/udc.h`，缓冲区宏来自 `zephyr/drivers/usb/usb_buf.h`。本仓库的[对应头文件](../../../include/zephyr/drivers/usb/udc.h)、[公共实现](../../../drivers/usb/udc/udc_common.c)、[内部辅助接口](../../../drivers/usb/udc/udc_common.h)和[驱动骨架](../../../drivers/usb/udc/udc_skeleton.c)可用于源码跟踪；版本可能与官方 latest 不同。译注依据保存的[官方头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/drivers/usb/udc.h)、[公共实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/usb/udc/udc_common.c)、[内部接口](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/usb/udc/udc_common.h)及[骨架实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/usb/udc/udc_skeleton.c)，摘要见[来源记录](../SOURCES.md)。本批没有编译、运行或操作USB设备。

<a id="header-func-members"></a>
<a id="func-members"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

[上一章](P029_USB设备控制器API说明.md) · [返回大纲](大纲.md) · [下一章](P031_USB设备控制器驱动接口.md)
