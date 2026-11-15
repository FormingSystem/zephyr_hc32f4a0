---
id: learning.zephyr-docs.api-source-reference.page-731
title: rpr.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rpr_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第731章\_rpr.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/rpr_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/rpr_8h.html)。

## 731.1\_原始可见代码（Source Code）

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
<a id="l00028"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="foldopen00043"></a>
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
<a id="foldopen00058"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="foldopen00064"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="foldopen00073"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="foldopen00082"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="foldopen00092"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00100"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="foldopen00109"></a>
<a id="l00109"></a>
<a id="l00111"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="agroup__bt__mesh__prov_html_gaf93f7b49dada5c3f7accc54663648e48"></a>
<a id="agroup__bt__mesh__rpr_html_ga0266611238d10f8e97f2b07156991f43"></a>
<a id="agroup__bt__mesh__rpr_html_ga77d2f7158e7629dc54acafbf65e6af90"></a>
<a id="agroup__bt__mesh__rpr_html_gabdc6782290a2c1652156e3f932e65291"></a>
<a id="agroup__bt__mesh__rpr_html_gafef25a17e477638702ed742656b59573"></a>
<a id="agroup__bt__mesh__rpr_html_gga0266611238d10f8e97f2b07156991f43a6e0002cda37a86ecc1b4eb66c3b1cee7"></a>
<a id="agroup__bt__mesh__rpr_html_gga0266611238d10f8e97f2b07156991f43a73441835adf51cd7c7cf57c36d4df4fb"></a>
<a id="agroup__bt__mesh__rpr_html_gga0266611238d10f8e97f2b07156991f43a86e13d121f282d5b8e5ee7f2cd69d494"></a>
<a id="agroup__bt__mesh__rpr_html_gga0266611238d10f8e97f2b07156991f43a8821935b6e6ea3dcf40a81c285a19c36"></a>
<a id="agroup__bt__mesh__rpr_html_gga0266611238d10f8e97f2b07156991f43aaf2850d86c8f176c1a00afd14f9f70a9"></a>
<a id="agroup__bt__mesh__rpr_html_gga77d2f7158e7629dc54acafbf65e6af90a5a0c58335ee0a2759de08c602d2922bb"></a>
<a id="agroup__bt__mesh__rpr_html_gga77d2f7158e7629dc54acafbf65e6af90a7677dece8ef7018469a30ec33b8cf9c8"></a>
<a id="agroup__bt__mesh__rpr_html_gga77d2f7158e7629dc54acafbf65e6af90a9297132714fd4a3a6e426a89da7205e3"></a>
<a id="agroup__bt__mesh__rpr_html_gga77d2f7158e7629dc54acafbf65e6af90a9375e568e9b69ab37484b91cfca75117"></a>
<a id="agroup__bt__mesh__rpr_html_gga77d2f7158e7629dc54acafbf65e6af90a97dd7c06604a54aa508ee044c3ad86e3"></a>
<a id="agroup__bt__mesh__rpr_html_gga77d2f7158e7629dc54acafbf65e6af90aa91b75cfc7e8ed3dde00fb727bb91943"></a>
<a id="agroup__bt__mesh__rpr_html_gga77d2f7158e7629dc54acafbf65e6af90ab5ff83c3503d6f709dfeb1423b957c26"></a>
<a id="agroup__bt__mesh__rpr_html_gga77d2f7158e7629dc54acafbf65e6af90abb00e5ea05d585e1350d2b46d2fdda82"></a>
<a id="agroup__bt__mesh__rpr_html_gga77d2f7158e7629dc54acafbf65e6af90aed508e4f4a7f37c7804322a44037b0b4"></a>
<a id="agroup__bt__mesh__rpr_html_gga77d2f7158e7629dc54acafbf65e6af90aedea52611aef2a72da9f41100d17edc4"></a>
<a id="agroup__bt__mesh__rpr_html_gga77d2f7158e7629dc54acafbf65e6af90aeec9abd5c000ea23fe9b7aa396f8b599"></a>
<a id="agroup__bt__mesh__rpr_html_gga77d2f7158e7629dc54acafbf65e6af90afe2ea78fee8b23c53d462f48ba530095"></a>
<a id="agroup__bt__mesh__rpr_html_ggabdc6782290a2c1652156e3f932e65291a3e732d2c256ec0c45b30b3623354c0fd"></a>
<a id="agroup__bt__mesh__rpr_html_ggabdc6782290a2c1652156e3f932e65291abb2fcc52856a2cf0b4315c253c498690"></a>
<a id="agroup__bt__mesh__rpr_html_ggabdc6782290a2c1652156e3f932e65291ad7b3cf3c950862565a8a6637448b3079"></a>
<a id="agroup__bt__mesh__rpr_html_ggafef25a17e477638702ed742656b59573a52ff469f64d554cd31ee2228c542b7bf"></a>
<a id="agroup__bt__mesh__rpr_html_ggafef25a17e477638702ed742656b59573a700c5b506c4c85d12e578c0c5e3016b6"></a>
<a id="agroup__bt__mesh__rpr_html_ggafef25a17e477638702ed742656b59573a9723efd45622d3a9ba7a2ae07dddb574"></a>
<a id="akernel_8h_html"></a>
<a id="amain_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_accbd6432732c88ad6adc5365800433b6"></a>
<a id="astructbt__mesh__rpr__link_html"></a>
<a id="astructbt__mesh__rpr__link_html_a03387a0134a1364c0c2420064960eb03"></a>
<a id="astructbt__mesh__rpr__link_html_ade33cee01b4f4d2a3a82ed868895c173"></a>
<a id="astructbt__mesh__rpr__node_html"></a>
<a id="astructbt__mesh__rpr__node_html_a10ec7b9c480513e742566c6c3b9c4973"></a>
<a id="astructbt__mesh__rpr__node_html_a2197a70aa97209a60136a09da1f513b2"></a>
<a id="astructbt__mesh__rpr__node_html_a4a73478764d4d15642475b8a822130af"></a>
<a id="astructbt__mesh__rpr__unprov_html"></a>
<a id="astructbt__mesh__rpr__unprov_html_a26ffffb174704a0a6a35418886e2a971"></a>
<a id="astructbt__mesh__rpr__unprov_html_a51e9bfeb3145c29644378d6ec5400e75"></a>
<a id="astructbt__mesh__rpr__unprov_html_a9d0103e4899b445c2c20d62749889e3e"></a>
<a id="astructbt__mesh__rpr__unprov_html_aa5fe6bad39edcb45d2e024c1c890c680"></a>
<a id="astructbt__mesh__rpr__unprov_html_ade58aed40bfaffb6f23a4e0570e370dd"></a>

```c
/*
 * Copyright (c) 2020 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_BLUETOOTH_MESH_RPR_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_MESH_RPR_H_

#include <zephyr/kernel.h>
#include <zephyr/bluetooth/mesh/main.h>

#ifdef __cplusplus
extern "C" {
#endif


#define BT_MESH_RPR_UNPROV_HASH           BIT(0)
#define BT_MESH_RPR_UNPROV_ACTIVE         BIT(1)
#define BT_MESH_RPR_UNPROV_FOUND          BIT(2)
#define BT_MESH_RPR_UNPROV_REPORTED       BIT(3)
#define BT_MESH_RPR_UNPROV_EXT            BIT(4)
#define BT_MESH_RPR_UNPROV_HAS_LINK       BIT(5)
#define BT_MESH_RPR_UNPROV_EXT_ADV_RXD    BIT(6)

#define BT_MESH_RPR_EXT_SCAN_TIME_MIN 1
#define BT_MESH_RPR_EXT_SCAN_TIME_MAX 21

enum bt_mesh_rpr_status {
        BT_MESH_RPR_SUCCESS,
        BT_MESH_RPR_ERR_SCANNING_CANNOT_START,
        BT_MESH_RPR_ERR_INVALID_STATE,
        BT_MESH_RPR_ERR_LIMITED_RESOURCES,
        BT_MESH_RPR_ERR_LINK_CANNOT_OPEN,
        BT_MESH_RPR_ERR_LINK_OPEN_FAILED,
        BT_MESH_RPR_ERR_LINK_CLOSED_BY_DEVICE,
        BT_MESH_RPR_ERR_LINK_CLOSED_BY_SERVER,
        BT_MESH_RPR_ERR_LINK_CLOSED_BY_CLIENT,
        BT_MESH_RPR_ERR_LINK_CLOSED_AS_CANNOT_RECEIVE_PDU,
        BT_MESH_RPR_ERR_LINK_CLOSED_AS_CANNOT_SEND_PDU,
        BT_MESH_RPR_ERR_LINK_CLOSED_AS_CANNOT_DELIVER_PDU_REPORT,
};

enum bt_mesh_rpr_scan {
        BT_MESH_RPR_SCAN_IDLE,
        BT_MESH_RPR_SCAN_MULTI,
        BT_MESH_RPR_SCAN_SINGLE,
};

enum bt_mesh_rpr_node_refresh {
        BT_MESH_RPR_NODE_REFRESH_DEVKEY,
        BT_MESH_RPR_NODE_REFRESH_ADDR,
        BT_MESH_RPR_NODE_REFRESH_COMPOSITION,
};

enum bt_mesh_rpr_link_state {
        BT_MESH_RPR_LINK_IDLE,
        BT_MESH_RPR_LINK_OPENING,
        BT_MESH_RPR_LINK_ACTIVE,
        BT_MESH_RPR_LINK_SENDING,
        BT_MESH_RPR_LINK_CLOSING,
};

struct bt_mesh_rpr_node {
        uint16_t addr;
        uint16_t net_idx;
        uint8_t ttl;
};

struct bt_mesh_rpr_unprov {
        uint8_t uuid[16];
        uint8_t flags;
        int8_t rssi;
        bt_mesh_prov_oob_info_t oob;
        uint32_t hash;
};

struct bt_mesh_rpr_link {
        enum bt_mesh_rpr_status status;
        enum bt_mesh_rpr_link_state state;
};


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_MESH_RPR_H_ */
```

## 731.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 122 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_MESH_RPR_H_`。

## 731.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/rpr_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/bluetooth/mesh/main.h](https://docs.zephyrproject.org/latest/doxygen/html/main_8h.html)
- [bt_mesh_rpr_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ga77d2f7158e7629dc54acafbf65e6af90)
- [BT_MESH_RPR_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga77d2f7158e7629dc54acafbf65e6af90a9375e568e9b69ab37484b91cfca75117)
- [BT_MESH_RPR_ERR_SCANNING_CANNOT_START](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga77d2f7158e7629dc54acafbf65e6af90aeec9abd5c000ea23fe9b7aa396f8b599)
- [BT_MESH_RPR_ERR_INVALID_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga77d2f7158e7629dc54acafbf65e6af90ab5ff83c3503d6f709dfeb1423b957c26)
- [BT_MESH_RPR_ERR_LIMITED_RESOURCES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga77d2f7158e7629dc54acafbf65e6af90abb00e5ea05d585e1350d2b46d2fdda82)
- [BT_MESH_RPR_ERR_LINK_CANNOT_OPEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga77d2f7158e7629dc54acafbf65e6af90a9297132714fd4a3a6e426a89da7205e3)
- [BT_MESH_RPR_ERR_LINK_OPEN_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga77d2f7158e7629dc54acafbf65e6af90aedea52611aef2a72da9f41100d17edc4)
- [BT_MESH_RPR_ERR_LINK_CLOSED_BY_DEVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga77d2f7158e7629dc54acafbf65e6af90a7677dece8ef7018469a30ec33b8cf9c8)
- [BT_MESH_RPR_ERR_LINK_CLOSED_BY_SERVER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga77d2f7158e7629dc54acafbf65e6af90afe2ea78fee8b23c53d462f48ba530095)
- [BT_MESH_RPR_ERR_LINK_CLOSED_BY_CLIENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga77d2f7158e7629dc54acafbf65e6af90a97dd7c06604a54aa508ee044c3ad86e3)
- [BT_MESH_RPR_ERR_LINK_CLOSED_AS_CANNOT_RECEIVE_PDU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga77d2f7158e7629dc54acafbf65e6af90aa91b75cfc7e8ed3dde00fb727bb91943)
- [BT_MESH_RPR_ERR_LINK_CLOSED_AS_CANNOT_SEND_PDU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga77d2f7158e7629dc54acafbf65e6af90a5a0c58335ee0a2759de08c602d2922bb)
- [BT_MESH_RPR_ERR_LINK_CLOSED_AS_CANNOT_DELIVER_PDU_REPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga77d2f7158e7629dc54acafbf65e6af90aed508e4f4a7f37c7804322a44037b0b4)
- [bt_mesh_rpr_scan](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gabdc6782290a2c1652156e3f932e65291)
- [BT_MESH_RPR_SCAN_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ggabdc6782290a2c1652156e3f932e65291ad7b3cf3c950862565a8a6637448b3079)
- [BT_MESH_RPR_SCAN_MULTI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ggabdc6782290a2c1652156e3f932e65291abb2fcc52856a2cf0b4315c253c498690)
- [BT_MESH_RPR_SCAN_SINGLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ggabdc6782290a2c1652156e3f932e65291a3e732d2c256ec0c45b30b3623354c0fd)
- [bt_mesh_rpr_node_refresh](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gafef25a17e477638702ed742656b59573)
- [BT_MESH_RPR_NODE_REFRESH_DEVKEY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ggafef25a17e477638702ed742656b59573a9723efd45622d3a9ba7a2ae07dddb574)
- [BT_MESH_RPR_NODE_REFRESH_ADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ggafef25a17e477638702ed742656b59573a52ff469f64d554cd31ee2228c542b7bf)
- [BT_MESH_RPR_NODE_REFRESH_COMPOSITION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ggafef25a17e477638702ed742656b59573a700c5b506c4c85d12e578c0c5e3016b6)
- [bt_mesh_rpr_link_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ga0266611238d10f8e97f2b07156991f43)
- [BT_MESH_RPR_LINK_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga0266611238d10f8e97f2b07156991f43a73441835adf51cd7c7cf57c36d4df4fb)
- [BT_MESH_RPR_LINK_OPENING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga0266611238d10f8e97f2b07156991f43aaf2850d86c8f176c1a00afd14f9f70a9)
- [BT_MESH_RPR_LINK_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga0266611238d10f8e97f2b07156991f43a8821935b6e6ea3dcf40a81c285a19c36)
- [BT_MESH_RPR_LINK_SENDING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga0266611238d10f8e97f2b07156991f43a6e0002cda37a86ecc1b4eb66c3b1cee7)
- [BT_MESH_RPR_LINK_CLOSING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#gga0266611238d10f8e97f2b07156991f43a86e13d121f282d5b8e5ee7f2cd69d494)
- [bt_mesh_rpr_node](../bluetooth_mesh_model_reference/P093_bt_mesh_rpr_node_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [addr](../bluetooth_mesh_model_reference/P093_bt_mesh_rpr_node_结构体.md#a10ec7b9c480513e742566c6c3b9c4973)
- [net_idx](../bluetooth_mesh_model_reference/P093_bt_mesh_rpr_node_结构体.md#a2197a70aa97209a60136a09da1f513b2)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [ttl](../bluetooth_mesh_model_reference/P093_bt_mesh_rpr_node_结构体.md#a4a73478764d4d15642475b8a822130af)
- [bt_mesh_rpr_unprov](../bluetooth_mesh_model_reference/P095_bt_mesh_rpr_unprov_结构体.md)
- [uuid](../bluetooth_mesh_model_reference/P095_bt_mesh_rpr_unprov_结构体.md#aa5fe6bad39edcb45d2e024c1c890c680)
- [flags](../bluetooth_mesh_model_reference/P095_bt_mesh_rpr_unprov_结构体.md#a9d0103e4899b445c2c20d62749889e3e)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [rssi](../bluetooth_mesh_model_reference/P095_bt_mesh_rpr_unprov_结构体.md#a26ffffb174704a0a6a35418886e2a971)
- [bt_mesh_prov_oob_info_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gaf93f7b49dada5c3f7accc54663648e48)
- [oob](../bluetooth_mesh_model_reference/P095_bt_mesh_rpr_unprov_结构体.md#a51e9bfeb3145c29644378d6ec5400e75)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [hash](../bluetooth_mesh_model_reference/P095_bt_mesh_rpr_unprov_结构体.md#ade58aed40bfaffb6f23a4e0570e370dd)
- [bt_mesh_rpr_link](../bluetooth_mesh_model_reference/P092_bt_mesh_rpr_link_结构体.md)
- [status](../bluetooth_mesh_model_reference/P092_bt_mesh_rpr_link_结构体.md#a03387a0134a1364c0c2420064960eb03)
- [state](../bluetooth_mesh_model_reference/P092_bt_mesh_rpr_link_结构体.md#ade33cee01b4f4d2a3a82ed868895c173)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [main.h](https://docs.zephyrproject.org/latest/doxygen/html/main_8h.html)
- [bt_mesh_rpr_link::status](../bluetooth_mesh_model_reference/P092_bt_mesh_rpr_link_结构体.md#a03387a0134a1364c0c2420064960eb03)
- [bt_mesh_rpr_link::state](../bluetooth_mesh_model_reference/P092_bt_mesh_rpr_link_结构体.md#ade33cee01b4f4d2a3a82ed868895c173)
- [bt_mesh_rpr_node::addr](../bluetooth_mesh_model_reference/P093_bt_mesh_rpr_node_结构体.md#a10ec7b9c480513e742566c6c3b9c4973)
- [bt_mesh_rpr_node::net_idx](../bluetooth_mesh_model_reference/P093_bt_mesh_rpr_node_结构体.md#a2197a70aa97209a60136a09da1f513b2)
- [bt_mesh_rpr_node::ttl](../bluetooth_mesh_model_reference/P093_bt_mesh_rpr_node_结构体.md#a4a73478764d4d15642475b8a822130af)
- [bt_mesh_rpr_unprov::rssi](../bluetooth_mesh_model_reference/P095_bt_mesh_rpr_unprov_结构体.md#a26ffffb174704a0a6a35418886e2a971)
- [bt_mesh_rpr_unprov::oob](../bluetooth_mesh_model_reference/P095_bt_mesh_rpr_unprov_结构体.md#a51e9bfeb3145c29644378d6ec5400e75)
- [bt_mesh_rpr_unprov::flags](../bluetooth_mesh_model_reference/P095_bt_mesh_rpr_unprov_结构体.md#a9d0103e4899b445c2c20d62749889e3e)
- [bt_mesh_rpr_unprov::uuid](../bluetooth_mesh_model_reference/P095_bt_mesh_rpr_unprov_结构体.md#aa5fe6bad39edcb45d2e024c1c890c680)
- [bt_mesh_rpr_unprov::hash](../bluetooth_mesh_model_reference/P095_bt_mesh_rpr_unprov_结构体.md#ade58aed40bfaffb6f23a4e0570e370dd)

---

[上一章](P730_rpi_pico_rp2350_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P732_rpr_srv.h_源码浏览.md)
