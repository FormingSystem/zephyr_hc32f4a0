---
id: learning.zephyr-docs.api-source-supplement-reference.page-49
title: ec_host_cmd.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ec__host__cmd_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第49章\_ec\_host\_cmd.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ec__host__cmd_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ec__host__cmd_8h.html)。

## 49.1\_原始可见代码（Source Code）

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
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="foldopen00034"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="foldopen00086"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="foldopen00097"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="foldopen00131"></a>
<a id="l00131"></a>
<a id="l00133"></a>
<a id="l00135"></a>
<a id="l00137"></a>
<a id="l00142"></a>
<a id="l00144"></a>
<a id="l00149"></a>
<a id="l00151"></a>
<a id="l00153"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="foldopen00161"></a>
<a id="l00161"></a>
<a id="l00163"></a>
<a id="l00165"></a>
<a id="l00170"></a>
<a id="l00172"></a>
<a id="l00174"></a>
<a id="l00176"></a>
<a id="l00178"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="foldopen00199"></a>
<a id="l00199"></a>
<a id="l00201"></a>
<a id="l00203"></a>
<a id="l00209"></a>
<a id="l00214"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="foldopen00236"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="foldopen00257"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="foldopen00279"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="foldopen00299"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="foldopen00315"></a>
<a id="l00315"></a>
<a id="l00320"></a>
<a id="l00325"></a>
<a id="l00327"></a>
<a id="l00332"></a>
<a id="l00334"></a>
<a id="l00336"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="foldopen00346"></a>
<a id="l00346"></a>
<a id="l00348"></a>
<a id="l00353"></a>
<a id="l00355"></a>
<a id="l00357"></a>
<a id="l00359"></a>
<a id="l00360"></a>
<a id="l00361"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="l00391"></a>
<a id="l00392"></a>
<a id="l00393"></a>
<a id="l00400"></a>
<a id="l00401"></a>
<a id="l00410"></a>
<a id="l00411"></a>
<a id="l00421"></a>
<a id="l00422"></a>
<a id="l00423"></a>
<a id="l00431"></a>
<a id="l00432"></a>
<a id="l00433"></a>
<a id="l00434"></a>
<a id="l00445"></a>
<a id="l00446"></a>
<a id="l00460"></a>
<a id="l00461"></a>
<a id="l00478"></a>
<a id="l00479"></a>
<a id="l00480"></a>
<a id="l00481"></a>
<a id="l00491"></a>
<a id="l00492"></a>
<a id="l00496"></a>
<a id="l00497"></a>
<a id="abackend_8h_html"></a>
<a id="agroup__ec__host__cmd__interface_html_ga027ae23ea11a0ec7711725d1b28125d7"></a>
<a id="agroup__ec__host__cmd__interface_html_ga0af800c7a27eb6d0a35179f472a3c37e"></a>
<a id="agroup__ec__host__cmd__interface_html_ga70cbd55129ef589688c6d2f5999337c9"></a>
<a id="agroup__ec__host__cmd__interface_html_ga95f36f8cf2d21ea73bd8a36f3f7303e8"></a>
<a id="agroup__ec__host__cmd__interface_html_ga9a234157f85e06413b60682055d44fd3"></a>
<a id="agroup__ec__host__cmd__interface_html_ga9b0b87983dcc92ea55ebfa1aecf82a8f"></a>
<a id="agroup__ec__host__cmd__interface_html_ga9d8349220771fd9570432c3e3bea3066"></a>
<a id="agroup__ec__host__cmd__interface_html_ga9f734642958684ca654a3c786b2ceb74"></a>
<a id="agroup__ec__host__cmd__interface_html_gaa6ea251ee113cc15fd085ef12b76a573"></a>
<a id="agroup__ec__host__cmd__interface_html_gaaa3dc6c413b9637a3817cf82e138b27a"></a>
<a id="agroup__ec__host__cmd__interface_html_gaab1fdcb0fd13a19447d262d496b8aed9"></a>
<a id="agroup__ec__host__cmd__interface_html_gaaf267a44816e5f856db2092fca681d3e"></a>
<a id="agroup__ec__host__cmd__interface_html_gabf0f1243bf55cb70078f2a9fd0a755ec"></a>
<a id="agroup__ec__host__cmd__interface_html_gacf91301985634f9a12cd80db5e818821"></a>
<a id="agroup__ec__host__cmd__interface_html_gadbee4a2588abeb6db63f70a90b67a8fb"></a>
<a id="agroup__ec__host__cmd__interface_html_gaf3b87533037c4d865641643736904d02"></a>
<a id="agroup__ec__host__cmd__interface_html_gga70cbd55129ef589688c6d2f5999337c9a6c10f7c18f897dc5475cd4b6fcf199d6"></a>
<a id="agroup__ec__host__cmd__interface_html_gga70cbd55129ef589688c6d2f5999337c9a7b4ec42c191d5a4231a2b1551c6e45a1"></a>
<a id="agroup__ec__host__cmd__interface_html_gga70cbd55129ef589688c6d2f5999337c9a7f293daec1f211c20145b25728421d38"></a>
<a id="agroup__ec__host__cmd__interface_html_gga70cbd55129ef589688c6d2f5999337c9a8fe3708b71fbb8e82cc799dc42b7231b"></a>
<a id="agroup__ec__host__cmd__interface_html_gga70cbd55129ef589688c6d2f5999337c9a9b5eaf7f57c8fb8537995ac2cd932c81"></a>
<a id="agroup__ec__host__cmd__interface_html_gga9b0b87983dcc92ea55ebfa1aecf82a8fa20b2d8c80da5ba25bb06501eec00afa1"></a>
<a id="agroup__ec__host__cmd__interface_html_gga9b0b87983dcc92ea55ebfa1aecf82a8fa35758ca8b95b79a7c1140319164a7c00"></a>
<a id="agroup__ec__host__cmd__interface_html_gga9b0b87983dcc92ea55ebfa1aecf82a8fa370917fb952a8ed478260290dc59c985"></a>
<a id="agroup__ec__host__cmd__interface_html_gga9b0b87983dcc92ea55ebfa1aecf82a8fa3897851061e4708d98f2ca385bea1a80"></a>
<a id="agroup__ec__host__cmd__interface_html_gga9b0b87983dcc92ea55ebfa1aecf82a8fa45e8b4169e1a88afcb3be1011f2da201"></a>
<a id="agroup__ec__host__cmd__interface_html_gga9b0b87983dcc92ea55ebfa1aecf82a8fa48a29fa396646f39c6d95f28d6ce986b"></a>
<a id="agroup__ec__host__cmd__interface_html_gga9b0b87983dcc92ea55ebfa1aecf82a8fa4c242c6a48fdf8991488df445512fcc5"></a>
<a id="agroup__ec__host__cmd__interface_html_gga9b0b87983dcc92ea55ebfa1aecf82a8fa619eeb03065f2729a69c7f26c90d8c2e"></a>
<a id="agroup__ec__host__cmd__interface_html_gga9b0b87983dcc92ea55ebfa1aecf82a8fa6a6e394a69d6575caf92646a63195b4e"></a>
<a id="agroup__ec__host__cmd__interface_html_gga9b0b87983dcc92ea55ebfa1aecf82a8fa6b0ab5efe8c76a022787be84b43e1b39"></a>
<a id="agroup__ec__host__cmd__interface_html_gga9b0b87983dcc92ea55ebfa1aecf82a8fa6ba692b3ff01ab6f382e7d5e4a7dd301"></a>
<a id="agroup__ec__host__cmd__interface_html_gga9b0b87983dcc92ea55ebfa1aecf82a8fa75dc8b9ba661e52c48735ea85360e996"></a>
<a id="agroup__ec__host__cmd__interface_html_gga9b0b87983dcc92ea55ebfa1aecf82a8fa9a7bc527e81b60c2af1b3e16d17ac57e"></a>
<a id="agroup__ec__host__cmd__interface_html_gga9b0b87983dcc92ea55ebfa1aecf82a8fad43b4a713754d52b77313f2222fe2432"></a>
<a id="agroup__ec__host__cmd__interface_html_gga9b0b87983dcc92ea55ebfa1aecf82a8fad8fef524b7ccf571f7abdf8dec56fb5c"></a>
<a id="agroup__ec__host__cmd__interface_html_gga9b0b87983dcc92ea55ebfa1aecf82a8fadeacab16ecc96772c137b65352dddf26"></a>
<a id="agroup__ec__host__cmd__interface_html_gga9b0b87983dcc92ea55ebfa1aecf82a8fadeb0f80d5150733aa4f1803ee2b19fd2"></a>
<a id="agroup__ec__host__cmd__interface_html_gga9b0b87983dcc92ea55ebfa1aecf82a8fae252c89c64d8ee5d65d7e6cf42c8fe1d"></a>
<a id="agroup__ec__host__cmd__interface_html_gga9b0b87983dcc92ea55ebfa1aecf82a8fae62986949bad505a8be6c46d19b4e443"></a>
<a id="agroup__ec__host__cmd__interface_html_gga9b0b87983dcc92ea55ebfa1aecf82a8fae6cadca18d937481814ae72023d54ff5"></a>
<a id="agroup__ec__host__cmd__interface_html_gga9b0b87983dcc92ea55ebfa1aecf82a8faff7377e35d78c46ae49085488e7e71b9"></a>
<a id="agroup__ec__host__cmd__interface_html_ggabf0f1243bf55cb70078f2a9fd0a755eca009b14c05655b9ebfdfac70fc77d2e20"></a>
<a id="agroup__ec__host__cmd__interface_html_ggabf0f1243bf55cb70078f2a9fd0a755eca2e0d060db73eba1e4ecf9726868f6ed8"></a>
<a id="agroup__ec__host__cmd__interface_html_ggabf0f1243bf55cb70078f2a9fd0a755eca394e27c2841c50c94daf273712a3a7af"></a>
<a id="agroup__ec__host__cmd__interface_html_ggabf0f1243bf55cb70078f2a9fd0a755ecac766c64d188e3df91f7ed40a84a9ef46"></a>
<a id="akernel_2thread_8h_html_a6379f5a1f19ffbc262a6877c4f6e3647"></a>
<a id="akernel_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a3ea490c9b3617d4479bd80ef93cd5602"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructec__host__cmd__backend_html"></a>
<a id="astructec__host__cmd__handler__args_html"></a>
<a id="astructec__host__cmd__handler__args_html_a059b20824ece1ada2d53c7e73f49972d"></a>
<a id="astructec__host__cmd__handler__args_html_a1a6f9a7ba7faf810f7095b4c053dd3b2"></a>
<a id="astructec__host__cmd__handler__args_html_a1ac9d891b168b4db55a1829d72362ca5"></a>
<a id="astructec__host__cmd__handler__args_html_a364bda288790f65205f26310148d2888"></a>
<a id="astructec__host__cmd__handler__args_html_a7d6d622f7dd9e3b8faf928befa72f36a"></a>
<a id="astructec__host__cmd__handler__args_html_a8c7fcd1d310b0622f45458388462c9ef"></a>
<a id="astructec__host__cmd__handler__args_html_ab3eaef25fd80d0ac38b8d2eb9e40ebd4"></a>
<a id="astructec__host__cmd__handler__args_html_ad346a4c196ee5e48c67640232a828745"></a>
<a id="astructec__host__cmd__handler_html"></a>
<a id="astructec__host__cmd__handler_html_a2e4643dc7ca0ee4b8f7169b9156dadc6"></a>
<a id="astructec__host__cmd__handler_html_a4777b0c23ddf568c36ca995886cf3248"></a>
<a id="astructec__host__cmd__handler_html_aa87d559e625871f78023fcc015a02c82"></a>
<a id="astructec__host__cmd__handler_html_ad0aea63728aa9254e2a14d8cf0352b87"></a>
<a id="astructec__host__cmd__handler_html_aef233f030a30032e9dcde620c1953394"></a>
<a id="astructec__host__cmd__request__header_html"></a>
<a id="astructec__host__cmd__request__header_html_a1b4bd2b53046e29554f27dd49eb3e807"></a>
<a id="astructec__host__cmd__request__header_html_a2eb262f5fd1c7106d75feb8a5a6333a3"></a>
<a id="astructec__host__cmd__request__header_html_a2f723addb6f8aec8b2d1b02a555d7b59"></a>
<a id="astructec__host__cmd__request__header_html_a91358051660c5fa5bab1cd61991ff6b5"></a>
<a id="astructec__host__cmd__request__header_html_ad5a54882becb66008a378be28a20dd2f"></a>
<a id="astructec__host__cmd__request__header_html_afedc78b6d294f73313f9eae9ecc6a03d"></a>
<a id="astructec__host__cmd__response__header_html"></a>
<a id="astructec__host__cmd__response__header_html_a50baff1f46f56c992194c3c244897aa8"></a>
<a id="astructec__host__cmd__response__header_html_ab45cadbdafc4ab1eb5d8b1b1db2303de"></a>
<a id="astructec__host__cmd__response__header_html_ab64789cfe9fc9008aa5d88182fee9885"></a>
<a id="astructec__host__cmd__response__header_html_ac77bfd822866c9f48cec249a60eaa82b"></a>
<a id="astructec__host__cmd__response__header_html_af0abf8f0d16b2089bb4f7abaac5191af"></a>
<a id="astructec__host__cmd__rx__ctx_html"></a>
<a id="astructec__host__cmd__tx__buf_html"></a>
<a id="astructec__host__cmd_html"></a>
<a id="astructec__host__cmd_html_a0e50770725cd93b0923769b3b650b04d"></a>
<a id="astructec__host__cmd_html_a1f5153ec8442ae8c70d4918ff21b908e"></a>
<a id="astructec__host__cmd_html_a444f295157c5ada6162aea803ff219e1"></a>
<a id="astructec__host__cmd_html_a465d588b50f0a881e7f1d8b761c4288f"></a>
<a id="astructec__host__cmd_html_a642d1b4e2325be11fcb628855c89cead"></a>
<a id="astructec__host__cmd_html_a7982f079e67180de58ebd0a6f0f5d7e0"></a>
<a id="astructec__host__cmd_html_ad269f3223fc0885ba5c847b4443c993c"></a>
<a id="astructec__host__cmd_html_ad2f10eda2e6c2743d9c3068bda4deb7c"></a>
<a id="astructec__host__cmd_html_af1a3f483c1a7ddb88db187e406caa08d"></a>
<a id="astructk__sem_html"></a>
<a id="asys_2iterable__sections_8h_html"></a>

```c
/*
 * Copyright (c) 2020 Google LLC
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_MGMT_EC_HOST_CMD_EC_HOST_CMD_H_
#define ZEPHYR_INCLUDE_MGMT_EC_HOST_CMD_EC_HOST_CMD_H_


#include <stdint.h>
#include <zephyr/kernel.h>
#include <zephyr/mgmt/ec_host_cmd/backend.h>
#include <zephyr/sys/__assert.h>
#include <zephyr/sys/iterable_sections.h>

enum ec_host_cmd_status {
        EC_HOST_CMD_SUCCESS = 0,
        EC_HOST_CMD_INVALID_COMMAND = 1,
        EC_HOST_CMD_ERROR = 2,
        EC_HOST_CMD_INVALID_PARAM = 3,
        EC_HOST_CMD_ACCESS_DENIED = 4,
        EC_HOST_CMD_INVALID_RESPONSE = 5,
        EC_HOST_CMD_INVALID_VERSION = 6,
        EC_HOST_CMD_INVALID_CHECKSUM = 7,
        EC_HOST_CMD_IN_PROGRESS = 8,
        EC_HOST_CMD_UNAVAILABLE = 9,
        EC_HOST_CMD_TIMEOUT = 10,
        EC_HOST_CMD_OVERFLOW = 11,
        EC_HOST_CMD_INVALID_HEADER = 12,
        EC_HOST_CMD_REQUEST_TRUNCATED = 13,
        EC_HOST_CMD_RESPONSE_TOO_BIG = 14,
        EC_HOST_CMD_BUS_ERROR = 15,
        EC_HOST_CMD_BUSY = 16,
        EC_HOST_CMD_INVALID_HEADER_VERSION = 17,
        EC_HOST_CMD_INVALID_HEADER_CRC = 18,
        EC_HOST_CMD_INVALID_DATA_CRC = 19,
        EC_HOST_CMD_DUP_UNAVAILABLE = 20,

        EC_HOST_CMD_MAX = UINT16_MAX /* Force enum to be 16 bits */
} __packed;

enum ec_host_cmd_log_level {
        EC_HOST_CMD_DEBUG_OFF,
        EC_HOST_CMD_DEBUG_NORMAL,
        EC_HOST_CMD_DEBUG_EVERY,
        EC_HOST_CMD_DEBUG_PARAMS,
        EC_HOST_CMD_DEBUG_MODES
};

enum ec_host_cmd_state {
        EC_HOST_CMD_STATE_DISABLED = 0,
        EC_HOST_CMD_STATE_RECEIVING,
        EC_HOST_CMD_STATE_PROCESSING,
        EC_HOST_CMD_STATE_SENDING,
};

typedef void (*ec_host_cmd_user_cb_t)(const struct ec_host_cmd_rx_ctx *rx_ctx, void *user_data);

typedef enum ec_host_cmd_status (*ec_host_cmd_in_progress_cb_t)(void *user_data);

struct ec_host_cmd {
        struct ec_host_cmd_rx_ctx rx_ctx;
        struct ec_host_cmd_tx_buf tx;
        struct ec_host_cmd_backend *backend;
        struct k_sem rx_ready;
        enum ec_host_cmd_status rx_status;
        ec_host_cmd_user_cb_t user_cb;
        void *user_data;
        enum ec_host_cmd_state state;
        k_tid_t thread;
};

struct ec_host_cmd_handler_args {
        void *reserved;
        uint16_t command;
        uint8_t version;
        const void *input_buf;
        uint16_t input_buf_size;
        void *output_buf;
        uint16_t output_buf_max;
        uint16_t output_buf_size;
};

typedef enum ec_host_cmd_status (*ec_host_cmd_handler_cb)(struct ec_host_cmd_handler_args *args);

struct ec_host_cmd_handler {
        ec_host_cmd_handler_cb handler;
        uint16_t id;
        uint16_t version_mask;
        uint16_t min_rqt_size;
        uint16_t min_rsp_size;
};

#define EC_HOST_CMD_HANDLER(_id, _function, _version_mask, _request_type, _response_type)          \
        const STRUCT_SECTION_ITERABLE(ec_host_cmd_handler, __cmd_##_id) = {                        \
                .handler = _function,                                                              \
                .id = _id,                                                                         \
                .version_mask = _version_mask,                                                     \
                .min_rqt_size = sizeof(_request_type),                                             \
                .min_rsp_size = sizeof(_response_type),                                            \
        }

#define EC_HOST_CMD_HANDLER_REQ_ONLY(_id, _function, _version_mask, _request_type)                 \
        const STRUCT_SECTION_ITERABLE(ec_host_cmd_handler, __cmd_##_id) = {                        \
                .handler = _function,                                                              \
                .id = _id,                                                                         \
                .version_mask = _version_mask,                                                     \
                .min_rqt_size = sizeof(_request_type),                                             \
                .min_rsp_size = 0,                                                                 \
        }

#define EC_HOST_CMD_HANDLER_RESP_ONLY(_id, _function, _version_mask, _response_type)               \
        const STRUCT_SECTION_ITERABLE(ec_host_cmd_handler, __cmd_##_id) = {                        \
                .handler = _function,                                                              \
                .id = _id,                                                                         \
                .version_mask = _version_mask,                                                     \
                .min_rqt_size = 0,                                                                 \
                .min_rsp_size = sizeof(_response_type),                                            \
        }

#define EC_HOST_CMD_HANDLER_UNBOUND(_id, _function, _version_mask)                                 \
        const STRUCT_SECTION_ITERABLE(ec_host_cmd_handler, __cmd_##_id) = {                        \
                .handler = _function,                                                              \
                .id = _id,                                                                         \
                .version_mask = _version_mask,                                                     \
                .min_rqt_size = 0,                                                                 \
                .min_rsp_size = 0,                                                                 \
        }

struct ec_host_cmd_request_header {
        uint8_t prtcl_ver;
        uint8_t checksum;
        uint16_t cmd_id;
        uint8_t cmd_ver;
        uint8_t reserved;
        uint16_t data_len;
} __packed;

struct ec_host_cmd_response_header {
        uint8_t prtcl_ver;
        uint8_t checksum;
        uint16_t result;
        uint16_t data_len;
        uint16_t reserved;
} __packed;

int ec_host_cmd_init(struct ec_host_cmd_backend *backend);

int ec_host_cmd_send_response(enum ec_host_cmd_status status,
                              const struct ec_host_cmd_handler_args *args);

void ec_host_cmd_rx_notify(void);

void ec_host_cmd_set_user_cb(ec_host_cmd_user_cb_t cb, void *user_data);

const struct ec_host_cmd *ec_host_cmd_get_hc(void);

#ifndef CONFIG_EC_HOST_CMD_DEDICATED_THREAD
FUNC_NORETURN void ec_host_cmd_task(void);
#endif

#if defined(CONFIG_EC_HOST_CMD_IN_PROGRESS_STATUS) || defined(__DOXYGEN__)
bool ec_host_cmd_send_in_progress_ended(void);

enum ec_host_cmd_status ec_host_cmd_send_in_progress_status(void);

enum ec_host_cmd_status ec_host_cmd_send_in_progress_continue(ec_host_cmd_in_progress_cb_t cb,
                                                              void *user_data);
#endif /* CONFIG_EC_HOST_CMD_IN_PROGRESS_STATUS */

int ec_host_cmd_add_suppressed(uint16_t cmd_id);


#endif /* ZEPHYR_INCLUDE_MGMT_EC_HOST_CMD_EC_HOST_CMD_H_ */
```

## 49.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 Google LLC。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 79 行

强制枚举（Enum）为 16 位。

### 注释 3：原第 480 行

条件编译配置（Configuration）标记：`CONFIG_EC_HOST_CMD_IN_PROGRESS_STATUS`。

### 注释 4：原第 497 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MGMT_EC_HOST_CMD_EC_HOST_CMD_H_`。

## 49.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ec__host__cmd_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/mgmt/ec_host_cmd/backend.h](https://docs.zephyrproject.org/latest/doxygen/html/backend_8h.html)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [ec_host_cmd_status](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ga9b0b87983dcc92ea55ebfa1aecf82a8f)
- [EC_HOST_CMD_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fa6a6e394a69d6575caf92646a63195b4e)
- [EC_HOST_CMD_INVALID_COMMAND](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fad43b4a713754d52b77313f2222fe2432)
- [EC_HOST_CMD_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fa45e8b4169e1a88afcb3be1011f2da201)
- [EC_HOST_CMD_INVALID_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fae252c89c64d8ee5d65d7e6cf42c8fe1d)
- [EC_HOST_CMD_ACCESS_DENIED](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fad8fef524b7ccf571f7abdf8dec56fb5c)
- [EC_HOST_CMD_INVALID_RESPONSE](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8faff7377e35d78c46ae49085488e7e71b9)
- [EC_HOST_CMD_INVALID_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fa6b0ab5efe8c76a022787be84b43e1b39)
- [EC_HOST_CMD_INVALID_CHECKSUM](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fa6ba692b3ff01ab6f382e7d5e4a7dd301)
- [EC_HOST_CMD_IN_PROGRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fa619eeb03065f2729a69c7f26c90d8c2e)
- [EC_HOST_CMD_UNAVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fa75dc8b9ba661e52c48735ea85360e996)
- [EC_HOST_CMD_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fadeacab16ecc96772c137b65352dddf26)
- [EC_HOST_CMD_OVERFLOW](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fae62986949bad505a8be6c46d19b4e443)
- [EC_HOST_CMD_INVALID_HEADER](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fa48a29fa396646f39c6d95f28d6ce986b)
- [EC_HOST_CMD_REQUEST_TRUNCATED](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fa35758ca8b95b79a7c1140319164a7c00)
- [EC_HOST_CMD_RESPONSE_TOO_BIG](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fae6cadca18d937481814ae72023d54ff5)
- [EC_HOST_CMD_BUS_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fadeb0f80d5150733aa4f1803ee2b19fd2)
- [EC_HOST_CMD_BUSY](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fa20b2d8c80da5ba25bb06501eec00afa1)
- [EC_HOST_CMD_INVALID_HEADER_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fa4c242c6a48fdf8991488df445512fcc5)
- [EC_HOST_CMD_INVALID_HEADER_CRC](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fa9a7bc527e81b60c2af1b3e16d17ac57e)
- [EC_HOST_CMD_INVALID_DATA_CRC](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fa370917fb952a8ed478260290dc59c985)
- [EC_HOST_CMD_DUP_UNAVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga9b0b87983dcc92ea55ebfa1aecf82a8fa3897851061e4708d98f2ca385bea1a80)
- [UINT16_MAX](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3ea490c9b3617d4479bd80ef93cd5602)
- [ec_host_cmd_log_level](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ga70cbd55129ef589688c6d2f5999337c9)
- [EC_HOST_CMD_DEBUG_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga70cbd55129ef589688c6d2f5999337c9a7f293daec1f211c20145b25728421d38)
- [EC_HOST_CMD_DEBUG_NORMAL](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga70cbd55129ef589688c6d2f5999337c9a9b5eaf7f57c8fb8537995ac2cd932c81)
- [EC_HOST_CMD_DEBUG_EVERY](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga70cbd55129ef589688c6d2f5999337c9a6c10f7c18f897dc5475cd4b6fcf199d6)
- [EC_HOST_CMD_DEBUG_PARAMS](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga70cbd55129ef589688c6d2f5999337c9a7b4ec42c191d5a4231a2b1551c6e45a1)
- [EC_HOST_CMD_DEBUG_MODES](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gga70cbd55129ef589688c6d2f5999337c9a8fe3708b71fbb8e82cc799dc42b7231b)
- [ec_host_cmd_state](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gabf0f1243bf55cb70078f2a9fd0a755ec)
- [EC_HOST_CMD_STATE_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ggabf0f1243bf55cb70078f2a9fd0a755eca394e27c2841c50c94daf273712a3a7af)
- [EC_HOST_CMD_STATE_RECEIVING](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ggabf0f1243bf55cb70078f2a9fd0a755eca009b14c05655b9ebfdfac70fc77d2e20)
- [EC_HOST_CMD_STATE_PROCESSING](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ggabf0f1243bf55cb70078f2a9fd0a755eca2e0d060db73eba1e4ecf9726868f6ed8)
- [EC_HOST_CMD_STATE_SENDING](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ggabf0f1243bf55cb70078f2a9fd0a755ecac766c64d188e3df91f7ed40a84a9ef46)
- [ec_host_cmd_user_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gaa6ea251ee113cc15fd085ef12b76a573)
- [ec_host_cmd_rx_ctx](../system_service_model_reference/P014_ec_host_cmd_rx_ctx_结构体.md)
- [ec_host_cmd_in_progress_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gacf91301985634f9a12cd80db5e818821)
- [ec_host_cmd](../system_service_model_reference/P007_ec_host_cmd_结构体.md)
- [rx_ctx](../system_service_model_reference/P007_ec_host_cmd_结构体.md#a1f5153ec8442ae8c70d4918ff21b908e)
- [ec_host_cmd_tx_buf](../system_service_model_reference/P015_ec_host_cmd_tx_buf_结构体.md)
- [tx](../system_service_model_reference/P007_ec_host_cmd_结构体.md#af1a3f483c1a7ddb88db187e406caa08d)
- [ec_host_cmd_backend](../system_service_model_reference/P008_ec_host_cmd_backend_结构体.md)
- [backend](../system_service_model_reference/P007_ec_host_cmd_结构体.md#ad269f3223fc0885ba5c847b4443c993c)
- [k_sem](../synchronization_reference/P009_内核信号量结构.md)
- [rx_ready](../system_service_model_reference/P007_ec_host_cmd_结构体.md#a465d588b50f0a881e7f1d8b761c4288f)
- [rx_status](../system_service_model_reference/P007_ec_host_cmd_结构体.md#a0e50770725cd93b0923769b3b650b04d)
- [user_cb](../system_service_model_reference/P007_ec_host_cmd_结构体.md#ad2f10eda2e6c2743d9c3068bda4deb7c)
- [user_data](../system_service_model_reference/P007_ec_host_cmd_结构体.md#a7982f079e67180de58ebd0a6f0f5d7e0)
- [state](../system_service_model_reference/P007_ec_host_cmd_结构体.md#a444f295157c5ada6162aea803ff219e1)
- [k_tid_t](../thread_core_reference/P002_线程头文件参考.md#a6379f5a1f19ffbc262a6877c4f6e3647)
- [thread](../system_service_model_reference/P007_ec_host_cmd_结构体.md#a642d1b4e2325be11fcb628855c89cead)
- [ec_host_cmd_handler_args](../system_service_model_reference/P011_ec_host_cmd_handler_args_结构体.md)
- [reserved](../system_service_model_reference/P011_ec_host_cmd_handler_args_结构体.md#a8c7fcd1d310b0622f45458388462c9ef)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [command](../system_service_model_reference/P011_ec_host_cmd_handler_args_结构体.md#a059b20824ece1ada2d53c7e73f49972d)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [version](../system_service_model_reference/P011_ec_host_cmd_handler_args_结构体.md#ad346a4c196ee5e48c67640232a828745)
- [input_buf](../system_service_model_reference/P011_ec_host_cmd_handler_args_结构体.md#a364bda288790f65205f26310148d2888)
- [input_buf_size](../system_service_model_reference/P011_ec_host_cmd_handler_args_结构体.md#a7d6d622f7dd9e3b8faf928befa72f36a)
- [output_buf](../system_service_model_reference/P011_ec_host_cmd_handler_args_结构体.md#a1ac9d891b168b4db55a1829d72362ca5)
- [output_buf_max](../system_service_model_reference/P011_ec_host_cmd_handler_args_结构体.md#ab3eaef25fd80d0ac38b8d2eb9e40ebd4)
- [output_buf_size](../system_service_model_reference/P011_ec_host_cmd_handler_args_结构体.md#a1a6f9a7ba7faf810f7095b4c053dd3b2)
- [ec_host_cmd_handler_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ga027ae23ea11a0ec7711725d1b28125d7)
- [ec_host_cmd_handler](../system_service_model_reference/P010_ec_host_cmd_handler_结构体.md)
- [handler](../system_service_model_reference/P010_ec_host_cmd_handler_结构体.md#aa87d559e625871f78023fcc015a02c82)
- [id](../system_service_model_reference/P010_ec_host_cmd_handler_结构体.md#ad0aea63728aa9254e2a14d8cf0352b87)
- [version_mask](../system_service_model_reference/P010_ec_host_cmd_handler_结构体.md#a2e4643dc7ca0ee4b8f7169b9156dadc6)
- [min_rqt_size](../system_service_model_reference/P010_ec_host_cmd_handler_结构体.md#aef233f030a30032e9dcde620c1953394)
- [min_rsp_size](../system_service_model_reference/P010_ec_host_cmd_handler_结构体.md#a4777b0c23ddf568c36ca995886cf3248)
- [ec_host_cmd_request_header](../system_service_model_reference/P012_ec_host_cmd_request_header_结构体.md)
- [prtcl_ver](../system_service_model_reference/P012_ec_host_cmd_request_header_结构体.md#a2f723addb6f8aec8b2d1b02a555d7b59)
- [checksum](../system_service_model_reference/P012_ec_host_cmd_request_header_结构体.md#a91358051660c5fa5bab1cd61991ff6b5)
- [cmd_id](../system_service_model_reference/P012_ec_host_cmd_request_header_结构体.md#a1b4bd2b53046e29554f27dd49eb3e807)
- [cmd_ver](../system_service_model_reference/P012_ec_host_cmd_request_header_结构体.md#a2eb262f5fd1c7106d75feb8a5a6333a3)
- [reserved](../system_service_model_reference/P012_ec_host_cmd_request_header_结构体.md#ad5a54882becb66008a378be28a20dd2f)
- [data_len](../system_service_model_reference/P012_ec_host_cmd_request_header_结构体.md#afedc78b6d294f73313f9eae9ecc6a03d)
- [ec_host_cmd_response_header](../system_service_model_reference/P013_ec_host_cmd_response_header_结构体.md)
- [prtcl_ver](../system_service_model_reference/P013_ec_host_cmd_response_header_结构体.md#a50baff1f46f56c992194c3c244897aa8)
- [checksum](../system_service_model_reference/P013_ec_host_cmd_response_header_结构体.md#ac77bfd822866c9f48cec249a60eaa82b)
- [result](../system_service_model_reference/P013_ec_host_cmd_response_header_结构体.md#ab64789cfe9fc9008aa5d88182fee9885)
- [data_len](../system_service_model_reference/P013_ec_host_cmd_response_header_结构体.md#af0abf8f0d16b2089bb4f7abaac5191af)
- [reserved](../system_service_model_reference/P013_ec_host_cmd_response_header_结构体.md#ab45cadbdafc4ab1eb5d8b1b1db2303de)
- [ec_host_cmd_init](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gaab1fdcb0fd13a19447d262d496b8aed9)
- [ec_host_cmd_send_response](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ga95f36f8cf2d21ea73bd8a36f3f7303e8)
- [ec_host_cmd_rx_notify](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gadbee4a2588abeb6db63f70a90b67a8fb)
- [ec_host_cmd_set_user_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gaaf267a44816e5f856db2092fca681d3e)
- [ec_host_cmd_get_hc](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gaf3b87533037c4d865641643736904d02)
- [ec_host_cmd_task](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gaaa3dc6c413b9637a3817cf82e138b27a)
- [ec_host_cmd_send_in_progress_ended](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ga9a234157f85e06413b60682055d44fd3)
- [ec_host_cmd_send_in_progress_status](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ga9d8349220771fd9570432c3e3bea3066)
- [ec_host_cmd_send_in_progress_continue](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ga0af800c7a27eb6d0a35179f472a3c37e)
- [ec_host_cmd_add_suppressed](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ga9f734642958684ca654a3c786b2ceb74)
- [backend.h](https://docs.zephyrproject.org/latest/doxygen/html/backend_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [ec_host_cmd_handler_args::command](../system_service_model_reference/P011_ec_host_cmd_handler_args_结构体.md#a059b20824ece1ada2d53c7e73f49972d)
- [ec_host_cmd_handler_args::output_buf_size](../system_service_model_reference/P011_ec_host_cmd_handler_args_结构体.md#a1a6f9a7ba7faf810f7095b4c053dd3b2)
- [ec_host_cmd_handler_args::output_buf](../system_service_model_reference/P011_ec_host_cmd_handler_args_结构体.md#a1ac9d891b168b4db55a1829d72362ca5)
- [ec_host_cmd_handler_args::input_buf](../system_service_model_reference/P011_ec_host_cmd_handler_args_结构体.md#a364bda288790f65205f26310148d2888)
- [ec_host_cmd_handler_args::input_buf_size](../system_service_model_reference/P011_ec_host_cmd_handler_args_结构体.md#a7d6d622f7dd9e3b8faf928befa72f36a)
- [ec_host_cmd_handler_args::reserved](../system_service_model_reference/P011_ec_host_cmd_handler_args_结构体.md#a8c7fcd1d310b0622f45458388462c9ef)
- [ec_host_cmd_handler_args::output_buf_max](../system_service_model_reference/P011_ec_host_cmd_handler_args_结构体.md#ab3eaef25fd80d0ac38b8d2eb9e40ebd4)
- [ec_host_cmd_handler_args::version](../system_service_model_reference/P011_ec_host_cmd_handler_args_结构体.md#ad346a4c196ee5e48c67640232a828745)
- [ec_host_cmd_handler::version_mask](../system_service_model_reference/P010_ec_host_cmd_handler_结构体.md#a2e4643dc7ca0ee4b8f7169b9156dadc6)
- [ec_host_cmd_handler::min_rsp_size](../system_service_model_reference/P010_ec_host_cmd_handler_结构体.md#a4777b0c23ddf568c36ca995886cf3248)
- [ec_host_cmd_handler::handler](../system_service_model_reference/P010_ec_host_cmd_handler_结构体.md#aa87d559e625871f78023fcc015a02c82)
- [ec_host_cmd_handler::id](../system_service_model_reference/P010_ec_host_cmd_handler_结构体.md#ad0aea63728aa9254e2a14d8cf0352b87)
- [ec_host_cmd_handler::min_rqt_size](../system_service_model_reference/P010_ec_host_cmd_handler_结构体.md#aef233f030a30032e9dcde620c1953394)
- [ec_host_cmd_request_header::cmd_id](../system_service_model_reference/P012_ec_host_cmd_request_header_结构体.md#a1b4bd2b53046e29554f27dd49eb3e807)
- [ec_host_cmd_request_header::cmd_ver](../system_service_model_reference/P012_ec_host_cmd_request_header_结构体.md#a2eb262f5fd1c7106d75feb8a5a6333a3)
- [ec_host_cmd_request_header::prtcl_ver](../system_service_model_reference/P012_ec_host_cmd_request_header_结构体.md#a2f723addb6f8aec8b2d1b02a555d7b59)
- [ec_host_cmd_request_header::checksum](../system_service_model_reference/P012_ec_host_cmd_request_header_结构体.md#a91358051660c5fa5bab1cd61991ff6b5)
- [ec_host_cmd_request_header::reserved](../system_service_model_reference/P012_ec_host_cmd_request_header_结构体.md#ad5a54882becb66008a378be28a20dd2f)
- [ec_host_cmd_request_header::data_len](../system_service_model_reference/P012_ec_host_cmd_request_header_结构体.md#afedc78b6d294f73313f9eae9ecc6a03d)
- [ec_host_cmd_response_header::prtcl_ver](../system_service_model_reference/P013_ec_host_cmd_response_header_结构体.md#a50baff1f46f56c992194c3c244897aa8)
- [ec_host_cmd_response_header::reserved](../system_service_model_reference/P013_ec_host_cmd_response_header_结构体.md#ab45cadbdafc4ab1eb5d8b1b1db2303de)
- [ec_host_cmd_response_header::result](../system_service_model_reference/P013_ec_host_cmd_response_header_结构体.md#ab64789cfe9fc9008aa5d88182fee9885)
- [ec_host_cmd_response_header::checksum](../system_service_model_reference/P013_ec_host_cmd_response_header_结构体.md#ac77bfd822866c9f48cec249a60eaa82b)
- [ec_host_cmd_response_header::data_len](../system_service_model_reference/P013_ec_host_cmd_response_header_结构体.md#af0abf8f0d16b2089bb4f7abaac5191af)
- [ec_host_cmd::rx_status](../system_service_model_reference/P007_ec_host_cmd_结构体.md#a0e50770725cd93b0923769b3b650b04d)
- [ec_host_cmd::rx_ctx](../system_service_model_reference/P007_ec_host_cmd_结构体.md#a1f5153ec8442ae8c70d4918ff21b908e)
- [ec_host_cmd::state](../system_service_model_reference/P007_ec_host_cmd_结构体.md#a444f295157c5ada6162aea803ff219e1)
- [ec_host_cmd::rx_ready](../system_service_model_reference/P007_ec_host_cmd_结构体.md#a465d588b50f0a881e7f1d8b761c4288f)
- [ec_host_cmd::thread](../system_service_model_reference/P007_ec_host_cmd_结构体.md#a642d1b4e2325be11fcb628855c89cead)
- [ec_host_cmd::user_data](../system_service_model_reference/P007_ec_host_cmd_结构体.md#a7982f079e67180de58ebd0a6f0f5d7e0)
- [ec_host_cmd::backend](../system_service_model_reference/P007_ec_host_cmd_结构体.md#ad269f3223fc0885ba5c847b4443c993c)
- [ec_host_cmd::user_cb](../system_service_model_reference/P007_ec_host_cmd_结构体.md#ad2f10eda2e6c2743d9c3068bda4deb7c)
- [ec_host_cmd::tx](../system_service_model_reference/P007_ec_host_cmd_结构体.md#af1a3f483c1a7ddb88db187e406caa08d)
- [iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)

---

[上一章](P048_dummy.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P050_ene-kb106x-pinctrl.h_源码浏览.md)
