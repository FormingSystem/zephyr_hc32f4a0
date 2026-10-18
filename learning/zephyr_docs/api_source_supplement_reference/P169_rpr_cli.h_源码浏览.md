---
id: learning.zephyr-docs.api-source-supplement-reference.page-169
title: rpr_cli.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rpr__cli_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第169章\_rpr\_cli.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/rpr__cli_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/rpr__cli_8h.html)。

## 169.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
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
<a id="l00029"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="foldopen00045"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="foldopen00050"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="foldopen00062"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="foldopen00070"></a>
<a id="l00070"></a>
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
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00254"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="aaccess_8h_html"></a>
<a id="agroup__bt__mesh__rpr__cli_html_ga007aa9b409d1370ed04c45efccdf0408"></a>
<a id="agroup__bt__mesh__rpr__cli_html_ga03602b651a5bf1c88dac810e272ea142"></a>
<a id="agroup__bt__mesh__rpr__cli_html_ga1cfef51b2d6389fb4b125cba4d21d739"></a>
<a id="agroup__bt__mesh__rpr__cli_html_ga36de5bfca8ba9b03a99625fbc1734839"></a>
<a id="agroup__bt__mesh__rpr__cli_html_ga5ad2a2f6f0b9a3f27ef8174cd15b8818"></a>
<a id="agroup__bt__mesh__rpr__cli_html_ga934104e6ee33ba8c228fde4c68e752e1"></a>
<a id="agroup__bt__mesh__rpr__cli_html_ga93aca19586795801eefa04ffc4635533"></a>
<a id="agroup__bt__mesh__rpr__cli_html_gaa240b465a1ed5796b190d241e484d467"></a>
<a id="agroup__bt__mesh__rpr__cli_html_gaf404922f2340442490f1ab29191f43e3"></a>
<a id="agroup__bt__mesh__rpr_html_ga0266611238d10f8e97f2b07156991f43"></a>
<a id="agroup__bt__mesh__rpr_html_ga77d2f7158e7629dc54acafbf65e6af90"></a>
<a id="agroup__bt__mesh__rpr_html_gabdc6782290a2c1652156e3f932e65291"></a>
<a id="akernel_8h_html"></a>
<a id="arpr_8h_html"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructbt__mesh__model__cb_html"></a>
<a id="astructbt__mesh__model__op_html"></a>
<a id="astructbt__mesh__model_html"></a>
<a id="astructbt__mesh__msg__ack__ctx_html"></a>
<a id="astructbt__mesh__rpr__caps_html"></a>
<a id="astructbt__mesh__rpr__caps_html_a2de75ef667698a6094051a71ba9808ce"></a>
<a id="astructbt__mesh__rpr__caps_html_af14cce916d388c18ca33d4fc9adb36b5"></a>
<a id="astructbt__mesh__rpr__cli_html"></a>
<a id="astructbt__mesh__rpr__cli_html_a0e5a8d697b87f5f05bbce0aaa8c1fb1a"></a>
<a id="astructbt__mesh__rpr__cli_html_a188c9e610035b7225411b45733be5a85"></a>
<a id="astructbt__mesh__rpr__cli_html_a32b3c63218b506d1bc5759640cb3fb81"></a>
<a id="astructbt__mesh__rpr__cli_html_a64b12ca2ef9e47723c77a8af41eb0f89"></a>
<a id="astructbt__mesh__rpr__cli_html_a68eaadc451224e155227d14102ff0a54"></a>
<a id="astructbt__mesh__rpr__cli_html_a8493c4b3c1e30cc0a6f58b765adb2e37"></a>
<a id="astructbt__mesh__rpr__cli_html_a8f5eea4cbb042f8a83050ad4ebfc64b7"></a>
<a id="astructbt__mesh__rpr__cli_html_a9cc5b67937ec8e0ff93ddfb55cb11528"></a>
<a id="astructbt__mesh__rpr__cli_html_aa29cbb7e19cc659ce13b0b98604c93d5"></a>
<a id="astructbt__mesh__rpr__cli_html_ad69049681d611aa48be4942745fb89a7"></a>
<a id="astructbt__mesh__rpr__cli_html_af03b9edb0a205e92182234c7a1355e0c"></a>
<a id="astructbt__mesh__rpr__link_html"></a>
<a id="astructbt__mesh__rpr__node_html"></a>
<a id="astructbt__mesh__rpr__scan__status_html"></a>
<a id="astructbt__mesh__rpr__scan__status_html_a2e2023bc7dcb31ae8716203b726f7ebb"></a>
<a id="astructbt__mesh__rpr__scan__status_html_a8d062579fb074ded769bf367e0287052"></a>
<a id="astructbt__mesh__rpr__scan__status_html_ac7fc9a15127dc1eae44d2ec610efd5be"></a>
<a id="astructbt__mesh__rpr__scan__status_html_ac9e5f2e4db9fc9b04dddd2687a712ff8"></a>
<a id="astructbt__mesh__rpr__unprov_html"></a>
<a id="astructk__work__delayable_html"></a>
<a id="astructnet__buf__simple_html"></a>
<a id="astructuuid_html"></a>

```c
/*
 * Copyright (c) 2020 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_BLUETOOTH_MESH_RPR_CLI_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_MESH_RPR_CLI_H_

#include <zephyr/kernel.h>
#include <zephyr/bluetooth/mesh/access.h>
#include <zephyr/bluetooth/mesh/rpr.h>

#ifdef __cplusplus
extern "C" {
#endif


#define BT_MESH_RPR_SCAN_MAX_DEVS_ANY 0

struct bt_mesh_rpr_cli;

#define BT_MESH_MODEL_RPR_CLI(_cli)                                            \
        BT_MESH_MODEL_CB(BT_MESH_MODEL_ID_REMOTE_PROV_CLI,                     \
                         _bt_mesh_rpr_cli_op, NULL, _cli, &_bt_mesh_rpr_cli_cb)

struct bt_mesh_rpr_scan_status {
        enum bt_mesh_rpr_status status;
        enum bt_mesh_rpr_scan scan;
        uint8_t max_devs;
        uint8_t timeout;
};

struct bt_mesh_rpr_caps {
        uint8_t max_devs;
        bool active_scan;
};

struct bt_mesh_rpr_cli {
        void (*scan_report)(struct bt_mesh_rpr_cli *cli,
                            const struct bt_mesh_rpr_node *srv,
                            struct bt_mesh_rpr_unprov *unprov,
                            struct net_buf_simple *adv_data);

        /* Internal parameters */

        struct bt_mesh_msg_ack_ctx scan_ack_ctx;
        struct bt_mesh_msg_ack_ctx prov_ack_ctx;

        struct {
                struct k_work_delayable timeout;
                struct bt_mesh_rpr_node srv;
                uint8_t time;
                uint8_t tx_pdu;
                uint8_t rx_pdu;
                enum bt_mesh_rpr_link_state state;
        } link;

        const struct bt_mesh_model *mod;
};

int bt_mesh_rpr_scan_caps_get(struct bt_mesh_rpr_cli *cli,
                              const struct bt_mesh_rpr_node *srv,
                              struct bt_mesh_rpr_caps *caps);

int bt_mesh_rpr_scan_get(struct bt_mesh_rpr_cli *cli,
                         const struct bt_mesh_rpr_node *srv,
                         struct bt_mesh_rpr_scan_status *status);

int bt_mesh_rpr_scan_start(struct bt_mesh_rpr_cli *cli,
                           const struct bt_mesh_rpr_node *srv,
                           const uint8_t uuid[16], uint8_t timeout,
                           uint8_t max_devs,
                           struct bt_mesh_rpr_scan_status *status);

int bt_mesh_rpr_scan_start_ext(struct bt_mesh_rpr_cli *cli,
                               const struct bt_mesh_rpr_node *srv,
                               const uint8_t uuid[16], uint8_t timeout,
                               const uint8_t *ad_types, size_t ad_count);

int bt_mesh_rpr_scan_stop(struct bt_mesh_rpr_cli *cli,
                          const struct bt_mesh_rpr_node *srv,
                          struct bt_mesh_rpr_scan_status *status);

int bt_mesh_rpr_link_get(struct bt_mesh_rpr_cli *cli,
                         const struct bt_mesh_rpr_node *srv,
                         struct bt_mesh_rpr_link *rsp);

int bt_mesh_rpr_link_close(struct bt_mesh_rpr_cli *cli,
                           const struct bt_mesh_rpr_node *srv,
                           struct bt_mesh_rpr_link *rsp);

int32_t bt_mesh_rpr_cli_timeout_get(void);

void bt_mesh_rpr_cli_timeout_set(int32_t timeout);

extern const struct bt_mesh_model_op _bt_mesh_rpr_cli_op[];
extern const struct bt_mesh_model_cb _bt_mesh_rpr_cli_cb;


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_MESH_RPR_CLI_H_ */
```

## 169.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 86 行

内部参数（Internal parameters）。

### 注释 3：原第 261 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_MESH_RPR_CLI_H_`。

## 169.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/rpr__cli_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/bluetooth/mesh/access.h](https://docs.zephyrproject.org/latest/doxygen/html/access_8h.html)
- [zephyr/bluetooth/mesh/rpr.h](https://docs.zephyrproject.org/latest/doxygen/html/rpr_8h.html)
- [bt_mesh_rpr_cli](../bluetooth_mesh_model_reference/P091_bt_mesh_rpr_cli_结构体.md)
- [bt_mesh_rpr_scan_status](../bluetooth_mesh_model_reference/P094_bt_mesh_rpr_scan_status_结构体.md)
- [bt_mesh_rpr_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ga77d2f7158e7629dc54acafbf65e6af90)
- [status](../bluetooth_mesh_model_reference/P094_bt_mesh_rpr_scan_status_结构体.md#a2e2023bc7dcb31ae8716203b726f7ebb)
- [bt_mesh_rpr_scan](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gabdc6782290a2c1652156e3f932e65291)
- [scan](../bluetooth_mesh_model_reference/P094_bt_mesh_rpr_scan_status_结构体.md#ac9e5f2e4db9fc9b04dddd2687a712ff8)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [max_devs](../bluetooth_mesh_model_reference/P094_bt_mesh_rpr_scan_status_结构体.md#ac7fc9a15127dc1eae44d2ec610efd5be)
- [timeout](../bluetooth_mesh_model_reference/P094_bt_mesh_rpr_scan_status_结构体.md#a8d062579fb074ded769bf367e0287052)
- [bt_mesh_rpr_caps](../bluetooth_mesh_model_reference/P090_bt_mesh_rpr_caps_结构体.md)
- [max_devs](../bluetooth_mesh_model_reference/P090_bt_mesh_rpr_caps_结构体.md#af14cce916d388c18ca33d4fc9adb36b5)
- [active_scan](../bluetooth_mesh_model_reference/P090_bt_mesh_rpr_caps_结构体.md#a2de75ef667698a6094051a71ba9808ce)
- [scan_report](../bluetooth_mesh_model_reference/P091_bt_mesh_rpr_cli_结构体.md#a32b3c63218b506d1bc5759640cb3fb81)
- [bt_mesh_rpr_node](../bluetooth_mesh_model_reference/P093_bt_mesh_rpr_node_结构体.md)
- [srv](../bluetooth_mesh_model_reference/P091_bt_mesh_rpr_cli_结构体.md#a8f5eea4cbb042f8a83050ad4ebfc64b7)
- [bt_mesh_rpr_unprov](../bluetooth_mesh_model_reference/P095_bt_mesh_rpr_unprov_结构体.md)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [bt_mesh_msg_ack_ctx](../bluetooth_mesh_model_reference/P081_bt_mesh_msg_ack_ctx_结构体.md)
- [scan_ack_ctx](../bluetooth_mesh_model_reference/P091_bt_mesh_rpr_cli_结构体.md#a9cc5b67937ec8e0ff93ddfb55cb11528)
- [prov_ack_ctx](../bluetooth_mesh_model_reference/P091_bt_mesh_rpr_cli_结构体.md#a0e5a8d697b87f5f05bbce0aaa8c1fb1a)
- [k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)
- [timeout](../bluetooth_mesh_model_reference/P091_bt_mesh_rpr_cli_结构体.md#a64b12ca2ef9e47723c77a8af41eb0f89)
- [time](../bluetooth_mesh_model_reference/P091_bt_mesh_rpr_cli_结构体.md#af03b9edb0a205e92182234c7a1355e0c)
- [tx_pdu](../bluetooth_mesh_model_reference/P091_bt_mesh_rpr_cli_结构体.md#a68eaadc451224e155227d14102ff0a54)
- [rx_pdu](../bluetooth_mesh_model_reference/P091_bt_mesh_rpr_cli_结构体.md#a8493c4b3c1e30cc0a6f58b765adb2e37)
- [bt_mesh_rpr_link_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ga0266611238d10f8e97f2b07156991f43)
- [state](../bluetooth_mesh_model_reference/P091_bt_mesh_rpr_cli_结构体.md#aa29cbb7e19cc659ce13b0b98604c93d5)
- [link](../bluetooth_mesh_model_reference/P091_bt_mesh_rpr_cli_结构体.md#ad69049681d611aa48be4942745fb89a7)
- [bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)
- [mod](../bluetooth_mesh_model_reference/P091_bt_mesh_rpr_cli_结构体.md#a188c9e610035b7225411b45733be5a85)
- [bt_mesh_rpr_scan_caps_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr__cli.html#ga1cfef51b2d6389fb4b125cba4d21d739)
- [bt_mesh_rpr_scan_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr__cli.html#ga03602b651a5bf1c88dac810e272ea142)
- [bt_mesh_rpr_scan_start](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr__cli.html#gaf404922f2340442490f1ab29191f43e3)
- [uuid](../data_utilities/P026_UUID二进制结构.md)
- [bt_mesh_rpr_scan_start_ext](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr__cli.html#ga934104e6ee33ba8c228fde4c68e752e1)
- [bt_mesh_rpr_scan_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr__cli.html#ga007aa9b409d1370ed04c45efccdf0408)
- [bt_mesh_rpr_link_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr__cli.html#ga36de5bfca8ba9b03a99625fbc1734839)
- [bt_mesh_rpr_link](../bluetooth_mesh_model_reference/P092_bt_mesh_rpr_link_结构体.md)
- [bt_mesh_rpr_link_close](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr__cli.html#gaa240b465a1ed5796b190d241e484d467)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [bt_mesh_rpr_cli_timeout_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr__cli.html#ga93aca19586795801eefa04ffc4635533)
- [bt_mesh_rpr_cli_timeout_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr__cli.html#ga5ad2a2f6f0b9a3f27ef8174cd15b8818)
- [bt_mesh_model_op](../bluetooth_mesh_model_reference/P078_bt_mesh_model_op_结构体.md)
- [bt_mesh_model_cb](../bluetooth_mesh_model_reference/P077_bt_mesh_model_cb_结构体.md)
- [access.h](https://docs.zephyrproject.org/latest/doxygen/html/access_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [rpr.h](https://docs.zephyrproject.org/latest/doxygen/html/rpr_8h.html)
- [bt_mesh_rpr_caps::active_scan](../bluetooth_mesh_model_reference/P090_bt_mesh_rpr_caps_结构体.md#a2de75ef667698a6094051a71ba9808ce)
- [bt_mesh_rpr_caps::max_devs](../bluetooth_mesh_model_reference/P090_bt_mesh_rpr_caps_结构体.md#af14cce916d388c18ca33d4fc9adb36b5)
- [bt_mesh_rpr_cli::prov_ack_ctx](../bluetooth_mesh_model_reference/P091_bt_mesh_rpr_cli_结构体.md#a0e5a8d697b87f5f05bbce0aaa8c1fb1a)
- [bt_mesh_rpr_cli::mod](../bluetooth_mesh_model_reference/P091_bt_mesh_rpr_cli_结构体.md#a188c9e610035b7225411b45733be5a85)
- [bt_mesh_rpr_cli::scan_report](../bluetooth_mesh_model_reference/P091_bt_mesh_rpr_cli_结构体.md#a32b3c63218b506d1bc5759640cb3fb81)
- [bt_mesh_rpr_cli::timeout](../bluetooth_mesh_model_reference/P091_bt_mesh_rpr_cli_结构体.md#a64b12ca2ef9e47723c77a8af41eb0f89)
- [bt_mesh_rpr_cli::tx_pdu](../bluetooth_mesh_model_reference/P091_bt_mesh_rpr_cli_结构体.md#a68eaadc451224e155227d14102ff0a54)
- [bt_mesh_rpr_cli::rx_pdu](../bluetooth_mesh_model_reference/P091_bt_mesh_rpr_cli_结构体.md#a8493c4b3c1e30cc0a6f58b765adb2e37)
- [bt_mesh_rpr_cli::srv](../bluetooth_mesh_model_reference/P091_bt_mesh_rpr_cli_结构体.md#a8f5eea4cbb042f8a83050ad4ebfc64b7)
- [bt_mesh_rpr_cli::scan_ack_ctx](../bluetooth_mesh_model_reference/P091_bt_mesh_rpr_cli_结构体.md#a9cc5b67937ec8e0ff93ddfb55cb11528)
- [bt_mesh_rpr_cli::state](../bluetooth_mesh_model_reference/P091_bt_mesh_rpr_cli_结构体.md#aa29cbb7e19cc659ce13b0b98604c93d5)
- [bt_mesh_rpr_cli::link](../bluetooth_mesh_model_reference/P091_bt_mesh_rpr_cli_结构体.md#ad69049681d611aa48be4942745fb89a7)
- [bt_mesh_rpr_cli::time](../bluetooth_mesh_model_reference/P091_bt_mesh_rpr_cli_结构体.md#af03b9edb0a205e92182234c7a1355e0c)
- [bt_mesh_rpr_scan_status::status](../bluetooth_mesh_model_reference/P094_bt_mesh_rpr_scan_status_结构体.md#a2e2023bc7dcb31ae8716203b726f7ebb)
- [bt_mesh_rpr_scan_status::timeout](../bluetooth_mesh_model_reference/P094_bt_mesh_rpr_scan_status_结构体.md#a8d062579fb074ded769bf367e0287052)
- [bt_mesh_rpr_scan_status::max_devs](../bluetooth_mesh_model_reference/P094_bt_mesh_rpr_scan_status_结构体.md#ac7fc9a15127dc1eae44d2ec610efd5be)
- [bt_mesh_rpr_scan_status::scan](../bluetooth_mesh_model_reference/P094_bt_mesh_rpr_scan_status_结构体.md#ac9e5f2e4db9fc9b04dddd2687a712ff8)

---

[上一章](P168_rpi_pico_clock_common.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P170_rtk_publish.h_源码浏览.md)
