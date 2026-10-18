---
id: learning.zephyr-docs.api-source-architecture-reference.page-3
title: blob_cli.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/blob__cli_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_blob\_cli.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/blob__cli_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/blob__cli_8h.html)。

## 3.1\_原始可见代码（Source Code）

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
<a id="l00024"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="foldopen00039"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="foldopen00046"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="foldopen00055"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="foldopen00083"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="foldopen00110"></a>
<a id="l00110"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="foldopen00145"></a>
<a id="l00145"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="foldopen00169"></a>
<a id="l00169"></a>
<a id="l00171"></a>
<a id="l00173"></a>
<a id="l00175"></a>
<a id="l00177"></a>
<a id="l00179"></a>
<a id="l00181"></a>
<a id="l00183"></a>
<a id="l00185"></a>
<a id="l00187"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="foldopen00196"></a>
<a id="l00196"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00269"></a>
<a id="l00271"></a>
<a id="l00273"></a>
<a id="l00278"></a>
<a id="l00282"></a>
<a id="l00284"></a>
<a id="l00286"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00295"></a>
<a id="l00297"></a>
<a id="foldopen00299"></a>
<a id="l00299"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00315"></a>
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
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="l00350"></a>
<a id="l00351"></a>
<a id="l00352"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="l00385"></a>
<a id="l00386"></a>
<a id="l00393"></a>
<a id="l00394"></a>
<a id="l00399"></a>
<a id="l00400"></a>
<a id="l00413"></a>
<a id="l00414"></a>
<a id="l00415"></a>
<a id="l00422"></a>
<a id="l00423"></a>
<a id="l00431"></a>
<a id="l00432"></a>
<a id="l00447"></a>
<a id="l00448"></a>
<a id="l00450"></a>
<a id="l00451"></a>
<a id="l00453"></a>
<a id="l00455"></a>
<a id="l00456"></a>
<a id="l00457"></a>
<a id="l00458"></a>
<a id="l00459"></a>
<a id="l00460"></a>
<a id="aaccess_8h_html"></a>
<a id="ablob_8h_html"></a>
<a id="agroup__bt__mesh__blob__cli_html_ga047e0cd9817b2ff0a241b2ccfad2acf6"></a>
<a id="agroup__bt__mesh__blob__cli_html_ga065196837cbf9d2626b5589ce2671441"></a>
<a id="agroup__bt__mesh__blob__cli_html_ga17a73cb313dbfc6652b4bcf638b9a30f"></a>
<a id="agroup__bt__mesh__blob__cli_html_ga222c650657e9a7958b119d4dddd55783"></a>
<a id="agroup__bt__mesh__blob__cli_html_ga37bbc559b48ea8cfe7cb3ddf8cad24da"></a>
<a id="agroup__bt__mesh__blob__cli_html_ga5aed01e812215d153fdfafd6375cc453"></a>
<a id="agroup__bt__mesh__blob__cli_html_ga708e4afb3d9e1d6a8fb02d8fd5ab78c2"></a>
<a id="agroup__bt__mesh__blob__cli_html_ga78487f10fae6c87edaaf4e6ec8f7362c"></a>
<a id="agroup__bt__mesh__blob__cli_html_gac401336775dc6274450d5e27ea1cd720"></a>
<a id="agroup__bt__mesh__blob__cli_html_gac86db11f09e53adb2e012bf9e446d073"></a>
<a id="agroup__bt__mesh__blob__cli_html_ggac86db11f09e53adb2e012bf9e446d073a18e10582c69e8f41416bf6833bd0db3c"></a>
<a id="agroup__bt__mesh__blob__cli_html_ggac86db11f09e53adb2e012bf9e446d073a39701bbca32d8e5604209ea9bfed4f67"></a>
<a id="agroup__bt__mesh__blob__cli_html_ggac86db11f09e53adb2e012bf9e446d073a4914077b12568211537a0861e7c2c646"></a>
<a id="agroup__bt__mesh__blob__cli_html_ggac86db11f09e53adb2e012bf9e446d073a62af740ae63c6fae5c57497cdb39e5de"></a>
<a id="agroup__bt__mesh__blob__cli_html_ggac86db11f09e53adb2e012bf9e446d073a7dd8ce9317e067084e9810b2fd8210d9"></a>
<a id="agroup__bt__mesh__blob__cli_html_ggac86db11f09e53adb2e012bf9e446d073a83147e88a189abaea6276d2e48817ba2"></a>
<a id="agroup__bt__mesh__blob__cli_html_ggac86db11f09e53adb2e012bf9e446d073aa4f4df9bf0f1e3e2ef976ce56373dd96"></a>
<a id="agroup__bt__mesh__blob__cli_html_ggac86db11f09e53adb2e012bf9e446d073adb4647d56ef152bde695eda6931df7c9"></a>
<a id="agroup__bt__mesh__blob__cli_html_ggac86db11f09e53adb2e012bf9e446d073aeb4ee8f592692287b13a5e973d12413c"></a>
<a id="agroup__bt__mesh__blob__cli_html_ggac86db11f09e53adb2e012bf9e446d073afd1a1426dd70e55f37ab822154d6cbb2"></a>
<a id="agroup__bt__mesh__blob_html_ga26ed2c64bae03758a8a53b28052d0f81"></a>
<a id="agroup__bt__mesh__blob_html_ga4e1ea17e8a8ffd42f62d64286ddc576e"></a>
<a id="agroup__bt__mesh__blob_html_ga7b5e2895a6577103a8a680a94ee7776d"></a>
<a id="agroup__bt__mesh__blob_html_gae0cb28c0e50d02f6e003062457053618"></a>
<a id="agroup__single-linked-list__apis_html_ga44658c336b634c03938a251cdc8134f8"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="agroup__sys-util_html_gae664e7492e37d324831caf2321ddda37"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html"></a>
<a id="aposix_2sys_2socket_8h_html_a16485de18b1ec93572e5d74b4a04e42f"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_ac714c0d2c1a4adb10e73cab29623314b"></a>
<a id="astructbt__mesh__blob__block_html"></a>
<a id="astructbt__mesh__blob__cli__caps_html"></a>
<a id="astructbt__mesh__blob__cli__caps_html_a1c848a3a2a2ece3764df5cbf6cbfec6b"></a>
<a id="astructbt__mesh__blob__cli__caps_html_a318c96b89597dfdf9b68fbc8b999af11"></a>
<a id="astructbt__mesh__blob__cli__caps_html_a5d44b3b9bf7e47af2e6ba930b2826b15"></a>
<a id="astructbt__mesh__blob__cli__caps_html_a89d6e1bbc55086cee410835edd6baf3a"></a>
<a id="astructbt__mesh__blob__cli__caps_html_ac446317efdeca9edbb7df924d4e5a995"></a>
<a id="astructbt__mesh__blob__cli__caps_html_ad149164240e7c20a57a28c25109079df"></a>
<a id="astructbt__mesh__blob__cli__caps_html_ae16411b1a36854d6f638a2bca1dc4c3b"></a>
<a id="astructbt__mesh__blob__cli__cb_html"></a>
<a id="astructbt__mesh__blob__cli__cb_html_a154a3308167eda4cd93ac28e379c52bc"></a>
<a id="astructbt__mesh__blob__cli__cb_html_a26a5ebe87db105900b150f71d770234d"></a>
<a id="astructbt__mesh__blob__cli__cb_html_a4b01ef0ab0a367739a75751b57149546"></a>
<a id="astructbt__mesh__blob__cli__cb_html_a58e749cadeb464299495ee74456c592c"></a>
<a id="astructbt__mesh__blob__cli__cb_html_a60bc49eab376b055a8c21099f86fdde7"></a>
<a id="astructbt__mesh__blob__cli__cb_html_abb4a4d4d24bef076aad7ae56b08d23ed"></a>
<a id="astructbt__mesh__blob__cli__inputs_html"></a>
<a id="astructbt__mesh__blob__cli__inputs_html_a30fd3cd7a6df07f6aa90b85cdc6aea18"></a>
<a id="astructbt__mesh__blob__cli__inputs_html_a7fb308f895c57b66b50e1ab060228cb3"></a>
<a id="astructbt__mesh__blob__cli__inputs_html_a835a539b307c659f57da6c20e9223ed1"></a>
<a id="astructbt__mesh__blob__cli__inputs_html_ac204e179c2a6ea9cb672fc3c2f9ab017"></a>
<a id="astructbt__mesh__blob__cli__inputs_html_adee5ecdba3adc4fe598483b1a160cafb"></a>
<a id="astructbt__mesh__blob__cli_html"></a>
<a id="astructbt__mesh__blob__cli_html_a1778ae8975ed4b9bc67616e5a0bdf3a9"></a>
<a id="astructbt__mesh__blob__cli_html_a21b064cceace34605e42d5c295f12cd5"></a>
<a id="astructbt__mesh__blob__cli_html_a2ffd91b68c0aab92f16d9fb4eac79f9d"></a>
<a id="astructbt__mesh__blob__cli_html_a388183549ed5b1af0d2ac09263611a33"></a>
<a id="astructbt__mesh__blob__cli_html_a49f0d79d76aaea785a5ad9160be40e8a"></a>
<a id="astructbt__mesh__blob__cli_html_a519aa0aa7aa66ca67cdf813fee1632c3"></a>
<a id="astructbt__mesh__blob__cli_html_a645fdb1f0efb281b1faae4692a3404f1"></a>
<a id="astructbt__mesh__blob__cli_html_a6a0229165fe19af03a26e5cffa1e1486"></a>
<a id="astructbt__mesh__blob__cli_html_a6d70ac26b7fec22dfdc21f479d867ef7"></a>
<a id="astructbt__mesh__blob__cli_html_a850cc6f4426fec9dc9066953a1b992c8"></a>
<a id="astructbt__mesh__blob__cli_html_a850d232b04118d7564537dc6763a476c"></a>
<a id="astructbt__mesh__blob__cli_html_a85fdd17b04a06e880f20a0e2b1319ff0"></a>
<a id="astructbt__mesh__blob__cli_html_a9185cdadba15bce7b2bf2fcc6f85904a"></a>
<a id="astructbt__mesh__blob__cli_html_aa6c79f5476f96a35c731b63723b2c6cc"></a>
<a id="astructbt__mesh__blob__cli_html_aa7713e6ad0183d18946646df7a5cb6ab"></a>
<a id="astructbt__mesh__blob__cli_html_aafaf644e30e10a8ad9ca6dc8b680eff6"></a>
<a id="astructbt__mesh__blob__cli_html_aafe943fcada25f32b9a31b8d7586032a"></a>
<a id="astructbt__mesh__blob__cli_html_ab131637681a0cf0b3ceebad015b28726"></a>
<a id="astructbt__mesh__blob__cli_html_ab291086be3d9ecf03becd4200d783835"></a>
<a id="astructbt__mesh__blob__cli_html_ac95970f7fd6b00fca284121394110250"></a>
<a id="astructbt__mesh__blob__cli_html_ada23952593d2a498ed421895828f461f"></a>
<a id="astructbt__mesh__blob__cli_html_add07e03f13b276fafabeb9cc4ba94d32"></a>
<a id="astructbt__mesh__blob__io_html"></a>
<a id="astructbt__mesh__blob__target__pull_html"></a>
<a id="astructbt__mesh__blob__target__pull_html_a4c43698926ba22eb43e4f92bb874ca46"></a>
<a id="astructbt__mesh__blob__target__pull_html_a9234ee3246890285b5cd30c32866b718"></a>
<a id="astructbt__mesh__blob__target_html"></a>
<a id="astructbt__mesh__blob__target_html_a0498f23d640af4b006398d5482fbaa53"></a>
<a id="astructbt__mesh__blob__target_html_a3e14f4518ee054754dfa50d8070c1725"></a>
<a id="astructbt__mesh__blob__target_html_a4eef4809023e8d4a4ee8beece5e83160"></a>
<a id="astructbt__mesh__blob__target_html_a62b5a5be44d52ebf09421de57933459d"></a>
<a id="astructbt__mesh__blob__target_html_a711a031e841bb54c4985d02a81c6846a"></a>
<a id="astructbt__mesh__blob__target_html_a7aa1066dbeee5ba4a5be5aa14d61d4d1"></a>
<a id="astructbt__mesh__blob__target_html_ab4c032f92a4ec12e4bbd6fa84139c085"></a>
<a id="astructbt__mesh__blob__target_html_aca0f3cabb5c457cfb11a4bc71c3bea85"></a>
<a id="astructbt__mesh__blob__xfer__info_html"></a>
<a id="astructbt__mesh__blob__xfer__info_html_a3a19a5f387b53dd32429c9e76e53a87f"></a>
<a id="astructbt__mesh__blob__xfer__info_html_a6a8686872018ceb6e4e9fc52eaff5b9e"></a>
<a id="astructbt__mesh__blob__xfer__info_html_a6cbb21582332cb23125624db5a02731a"></a>
<a id="astructbt__mesh__blob__xfer__info_html_a8825fba3258805db956b099ddfa19f9f"></a>
<a id="astructbt__mesh__blob__xfer__info_html_aaeda1f5688bfb3cc3708e3797f3190a5"></a>
<a id="astructbt__mesh__blob__xfer__info_html_ac03d3ad7a618ee67f9bd7f1d52019cb7"></a>
<a id="astructbt__mesh__blob__xfer__info_html_ad09a0e80202b4953788fcade5788f0ef"></a>
<a id="astructbt__mesh__blob__xfer__info_html_ae24ed28faaef6187850cb0f04da2b8c7"></a>
<a id="astructbt__mesh__blob__xfer_html"></a>
<a id="astructbt__mesh__model__cb_html"></a>
<a id="astructbt__mesh__model__op_html"></a>
<a id="astructbt__mesh__model_html"></a>
<a id="astructk__work__delayable_html"></a>

```c
/*
 * Copyright (c) 2020 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_BLUETOOTH_MESH_BLOB_CLI_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_MESH_BLOB_CLI_H_

#include <sys/types.h>

#include <zephyr/bluetooth/mesh/access.h>
#include <zephyr/bluetooth/mesh/blob.h>

#ifdef __cplusplus
extern "C" {
#endif


struct bt_mesh_blob_cli;

#define BT_MESH_MODEL_BLOB_CLI(_cli)                                           \
        BT_MESH_MODEL_CB(BT_MESH_MODEL_ID_BLOB_CLI, _bt_mesh_blob_cli_op,      \
                         NULL, _cli, &_bt_mesh_blob_cli_cb)

struct bt_mesh_blob_target_pull {
        int64_t block_report_timestamp;

        uint8_t missing[DIV_ROUND_UP(CONFIG_BT_MESH_BLOB_CHUNK_COUNT_MAX, 8)];
};

struct bt_mesh_blob_target {
        sys_snode_t n;

        uint16_t addr;

        struct bt_mesh_blob_target_pull *pull;

        uint8_t status;

        uint8_t procedure_complete:1, /* Procedure has been completed. */
                acked:1,              /* Message has been acknowledged. Not used when sending. */
                timedout:1,           /* Target node didn't respond after specified timeout. */
                skip:1;               /* Skip Target node from broadcast. */
};

struct bt_mesh_blob_xfer_info {
        enum bt_mesh_blob_status status;

        enum bt_mesh_blob_xfer_mode mode;

        enum bt_mesh_blob_xfer_phase phase;

        uint64_t id;

        uint32_t size;

        uint8_t block_size_log;

        uint16_t mtu_size;

        const uint8_t *missing_blocks;
};

struct bt_mesh_blob_cli_inputs {
        sys_slist_t targets;

        uint16_t app_idx;

        uint16_t group;

        uint8_t ttl;

        uint16_t timeout_base;
};

struct bt_mesh_blob_cli_caps {
        size_t max_size;

        uint8_t min_block_size_log;

        uint8_t max_block_size_log;

        uint16_t max_chunks;

        uint16_t max_chunk_size;

        uint16_t mtu_size;

        enum bt_mesh_blob_xfer_mode modes;
};

enum bt_mesh_blob_cli_state {
        BT_MESH_BLOB_CLI_STATE_NONE,
        BT_MESH_BLOB_CLI_STATE_CAPS_GET,
        BT_MESH_BLOB_CLI_STATE_START,
        BT_MESH_BLOB_CLI_STATE_BLOCK_START,
        BT_MESH_BLOB_CLI_STATE_BLOCK_SEND,
        BT_MESH_BLOB_CLI_STATE_BLOCK_CHECK,
        BT_MESH_BLOB_CLI_STATE_XFER_CHECK,
        BT_MESH_BLOB_CLI_STATE_CANCEL,
        BT_MESH_BLOB_CLI_STATE_SUSPENDED,
        BT_MESH_BLOB_CLI_STATE_XFER_PROGRESS_GET,
};

struct bt_mesh_blob_cli_cb {
        void (*caps)(struct bt_mesh_blob_cli *cli,
                     const struct bt_mesh_blob_cli_caps *caps);

        void (*lost_target)(struct bt_mesh_blob_cli *cli,
                            struct bt_mesh_blob_target *target,
                            enum bt_mesh_blob_status reason);

        void (*suspended)(struct bt_mesh_blob_cli *cli);

        void (*end)(struct bt_mesh_blob_cli *cli,
                    const struct bt_mesh_blob_xfer *xfer, bool success);

        void (*xfer_progress)(struct bt_mesh_blob_cli *cli,
                              struct bt_mesh_blob_target *target,
                              const struct bt_mesh_blob_xfer_info *info);

        void (*xfer_progress_complete)(struct bt_mesh_blob_cli *cli);
};

struct blob_cli_broadcast_ctx {
        void (*send)(struct bt_mesh_blob_cli *cli, uint16_t dst);
        void (*send_complete)(struct bt_mesh_blob_cli *cli, uint16_t dst);
        void (*next)(struct bt_mesh_blob_cli *cli);
        bool acked;
        bool force_unicast;
        bool optional;
        bool is_inited;
        /* Defines a time in ms by which the broadcast API postpones sending the message to a next
         * target or completing the broadcast.
         */
        uint32_t post_send_delay_ms;
};

struct bt_mesh_blob_cli {
        const struct bt_mesh_blob_cli_cb *cb;

        /* Runtime state */
        const struct bt_mesh_model *mod;

        struct {
                struct bt_mesh_blob_target *target;
                struct blob_cli_broadcast_ctx ctx;
                struct k_work_delayable retry;
                /* Represents Client Timeout timer in a timestamp. Used in Pull mode only. */
                int64_t cli_timestamp;
                struct k_work_delayable complete;
                uint16_t pending;
                uint8_t retries;
                uint8_t sending : 1,
                        cancelled : 1;
        } tx;

        const struct bt_mesh_blob_io *io;
        const struct bt_mesh_blob_cli_inputs *inputs;
        const struct bt_mesh_blob_xfer *xfer;
        uint32_t chunk_interval_ms;
        uint16_t block_count;
        uint16_t chunk_idx;
        uint16_t mtu_size;
        enum bt_mesh_blob_cli_state state;
        struct bt_mesh_blob_block block;
        struct bt_mesh_blob_cli_caps caps;
};

int bt_mesh_blob_cli_caps_get(struct bt_mesh_blob_cli *cli,
                              const struct bt_mesh_blob_cli_inputs *inputs);

int bt_mesh_blob_cli_send(struct bt_mesh_blob_cli *cli,
                          const struct bt_mesh_blob_cli_inputs *inputs,
                          const struct bt_mesh_blob_xfer *xfer,
                          const struct bt_mesh_blob_io *io);

int bt_mesh_blob_cli_suspend(struct bt_mesh_blob_cli *cli);

int bt_mesh_blob_cli_resume(struct bt_mesh_blob_cli *cli);

void bt_mesh_blob_cli_cancel(struct bt_mesh_blob_cli *cli);

int bt_mesh_blob_cli_xfer_progress_get(struct bt_mesh_blob_cli *cli,
                                       const struct bt_mesh_blob_cli_inputs *inputs);

uint8_t bt_mesh_blob_cli_xfer_progress_active_get(struct bt_mesh_blob_cli *cli);

bool bt_mesh_blob_cli_is_busy(struct bt_mesh_blob_cli *cli);

void bt_mesh_blob_cli_set_chunk_interval_ms(struct bt_mesh_blob_cli *cli, uint32_t interval_ms);

extern const struct bt_mesh_model_op _bt_mesh_blob_cli_op[];
extern const struct bt_mesh_model_cb _bt_mesh_blob_cli_cb;


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_MESH_BLOB_CLI_H_ */
```

## 3.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 70 行

过程（Procedure）已经完成。

### 注释 3：原第 71 行

消息（Message）已确认（Acknowledged）；发送时不使用。

### 注释 4：原第 72 行

目标节点（Target Node）在指定超时（Timeout）后仍未响应。

### 注释 5：原第 73 行

广播（Broadcast）时跳过目标节点（Target Node）。

### 注释 6：原第 291 行

定义广播 API 延后向下一个目标（Target）发送消息或完成广播（Broadcast）的时间，单位为毫秒（ms）。

### 注释 7：原第 303 行

运行时状态（Runtime state）。

### 注释 8：原第 310 行

以时间戳（Timestamp）表示客户端超时定时器（Client Timeout Timer）；仅在拉取模式（Pull Mode）下使用。

### 注释 9：原第 460 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_MESH_BLOB_CLI_H_`。

## 3.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/blob__cli_8h.html)
- [sys/types.h](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md)
- [zephyr/bluetooth/mesh/access.h](https://docs.zephyrproject.org/latest/doxygen/html/access_8h.html)
- [zephyr/bluetooth/mesh/blob.h](../api_file_runtime_reference/P004_zephyr__bluetooth__mesh__blob.h_文件参考.md)
- [bt_mesh_blob_cli](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md)
- [bt_mesh_blob_target_pull](../bluetooth_mesh_model_reference/P013_bt_mesh_blob_target_pull_结构体.md)
- [int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)
- [block_report_timestamp](../bluetooth_mesh_model_reference/P013_bt_mesh_blob_target_pull_结构体.md#a9234ee3246890285b5cd30c32866b718)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [missing](../bluetooth_mesh_model_reference/P013_bt_mesh_blob_target_pull_结构体.md#a4c43698926ba22eb43e4f92bb874ca46)
- [DIV_ROUND_UP](../util_reference/P001_通用工具公共接口.md#gae664e7492e37d324831caf2321ddda37)
- [CONFIG_BT_MESH_BLOB_CHUNK_COUNT_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#ga4e1ea17e8a8ffd42f62d64286ddc576e)
- [bt_mesh_blob_target](../bluetooth_mesh_model_reference/P012_bt_mesh_blob_target_结构体.md)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [n](../bluetooth_mesh_model_reference/P012_bt_mesh_blob_target_结构体.md#aca0f3cabb5c457cfb11a4bc71c3bea85)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [addr](../bluetooth_mesh_model_reference/P012_bt_mesh_blob_target_结构体.md#ab4c032f92a4ec12e4bbd6fa84139c085)
- [pull](../bluetooth_mesh_model_reference/P012_bt_mesh_blob_target_结构体.md#a0498f23d640af4b006398d5482fbaa53)
- [status](../bluetooth_mesh_model_reference/P012_bt_mesh_blob_target_结构体.md#a62b5a5be44d52ebf09421de57933459d)
- [procedure_complete](../bluetooth_mesh_model_reference/P012_bt_mesh_blob_target_结构体.md#a711a031e841bb54c4985d02a81c6846a)
- [acked](../bluetooth_mesh_model_reference/P012_bt_mesh_blob_target_结构体.md#a4eef4809023e8d4a4ee8beece5e83160)
- [timedout](../bluetooth_mesh_model_reference/P012_bt_mesh_blob_target_结构体.md#a3e14f4518ee054754dfa50d8070c1725)
- [skip](../bluetooth_mesh_model_reference/P012_bt_mesh_blob_target_结构体.md#a7aa1066dbeee5ba4a5be5aa14d61d4d1)
- [bt_mesh_blob_xfer_info](../bluetooth_mesh_model_reference/P015_bt_mesh_blob_xfer_info_结构体.md)
- [bt_mesh_blob_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#ga7b5e2895a6577103a8a680a94ee7776d)
- [status](../bluetooth_mesh_model_reference/P015_bt_mesh_blob_xfer_info_结构体.md#aaeda1f5688bfb3cc3708e3797f3190a5)
- [bt_mesh_blob_xfer_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gae0cb28c0e50d02f6e003062457053618)
- [mode](../bluetooth_mesh_model_reference/P015_bt_mesh_blob_xfer_info_结构体.md#a6cbb21582332cb23125624db5a02731a)
- [bt_mesh_blob_xfer_phase](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#ga26ed2c64bae03758a8a53b28052d0f81)
- [phase](../bluetooth_mesh_model_reference/P015_bt_mesh_blob_xfer_info_结构体.md#a6a8686872018ceb6e4e9fc52eaff5b9e)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [id](../bluetooth_mesh_model_reference/P015_bt_mesh_blob_xfer_info_结构体.md#a3a19a5f387b53dd32429c9e76e53a87f)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [size](../bluetooth_mesh_model_reference/P015_bt_mesh_blob_xfer_info_结构体.md#ac03d3ad7a618ee67f9bd7f1d52019cb7)
- [block_size_log](../bluetooth_mesh_model_reference/P015_bt_mesh_blob_xfer_info_结构体.md#ad09a0e80202b4953788fcade5788f0ef)
- [mtu_size](../bluetooth_mesh_model_reference/P015_bt_mesh_blob_xfer_info_结构体.md#ae24ed28faaef6187850cb0f04da2b8c7)
- [missing_blocks](../bluetooth_mesh_model_reference/P015_bt_mesh_blob_xfer_info_结构体.md#a8825fba3258805db956b099ddfa19f9f)
- [bt_mesh_blob_cli_inputs](../bluetooth_mesh_model_reference/P006_bt_mesh_blob_cli_inputs_结构体.md)
- [sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)
- [targets](../bluetooth_mesh_model_reference/P006_bt_mesh_blob_cli_inputs_结构体.md#a835a539b307c659f57da6c20e9223ed1)
- [app_idx](../bluetooth_mesh_model_reference/P006_bt_mesh_blob_cli_inputs_结构体.md#a7fb308f895c57b66b50e1ab060228cb3)
- [group](../bluetooth_mesh_model_reference/P006_bt_mesh_blob_cli_inputs_结构体.md#ac204e179c2a6ea9cb672fc3c2f9ab017)
- [ttl](../bluetooth_mesh_model_reference/P006_bt_mesh_blob_cli_inputs_结构体.md#adee5ecdba3adc4fe598483b1a160cafb)
- [timeout_base](../bluetooth_mesh_model_reference/P006_bt_mesh_blob_cli_inputs_结构体.md#a30fd3cd7a6df07f6aa90b85cdc6aea18)
- [bt_mesh_blob_cli_caps](../bluetooth_mesh_model_reference/P004_bt_mesh_blob_cli_caps_结构体.md)
- [max_size](../bluetooth_mesh_model_reference/P004_bt_mesh_blob_cli_caps_结构体.md#ae16411b1a36854d6f638a2bca1dc4c3b)
- [min_block_size_log](../bluetooth_mesh_model_reference/P004_bt_mesh_blob_cli_caps_结构体.md#ac446317efdeca9edbb7df924d4e5a995)
- [max_block_size_log](../bluetooth_mesh_model_reference/P004_bt_mesh_blob_cli_caps_结构体.md#a5d44b3b9bf7e47af2e6ba930b2826b15)
- [max_chunks](../bluetooth_mesh_model_reference/P004_bt_mesh_blob_cli_caps_结构体.md#a318c96b89597dfdf9b68fbc8b999af11)
- [max_chunk_size](../bluetooth_mesh_model_reference/P004_bt_mesh_blob_cli_caps_结构体.md#ad149164240e7c20a57a28c25109079df)
- [mtu_size](../bluetooth_mesh_model_reference/P004_bt_mesh_blob_cli_caps_结构体.md#a89d6e1bbc55086cee410835edd6baf3a)
- [modes](../bluetooth_mesh_model_reference/P004_bt_mesh_blob_cli_caps_结构体.md#a1c848a3a2a2ece3764df5cbf6cbfec6b)
- [bt_mesh_blob_cli_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#gac86db11f09e53adb2e012bf9e446d073)
- [BT_MESH_BLOB_CLI_STATE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ggac86db11f09e53adb2e012bf9e446d073a39701bbca32d8e5604209ea9bfed4f67)
- [BT_MESH_BLOB_CLI_STATE_CAPS_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ggac86db11f09e53adb2e012bf9e446d073a62af740ae63c6fae5c57497cdb39e5de)
- [BT_MESH_BLOB_CLI_STATE_START](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ggac86db11f09e53adb2e012bf9e446d073a83147e88a189abaea6276d2e48817ba2)
- [BT_MESH_BLOB_CLI_STATE_BLOCK_START](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ggac86db11f09e53adb2e012bf9e446d073afd1a1426dd70e55f37ab822154d6cbb2)
- [BT_MESH_BLOB_CLI_STATE_BLOCK_SEND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ggac86db11f09e53adb2e012bf9e446d073adb4647d56ef152bde695eda6931df7c9)
- [BT_MESH_BLOB_CLI_STATE_BLOCK_CHECK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ggac86db11f09e53adb2e012bf9e446d073a18e10582c69e8f41416bf6833bd0db3c)
- [BT_MESH_BLOB_CLI_STATE_XFER_CHECK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ggac86db11f09e53adb2e012bf9e446d073aa4f4df9bf0f1e3e2ef976ce56373dd96)
- [BT_MESH_BLOB_CLI_STATE_CANCEL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ggac86db11f09e53adb2e012bf9e446d073a4914077b12568211537a0861e7c2c646)
- [BT_MESH_BLOB_CLI_STATE_SUSPENDED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ggac86db11f09e53adb2e012bf9e446d073a7dd8ce9317e067084e9810b2fd8210d9)
- [BT_MESH_BLOB_CLI_STATE_XFER_PROGRESS_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ggac86db11f09e53adb2e012bf9e446d073aeb4ee8f592692287b13a5e973d12413c)
- [bt_mesh_blob_cli_cb](../bluetooth_mesh_model_reference/P005_bt_mesh_blob_cli_cb_结构体.md)
- [caps](../bluetooth_mesh_model_reference/P005_bt_mesh_blob_cli_cb_结构体.md#a58e749cadeb464299495ee74456c592c)
- [lost_target](../bluetooth_mesh_model_reference/P005_bt_mesh_blob_cli_cb_结构体.md#a26a5ebe87db105900b150f71d770234d)
- [suspended](../bluetooth_mesh_model_reference/P005_bt_mesh_blob_cli_cb_结构体.md#a154a3308167eda4cd93ac28e379c52bc)
- [end](../bluetooth_mesh_model_reference/P005_bt_mesh_blob_cli_cb_结构体.md#a60bc49eab376b055a8c21099f86fdde7)
- [bt_mesh_blob_xfer](../bluetooth_mesh_model_reference/P014_bt_mesh_blob_xfer_结构体.md)
- [xfer_progress](../bluetooth_mesh_model_reference/P005_bt_mesh_blob_cli_cb_结构体.md#a4b01ef0ab0a367739a75751b57149546)
- [xfer_progress_complete](../bluetooth_mesh_model_reference/P005_bt_mesh_blob_cli_cb_结构体.md#abb4a4d4d24bef076aad7ae56b08d23ed)
- [send](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#a16485de18b1ec93572e5d74b4a04e42f)
- [cb](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md#a6a0229165fe19af03a26e5cffa1e1486)
- [bt_mesh_model](../bluetooth_mesh_model_reference/P075_bt_mesh_model_结构体.md)
- [mod](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md#ada23952593d2a498ed421895828f461f)
- [target](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md#a519aa0aa7aa66ca67cdf813fee1632c3)
- [ctx](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md#a850d232b04118d7564537dc6763a476c)
- [k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)
- [retry](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md#add07e03f13b276fafabeb9cc4ba94d32)
- [cli_timestamp](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md#a850cc6f4426fec9dc9066953a1b992c8)
- [complete](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md#a21b064cceace34605e42d5c295f12cd5)
- [pending](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md#a1778ae8975ed4b9bc67616e5a0bdf3a9)
- [retries](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md#ab291086be3d9ecf03becd4200d783835)
- [sending](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md#a85fdd17b04a06e880f20a0e2b1319ff0)
- [cancelled](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md#a6d70ac26b7fec22dfdc21f479d867ef7)
- [tx](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md#a388183549ed5b1af0d2ac09263611a33)
- [bt_mesh_blob_io](../bluetooth_mesh_model_reference/P007_bt_mesh_blob_io_结构体.md)
- [io](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md#a49f0d79d76aaea785a5ad9160be40e8a)
- [inputs](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md#aa6c79f5476f96a35c731b63723b2c6cc)
- [xfer](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md#a9185cdadba15bce7b2bf2fcc6f85904a)
- [chunk_interval_ms](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md#a2ffd91b68c0aab92f16d9fb4eac79f9d)
- [block_count](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md#a645fdb1f0efb281b1faae4692a3404f1)
- [chunk_idx](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md#aafaf644e30e10a8ad9ca6dc8b680eff6)
- [mtu_size](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md#aafe943fcada25f32b9a31b8d7586032a)
- [state](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md#ab131637681a0cf0b3ceebad015b28726)
- [bt_mesh_blob_block](../bluetooth_mesh_model_reference/P001_bt_mesh_blob_block_结构体.md)
- [block](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md#ac95970f7fd6b00fca284121394110250)
- [caps](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md#aa7713e6ad0183d18946646df7a5cb6ab)
- [bt_mesh_blob_cli_caps_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#gac401336775dc6274450d5e27ea1cd720)
- [bt_mesh_blob_cli_send](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ga708e4afb3d9e1d6a8fb02d8fd5ab78c2)
- [bt_mesh_blob_cli_suspend](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ga78487f10fae6c87edaaf4e6ec8f7362c)
- [bt_mesh_blob_cli_resume](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ga5aed01e812215d153fdfafd6375cc453)
- [bt_mesh_blob_cli_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ga222c650657e9a7958b119d4dddd55783)
- [bt_mesh_blob_cli_xfer_progress_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ga17a73cb313dbfc6652b4bcf638b9a30f)
- [bt_mesh_blob_cli_xfer_progress_active_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ga065196837cbf9d2626b5589ce2671441)
- [bt_mesh_blob_cli_is_busy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ga37bbc559b48ea8cfe7cb3ddf8cad24da)
- [bt_mesh_blob_cli_set_chunk_interval_ms](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#ga047e0cd9817b2ff0a241b2ccfad2acf6)
- [bt_mesh_model_op](../bluetooth_mesh_model_reference/P078_bt_mesh_model_op_结构体.md)
- [bt_mesh_model_cb](../bluetooth_mesh_model_reference/P077_bt_mesh_model_cb_结构体.md)
- [access.h](https://docs.zephyrproject.org/latest/doxygen/html/access_8h.html)
- [blob.h](../api_file_runtime_reference/P004_zephyr__bluetooth__mesh__blob.h_文件参考.md)
- [types.h](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md)
- [bt_mesh_blob_cli_caps::modes](../bluetooth_mesh_model_reference/P004_bt_mesh_blob_cli_caps_结构体.md#a1c848a3a2a2ece3764df5cbf6cbfec6b)
- [bt_mesh_blob_cli_caps::max_chunks](../bluetooth_mesh_model_reference/P004_bt_mesh_blob_cli_caps_结构体.md#a318c96b89597dfdf9b68fbc8b999af11)
- [bt_mesh_blob_cli_caps::max_block_size_log](../bluetooth_mesh_model_reference/P004_bt_mesh_blob_cli_caps_结构体.md#a5d44b3b9bf7e47af2e6ba930b2826b15)
- [bt_mesh_blob_cli_caps::mtu_size](../bluetooth_mesh_model_reference/P004_bt_mesh_blob_cli_caps_结构体.md#a89d6e1bbc55086cee410835edd6baf3a)
- [bt_mesh_blob_cli_caps::min_block_size_log](../bluetooth_mesh_model_reference/P004_bt_mesh_blob_cli_caps_结构体.md#ac446317efdeca9edbb7df924d4e5a995)
- [bt_mesh_blob_cli_caps::max_chunk_size](../bluetooth_mesh_model_reference/P004_bt_mesh_blob_cli_caps_结构体.md#ad149164240e7c20a57a28c25109079df)
- [bt_mesh_blob_cli_caps::max_size](../bluetooth_mesh_model_reference/P004_bt_mesh_blob_cli_caps_结构体.md#ae16411b1a36854d6f638a2bca1dc4c3b)
- [bt_mesh_blob_cli_cb::suspended](../bluetooth_mesh_model_reference/P005_bt_mesh_blob_cli_cb_结构体.md#a154a3308167eda4cd93ac28e379c52bc)
- [bt_mesh_blob_cli_cb::lost_target](../bluetooth_mesh_model_reference/P005_bt_mesh_blob_cli_cb_结构体.md#a26a5ebe87db105900b150f71d770234d)
- [bt_mesh_blob_cli_cb::xfer_progress](../bluetooth_mesh_model_reference/P005_bt_mesh_blob_cli_cb_结构体.md#a4b01ef0ab0a367739a75751b57149546)
- [bt_mesh_blob_cli_cb::caps](../bluetooth_mesh_model_reference/P005_bt_mesh_blob_cli_cb_结构体.md#a58e749cadeb464299495ee74456c592c)
- [bt_mesh_blob_cli_cb::end](../bluetooth_mesh_model_reference/P005_bt_mesh_blob_cli_cb_结构体.md#a60bc49eab376b055a8c21099f86fdde7)
- [bt_mesh_blob_cli_cb::xfer_progress_complete](../bluetooth_mesh_model_reference/P005_bt_mesh_blob_cli_cb_结构体.md#abb4a4d4d24bef076aad7ae56b08d23ed)
- [bt_mesh_blob_cli_inputs::timeout_base](../bluetooth_mesh_model_reference/P006_bt_mesh_blob_cli_inputs_结构体.md#a30fd3cd7a6df07f6aa90b85cdc6aea18)
- [bt_mesh_blob_cli_inputs::app_idx](../bluetooth_mesh_model_reference/P006_bt_mesh_blob_cli_inputs_结构体.md#a7fb308f895c57b66b50e1ab060228cb3)
- [bt_mesh_blob_cli_inputs::targets](../bluetooth_mesh_model_reference/P006_bt_mesh_blob_cli_inputs_结构体.md#a835a539b307c659f57da6c20e9223ed1)
- [bt_mesh_blob_cli_inputs::group](../bluetooth_mesh_model_reference/P006_bt_mesh_blob_cli_inputs_结构体.md#ac204e179c2a6ea9cb672fc3c2f9ab017)
- [bt_mesh_blob_cli_inputs::ttl](../bluetooth_mesh_model_reference/P006_bt_mesh_blob_cli_inputs_结构体.md#adee5ecdba3adc4fe598483b1a160cafb)
- [bt_mesh_blob_cli::pending](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md#a1778ae8975ed4b9bc67616e5a0bdf3a9)
- [bt_mesh_blob_cli::complete](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md#a21b064cceace34605e42d5c295f12cd5)
- [bt_mesh_blob_cli::chunk_interval_ms](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md#a2ffd91b68c0aab92f16d9fb4eac79f9d)
- [bt_mesh_blob_cli::tx](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md#a388183549ed5b1af0d2ac09263611a33)
- [bt_mesh_blob_cli::io](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md#a49f0d79d76aaea785a5ad9160be40e8a)
- [bt_mesh_blob_cli::target](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md#a519aa0aa7aa66ca67cdf813fee1632c3)
- [bt_mesh_blob_cli::block_count](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md#a645fdb1f0efb281b1faae4692a3404f1)
- [bt_mesh_blob_cli::cb](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md#a6a0229165fe19af03a26e5cffa1e1486)
- [bt_mesh_blob_cli::cancelled](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md#a6d70ac26b7fec22dfdc21f479d867ef7)
- [bt_mesh_blob_cli::cli_timestamp](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md#a850cc6f4426fec9dc9066953a1b992c8)
- [bt_mesh_blob_cli::ctx](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md#a850d232b04118d7564537dc6763a476c)
- [bt_mesh_blob_cli::sending](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md#a85fdd17b04a06e880f20a0e2b1319ff0)
- [bt_mesh_blob_cli::xfer](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md#a9185cdadba15bce7b2bf2fcc6f85904a)
- [bt_mesh_blob_cli::inputs](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md#aa6c79f5476f96a35c731b63723b2c6cc)
- [bt_mesh_blob_cli::caps](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md#aa7713e6ad0183d18946646df7a5cb6ab)
- [bt_mesh_blob_cli::chunk_idx](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md#aafaf644e30e10a8ad9ca6dc8b680eff6)
- [bt_mesh_blob_cli::mtu_size](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md#aafe943fcada25f32b9a31b8d7586032a)
- [bt_mesh_blob_cli::state](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md#ab131637681a0cf0b3ceebad015b28726)
- [bt_mesh_blob_cli::retries](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md#ab291086be3d9ecf03becd4200d783835)
- [bt_mesh_blob_cli::block](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md#ac95970f7fd6b00fca284121394110250)
- [bt_mesh_blob_cli::mod](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md#ada23952593d2a498ed421895828f461f)
- [bt_mesh_blob_cli::retry](../bluetooth_mesh_model_reference/P003_bt_mesh_blob_cli_结构体.md#add07e03f13b276fafabeb9cc4ba94d32)
- [bt_mesh_blob_target_pull::missing](../bluetooth_mesh_model_reference/P013_bt_mesh_blob_target_pull_结构体.md#a4c43698926ba22eb43e4f92bb874ca46)
- [bt_mesh_blob_target_pull::block_report_timestamp](../bluetooth_mesh_model_reference/P013_bt_mesh_blob_target_pull_结构体.md#a9234ee3246890285b5cd30c32866b718)
- [bt_mesh_blob_target::pull](../bluetooth_mesh_model_reference/P012_bt_mesh_blob_target_结构体.md#a0498f23d640af4b006398d5482fbaa53)
- [bt_mesh_blob_target::timedout](../bluetooth_mesh_model_reference/P012_bt_mesh_blob_target_结构体.md#a3e14f4518ee054754dfa50d8070c1725)
- [bt_mesh_blob_target::acked](../bluetooth_mesh_model_reference/P012_bt_mesh_blob_target_结构体.md#a4eef4809023e8d4a4ee8beece5e83160)
- [bt_mesh_blob_target::status](../bluetooth_mesh_model_reference/P012_bt_mesh_blob_target_结构体.md#a62b5a5be44d52ebf09421de57933459d)
- [bt_mesh_blob_target::procedure_complete](../bluetooth_mesh_model_reference/P012_bt_mesh_blob_target_结构体.md#a711a031e841bb54c4985d02a81c6846a)
- [bt_mesh_blob_target::skip](../bluetooth_mesh_model_reference/P012_bt_mesh_blob_target_结构体.md#a7aa1066dbeee5ba4a5be5aa14d61d4d1)
- [bt_mesh_blob_target::addr](../bluetooth_mesh_model_reference/P012_bt_mesh_blob_target_结构体.md#ab4c032f92a4ec12e4bbd6fa84139c085)
- [bt_mesh_blob_target::n](../bluetooth_mesh_model_reference/P012_bt_mesh_blob_target_结构体.md#aca0f3cabb5c457cfb11a4bc71c3bea85)
- [bt_mesh_blob_xfer_info::id](../bluetooth_mesh_model_reference/P015_bt_mesh_blob_xfer_info_结构体.md#a3a19a5f387b53dd32429c9e76e53a87f)
- [bt_mesh_blob_xfer_info::phase](../bluetooth_mesh_model_reference/P015_bt_mesh_blob_xfer_info_结构体.md#a6a8686872018ceb6e4e9fc52eaff5b9e)
- [bt_mesh_blob_xfer_info::mode](../bluetooth_mesh_model_reference/P015_bt_mesh_blob_xfer_info_结构体.md#a6cbb21582332cb23125624db5a02731a)
- [bt_mesh_blob_xfer_info::missing_blocks](../bluetooth_mesh_model_reference/P015_bt_mesh_blob_xfer_info_结构体.md#a8825fba3258805db956b099ddfa19f9f)
- [bt_mesh_blob_xfer_info::status](../bluetooth_mesh_model_reference/P015_bt_mesh_blob_xfer_info_结构体.md#aaeda1f5688bfb3cc3708e3797f3190a5)
- [bt_mesh_blob_xfer_info::size](../bluetooth_mesh_model_reference/P015_bt_mesh_blob_xfer_info_结构体.md#ac03d3ad7a618ee67f9bd7f1d52019cb7)
- [bt_mesh_blob_xfer_info::block_size_log](../bluetooth_mesh_model_reference/P015_bt_mesh_blob_xfer_info_结构体.md#ad09a0e80202b4953788fcade5788f0ef)
- [bt_mesh_blob_xfer_info::mtu_size](../bluetooth_mesh_model_reference/P015_bt_mesh_blob_xfer_info_结构体.md#ae24ed28faaef6187850cb0f04da2b8c7)

---

[上一章](P002_b91-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P004_ch32v003-pinctrl.h_源码浏览.md)
