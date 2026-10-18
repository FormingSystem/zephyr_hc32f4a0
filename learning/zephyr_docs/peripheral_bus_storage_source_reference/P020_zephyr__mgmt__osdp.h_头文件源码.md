---
id: learning.zephyr-docs.peripheral-bus-storage-source-reference.page-20
title: zephyr__mgmt__osdp.h_头文件源码
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/osdp_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_zephyr__mgmt__osdp.h_头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/osdp_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应头文件参考](../peripheral_bus_storage_header_reference/P020_zephyr__mgmt__osdp.h_头文件参考.md)。

## 20.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
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
<a id="foldopen00031"></a>
<a id="l00031"></a>
<a id="l00037"></a>
<a id="l00049"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="foldopen00059"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="foldopen00071"></a>
<a id="l00071"></a>
<a id="l00083"></a>
<a id="l00087"></a>
<a id="l00091"></a>
<a id="l00095"></a>
<a id="l00099"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="foldopen00109"></a>
<a id="l00109"></a>
<a id="l00113"></a>
<a id="l00117"></a>
<a id="l00121"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="foldopen00131"></a>
<a id="l00131"></a>
<a id="l00135"></a>
<a id="l00143"></a>
<a id="l00147"></a>
<a id="l00151"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="foldopen00161"></a>
<a id="l00161"></a>
<a id="l00165"></a>
<a id="l00173"></a>
<a id="l00177"></a>
<a id="l00181"></a>
<a id="l00185"></a>
<a id="l00189"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="foldopen00200"></a>
<a id="l00200"></a>
<a id="l00204"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="foldopen00221"></a>
<a id="l00221"></a>
<a id="l00226"></a>
<a id="l00230"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="foldopen00240"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="foldopen00254"></a>
<a id="l00254"></a>
<a id="l00256"></a>
<a id="l00262"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="foldopen00278"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="foldopen00293"></a>
<a id="l00293"></a>
<a id="l00297"></a>
<a id="l00301"></a>
<a id="l00307"></a>
<a id="l00311"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="foldopen00321"></a>
<a id="l00321"></a>
<a id="l00327"></a>
<a id="l00331"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="l00337"></a>
<a id="foldopen00341"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00343"></a>
<a id="l00344"></a>
<a id="l00345"></a>
<a id="l00346"></a>
<a id="foldopen00350"></a>
<a id="l00350"></a>
<a id="l00352"></a>
<a id="l00358"></a>
<a id="l00360"></a>
<a id="l00361"></a>
<a id="l00362"></a>
<a id="l00363"></a>
<a id="l00364"></a>
<a id="l00365"></a>
<a id="l00381"></a>
<a id="l00382"></a>
<a id="l00396"></a>
<a id="l00397"></a>
<a id="l00398"></a>
<a id="l00399"></a>
<a id="l00405"></a>
<a id="l00413"></a>
<a id="l00414"></a>
<a id="l00424"></a>
<a id="l00425"></a>
<a id="l00429"></a>
<a id="l00430"></a>
<a id="l00431"></a>
<a id="l00444"></a>
<a id="l00445"></a>
<a id="l00446"></a>
<a id="l00454"></a>
<a id="l00455"></a>
<a id="l00456"></a>
<a id="l00457"></a>
<a id="l00458"></a>
<a id="l00459"></a>
<a id="l00466"></a>
<a id="l00471"></a>
<a id="l00472"></a>
<a id="l00476"></a>
<a id="l00477"></a>
<a id="l00478"></a>
<a id="l00479"></a>
<a id="l00480"></a>
<a id="l00481"></a>
<a id="l00482"></a>
<a id="l00483"></a>
<a id="agroup__ft8xx__reference__api_html_gacde1ca3945cbe6c828f65051c5c3a615"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="akernel_8h_html"></a>
<a id="aosdp_8h_html_a04a0aa00cbe34e1723be1a4763f63e94"></a>
<a id="aosdp_8h_html_a6a71149ab51996f345c20ad34d725803"></a>
<a id="aosdp_8h_html_a81548fab575d89f66b45a5d4ac85984d"></a>
<a id="aosdp_8h_html_a81548fab575d89f66b45a5d4ac85984da0e5b42ad610675190f1d32a736a51250"></a>
<a id="aosdp_8h_html_a81548fab575d89f66b45a5d4ac85984da34bf34919ee65fe9a943856df65c5e47"></a>
<a id="aosdp_8h_html_a81548fab575d89f66b45a5d4ac85984da7c51d3f04f97758a6fb24eb4fc69a05c"></a>
<a id="aosdp_8h_html_a976512dfb1a4dc3ea9326d72a0abb5e7"></a>
<a id="aosdp_8h_html_a976512dfb1a4dc3ea9326d72a0abb5e7a5e654daacf0c0c084bac2ea4886bb059"></a>
<a id="aosdp_8h_html_a976512dfb1a4dc3ea9326d72a0abb5e7a6b7fa6ec118b9602fd68eceb6b4959d1"></a>
<a id="aosdp_8h_html_a976512dfb1a4dc3ea9326d72a0abb5e7a8ae3a81c63d022a674e9282a770b8471"></a>
<a id="aosdp_8h_html_a976512dfb1a4dc3ea9326d72a0abb5e7ab051b59f26c70ea48f7c353fae16b29e"></a>
<a id="aosdp_8h_html_a97ee0d8eb19e4e37ac89b2b6d338b84e"></a>
<a id="aosdp_8h_html_a97ee0d8eb19e4e37ac89b2b6d338b84ea0a80ccbb26b42ebc2cca602c7be3117a"></a>
<a id="aosdp_8h_html_a97ee0d8eb19e4e37ac89b2b6d338b84ea6832c2b25f228213022d0dbb5f5e1584"></a>
<a id="aosdp_8h_html_a97ee0d8eb19e4e37ac89b2b6d338b84ea72a45fa8f0b48a165c5507e456b4b1e7"></a>
<a id="aosdp_8h_html_a97ee0d8eb19e4e37ac89b2b6d338b84eac4024077b8804580d2480708e0b14ae4"></a>
<a id="aosdp_8h_html_a97ee0d8eb19e4e37ac89b2b6d338b84eadc9d0a41de52b0aa20e428e79e7c6b66"></a>
<a id="aosdp_8h_html_a97ee0d8eb19e4e37ac89b2b6d338b84eadd22879185802d0705d7195e1d9bd42c"></a>
<a id="aosdp_8h_html_aa02ec1fa8d7da5d694d5c2ae163e03cd"></a>
<a id="aosdp_8h_html_aa79d4fde3ae007e6c829d56daf8c3e49"></a>
<a id="aosdp_8h_html_ab1335ca06ebddff18873971e4dc03c40"></a>
<a id="aosdp_8h_html_abd8555e895d9370da1400f76c931ba21"></a>
<a id="aosdp_8h_html_abd8555e895d9370da1400f76c931ba21a008614ac1abea52942de74ffd33ce289"></a>
<a id="aosdp_8h_html_abd8555e895d9370da1400f76c931ba21a3abb5eec417c6889734c7f91b34b7a8f"></a>
<a id="aosdp_8h_html_abd8555e895d9370da1400f76c931ba21a652b1ddc2ecbf295ef20e7f896a45c42"></a>
<a id="aosdp_8h_html_abd8555e895d9370da1400f76c931ba21a80e5942403acbd058d52dd5d58a3aeea"></a>
<a id="aosdp_8h_html_abd8555e895d9370da1400f76c931ba21a876b0be45c76196699326ac80f05fc03"></a>
<a id="aosdp_8h_html_abd8555e895d9370da1400f76c931ba21ac59ca019a8253de6e662cd0a09adae1b"></a>
<a id="aosdp_8h_html_abd8555e895d9370da1400f76c931ba21ae7da10f0f9c405838264d475b92b4c01"></a>
<a id="aosdp_8h_html_ac097208c2b197ec4ebe567d59831a29f"></a>
<a id="aosdp_8h_html_acfd9e52e3ca23e6ef3d1cb55a0fa5714"></a>
<a id="aosdp_8h_html_af531800483155468768b89d20c3377d6"></a>
<a id="aslist_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructosdp__cmd__buzzer_html"></a>
<a id="astructosdp__cmd__buzzer_html_a0e97e1e33eac4f25e5a05586f8135ab3"></a>
<a id="astructosdp__cmd__buzzer_html_a0ea92ffb8ed7527e0373c0530edfb61d"></a>
<a id="astructosdp__cmd__buzzer_html_a16d0f385264e247d942367a6a13a77af"></a>
<a id="astructosdp__cmd__buzzer_html_a9082cf0dd2e3e9d31d95051f2952d611"></a>
<a id="astructosdp__cmd__buzzer_html_ac83cdb57418fc28f11c686e79e811492"></a>
<a id="astructosdp__cmd__comset_html"></a>
<a id="astructosdp__cmd__comset_html_a9de97b54c83b9643f1dd3413ec3b15e6"></a>
<a id="astructosdp__cmd__comset_html_af318dc8d5c8148902a2f824d72120ddc"></a>
<a id="astructosdp__cmd__keyset_html"></a>
<a id="astructosdp__cmd__keyset_html_a673a4897ae2ff6aa9b88af6440fdc5a6"></a>
<a id="astructosdp__cmd__keyset_html_add89930f6c3b88355fcd2f95573080e6"></a>
<a id="astructosdp__cmd__keyset_html_af85adb3e9c4f73a91fb7a430ff17f6df"></a>
<a id="astructosdp__cmd__led__params_html"></a>
<a id="astructosdp__cmd__led__params_html_a002de25cd5070cb96e90ccd0d2091216"></a>
<a id="astructosdp__cmd__led__params_html_a278ff380c2ab7d9c83b55aa49b3137cb"></a>
<a id="astructosdp__cmd__led__params_html_a80b47a4c55494d7062c4a83fd81b0910"></a>
<a id="astructosdp__cmd__led__params_html_ac6f1c1269697fcab96b6f68d62381ded"></a>
<a id="astructosdp__cmd__led__params_html_adde9dfdd167d9dfc122b56cf5e47b10f"></a>
<a id="astructosdp__cmd__led__params_html_ae95e3b87bbccd7d9897fef329001ce39"></a>
<a id="astructosdp__cmd__led_html"></a>
<a id="astructosdp__cmd__led_html_a033fd34a88b03d22a088bd7d2676efb5"></a>
<a id="astructosdp__cmd__led_html_a2130237d1b79ee36c5f5087cdec7acfb"></a>
<a id="astructosdp__cmd__led_html_ae4ff10389198d00047ffa2a7ec7d15ac"></a>
<a id="astructosdp__cmd__led_html_afe5e061d91fda9f008b5f8e5441df467"></a>
<a id="astructosdp__cmd__output_html"></a>
<a id="astructosdp__cmd__output_html_a1037244ed5f7c78eab51d6c08130b5d0"></a>
<a id="astructosdp__cmd__output_html_a4cd89d5c683b31d0e8eaf007443703a6"></a>
<a id="astructosdp__cmd__output_html_af5e1d55c987dd82ed4959f251a811846"></a>
<a id="astructosdp__cmd__text_html"></a>
<a id="astructosdp__cmd__text_html_a16f11f35eacb2876b09d148349b7ed3c"></a>
<a id="astructosdp__cmd__text_html_a3a94fa8b18d18845b60476148e2b7325"></a>
<a id="astructosdp__cmd__text_html_a3fa3d0780aa98542a270f6bdb6f49737"></a>
<a id="astructosdp__cmd__text_html_a46fe3f66e01229e763a6f06bd8bdfab8"></a>
<a id="astructosdp__cmd__text_html_a4dcdd83d3b8d424533ca997111f5cd94"></a>
<a id="astructosdp__cmd__text_html_a5e7b4c03b1649d8edbf53932ee90f7b3"></a>
<a id="astructosdp__cmd__text_html_acde9abcb023eb77845af8ea0935e63fa"></a>
<a id="astructosdp__cmd_html"></a>
<a id="astructosdp__cmd_html_a47c50d8c39cd47a7ad282dc91c4e9da8"></a>
<a id="astructosdp__cmd_html_a54d63398e914cd41567288f0da456e11"></a>
<a id="astructosdp__cmd_html_a62250f899e17c6fd94a1629f5ef9a479"></a>
<a id="astructosdp__cmd_html_a70630f6a8fbebacc27d889dec52336c8"></a>
<a id="astructosdp__cmd_html_aa745b1efadce9bc41e7253b76bdf2adf"></a>
<a id="astructosdp__cmd_html_acc408da549c0ef9a83e5a569b64dcb36"></a>
<a id="astructosdp__cmd_html_ad629c2622377800a0deab60756fa35a4"></a>
<a id="astructosdp__event__cardread_html"></a>
<a id="astructosdp__event__cardread_html_a025b2965987644fe08581b93d1067cb1"></a>
<a id="astructosdp__event__cardread_html_a025f3a460042fda69212db1c20d40bc5"></a>
<a id="astructosdp__event__cardread_html_a7a94e50e9729468baac011dde4806f00"></a>
<a id="astructosdp__event__cardread_html_ac6be298c814fcc933d6919a2c7fbb24c"></a>
<a id="astructosdp__event__cardread_html_af431337d9312618312360ef723f15b98"></a>
<a id="astructosdp__event__keypress_html"></a>
<a id="astructosdp__event__keypress_html_a41460942a34a488c78712bfba164f865"></a>
<a id="astructosdp__event__keypress_html_a88ac427349340142426e69fb99242cb4"></a>
<a id="astructosdp__event__keypress_html_ae6964a42e982021ef44372dca6af1166"></a>
<a id="astructosdp__event_html"></a>
<a id="astructosdp__event_html_a35759c65fc80592e42d948059f8178d3"></a>
<a id="astructosdp__event_html_ae2488838c114c72ebf0286a6f5c67814"></a>
<a id="astructosdp__event_html_ae72763214c94751d359bf1887d8ea35a"></a>

```c
/*
 * Copyright (c) 2020 Siddharth Chandrasekaran <siddharth@embedjournal.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_MGMT_OSDP_H_
#define ZEPHYR_INCLUDE_MGMT_OSDP_H_

#include <zephyr/kernel.h>
#include <stdint.h>

#include <zephyr/sys/slist.h>

#ifdef __cplusplus
extern "C" {
#endif

#define OSDP_CMD_TEXT_MAX_LEN          32
#define OSDP_CMD_KEYSET_KEY_MAX_LEN    32
#define OSDP_EVENT_MAX_DATALEN         64

struct osdp_cmd_output {
        uint8_t output_no;
        uint8_t control_code;
        uint16_t timer_count;
};

enum osdp_led_color_e {
        OSDP_LED_COLOR_NONE,
        OSDP_LED_COLOR_RED,
        OSDP_LED_COLOR_GREEN,
        OSDP_LED_COLOR_AMBER,
        OSDP_LED_COLOR_BLUE,
        OSDP_LED_COLOR_SENTINEL
};

struct osdp_cmd_led_params {
        uint8_t control_code;
        uint8_t on_count;
        uint8_t off_count;
        uint8_t on_color;
        uint8_t off_color;
        uint16_t timer_count;
};

struct osdp_cmd_led {
        uint8_t reader;
        uint8_t led_number;
        struct osdp_cmd_led_params temporary;
        struct osdp_cmd_led_params permanent;
};

struct osdp_cmd_buzzer {
        uint8_t reader;
        uint8_t control_code;
        uint8_t on_count;
        uint8_t off_count;
        uint8_t rep_count;
};

struct osdp_cmd_text {
        uint8_t reader;
        uint8_t control_code;
        uint8_t temp_time;
        uint8_t offset_row;
        uint8_t offset_col;
        uint8_t length;
        uint8_t data[OSDP_CMD_TEXT_MAX_LEN];
};

struct osdp_cmd_comset {
        uint8_t address;
        uint32_t baud_rate;
};

struct osdp_cmd_keyset {
        uint8_t type;
        uint8_t length;
        uint8_t data[OSDP_CMD_KEYSET_KEY_MAX_LEN];
};

enum osdp_cmd_e {
        OSDP_CMD_OUTPUT = 1,
        OSDP_CMD_LED,
        OSDP_CMD_BUZZER,
        OSDP_CMD_TEXT,
        OSDP_CMD_KEYSET,
        OSDP_CMD_COMSET,
        OSDP_CMD_SENTINEL
};

struct osdp_cmd {
        sys_snode_t node;
        enum osdp_cmd_e id;
        union {
                struct osdp_cmd_led    led;
                struct osdp_cmd_buzzer buzzer;
                struct osdp_cmd_text   text;
                struct osdp_cmd_output output;
                struct osdp_cmd_comset comset;
                struct osdp_cmd_keyset keyset;
        };
};

enum osdp_event_cardread_format_e {
        OSDP_CARD_FMT_RAW_UNSPECIFIED,
        OSDP_CARD_FMT_RAW_WIEGAND,
        OSDP_CARD_FMT_ASCII,
        OSDP_CARD_FMT_SENTINEL
};

struct osdp_event_cardread {
        int reader_no;
        enum osdp_event_cardread_format_e format;
        int direction;
        int length;
        uint8_t data[OSDP_EVENT_MAX_DATALEN];
};

struct osdp_event_keypress {
        int reader_no;
        int length;
        uint8_t data[OSDP_EVENT_MAX_DATALEN];
};

enum osdp_event_type {
        OSDP_EVENT_CARDREAD,
        OSDP_EVENT_KEYPRESS,
        OSDP_EVENT_SENTINEL
};

struct osdp_event {
        sys_snode_t node;
        enum osdp_event_type type;
        union {
                struct osdp_event_keypress keypress;
                struct osdp_event_cardread cardread;
        };
};

typedef int (*pd_command_callback_t)(void *arg, struct osdp_cmd *cmd);

typedef int (*cp_event_callback_t)(void *arg, int pd, struct osdp_event *ev);

#if defined(CONFIG_OSDP_MODE_PD) || defined(__DOXYGEN__)


void osdp_pd_set_command_callback(pd_command_callback_t cb, void *arg);

int osdp_pd_notify_event(const struct osdp_event *event);


#else /* CONFIG_OSDP_MODE_PD */

int osdp_cp_send_command(int pd, struct osdp_cmd *cmd);


void osdp_cp_set_event_callback(cp_event_callback_t cb, void *arg);

#endif /* CONFIG_OSDP_MODE_PD */

#if defined(CONFIG_OSDP_SC_ENABLED) || defined(__DOXYGEN__)


uint32_t osdp_get_sc_status_mask(void);


#endif

#ifdef __cplusplus
}
#endif

#endif  /* ZEPHYR_INCLUDE_MGMT_OSDP_H_ */
```

## 20.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 Siddharth Chandrasekaran <siddharth@embedjournal.com>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 430 行

条件编译配置（Configuration）标记：`CONFIG_OSDP_MODE_PD`。

### 注释 3：原第 456 行

条件编译配置（Configuration）标记：`CONFIG_OSDP_MODE_PD`。

### 注释 4：原第 483 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MGMT_OSDP_H_`。

## 20.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../peripheral_bus_storage_header_reference/P020_zephyr__mgmt__osdp.h_头文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/sys/slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [osdp_cmd_output](../peripheral_bus_storage_model_reference/P061_osdp_cmd_output_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [output_no](../peripheral_bus_storage_model_reference/P061_osdp_cmd_output_结构体.md#af5e1d55c987dd82ed4959f251a811846)
- [control_code](../peripheral_bus_storage_model_reference/P061_osdp_cmd_output_结构体.md#a1037244ed5f7c78eab51d6c08130b5d0)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [timer_count](../peripheral_bus_storage_model_reference/P061_osdp_cmd_output_结构体.md#a4cd89d5c683b31d0e8eaf007443703a6)
- [osdp_led_color_e](../peripheral_bus_storage_header_reference/P020_zephyr__mgmt__osdp.h_头文件参考.md#a97ee0d8eb19e4e37ac89b2b6d338b84e)
- [OSDP_LED_COLOR_NONE](../peripheral_bus_storage_header_reference/P020_zephyr__mgmt__osdp.h_头文件参考.md#a97ee0d8eb19e4e37ac89b2b6d338b84ea72a45fa8f0b48a165c5507e456b4b1e7)
- [OSDP_LED_COLOR_RED](../peripheral_bus_storage_header_reference/P020_zephyr__mgmt__osdp.h_头文件参考.md#a97ee0d8eb19e4e37ac89b2b6d338b84ea6832c2b25f228213022d0dbb5f5e1584)
- [OSDP_LED_COLOR_GREEN](../peripheral_bus_storage_header_reference/P020_zephyr__mgmt__osdp.h_头文件参考.md#a97ee0d8eb19e4e37ac89b2b6d338b84eac4024077b8804580d2480708e0b14ae4)
- [OSDP_LED_COLOR_AMBER](../peripheral_bus_storage_header_reference/P020_zephyr__mgmt__osdp.h_头文件参考.md#a97ee0d8eb19e4e37ac89b2b6d338b84eadd22879185802d0705d7195e1d9bd42c)
- [OSDP_LED_COLOR_BLUE](../peripheral_bus_storage_header_reference/P020_zephyr__mgmt__osdp.h_头文件参考.md#a97ee0d8eb19e4e37ac89b2b6d338b84eadc9d0a41de52b0aa20e428e79e7c6b66)
- [OSDP_LED_COLOR_SENTINEL](../peripheral_bus_storage_header_reference/P020_zephyr__mgmt__osdp.h_头文件参考.md#a97ee0d8eb19e4e37ac89b2b6d338b84ea0a80ccbb26b42ebc2cca602c7be3117a)
- [osdp_cmd_led_params](../peripheral_bus_storage_model_reference/P060_osdp_cmd_led_params_结构体.md)
- [control_code](../peripheral_bus_storage_model_reference/P060_osdp_cmd_led_params_结构体.md#ae95e3b87bbccd7d9897fef329001ce39)
- [on_count](../peripheral_bus_storage_model_reference/P060_osdp_cmd_led_params_结构体.md#adde9dfdd167d9dfc122b56cf5e47b10f)
- [off_count](../peripheral_bus_storage_model_reference/P060_osdp_cmd_led_params_结构体.md#a278ff380c2ab7d9c83b55aa49b3137cb)
- [on_color](../peripheral_bus_storage_model_reference/P060_osdp_cmd_led_params_结构体.md#a80b47a4c55494d7062c4a83fd81b0910)
- [off_color](../peripheral_bus_storage_model_reference/P060_osdp_cmd_led_params_结构体.md#ac6f1c1269697fcab96b6f68d62381ded)
- [timer_count](../peripheral_bus_storage_model_reference/P060_osdp_cmd_led_params_结构体.md#a002de25cd5070cb96e90ccd0d2091216)
- [osdp_cmd_led](../peripheral_bus_storage_model_reference/P059_osdp_cmd_led_结构体.md)
- [reader](../peripheral_bus_storage_model_reference/P059_osdp_cmd_led_结构体.md#afe5e061d91fda9f008b5f8e5441df467)
- [led_number](../peripheral_bus_storage_model_reference/P059_osdp_cmd_led_结构体.md#ae4ff10389198d00047ffa2a7ec7d15ac)
- [temporary](../peripheral_bus_storage_model_reference/P059_osdp_cmd_led_结构体.md#a2130237d1b79ee36c5f5087cdec7acfb)
- [permanent](../peripheral_bus_storage_model_reference/P059_osdp_cmd_led_结构体.md#a033fd34a88b03d22a088bd7d2676efb5)
- [osdp_cmd_buzzer](../peripheral_bus_storage_model_reference/P056_osdp_cmd_buzzer_结构体.md)
- [reader](../peripheral_bus_storage_model_reference/P056_osdp_cmd_buzzer_结构体.md#a0e97e1e33eac4f25e5a05586f8135ab3)
- [control_code](../peripheral_bus_storage_model_reference/P056_osdp_cmd_buzzer_结构体.md#a16d0f385264e247d942367a6a13a77af)
- [on_count](../peripheral_bus_storage_model_reference/P056_osdp_cmd_buzzer_结构体.md#a9082cf0dd2e3e9d31d95051f2952d611)
- [off_count](../peripheral_bus_storage_model_reference/P056_osdp_cmd_buzzer_结构体.md#ac83cdb57418fc28f11c686e79e811492)
- [rep_count](../peripheral_bus_storage_model_reference/P056_osdp_cmd_buzzer_结构体.md#a0ea92ffb8ed7527e0373c0530edfb61d)
- [osdp_cmd_text](../peripheral_bus_storage_model_reference/P062_osdp_cmd_text_结构体.md)
- [reader](../peripheral_bus_storage_model_reference/P062_osdp_cmd_text_结构体.md#a3fa3d0780aa98542a270f6bdb6f49737)
- [control_code](../peripheral_bus_storage_model_reference/P062_osdp_cmd_text_结构体.md#a46fe3f66e01229e763a6f06bd8bdfab8)
- [temp_time](../peripheral_bus_storage_model_reference/P062_osdp_cmd_text_结构体.md#acde9abcb023eb77845af8ea0935e63fa)
- [offset_row](../peripheral_bus_storage_model_reference/P062_osdp_cmd_text_结构体.md#a16f11f35eacb2876b09d148349b7ed3c)
- [offset_col](../peripheral_bus_storage_model_reference/P062_osdp_cmd_text_结构体.md#a5e7b4c03b1649d8edbf53932ee90f7b3)
- [length](../peripheral_bus_storage_model_reference/P062_osdp_cmd_text_结构体.md#a4dcdd83d3b8d424533ca997111f5cd94)
- [data](../peripheral_bus_storage_model_reference/P062_osdp_cmd_text_结构体.md#a3a94fa8b18d18845b60476148e2b7325)
- [OSDP_CMD_TEXT_MAX_LEN](../peripheral_bus_storage_header_reference/P020_zephyr__mgmt__osdp.h_头文件参考.md#acfd9e52e3ca23e6ef3d1cb55a0fa5714)
- [osdp_cmd_comset](../peripheral_bus_storage_model_reference/P057_osdp_cmd_comset_结构体.md)
- [address](../peripheral_bus_storage_model_reference/P057_osdp_cmd_comset_结构体.md#af318dc8d5c8148902a2f824d72120ddc)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [baud_rate](../peripheral_bus_storage_model_reference/P057_osdp_cmd_comset_结构体.md#a9de97b54c83b9643f1dd3413ec3b15e6)
- [osdp_cmd_keyset](../peripheral_bus_storage_model_reference/P058_osdp_cmd_keyset_结构体.md)
- [type](../peripheral_bus_storage_model_reference/P058_osdp_cmd_keyset_结构体.md#add89930f6c3b88355fcd2f95573080e6)
- [length](../peripheral_bus_storage_model_reference/P058_osdp_cmd_keyset_结构体.md#a673a4897ae2ff6aa9b88af6440fdc5a6)
- [data](../peripheral_bus_storage_model_reference/P058_osdp_cmd_keyset_结构体.md#af85adb3e9c4f73a91fb7a430ff17f6df)
- [OSDP_CMD_KEYSET_KEY_MAX_LEN](../peripheral_bus_storage_header_reference/P020_zephyr__mgmt__osdp.h_头文件参考.md#a04a0aa00cbe34e1723be1a4763f63e94)
- [osdp_cmd_e](../peripheral_bus_storage_header_reference/P020_zephyr__mgmt__osdp.h_头文件参考.md#abd8555e895d9370da1400f76c931ba21)
- [OSDP_CMD_OUTPUT](../peripheral_bus_storage_header_reference/P020_zephyr__mgmt__osdp.h_头文件参考.md#abd8555e895d9370da1400f76c931ba21ac59ca019a8253de6e662cd0a09adae1b)
- [OSDP_CMD_LED](../peripheral_bus_storage_header_reference/P020_zephyr__mgmt__osdp.h_头文件参考.md#abd8555e895d9370da1400f76c931ba21a652b1ddc2ecbf295ef20e7f896a45c42)
- [OSDP_CMD_BUZZER](../peripheral_bus_storage_header_reference/P020_zephyr__mgmt__osdp.h_头文件参考.md#abd8555e895d9370da1400f76c931ba21a876b0be45c76196699326ac80f05fc03)
- [OSDP_CMD_TEXT](../peripheral_bus_storage_header_reference/P020_zephyr__mgmt__osdp.h_头文件参考.md#abd8555e895d9370da1400f76c931ba21ae7da10f0f9c405838264d475b92b4c01)
- [OSDP_CMD_KEYSET](../peripheral_bus_storage_header_reference/P020_zephyr__mgmt__osdp.h_头文件参考.md#abd8555e895d9370da1400f76c931ba21a3abb5eec417c6889734c7f91b34b7a8f)
- [OSDP_CMD_COMSET](../peripheral_bus_storage_header_reference/P020_zephyr__mgmt__osdp.h_头文件参考.md#abd8555e895d9370da1400f76c931ba21a008614ac1abea52942de74ffd33ce289)
- [OSDP_CMD_SENTINEL](../peripheral_bus_storage_header_reference/P020_zephyr__mgmt__osdp.h_头文件参考.md#abd8555e895d9370da1400f76c931ba21a80e5942403acbd058d52dd5d58a3aeea)
- [osdp_cmd](../peripheral_bus_storage_model_reference/P055_osdp_cmd_结构体.md)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [id](../peripheral_bus_storage_model_reference/P055_osdp_cmd_结构体.md#a47c50d8c39cd47a7ad282dc91c4e9da8)
- [led](../peripheral_bus_storage_model_reference/P055_osdp_cmd_结构体.md#acc408da549c0ef9a83e5a569b64dcb36)
- [buzzer](../peripheral_bus_storage_model_reference/P055_osdp_cmd_结构体.md#a62250f899e17c6fd94a1629f5ef9a479)
- [text](../peripheral_bus_storage_model_reference/P055_osdp_cmd_结构体.md#a70630f6a8fbebacc27d889dec52336c8)
- [output](../peripheral_bus_storage_model_reference/P055_osdp_cmd_结构体.md#aa745b1efadce9bc41e7253b76bdf2adf)
- [comset](../peripheral_bus_storage_model_reference/P055_osdp_cmd_结构体.md#a54d63398e914cd41567288f0da456e11)
- [keyset](../peripheral_bus_storage_model_reference/P055_osdp_cmd_结构体.md#ad629c2622377800a0deab60756fa35a4)
- [osdp_event_cardread_format_e](../peripheral_bus_storage_header_reference/P020_zephyr__mgmt__osdp.h_头文件参考.md#a976512dfb1a4dc3ea9326d72a0abb5e7)
- [OSDP_CARD_FMT_RAW_UNSPECIFIED](../peripheral_bus_storage_header_reference/P020_zephyr__mgmt__osdp.h_头文件参考.md#a976512dfb1a4dc3ea9326d72a0abb5e7a8ae3a81c63d022a674e9282a770b8471)
- [OSDP_CARD_FMT_RAW_WIEGAND](../peripheral_bus_storage_header_reference/P020_zephyr__mgmt__osdp.h_头文件参考.md#a976512dfb1a4dc3ea9326d72a0abb5e7ab051b59f26c70ea48f7c353fae16b29e)
- [OSDP_CARD_FMT_ASCII](../peripheral_bus_storage_header_reference/P020_zephyr__mgmt__osdp.h_头文件参考.md#a976512dfb1a4dc3ea9326d72a0abb5e7a5e654daacf0c0c084bac2ea4886bb059)
- [OSDP_CARD_FMT_SENTINEL](../peripheral_bus_storage_header_reference/P020_zephyr__mgmt__osdp.h_头文件参考.md#a976512dfb1a4dc3ea9326d72a0abb5e7a6b7fa6ec118b9602fd68eceb6b4959d1)
- [osdp_event_cardread](../peripheral_bus_storage_model_reference/P064_osdp_event_cardread_结构体.md)
- [reader_no](../peripheral_bus_storage_model_reference/P064_osdp_event_cardread_结构体.md#ac6be298c814fcc933d6919a2c7fbb24c)
- [format](../peripheral_bus_storage_model_reference/P064_osdp_event_cardread_结构体.md#a7a94e50e9729468baac011dde4806f00)
- [direction](../peripheral_bus_storage_model_reference/P064_osdp_event_cardread_结构体.md#a025b2965987644fe08581b93d1067cb1)
- [length](../peripheral_bus_storage_model_reference/P064_osdp_event_cardread_结构体.md#a025f3a460042fda69212db1c20d40bc5)
- [data](../peripheral_bus_storage_model_reference/P064_osdp_event_cardread_结构体.md#af431337d9312618312360ef723f15b98)
- [OSDP_EVENT_MAX_DATALEN](../peripheral_bus_storage_header_reference/P020_zephyr__mgmt__osdp.h_头文件参考.md#af531800483155468768b89d20c3377d6)
- [osdp_event_keypress](../peripheral_bus_storage_model_reference/P065_osdp_event_keypress_结构体.md)
- [reader_no](../peripheral_bus_storage_model_reference/P065_osdp_event_keypress_结构体.md#ae6964a42e982021ef44372dca6af1166)
- [length](../peripheral_bus_storage_model_reference/P065_osdp_event_keypress_结构体.md#a41460942a34a488c78712bfba164f865)
- [data](../peripheral_bus_storage_model_reference/P065_osdp_event_keypress_结构体.md#a88ac427349340142426e69fb99242cb4)
- [osdp_event_type](../peripheral_bus_storage_header_reference/P020_zephyr__mgmt__osdp.h_头文件参考.md#a81548fab575d89f66b45a5d4ac85984d)
- [OSDP_EVENT_CARDREAD](../peripheral_bus_storage_header_reference/P020_zephyr__mgmt__osdp.h_头文件参考.md#a81548fab575d89f66b45a5d4ac85984da0e5b42ad610675190f1d32a736a51250)
- [OSDP_EVENT_KEYPRESS](../peripheral_bus_storage_header_reference/P020_zephyr__mgmt__osdp.h_头文件参考.md#a81548fab575d89f66b45a5d4ac85984da7c51d3f04f97758a6fb24eb4fc69a05c)
- [OSDP_EVENT_SENTINEL](../peripheral_bus_storage_header_reference/P020_zephyr__mgmt__osdp.h_头文件参考.md#a81548fab575d89f66b45a5d4ac85984da34bf34919ee65fe9a943856df65c5e47)
- [osdp_event](../peripheral_bus_storage_model_reference/P063_osdp_event_结构体.md)
- [type](../peripheral_bus_storage_model_reference/P063_osdp_event_结构体.md#ae72763214c94751d359bf1887d8ea35a)
- [keypress](../peripheral_bus_storage_model_reference/P063_osdp_event_结构体.md#a35759c65fc80592e42d948059f8178d3)
- [cardread](../peripheral_bus_storage_model_reference/P063_osdp_event_结构体.md#ae2488838c114c72ebf0286a6f5c67814)
- [pd_command_callback_t](../peripheral_bus_storage_header_reference/P020_zephyr__mgmt__osdp.h_头文件参考.md#a6a71149ab51996f345c20ad34d725803)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)
- [cp_event_callback_t](../peripheral_bus_storage_header_reference/P020_zephyr__mgmt__osdp.h_头文件参考.md#aa02ec1fa8d7da5d694d5c2ae163e03cd)
- [osdp_pd_set_command_callback](../peripheral_bus_storage_header_reference/P020_zephyr__mgmt__osdp.h_头文件参考.md#aa79d4fde3ae007e6c829d56daf8c3e49)
- [osdp_pd_notify_event](../peripheral_bus_storage_header_reference/P020_zephyr__mgmt__osdp.h_头文件参考.md#ac097208c2b197ec4ebe567d59831a29f)
- [osdp_get_sc_status_mask](../peripheral_bus_storage_header_reference/P020_zephyr__mgmt__osdp.h_头文件参考.md#ab1335ca06ebddff18873971e4dc03c40)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [osdp_cmd_buzzer::reader](../peripheral_bus_storage_model_reference/P056_osdp_cmd_buzzer_结构体.md#a0e97e1e33eac4f25e5a05586f8135ab3)
- [osdp_cmd_buzzer::rep_count](../peripheral_bus_storage_model_reference/P056_osdp_cmd_buzzer_结构体.md#a0ea92ffb8ed7527e0373c0530edfb61d)
- [osdp_cmd_buzzer::control_code](../peripheral_bus_storage_model_reference/P056_osdp_cmd_buzzer_结构体.md#a16d0f385264e247d942367a6a13a77af)
- [osdp_cmd_buzzer::on_count](../peripheral_bus_storage_model_reference/P056_osdp_cmd_buzzer_结构体.md#a9082cf0dd2e3e9d31d95051f2952d611)
- [osdp_cmd_buzzer::off_count](../peripheral_bus_storage_model_reference/P056_osdp_cmd_buzzer_结构体.md#ac83cdb57418fc28f11c686e79e811492)
- [osdp_cmd_comset::baud_rate](../peripheral_bus_storage_model_reference/P057_osdp_cmd_comset_结构体.md#a9de97b54c83b9643f1dd3413ec3b15e6)
- [osdp_cmd_comset::address](../peripheral_bus_storage_model_reference/P057_osdp_cmd_comset_结构体.md#af318dc8d5c8148902a2f824d72120ddc)
- [osdp_cmd_keyset::length](../peripheral_bus_storage_model_reference/P058_osdp_cmd_keyset_结构体.md#a673a4897ae2ff6aa9b88af6440fdc5a6)
- [osdp_cmd_keyset::type](../peripheral_bus_storage_model_reference/P058_osdp_cmd_keyset_结构体.md#add89930f6c3b88355fcd2f95573080e6)
- [osdp_cmd_keyset::data](../peripheral_bus_storage_model_reference/P058_osdp_cmd_keyset_结构体.md#af85adb3e9c4f73a91fb7a430ff17f6df)
- [osdp_cmd_led_params::timer_count](../peripheral_bus_storage_model_reference/P060_osdp_cmd_led_params_结构体.md#a002de25cd5070cb96e90ccd0d2091216)
- [osdp_cmd_led_params::off_count](../peripheral_bus_storage_model_reference/P060_osdp_cmd_led_params_结构体.md#a278ff380c2ab7d9c83b55aa49b3137cb)
- [osdp_cmd_led_params::on_color](../peripheral_bus_storage_model_reference/P060_osdp_cmd_led_params_结构体.md#a80b47a4c55494d7062c4a83fd81b0910)
- [osdp_cmd_led_params::off_color](../peripheral_bus_storage_model_reference/P060_osdp_cmd_led_params_结构体.md#ac6f1c1269697fcab96b6f68d62381ded)
- [osdp_cmd_led_params::on_count](../peripheral_bus_storage_model_reference/P060_osdp_cmd_led_params_结构体.md#adde9dfdd167d9dfc122b56cf5e47b10f)
- [osdp_cmd_led_params::control_code](../peripheral_bus_storage_model_reference/P060_osdp_cmd_led_params_结构体.md#ae95e3b87bbccd7d9897fef329001ce39)
- [osdp_cmd_led::permanent](../peripheral_bus_storage_model_reference/P059_osdp_cmd_led_结构体.md#a033fd34a88b03d22a088bd7d2676efb5)
- [osdp_cmd_led::temporary](../peripheral_bus_storage_model_reference/P059_osdp_cmd_led_结构体.md#a2130237d1b79ee36c5f5087cdec7acfb)
- [osdp_cmd_led::led_number](../peripheral_bus_storage_model_reference/P059_osdp_cmd_led_结构体.md#ae4ff10389198d00047ffa2a7ec7d15ac)
- [osdp_cmd_led::reader](../peripheral_bus_storage_model_reference/P059_osdp_cmd_led_结构体.md#afe5e061d91fda9f008b5f8e5441df467)
- [osdp_cmd_output::control_code](../peripheral_bus_storage_model_reference/P061_osdp_cmd_output_结构体.md#a1037244ed5f7c78eab51d6c08130b5d0)
- [osdp_cmd_output::timer_count](../peripheral_bus_storage_model_reference/P061_osdp_cmd_output_结构体.md#a4cd89d5c683b31d0e8eaf007443703a6)
- [osdp_cmd_output::output_no](../peripheral_bus_storage_model_reference/P061_osdp_cmd_output_结构体.md#af5e1d55c987dd82ed4959f251a811846)
- [osdp_cmd_text::offset_row](../peripheral_bus_storage_model_reference/P062_osdp_cmd_text_结构体.md#a16f11f35eacb2876b09d148349b7ed3c)
- [osdp_cmd_text::data](../peripheral_bus_storage_model_reference/P062_osdp_cmd_text_结构体.md#a3a94fa8b18d18845b60476148e2b7325)
- [osdp_cmd_text::reader](../peripheral_bus_storage_model_reference/P062_osdp_cmd_text_结构体.md#a3fa3d0780aa98542a270f6bdb6f49737)
- [osdp_cmd_text::control_code](../peripheral_bus_storage_model_reference/P062_osdp_cmd_text_结构体.md#a46fe3f66e01229e763a6f06bd8bdfab8)
- [osdp_cmd_text::length](../peripheral_bus_storage_model_reference/P062_osdp_cmd_text_结构体.md#a4dcdd83d3b8d424533ca997111f5cd94)
- [osdp_cmd_text::offset_col](../peripheral_bus_storage_model_reference/P062_osdp_cmd_text_结构体.md#a5e7b4c03b1649d8edbf53932ee90f7b3)
- [osdp_cmd_text::temp_time](../peripheral_bus_storage_model_reference/P062_osdp_cmd_text_结构体.md#acde9abcb023eb77845af8ea0935e63fa)
- [osdp_cmd::id](../peripheral_bus_storage_model_reference/P055_osdp_cmd_结构体.md#a47c50d8c39cd47a7ad282dc91c4e9da8)
- [osdp_cmd::comset](../peripheral_bus_storage_model_reference/P055_osdp_cmd_结构体.md#a54d63398e914cd41567288f0da456e11)
- [osdp_cmd::buzzer](../peripheral_bus_storage_model_reference/P055_osdp_cmd_结构体.md#a62250f899e17c6fd94a1629f5ef9a479)
- [osdp_cmd::text](../peripheral_bus_storage_model_reference/P055_osdp_cmd_结构体.md#a70630f6a8fbebacc27d889dec52336c8)
- [osdp_cmd::output](../peripheral_bus_storage_model_reference/P055_osdp_cmd_结构体.md#aa745b1efadce9bc41e7253b76bdf2adf)
- [osdp_cmd::led](../peripheral_bus_storage_model_reference/P055_osdp_cmd_结构体.md#acc408da549c0ef9a83e5a569b64dcb36)
- [osdp_cmd::keyset](../peripheral_bus_storage_model_reference/P055_osdp_cmd_结构体.md#ad629c2622377800a0deab60756fa35a4)
- [osdp_event_cardread::direction](../peripheral_bus_storage_model_reference/P064_osdp_event_cardread_结构体.md#a025b2965987644fe08581b93d1067cb1)
- [osdp_event_cardread::length](../peripheral_bus_storage_model_reference/P064_osdp_event_cardread_结构体.md#a025f3a460042fda69212db1c20d40bc5)
- [osdp_event_cardread::format](../peripheral_bus_storage_model_reference/P064_osdp_event_cardread_结构体.md#a7a94e50e9729468baac011dde4806f00)
- [osdp_event_cardread::reader_no](../peripheral_bus_storage_model_reference/P064_osdp_event_cardread_结构体.md#ac6be298c814fcc933d6919a2c7fbb24c)
- [osdp_event_cardread::data](../peripheral_bus_storage_model_reference/P064_osdp_event_cardread_结构体.md#af431337d9312618312360ef723f15b98)
- [osdp_event_keypress::length](../peripheral_bus_storage_model_reference/P065_osdp_event_keypress_结构体.md#a41460942a34a488c78712bfba164f865)
- [osdp_event_keypress::data](../peripheral_bus_storage_model_reference/P065_osdp_event_keypress_结构体.md#a88ac427349340142426e69fb99242cb4)
- [osdp_event_keypress::reader_no](../peripheral_bus_storage_model_reference/P065_osdp_event_keypress_结构体.md#ae6964a42e982021ef44372dca6af1166)
- [osdp_event::keypress](../peripheral_bus_storage_model_reference/P063_osdp_event_结构体.md#a35759c65fc80592e42d948059f8178d3)
- [osdp_event::cardread](../peripheral_bus_storage_model_reference/P063_osdp_event_结构体.md#ae2488838c114c72ebf0286a6f5c67814)
- [osdp_event::type](../peripheral_bus_storage_model_reference/P063_osdp_event_结构体.md#ae72763214c94751d359bf1887d8ea35a)

---

[上一章](P019_zephyr__drivers__mux.h_头文件源码.md) · [返回大纲](大纲.md) · [下一章](P021_zephyr__drivers__peci.h_头文件源码.md)
