---
id: learning.zephyr-docs.api-source-timing-sensor-reference.page-2
title: cmux.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/cmux_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_cmux.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/cmux_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/cmux_8h.html)。

## 2.1\_原始可见代码（Source Code）

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
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="foldopen00049"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="foldopen00060"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
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
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
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
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
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
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00236"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="foldopen00247"></a>
<a id="l00247"></a>
<a id="l00249"></a>
<a id="l00251"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="aatomic_8h_html"></a>
<a id="agroup__modem__cmux_html_ga362cd4b2dff122e3bbaee02b378dd226"></a>
<a id="agroup__modem__cmux_html_ga482171f67db206780d0b8a2cf5b32a93"></a>
<a id="agroup__modem__cmux_html_ga988c8efbebf63871730918d862b7c490"></a>
<a id="agroup__modem__cmux_html_ga998b334620c9970ebbb0bcf620ea5923"></a>
<a id="agroup__modem__cmux_html_ga9fa4a1cd9cf1e1c253e621c650a611d0"></a>
<a id="agroup__modem__cmux_html_gab60ea756d37bd9ed59f07c6380952d36"></a>
<a id="agroup__modem__cmux_html_gab85f5c71a3cf131ff97aa47749197cb3"></a>
<a id="agroup__modem__cmux_html_gabfd8e728eb8940b4093ae132b7add7d7"></a>
<a id="agroup__modem__cmux_html_gad72973ad82504ae64d184ce11572ab88"></a>
<a id="agroup__modem__cmux_html_gadc7c6ff92b7ac52717151bd6bf1efdff"></a>
<a id="agroup__modem__cmux_html_ggab60ea756d37bd9ed59f07c6380952d36a095af6ed667b014e4beb4c13c34c8a21"></a>
<a id="agroup__modem__cmux_html_ggab60ea756d37bd9ed59f07c6380952d36a8d37518bf5ba31237e59a413f36be4b2"></a>
<a id="agroup__single-linked-list__apis_html_ga44658c336b634c03938a251cdc8134f8"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="amodem_2stats_8h_html"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="apipe_8h_html"></a>
<a id="aring__buffer_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructk__timeout__t_html"></a>
<a id="astructmodem__cmux__config_html"></a>
<a id="astructmodem__cmux__config_html_a11333197710a1fc3c6c1d1ac5f706b09"></a>
<a id="astructmodem__cmux__config_html_a1f955b28efb6f3e1a2a6e6eac66d687e"></a>
<a id="astructmodem__cmux__config_html_a2935694a75a95da8571b1c520a9800c8"></a>
<a id="astructmodem__cmux__config_html_a2cba948c704f02429022d360326b9838"></a>
<a id="astructmodem__cmux__config_html_a2fcf4ba7f088701ec6c5b750c8af3a89"></a>
<a id="astructmodem__cmux__config_html_a6714790f733ba7e4431353b6cdbbe3ee"></a>
<a id="astructmodem__cmux__config_html_a6920bf8f7c52522e8b76ba09051887c5"></a>
<a id="astructmodem__cmux__config_html_aade573d6cd09b2b2ca0efbefc25f0759"></a>
<a id="astructmodem__cmux__config_html_acf451afdc3033fffac12d546f7e7c6c0"></a>
<a id="astructmodem__cmux__config_html_ae028b4dde63311a810c67686dc662154"></a>
<a id="astructmodem__cmux__dlci__config_html"></a>
<a id="astructmodem__cmux__dlci__config_html_ad0b1fe93bbee6343c8446da5a0ad88c9"></a>
<a id="astructmodem__cmux__dlci__config_html_ad3d6c1e0adce243aa536e52e5e4c4374"></a>
<a id="astructmodem__cmux__dlci__config_html_af7715440c78d87466f91464000db1fef"></a>
<a id="asys_2util_8h_html"></a>

```c
/*
 * Copyright (c) 2022 Trackunit Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

/*
 * This library uses CMUX to create multiple data channels, called DLCIs, on a single serial bus.
 * Each DLCI has an address from 1 to 63. DLCI address 0 is reserved for control commands.
 *
 * Design overview:
 *
 *     DLCI1 <-----------+                              +-------> DLCI1
 *                       v                              v
 *     DLCI2 <---> CMUX instance <--> Serial bus <--> Client <--> DLCI2
 *                       ^                              ^
 *     DLCI3 <-----------+                              +-------> DLCI3
 *
 * Writing to and from the CMUX instances is done using the modem_pipe API.
 */

#include <zephyr/kernel.h>
#include <zephyr/types.h>
#include <zephyr/sys/ring_buffer.h>
#include <zephyr/sys/atomic.h>
#include <zephyr/sys/util.h>

#include <zephyr/modem/pipe.h>
#include <zephyr/modem/stats.h>

#ifndef ZEPHYR_INCLUDE_MODEM_CMUX_H_
#define ZEPHYR_INCLUDE_MODEM_CMUX_H_

#ifdef __cplusplus
extern "C" {
#endif


struct modem_cmux;

enum modem_cmux_event {
        MODEM_CMUX_EVENT_CONNECTED = 0,
        MODEM_CMUX_EVENT_DISCONNECTED,
};

typedef void (*modem_cmux_callback)(struct modem_cmux *cmux, enum modem_cmux_event event,
                                    void *user_data);

struct modem_cmux_config {
        modem_cmux_callback callback;
        void *user_data;
        uint8_t *receive_buf;
        uint16_t receive_buf_size;
        uint8_t *transmit_buf;
        uint16_t transmit_buf_size;
        bool enable_runtime_power_management;
        bool close_pipe_on_power_save;
        bool no_powersave_handshake;
        k_timeout_t idle_timeout;
};


#if CONFIG_MODEM_CMUX_MTU > 127
#define MODEM_CMUX_HEADER_SIZE                  7
#else
#define MODEM_CMUX_HEADER_SIZE                  6
#endif

/* Minimum required size for CMUX RX buffers */
#define MODEM_CMUX_RX_BUFFER_SIZE_MIN           126

/* Total size of the CMUX work buffers from the MTU */
#define MODEM_CMUX_WORK_BUFFER_FROM_MTU (CONFIG_MODEM_CMUX_MTU + MODEM_CMUX_HEADER_SIZE + \
                                         CONFIG_MODEM_CMUX_WORK_BUFFER_SIZE_EXTRA)

/* Enforce the minimum size required by CMUX */
#define MODEM_CMUX_WORK_BUFFER_SIZE MAX(MODEM_CMUX_WORK_BUFFER_FROM_MTU, \
                                        MODEM_CMUX_RX_BUFFER_SIZE_MIN)

enum modem_cmux_state {
        MODEM_CMUX_STATE_DISCONNECTED = 0,
        MODEM_CMUX_STATE_CONNECTING,
        MODEM_CMUX_STATE_CONNECTED,
        MODEM_CMUX_STATE_ENTER_POWERSAVE,
        MODEM_CMUX_STATE_POWERSAVE,
        MODEM_CMUX_STATE_CONFIRM_POWERSAVE,
        MODEM_CMUX_STATE_WAKEUP,
        MODEM_CMUX_STATE_DISCONNECTING,
};

enum modem_cmux_receive_state {
        MODEM_CMUX_RECEIVE_STATE_SOF = 0,
        MODEM_CMUX_RECEIVE_STATE_RESYNC,
        MODEM_CMUX_RECEIVE_STATE_ADDRESS,
        MODEM_CMUX_RECEIVE_STATE_ADDRESS_CONT,
        MODEM_CMUX_RECEIVE_STATE_CONTROL,
        MODEM_CMUX_RECEIVE_STATE_LENGTH,
        MODEM_CMUX_RECEIVE_STATE_LENGTH_CONT,
        MODEM_CMUX_RECEIVE_STATE_DATA,
        MODEM_CMUX_RECEIVE_STATE_DATA_CONT,
        MODEM_CMUX_RECEIVE_STATE_FCS,
        MODEM_CMUX_RECEIVE_STATE_EOF,
};

enum modem_cmux_dlci_state {
        MODEM_CMUX_DLCI_STATE_CLOSED,
        MODEM_CMUX_DLCI_STATE_OPENING,
        MODEM_CMUX_DLCI_STATE_OPEN,
        MODEM_CMUX_DLCI_STATE_CLOSING,
};

struct modem_cmux_dlci {
        sys_snode_t node;

        /* Pipe */
        struct modem_pipe pipe;

        /* Context */
        uint16_t dlci_address;
        struct modem_cmux *cmux;

        /* Receive buffer */
        struct ring_buf receive_rb;
        struct k_mutex receive_rb_lock;

        /* Work */
        struct k_work_delayable open_work;
        struct k_work_delayable close_work;

        /* State */
        enum modem_cmux_dlci_state state;

        /* Statistics */
#if CONFIG_MODEM_STATS
        struct modem_stats_buffer receive_buf_stats;
#endif
        /* Flow control */
        bool flow_control : 1;
        bool rx_full : 1;
        bool msc_sent : 1;
};

struct modem_cmux_frame {
        uint8_t dlci_address;
        bool cr;
        bool pf;
        uint8_t type;
        const uint8_t *data;
        const uint8_t *tx_extra;
        uint16_t data_len;
        uint16_t tx_extra_len;
};

struct modem_cmux_work {
        struct k_work_delayable dwork;
        struct modem_cmux *cmux;
};

struct modem_cmux {
        /* Bus pipe */
        struct modem_pipe *pipe;

        /* DLCI channel contexts */
        sys_slist_t dlcis;

        /* State */
        enum modem_cmux_state state;
        uint8_t retry_count;
        bool flow_control_on : 1;
        bool initiator : 1;

        /* Work lock */
        bool attached : 1;
        struct k_spinlock work_lock;

        /* Receive state*/
        enum modem_cmux_receive_state receive_state;
        int receive_buf_len;

        /* Transmit buffer */
        struct ring_buf transmit_rb;
        struct k_mutex transmit_rb_lock;

        /* Received frame */
        struct modem_cmux_frame frame;
        int frame_start;
        uint16_t frame_header_len;

        /* Work */
        struct k_work_delayable receive_work;
        struct k_work_delayable transmit_work;
        struct k_work_delayable connect_work;
        struct k_work_delayable disconnect_work;
        struct k_work_delayable runtime_pm_work;

        /* Synchronize actions */
        struct k_event event;
        k_timepoint_t t3_timepoint;
        k_timepoint_t idle_timepoint;

        /* Statistics */
#if CONFIG_MODEM_STATS
        struct modem_stats_buffer receive_buf_stats;
        struct modem_stats_buffer transmit_buf_stats;
#endif
        struct modem_cmux_config config;
};


void modem_cmux_init(struct modem_cmux *cmux, const struct modem_cmux_config *config);

struct modem_cmux_dlci_config {
        uint8_t dlci_address;
        uint8_t *receive_buf;
        uint16_t receive_buf_size;
};

struct modem_pipe *modem_cmux_dlci_init(struct modem_cmux *cmux, struct modem_cmux_dlci *dlci,
                                        const struct modem_cmux_dlci_config *config);

int modem_cmux_attach(struct modem_cmux *cmux, struct modem_pipe *pipe);

int modem_cmux_connect(struct modem_cmux *cmux);

int modem_cmux_connect_async(struct modem_cmux *cmux);

int modem_cmux_disconnect(struct modem_cmux *cmux);

int modem_cmux_disconnect_async(struct modem_cmux *cmux);

void modem_cmux_release(struct modem_cmux *cmux);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_MODEM_CMUX_H_ */
```

## 2.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Trackunit Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 7 行

本库使用串口多路复用（CMUX），在一条串行总线上创建多个数据通道，称为数据链路连接标识符（DLCI）通道。每个 DLCI 的地址范围为 1–63，地址 0 保留给控制命令。

设计概览（Design overview）见下方保留的原始示意图。对 CMUX 实例的读写通过 `modem_pipe` API 完成。

```text
    DLCI1 <-----------+                              +-------> DLCI1
                      v                              v
    DLCI2 <---> CMUX instance <--> Serial bus <--> Client <--> DLCI2
                      ^                              ^
    DLCI3 <-----------+                              +-------> DLCI3
```

### 注释 3：原第 93 行

CMUX 接收（RX）缓冲区所需的最小大小。

### 注释 4：原第 96 行

根据最大传输单元（MTU）计算的 CMUX 工作缓冲区总大小。

### 注释 5：原第 100 行

强制满足 CMUX 所需的最小大小。

### 注释 6：原第 139 行

管道（Pipe）

### 注释 7：原第 142 行

上下文。

### 注释 8：原第 146 行

接收缓冲区。

### 注释 9：原第 150 行

工作项（work）。

### 注释 10：原第 154 行

状态（State）。

### 注释 11：原第 157 行

统计信息（Statistics）。

### 注释 12：原第 161 行

流量控制（flow control）。

### 注释 13：原第 184 行

总线管道（bus pipe）。

### 注释 14：原第 187 行

DLCI 通道上下文（channel contexts）。

### 注释 15：原第 190 行

状态（State）。

### 注释 16：原第 196 行

工作锁（work lock）。

### 注释 17：原第 200 行

接收状态（receive state）。

### 注释 18：原第 204 行

发送缓冲区。

### 注释 19：原第 208 行

已接收的帧（received frame）。

### 注释 20：原第 213 行

工作项（work）。

### 注释 21：原第 220 行

同步各项操作（synchronize actions）。

### 注释 22：原第 225 行

统计信息（Statistics）。

### 注释 23：原第 342 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MODEM_CMUX_H_`。

## 2.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/cmux_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [zephyr/sys/ring_buffer.h](../ringbuffer_reference/P003_环形缓冲区头文件参考.md)
- [zephyr/sys/atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [zephyr/modem/pipe.h](https://docs.zephyrproject.org/latest/doxygen/html/pipe_8h.html)
- [zephyr/modem/stats.h](https://docs.zephyrproject.org/latest/doxygen/html/modem_2stats_8h.html)
- [modem_cmux_event](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__cmux.html#gab60ea756d37bd9ed59f07c6380952d36)
- [MODEM_CMUX_EVENT_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__cmux.html#ggab60ea756d37bd9ed59f07c6380952d36a8d37518bf5ba31237e59a413f36be4b2)
- [MODEM_CMUX_EVENT_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__cmux.html#ggab60ea756d37bd9ed59f07c6380952d36a095af6ed667b014e4beb4c13c34c8a21)
- [modem_cmux_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__cmux.html#ga998b334620c9970ebbb0bcf620ea5923)
- [modem_cmux_config](../modem_wireless_model_reference/P058_modem_cmux_config_结构体.md)
- [callback](../modem_wireless_model_reference/P058_modem_cmux_config_结构体.md#a2cba948c704f02429022d360326b9838)
- [user_data](../modem_wireless_model_reference/P058_modem_cmux_config_结构体.md#a6714790f733ba7e4431353b6cdbbe3ee)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [receive_buf](../modem_wireless_model_reference/P058_modem_cmux_config_结构体.md#a2935694a75a95da8571b1c520a9800c8)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [receive_buf_size](../modem_wireless_model_reference/P058_modem_cmux_config_结构体.md#a2fcf4ba7f088701ec6c5b750c8af3a89)
- [transmit_buf](../modem_wireless_model_reference/P058_modem_cmux_config_结构体.md#a6920bf8f7c52522e8b76ba09051887c5)
- [transmit_buf_size](../modem_wireless_model_reference/P058_modem_cmux_config_结构体.md#ae028b4dde63311a810c67686dc662154)
- [enable_runtime_power_management](../modem_wireless_model_reference/P058_modem_cmux_config_结构体.md#a1f955b28efb6f3e1a2a6e6eac66d687e)
- [close_pipe_on_power_save](../modem_wireless_model_reference/P058_modem_cmux_config_结构体.md#acf451afdc3033fffac12d546f7e7c6c0)
- [no_powersave_handshake](../modem_wireless_model_reference/P058_modem_cmux_config_结构体.md#a11333197710a1fc3c6c1d1ac5f706b09)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [idle_timeout](../modem_wireless_model_reference/P058_modem_cmux_config_结构体.md#aade573d6cd09b2b2ca0efbefc25f0759)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)
- [modem_cmux_init](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__cmux.html#gad72973ad82504ae64d184ce11572ab88)
- [modem_cmux_dlci_config](../modem_wireless_model_reference/P059_modem_cmux_dlci_config_结构体.md)
- [dlci_address](../modem_wireless_model_reference/P059_modem_cmux_dlci_config_结构体.md#ad0b1fe93bbee6343c8446da5a0ad88c9)
- [receive_buf](../modem_wireless_model_reference/P059_modem_cmux_dlci_config_结构体.md#ad3d6c1e0adce243aa536e52e5e4c4374)
- [receive_buf_size](../modem_wireless_model_reference/P059_modem_cmux_dlci_config_结构体.md#af7715440c78d87466f91464000db1fef)
- [modem_cmux_dlci_init](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__cmux.html#gabfd8e728eb8940b4093ae132b7add7d7)
- [modem_cmux_attach](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__cmux.html#gab85f5c71a3cf131ff97aa47749197cb3)
- [modem_cmux_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__cmux.html#ga362cd4b2dff122e3bbaee02b378dd226)
- [modem_cmux_connect_async](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__cmux.html#ga9fa4a1cd9cf1e1c253e621c650a611d0)
- [modem_cmux_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__cmux.html#ga482171f67db206780d0b8a2cf5b32a93)
- [modem_cmux_disconnect_async](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__cmux.html#ga988c8efbebf63871730918d862b7c490)
- [modem_cmux_release](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__cmux.html#gadc7c6ff92b7ac52717151bd6bf1efdff)
- [atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [stats.h](https://docs.zephyrproject.org/latest/doxygen/html/modem_2stats_8h.html)
- [pipe.h](https://docs.zephyrproject.org/latest/doxygen/html/pipe_8h.html)
- [ring_buffer.h](../ringbuffer_reference/P003_环形缓冲区头文件参考.md)
- [modem_cmux_config::no_powersave_handshake](../modem_wireless_model_reference/P058_modem_cmux_config_结构体.md#a11333197710a1fc3c6c1d1ac5f706b09)
- [modem_cmux_config::enable_runtime_power_management](../modem_wireless_model_reference/P058_modem_cmux_config_结构体.md#a1f955b28efb6f3e1a2a6e6eac66d687e)
- [modem_cmux_config::receive_buf](../modem_wireless_model_reference/P058_modem_cmux_config_结构体.md#a2935694a75a95da8571b1c520a9800c8)
- [modem_cmux_config::callback](../modem_wireless_model_reference/P058_modem_cmux_config_结构体.md#a2cba948c704f02429022d360326b9838)
- [modem_cmux_config::receive_buf_size](../modem_wireless_model_reference/P058_modem_cmux_config_结构体.md#a2fcf4ba7f088701ec6c5b750c8af3a89)
- [modem_cmux_config::user_data](../modem_wireless_model_reference/P058_modem_cmux_config_结构体.md#a6714790f733ba7e4431353b6cdbbe3ee)
- [modem_cmux_config::transmit_buf](../modem_wireless_model_reference/P058_modem_cmux_config_结构体.md#a6920bf8f7c52522e8b76ba09051887c5)
- [modem_cmux_config::idle_timeout](../modem_wireless_model_reference/P058_modem_cmux_config_结构体.md#aade573d6cd09b2b2ca0efbefc25f0759)
- [modem_cmux_config::close_pipe_on_power_save](../modem_wireless_model_reference/P058_modem_cmux_config_结构体.md#acf451afdc3033fffac12d546f7e7c6c0)
- [modem_cmux_config::transmit_buf_size](../modem_wireless_model_reference/P058_modem_cmux_config_结构体.md#ae028b4dde63311a810c67686dc662154)
- [modem_cmux_dlci_config::dlci_address](../modem_wireless_model_reference/P059_modem_cmux_dlci_config_结构体.md#ad0b1fe93bbee6343c8446da5a0ad88c9)
- [modem_cmux_dlci_config::receive_buf](../modem_wireless_model_reference/P059_modem_cmux_dlci_config_结构体.md#ad3d6c1e0adce243aa536e52e5e4c4374)
- [modem_cmux_dlci_config::receive_buf_size](../modem_wireless_model_reference/P059_modem_cmux_dlci_config_结构体.md#af7715440c78d87466f91464000db1fef)
- [util.h](../util_reference/P002_通用工具头文件参考.md)

---

[上一章](P001_adi_max32_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P003_cs.h_源码浏览.md)
