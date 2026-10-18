---
id: learning.zephyr-docs.api-source-reference.page-886
title: ump_stream_responder.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ump__stream__responder_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第886章\_ump\_stream\_responder.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ump__stream__responder_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../usb/P111_UMP流响应器头文件接口.md)。

## 886.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="foldopen00030"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="foldopen00053"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="foldopen00073"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="foldopen00083"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="foldopen00097"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="foldopen00108"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="foldopen00118"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="agroup__ump__stream__responder_html_ga276d63d84c2131290293ed6963e41f56"></a>
<a id="agroup__ump__stream__responder_html_ga2eb945a1c7ab32ffe8a88cb8389ecee2"></a>
<a id="agroup__ump__stream__responder_html_ga60167d03152b8f97555567f5cc7b73e7"></a>
<a id="akernel_8h_html"></a>
<a id="amidi_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructmidi__ump_html"></a>
<a id="astructump__block__dt__spec_html"></a>
<a id="astructump__block__dt__spec_html_a081ed3cfda4c5ac6cb9c618acb20aeaf"></a>
<a id="astructump__block__dt__spec_html_a09299c0d4979a0d77e951511f89f4783"></a>
<a id="astructump__block__dt__spec_html_a3ecdc37b74894cf05909e6a61b74c28f"></a>
<a id="astructump__block__dt__spec_html_a43e7308ad22965d32b9ab174b09e9948"></a>
<a id="astructump__block__dt__spec_html_a94d49a45f045e4263c20f8d1af07b562"></a>
<a id="astructump__block__dt__spec_html_aa9238db0496387de9459c1862e239ae5"></a>
<a id="astructump__block__dt__spec_html_ad090f11096cbd142d12f53374aec5abc"></a>
<a id="astructump__endpoint__dt__spec_html"></a>
<a id="astructump__endpoint__dt__spec_html_ab7ca8d380d52b184db8bddcc59516f7e"></a>
<a id="astructump__endpoint__dt__spec_html_ae446e4a4778b2c89de2120d935068c03"></a>
<a id="astructump__endpoint__dt__spec_html_afdb120b1f342c1e078ef30ccabcfd0a0"></a>
<a id="astructump__stream__responder__cfg_html"></a>
<a id="astructump__stream__responder__cfg_html_a9107c4a2926092a52ea4616f505013ec"></a>
<a id="astructump__stream__responder__cfg_html_aa1f59013c817617d0ed3cf4b34d92fb6"></a>
<a id="astructump__stream__responder__cfg_html_afb02b5ac03c76a9d4af2513a99c11903"></a>

```c
/*
 * Copyright (c) 2025 Titouan Christophe
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_LIB_MIDI2_UMP_STREAM_RESPONDER_H_
#define ZEPHYR_LIB_MIDI2_UMP_STREAM_RESPONDER_H_


#include <zephyr/kernel.h>
#include <zephyr/audio/midi.h>

#ifdef __cplusplus
extern "C" {
#endif

struct ump_block_dt_spec {
        const char *name;
        uint8_t first_group;
        uint8_t groups_spanned;
        bool is_input;
        bool is_output;
        bool is_midi1;
        bool is_31250bps;
};

struct ump_endpoint_dt_spec {
        const char *name;
        size_t n_blocks;
        struct ump_block_dt_spec blocks[];
};

typedef void (*ump_send_func)(const void *, const struct midi_ump);

#define UMP_STREAM_RESPONDER(_dev, _send, _ep_spec)                             \
        {                                                                       \
                .dev = _dev,                                                    \
                .send = (ump_send_func) _send,  \
                .ep_spec = _ep_spec,                                            \
        }

struct ump_stream_responder_cfg {
        const void *dev;
        ump_send_func send;
        const struct ump_endpoint_dt_spec *ep_spec;
};

#define UMP_BLOCK_DT_SPEC_GET(_node)                                       \
{                                                                          \
        .name = DT_PROP_OR(_node, label, NULL),                            \
        .first_group = DT_REG_ADDR(_node),                                 \
        .groups_spanned = DT_REG_SIZE(_node),                              \
        .is_input = !DT_ENUM_HAS_VALUE(_node, terminal_type, output_only), \
        .is_output = !DT_ENUM_HAS_VALUE(_node, terminal_type, input_only), \
        .is_midi1 = !DT_ENUM_HAS_VALUE(_node, protocol, midi2),            \
        .is_31250bps = DT_PROP(_node, serial_31250bps),                    \
}

#define UMP_BLOCK_SEP_IF_OKAY(_node)                    \
        COND_CODE_1(DT_NODE_HAS_STATUS_OKAY(_node),     \
                    (UMP_BLOCK_DT_SPEC_GET(_node),),    \
                    ())

#define UMP_ENDPOINT_DT_SPEC_GET(_node)                                         \
{                                                                               \
        .name = DT_PROP_OR(_node, label, NULL),                                 \
        .n_blocks = DT_FOREACH_CHILD_SEP(_node, DT_NODE_HAS_STATUS_OKAY, (+)),  \
        .blocks = {DT_FOREACH_CHILD(_node, UMP_BLOCK_SEP_IF_OKAY)},             \
}

int ump_stream_respond(const struct ump_stream_responder_cfg *cfg,
                       const struct midi_ump pkt);

const char *ump_product_instance_id(void);


#ifdef __cplusplus
}
#endif

#endif
```

## 886.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Titouan Christophe。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

## 886.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../usb/P111_UMP流响应器头文件接口.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/audio/midi.h](https://docs.zephyrproject.org/latest/doxygen/html/midi_8h.html)
- [ump_block_dt_spec](../usb/P114_UMP功能块设备树配置.md)
- [name](../usb/P114_UMP功能块设备树配置.md#a081ed3cfda4c5ac6cb9c618acb20aeaf)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [first_group](../usb/P114_UMP功能块设备树配置.md#a43e7308ad22965d32b9ab174b09e9948)
- [groups_spanned](../usb/P114_UMP功能块设备树配置.md#ad090f11096cbd142d12f53374aec5abc)
- [is_input](../usb/P114_UMP功能块设备树配置.md#a3ecdc37b74894cf05909e6a61b74c28f)
- [is_output](../usb/P114_UMP功能块设备树配置.md#a94d49a45f045e4263c20f8d1af07b562)
- [is_midi1](../usb/P114_UMP功能块设备树配置.md#a09299c0d4979a0d77e951511f89f4783)
- [is_31250bps](../usb/P114_UMP功能块设备树配置.md#aa9238db0496387de9459c1862e239ae5)
- [ump_endpoint_dt_spec](../usb/P109_UMP端点设备树配置.md)
- [name](../usb/P109_UMP端点设备树配置.md#afdb120b1f342c1e078ef30ccabcfd0a0)
- [n_blocks](../usb/P109_UMP端点设备树配置.md#ab7ca8d380d52b184db8bddcc59516f7e)
- [blocks](../usb/P109_UMP端点设备树配置.md#ae446e4a4778b2c89de2120d935068c03)
- [ump_send_func](../usb/P108_UMP流响应器API.md#ga2eb945a1c7ab32ffe8a88cb8389ecee2)
- [midi_ump](../usb/P099_通用MIDI数据包结构.md)
- [ump_stream_responder_cfg](../usb/P110_UMP流响应器配置.md)
- [dev](../usb/P110_UMP流响应器配置.md#a9107c4a2926092a52ea4616f505013ec)
- [send](../usb/P110_UMP流响应器配置.md#aa1f59013c817617d0ed3cf4b34d92fb6)
- [ep_spec](../usb/P110_UMP流响应器配置.md#afb02b5ac03c76a9d4af2513a99c11903)
- [ump_stream_respond](../usb/P108_UMP流响应器API.md#ga60167d03152b8f97555567f5cc7b73e7)
- [ump_product_instance_id](../usb/P108_UMP流响应器API.md#ga276d63d84c2131290293ed6963e41f56)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [midi.h](https://docs.zephyrproject.org/latest/doxygen/html/midi_8h.html)
- [ump_block_dt_spec::name](../usb/P114_UMP功能块设备树配置.md#a081ed3cfda4c5ac6cb9c618acb20aeaf)
- [ump_block_dt_spec::is_midi1](../usb/P114_UMP功能块设备树配置.md#a09299c0d4979a0d77e951511f89f4783)
- [ump_block_dt_spec::is_input](../usb/P114_UMP功能块设备树配置.md#a3ecdc37b74894cf05909e6a61b74c28f)
- [ump_block_dt_spec::first_group](../usb/P114_UMP功能块设备树配置.md#a43e7308ad22965d32b9ab174b09e9948)
- [ump_block_dt_spec::is_output](../usb/P114_UMP功能块设备树配置.md#a94d49a45f045e4263c20f8d1af07b562)
- [ump_block_dt_spec::is_31250bps](../usb/P114_UMP功能块设备树配置.md#aa9238db0496387de9459c1862e239ae5)
- [ump_block_dt_spec::groups_spanned](../usb/P114_UMP功能块设备树配置.md#ad090f11096cbd142d12f53374aec5abc)
- [ump_endpoint_dt_spec::n_blocks](../usb/P109_UMP端点设备树配置.md#ab7ca8d380d52b184db8bddcc59516f7e)
- [ump_endpoint_dt_spec::blocks](../usb/P109_UMP端点设备树配置.md#ae446e4a4778b2c89de2120d935068c03)
- [ump_endpoint_dt_spec::name](../usb/P109_UMP端点设备树配置.md#afdb120b1f342c1e078ef30ccabcfd0a0)
- [ump_stream_responder_cfg::dev](../usb/P110_UMP流响应器配置.md#a9107c4a2926092a52ea4616f505013ec)
- [ump_stream_responder_cfg::send](../usb/P110_UMP流响应器配置.md#aa1f59013c817617d0ed3cf4b34d92fb6)
- [ump_stream_responder_cfg::ep_spec](../usb/P110_UMP流响应器配置.md#afb02b5ac03c76a9d4af2513a99c11903)

---

[上一章](P885_uhc.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P887_updatehub.h_源码浏览.md)
