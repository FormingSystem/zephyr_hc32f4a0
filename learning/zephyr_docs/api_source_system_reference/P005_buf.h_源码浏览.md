---
id: learning.zephyr-docs.api-source-system-reference.page-5
title: buf.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/buf_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_buf.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/buf_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/buf_8h.html)。

## 5.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="foldopen00040"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="foldopen00058"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="foldopen00070"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="foldopen00095"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="foldopen00127"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="foldopen00167"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="foldopen00177"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="aclock_8h_html"></a>
<a id="agroup__bt__buf_html_ga01c7d236ef77e4ba334401c628f582a9"></a>
<a id="agroup__bt__buf_html_ga1f2226f2fb0a4ea2b215e1c5572ecbf6"></a>
<a id="agroup__bt__buf_html_ga4013cce9637f5aa2742d1f1aaa00e7ee"></a>
<a id="agroup__bt__buf_html_ga761a31b7fb19f2325b3a9ac6b1fb1700"></a>
<a id="agroup__bt__buf_html_ga7b7a19302881dea458fbd2e9e2309b30"></a>
<a id="agroup__bt__buf_html_ga9a196035ab78158867ce301c698c08e1"></a>
<a id="agroup__bt__buf_html_gaba424dbbb447b1826cbbe715a228744c"></a>
<a id="agroup__bt__buf_html_gae355c6555a1d514332b2d594bcaf416c"></a>
<a id="agroup__bt__buf_html_gaf5c7be1db66cc51c588938fe0b332040"></a>
<a id="agroup__bt__buf_html_gaf946b1bf3706fe74c6d0c9faaaf478f5"></a>
<a id="agroup__bt__buf_html_gafe1539a89ba3389d52d010a071620d7b"></a>
<a id="agroup__bt__buf_html_ggaba424dbbb447b1826cbbe715a228744ca14de2807d9e45293b6d219b9ca28bc05"></a>
<a id="agroup__bt__buf_html_ggaba424dbbb447b1826cbbe715a228744cac877edada534dc90a2ad7a8fcb9ffc77"></a>
<a id="agroup__bt__buf_html_ggafe1539a89ba3389d52d010a071620d7ba350a2419b238423e479203a61d45a6e5"></a>
<a id="agroup__bt__buf_html_ggafe1539a89ba3389d52d010a071620d7ba370190256608b003d85a149fa8039a8d"></a>
<a id="agroup__bt__buf_html_ggafe1539a89ba3389d52d010a071620d7ba4137aa547b58a7dbf69ef9c29127fa7e"></a>
<a id="agroup__bt__buf_html_ggafe1539a89ba3389d52d010a071620d7ba4332d09d0ae276cf48aa550cf2ab4091"></a>
<a id="agroup__bt__buf_html_ggafe1539a89ba3389d52d010a071620d7badd49c17ef6b2f452c9172fce6f96fb9e"></a>
<a id="agroup__bt__buf_html_ggafe1539a89ba3389d52d010a071620d7baead9b640992dd72bd90ebd5d1fa3aaf1"></a>
<a id="agroup__bt__buf_html_ggafe1539a89ba3389d52d010a071620d7baff31d58d06bf1d330f570bf8f1600c13"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="ahci_8h_html"></a>
<a id="ahci__types_8h_html"></a>
<a id="ahci__types_8h_html_a17386452bbd60c85959296b6539232bd"></a>
<a id="ahci__types_8h_html_a524788ee4d21fe9a4625c35e1756bfe9"></a>
<a id="ahci__types_8h_html_a783053bc2846063e50755f1590e81ba8"></a>
<a id="ahci__types_8h_html_af5e6a53cc7d9619f4ac2ea5bd3256149"></a>
<a id="anet__buf_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructk__timeout__t_html"></a>
<a id="astructnet__buf_html"></a>
<a id="astructnet__buf_html_a1522d81a002804223e25300a6961f527"></a>
<a id="astructnet__buf_html_ac6eef59915e7ce167442fdacbbfb5e56"></a>
<a id="asys_2util_8h_html"></a>
<a id="atoolchain_8h_html"></a>
<a id="autil__macro_8h_html"></a>

```c


/*
 * Copyright (c) 2016 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_BLUETOOTH_BUF_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_BUF_H_


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

#ifdef __cplusplus
extern "C" {
#endif

enum bt_buf_type {
        BT_BUF_TYPE_NONE = 0,
        BT_BUF_CMD = BIT(0),
        BT_BUF_EVT = BIT(1),
        BT_BUF_ACL_OUT = BIT(2),
        BT_BUF_ACL_IN = BIT(3),
        BT_BUF_ISO_OUT = BIT(4),
        BT_BUF_ISO_IN = BIT(5),
};

enum bt_buf_dir {
        BT_BUF_IN,
        BT_BUF_OUT,
};

static inline uint8_t bt_buf_type_to_h4(enum bt_buf_type type)
{
        switch (type) {
        case BT_BUF_CMD:
                return BT_HCI_H4_CMD;
        case BT_BUF_ACL_IN:
        case BT_BUF_ACL_OUT:
                return BT_HCI_H4_ACL;
        case BT_BUF_ISO_IN:
        case BT_BUF_ISO_OUT:
                return BT_HCI_H4_ISO;
        case BT_BUF_EVT:
                return BT_HCI_H4_EVT;
        default:
                __ASSERT_NO_MSG(false);
                return 0;
        }
}

static inline enum bt_buf_type bt_buf_type_from_h4(uint8_t h4_type, enum bt_buf_dir dir)
{
        switch (h4_type) {
        case BT_HCI_H4_CMD:
                return BT_BUF_CMD;
        case BT_HCI_H4_ACL:
                return dir == BT_BUF_OUT ? BT_BUF_ACL_OUT : BT_BUF_ACL_IN;
        case BT_HCI_H4_EVT:
                return BT_BUF_EVT;
        case BT_HCI_H4_ISO:
                return dir == BT_BUF_OUT ? BT_BUF_ISO_OUT : BT_BUF_ISO_IN;
        default:
                return BT_BUF_TYPE_NONE;
        }
}

/* Headroom reserved in buffers, primarily for HCI transport encoding purposes */
#define BT_BUF_RESERVE 1

#define BT_BUF_SIZE(size) (BT_BUF_RESERVE + (size))

#define BT_BUF_ACL_SIZE(size) BT_BUF_SIZE(BT_HCI_ACL_HDR_SIZE + (size))

#define BT_BUF_EVT_SIZE(size) BT_BUF_SIZE(BT_HCI_EVT_HDR_SIZE + (size))

#define BT_BUF_CMD_SIZE(size) BT_BUF_SIZE(BT_HCI_CMD_HDR_SIZE + (size))

#define BT_BUF_ISO_SIZE(size) BT_BUF_SIZE(BT_HCI_ISO_HDR_SIZE + \
                                          BT_HCI_ISO_SDU_TS_HDR_SIZE + \
                                          (size))

#define BT_BUF_ACL_RX_SIZE BT_BUF_ACL_SIZE(CONFIG_BT_BUF_ACL_RX_SIZE)

#define BT_BUF_EVT_RX_SIZE BT_BUF_EVT_SIZE(CONFIG_BT_BUF_EVT_RX_SIZE)

#if defined(CONFIG_BT_ISO)
#define BT_BUF_ISO_RX_SIZE BT_BUF_ISO_SIZE(CONFIG_BT_ISO_RX_MTU)
#define BT_BUF_ISO_RX_COUNT CONFIG_BT_ISO_RX_BUF_COUNT
#else
#define BT_BUF_ISO_RX_SIZE 0
#define BT_BUF_ISO_RX_COUNT 0
#endif /* CONFIG_BT_ISO */

/* see Core Spec v6.0 vol.4 part E 7.4.5 */
#define BT_BUF_ACL_RX_COUNT_MAX 65535

#if defined(CONFIG_BT_CONN) && defined(CONFIG_BT_HCI_HOST)
/* The host needs more ACL buffers than maximum ACL links. This is because of
 * the way we re-assemble ACL packets into L2CAP PDUs.
 *
 * We keep around the first buffer (that comes from the driver) to do
 * re-assembly into, and if all links are re-assembling, there will be no buffer
 * available for the HCI driver to allocate from.
 */
#define BT_BUF_ACL_RX_COUNT_EXTRA CONFIG_BT_BUF_ACL_RX_COUNT_EXTRA
#define BT_BUF_ACL_RX_COUNT       (1 + BT_BUF_ACL_RX_COUNT_EXTRA)
#else
#define BT_BUF_ACL_RX_COUNT_EXTRA 0
#define BT_BUF_ACL_RX_COUNT       0
#endif /* CONFIG_BT_CONN && CONFIG_BT_HCI_HOST */

BUILD_ASSERT(BT_BUF_ACL_RX_COUNT <= BT_BUF_ACL_RX_COUNT_MAX,
             "Maximum number of ACL RX buffer is 65535, reduce CONFIG_BT_BUF_ACL_RX_COUNT_EXTRA");

#define BT_BUF_RX_SIZE (MAX(MAX(BT_BUF_ACL_RX_SIZE, BT_BUF_EVT_RX_SIZE), \
                            BT_BUF_ISO_RX_SIZE))

/* Controller can generate up to CONFIG_BT_BUF_ACL_TX_COUNT number of unique HCI Number of Completed
 * Packets events.
 */
BUILD_ASSERT(CONFIG_BT_BUF_EVT_RX_COUNT > CONFIG_BT_BUF_ACL_TX_COUNT,
             "Increase Event RX buffer count to be greater than ACL TX buffer count");

#define BT_BUF_RX_COUNT (CONFIG_BT_BUF_EVT_RX_COUNT + \
                         MAX(BT_BUF_ACL_RX_COUNT, BT_BUF_ISO_RX_COUNT))

#define BT_BUF_CMD_TX_SIZE BT_BUF_CMD_SIZE(CONFIG_BT_BUF_CMD_TX_SIZE)

struct net_buf *bt_buf_get_rx(enum bt_buf_type type, k_timeout_t timeout);

typedef void (*bt_buf_rx_freed_cb_t)(enum bt_buf_type type_mask);

void bt_buf_rx_freed_cb_set(bt_buf_rx_freed_cb_t cb);

struct net_buf *bt_buf_get_tx(enum bt_buf_type type, k_timeout_t timeout,
                              const void *data, size_t size);

struct net_buf *bt_buf_get_evt(uint8_t evt, bool discardable, k_timeout_t timeout);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_BUF_H_ */
```

## 5.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：© 2016 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 111 行

缓冲区中保留的头部余量（Headroom），主要用于主机控制器接口传输编码（HCI Transport Encoding）。

### 注释 3：原第 143 行

条件编译配置（Configuration）标记：`CONFIG_BT_ISO`。

### 注释 4：原第 145 行

参见《核心规范》（Core Spec）v6.0，第 4 卷 E 部分 7.4.5 节。

### 注释 5：原第 149 行

主机（Host）所需的异步面向连接逻辑传输缓冲区（ACL Buffers）数量，必须多于最大 ACL 链路数。这与将 ACL 数据包重组为逻辑链路控制和适配协议数据单元（L2CAP PDUs）的方式有关。

我们保留来自驱动的第一个缓冲区，作为重组目的缓冲区。如果所有链路都在重组，HCI 驱动就没有可分配的缓冲区。

### 注释 6：原第 161 行

条件编译（Conditional Compilation）：`CONFIG_BT_CONN && CONFIG_BT_HCI_HOST`。

### 注释 7：原第 170 行

控制器（Controller）最多可以生成 `CONFIG_BT_BUF_ACL_TX_COUNT` 个不同的 HCI 已完成数据包数事件（HCI Number of Completed Packets Events）。

### 注释 8：原第 257 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_BUF_H_`。

## 5.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/buf_8h.html)
- [stdint.h](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md)
- [zephyr/bluetooth/hci.h](https://docs.zephyrproject.org/latest/doxygen/html/hci_8h.html)
- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html)
- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [zephyr/sys/util_macro.h](../util_reference/P004_宏工具头文件参考.md)
- [zephyr/sys/clock.h](../timer_reference/P090_系统时钟头文件参考.md)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [bt_buf_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#gafe1539a89ba3389d52d010a071620d7b)
- [BT_BUF_TYPE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ggafe1539a89ba3389d52d010a071620d7ba370190256608b003d85a149fa8039a8d)
- [BT_BUF_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ggafe1539a89ba3389d52d010a071620d7baead9b640992dd72bd90ebd5d1fa3aaf1)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
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
- [BT_HCI_H4_CMD](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a524788ee4d21fe9a4625c35e1756bfe9)
- [BT_HCI_H4_ACL](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a17386452bbd60c85959296b6539232bd)
- [BT_HCI_H4_ISO](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#af5e6a53cc7d9619f4ac2ea5bd3256149)
- [BT_HCI_H4_EVT](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a783053bc2846063e50755f1590e81ba8)
- [bt_buf_type_from_h4](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ga01c7d236ef77e4ba334401c628f582a9)
- [BT_BUF_ACL_RX_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ga1f2226f2fb0a4ea2b215e1c5572ecbf6)
- [BT_BUF_ACL_RX_COUNT_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ga9a196035ab78158867ce301c698c08e1)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [bt_buf_get_rx](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ga4013cce9637f5aa2742d1f1aaa00e7ee)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [bt_buf_rx_freed_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#gaf5c7be1db66cc51c588938fe0b332040)
- [bt_buf_rx_freed_cb_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#gaf946b1bf3706fe74c6d0c9faaaf478f5)
- [bt_buf_get_tx](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ga761a31b7fb19f2325b3a9ac6b1fb1700)
- [data](../network_core_model_reference/P046_net_buf_结构体.md#ac6eef59915e7ce167442fdacbbfb5e56)
- [size](../network_core_model_reference/P046_net_buf_结构体.md#a1522d81a002804223e25300a6961f527)
- [bt_buf_get_evt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ga7b7a19302881dea458fbd2e9e2309b30)
- [clock.h](../timer_reference/P090_系统时钟头文件参考.md)
- [hci.h](https://docs.zephyrproject.org/latest/doxygen/html/hci_8h.html)
- [hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html)
- [net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [net_buf::size](../network_core_model_reference/P046_net_buf_结构体.md#a1522d81a002804223e25300a6961f527)
- [net_buf::data](../network_core_model_reference/P046_net_buf_结构体.md#ac6eef59915e7ce167442fdacbbfb5e56)
- [util.h](../util_reference/P002_通用工具头文件参考.md)
- [toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [util_macro.h](../util_reference/P004_宏工具头文件参考.md)

---

[上一章](P004_brg_cfg.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P006_coap_client.h_源码浏览.md)
