---
id: learning.zephyr-docs.api-file-display-management-reference.page-3
title: zephyr__bluetooth__buf.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/buf_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_zephyr\_\_bluetooth\_\_buf.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/buf_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙数据缓冲区（Bluetooth Data Buffer）的API。

<a id="details"></a>

```c
#include <stddef.h>
#include <stdint.h>
#include <zephyr/autoconf.h>
#include <zephyr/bluetooth/hci.h>
#include <zephyr/bluetooth/hci_types.h>
#include <zephyr/net_buf.h>
#include <zephyr/sys/util.h>
#include <zephyr/sys/util_macro.h>
#include <zephyr/sys/clock.h>
#include <zephyr/toolchain.h>
```

查看此文件的源码。

蓝牙数据缓冲区（Bluetooth Data Buffer）的API。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.1\_宏定义（Macros）

<a id="r_ga41f80f3995e79982f704f832394a6bef"></a>

```c
#define BT_BUF_RESERVE 1
```

相关声明：[BT_BUF_RESERVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ga41f80f3995e79982f704f832394a6bef)。

<a id="r_ga9c114a415dc8fc2b84503736b1283468"></a>

```c
#define BT_BUF_SIZE(size)
```

相关声明：[BT_BUF_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ga9c114a415dc8fc2b84503736b1283468)。

用于在缓冲区大小计算中计入预留主机控制器接口数据（HCI Data）的辅助宏。

<a id="r_ga8f570211d5e391be63bd46c189eac637"></a>

```c
#define BT_BUF_ACL_SIZE(size)
```

相关声明：[BT_BUF_ACL_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ga8f570211d5e391be63bd46c189eac637)。

计算 HCI 异步面向连接（ACL）数据包所需缓冲区大小的辅助宏。

<a id="r_ga098d042ed58592d7c2428967928ee478"></a>

```c
#define BT_BUF_EVT_SIZE(size)
```

相关声明：[BT_BUF_EVT_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ga098d042ed58592d7c2428967928ee478)。

计算 HCI 事件数据包（Event Packets）所需缓冲区大小的辅助宏。

<a id="r_ga9dc9de00be5e8bf673ec60921ea6681b"></a>

```c
#define BT_BUF_CMD_SIZE(size)
```

相关声明：[BT_BUF_CMD_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ga9dc9de00be5e8bf673ec60921ea6681b)。

计算 HCI 命令数据包（Command Packets）所需缓冲区大小的辅助宏。

<a id="r_gaa820dee05a7202304e1aaa9a36386ca4"></a>

```c
#define BT_BUF_ISO_SIZE(size)
```

相关声明：[BT_BUF_ISO_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#gaa820dee05a7202304e1aaa9a36386ca4)。

计算 HCI 等时数据包（ISO Packets）所需缓冲区大小的辅助宏。

<a id="r_ga3ad106326ce13d6eb61d0ac16f592003"></a>

```c
#define BT_BUF_ACL_RX_SIZE BT_BUF_ACL_SIZE(CONFIG_BT_BUF_ACL_RX_SIZE)
```

相关声明：[BT_BUF_ACL_RX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ga3ad106326ce13d6eb61d0ac16f592003)、[BT_BUF_ACL_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ga8f570211d5e391be63bd46c189eac637)。

HCI ACL 接收缓冲区（RX Buffers）所需的数据大小。

<a id="r_gac76caf2a7fce82ba652eab094162ec66"></a>

```c
#define BT_BUF_EVT_RX_SIZE BT_BUF_EVT_SIZE(CONFIG_BT_BUF_EVT_RX_SIZE)
```

相关声明：[BT_BUF_EVT_RX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#gac76caf2a7fce82ba652eab094162ec66)、[BT_BUF_EVT_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ga098d042ed58592d7c2428967928ee478)。

HCI 事件接收缓冲区（Event RX Buffers）所需的数据大小。

<a id="r_gae5db5f9f282f9675fe620842e0c50337"></a>

```c
#define BT_BUF_ISO_RX_SIZE 0
```

相关声明：[BT_BUF_ISO_RX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#gae5db5f9f282f9675fe620842e0c50337)。

<a id="r_gac45f7915fff9516d9d156a42794e8221"></a>

```c
#define BT_BUF_ISO_RX_COUNT 0
```

相关声明：[BT_BUF_ISO_RX_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#gac45f7915fff9516d9d156a42794e8221)。

<a id="r_ga9a196035ab78158867ce301c698c08e1"></a>

```c
#define BT_BUF_ACL_RX_COUNT_MAX 65535
```

相关声明：[BT_BUF_ACL_RX_COUNT_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ga9a196035ab78158867ce301c698c08e1)。

<a id="r_ga2a43657d82801ab838928fd544d93f1f"></a>

```c
#define BT_BUF_ACL_RX_COUNT_EXTRA 0
```

相关声明：[BT_BUF_ACL_RX_COUNT_EXTRA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ga2a43657d82801ab838928fd544d93f1f)。

<a id="r_ga1f2226f2fb0a4ea2b215e1c5572ecbf6"></a>

```c
#define BT_BUF_ACL_RX_COUNT 0
```

相关声明：[BT_BUF_ACL_RX_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ga1f2226f2fb0a4ea2b215e1c5572ecbf6)。

<a id="r_ga3e16a5f4c0c9c4c9117d972b7043d82b"></a>

```c
#define BT_BUF_RX_SIZE
```

相关声明：[BT_BUF_RX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ga3e16a5f4c0c9c4c9117d972b7043d82b)。

HCI ACL、HCI ISO 或事件接收缓冲区（RX Buffers）所需的数据大小。

<a id="r_gaa3ab0861dfd4ebc5f7485f36c1b0fdf1"></a>

```c
#define BT_BUF_RX_COUNT
```

相关声明：[BT_BUF_RX_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#gaa3ab0861dfd4ebc5f7485f36c1b0fdf1)。

HCI ACL 或 HCI ISO 接收缓冲区，加上事件接收缓冲区（Event RX Buffers）所需的缓冲区数量。

<a id="r_ga366c2eee5dcc6056430b203d1c020042"></a>

```c
#define BT_BUF_CMD_TX_SIZE BT_BUF_CMD_SIZE(CONFIG_BT_BUF_CMD_TX_SIZE)
```

相关声明：[BT_BUF_CMD_TX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ga366c2eee5dcc6056430b203d1c020042)、[BT_BUF_CMD_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ga9dc9de00be5e8bf673ec60921ea6681b)。

HCI 命令缓冲区（Command Buffers）所需的数据大小。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 3.2\_类型定义（Typedefs）

<a id="r_gaf5c7be1db66cc51c588938fe0b332040"></a>

```c
typedef void(* bt_buf_rx_freed_cb_t) (enum bt_buf_type type_mask)
```

相关声明：[bt_buf_rx_freed_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#gaf5c7be1db66cc51c588938fe0b332040)、[bt_buf_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#gafe1539a89ba3389d52d010a071620d7b)。

用于通知传入数据池（Incoming Data Pool）中有缓冲区被释放的回调函数（Callback）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 3.3\_枚举（Enumerations）

<a id="r_gafe1539a89ba3389d52d010a071620d7b"></a>

```c
enum bt_buf_type { BT_BUF_TYPE_NONE = 0 , BT_BUF_CMD = (1UL << (0)) , BT_BUF_EVT = (1UL << (1)) , BT_BUF_ACL_OUT = (1UL << (2)) , BT_BUF_ACL_IN = (1UL << (3)) , BT_BUF_ISO_OUT = (1UL << (4)) , BT_BUF_ISO_IN = (1UL << (5)) }
```

相关声明：[bt_buf_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#gafe1539a89ba3389d52d010a071620d7b)、[BT_BUF_TYPE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ggafe1539a89ba3389d52d010a071620d7ba370190256608b003d85a149fa8039a8d)、[BT_BUF_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ggafe1539a89ba3389d52d010a071620d7baead9b640992dd72bd90ebd5d1fa3aaf1)、[BT_BUF_EVT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ggafe1539a89ba3389d52d010a071620d7ba350a2419b238423e479203a61d45a6e5)、[BT_BUF_ACL_OUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ggafe1539a89ba3389d52d010a071620d7ba4332d09d0ae276cf48aa550cf2ab4091)、[BT_BUF_ACL_IN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ggafe1539a89ba3389d52d010a071620d7baff31d58d06bf1d330f570bf8f1600c13)、[BT_BUF_ISO_OUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ggafe1539a89ba3389d52d010a071620d7ba4137aa547b58a7dbf69ef9c29127fa7e)、[BT_BUF_ISO_IN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ggafe1539a89ba3389d52d010a071620d7badd49c17ef6b2f452c9172fce6f96fb9e)。

以位掩码（Bitmask）形式表示在蓝牙协议栈中传递的缓冲区可能具有的类型。

<a id="r_gaba424dbbb447b1826cbbe715a228744c"></a>

```c
enum bt_buf_dir { BT_BUF_IN , BT_BUF_OUT }
```

相关声明：[bt_buf_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#gaba424dbbb447b1826cbbe715a228744c)、[BT_BUF_IN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ggaba424dbbb447b1826cbbe715a228744cac877edada534dc90a2ad7a8fcb9ffc77)、[BT_BUF_OUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ggaba424dbbb447b1826cbbe715a228744ca14de2807d9e45293b6d219b9ca28bc05)。

HCI 数据包方向（Packet Direction）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 3.4\_函数（Functions）

<a id="r_gae355c6555a1d514332b2d594bcaf416c"></a>

```c
static uint8_t bt_buf_type_to_h4 (enum bt_buf_type type)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_buf_type_to_h4](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#gae355c6555a1d514332b2d594bcaf416c)、[bt_buf_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#gafe1539a89ba3389d52d010a071620d7b)。

从 `bt_buf_type` 转换为 H:4 类型（Type）。

<a id="r_ga01c7d236ef77e4ba334401c628f582a9"></a>

```c
static enum bt_buf_type bt_buf_type_from_h4 (uint8_t h4_type, enum bt_buf_dir dir)
```

相关声明：[bt_buf_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#gafe1539a89ba3389d52d010a071620d7b)、[bt_buf_type_from_h4](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ga01c7d236ef77e4ba334401c628f582a9)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_buf_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#gaba424dbbb447b1826cbbe715a228744c)。

从 H:4 类型转换为 `bt_buf_type`。

<a id="r_ga4013cce9637f5aa2742d1f1aaa00e7ee"></a>

```c
struct net_buf * bt_buf_get_rx (enum bt_buf_type type, k_timeout_t timeout)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_buf_get_rx](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ga4013cce9637f5aa2742d1f1aaa00e7ee)、[bt_buf_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#gafe1539a89ba3389d52d010a071620d7b)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

为传入数据（Incoming Data）分配缓冲区。

<a id="r_gaf946b1bf3706fe74c6d0c9faaaf478f5"></a>

```c
void bt_buf_rx_freed_cb_set (bt_buf_rx_freed_cb_t cb)
```

相关声明：[bt_buf_rx_freed_cb_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#gaf946b1bf3706fe74c6d0c9faaaf478f5)、[bt_buf_rx_freed_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#gaf5c7be1db66cc51c588938fe0b332040)。

设置回调，以通知传入数据池（Incoming Data Pool）中有缓冲区被释放。

<a id="r_ga761a31b7fb19f2325b3a9ac6b1fb1700"></a>

```c
struct net_buf * bt_buf_get_tx (enum bt_buf_type type, k_timeout_t timeout, const void *data, size_t size)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_buf_get_tx](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ga761a31b7fb19f2325b3a9ac6b1fb1700)、[bt_buf_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#gafe1539a89ba3389d52d010a071620d7b)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

为传出数据（Outgoing Data）分配缓冲区。

<a id="r_ga7b7a19302881dea458fbd2e9e2309b30"></a>

```c
struct net_buf * bt_buf_get_evt (uint8_t evt, bool discardable, k_timeout_t timeout)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_buf_get_evt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ga7b7a19302881dea458fbd2e9e2309b30)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

为 HCI 事件（Event）分配缓冲区。


## 3.5\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/bluetooth/hci.h](../api_source_supplement_reference/P085_hci.h_源码浏览.md)
- [zephyr/bluetooth/hci_types.h](../api_source_hci_multifunction_reference/P001_hci_types.h_源码浏览.md)
- [zephyr/net_buf.h](../api_source_system_reference/P021_net_buf.h_源码浏览.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [zephyr/sys/util_macro.h](../util_reference/P005_宏工具头文件源码.md)
- [zephyr/sys/clock.h](../timer_reference/P091_系统时钟头文件源码.md)
- [zephyr/toolchain.h](../api_source_compiler_device_reference/P023_toolchain.h_源码浏览.md)
- [查看此文件的源码。](../api_source_system_reference/P005_buf.h_源码浏览.md)
- [BT_BUF_RESERVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ga41f80f3995e79982f704f832394a6bef)
- [BT_BUF_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ga9c114a415dc8fc2b84503736b1283468)
- [BT_BUF_ACL_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ga8f570211d5e391be63bd46c189eac637)
- [BT_BUF_EVT_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ga098d042ed58592d7c2428967928ee478)
- [BT_BUF_CMD_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ga9dc9de00be5e8bf673ec60921ea6681b)
- [BT_BUF_ISO_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#gaa820dee05a7202304e1aaa9a36386ca4)
- [BT_BUF_ACL_RX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ga3ad106326ce13d6eb61d0ac16f592003)
- [BT_BUF_EVT_RX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#gac76caf2a7fce82ba652eab094162ec66)
- [BT_BUF_ISO_RX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#gae5db5f9f282f9675fe620842e0c50337)
- [BT_BUF_ISO_RX_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#gac45f7915fff9516d9d156a42794e8221)
- [BT_BUF_ACL_RX_COUNT_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ga9a196035ab78158867ce301c698c08e1)
- [BT_BUF_ACL_RX_COUNT_EXTRA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ga2a43657d82801ab838928fd544d93f1f)
- [BT_BUF_ACL_RX_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ga1f2226f2fb0a4ea2b215e1c5572ecbf6)
- [BT_BUF_RX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ga3e16a5f4c0c9c4c9117d972b7043d82b)
- [BT_BUF_RX_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#gaa3ab0861dfd4ebc5f7485f36c1b0fdf1)
- [BT_BUF_CMD_TX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ga366c2eee5dcc6056430b203d1c020042)
- [bt_buf_rx_freed_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#gaf5c7be1db66cc51c588938fe0b332040)
- [bt_buf_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#gafe1539a89ba3389d52d010a071620d7b)
- [BT_BUF_TYPE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ggafe1539a89ba3389d52d010a071620d7ba370190256608b003d85a149fa8039a8d)
- [BT_BUF_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ggafe1539a89ba3389d52d010a071620d7baead9b640992dd72bd90ebd5d1fa3aaf1)
- [BT_BUF_EVT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ggafe1539a89ba3389d52d010a071620d7ba350a2419b238423e479203a61d45a6e5)
- [BT_BUF_ACL_OUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ggafe1539a89ba3389d52d010a071620d7ba4332d09d0ae276cf48aa550cf2ab4091)
- [BT_BUF_ACL_IN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ggafe1539a89ba3389d52d010a071620d7baff31d58d06bf1d330f570bf8f1600c13)
- [BT_BUF_ISO_OUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ggafe1539a89ba3389d52d010a071620d7ba4137aa547b58a7dbf69ef9c29127fa7e)
- [BT_BUF_ISO_IN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ggafe1539a89ba3389d52d010a071620d7badd49c17ef6b2f452c9172fce6f96fb9e)
- [bt_buf_dir](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#gaba424dbbb447b1826cbbe715a228744c)
- [BT_BUF_IN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ggaba424dbbb447b1826cbbe715a228744cac877edada534dc90a2ad7a8fcb9ffc77)
- [BT_BUF_OUT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ggaba424dbbb447b1826cbbe715a228744ca14de2807d9e45293b6d219b9ca28bc05)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_buf_type_to_h4](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#gae355c6555a1d514332b2d594bcaf416c)
- [bt_buf_type_from_h4](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ga01c7d236ef77e4ba334401c628f582a9)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [bt_buf_get_rx](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ga4013cce9637f5aa2742d1f1aaa00e7ee)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [bt_buf_rx_freed_cb_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#gaf946b1bf3706fe74c6d0c9faaaf478f5)
- [bt_buf_get_tx](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ga761a31b7fb19f2325b3a9ac6b1fb1700)
- [bt_buf_get_evt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ga7b7a19302881dea458fbd2e9e2309b30)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>

---

[上一章](P002_zephyr__bluetooth__classic__avrcp_cover_art.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P004_zephyr__net__coap_client_tcp.h_文件参考.md)
