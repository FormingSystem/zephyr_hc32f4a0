---
id: learning.zephyr-docs.api-source-runtime-reference.page-53
title: rfcomm.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rfcomm_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第53章\_rfcomm.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/rfcomm_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/rfcomm_8h.html)。

## 53.1\_原始可见代码（Source Code）

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
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="foldopen00046"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
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
<a id="foldopen00082"></a>
<a id="l00082"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="foldopen00142"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="foldopen00148"></a>
<a id="l00148"></a>
<a id="l00150"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00189"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00194"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00199"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00204"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00209"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00218"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00240"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00261"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="foldopen00283"></a>
<a id="l00283"></a>
<a id="l00294"></a>
<a id="l00295"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="l00311"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00327"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="l00343"></a>
<a id="l00344"></a>
<a id="l00345"></a>
<a id="l00346"></a>
<a id="l00347"></a>
<a id="l00348"></a>
<a id="l00349"></a>
<a id="l00350"></a>
<a id="foldopen00359"></a>
<a id="l00359"></a>
<a id="l00360"></a>
<a id="l00361"></a>
<a id="l00362"></a>
<a id="l00363"></a>
<a id="l00364"></a>
<a id="l00365"></a>
<a id="l00366"></a>
<a id="l00367"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="foldopen00371"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="l00380"></a>
<a id="l00391"></a>
<a id="l00392"></a>
<a id="l00401"></a>
<a id="l00402"></a>
<a id="l00415"></a>
<a id="l00416"></a>
<a id="l00417"></a>
<a id="l00428"></a>
<a id="l00429"></a>
<a id="l00439"></a>
<a id="l00440"></a>
<a id="l00473"></a>
<a id="l00474"></a>
<a id="l00482"></a>
<a id="l00483"></a>
<a id="l00492"></a>
<a id="l00493"></a>
<a id="l00495"></a>
<a id="l00496"></a>
<a id="l00505"></a>
<a id="l00506"></a>
<a id="l00508"></a>
<a id="l00509"></a>
<a id="l00511"></a>
<a id="l00512"></a>
<a id="l00514"></a>
<a id="l00515"></a>
<a id="l00536"></a>
<a id="l00537"></a>
<a id="l00538"></a>
<a id="l00539"></a>
<a id="l00540"></a>
<a id="l00541"></a>
<a id="l00545"></a>
<a id="l00546"></a>
<a id="abuf_8h_html"></a>
<a id="aconn_8h_html"></a>
<a id="agroup__atomic__apis_html_ga124f07c3a788e53c3a40e4e1c06d8af8"></a>
<a id="agroup__bt__conn_html_gaf0c56cd26c4147f6c9f0faa11fa01783"></a>
<a id="agroup__bt__rfcomm_html_ga11f290d34ad631afaa10caf2cefd72b9"></a>
<a id="agroup__bt__rfcomm_html_ga1a46f58b41dab9a81b8d2b88f0f22547"></a>
<a id="agroup__bt__rfcomm_html_ga2ce765351798976136c3096a9a7f9465"></a>
<a id="agroup__bt__rfcomm_html_ga2fb8e3ce2a39d0a3c5bea9b3c24a7ab7"></a>
<a id="agroup__bt__rfcomm_html_ga593841aef52027598977b7b2bbd0237d"></a>
<a id="agroup__bt__rfcomm_html_ga998328b021ec53f7e291ab76856ffa18"></a>
<a id="agroup__bt__rfcomm_html_gaa70d7971435dc7e6421372d7385811b2"></a>
<a id="agroup__bt__rfcomm_html_gab38378db71d7f4631e47742ce4a5c59d"></a>
<a id="agroup__bt__rfcomm_html_gaed05e67dc975d94e1209372d5817077a"></a>
<a id="agroup__bt__rfcomm_html_gaf6bb5c563ba32fa76fc774271d958fe4"></a>
<a id="agroup__bt__rfcomm_html_gafd0ffcff41e233f74dc2726e889f5401"></a>
<a id="agroup__bt__rfcomm_html_gga15600feb01d876e319e1d5f93991592ba5f1673591e5000a115e245bd03ecf1d1"></a>
<a id="agroup__bt__rfcomm_html_gga15600feb01d876e319e1d5f93991592ba5fd45643d1d17830ee62d4306ab53867"></a>
<a id="agroup__bt__rfcomm_html_gga15600feb01d876e319e1d5f93991592ba71dfabec6fec6ac77ee8705a5bbcf3bc"></a>
<a id="agroup__bt__rfcomm_html_gga15600feb01d876e319e1d5f93991592bada0317ee756dc6887917cb47057e2f83"></a>
<a id="agroup__bt__rfcomm_html_gga61637d261987529c219dcd1179ed1711a59c1506cbc6c7fdd5a36788d8ef39c60"></a>
<a id="agroup__bt__rfcomm_html_gga61637d261987529c219dcd1179ed1711a62dff7e4366dd199a587fc70a716606c"></a>
<a id="agroup__bt__rfcomm_html_gga61637d261987529c219dcd1179ed1711a69c572ab3be43441a49faf2253a47593"></a>
<a id="agroup__bt__rfcomm_html_gga61637d261987529c219dcd1179ed1711a8b3417a1fe245ec0323e53ddcaff1760"></a>
<a id="agroup__bt__rfcomm_html_gga61637d261987529c219dcd1179ed1711a8b9599a9fb16f3117a8a7197b08b32a5"></a>
<a id="agroup__bt__rfcomm_html_gga61637d261987529c219dcd1179ed1711a9c6a80ed27f57ac5dc0d3547d53002b9"></a>
<a id="agroup__bt__rfcomm_html_gga61637d261987529c219dcd1179ed1711aa16395c45811836119468c7d68cdf8e3"></a>
<a id="agroup__bt__rfcomm_html_gga61637d261987529c219dcd1179ed1711adab0850dc108831ba7d1a7c8ac8d0048"></a>
<a id="agroup__bt__rfcomm_html_gga61637d261987529c219dcd1179ed1711af6e5a7d8af8654726bfacdd6f29e8e33"></a>
<a id="agroup__bt__rfcomm_html_ggaa70d7971435dc7e6421372d7385811b2a20601c2b890ee84b83dfc9ed55e07cf8"></a>
<a id="agroup__bt__rfcomm_html_ggaa70d7971435dc7e6421372d7385811b2aa0b65eed9632ff8ad3235b4c0eae166d"></a>
<a id="agroup__bt__rfcomm_html_ggabe97ddd372c3b0b44a9b78539ddf9ffca69c2bfefd90f2cea4b157c00b7b460b6"></a>
<a id="agroup__bt__rfcomm_html_ggabe97ddd372c3b0b44a9b78539ddf9ffcab59060e62e8df130c857d3873159c339"></a>
<a id="agroup__bt__rfcomm_html_ggad1794db284f7b39f4816f04f21ed3f4ba137092626a52e1d2e8fada8d8594a90b"></a>
<a id="agroup__bt__rfcomm_html_ggad1794db284f7b39f4816f04f21ed3f4ba365e32b5820a0921611325d7c61dd169"></a>
<a id="agroup__bt__rfcomm_html_ggad1794db284f7b39f4816f04f21ed3f4ba376c5d59c7fea34b79ad4d9cd9e66e18"></a>
<a id="agroup__bt__rfcomm_html_ggad1794db284f7b39f4816f04f21ed3f4ba43d7b78c72b589f51a2811176d816fc9"></a>
<a id="agroup__bt__rfcomm_html_ggad1794db284f7b39f4816f04f21ed3f4ba5466e7f23ce5550bffada30ff15658e1"></a>
<a id="agroup__bt__rfcomm_html_ggafccaaeb8f4d4f3e3834f358ccfdfb86ba05cfd05b25c785acb72916b723141495"></a>
<a id="agroup__bt__rfcomm_html_ggafccaaeb8f4d4f3e3834f358ccfdfb86ba91be303c7fb7bb210d8209ee746a4302"></a>
<a id="agroup__bt__rfcomm_html_ggafccaaeb8f4d4f3e3834f358ccfdfb86baa62985d89ab11a130eed284d98b7b1e4"></a>
<a id="agroup__bt__rfcomm_html_ggafccaaeb8f4d4f3e3834f358ccfdfb86baaf92af85143e2a0430d5a99c9a0d3c25"></a>
<a id="agroup__bt__rfcomm_html_ggafccaaeb8f4d4f3e3834f358ccfdfb86bac7f345a01b4d9aca4c2a879dce05e0dd"></a>
<a id="agroup__bt__rfcomm_html_ggafccaaeb8f4d4f3e3834f358ccfdfb86badc095ec30d3edf16ef95ece5b3c1104b"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="al2cap_8h_html"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="aslist_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructbt__conn_html"></a>
<a id="astructbt__rfcomm__dlc__ops_html"></a>
<a id="astructbt__rfcomm__dlc__ops_html_a3ba98c41e03c88f330cba0e3539a1cec"></a>
<a id="astructbt__rfcomm__dlc__ops_html_a4eeaf7b5db6c93e846a72797e6612d30"></a>
<a id="astructbt__rfcomm__dlc__ops_html_ab8ef2f8c1d27eee20d0b5e7fce6f7354"></a>
<a id="astructbt__rfcomm__dlc__ops_html_aba1719c36e7a1dc9705994bcdf134e28"></a>
<a id="astructbt__rfcomm__dlc_html"></a>
<a id="astructbt__rfcomm__dlc_html_a0054c0b539b947688555b5663c585bb7"></a>
<a id="astructbt__rfcomm__dlc_html_a2334abbaacad9b98c2cb2c5650644854"></a>
<a id="astructbt__rfcomm__dlc_html_a27157f693d91aac6aaafe1bd70593404"></a>
<a id="astructbt__rfcomm__dlc_html_ab298ebd444566533018eabdc5a69c8ba"></a>
<a id="astructbt__rfcomm__rpn_html"></a>
<a id="astructbt__rfcomm__rpn_html_a9eaac13558a5be2fed82084e0bb7a20a"></a>
<a id="astructbt__rfcomm__rpn_html_aad2f64edcb82e864293869474d20fa81"></a>
<a id="astructbt__rfcomm__rpn_html_acd61f81d3de1fe4da58fd5ee0d4e5e77"></a>
<a id="astructbt__rfcomm__rpn_html_adc651e1ac74d616fd03b07a647139296"></a>
<a id="astructbt__rfcomm__rpn_html_ae0db46df73fae846cb53f8a0cf01350a"></a>
<a id="astructbt__rfcomm__rpn_html_ae637cd243e9b016231b5071e171b6b54"></a>
<a id="astructbt__rfcomm__rpn_html_afacd73edbb63e3ade9573100967faffa"></a>
<a id="astructbt__rfcomm__server_html"></a>
<a id="astructbt__rfcomm__server_html_a30b22ea64c0fdd7130e8aaa79519e776"></a>
<a id="astructbt__rfcomm__server_html_ac08708bb8161f787737962f62d3c003f"></a>
<a id="astructk__fifo_html"></a>
<a id="astructk__sem_html"></a>
<a id="astructk__work__delayable_html"></a>
<a id="astructnet__buf__pool_html"></a>
<a id="astructnet__buf_html"></a>

```c


/*
 * Copyright (c) 2015-2016 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_RFCOMM_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_RFCOMM_H_


#include <zephyr/bluetooth/buf.h>
#include <zephyr/bluetooth/conn.h>
#include <zephyr/bluetooth/l2cap.h>
#include <zephyr/sys/slist.h>

#ifdef __cplusplus
extern "C" {
#endif

#define BT_RFCOMM_HDR_MAX_SIZE 4
#define BT_RFCOMM_FCS_SIZE     1
#define BT_RFCOMM_CREDITS_SIZE 1

#define BT_RFCOMM_OVERHEAD_SIZE                                                                    \
        (BT_RFCOMM_HDR_MAX_SIZE + BT_RFCOMM_FCS_SIZE + BT_RFCOMM_CREDITS_SIZE)

#define BT_RFCOMM_BUF_SIZE(mtu) BT_L2CAP_BUF_SIZE(BT_RFCOMM_OVERHEAD_SIZE + (mtu))

/* RFCOMM channels (1-30): pre-allocated for profiles to avoid conflicts */
enum {
        BT_RFCOMM_CHAN_HFP_HF = 1,
        BT_RFCOMM_CHAN_HFP_AG,
        BT_RFCOMM_CHAN_HSP_AG,
        BT_RFCOMM_CHAN_HSP_HS,
        BT_RFCOMM_CHAN_SPP,
        BT_RFCOMM_CHAN_DYNAMIC_START,
};

struct bt_rfcomm_dlc;

struct bt_rfcomm_dlc_ops {
        void (*connected)(struct bt_rfcomm_dlc *dlc);

        void (*disconnected)(struct bt_rfcomm_dlc *dlc);

        int (*recv)(struct bt_rfcomm_dlc *dlc, struct net_buf *buf);

        void (*sent)(struct bt_rfcomm_dlc *dlc, int err);
};

typedef enum bt_rfcomm_role {
        BT_RFCOMM_ROLE_ACCEPTOR,
        BT_RFCOMM_ROLE_INITIATOR
} __packed bt_rfcomm_role_t;

struct bt_rfcomm_dlc {

        struct k_work_delayable rtx_work;

        struct k_fifo tx_queue;

        struct k_sem tx_credits;

        struct k_work_delayable tx_work;

        /* Retry timeout expired timer */
        struct k_work_delayable retry_timeout_work;

        struct bt_rfcomm_session *session;


        struct bt_rfcomm_dlc_ops *ops;


        sys_snode_t _node;


        bt_security_t required_sec_level;


        bt_rfcomm_role_t role;


        uint16_t mtu;


        uint8_t dlci;

        uint8_t state;

        uint8_t rx_credit;


        uint8_t rx_credit_limit;


        atomic_t rx_credit_inprogress;

        atomic_t flags;

};

struct bt_rfcomm_server {
        uint8_t channel;

        int (*accept)(struct bt_conn *conn, struct bt_rfcomm_server *server,
                      struct bt_rfcomm_dlc **dlc);

        sys_snode_t node;
};

enum {
        BT_RFCOMM_RPN_BAUD_RATE_2400 = 0x0,
        BT_RFCOMM_RPN_BAUD_RATE_4800 = 0x1,
        BT_RFCOMM_RPN_BAUD_RATE_7200 = 0x2,
        BT_RFCOMM_RPN_BAUD_RATE_9600 = 0x3,
        BT_RFCOMM_RPN_BAUD_RATE_19200 = 0x4,
        BT_RFCOMM_RPN_BAUD_RATE_38400 = 0x5,
        BT_RFCOMM_RPN_BAUD_RATE_57600 = 0x6,
        BT_RFCOMM_RPN_BAUD_RATE_115200 = 0x7,
        BT_RFCOMM_RPN_BAUD_RATE_230400 = 0x8
};

enum {
        BT_RFCOMM_RPN_DATA_BITS_5 = 0x0,
        BT_RFCOMM_RPN_DATA_BITS_6 = 0x1,
        BT_RFCOMM_RPN_DATA_BITS_7 = 0x2,
        BT_RFCOMM_RPN_DATA_BITS_8 = 0x3
};

enum {
        BT_RFCOMM_RPN_STOP_BITS_1 = 0,
        BT_RFCOMM_RPN_STOP_BITS_1_5 = 1
};

enum {
        BT_RFCOMM_RPN_PARITY_NONE = 0x0,
        BT_RFCOMM_RPN_PARITY_ODD = 0x1,
        BT_RFCOMM_RPN_PARITY_EVEN = 0x3,
        BT_RFCOMM_RPN_PARITY_MARK = 0x5,
        BT_RFCOMM_RPN_PARITY_SPACE = 0x7
};

#define BT_RFCOMM_SET_LINE_SETTINGS(data, stop, parity) ((data & 0x3) | \
                                                         ((stop & 0x1) << 2) | \
                                                         ((parity & 0x7) << 3))

#define BT_RFCOMM_RPN_FLOW_NONE         0x00
#define BT_RFCOMM_RPN_XON_CHAR          0x11
#define BT_RFCOMM_RPN_XOFF_CHAR         0x13

/* Set 1 to all the param mask except reserved */
#define BT_RFCOMM_RPN_PARAM_MASK_ALL    0x3f7f

struct bt_rfcomm_rpn {
        uint8_t  dlci;
        uint8_t  baud_rate;
        uint8_t  line_settings;
        uint8_t  flow_control;
        uint8_t  xon_char;
        uint8_t  xoff_char;
        uint16_t param_mask;
} __packed;

int bt_rfcomm_server_register(struct bt_rfcomm_server *server);

int bt_rfcomm_server_unregister(struct bt_rfcomm_server *server);

int bt_rfcomm_dlc_connect(struct bt_conn *conn, struct bt_rfcomm_dlc *dlc,
                          uint8_t channel);

int bt_rfcomm_dlc_send(struct bt_rfcomm_dlc *dlc, struct net_buf *buf);

int bt_rfcomm_dlc_disconnect(struct bt_rfcomm_dlc *dlc);

int bt_rfcomm_dlc_recv_complete(struct bt_rfcomm_dlc *dlc, struct net_buf *buf);

struct net_buf *bt_rfcomm_create_pdu(struct net_buf_pool *pool);

int bt_rfcomm_send_rpn_cmd(struct bt_rfcomm_dlc *dlc, struct bt_rfcomm_rpn *rpn);

#define BT_RFCOMM_RLS_NO_ERR (0x00U)

#define BT_RFCOMM_RLS_ERR(err) (BIT(0) | (err))

#define BT_RFCOMM_RLS_ERR_OVERRUN_ERROR BIT(1)

#define BT_RFCOMM_RLS_ERR_PARITY_ERROR BIT(2)

#define BT_RFCOMM_RLS_ERR_FRAMING_ERROR BIT(3)

int bt_rfcomm_send_rls_cmd(struct bt_rfcomm_dlc *dlc, uint8_t line_status);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_RFCOMM_H_ */
```

## 53.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：© 2015-2016 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 58 行

RFCOMM 通道 1–30，预先分配给各配置文件（Profiles）以避免冲突。

### 注释 3：原第 182 行

重试超时到期定时器（Retry timeout expired timer）。

### 注释 4：原第 367 行

除保留位外，将参数掩码中的所有位设为 1。

### 注释 5：原第 546 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_CLASSIC_RFCOMM_H_`。

## 53.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/rfcomm_8h.html)
- [zephyr/bluetooth/buf.h](https://docs.zephyrproject.org/latest/doxygen/html/buf_8h.html)
- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [zephyr/bluetooth/l2cap.h](https://docs.zephyrproject.org/latest/doxygen/html/l2cap_8h.html)
- [zephyr/sys/slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [BT_RFCOMM_CHAN_HFP_HF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ggafccaaeb8f4d4f3e3834f358ccfdfb86baa62985d89ab11a130eed284d98b7b1e4)
- [BT_RFCOMM_CHAN_HFP_AG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ggafccaaeb8f4d4f3e3834f358ccfdfb86bac7f345a01b4d9aca4c2a879dce05e0dd)
- [BT_RFCOMM_CHAN_HSP_AG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ggafccaaeb8f4d4f3e3834f358ccfdfb86badc095ec30d3edf16ef95ece5b3c1104b)
- [BT_RFCOMM_CHAN_HSP_HS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ggafccaaeb8f4d4f3e3834f358ccfdfb86baaf92af85143e2a0430d5a99c9a0d3c25)
- [BT_RFCOMM_CHAN_SPP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ggafccaaeb8f4d4f3e3834f358ccfdfb86ba05cfd05b25c785acb72916b723141495)
- [BT_RFCOMM_CHAN_DYNAMIC_START](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ggafccaaeb8f4d4f3e3834f358ccfdfb86ba91be303c7fb7bb210d8209ee746a4302)
- [bt_rfcomm_dlc](../bluetooth_service_model_reference/P155_bt_rfcomm_dlc_结构体.md)
- [bt_rfcomm_dlc_ops](../bluetooth_service_model_reference/P156_bt_rfcomm_dlc_ops_结构体.md)
- [connected](../bluetooth_service_model_reference/P156_bt_rfcomm_dlc_ops_结构体.md#aba1719c36e7a1dc9705994bcdf134e28)
- [disconnected](../bluetooth_service_model_reference/P156_bt_rfcomm_dlc_ops_结构体.md#a4eeaf7b5db6c93e846a72797e6612d30)
- [recv](../bluetooth_service_model_reference/P156_bt_rfcomm_dlc_ops_结构体.md#ab8ef2f8c1d27eee20d0b5e7fce6f7354)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [sent](../bluetooth_service_model_reference/P156_bt_rfcomm_dlc_ops_结构体.md#a3ba98c41e03c88f330cba0e3539a1cec)
- [bt_rfcomm_role](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gaa70d7971435dc7e6421372d7385811b2)
- [BT_RFCOMM_ROLE_ACCEPTOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ggaa70d7971435dc7e6421372d7385811b2aa0b65eed9632ff8ad3235b4c0eae166d)
- [BT_RFCOMM_ROLE_INITIATOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ggaa70d7971435dc7e6421372d7385811b2a20601c2b890ee84b83dfc9ed55e07cf8)
- [bt_rfcomm_role_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ga11f290d34ad631afaa10caf2cefd72b9)
- [k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)
- [k_fifo](../queue_reference/P004_内核FIFO结构.md)
- [k_sem](../synchronization_reference/P009_内核信号量结构.md)
- [ops](../bluetooth_service_model_reference/P155_bt_rfcomm_dlc_结构体.md#a0054c0b539b947688555b5663c585bb7)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [bt_security_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf0c56cd26c4147f6c9f0faa11fa01783)
- [required_sec_level](../bluetooth_service_model_reference/P155_bt_rfcomm_dlc_结构体.md#ab298ebd444566533018eabdc5a69c8ba)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [mtu](../bluetooth_service_model_reference/P155_bt_rfcomm_dlc_结构体.md#a2334abbaacad9b98c2cb2c5650644854)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [rx_credit_limit](../bluetooth_service_model_reference/P155_bt_rfcomm_dlc_结构体.md#a27157f693d91aac6aaafe1bd70593404)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [bt_rfcomm_server](../bluetooth_service_model_reference/P158_bt_rfcomm_server_结构体.md)
- [channel](../bluetooth_service_model_reference/P158_bt_rfcomm_server_结构体.md#a30b22ea64c0fdd7130e8aaa79519e776)
- [accept](../bluetooth_service_model_reference/P158_bt_rfcomm_server_结构体.md#ac08708bb8161f787737962f62d3c003f)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [BT_RFCOMM_RPN_BAUD_RATE_2400](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gga61637d261987529c219dcd1179ed1711aa16395c45811836119468c7d68cdf8e3)
- [BT_RFCOMM_RPN_BAUD_RATE_4800](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gga61637d261987529c219dcd1179ed1711a59c1506cbc6c7fdd5a36788d8ef39c60)
- [BT_RFCOMM_RPN_BAUD_RATE_7200](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gga61637d261987529c219dcd1179ed1711a69c572ab3be43441a49faf2253a47593)
- [BT_RFCOMM_RPN_BAUD_RATE_9600](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gga61637d261987529c219dcd1179ed1711a9c6a80ed27f57ac5dc0d3547d53002b9)
- [BT_RFCOMM_RPN_BAUD_RATE_19200](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gga61637d261987529c219dcd1179ed1711a62dff7e4366dd199a587fc70a716606c)
- [BT_RFCOMM_RPN_BAUD_RATE_38400](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gga61637d261987529c219dcd1179ed1711a8b9599a9fb16f3117a8a7197b08b32a5)
- [BT_RFCOMM_RPN_BAUD_RATE_57600](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gga61637d261987529c219dcd1179ed1711adab0850dc108831ba7d1a7c8ac8d0048)
- [BT_RFCOMM_RPN_BAUD_RATE_115200](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gga61637d261987529c219dcd1179ed1711af6e5a7d8af8654726bfacdd6f29e8e33)
- [BT_RFCOMM_RPN_BAUD_RATE_230400](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gga61637d261987529c219dcd1179ed1711a8b3417a1fe245ec0323e53ddcaff1760)
- [BT_RFCOMM_RPN_DATA_BITS_5](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gga15600feb01d876e319e1d5f93991592ba5f1673591e5000a115e245bd03ecf1d1)
- [BT_RFCOMM_RPN_DATA_BITS_6](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gga15600feb01d876e319e1d5f93991592ba71dfabec6fec6ac77ee8705a5bbcf3bc)
- [BT_RFCOMM_RPN_DATA_BITS_7](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gga15600feb01d876e319e1d5f93991592ba5fd45643d1d17830ee62d4306ab53867)
- [BT_RFCOMM_RPN_DATA_BITS_8](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gga15600feb01d876e319e1d5f93991592bada0317ee756dc6887917cb47057e2f83)
- [BT_RFCOMM_RPN_STOP_BITS_1](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ggabe97ddd372c3b0b44a9b78539ddf9ffcab59060e62e8df130c857d3873159c339)
- [BT_RFCOMM_RPN_STOP_BITS_1_5](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ggabe97ddd372c3b0b44a9b78539ddf9ffca69c2bfefd90f2cea4b157c00b7b460b6)
- [BT_RFCOMM_RPN_PARITY_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ggad1794db284f7b39f4816f04f21ed3f4ba137092626a52e1d2e8fada8d8594a90b)
- [BT_RFCOMM_RPN_PARITY_ODD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ggad1794db284f7b39f4816f04f21ed3f4ba365e32b5820a0921611325d7c61dd169)
- [BT_RFCOMM_RPN_PARITY_EVEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ggad1794db284f7b39f4816f04f21ed3f4ba376c5d59c7fea34b79ad4d9cd9e66e18)
- [BT_RFCOMM_RPN_PARITY_MARK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ggad1794db284f7b39f4816f04f21ed3f4ba43d7b78c72b589f51a2811176d816fc9)
- [BT_RFCOMM_RPN_PARITY_SPACE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ggad1794db284f7b39f4816f04f21ed3f4ba5466e7f23ce5550bffada30ff15658e1)
- [bt_rfcomm_rpn](../bluetooth_service_model_reference/P157_bt_rfcomm_rpn_结构体.md)
- [dlci](../bluetooth_service_model_reference/P157_bt_rfcomm_rpn_结构体.md#afacd73edbb63e3ade9573100967faffa)
- [baud_rate](../bluetooth_service_model_reference/P157_bt_rfcomm_rpn_结构体.md#aad2f64edcb82e864293869474d20fa81)
- [line_settings](../bluetooth_service_model_reference/P157_bt_rfcomm_rpn_结构体.md#acd61f81d3de1fe4da58fd5ee0d4e5e77)
- [flow_control](../bluetooth_service_model_reference/P157_bt_rfcomm_rpn_结构体.md#ae0db46df73fae846cb53f8a0cf01350a)
- [xon_char](../bluetooth_service_model_reference/P157_bt_rfcomm_rpn_结构体.md#ae637cd243e9b016231b5071e171b6b54)
- [xoff_char](../bluetooth_service_model_reference/P157_bt_rfcomm_rpn_结构体.md#adc651e1ac74d616fd03b07a647139296)
- [param_mask](../bluetooth_service_model_reference/P157_bt_rfcomm_rpn_结构体.md#a9eaac13558a5be2fed82084e0bb7a20a)
- [bt_rfcomm_server_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gafd0ffcff41e233f74dc2726e889f5401)
- [bt_rfcomm_server_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gaf6bb5c563ba32fa76fc774271d958fe4)
- [bt_rfcomm_dlc_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ga2fb8e3ce2a39d0a3c5bea9b3c24a7ab7)
- [bt_rfcomm_dlc_send](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ga593841aef52027598977b7b2bbd0237d)
- [bt_rfcomm_dlc_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ga998328b021ec53f7e291ab76856ffa18)
- [bt_rfcomm_dlc_recv_complete](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ga2ce765351798976136c3096a9a7f9465)
- [bt_rfcomm_create_pdu](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gaed05e67dc975d94e1209372d5817077a)
- [net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)
- [bt_rfcomm_send_rpn_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#gab38378db71d7f4631e47742ce4a5c59d)
- [bt_rfcomm_send_rls_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ga1a46f58b41dab9a81b8d2b88f0f22547)
- [buf.h](https://docs.zephyrproject.org/latest/doxygen/html/buf_8h.html)
- [conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [l2cap.h](https://docs.zephyrproject.org/latest/doxygen/html/l2cap_8h.html)
- [slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [bt_rfcomm_dlc_ops::sent](../bluetooth_service_model_reference/P156_bt_rfcomm_dlc_ops_结构体.md#a3ba98c41e03c88f330cba0e3539a1cec)
- [bt_rfcomm_dlc_ops::disconnected](../bluetooth_service_model_reference/P156_bt_rfcomm_dlc_ops_结构体.md#a4eeaf7b5db6c93e846a72797e6612d30)
- [bt_rfcomm_dlc_ops::recv](../bluetooth_service_model_reference/P156_bt_rfcomm_dlc_ops_结构体.md#ab8ef2f8c1d27eee20d0b5e7fce6f7354)
- [bt_rfcomm_dlc_ops::connected](../bluetooth_service_model_reference/P156_bt_rfcomm_dlc_ops_结构体.md#aba1719c36e7a1dc9705994bcdf134e28)
- [bt_rfcomm_dlc::ops](../bluetooth_service_model_reference/P155_bt_rfcomm_dlc_结构体.md#a0054c0b539b947688555b5663c585bb7)
- [bt_rfcomm_dlc::mtu](../bluetooth_service_model_reference/P155_bt_rfcomm_dlc_结构体.md#a2334abbaacad9b98c2cb2c5650644854)
- [bt_rfcomm_dlc::rx_credit_limit](../bluetooth_service_model_reference/P155_bt_rfcomm_dlc_结构体.md#a27157f693d91aac6aaafe1bd70593404)
- [bt_rfcomm_dlc::required_sec_level](../bluetooth_service_model_reference/P155_bt_rfcomm_dlc_结构体.md#ab298ebd444566533018eabdc5a69c8ba)
- [bt_rfcomm_rpn::param_mask](../bluetooth_service_model_reference/P157_bt_rfcomm_rpn_结构体.md#a9eaac13558a5be2fed82084e0bb7a20a)
- [bt_rfcomm_rpn::baud_rate](../bluetooth_service_model_reference/P157_bt_rfcomm_rpn_结构体.md#aad2f64edcb82e864293869474d20fa81)
- [bt_rfcomm_rpn::line_settings](../bluetooth_service_model_reference/P157_bt_rfcomm_rpn_结构体.md#acd61f81d3de1fe4da58fd5ee0d4e5e77)
- [bt_rfcomm_rpn::xoff_char](../bluetooth_service_model_reference/P157_bt_rfcomm_rpn_结构体.md#adc651e1ac74d616fd03b07a647139296)
- [bt_rfcomm_rpn::flow_control](../bluetooth_service_model_reference/P157_bt_rfcomm_rpn_结构体.md#ae0db46df73fae846cb53f8a0cf01350a)
- [bt_rfcomm_rpn::xon_char](../bluetooth_service_model_reference/P157_bt_rfcomm_rpn_结构体.md#ae637cd243e9b016231b5071e171b6b54)
- [bt_rfcomm_rpn::dlci](../bluetooth_service_model_reference/P157_bt_rfcomm_rpn_结构体.md#afacd73edbb63e3ade9573100967faffa)
- [bt_rfcomm_server::channel](../bluetooth_service_model_reference/P158_bt_rfcomm_server_结构体.md#a30b22ea64c0fdd7130e8aaa79519e776)
- [bt_rfcomm_server::accept](../bluetooth_service_model_reference/P158_bt_rfcomm_server_结构体.md#ac08708bb8161f787737962f62d3c003f)

---

[上一章](P052_renesas_ra_cgc.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P054_socket_net_mgmt.h_源码浏览.md)
