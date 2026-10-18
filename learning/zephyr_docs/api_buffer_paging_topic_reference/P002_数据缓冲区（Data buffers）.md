---
id: learning.zephyr-docs.api-buffer-paging-topic-reference.page-2
title: 数据缓冲区（Data buffers）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_数据缓冲区（Data buffers）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

数据缓冲区（Data buffers）

<a id="details"></a>

数据缓冲区（Data Buffers）。引入版本（Since）：1.7；API 版本（Version）：1.0.0。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.1\_宏定义（Macros）

<a id="r_ga41f80f3995e79982f704f832394a6bef"></a>

```c
#define BT_BUF_RESERVE 1
```

相关声明：[BT_BUF_RESERVE](#ga41f80f3995e79982f704f832394a6bef)。

<a id="r_ga9c114a415dc8fc2b84503736b1283468"></a>

```c
#define BT_BUF_SIZE(size)
```

相关声明：[BT_BUF_SIZE](#ga9c114a415dc8fc2b84503736b1283468)。

用于在缓冲区大小计算中计入预留主机控制器接口数据（HCI Data）的辅助宏。

<a id="r_ga8f570211d5e391be63bd46c189eac637"></a>

```c
#define BT_BUF_ACL_SIZE(size)
```

相关声明：[BT_BUF_ACL_SIZE](#ga8f570211d5e391be63bd46c189eac637)。

计算 HCI 异步面向连接（ACL）数据包所需缓冲区大小的辅助宏。

<a id="r_ga098d042ed58592d7c2428967928ee478"></a>

```c
#define BT_BUF_EVT_SIZE(size)
```

相关声明：[BT_BUF_EVT_SIZE](#ga098d042ed58592d7c2428967928ee478)。

计算 HCI 事件数据包（Event Packets）所需缓冲区大小的辅助宏。

<a id="r_ga9dc9de00be5e8bf673ec60921ea6681b"></a>

```c
#define BT_BUF_CMD_SIZE(size)
```

相关声明：[BT_BUF_CMD_SIZE](#ga9dc9de00be5e8bf673ec60921ea6681b)。

计算 HCI 命令数据包（Command Packets）所需缓冲区大小的辅助宏。

<a id="r_gaa820dee05a7202304e1aaa9a36386ca4"></a>

```c
#define BT_BUF_ISO_SIZE(size)
```

相关声明：[BT_BUF_ISO_SIZE](#gaa820dee05a7202304e1aaa9a36386ca4)。

计算 HCI 等时数据包（ISO Packets）所需缓冲区大小的辅助宏。

<a id="r_ga3ad106326ce13d6eb61d0ac16f592003"></a>

```c
#define BT_BUF_ACL_RX_SIZE BT_BUF_ACL_SIZE(CONFIG_BT_BUF_ACL_RX_SIZE)
```

相关声明：[BT_BUF_ACL_RX_SIZE](#ga3ad106326ce13d6eb61d0ac16f592003)、[BT_BUF_ACL_SIZE](#ga8f570211d5e391be63bd46c189eac637)。

HCI ACL 接收缓冲区（RX Buffers）所需的数据大小。

<a id="r_gac76caf2a7fce82ba652eab094162ec66"></a>

```c
#define BT_BUF_EVT_RX_SIZE BT_BUF_EVT_SIZE(CONFIG_BT_BUF_EVT_RX_SIZE)
```

相关声明：[BT_BUF_EVT_RX_SIZE](#gac76caf2a7fce82ba652eab094162ec66)、[BT_BUF_EVT_SIZE](#ga098d042ed58592d7c2428967928ee478)。

HCI 事件接收缓冲区（Event RX Buffers）所需的数据大小。

<a id="r_gae5db5f9f282f9675fe620842e0c50337"></a>

```c
#define BT_BUF_ISO_RX_SIZE 0
```

相关声明：[BT_BUF_ISO_RX_SIZE](#gae5db5f9f282f9675fe620842e0c50337)。

<a id="r_gac45f7915fff9516d9d156a42794e8221"></a>

```c
#define BT_BUF_ISO_RX_COUNT 0
```

相关声明：[BT_BUF_ISO_RX_COUNT](#gac45f7915fff9516d9d156a42794e8221)。

<a id="r_ga9a196035ab78158867ce301c698c08e1"></a>

```c
#define BT_BUF_ACL_RX_COUNT_MAX 65535
```

相关声明：[BT_BUF_ACL_RX_COUNT_MAX](#ga9a196035ab78158867ce301c698c08e1)。

<a id="r_ga2a43657d82801ab838928fd544d93f1f"></a>

```c
#define BT_BUF_ACL_RX_COUNT_EXTRA 0
```

相关声明：[BT_BUF_ACL_RX_COUNT_EXTRA](#ga2a43657d82801ab838928fd544d93f1f)。

<a id="r_ga1f2226f2fb0a4ea2b215e1c5572ecbf6"></a>

```c
#define BT_BUF_ACL_RX_COUNT 0
```

相关声明：[BT_BUF_ACL_RX_COUNT](#ga1f2226f2fb0a4ea2b215e1c5572ecbf6)。

<a id="r_ga3e16a5f4c0c9c4c9117d972b7043d82b"></a>

```c
#define BT_BUF_RX_SIZE
```

相关声明：[BT_BUF_RX_SIZE](#ga3e16a5f4c0c9c4c9117d972b7043d82b)。

HCI ACL、HCI ISO 或事件接收缓冲区（RX Buffers）所需的数据大小。

<a id="r_gaa3ab0861dfd4ebc5f7485f36c1b0fdf1"></a>

```c
#define BT_BUF_RX_COUNT
```

相关声明：[BT_BUF_RX_COUNT](#gaa3ab0861dfd4ebc5f7485f36c1b0fdf1)。

HCI ACL 或 HCI ISO 接收缓冲区，加上事件接收缓冲区（Event RX Buffers）所需的缓冲区数量。

<a id="r_ga366c2eee5dcc6056430b203d1c020042"></a>

```c
#define BT_BUF_CMD_TX_SIZE BT_BUF_CMD_SIZE(CONFIG_BT_BUF_CMD_TX_SIZE)
```

相关声明：[BT_BUF_CMD_TX_SIZE](#ga366c2eee5dcc6056430b203d1c020042)、[BT_BUF_CMD_SIZE](#ga9dc9de00be5e8bf673ec60921ea6681b)。

HCI 命令缓冲区（Command Buffers）所需的数据大小。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 2.2\_类型定义（Typedefs）

<a id="r_gaf5c7be1db66cc51c588938fe0b332040"></a>

```c
typedef void(* bt_buf_rx_freed_cb_t) (enum bt_buf_type type_mask)
```

相关声明：[bt_buf_rx_freed_cb_t](#gaf5c7be1db66cc51c588938fe0b332040)、[bt_buf_type](#gafe1539a89ba3389d52d010a071620d7b)。

用于通知传入数据池（Incoming Data Pool）中有缓冲区被释放的回调函数（Callback）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 2.3\_枚举（Enumerations）

<a id="r_gafe1539a89ba3389d52d010a071620d7b"></a>

```c
enum bt_buf_type { BT_BUF_TYPE_NONE = 0 , BT_BUF_CMD = (1UL << (0)) , BT_BUF_EVT = (1UL << (1)) , BT_BUF_ACL_OUT = (1UL << (2)) , BT_BUF_ACL_IN = (1UL << (3)) , BT_BUF_ISO_OUT = (1UL << (4)) , BT_BUF_ISO_IN = (1UL << (5)) }
```

相关声明：[bt_buf_type](#gafe1539a89ba3389d52d010a071620d7b)、[BT_BUF_TYPE_NONE](#ggafe1539a89ba3389d52d010a071620d7ba370190256608b003d85a149fa8039a8d)、[BT_BUF_CMD](#ggafe1539a89ba3389d52d010a071620d7baead9b640992dd72bd90ebd5d1fa3aaf1)、[BT_BUF_EVT](#ggafe1539a89ba3389d52d010a071620d7ba350a2419b238423e479203a61d45a6e5)、[BT_BUF_ACL_OUT](#ggafe1539a89ba3389d52d010a071620d7ba4332d09d0ae276cf48aa550cf2ab4091)、[BT_BUF_ACL_IN](#ggafe1539a89ba3389d52d010a071620d7baff31d58d06bf1d330f570bf8f1600c13)、[BT_BUF_ISO_OUT](#ggafe1539a89ba3389d52d010a071620d7ba4137aa547b58a7dbf69ef9c29127fa7e)、[BT_BUF_ISO_IN](#ggafe1539a89ba3389d52d010a071620d7badd49c17ef6b2f452c9172fce6f96fb9e)。

以位掩码（Bitmask）形式表示在蓝牙协议栈中传递的缓冲区可能具有的类型。

<a id="r_gaba424dbbb447b1826cbbe715a228744c"></a>

```c
enum bt_buf_dir { BT_BUF_IN , BT_BUF_OUT }
```

相关声明：[bt_buf_dir](#gaba424dbbb447b1826cbbe715a228744c)、[BT_BUF_IN](#ggaba424dbbb447b1826cbbe715a228744cac877edada534dc90a2ad7a8fcb9ffc77)、[BT_BUF_OUT](#ggaba424dbbb447b1826cbbe715a228744ca14de2807d9e45293b6d219b9ca28bc05)。

HCI 数据包方向（Packet Direction）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.4\_函数（Functions）

<a id="r_gae355c6555a1d514332b2d594bcaf416c"></a>

```c
static uint8_t bt_buf_type_to_h4 (enum bt_buf_type type)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_buf_type_to_h4](#gae355c6555a1d514332b2d594bcaf416c)、[bt_buf_type](#gafe1539a89ba3389d52d010a071620d7b)。

从 `bt_buf_type` 转换为 H:4 类型（Type）。

<a id="r_ga01c7d236ef77e4ba334401c628f582a9"></a>

```c
static enum bt_buf_type bt_buf_type_from_h4 (uint8_t h4_type, enum bt_buf_dir dir)
```

相关声明：[bt_buf_type](#gafe1539a89ba3389d52d010a071620d7b)、[bt_buf_type_from_h4](#ga01c7d236ef77e4ba334401c628f582a9)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_buf_dir](#gaba424dbbb447b1826cbbe715a228744c)。

从 H:4 类型转换为 `bt_buf_type`。

<a id="r_ga4013cce9637f5aa2742d1f1aaa00e7ee"></a>

```c
struct net_buf * bt_buf_get_rx (enum bt_buf_type type, k_timeout_t timeout)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_buf_get_rx](#ga4013cce9637f5aa2742d1f1aaa00e7ee)、[bt_buf_type](#gafe1539a89ba3389d52d010a071620d7b)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

为传入数据（Incoming Data）分配缓冲区。

<a id="r_gaf946b1bf3706fe74c6d0c9faaaf478f5"></a>

```c
void bt_buf_rx_freed_cb_set (bt_buf_rx_freed_cb_t cb)
```

相关声明：[bt_buf_rx_freed_cb_set](#gaf946b1bf3706fe74c6d0c9faaaf478f5)、[bt_buf_rx_freed_cb_t](#gaf5c7be1db66cc51c588938fe0b332040)。

设置回调，以通知传入数据池（Incoming Data Pool）中有缓冲区被释放。

<a id="r_ga761a31b7fb19f2325b3a9ac6b1fb1700"></a>

```c
struct net_buf * bt_buf_get_tx (enum bt_buf_type type, k_timeout_t timeout, const void *data, size_t size)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_buf_get_tx](#ga761a31b7fb19f2325b3a9ac6b1fb1700)、[bt_buf_type](#gafe1539a89ba3389d52d010a071620d7b)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

为传出数据（Outgoing Data）分配缓冲区。

<a id="r_ga7b7a19302881dea458fbd2e9e2309b30"></a>

```c
struct net_buf * bt_buf_get_evt (uint8_t evt, bool discardable, k_timeout_t timeout)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_buf_get_evt](#ga7b7a19302881dea458fbd2e9e2309b30)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

为 HCI 事件（Event）分配缓冲区。

## 2.5\_详细说明（Detailed Documentation）

<a id="ga1f2226f2fb0a4ea2b215e1c5572ecbf6"></a>

### `BT_BUF_ACL_RX_COUNT`

```c
#define BT_BUF_ACL_RX_COUNT 0
```

```c
#include <zephyr/bluetooth/buf.h>
```

<a id="ga2a43657d82801ab838928fd544d93f1f"></a>

### `BT_BUF_ACL_RX_COUNT_EXTRA`

```c
#define BT_BUF_ACL_RX_COUNT_EXTRA 0
```

```c
#include <zephyr/bluetooth/buf.h>
```

<a id="ga9a196035ab78158867ce301c698c08e1"></a>

### `BT_BUF_ACL_RX_COUNT_MAX`

```c
#define BT_BUF_ACL_RX_COUNT_MAX 65535
```

```c
#include <zephyr/bluetooth/buf.h>
```

<a id="ga3ad106326ce13d6eb61d0ac16f592003"></a>

### `BT_BUF_ACL_RX_SIZE`

```c
#define BT_BUF_ACL_RX_SIZE BT_BUF_ACL_SIZE(CONFIG_BT_BUF_ACL_RX_SIZE)
```

```c
#include <zephyr/bluetooth/buf.h>
```

HCI ACL 接收缓冲区（RX Buffers）所需的数据大小。

<a id="ga8f570211d5e391be63bd46c189eac637"></a>

### `BT_BUF_ACL_SIZE`

```c
#define BT_BUF_ACL_SIZE ( size)
```

```c
#include <zephyr/bluetooth/buf.h>
```

展开值（Value）：

```c
BT_BUF_SIZE(BT_HCI_ACL_HDR_SIZE + (size))
```

计算 HCI 异步面向连接（ACL）数据包所需缓冲区大小的辅助宏。

<a id="ga9dc9de00be5e8bf673ec60921ea6681b"></a>

### `BT_BUF_CMD_SIZE`

```c
#define BT_BUF_CMD_SIZE ( size)
```

```c
#include <zephyr/bluetooth/buf.h>
```

展开值（Value）：

```c
BT_BUF_SIZE(BT_HCI_CMD_HDR_SIZE + (size))
```

计算 HCI 命令数据包（Command Packets）所需缓冲区大小的辅助宏。

<a id="ga366c2eee5dcc6056430b203d1c020042"></a>

### `BT_BUF_CMD_TX_SIZE`

```c
#define BT_BUF_CMD_TX_SIZE BT_BUF_CMD_SIZE(CONFIG_BT_BUF_CMD_TX_SIZE)
```

```c
#include <zephyr/bluetooth/buf.h>
```

HCI 命令缓冲区（Command Buffers）所需的数据大小。

<a id="gac76caf2a7fce82ba652eab094162ec66"></a>

### `BT_BUF_EVT_RX_SIZE`

```c
#define BT_BUF_EVT_RX_SIZE BT_BUF_EVT_SIZE(CONFIG_BT_BUF_EVT_RX_SIZE)
```

```c
#include <zephyr/bluetooth/buf.h>
```

HCI 事件接收缓冲区（Event RX Buffers）所需的数据大小。

<a id="ga098d042ed58592d7c2428967928ee478"></a>

### `BT_BUF_EVT_SIZE`

```c
#define BT_BUF_EVT_SIZE ( size)
```

```c
#include <zephyr/bluetooth/buf.h>
```

展开值（Value）：

```c
BT_BUF_SIZE(BT_HCI_EVT_HDR_SIZE + (size))
```

计算 HCI 事件数据包（Event Packets）所需缓冲区大小的辅助宏。

<a id="gac45f7915fff9516d9d156a42794e8221"></a>

### `BT_BUF_ISO_RX_COUNT`

```c
#define BT_BUF_ISO_RX_COUNT 0
```

```c
#include <zephyr/bluetooth/buf.h>
```

<a id="gae5db5f9f282f9675fe620842e0c50337"></a>

### `BT_BUF_ISO_RX_SIZE`

```c
#define BT_BUF_ISO_RX_SIZE 0
```

```c
#include <zephyr/bluetooth/buf.h>
```

<a id="gaa820dee05a7202304e1aaa9a36386ca4"></a>

### `BT_BUF_ISO_SIZE`

```c
#define BT_BUF_ISO_SIZE ( size)
```

```c
#include <zephyr/bluetooth/buf.h>
```

展开值（Value）：

```c
BT_BUF_SIZE(BT_HCI_ISO_HDR_SIZE + \
BT_HCI_ISO_SDU_TS_HDR_SIZE + \
(size))
```

计算 HCI 等时数据包（ISO Packets）所需缓冲区大小的辅助宏。

<a id="ga41f80f3995e79982f704f832394a6bef"></a>

### `BT_BUF_RESERVE`

```c
#define BT_BUF_RESERVE 1
```

```c
#include <zephyr/bluetooth/buf.h>
```

<a id="gaa3ab0861dfd4ebc5f7485f36c1b0fdf1"></a>

### `BT_BUF_RX_COUNT`

```c
#define BT_BUF_RX_COUNT
```

```c
#include <zephyr/bluetooth/buf.h>
```

展开值（Value）：

```c
(CONFIG_BT_BUF_EVT_RX_COUNT + \
MAX(BT_BUF_ACL_RX_COUNT, BT_BUF_ISO_RX_COUNT))
```

HCI ACL 或 HCI ISO 接收缓冲区，加上事件接收缓冲区（Event RX Buffers）所需的缓冲区数量。

<a id="ga3e16a5f4c0c9c4c9117d972b7043d82b"></a>

### `BT_BUF_RX_SIZE`

```c
#define BT_BUF_RX_SIZE
```

```c
#include <zephyr/bluetooth/buf.h>
```

展开值（Value）：

```c
(MAX(MAX(BT_BUF_ACL_RX_SIZE, BT_BUF_EVT_RX_SIZE), \
BT_BUF_ISO_RX_SIZE))
```

HCI ACL、HCI ISO 或事件接收缓冲区（RX Buffers）所需的数据大小。

<a id="ga9c114a415dc8fc2b84503736b1283468"></a>

### `BT_BUF_SIZE`

```c
#define BT_BUF_SIZE ( size)
```

```c
#include <zephyr/bluetooth/buf.h>
```

展开值（Value）：

```c
(BT_BUF_RESERVE + (size))
```

用于在缓冲区大小计算中计入预留主机控制器接口数据（HCI Data）的辅助宏。

<a id="gaf5c7be1db66cc51c588938fe0b332040"></a>

### `bt_buf_rx_freed_cb_t`

```c
typedef void(* bt_buf_rx_freed_cb_t) (enum bt_buf_type type_mask)
```

声明属性：`isr-ok`（允许从中断服务程序ISR调用）。

```c
#include <zephyr/bluetooth/buf.h>
```

用于通知传入数据池（Incoming Data Pool）中有缓冲区被释放的回调函数（Callback）。

释放指定类型的缓冲区且可通过 bt_buf_get_rx 函数重新申请该缓冲区时，调用此回调（Callback）。但此回调在释放缓冲区的操作上下文中调用，不得尝试从同一个池分配新缓冲区。

此回调只能执行极短的非阻塞操作（Non-blocking Operations），例如提交工作项。在线程上下文中调用时，执行期间调度器被锁定，被调用方不得进行任何使当前线程退出就绪状态的操作。在中断服务例程（ISR）上下文中调用时，回调在未锁定调度器的情况下运行。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `type_mask` | 已释放缓冲区类型的位掩码（Bit Mask）。 |

<a id="gaba424dbbb447b1826cbbe715a228744c"></a>

### `bt_buf_dir`

```c
enum bt_buf_dir
```

```c
#include <zephyr/bluetooth/buf.h>
```

HCI 数据包方向（Packet Direction）。

仅用于将 H:4 映射为 BT_BUF_* 值。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_BUF_IN` | 从控制器（Controller）发往主机（Host）的数据包。 |
| `BT_BUF_OUT` | 从主机（Host）发往控制器（Controller）的数据包。 |

<a id="gafe1539a89ba3389d52d010a071620d7b"></a>

### `bt_buf_type`

```c
enum bt_buf_type
```

```c
#include <zephyr/bluetooth/buf.h>
```

以位掩码（Bitmask）形式表示在蓝牙协议栈中传递的缓冲区可能具有的类型。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_BUF_TYPE_NONE` | 未知／无效的数据包类型，用于错误检查。 |
| `BT_BUF_CMD` | HCI 命令（Command）。 |
| `BT_BUF_EVT` | HCI 事件（Event）。 |
| `BT_BUF_ACL_OUT` | 出站 ACL 数据（Outgoing ACL Data）。 |
| `BT_BUF_ACL_IN` | 入站 ACL 数据（Incoming ACL Data）。 |
| `BT_BUF_ISO_OUT` | 出站 ISO 数据（Outgoing ISO Data）。 |
| `BT_BUF_ISO_IN` | 入站 ISO 数据（Incoming ISO Data）。 |

<a id="ga7b7a19302881dea458fbd2e9e2309b30"></a>

### `bt_buf_get_evt()`

```c
struct net_buf * bt_buf_get_evt ( uint8_t evt, bool discardable, k_timeout_t timeout )
```

```c
#include <zephyr/bluetooth/buf.h>
```

为 HCI 事件（Event）分配缓冲区。

此操作设置缓冲区类型（Buffer Type），因此无需再将其显式编码到缓冲区内。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `evt` | HCI 事件码（Event Code） |
| `discardable` | 驱动是否认为该事件可以丢弃（Discardable）。 |
| `timeout` | 获取缓冲区的非负等待时长，或特殊值 K_NO_WAIT、K_FOREVER 之一。 |

**返回（Returns）**：返回值（Returns）：新缓冲区。

<a id="ga4013cce9637f5aa2742d1f1aaa00e7ee"></a>

### `bt_buf_get_rx()`

```c
struct net_buf * bt_buf_get_rx ( enum bt_buf_type type, k_timeout_t timeout )
```

```c
#include <zephyr/bluetooth/buf.h>
```

为传入数据（Incoming Data）分配缓冲区。

此操作设置缓冲区类型（Buffer Type），因此无需再将其显式编码到缓冲区内。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `type` | 缓冲区类型，仅允许 BT_BUF_EVT、BT_BUF_ACL_IN 和 BT_BUF_ISO_IN。 |
| `timeout` | 获取缓冲区的非负等待时长，或特殊值 K_NO_WAIT、K_FOREVER 之一。 |

**返回（Returns）**：返回值（Returns）：新缓冲区。

<a id="ga761a31b7fb19f2325b3a9ac6b1fb1700"></a>

### `bt_buf_get_tx()`

```c
struct net_buf * bt_buf_get_tx ( enum bt_buf_type type, k_timeout_t timeout, const void * data, size_t size )
```

```c
#include <zephyr/bluetooth/buf.h>
```

为传出数据（Outgoing Data）分配缓冲区。

此操作设置缓冲区类型（Buffer Type），因此无需再将其显式编码到缓冲区内。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `type` | 缓冲区类型，为 BT_BUF_CMD 或 BT_BUF_ACL_OUT。 |
| `timeout` | 获取缓冲区的非负等待时长，或特殊值 K_NO_WAIT、K_FOREVER 之一。 |
| `data` | 追加到缓冲区的初始数据（Initial Data）；此参数可选，可以为 NULL。 |
| `size` | 初始数据大小（Initial Data Size）。 |

**返回（Returns）**：返回值（Returns）：新缓冲区。

<a id="gaf946b1bf3706fe74c6d0c9faaaf478f5"></a>

### `bt_buf_rx_freed_cb_set()`

```c
void bt_buf_rx_freed_cb_set ( bt_buf_rx_freed_cb_t cb)
```

声明属性：`isr-ok`（允许从中断服务程序ISR调用）。

```c
#include <zephyr/bluetooth/buf.h>
```

设置回调，以通知传入数据池（Incoming Data Pool）中有缓冲区被释放。

可以安全地在该回调自身内部调用此函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 通知入站数据池缓冲区已释放的回调（Callback）。设为 NULL 可禁用回调。 |

<a id="ga01c7d236ef77e4ba334401c628f582a9"></a>

### `bt_buf_type_from_h4()`

```c
enum bt_buf_type bt_buf_type_from_h4 ( uint8_t h4_type, enum bt_buf_dir dir )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/buf.h>
```

从 H:4 类型转换为 `bt_buf_type`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `h4_type` | 要转换的 H:4 类型 |
| `dir` | 数据包方向（Direction） |

**返回（Returns）**：返回值（Returns）：bt_buf_type。

<a id="gae355c6555a1d514332b2d594bcaf416c"></a>

### `bt_buf_type_to_h4()`

```c
uint8_t bt_buf_type_to_h4 ( enum bt_buf_type type)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/buf.h>
```

从 `bt_buf_type` 转换为 H:4 类型（Type）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `type` | 要转换的 bt_buf_type |

**返回（Returns）**：返回值（Returns）：H:4 类型。


## 2.6\_原页交叉引用（Cross References）

- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [zephyr/bluetooth/buf.h](../api_file_display_management_reference/P003_zephyr__bluetooth__buf.h_文件参考.md)
- [BT_HCI_ACL_HDR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a7418d845532d6b077a9695454fa65bc5)
- [BT_HCI_CMD_HDR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#acdf2b6de1459a7492415a8987ad9a896)
- [BT_HCI_EVT_HDR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a0edb7e700cfa557e7fb8ec44f5eea961)
- [BT_HCI_ISO_HDR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a75c1f5e8a44b034004ecfebdb75ee4be)
- [BT_HCI_ISO_SDU_TS_HDR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a22db454317bc89afe092ab9127888441)
- [MAX](../util_reference/P001_通用工具公共接口.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__bt__buf_html_ga9c114a415dc8fc2b84503736b1283468"></a>
<a id="ahci__types_8h_html_a7418d845532d6b077a9695454fa65bc5"></a>
<a id="ahci__types_8h_html_acdf2b6de1459a7492415a8987ad9a896"></a>
<a id="ahci__types_8h_html_a0edb7e700cfa557e7fb8ec44f5eea961"></a>
<a id="ahci__types_8h_html_a22db454317bc89afe092ab9127888441"></a>
<a id="ahci__types_8h_html_a75c1f5e8a44b034004ecfebdb75ee4be"></a>
<a id="agroup__bt__buf_html_ga1f2226f2fb0a4ea2b215e1c5572ecbf6"></a>
<a id="agroup__bt__buf_html_gac45f7915fff9516d9d156a42794e8221"></a>
<a id="agroup__bt__buf_html_ga3ad106326ce13d6eb61d0ac16f592003"></a>
<a id="agroup__bt__buf_html_gac76caf2a7fce82ba652eab094162ec66"></a>
<a id="agroup__bt__buf_html_gae5db5f9f282f9675fe620842e0c50337"></a>
<a id="agroup__sys-util_html_gafa99ec4acc4ecb2dc3c2d05da15d0e3f"></a>
<a id="agroup__bt__buf_html_ga41f80f3995e79982f704f832394a6bef"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggaba424dbbb447b1826cbbe715a228744cac877edada534dc90a2ad7a8fcb9ffc77"></a>
<a id="ggaba424dbbb447b1826cbbe715a228744ca14de2807d9e45293b6d219b9ca28bc05"></a>
<a id="ggafe1539a89ba3389d52d010a071620d7ba370190256608b003d85a149fa8039a8d"></a>
<a id="ggafe1539a89ba3389d52d010a071620d7baead9b640992dd72bd90ebd5d1fa3aaf1"></a>
<a id="ggafe1539a89ba3389d52d010a071620d7ba350a2419b238423e479203a61d45a6e5"></a>
<a id="ggafe1539a89ba3389d52d010a071620d7ba4332d09d0ae276cf48aa550cf2ab4091"></a>
<a id="ggafe1539a89ba3389d52d010a071620d7baff31d58d06bf1d330f570bf8f1600c13"></a>
<a id="ggafe1539a89ba3389d52d010a071620d7ba4137aa547b58a7dbf69ef9c29127fa7e"></a>
<a id="ggafe1539a89ba3389d52d010a071620d7badd49c17ef6b2f452c9172fce6f96fb9e"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P001_音频编解码器驱动后端 API（Audio Codec Driver Backend API）.md) · [返回大纲](大纲.md) · [下一章](P003_密码学（Cryptography）.md)
