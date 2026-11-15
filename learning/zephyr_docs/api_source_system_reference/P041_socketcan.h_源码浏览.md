---
id: learning.zephyr-docs.api-source-system-reference.page-41
title: socketcan.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/socketcan_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第41章\_socketcan.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/socketcan_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/socketcan_8h.html)。

## 41.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00076"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="foldopen00103"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00107"></a>
<a id="l00109"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00114"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="foldopen00124"></a>
<a id="l00124"></a>
<a id="l00126"></a>
<a id="l00128"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00134"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="agroup__socket__can_html_ga35a7941726d1e22defd8c3098391ca8e"></a>
<a id="agroup__socket__can_html_ga3ec3e39a63684e78a52cf9160c82c257"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="anet__if_8h_html"></a>
<a id="anet__ip_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructsocketcan__filter_html"></a>
<a id="astructsocketcan__filter_html_a841857f05f1e1a887be50d8e507a03f9"></a>
<a id="astructsocketcan__filter_html_a84abbc2f8a18bfe2d53cacf582f9fa10"></a>
<a id="astructsocketcan__filter_html_a9217950edb190dc70783d9b87676ae47"></a>
<a id="astructsocketcan__frame_html"></a>
<a id="astructsocketcan__frame_html_a43511a491c9b8cf63b4ff592eb77a6e6"></a>
<a id="astructsocketcan__frame_html_a4ab22ff419e3c7397c64a1309cbdb623"></a>
<a id="astructsocketcan__frame_html_aa21e8007363ab0183c7b9d6c59cb4731"></a>
<a id="astructsocketcan__frame_html_af9ddb322cdc3d886182cce65f673177d"></a>

```c


/*
 * Copyright (c) 2019 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_SOCKETCAN_H_
#define ZEPHYR_INCLUDE_NET_SOCKETCAN_H_

#include <zephyr/types.h>
#include <zephyr/net/net_ip.h>
#include <zephyr/net/net_if.h>

#ifdef __cplusplus
extern "C" {
#endif


#define NET_CAN_RAW 1


/* SocketCAN options */
#define NET_SOL_CAN_BASE 100
#define NET_SOL_CAN_RAW (NET_SOL_CAN_BASE + NET_CAN_RAW)

enum {
        NET_CAN_RAW_FILTER = 1,
};


/* SocketCAN MTU size compatible with Linux */
#ifdef CONFIG_CAN_FD_MODE
#define SOCKETCAN_MAX_DLEN 64U
#define CANFD_MTU (sizeof(struct socketcan_frame))
#define CAN_MTU (CANFD_MTU - 56U)
#else /* CONFIG_CAN_FD_MODE */
#define SOCKETCAN_MAX_DLEN 8U
#define CAN_MTU (sizeof(struct socketcan_frame))
#endif /* !CONFIG_CAN_FD_MODE */

/* CAN FD specific flags from Linux Kernel (include/uapi/linux/can.h) */
#define CANFD_BRS 0x01
#define CANFD_ESI 0x02
#define CANFD_FDF 0x04


typedef uint32_t socketcan_id_t;

struct socketcan_frame {
        socketcan_id_t can_id;
        uint8_t len;
        uint8_t flags;
        uint8_t res0;  /* reserved/padding. */
        uint8_t res1;  /* reserved/padding. */

        uint8_t data[SOCKETCAN_MAX_DLEN];
};

struct socketcan_filter {
        socketcan_id_t can_id;
        socketcan_id_t can_mask;
        uint8_t flags;
};



#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_SOCKETCAN_H_ */
```

## 41.2\_可见注释译文（Comments）

### 注释 1：原第 7 行

版权（Copyright）：© 2019 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 38 行

套接字 CAN 选项（SocketCAN Options）。

### 注释 3：原第 48 行

与 Linux 兼容的 SocketCAN 最大传输单元大小（MTU Size）。

### 注释 4：原第 56 行

条件编译配置（Configuration）标记：`CONFIG_CAN_FD_MODE`。

### 注释 5：原第 61 行

条件编译（Conditional Compilation）：`!CONFIG_CAN_FD_MODE`。

### 注释 6：原第 63 行

来自 Linux 内核 `include/uapi/linux/can.h` 的 CAN 灵活数据速率专用标志（CAN FD Specific Flags）。

### 注释 7：原第 111 行

保留／填充（Reserved / Padding）。

### 注释 8：原第 112 行

保留／填充（Reserved / Padding）。

### 注释 9：原第 143 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_SOCKETCAN_H_`。

## 41.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/socketcan_8h.html)
- [zephyr/types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [socketcan_id_t](https://docs.zephyrproject.org/latest/doxygen/html/group__socket__can.html#ga35a7941726d1e22defd8c3098391ca8e)
- [socketcan_frame](../network_service_model_reference/P057_socketcan_frame_结构体.md)
- [can_id](../network_service_model_reference/P057_socketcan_frame_结构体.md#a43511a491c9b8cf63b4ff592eb77a6e6)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [len](../network_service_model_reference/P057_socketcan_frame_结构体.md#aa21e8007363ab0183c7b9d6c59cb4731)
- [flags](../network_service_model_reference/P057_socketcan_frame_结构体.md#af9ddb322cdc3d886182cce65f673177d)
- [data](../network_service_model_reference/P057_socketcan_frame_结构体.md#a4ab22ff419e3c7397c64a1309cbdb623)
- [SOCKETCAN_MAX_DLEN](https://docs.zephyrproject.org/latest/doxygen/html/group__socket__can.html#ga3ec3e39a63684e78a52cf9160c82c257)
- [socketcan_filter](../network_service_model_reference/P056_socketcan_filter_结构体.md)
- [can_id](../network_service_model_reference/P056_socketcan_filter_结构体.md#a9217950edb190dc70783d9b87676ae47)
- [can_mask](../network_service_model_reference/P056_socketcan_filter_结构体.md#a841857f05f1e1a887be50d8e507a03f9)
- [flags](../network_service_model_reference/P056_socketcan_filter_结构体.md#a84abbc2f8a18bfe2d53cacf582f9fa10)
- [types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [socketcan_filter::can_mask](../network_service_model_reference/P056_socketcan_filter_结构体.md#a841857f05f1e1a887be50d8e507a03f9)
- [socketcan_filter::flags](../network_service_model_reference/P056_socketcan_filter_结构体.md#a84abbc2f8a18bfe2d53cacf582f9fa10)
- [socketcan_filter::can_id](../network_service_model_reference/P056_socketcan_filter_结构体.md#a9217950edb190dc70783d9b87676ae47)
- [socketcan_frame::can_id](../network_service_model_reference/P057_socketcan_frame_结构体.md#a43511a491c9b8cf63b4ff592eb77a6e6)
- [socketcan_frame::data](../network_service_model_reference/P057_socketcan_frame_结构体.md#a4ab22ff419e3c7397c64a1309cbdb623)
- [socketcan_frame::len](../network_service_model_reference/P057_socketcan_frame_结构体.md#aa21e8007363ab0183c7b9d6c59cb4731)
- [socketcan_frame::flags](../network_service_model_reference/P057_socketcan_frame_结构体.md#af9ddb322cdc3d886182cce65f673177d)

---

[上一章](P040_sip_svc_agilex_smc.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P042_stdio.h_源码浏览.md)
