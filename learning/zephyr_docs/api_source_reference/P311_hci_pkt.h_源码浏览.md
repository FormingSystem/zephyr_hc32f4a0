---
id: learning.zephyr-docs.api-source-reference.page-311
title: hci_pkt.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/hci__pkt_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第311章\_hci\_pkt.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/hci__pkt_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/hci__pkt_8h.html)。

## 311.1\_原始可见代码（Source Code）

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
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00053"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="foldopen00091"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="foldopen00101"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="foldopen00142"></a>
<a id="l00142"></a>
<a id="l00148"></a>
<a id="l00153"></a>
<a id="l00164"></a>
<a id="l00172"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="agroup__bt__hci__pkt_html_ga5494d5cdc68840408f6b4b254dd474c9"></a>
<a id="agroup__bt__hci__pkt_html_ga588ed90a133f526c4abfa3fcd87ad8e5"></a>
<a id="agroup__bt__hci__pkt_html_ga591c10d3d94a29be93ff5c4eb690201f"></a>
<a id="agroup__bt__hci__pkt_html_ga7f6c2d3674275bb9ce6752cf3f7e3228"></a>
<a id="agroup__bt__hci__pkt_html_gac9d4ade374ccf35895cf601cdd6b3f79"></a>
<a id="ahci__types_8h_html"></a>
<a id="anet__buf_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructbt__hci__pkt__cmd__rsp_html"></a>
<a id="astructbt__hci__pkt__cmd__rsp_html_a0f381a50b06e919ee4b66d7781750ee4"></a>
<a id="astructbt__hci__pkt__cmd__rsp_html_a16a24c4f86c12dcb5fba854609b9bb96"></a>
<a id="astructbt__hci__pkt__cmd__rsp_html_a28f51c385cac564330fef45c3fca84cc"></a>
<a id="astructbt__hci__pkt__cmd__rsp_html_a2a276baa7340943d9b72ae59f85b86db"></a>
<a id="astructbt__hci__pkt__cmd__rsp_html_a51769d2ade34c7563fb30c1a31cf26b0"></a>
<a id="astructnet__buf__simple_html"></a>

```c


/*
 * Copyright (c) 2026 Silicon Laboratories Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_BLUETOOTH_HCI_PKT_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_HCI_PKT_H_

#include <stdint.h>

#include <zephyr/bluetooth/hci_types.h>
#include <zephyr/net_buf.h>

#ifdef __cplusplus
extern "C" {
#endif


#define BT_HCI_PKT_CMD_HDR_SIZE (sizeof(uint8_t) + BT_HCI_CMD_HDR_SIZE)

#define BT_HCI_PKT_CMD_SIZE(param_len) (BT_HCI_PKT_CMD_HDR_SIZE + (param_len))

#define Z_BT_HCI_PKT_CMD_DEFINE(_name, _max_param_len, _storage)                                  \
        _storage uint8_t net_buf_data_##_name[BT_HCI_PKT_CMD_SIZE(_max_param_len)];                \
        _storage struct net_buf_simple _name = {                                                   \
                .data = net_buf_data_##_name + BT_HCI_PKT_CMD_HDR_SIZE,                            \
                .len = 0,                                                                          \
                .size = BT_HCI_PKT_CMD_SIZE(_max_param_len),                                       \
                .__buf = net_buf_data_##_name,                                                     \
        }

#define BT_HCI_PKT_CMD_DEFINE(_name, _max_param_len)                                               \
        Z_BT_HCI_PKT_CMD_DEFINE(_name, _max_param_len,)

#define BT_HCI_PKT_CMD_DEFINE_STATIC(_name, _max_param_len)                                        \
        Z_BT_HCI_PKT_CMD_DEFINE(_name, _max_param_len, static)

void bt_hci_pkt_reset_cmd(struct net_buf_simple *buf);

int bt_hci_pkt_push_cmd_hdr(struct net_buf_simple *buf, uint16_t opcode);

struct bt_hci_pkt_cmd_rsp {
        uint16_t opcode;
        uint8_t ncmd;
        uint8_t status;
        const uint8_t *rp;
        size_t rp_len;
};

int bt_hci_pkt_pull_cmd_complete(struct net_buf_simple *buf, struct bt_hci_pkt_cmd_rsp *rsp);

int bt_hci_pkt_pull_cmd_status(struct net_buf_simple *buf, struct bt_hci_pkt_cmd_rsp *rsp);

int bt_hci_pkt_parse_cmd_rsp(const uint8_t *pkt, size_t len, struct bt_hci_pkt_cmd_rsp *rsp);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_HCI_PKT_H_ */
```

## 311.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：© 2026 Silicon Laboratories Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 242 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_HCI_PKT_H_`。

## 311.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/hci__pkt_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html)
- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [bt_hci_pkt_reset_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__pkt.html#ga7f6c2d3674275bb9ce6752cf3f7e3228)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [bt_hci_pkt_push_cmd_hdr](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__pkt.html#gac9d4ade374ccf35895cf601cdd6b3f79)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_hci_pkt_cmd_rsp](../bluetooth_hci_model_reference/P333_bt_hci_pkt_cmd_rsp_结构体.md)
- [opcode](../bluetooth_hci_model_reference/P333_bt_hci_pkt_cmd_rsp_结构体.md#a28f51c385cac564330fef45c3fca84cc)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [ncmd](../bluetooth_hci_model_reference/P333_bt_hci_pkt_cmd_rsp_结构体.md#a2a276baa7340943d9b72ae59f85b86db)
- [status](../bluetooth_hci_model_reference/P333_bt_hci_pkt_cmd_rsp_结构体.md#a0f381a50b06e919ee4b66d7781750ee4)
- [rp](../bluetooth_hci_model_reference/P333_bt_hci_pkt_cmd_rsp_结构体.md#a16a24c4f86c12dcb5fba854609b9bb96)
- [rp_len](../bluetooth_hci_model_reference/P333_bt_hci_pkt_cmd_rsp_结构体.md#a51769d2ade34c7563fb30c1a31cf26b0)
- [bt_hci_pkt_pull_cmd_complete](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__pkt.html#ga5494d5cdc68840408f6b4b254dd474c9)
- [bt_hci_pkt_pull_cmd_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__pkt.html#ga591c10d3d94a29be93ff5c4eb690201f)
- [bt_hci_pkt_parse_cmd_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__pkt.html#ga588ed90a133f526c4abfa3fcd87ad8e5)
- [hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html)
- [net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [bt_hci_pkt_cmd_rsp::status](../bluetooth_hci_model_reference/P333_bt_hci_pkt_cmd_rsp_结构体.md#a0f381a50b06e919ee4b66d7781750ee4)
- [bt_hci_pkt_cmd_rsp::rp](../bluetooth_hci_model_reference/P333_bt_hci_pkt_cmd_rsp_结构体.md#a16a24c4f86c12dcb5fba854609b9bb96)
- [bt_hci_pkt_cmd_rsp::opcode](../bluetooth_hci_model_reference/P333_bt_hci_pkt_cmd_rsp_结构体.md#a28f51c385cac564330fef45c3fca84cc)
- [bt_hci_pkt_cmd_rsp::ncmd](../bluetooth_hci_model_reference/P333_bt_hci_pkt_cmd_rsp_结构体.md#a2a276baa7340943d9b72ae59f85b86db)
- [bt_hci_pkt_cmd_rsp::rp_len](../bluetooth_hci_model_reference/P333_bt_hci_pkt_cmd_rsp_结构体.md#a51769d2ade34c7563fb30c1a31cf26b0)

---

[上一章](P310_hci_nxp_setup.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P312_hci_raw.h_源码浏览.md)
