---
id: learning.zephyr-docs.api-source-reference.page-566
title: msg.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/msg_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第566章\_msg.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/msg_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/msg_8h.html)。

## 566.1\_原始可见代码（Source Code）

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
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="foldopen00050"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="foldopen00062"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="foldopen00072"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="foldopen00076"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="foldopen00119"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="foldopen00133"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="foldopen00143"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="foldopen00151"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="foldopen00172"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="foldopen00186"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="foldopen00197"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="foldopen00233"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="foldopen00255"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="agroup__bt__mesh__msg_html_ga1bb34a904103933140e2159cb53d49f5"></a>
<a id="agroup__bt__mesh__msg_html_ga2b054f7dc01daeef067cd3d819a7c42c"></a>
<a id="agroup__bt__mesh__msg_html_ga3da92606640cdba69a676c2a03c72311"></a>
<a id="agroup__bt__mesh__msg_html_ga83561f4d003c6c3c2b91a6afd180d1fd"></a>
<a id="agroup__bt__mesh__msg_html_ga86d3803bde26f496b7de3fa348a04525"></a>
<a id="agroup__bt__mesh__msg_html_ga974ba5d7df597a21945b75ac5919debd"></a>
<a id="agroup__bt__mesh__msg_html_gaa26850aebc9bfc97d1dafb66ba02021c"></a>
<a id="agroup__bt__mesh__msg_html_gadd25e335133fe29f234243a39f4d7626"></a>
<a id="agroup__bt__mesh__msg_html_gae10c4229cabf7774684c99154d4ed8ae"></a>
<a id="agroup__semaphore__apis_html_ga1bd12d8d8c1b9c6be9b665d0fefe5562"></a>
<a id="agroup__semaphore__apis_html_gab9be3cf1988af2cd6afdace52d497c84"></a>
<a id="agroup__semaphore__apis_html_gadcd0e6cfba3392fb887222eafe4c1845"></a>
<a id="akernel_8h_html"></a>
<a id="anet__buf_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_accbd6432732c88ad6adc5365800433b6"></a>
<a id="astructbt__mesh__model_html"></a>
<a id="astructbt__mesh__msg__ack__ctx_html"></a>
<a id="astructbt__mesh__msg__ack__ctx_html_a08f50fcae687026c45d891c9381bd9c2"></a>
<a id="astructbt__mesh__msg__ack__ctx_html_a510baede03d53b2419ade8da6d02fa10"></a>
<a id="astructbt__mesh__msg__ack__ctx_html_a53ce3e10f27da773c227de6d6eaba5e3"></a>
<a id="astructbt__mesh__msg__ack__ctx_html_ac83626299e197dbd0a9a36a6617c3b21"></a>
<a id="astructbt__mesh__msg__ctx_html"></a>
<a id="astructbt__mesh__msg__ctx_html_a106a615ce13040e99413a15ff74bb0a9"></a>
<a id="astructbt__mesh__msg__ctx_html_a1838579bb63c1976322e8eda039052db"></a>
<a id="astructbt__mesh__msg__ctx_html_a21cfb308ed8c718303bb2bc414c50753"></a>
<a id="astructbt__mesh__msg__ctx_html_a2ead7791000e9a55ed1b92c40b84bc7a"></a>
<a id="astructbt__mesh__msg__ctx_html_a43b0ebfdc3c8018a02886d93dfe2f21b"></a>
<a id="astructbt__mesh__msg__ctx_html_a548cab1ea578b29d6adf36afcf5d0299"></a>
<a id="astructbt__mesh__msg__ctx_html_a58de4d7cef6a8236a6517fc0bd961917"></a>
<a id="astructbt__mesh__msg__ctx_html_a682b192d416620a33a12b248b299b31e"></a>
<a id="astructbt__mesh__msg__ctx_html_acb5b5de55f35b37ba4f34ffc08943184"></a>
<a id="astructbt__mesh__msg__ctx_html_af8ff3238c184c541ff5417f37dd2c1e4"></a>
<a id="astructk__sem_html"></a>
<a id="astructk__timeout__t_html"></a>
<a id="astructnet__buf__simple_html"></a>

```c


/*
 * Copyright (c) 2021 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_BLUETOOTH_MESH_MSG_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_MESH_MSG_H_


#include <zephyr/kernel.h>
#include <zephyr/net_buf.h>

#ifdef __cplusplus
extern "C" {
#endif

struct bt_mesh_model;

#define BT_MESH_MIC_SHORT 4
#define BT_MESH_MIC_LONG 8

#define BT_MESH_MODEL_OP_LEN(_op) ((_op) <= 0xff ? 1 : (_op) <= 0xffff ? 2 : 3)

#define BT_MESH_MODEL_BUF_LEN(_op, _payload_len)                               \
        (BT_MESH_MODEL_OP_LEN(_op) + (_payload_len) + BT_MESH_MIC_SHORT)

#define BT_MESH_MODEL_BUF_LEN_LONG_MIC(_op, _payload_len)                      \
        (BT_MESH_MODEL_OP_LEN(_op) + (_payload_len) + BT_MESH_MIC_LONG)

#define BT_MESH_MODEL_BUF_DEFINE(_buf, _op, _payload_len)                      \
        NET_BUF_SIMPLE_DEFINE(_buf, BT_MESH_MODEL_BUF_LEN(_op, (_payload_len)))

struct bt_mesh_msg_ctx {
        uint16_t net_idx;

        uint16_t app_idx;

        uint16_t addr;

        uint16_t recv_dst;

        const uint8_t *uuid;

        int8_t  recv_rssi;

        uint8_t  recv_ttl;

        bool  send_rel;

        bool  rnd_delay;

        uint8_t  send_ttl;
};

#define BT_MESH_MSG_CTX_INIT(net_key_idx, app_key_idx, dst, ttl) \
        { \
                .net_idx = (net_key_idx), \
                .app_idx = (app_key_idx), \
                .addr = (dst), \
                .send_ttl = (ttl), \
        }

#define BT_MESH_MSG_CTX_INIT_APP(app_key_idx, dst) \
        BT_MESH_MSG_CTX_INIT(0, app_key_idx, dst, BT_MESH_TTL_DEFAULT)

#define BT_MESH_MSG_CTX_INIT_DEV(net_key_idx, dst) \
        BT_MESH_MSG_CTX_INIT(net_key_idx, BT_MESH_KEY_DEV_REMOTE, dst, BT_MESH_TTL_DEFAULT)

#define BT_MESH_MSG_CTX_INIT_PUB(pub) \
        { \
                .app_idx = (pub)->key, \
                .addr = (pub)->addr, \
                .send_ttl = (pub)->ttl, \
                .uuid = (pub)->uuid, \
        }

void bt_mesh_model_msg_init(struct net_buf_simple *msg, uint32_t opcode);

struct bt_mesh_msg_ack_ctx {
        struct k_sem          sem;
        uint32_t              op;
        uint16_t              dst;
        void                 *user_data;
};

static inline void bt_mesh_msg_ack_ctx_init(struct bt_mesh_msg_ack_ctx *ack)
{
        k_sem_init(&ack->sem, 0, 1);
}

static inline void bt_mesh_msg_ack_ctx_reset(struct bt_mesh_msg_ack_ctx *ack)
{
        k_sem_reset(&ack->sem);
}

void bt_mesh_msg_ack_ctx_clear(struct bt_mesh_msg_ack_ctx *ack);

int bt_mesh_msg_ack_ctx_prepare(struct bt_mesh_msg_ack_ctx *ack,
                                uint32_t op, uint16_t dst, void *user_data);

static inline bool bt_mesh_msg_ack_ctx_busy(struct bt_mesh_msg_ack_ctx *ack)
{
        return (ack->op != 0);
}

int bt_mesh_msg_ack_ctx_wait(struct bt_mesh_msg_ack_ctx *ack, k_timeout_t timeout);

static inline void bt_mesh_msg_ack_ctx_rx(struct bt_mesh_msg_ack_ctx *ack)
{
        k_sem_give(&ack->sem);
}

bool bt_mesh_msg_ack_ctx_match(const struct bt_mesh_msg_ack_ctx *ack,
                               uint32_t op, uint16_t addr, void **user_data);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_MESH_MSG_H_ */
```

## 566.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：© 2021 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 281 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_MESH_MSG_H_`。

## 566.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/msg_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)
- [bt_mesh_msg_ctx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_idx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md#a106a615ce13040e99413a15ff74bb0a9)
- [app_idx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md#a58de4d7cef6a8236a6517fc0bd961917)
- [addr](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md#a2ead7791000e9a55ed1b92c40b84bc7a)
- [recv_dst](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md#a682b192d416620a33a12b248b299b31e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uuid](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md#a548cab1ea578b29d6adf36afcf5d0299)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [recv_rssi](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md#a1838579bb63c1976322e8eda039052db)
- [recv_ttl](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md#af8ff3238c184c541ff5417f37dd2c1e4)
- [send_rel](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md#a21cfb308ed8c718303bb2bc414c50753)
- [rnd_delay](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md#acb5b5de55f35b37ba4f34ffc08943184)
- [send_ttl](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md#a43b0ebfdc3c8018a02886d93dfe2f21b)
- [bt_mesh_model_msg_init](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#gaa26850aebc9bfc97d1dafb66ba02021c)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bt_mesh_msg_ack_ctx](../bluetooth_mesh_model_reference/P081_bt_mesh_msg_ack_ctx_结构体.md)
- [k_sem](../synchronization_reference/P009_内核信号量结构.md)
- [sem](../bluetooth_mesh_model_reference/P081_bt_mesh_msg_ack_ctx_结构体.md#a53ce3e10f27da773c227de6d6eaba5e3)
- [op](../bluetooth_mesh_model_reference/P081_bt_mesh_msg_ack_ctx_结构体.md#a08f50fcae687026c45d891c9381bd9c2)
- [dst](../bluetooth_mesh_model_reference/P081_bt_mesh_msg_ack_ctx_结构体.md#ac83626299e197dbd0a9a36a6617c3b21)
- [user_data](../bluetooth_mesh_model_reference/P081_bt_mesh_msg_ack_ctx_结构体.md#a510baede03d53b2419ade8da6d02fa10)
- [bt_mesh_msg_ack_ctx_init](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#gadd25e335133fe29f234243a39f4d7626)
- [k_sem_init](../synchronization_reference/P008_信号量公共接口.md#gadcd0e6cfba3392fb887222eafe4c1845)
- [bt_mesh_msg_ack_ctx_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#ga86d3803bde26f496b7de3fa348a04525)
- [k_sem_reset](../synchronization_reference/P008_信号量公共接口.md#ga1bd12d8d8c1b9c6be9b665d0fefe5562)
- [bt_mesh_msg_ack_ctx_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#ga3da92606640cdba69a676c2a03c72311)
- [bt_mesh_msg_ack_ctx_prepare](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#ga1bb34a904103933140e2159cb53d49f5)
- [bt_mesh_msg_ack_ctx_busy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#ga974ba5d7df597a21945b75ac5919debd)
- [bt_mesh_msg_ack_ctx_wait](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#ga83561f4d003c6c3c2b91a6afd180d1fd)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [bt_mesh_msg_ack_ctx_rx](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#ga2b054f7dc01daeef067cd3d819a7c42c)
- [k_sem_give](../synchronization_reference/P008_信号量公共接口.md#gab9be3cf1988af2cd6afdace52d497c84)
- [bt_mesh_msg_ack_ctx_match](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__msg.html#gae10c4229cabf7774684c99154d4ed8ae)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [bt_mesh_msg_ack_ctx::op](../bluetooth_mesh_model_reference/P081_bt_mesh_msg_ack_ctx_结构体.md#a08f50fcae687026c45d891c9381bd9c2)
- [bt_mesh_msg_ack_ctx::user_data](../bluetooth_mesh_model_reference/P081_bt_mesh_msg_ack_ctx_结构体.md#a510baede03d53b2419ade8da6d02fa10)
- [bt_mesh_msg_ack_ctx::sem](../bluetooth_mesh_model_reference/P081_bt_mesh_msg_ack_ctx_结构体.md#a53ce3e10f27da773c227de6d6eaba5e3)
- [bt_mesh_msg_ack_ctx::dst](../bluetooth_mesh_model_reference/P081_bt_mesh_msg_ack_ctx_结构体.md#ac83626299e197dbd0a9a36a6617c3b21)
- [bt_mesh_msg_ctx::net_idx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md#a106a615ce13040e99413a15ff74bb0a9)
- [bt_mesh_msg_ctx::recv_rssi](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md#a1838579bb63c1976322e8eda039052db)
- [bt_mesh_msg_ctx::send_rel](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md#a21cfb308ed8c718303bb2bc414c50753)
- [bt_mesh_msg_ctx::addr](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md#a2ead7791000e9a55ed1b92c40b84bc7a)
- [bt_mesh_msg_ctx::send_ttl](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md#a43b0ebfdc3c8018a02886d93dfe2f21b)
- [bt_mesh_msg_ctx::uuid](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md#a548cab1ea578b29d6adf36afcf5d0299)
- [bt_mesh_msg_ctx::app_idx](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md#a58de4d7cef6a8236a6517fc0bd961917)
- [bt_mesh_msg_ctx::recv_dst](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md#a682b192d416620a33a12b248b299b31e)
- [bt_mesh_msg_ctx::rnd_delay](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md#acb5b5de55f35b37ba4f34ffc08943184)
- [bt_mesh_msg_ctx::recv_ttl](../bluetooth_mesh_model_reference/P082_bt_mesh_msg_ctx_结构体.md#af8ff3238c184c541ff5417f37dd2c1e4)

---

[上一章](P565_mpipe_workqueue.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P567_mspi_emul.h_源码浏览.md)
