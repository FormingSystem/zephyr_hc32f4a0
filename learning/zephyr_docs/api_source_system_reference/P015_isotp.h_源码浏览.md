---
id: learning.zephyr-docs.api-source-system-reference.page-15
title: isotp.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/isotp_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_isotp.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/isotp_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/isotp_8h.html)。

## 15.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
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
<a id="l00039"></a>
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
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00099"></a>
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
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00145"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00165"></a>
<a id="foldopen00171"></a>
<a id="l00171"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00183"></a>
<a id="l00194"></a>
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
<a id="foldopen00212"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="l00327"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="l00352"></a>
<a id="l00353"></a>
<a id="l00354"></a>
<a id="l00355"></a>
<a id="l00356"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="l00380"></a>
<a id="l00381"></a>
<a id="l00382"></a>
<a id="l00383"></a>
<a id="l00384"></a>
<a id="l00385"></a>
<a id="l00386"></a>
<a id="l00387"></a>
<a id="l00407"></a>
<a id="l00408"></a>
<a id="l00409"></a>
<a id="l00410"></a>
<a id="l00411"></a>
<a id="l00412"></a>
<a id="l00413"></a>
<a id="l00414"></a>
<a id="l00416"></a>
<a id="l00417"></a>
<a id="l00418"></a>
<a id="l00419"></a>
<a id="l00420"></a>
<a id="l00421"></a>
<a id="l00422"></a>
<a id="l00423"></a>
<a id="l00424"></a>
<a id="l00425"></a>
<a id="l00426"></a>
<a id="l00427"></a>
<a id="l00428"></a>
<a id="l00429"></a>
<a id="l00430"></a>
<a id="l00431"></a>
<a id="l00432"></a>
<a id="l00433"></a>
<a id="l00434"></a>
<a id="l00435"></a>
<a id="l00436"></a>
<a id="l00437"></a>
<a id="l00438"></a>
<a id="l00439"></a>
<a id="l00440"></a>
<a id="l00441"></a>
<a id="l00442"></a>
<a id="l00443"></a>
<a id="l00444"></a>
<a id="l00445"></a>
<a id="l00446"></a>
<a id="l00447"></a>
<a id="l00448"></a>
<a id="l00449"></a>
<a id="l00450"></a>
<a id="l00451"></a>
<a id="l00452"></a>
<a id="l00453"></a>
<a id="l00454"></a>
<a id="l00455"></a>
<a id="l00456"></a>
<a id="l00457"></a>
<a id="l00458"></a>
<a id="l00459"></a>
<a id="l00460"></a>
<a id="l00461"></a>
<a id="l00462"></a>
<a id="l00463"></a>
<a id="l00464"></a>
<a id="l00465"></a>
<a id="l00466"></a>
<a id="l00467"></a>
<a id="l00468"></a>
<a id="l00469"></a>
<a id="l00470"></a>
<a id="l00471"></a>
<a id="l00472"></a>
<a id="l00473"></a>
<a id="l00474"></a>
<a id="l00476"></a>
<a id="l00480"></a>
<a id="l00481"></a>
<a id="l00482"></a>
<a id="l00483"></a>
<a id="l00484"></a>
<a id="l00485"></a>
<a id="adrivers_2can_8h_html"></a>
<a id="agroup__can__isotp_html_ga3723fae583a1d7deabc2deee475ba756"></a>
<a id="agroup__can__isotp_html_ga4fb0ef794b7c4104d6e6b17bc68e09d8"></a>
<a id="agroup__can__isotp_html_ga622293da5564203bf6dcb993410d21ba"></a>
<a id="agroup__can__isotp_html_ga725696a26c3bdc0c99e3c4e611a897f9"></a>
<a id="agroup__can__isotp_html_ga79c9cad7f39802c5c80af743717e22c6"></a>
<a id="agroup__can__isotp_html_gad4f9c0d3f847d453ea662128db2603bb"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="anet__buf_8h_html"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>
<a id="astructisotp__fc__opts_html"></a>
<a id="astructisotp__fc__opts_html_a5db0ceeed259c26d1d8fe0a901edcbca"></a>
<a id="astructisotp__fc__opts_html_a8f31bf5c95069352043da33541911b3c"></a>
<a id="astructisotp__msg__id_html"></a>
<a id="astructisotp__msg__id_html_a3185e5b5fddb5d7fc94b86c8d30e61a9"></a>
<a id="astructisotp__msg__id_html_a3f9d4a6efd9b1c147f889a6396d7ef1c"></a>
<a id="astructisotp__msg__id_html_a7b818e7c6dab02347b32bcc74dfc44a3"></a>
<a id="astructisotp__msg__id_html_ac9ded92f8e0afa88609003c5cf819704"></a>
<a id="astructisotp__msg__id_html_adc7ff4eac4573221b89a5bb5a5e53d49"></a>
<a id="astructk__timeout__t_html"></a>
<a id="astructnet__buf_html"></a>

```c
/*
 * Copyright (c) 2019 Alexander Wachter
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_CANBUS_ISOTP_H_
#define ZEPHYR_INCLUDE_CANBUS_ISOTP_H_


#include <zephyr/drivers/can.h>
#include <zephyr/types.h>
#include <zephyr/net_buf.h>

/*
 * Abbreviations
 * BS      Block Size
 * CAN_DL  CAN LL data size
 * CF      Consecutive Frame
 * CTS     Continue to send
 * DLC     Data length code
 * FC      Flow Control
 * FF      First Frame
 * SF      Single Frame
 * FS      Flow Status
 * AE      Address Extension
 * SN      Sequence Number
 * ST      Separation time
 * SA      Source Address
 * TA      Target Address
 * RX_DL   CAN RX LL data size
 * TX_DL   CAN TX LL data size
 * PCI     Process Control Information
 */

/*
 * N_Result according to ISO 15765-2:2016
 * ISOTP_ prefix is used to be zephyr conform
 */

#define ISOTP_N_OK              0

#define ISOTP_N_TIMEOUT_A      -1

#define ISOTP_N_TIMEOUT_BS     -2

#define ISOTP_N_TIMEOUT_CR     -3

#define ISOTP_N_WRONG_SN       -4

#define ISOTP_N_INVALID_FS     -5

#define ISOTP_N_UNEXP_PDU      -6

#define ISOTP_N_WFT_OVRN       -7

#define ISOTP_N_BUFFER_OVERFLW -8

#define ISOTP_N_ERROR          -9


#define ISOTP_NO_FREE_FILTER    -10

#define ISOTP_NO_NET_BUF_LEFT   -11

#define ISOTP_NO_BUF_DATA_LEFT  -12

#define ISOTP_NO_CTX_LEFT       -13

#define ISOTP_RECV_TIMEOUT      -14

/*
 * CAN ID filtering for ISO-TP fixed addressing according to SAE J1939
 *
 * Format of 29-bit CAN identifier:
 * ------------------------------------------------------
 * | 28 .. 26 | 25  | 24 | 23 .. 16 | 15 .. 8  | 7 .. 0 |
 * ------------------------------------------------------
 * | Priority | EDP | DP | N_TAtype |   N_TA   |  N_SA  |
 * ------------------------------------------------------
 */

#define ISOTP_FIXED_ADDR_SA_POS         (CONFIG_ISOTP_FIXED_ADDR_SA_POS)

#define ISOTP_FIXED_ADDR_SA_MASK        (CONFIG_ISOTP_FIXED_ADDR_SA_MASK)

#define ISOTP_FIXED_ADDR_TA_POS         (CONFIG_ISOTP_FIXED_ADDR_TA_POS)

#define ISOTP_FIXED_ADDR_TA_MASK        (CONFIG_ISOTP_FIXED_ADDR_TA_MASK)

#define ISOTP_FIXED_ADDR_PRIO_POS       (CONFIG_ISOTP_FIXED_ADDR_PRIO_POS)

#define ISOTP_FIXED_ADDR_PRIO_MASK      (CONFIG_ISOTP_FIXED_ADDR_PRIO_MASK)

#define ISOTP_FIXED_ADDR_RX_MASK        (CONFIG_ISOTP_FIXED_ADDR_RX_MASK)

#ifdef __cplusplus
extern "C" {
#endif


#define ISOTP_MSG_EXT_ADDR BIT(0)

#define ISOTP_MSG_FIXED_ADDR BIT(1)

#define ISOTP_MSG_IDE BIT(2)

#define ISOTP_MSG_FDF BIT(3)

#define ISOTP_MSG_BRS BIT(4)


struct isotp_msg_id {
        union {
                uint32_t std_id  : 11;
                uint32_t ext_id  : 29;
        };
        uint8_t ext_addr;
        uint8_t dl;
        uint8_t flags;
};

/*
 * STmin is split in two valid ranges:
 *   0-127: 0ms-127ms
 * 128-240: Reserved
 * 241-249: 100us-900us (multiples of 100us)
 * 250-   : Reserved
 */

struct isotp_fc_opts {
        uint8_t bs;
        uint8_t stmin;
};

typedef void (*isotp_tx_callback_t)(int error_nr, void *arg);

struct isotp_send_ctx;
struct isotp_recv_ctx;

int isotp_bind(struct isotp_recv_ctx *rctx, const struct device *can_dev,
               const struct isotp_msg_id *rx_addr,
               const struct isotp_msg_id *tx_addr,
               const struct isotp_fc_opts *opts,
               k_timeout_t timeout);

void isotp_unbind(struct isotp_recv_ctx *rctx);

int isotp_recv(struct isotp_recv_ctx *rctx, uint8_t *data, size_t len, k_timeout_t timeout);

int isotp_recv_net(struct isotp_recv_ctx *rctx, struct net_buf **buffer, k_timeout_t timeout);

int isotp_send(struct isotp_send_ctx *sctx, const struct device *can_dev,
               const uint8_t *data, size_t len,
               const struct isotp_msg_id *tx_addr,
               const struct isotp_msg_id *rx_addr,
               isotp_tx_callback_t complete_cb, void *cb_arg);

#ifdef CONFIG_ISOTP_ENABLE_CONTEXT_BUFFERS
int isotp_send_ctx_buf(const struct device *can_dev,
                       const uint8_t *data, size_t len,
                       const struct isotp_msg_id *tx_addr,
                       const struct isotp_msg_id *rx_addr,
                       isotp_tx_callback_t complete_cb, void *cb_arg,
                       k_timeout_t timeout);

int isotp_send_net_ctx_buf(const struct device *can_dev,
                           struct net_buf *data,
                           const struct isotp_msg_id *tx_addr,
                           const struct isotp_msg_id *rx_addr,
                           isotp_tx_callback_t complete_cb, void *cb_arg,
                           k_timeout_t timeout);

#endif /*CONFIG_ISOTP_ENABLE_CONTEXT_BUFFERS*/

#if defined(CONFIG_ISOTP_USE_TX_BUF) && \
        defined(CONFIG_ISOTP_ENABLE_CONTEXT_BUFFERS)
int isotp_send_buf(const struct device *can_dev,
                   const uint8_t *data, size_t len,
                   const struct isotp_msg_id *tx_addr,
                   const struct isotp_msg_id *rx_addr,
                   isotp_tx_callback_t complete_cb, void *cb_arg,
                   k_timeout_t timeout);
#endif


struct isotp_callback {
        isotp_tx_callback_t cb;
        void *arg;
};

struct isotp_send_ctx {
        int filter_id;
        uint32_t error_nr;
        const struct device *can_dev;
        union {
                struct net_buf *buf;
                struct {
                        const uint8_t *data;
                        size_t len;
                };
        };
        struct k_work work;
        struct k_timer timer;
        union {
                struct isotp_callback fin_cb;
                struct k_sem fin_sem;
        };
        struct isotp_fc_opts opts;
        uint8_t state;
        uint8_t tx_backlog;
        struct k_sem tx_sem;
        struct isotp_msg_id rx_addr;
        struct isotp_msg_id tx_addr;
        uint8_t wft;
        uint8_t bs;
        uint8_t sn : 4;
        uint8_t is_net_buf  : 1;
        uint8_t is_ctx_slab : 1;
        uint8_t has_callback: 1;
};

struct isotp_recv_ctx {
        int filter_id;
        const struct device *can_dev;
        struct net_buf *buf;
        struct net_buf *act_frag;
        /* buffer currently processed in isotp_recv */
        struct net_buf *recv_buf;
        sys_snode_t alloc_node;
        uint32_t length;
        int error_nr;
        struct k_work work;
        struct k_timer timer;
        struct k_fifo fifo;
        struct isotp_msg_id rx_addr;
        struct isotp_msg_id tx_addr;
        struct isotp_fc_opts opts;
        uint8_t state;
        uint8_t bs;
        uint8_t wft;
        uint8_t sn_expected : 4;
};



#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_CANBUS_ISOTP_H_ */
```

## 15.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2019 Alexander Wachter。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 30 行

缩写（Abbreviations）：

| 缩写 | 中文 | 英文 |
| --- | --- | --- |
| BS | 块大小 | Block Size |
| CAN_DL | CAN 链路层数据大小 | CAN LL Data Size |
| CF | 连续帧 | Consecutive Frame |
| CTS | 继续发送 | Continue to Send |
| DLC | 数据长度码 | Data Length Code |
| FC | 流控制 | Flow Control |
| FF | 首帧 | First Frame |
| SF | 单帧 | Single Frame |
| FS | 流状态 | Flow Status |
| AE | 地址扩展 | Address Extension |
| SN | 序号 | Sequence Number |
| ST | 帧间隔时间 | Separation Time |
| SA | 源地址 | Source Address |
| TA | 目标地址 | Target Address |
| RX_DL | CAN 接收链路层数据大小 | CAN RX LL Data Size |
| TX_DL | CAN 发送链路层数据大小 | CAN TX LL Data Size |
| PCI | 过程控制信息（按原注释） | Process Control Information |

### 注释 3：原第 51 行

符合 ISO 15765-2:2016 的 `N_Result`。
使用 `ISOTP_` 前缀，以符合 Zephyr 约定。

### 注释 4：原第 103 行

根据 SAE J1939，采用 ISO-TP 固定寻址（Fixed Addressing）的 CAN 标识过滤（CAN ID Filtering）。

29 位 CAN 标识符（Identifier）的格式：

| 位范围 | 字段 |
| --- | --- |
| 28～26 | 优先级（Priority） |
| 25 | `EDP` |
| 24 | `DP` |
| 23～16 | `N_TAtype` |
| 15～8 | `N_TA` |
| 7～0 | `N_SA` |

### 注释 5：原第 199 行

最小帧间隔（STmin）具有两个有效范围：

- 0～127：0～127 ms。
- 128～240：保留（Reserved）。
- 241～249：100～900 μs，步长为 100 μs。
- 250 及以上：保留（Reserved）。

### 注释 6：原第 384 行

条件编译配置（Configuration）标记：`CONFIG_ISOTP_ENABLE_CONTEXT_BUFFERS`。

### 注释 7：原第 458 行

`isotp_recv` 当前正在处理的缓冲区（Buffer）。

### 注释 8：原第 485 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_CANBUS_ISOTP_H_`。

## 15.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/isotp_8h.html)
- [zephyr/drivers/can.h](../can_driver_reference/P001_CAN驱动头文件参考.md)
- [zephyr/types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [isotp_msg_id](../hardware/P381_ISO-TP消息标识.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [std_id](https://docs.zephyrproject.org/latest/doxygen/html/structisotp__msg__id.html#ac9ded92f8e0afa88609003c5cf819704)
- [ext_id](https://docs.zephyrproject.org/latest/doxygen/html/structisotp__msg__id.html#a3f9d4a6efd9b1c147f889a6396d7ef1c)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [ext_addr](https://docs.zephyrproject.org/latest/doxygen/html/structisotp__msg__id.html#a7b818e7c6dab02347b32bcc74dfc44a3)
- [dl](https://docs.zephyrproject.org/latest/doxygen/html/structisotp__msg__id.html#adc7ff4eac4573221b89a5bb5a5e53d49)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/structisotp__msg__id.html#a3185e5b5fddb5d7fc94b86c8d30e61a9)
- [isotp_fc_opts](../hardware/P382_ISO-TP流控选项.md)
- [bs](https://docs.zephyrproject.org/latest/doxygen/html/structisotp__fc__opts.html#a8f31bf5c95069352043da33541911b3c)
- [stmin](https://docs.zephyrproject.org/latest/doxygen/html/structisotp__fc__opts.html#a5db0ceeed259c26d1d8fe0a901edcbca)
- [isotp_tx_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#gad4f9c0d3f847d453ea662128db2603bb)
- [isotp_bind](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga725696a26c3bdc0c99e3c4e611a897f9)
- [device](../device_reference/P002_设备对象结构.md)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [isotp_unbind](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga622293da5564203bf6dcb993410d21ba)
- [isotp_recv](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga79c9cad7f39802c5c80af743717e22c6)
- [isotp_recv_net](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga4fb0ef794b7c4104d6e6b17bc68e09d8)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [isotp_send](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga3723fae583a1d7deabc2deee475ba756)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [can.h](../can_driver_reference/P001_CAN驱动头文件参考.md)
- [types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [isotp_fc_opts::stmin](https://docs.zephyrproject.org/latest/doxygen/html/structisotp__fc__opts.html#a5db0ceeed259c26d1d8fe0a901edcbca)
- [isotp_fc_opts::bs](https://docs.zephyrproject.org/latest/doxygen/html/structisotp__fc__opts.html#a8f31bf5c95069352043da33541911b3c)
- [isotp_msg_id::flags](https://docs.zephyrproject.org/latest/doxygen/html/structisotp__msg__id.html#a3185e5b5fddb5d7fc94b86c8d30e61a9)
- [isotp_msg_id::ext_id](https://docs.zephyrproject.org/latest/doxygen/html/structisotp__msg__id.html#a3f9d4a6efd9b1c147f889a6396d7ef1c)
- [isotp_msg_id::ext_addr](https://docs.zephyrproject.org/latest/doxygen/html/structisotp__msg__id.html#a7b818e7c6dab02347b32bcc74dfc44a3)
- [isotp_msg_id::std_id](https://docs.zephyrproject.org/latest/doxygen/html/structisotp__msg__id.html#ac9ded92f8e0afa88609003c5cf819704)
- [isotp_msg_id::dl](https://docs.zephyrproject.org/latest/doxygen/html/structisotp__msg__id.html#adc7ff4eac4573221b89a5bb5a5e53d49)

---

[上一章](P014_irq.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P016_l2cap.h_源码浏览.md)
