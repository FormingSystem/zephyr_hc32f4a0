---
id: learning.zephyr-docs.api-source-supplement-reference.page-31
title: cobs.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/cobs_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第31章\_cobs.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/cobs_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/cobs_8h.html)。

## 31.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
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
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00041"></a>
<a id="l00048"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00087"></a>
<a id="foldopen00096"></a>
<a id="l00096"></a>
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
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="foldopen00169"></a>
<a id="l00169"></a>
<a id="l00172"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00177"></a>
<a id="l00179"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="foldopen00189"></a>
<a id="l00189"></a>
<a id="l00192"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00197"></a>
<a id="l00199"></a>
<a id="l00201"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00305"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="agroup__cobs_html_ga016e001ca84dae52391b5bc22b5c92ad"></a>
<a id="agroup__cobs_html_ga0b6ad6f90e70629f143c65f8dbe76a33"></a>
<a id="agroup__cobs_html_ga16669d639b1bdf7bc4a90190530ec2d9"></a>
<a id="agroup__cobs_html_ga49fa5a2c541ac72c2a0fe89971bec38d"></a>
<a id="agroup__cobs_html_ga71047f135e408e95d83828e898e823b0"></a>
<a id="agroup__cobs_html_ga88a7600ca21e3a160ed8354a5af0987b"></a>
<a id="agroup__cobs_html_gabb6193b8d15b33e5c739c9609376950f"></a>
<a id="agroup__cobs_html_gac50b6fd7bf9943429a4c0706350fcd76"></a>
<a id="agroup__cobs_html_gadf39d47a13fe1e3b10bcc9208f5b4786"></a>
<a id="agroup__cobs_html_gaf07cf3c33fd82490a8db4fa0f64bf906"></a>
<a id="agroup__cobs_html_gafebbd3ea1b058cf7834dd534048602fb"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html"></a>
<a id="anet__buf_8h_html"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructcobs__decoder_html"></a>
<a id="astructcobs__encoder_html"></a>
<a id="astructnet__buf_html"></a>
<a id="asys_2util_8h_html"></a>

```c
/*
 * Copyright (c) 2024 Kelly Helmut Lord
 * Copyright (c) 2026 Basalte bv
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DATA_COBS_H_
#define ZEPHYR_INCLUDE_DATA_COBS_H_

#include <stddef.h>
#include <sys/types.h>
#include <zephyr/sys/util.h>

#if defined(CONFIG_NET_BUF)
#include <zephyr/net_buf.h>
#endif

#ifdef __cplusplus
extern "C" {
#endif




#define COBS_DEFAULT_DELIMITER 0x00

#define COBS_FLAG_TRAILING_DELIMITER BIT(8)

#define COBS_FLAG_CUSTOM_DELIMITER(x) ((x) & 0xff)


static inline size_t cobs_max_encoded_len(size_t decoded_size, uint32_t flags)
{
        if (flags & COBS_FLAG_TRAILING_DELIMITER) {
                return decoded_size + decoded_size / 254 + 1 + 1;
        } else {
                return decoded_size + decoded_size / 254 + 1;
        }
}

#if defined(CONFIG_NET_BUF) || defined(__DOXYGEN__)


int cobs_encode(struct net_buf *src, struct net_buf *dst, uint32_t flags);

int cobs_decode(struct net_buf *src, struct net_buf *dst, uint32_t flags);

#endif /* defined(CONFIG_NET_BUF) || defined(__DOXYGEN__) */

typedef int (*cobs_stream_cb)(const uint8_t *buf, size_t len, void *user_data);

struct cobs_encoder {
        cobs_stream_cb cb;
        void *cb_user_data;

        uint8_t fragment[255];
        uint32_t flags;
};

struct cobs_decoder {
        cobs_stream_cb cb;
        void *cb_user_data;

        uint8_t code;
        uint8_t code_index;
        uint32_t flags;
};

int cobs_encoder_init(struct cobs_encoder *enc, cobs_stream_cb cb, void *user_data, uint32_t flags);

int cobs_encoder_close(struct cobs_encoder *enc);

int cobs_encoder_write(struct cobs_encoder *enc, const uint8_t *buf, size_t len);

int cobs_decoder_init(struct cobs_decoder *dec, cobs_stream_cb cb, void *user_data, uint32_t flags);

int cobs_decoder_close(struct cobs_decoder *dec);

int cobs_decoder_write(struct cobs_decoder *dec, const uint8_t *buf, size_t len);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DATA_COBS_H_ */
```

## 31.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Kelly Helmut Lord。

版权（Copyright）：© 2026 Basalte bv。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 142 行

条件编译表达式：`defined(CONFIG_NET_BUF) || defined(__DOXYGEN__)`。

### 注释 3：原第 310 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DATA_COBS_H_`。

## 31.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/cobs_8h.html)
- [sys/types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [cobs_max_encoded_len](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html#ga71047f135e408e95d83828e898e823b0)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [COBS_FLAG_TRAILING_DELIMITER](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html#ga016e001ca84dae52391b5bc22b5c92ad)
- [cobs_encode](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html#gadf39d47a13fe1e3b10bcc9208f5b4786)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [cobs_decode](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html#gabb6193b8d15b33e5c739c9609376950f)
- [cobs_stream_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html#gaf07cf3c33fd82490a8db4fa0f64bf906)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [cobs_encoder](../system_service_model_reference/P004_cobs_encoder_结构体.md)
- [cobs_decoder](../system_service_model_reference/P003_cobs_decoder_结构体.md)
- [cobs_encoder_init](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html#gafebbd3ea1b058cf7834dd534048602fb)
- [cobs_encoder_close](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html#ga0b6ad6f90e70629f143c65f8dbe76a33)
- [cobs_encoder_write](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html#ga88a7600ca21e3a160ed8354a5af0987b)
- [cobs_decoder_init](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html#ga49fa5a2c541ac72c2a0fe89971bec38d)
- [cobs_decoder_close](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html#gac50b6fd7bf9943429a4c0706350fcd76)
- [cobs_decoder_write](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html#ga16669d639b1bdf7bc4a90190530ec2d9)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [util.h](../util_reference/P002_通用工具头文件参考.md)

---

[上一章](P030_clock_control_ti_cdce9xx.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P032_codec.h_源码浏览.md)
