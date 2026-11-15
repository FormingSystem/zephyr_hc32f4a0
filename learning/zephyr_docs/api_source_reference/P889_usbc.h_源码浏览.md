---
id: learning.zephyr-docs.api-source-reference.page-889
title: usbc.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usbc_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第889章\_usbc.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/usbc_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/usbc_8h.html)。

## 889.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
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
<a id="l00033"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="foldopen00054"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00074"></a>
<a id="l00079"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="foldopen00090"></a>
<a id="l00090"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00100"></a>
<a id="l00102"></a>
<a id="l00104"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00110"></a>
<a id="l00112"></a>
<a id="l00114"></a>
<a id="l00116"></a>
<a id="l00118"></a>
<a id="l00120"></a>
<a id="l00122"></a>
<a id="l00124"></a>
<a id="l00126"></a>
<a id="l00128"></a>
<a id="l00130"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="foldopen00138"></a>
<a id="l00138"></a>
<a id="l00140"></a>
<a id="l00142"></a>
<a id="l00144"></a>
<a id="l00146"></a>
<a id="l00148"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="foldopen00156"></a>
<a id="l00156"></a>
<a id="l00158"></a>
<a id="l00160"></a>
<a id="l00162"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="foldopen00170"></a>
<a id="l00170"></a>
<a id="l00172"></a>
<a id="l00174"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00190"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00321"></a>
<a id="l00329"></a>
<a id="l00331"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="l00348"></a>
<a id="l00349"></a>
<a id="l00358"></a>
<a id="l00359"></a>
<a id="l00361"></a>
<a id="l00369"></a>
<a id="l00370"></a>
<a id="l00372"></a>
<a id="l00379"></a>
<a id="l00380"></a>
<a id="l00389"></a>
<a id="l00390"></a>
<a id="l00397"></a>
<a id="l00398"></a>
<a id="l00405"></a>
<a id="l00406"></a>
<a id="l00413"></a>
<a id="l00414"></a>
<a id="l00422"></a>
<a id="l00423"></a>
<a id="l00431"></a>
<a id="l00432"></a>
<a id="l00439"></a>
<a id="l00440"></a>
<a id="l00448"></a>
<a id="l00449"></a>
<a id="l00456"></a>
<a id="l00457"></a>
<a id="l00465"></a>
<a id="l00466"></a>
<a id="l00467"></a>
<a id="l00475"></a>
<a id="l00476"></a>
<a id="l00483"></a>
<a id="l00484"></a>
<a id="l00492"></a>
<a id="l00493"></a>
<a id="l00500"></a>
<a id="l00501"></a>
<a id="l00502"></a>
<a id="l00509"></a>
<a id="l00510"></a>
<a id="l00511"></a>
<a id="l00518"></a>
<a id="l00519"></a>
<a id="l00520"></a>
<a id="l00528"></a>
<a id="l00529"></a>
<a id="l00530"></a>
<a id="l00537"></a>
<a id="l00538"></a>
<a id="l00539"></a>
<a id="l00543"></a>
<a id="l00544"></a>
<a id="l00545"></a>
<a id="l00546"></a>
<a id="l00547"></a>
<a id="l00548"></a>
<a id="adevice_8h_html"></a>
<a id="agroup____usbc__device__api_html_ga1535f7f53b3cc859ff536883fd631830"></a>
<a id="agroup____usbc__device__api_html_ga38a301a97a5e1a85e9836bbf083859f3"></a>
<a id="agroup____usbc__device__api_html_ga42691b0bb2b4be50147ac655e2cd9761"></a>
<a id="agroup____usbc__device__api_html_ga4536f47082f58f49d492de6f2b00dd17"></a>
<a id="agroup____usbc__device__api_html_ga4c4f0592a034b4e49eee85e95af33f94"></a>
<a id="agroup____usbc__device__api_html_ga5b4adb4330dfadf127d0a01253d722bb"></a>
<a id="agroup____usbc__device__api_html_ga66f934a5c5cd88b574c71d1f18fbda23"></a>
<a id="agroup____usbc__device__api_html_ga67a046b411134d7c631942ae6ba73fc5"></a>
<a id="agroup____usbc__device__api_html_ga68b73c03a5098a21260b5c3638edc973"></a>
<a id="agroup____usbc__device__api_html_ga7800c065ae5cfb7a95b58865d47c7f04"></a>
<a id="agroup____usbc__device__api_html_ga7c1ffea81f71416ab2942fc5a5b67d41"></a>
<a id="agroup____usbc__device__api_html_ga7f85188cc4f1a95350195abd0d736ada"></a>
<a id="agroup____usbc__device__api_html_ga8741df33b5432d9c7d5902af9bd67084"></a>
<a id="agroup____usbc__device__api_html_ga8974f9661dfebf8f686d677f999d5957"></a>
<a id="agroup____usbc__device__api_html_ga9846b36061453023e16c160f5f120159"></a>
<a id="agroup____usbc__device__api_html_ga997007cab2e54ad53b774b4215d0f593"></a>
<a id="agroup____usbc__device__api_html_gaa295593c7d5ede31328efaaab38b5880"></a>
<a id="agroup____usbc__device__api_html_gaa8f89bfb1e9a1840b2d61ebaa13aeb2f"></a>
<a id="agroup____usbc__device__api_html_gabd99b6926baf67212d65c4a4d147ce5b"></a>
<a id="agroup____usbc__device__api_html_gadf5d2934b5dc8e2b01d20bb904988784"></a>
<a id="agroup____usbc__device__api_html_gaedec1b4ad7b028ad18e1bcbe5396f1ee"></a>
<a id="agroup____usbc__device__api_html_gaf25c9cc2b6c514b9dcddc8129a76ccee"></a>
<a id="agroup____usbc__device__api_html_gaf5332ba0c87ff737e1c476d7be071fec"></a>
<a id="agroup____usbc__device__api_html_gafbd2885d758aa869635041fa89750596"></a>
<a id="agroup____usbc__device__api_html_gafd0a407558bb92dc8b7007d9d717b940"></a>
<a id="agroup____usbc__device__api_html_gafea882f4f3cc96c502d53a24a3e5aec5"></a>
<a id="agroup____usbc__device__api_html_gaffa045ee6e2fbc07fde7e84e44d3853f"></a>
<a id="agroup____usbc__device__api_html_gga38a301a97a5e1a85e9836bbf083859f3a0c5ff3bc4c0d6f636663fd3911ed85d5"></a>
<a id="agroup____usbc__device__api_html_gga38a301a97a5e1a85e9836bbf083859f3a1fe9f57fac7f5149fe5f0f7c42523536"></a>
<a id="agroup____usbc__device__api_html_gga38a301a97a5e1a85e9836bbf083859f3a2274197ac367b3da6358cac8dd781134"></a>
<a id="agroup____usbc__device__api_html_gga38a301a97a5e1a85e9836bbf083859f3a7c3c9c959439ee73539cff13e561c403"></a>
<a id="agroup____usbc__device__api_html_gga38a301a97a5e1a85e9836bbf083859f3a899633a1b63b1c3a826b5556f0f23d8b"></a>
<a id="agroup____usbc__device__api_html_gga38a301a97a5e1a85e9836bbf083859f3a8a7b77d81428f0c4784af3204f33b290"></a>
<a id="agroup____usbc__device__api_html_gga38a301a97a5e1a85e9836bbf083859f3a8c6083028ee8655cd0bebb6d9aab2e1e"></a>
<a id="agroup____usbc__device__api_html_gga38a301a97a5e1a85e9836bbf083859f3ad45120b1ceabeb054c2c2273b8431894"></a>
<a id="agroup____usbc__device__api_html_gga38a301a97a5e1a85e9836bbf083859f3ade1edc3aef0e4d563934edbc9ce784bc"></a>
<a id="agroup____usbc__device__api_html_gga38a301a97a5e1a85e9836bbf083859f3ae5b4eb0db00e81a98cfe2436b64a7018"></a>
<a id="agroup____usbc__device__api_html_gga4c4f0592a034b4e49eee85e95af33f94a714f82e830f9528a8200c2c14795b282"></a>
<a id="agroup____usbc__device__api_html_gga4c4f0592a034b4e49eee85e95af33f94a7922edb67afe83596819994a71de76dd"></a>
<a id="agroup____usbc__device__api_html_gga4c4f0592a034b4e49eee85e95af33f94a7ae46f6deb593eedd0564d30cb4c75fb"></a>
<a id="agroup____usbc__device__api_html_gga66f934a5c5cd88b574c71d1f18fbda23a0266a21d8c836cf281c30542eb6badd4"></a>
<a id="agroup____usbc__device__api_html_gga66f934a5c5cd88b574c71d1f18fbda23a0fb0676a11ad8bad2d5249031ba5fd19"></a>
<a id="agroup____usbc__device__api_html_gga66f934a5c5cd88b574c71d1f18fbda23a336bfb983c4d07684d67d4d9ef6c1489"></a>
<a id="agroup____usbc__device__api_html_gga66f934a5c5cd88b574c71d1f18fbda23a3477c1c6ad8885c3ab7a9c58b7399dcf"></a>
<a id="agroup____usbc__device__api_html_gga66f934a5c5cd88b574c71d1f18fbda23a3a27b8e70ffe5788aa3ffea1bf61cae9"></a>
<a id="agroup____usbc__device__api_html_gga66f934a5c5cd88b574c71d1f18fbda23a3a50be6f70c1a7abd724ab447491c46a"></a>
<a id="agroup____usbc__device__api_html_gga66f934a5c5cd88b574c71d1f18fbda23a4020203569dcb95ab1b3d2946efced19"></a>
<a id="agroup____usbc__device__api_html_gga66f934a5c5cd88b574c71d1f18fbda23a43bc56906b5dc4767d3297400053d286"></a>
<a id="agroup____usbc__device__api_html_gga66f934a5c5cd88b574c71d1f18fbda23a4ad0620e76c694004d3a1b43458a14b2"></a>
<a id="agroup____usbc__device__api_html_gga66f934a5c5cd88b574c71d1f18fbda23a75abb66ae57bb7ad946b8c3c2734f445"></a>
<a id="agroup____usbc__device__api_html_gga66f934a5c5cd88b574c71d1f18fbda23a791604f4f0b2a2c3ccea4e98d1659a61"></a>
<a id="agroup____usbc__device__api_html_gga66f934a5c5cd88b574c71d1f18fbda23a8cb937247ec21f791706f4f426496a8c"></a>
<a id="agroup____usbc__device__api_html_gga66f934a5c5cd88b574c71d1f18fbda23aa02158d0afdd60c755453977200dfb28"></a>
<a id="agroup____usbc__device__api_html_gga66f934a5c5cd88b574c71d1f18fbda23aa316636e8353dad1a9d5dec8b85a67e4"></a>
<a id="agroup____usbc__device__api_html_gga66f934a5c5cd88b574c71d1f18fbda23ab2f97ffaa13c84e656f7ac0004ec86ae"></a>
<a id="agroup____usbc__device__api_html_gga66f934a5c5cd88b574c71d1f18fbda23ab74f5bcaa94a5fb1e46cdd7c6a5d822f"></a>
<a id="agroup____usbc__device__api_html_gga66f934a5c5cd88b574c71d1f18fbda23ac22b0026881f65c574d0bf7454321745"></a>
<a id="agroup____usbc__device__api_html_gga66f934a5c5cd88b574c71d1f18fbda23ad52e1c4f949bb64fef1d996ac2f4e0de"></a>
<a id="agroup____usbc__device__api_html_gga66f934a5c5cd88b574c71d1f18fbda23adbefad204068244fdf75ba1ff211fbfc"></a>
<a id="agroup____usbc__device__api_html_gga66f934a5c5cd88b574c71d1f18fbda23adebcbf5155b43ce562127d4077d46d7d"></a>
<a id="agroup____usbc__device__api_html_gga66f934a5c5cd88b574c71d1f18fbda23ae0372eb6238d86c3cfb2a10764180451"></a>
<a id="agroup____usbc__device__api_html_ggadf5d2934b5dc8e2b01d20bb904988784a009ce2ceacd92db88d9a6beb01f84a28"></a>
<a id="agroup____usbc__device__api_html_ggadf5d2934b5dc8e2b01d20bb904988784a91f1f41bf9318e06c02c1957a39a762a"></a>
<a id="agroup____usbc__device__api_html_ggadf5d2934b5dc8e2b01d20bb904988784aa982aed81f39e35cde74399c6d74e601"></a>
<a id="agroup____usbc__device__api_html_ggadf5d2934b5dc8e2b01d20bb904988784ae5ef03f78d78a7014404c581bad77c18"></a>
<a id="agroup____usbc__device__api_html_ggafea882f4f3cc96c502d53a24a3e5aec5a1181a470497b797136cf0eb204394106"></a>
<a id="agroup____usbc__device__api_html_ggafea882f4f3cc96c502d53a24a3e5aec5a17f7f4fc9aa4178f0358769dedd29ade"></a>
<a id="agroup____usbc__device__api_html_ggafea882f4f3cc96c502d53a24a3e5aec5a42b660bb630edcca5ae8b031033d0718"></a>
<a id="agroup____usbc__device__api_html_ggafea882f4f3cc96c502d53a24a3e5aec5a655e913c86db5caa961083dad9f6b7a1"></a>
<a id="agroup____usbc__device__api_html_ggafea882f4f3cc96c502d53a24a3e5aec5a7c97208a8a12f70e7ffa43bb406b9ebd"></a>
<a id="agroup____usbc__device__api_html_ggafea882f4f3cc96c502d53a24a3e5aec5afa602e00bf418656e365baa4d9ff6cef"></a>
<a id="agroup__sink__callbacks_html_ga1a3da6faad509213f607893fef16b673"></a>
<a id="agroup__sink__callbacks_html_ga2aacd704d08a8cecbf818150e8ec51b6"></a>
<a id="agroup__sink__callbacks_html_ga44af668d9c22e757983c803d7b8ff82e"></a>
<a id="agroup__sink__callbacks_html_ga6096d6909698f1b86a1a9cbd1f8d4097"></a>
<a id="agroup__sink__callbacks_html_gaaed0161142c3481ce9180015b6968357"></a>
<a id="agroup__sink__callbacks_html_gae0448c6b271273c5db59775c3a6260dc"></a>
<a id="agroup__sink__callbacks_html_gaea62016b263dfaf5f869dd6ea036fdad"></a>
<a id="agroup__source__callbacks_html_ga2925e462140a700920251d92ae5a3aa4"></a>
<a id="agroup__source__callbacks_html_ga4bbf78bd752d38d915412dd942d3aab8"></a>
<a id="agroup__source__callbacks_html_ga699811c862990b31ec0126dd3a4c3e4d"></a>
<a id="agroup__source__callbacks_html_ga7c75f8192001179f20bf1fe48316f3c6"></a>
<a id="agroup__source__callbacks_html_gaaecac7683d7092c0a477e8d9ca0e5a33"></a>
<a id="agroup__source__callbacks_html_gae7391e858485e44a74e5fcdbb7931ca7"></a>
<a id="agroup__source__callbacks_html_gae903c8108e8d1563cb0b1ccdd901c925"></a>
<a id="agroup__source__callbacks_html_gaeeda677224456f685137e4b345c0e173"></a>
<a id="agroup__usb__type__c__port__controller__api_html_ga073ad4a46a5ea1f9e5cad45488d672f0"></a>
<a id="agroup__usb__type__c__port__controller__api_html_ga4d2b77f6ee685d1bff1117843150e664"></a>
<a id="agroup__usb__type__c_html_ga4e0eec97f7c5c97b87eff9561deea2d5"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="astdbool_8h_html_abb452686968e48b67397da5f97445f5b"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructdevice_html"></a>
<a id="ausbc__tcpc_8h_html"></a>
<a id="ausbc__vbus_8h_html"></a>

```c
/*
 * Copyright 2022 The Chromium OS Authors
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_USB_C_USBC_H_
#define ZEPHYR_INCLUDE_USB_C_USBC_H_

#include <zephyr/types.h>
#include <zephyr/device.h>
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
#include <zephyr/drivers/usb_c/usbc_vbus.h>

#ifdef __cplusplus
extern "C" {
#endif


#define FIXED_5V_100MA_RDO 0x1100280a

enum usbc_policy_request_t {
        REQUEST_NOP,
        REQUEST_TC_DISABLED,
        REQUEST_TC_ERROR_RECOVERY,
        REQUEST_TC_END,

        REQUEST_PE_DR_SWAP,
        REQUEST_PE_HARD_RESET_SEND,
        REQUEST_PE_SOFT_RESET_SEND,
        REQUEST_PE_GET_SRC_CAPS,
        REQUEST_GET_SNK_CAPS,
        REQUEST_PE_GOTO_MIN,
};

enum usbc_policy_notify_t {
        MSG_ACCEPT_RECEIVED,
        MSG_REJECTED_RECEIVED,
        MSG_DISCARDED,
        MSG_NOT_SUPPORTED_RECEIVED,
        DATA_ROLE_IS_UFP,
        DATA_ROLE_IS_DFP,
        POWER_ROLE_IS_SOURCE,
        POWER_ROLE_IS_SINK,
        PD_CONNECTED,
        NOT_PD_CONNECTED,
        TRANSITION_PS,
        PORT_PARTNER_NOT_RESPONSIVE,
        PROTOCOL_ERROR,
        SNK_TRANSITION_TO_DEFAULT,
        HARD_RESET_RECEIVED,
        POWER_CHANGE_0A0,
        POWER_CHANGE_DEF,
        POWER_CHANGE_1A5,
        POWER_CHANGE_3A0,
        SENDER_RESPONSE_TIMEOUT,
        SOURCE_CAPABILITIES_RECEIVED,
};

enum usbc_policy_check_t {
        CHECK_POWER_ROLE_SWAP,
        CHECK_DATA_ROLE_SWAP_TO_DFP,
        CHECK_DATA_ROLE_SWAP_TO_UFP,
        CHECK_SNK_AT_DEFAULT_LEVEL,
        CHECK_VCONN_CONTROL,
        CHECK_SRC_PS_AT_DEFAULT_LEVEL,
};

enum usbc_policy_wait_t {
        WAIT_SINK_REQUEST,
        WAIT_POWER_ROLE_SWAP,
        WAIT_DATA_ROLE_SWAP,
        WAIT_VCONN_SWAP,
};

enum usbc_snk_req_reply_t {
        SNK_REQUEST_VALID,
        SNK_REQUEST_REJECT,
        SNK_REQUEST_WAIT,
};

typedef int (*policy_cb_get_snk_cap_t)(const struct device *dev, uint32_t **pdos, int *num_pdos);
typedef void (*policy_cb_set_src_cap_t)(const struct device *dev, const uint32_t *pdos,
                                        const int num_pdos);

typedef bool (*policy_cb_check_t)(const struct device *dev,
                                  const enum usbc_policy_check_t policy_check);

typedef bool (*policy_cb_wait_notify_t)(const struct device *dev,
                                        const enum usbc_policy_wait_t wait_notify);

typedef void (*policy_cb_notify_t)(const struct device *dev,
                                   const enum usbc_policy_notify_t policy_notify);

typedef uint32_t (*policy_cb_get_rdo_t)(const struct device *dev);

typedef bool (*policy_cb_is_snk_at_default_t)(const struct device *dev);

typedef int (*policy_cb_get_src_caps_t)(const struct device *dev, const uint32_t **pdos,
                                        uint32_t *num_pdos);

typedef enum usbc_snk_req_reply_t (*policy_cb_check_sink_request_t)(const struct device *dev,
                                                                    const uint32_t request_msg);

typedef bool (*policy_cb_is_ps_ready_t)(const struct device *dev);

typedef bool (*policy_cb_present_contract_is_valid_t)(const struct device *dev,
                                                   const uint32_t present_contract);

typedef bool (*policy_cb_change_src_caps_t)(const struct device *dev);

typedef void (*policy_cb_set_port_partner_snk_cap_t)(const struct device *dev, const uint32_t *pdos,
                                                     const int num_pdos);
typedef int (*policy_cb_get_src_rp_t)(const struct device *dev, enum tc_rp_value *rp);
typedef int (*policy_cb_src_en_t)(const struct device *dev, bool en);

int usbc_start(const struct device *dev);

int usbc_suspend(const struct device *dev);

int usbc_request(const struct device *dev, const enum usbc_policy_request_t req);


void usbc_bypass_next_sleep(const struct device *dev);


void usbc_set_dpm_data(const struct device *dev, void *dpm_data);

void *usbc_get_dpm_data(const struct device *dev);

void usbc_set_vconn_control_cb(const struct device *dev, const tcpc_vconn_control_cb_t cb);

void usbc_set_vconn_discharge_cb(const struct device *dev, const tcpc_vconn_discharge_cb_t cb);

void usbc_set_policy_cb_check(const struct device *dev, const policy_cb_check_t cb);

void usbc_set_policy_cb_notify(const struct device *dev, const policy_cb_notify_t cb);

void usbc_set_policy_cb_wait_notify(const struct device *dev, const policy_cb_wait_notify_t cb);

void usbc_set_policy_cb_get_snk_cap(const struct device *dev, const policy_cb_get_snk_cap_t cb);

void usbc_set_policy_cb_set_src_cap(const struct device *dev, const policy_cb_set_src_cap_t cb);

void usbc_set_policy_cb_get_rdo(const struct device *dev, const policy_cb_get_rdo_t cb);

void usbc_set_policy_cb_is_snk_at_default(const struct device *dev,
                                          const policy_cb_is_snk_at_default_t cb);

void usbc_set_policy_cb_get_src_rp(const struct device *dev, const policy_cb_get_src_rp_t cb);

void usbc_set_policy_cb_src_en(const struct device *dev, const policy_cb_src_en_t cb);

void usbc_set_policy_cb_get_src_caps(const struct device *dev, const policy_cb_get_src_caps_t cb);

void usbc_set_policy_cb_check_sink_request(const struct device *dev,
                                           const policy_cb_check_sink_request_t cb);

void usbc_set_policy_cb_is_ps_ready(const struct device *dev,
                                          const policy_cb_is_ps_ready_t cb);

void usbc_set_policy_cb_present_contract_is_valid(const struct device *dev,
                                               const policy_cb_present_contract_is_valid_t cb);

void usbc_set_policy_cb_change_src_caps(const struct device *dev,
                                        const policy_cb_change_src_caps_t cb);

void usbc_set_policy_cb_set_port_partner_snk_cap(const struct device *dev,
                                                 const policy_cb_set_port_partner_snk_cap_t cb);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_USB_C_USBC_H_ */
```

## 889.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2022 The Chromium OS Authors。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 548 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_USB_C_USBC_H_`。

## 889.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/usbc_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/drivers/usb_c/usbc_tcpc.h](https://docs.zephyrproject.org/latest/doxygen/html/usbc__tcpc_8h.html)
- [zephyr/drivers/usb_c/usbc_vbus.h](https://docs.zephyrproject.org/latest/doxygen/html/usbc__vbus_8h.html)
- [usbc_policy_request_t](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga38a301a97a5e1a85e9836bbf083859f3)
- [REQUEST_NOP](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga38a301a97a5e1a85e9836bbf083859f3a2274197ac367b3da6358cac8dd781134)
- [REQUEST_TC_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga38a301a97a5e1a85e9836bbf083859f3a899633a1b63b1c3a826b5556f0f23d8b)
- [REQUEST_TC_ERROR_RECOVERY](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga38a301a97a5e1a85e9836bbf083859f3a8a7b77d81428f0c4784af3204f33b290)
- [REQUEST_TC_END](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga38a301a97a5e1a85e9836bbf083859f3a0c5ff3bc4c0d6f636663fd3911ed85d5)
- [REQUEST_PE_DR_SWAP](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga38a301a97a5e1a85e9836bbf083859f3a1fe9f57fac7f5149fe5f0f7c42523536)
- [REQUEST_PE_HARD_RESET_SEND](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga38a301a97a5e1a85e9836bbf083859f3a7c3c9c959439ee73539cff13e561c403)
- [REQUEST_PE_SOFT_RESET_SEND](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga38a301a97a5e1a85e9836bbf083859f3ad45120b1ceabeb054c2c2273b8431894)
- [REQUEST_PE_GET_SRC_CAPS](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga38a301a97a5e1a85e9836bbf083859f3a8c6083028ee8655cd0bebb6d9aab2e1e)
- [REQUEST_GET_SNK_CAPS](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga38a301a97a5e1a85e9836bbf083859f3ade1edc3aef0e4d563934edbc9ce784bc)
- [REQUEST_PE_GOTO_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga38a301a97a5e1a85e9836bbf083859f3ae5b4eb0db00e81a98cfe2436b64a7018)
- [usbc_policy_notify_t](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga66f934a5c5cd88b574c71d1f18fbda23)
- [MSG_ACCEPT_RECEIVED](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23a43bc56906b5dc4767d3297400053d286)
- [MSG_REJECTED_RECEIVED](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23a4ad0620e76c694004d3a1b43458a14b2)
- [MSG_DISCARDED](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23aa316636e8353dad1a9d5dec8b85a67e4)
- [MSG_NOT_SUPPORTED_RECEIVED](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23ab2f97ffaa13c84e656f7ac0004ec86ae)
- [DATA_ROLE_IS_UFP](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23a4020203569dcb95ab1b3d2946efced19)
- [DATA_ROLE_IS_DFP](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23a791604f4f0b2a2c3ccea4e98d1659a61)
- [POWER_ROLE_IS_SOURCE](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23a75abb66ae57bb7ad946b8c3c2734f445)
- [POWER_ROLE_IS_SINK](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23ae0372eb6238d86c3cfb2a10764180451)
- [PD_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23adbefad204068244fdf75ba1ff211fbfc)
- [NOT_PD_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23adebcbf5155b43ce562127d4077d46d7d)
- [TRANSITION_PS](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23a3a27b8e70ffe5788aa3ffea1bf61cae9)
- [PORT_PARTNER_NOT_RESPONSIVE](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23ad52e1c4f949bb64fef1d996ac2f4e0de)
- [PROTOCOL_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23a8cb937247ec21f791706f4f426496a8c)
- [SNK_TRANSITION_TO_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23aa02158d0afdd60c755453977200dfb28)
- [HARD_RESET_RECEIVED](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23ab74f5bcaa94a5fb1e46cdd7c6a5d822f)
- [POWER_CHANGE_0A0](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23a0fb0676a11ad8bad2d5249031ba5fd19)
- [POWER_CHANGE_DEF](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23a3a50be6f70c1a7abd724ab447491c46a)
- [POWER_CHANGE_1A5](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23a336bfb983c4d07684d67d4d9ef6c1489)
- [POWER_CHANGE_3A0](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23a3477c1c6ad8885c3ab7a9c58b7399dcf)
- [SENDER_RESPONSE_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23ac22b0026881f65c574d0bf7454321745)
- [SOURCE_CAPABILITIES_RECEIVED](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga66f934a5c5cd88b574c71d1f18fbda23a0266a21d8c836cf281c30542eb6badd4)
- [usbc_policy_check_t](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gafea882f4f3cc96c502d53a24a3e5aec5)
- [CHECK_POWER_ROLE_SWAP](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ggafea882f4f3cc96c502d53a24a3e5aec5a1181a470497b797136cf0eb204394106)
- [CHECK_DATA_ROLE_SWAP_TO_DFP](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ggafea882f4f3cc96c502d53a24a3e5aec5afa602e00bf418656e365baa4d9ff6cef)
- [CHECK_DATA_ROLE_SWAP_TO_UFP](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ggafea882f4f3cc96c502d53a24a3e5aec5a7c97208a8a12f70e7ffa43bb406b9ebd)
- [CHECK_SNK_AT_DEFAULT_LEVEL](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ggafea882f4f3cc96c502d53a24a3e5aec5a17f7f4fc9aa4178f0358769dedd29ade)
- [CHECK_VCONN_CONTROL](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ggafea882f4f3cc96c502d53a24a3e5aec5a655e913c86db5caa961083dad9f6b7a1)
- [CHECK_SRC_PS_AT_DEFAULT_LEVEL](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ggafea882f4f3cc96c502d53a24a3e5aec5a42b660bb630edcca5ae8b031033d0718)
- [usbc_policy_wait_t](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gadf5d2934b5dc8e2b01d20bb904988784)
- [WAIT_SINK_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ggadf5d2934b5dc8e2b01d20bb904988784a009ce2ceacd92db88d9a6beb01f84a28)
- [WAIT_POWER_ROLE_SWAP](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ggadf5d2934b5dc8e2b01d20bb904988784a91f1f41bf9318e06c02c1957a39a762a)
- [WAIT_DATA_ROLE_SWAP](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ggadf5d2934b5dc8e2b01d20bb904988784ae5ef03f78d78a7014404c581bad77c18)
- [WAIT_VCONN_SWAP](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ggadf5d2934b5dc8e2b01d20bb904988784aa982aed81f39e35cde74399c6d74e601)
- [usbc_snk_req_reply_t](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga4c4f0592a034b4e49eee85e95af33f94)
- [SNK_REQUEST_VALID](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga4c4f0592a034b4e49eee85e95af33f94a7922edb67afe83596819994a71de76dd)
- [SNK_REQUEST_REJECT](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga4c4f0592a034b4e49eee85e95af33f94a714f82e830f9528a8200c2c14795b282)
- [SNK_REQUEST_WAIT](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gga4c4f0592a034b4e49eee85e95af33f94a7ae46f6deb593eedd0564d30cb4c75fb)
- [policy_cb_get_snk_cap_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sink__callbacks.html#gaaed0161142c3481ce9180015b6968357)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [policy_cb_set_src_cap_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sink__callbacks.html#ga6096d6909698f1b86a1a9cbd1f8d4097)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [policy_cb_check_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sink__callbacks.html#ga2aacd704d08a8cecbf818150e8ec51b6)
- [policy_cb_wait_notify_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sink__callbacks.html#gaea62016b263dfaf5f869dd6ea036fdad)
- [policy_cb_notify_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sink__callbacks.html#ga44af668d9c22e757983c803d7b8ff82e)
- [policy_cb_get_rdo_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sink__callbacks.html#gae0448c6b271273c5db59775c3a6260dc)
- [policy_cb_is_snk_at_default_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sink__callbacks.html#ga1a3da6faad509213f607893fef16b673)
- [policy_cb_get_src_caps_t](https://docs.zephyrproject.org/latest/doxygen/html/group__source__callbacks.html#ga4bbf78bd752d38d915412dd942d3aab8)
- [policy_cb_check_sink_request_t](https://docs.zephyrproject.org/latest/doxygen/html/group__source__callbacks.html#gaeeda677224456f685137e4b345c0e173)
- [policy_cb_is_ps_ready_t](https://docs.zephyrproject.org/latest/doxygen/html/group__source__callbacks.html#gae7391e858485e44a74e5fcdbb7931ca7)
- [policy_cb_present_contract_is_valid_t](https://docs.zephyrproject.org/latest/doxygen/html/group__source__callbacks.html#ga2925e462140a700920251d92ae5a3aa4)
- [policy_cb_change_src_caps_t](https://docs.zephyrproject.org/latest/doxygen/html/group__source__callbacks.html#ga699811c862990b31ec0126dd3a4c3e4d)
- [policy_cb_set_port_partner_snk_cap_t](https://docs.zephyrproject.org/latest/doxygen/html/group__source__callbacks.html#gae903c8108e8d1563cb0b1ccdd901c925)
- [policy_cb_get_src_rp_t](https://docs.zephyrproject.org/latest/doxygen/html/group__source__callbacks.html#ga7c75f8192001179f20bf1fe48316f3c6)
- [tc_rp_value](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#ga4e0eec97f7c5c97b87eff9561deea2d5)
- [policy_cb_src_en_t](https://docs.zephyrproject.org/latest/doxygen/html/group__source__callbacks.html#gaaecac7683d7092c0a477e8d9ca0e5a33)
- [usbc_start](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga1535f7f53b3cc859ff536883fd631830)
- [usbc_suspend](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga68b73c03a5098a21260b5c3638edc973)
- [usbc_request](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga42691b0bb2b4be50147ac655e2cd9761)
- [usbc_set_dpm_data](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga997007cab2e54ad53b774b4215d0f593)
- [usbc_get_dpm_data](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gabd99b6926baf67212d65c4a4d147ce5b)
- [usbc_set_vconn_control_cb](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga9846b36061453023e16c160f5f120159)
- [tcpc_vconn_control_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga073ad4a46a5ea1f9e5cad45488d672f0)
- [usbc_set_vconn_discharge_cb](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga8741df33b5432d9c7d5902af9bd67084)
- [tcpc_vconn_discharge_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c__port__controller__api.html#ga4d2b77f6ee685d1bff1117843150e664)
- [usbc_set_policy_cb_check](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga67a046b411134d7c631942ae6ba73fc5)
- [usbc_set_policy_cb_notify](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gaedec1b4ad7b028ad18e1bcbe5396f1ee)
- [usbc_set_policy_cb_wait_notify](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gaa295593c7d5ede31328efaaab38b5880)
- [usbc_set_policy_cb_get_snk_cap](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gafbd2885d758aa869635041fa89750596)
- [usbc_set_policy_cb_set_src_cap](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga4536f47082f58f49d492de6f2b00dd17)
- [usbc_set_policy_cb_get_rdo](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga7c1ffea81f71416ab2942fc5a5b67d41)
- [usbc_set_policy_cb_is_snk_at_default](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gaffa045ee6e2fbc07fde7e84e44d3853f)
- [usbc_set_policy_cb_get_src_rp](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga8974f9661dfebf8f686d677f999d5957)
- [usbc_set_policy_cb_src_en](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gaf5332ba0c87ff737e1c476d7be071fec)
- [usbc_set_policy_cb_get_src_caps](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga7800c065ae5cfb7a95b58865d47c7f04)
- [usbc_set_policy_cb_check_sink_request](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga7f85188cc4f1a95350195abd0d736ada)
- [usbc_set_policy_cb_is_ps_ready](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gaf25c9cc2b6c514b9dcddc8129a76ccee)
- [usbc_set_policy_cb_present_contract_is_valid](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga5b4adb4330dfadf127d0a01253d722bb)
- [usbc_set_policy_cb_change_src_caps](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gaa8f89bfb1e9a1840b2d61ebaa13aeb2f)
- [usbc_set_policy_cb_set_port_partner_snk_cap](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gafd0a407558bb92dc8b7007d9d717b940)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [usbc_tcpc.h](https://docs.zephyrproject.org/latest/doxygen/html/usbc__tcpc_8h.html)
- [usbc_vbus.h](https://docs.zephyrproject.org/latest/doxygen/html/usbc__vbus_8h.html)

---

[上一章](P888_usb_hub.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P890_usbc_pd.h_源码浏览.md)
