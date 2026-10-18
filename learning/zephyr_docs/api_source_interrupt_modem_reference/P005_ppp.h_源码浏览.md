---
id: learning.zephyr-docs.api-source-interrupt-modem-reference.page-5
title: ppp.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/modem_2ppp_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_ppp.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ppp_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ppp_8h.html)。

## 5.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
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
<a id="l00024"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
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
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
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
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00126"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00153"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00164"></a>
<a id="foldopen00181"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="foldopen00207"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="foldopen00215"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="aatomic_8h_html"></a>
<a id="agroup__atomic__apis_html_ga124f07c3a788e53c3a40e4e1c06d8af8"></a>
<a id="agroup__modem__ppp_html_gad3ce02dd0a6cf7067c5ca0341f807f88"></a>
<a id="agroup__modem__ppp_html_gaebb69341b2b88338b2cfccaa1c0cba0b"></a>
<a id="agroup__modem__ppp_html_gaf2177b83100647ed0894cac7fa435cb3"></a>
<a id="agroup__modem__ppp_html_gafdd04a06c32e9ab70755d4f2e68deaad"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="amodem_2stats_8h_html"></a>
<a id="anet_2ppp_8h_html"></a>
<a id="anet__if_8h_html"></a>
<a id="anet__pkt_8h_html"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="apipe_8h_html"></a>
<a id="aring__buffer_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructnet__if_html"></a>

```c
/*
 * Copyright (c) 2022 Trackunit Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include <zephyr/kernel.h>
#include <zephyr/types.h>
#include <zephyr/net/net_if.h>
#include <zephyr/net/net_pkt.h>
#include <zephyr/net/ppp.h>
#include <zephyr/sys/ring_buffer.h>
#include <zephyr/sys/atomic.h>

#include <zephyr/modem/pipe.h>
#include <zephyr/modem/stats.h>

#ifndef ZEPHYR_INCLUDE_MODEM_PPP_H_
#define ZEPHYR_INCLUDE_MODEM_PPP_H_

#ifdef __cplusplus
extern "C" {
#endif


typedef void (*modem_ppp_init_iface)(struct net_if *iface);


enum modem_ppp_state {
        /* Pipe is attached */
        MODEM_PPP_STATE_ATTACHED_BIT = 0,
        /* Link is dead */
        MODEM_PPP_STATE_DEAD_BIT,
};

enum modem_ppp_receive_state {
        /* Searching for start of frame and header */
        MODEM_PPP_RECEIVE_STATE_HDR_SOF = 0,
        MODEM_PPP_RECEIVE_STATE_HDR_FF,
        MODEM_PPP_RECEIVE_STATE_HDR_FF_UNESCAPE,
        MODEM_PPP_RECEIVE_STATE_HDR_CTRL_UNESCAPE,
        MODEM_PPP_RECEIVE_STATE_HDR_CTRL,
        /* Writing bytes to network packet */
        MODEM_PPP_RECEIVE_STATE_WRITING,
        /* Unescaping next byte before writing to network packet */
        MODEM_PPP_RECEIVE_STATE_UNESCAPING,
        /* Receiving an unsolicited "NO CARRIER" event */
        MODEM_PPP_RECEIVE_STATE_UNSOLICITED_NO_CARRIER,
};

enum modem_ppp_transmit_state {
        MODEM_PPP_TRANSMIT_STATE_IDLE = 0,
        MODEM_PPP_TRANSMIT_STATE_SOF,
        MODEM_PPP_TRANSMIT_STATE_PROTOCOL,
        MODEM_PPP_TRANSMIT_STATE_DATA,
        MODEM_PPP_TRANSMIT_STATE_EOF,
};

struct modem_ppp {
        /* Network interface instance is bound to */
        struct net_if *iface;

        /* Hook for PPP L2 network interface initialization */
        modem_ppp_init_iface init_iface;

        atomic_t state;

        /* Buffers used for processing partial frames */
        uint8_t *receive_buf;
        uint8_t *transmit_buf;
        uint16_t buf_size;

        /* Wrapped PPP frames are sent and received through this pipe */
        struct modem_pipe *pipe;

        /* Receive PPP frame state */
        enum modem_ppp_receive_state receive_state;
        uint8_t receive_offset;

        /* Allocated network packet being created */
        struct net_pkt *rx_pkt;

        /* Packet being sent */
        enum modem_ppp_transmit_state transmit_state;
        struct net_pkt *tx_pkt;
        uint16_t tx_pkt_fcs;

        /* Ring buffer used for transmitting partial PPP frame */
        struct ring_buf transmit_rb;

        struct k_fifo tx_pkt_fifo;

        /* Work */
        struct k_work send_work;
        struct k_work process_work;

#if defined(CONFIG_NET_STATISTICS_PPP)
        struct net_stats_ppp stats;
#endif

#if CONFIG_MODEM_STATS
        struct modem_stats_buffer receive_buf_stats;
        struct modem_stats_buffer transmit_buf_stats;
#endif
};

struct modem_ppp_config {
        const struct device *dev;
};


int modem_ppp_attach(struct modem_ppp *ppp, struct modem_pipe *pipe);

struct net_if *modem_ppp_get_iface(struct modem_ppp *ppp);

void modem_ppp_release(struct modem_ppp *ppp);


int modem_ppp_init_internal(const struct device *dev);


#define MODEM_DEV_PPP_DEFINE(_dev, _name, _init_iface, _mtu, _buf_size)                            \
        extern const struct ppp_api modem_ppp_ppp_api;                                             \
                                                                                                   \
        static uint8_t _CONCAT(_name, _receive_buf)[_buf_size];                                    \
        static uint8_t _CONCAT(_name, _transmit_buf)[_buf_size];                                   \
                                                                                                   \
        static struct modem_ppp _name = {                                                          \
                .init_iface = _init_iface,                                                         \
                .receive_buf = _CONCAT(_name, _receive_buf),                                       \
                .transmit_buf = _CONCAT(_name, _transmit_buf),                                     \
                .buf_size = _buf_size,                                                             \
        };                                                                                         \
        static const struct modem_ppp_config _CONCAT(_name, _config) = {                           \
                .dev = _dev,                                                                       \
        };                                                                                         \
                                                                                                   \
        NET_DEVICE_INIT(_CONCAT(ppp_net_dev_, _name), "modem_ppp_" #_name,                         \
                        modem_ppp_init_internal, NULL, &_name, &_CONCAT(_name, _config),           \
                        CONFIG_KERNEL_INIT_PRIORITY_DEFAULT,                                       \
                        &modem_ppp_ppp_api, PPP_L2, NET_L2_GET_CTX_TYPE(PPP_L2), _mtu)

#define MODEM_DT_INST_PPP_DEFINE(inst, _name, _init_iface, _mtu, _buf_size)                        \
        MODEM_DEV_PPP_DEFINE(DEVICE_DT_INST_GET(inst), _name, _init_iface, _mtu, _buf_size)

#define MODEM_PPP_DEFINE(_name, _init_iface, _mtu, _buf_size)                                      \
        MODEM_DEV_PPP_DEFINE(NULL, _name, _init_iface, _mtu, _buf_size)


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_MODEM_PPP_H_ */
```

## 5.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Trackunit Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 42 行

管道（pipe）已附接。

### 注释 3：原第 44 行

链路（link）已失效。

### 注释 4：原第 49 行

正在搜索帧起点和首部（header）。

### 注释 5：原第 55 行

正在向网络数据包写入字节。

### 注释 6：原第 57 行

在向网络数据包写入之前，对下一个字节进行反转义（unescaping）。

### 注释 7：原第 59 行

收到非请求（unsolicited）的 `NO CARRIER` 事件。

### 注释 8：原第 72 行

本实例绑定到的网络接口（network interface）。

### 注释 9：原第 75 行

用于点对点协议第二层（PPP L2）网络接口初始化的钩子（hook）。

### 注释 10：原第 80 行

用于处理不完整帧（partial frames）的缓冲区。

### 注释 11：原第 85 行

封装的 PPP 帧通过此管道发送和接收。

### 注释 12：原第 88 行

接收 PPP 帧的状态（receive state）。

### 注释 13：原第 92 行

正在构造的已分配网络数据包。

### 注释 14：原第 95 行

正在发送的数据包。

### 注释 15：原第 100 行

用于发送不完整 PPP 帧的环形缓冲区（ring buffer）。

### 注释 16：原第 105 行

工作项（work）。

### 注释 17：原第 226 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MODEM_PPP_H_`。

## 5.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ppp_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [zephyr/net/net_pkt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__pkt_8h.html)
- [zephyr/net/ppp.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2ppp_8h.html)
- [zephyr/sys/ring_buffer.h](../ringbuffer_reference/P003_环形缓冲区头文件参考.md)
- [zephyr/sys/atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [zephyr/modem/pipe.h](https://docs.zephyrproject.org/latest/doxygen/html/pipe_8h.html)
- [zephyr/modem/stats.h](../api_file_management_reference/P035_zephyr__modem__stats.h_文件参考.md)
- [modem_ppp_init_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ppp.html#gafdd04a06c32e9ab70755d4f2e68deaad)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [modem_ppp_attach](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ppp.html#gad3ce02dd0a6cf7067c5ca0341f807f88)
- [modem_ppp_get_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ppp.html#gaebb69341b2b88338b2cfccaa1c0cba0b)
- [modem_ppp_release](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ppp.html#gaf2177b83100647ed0894cac7fa435cb3)
- [device](../device_reference/P002_设备对象结构.md)
- [atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [stats.h](../api_file_management_reference/P035_zephyr__modem__stats.h_文件参考.md)
- [ppp.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2ppp_8h.html)
- [net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [net_pkt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__pkt_8h.html)
- [pipe.h](https://docs.zephyrproject.org/latest/doxygen/html/pipe_8h.html)
- [ring_buffer.h](../ringbuffer_reference/P003_环形缓冲区头文件参考.md)

---

[上一章](P004_ieee802154_pkt.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P006_modem_cellular.h_源码浏览.md)
