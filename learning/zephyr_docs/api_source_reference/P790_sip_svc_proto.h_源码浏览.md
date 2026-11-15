---
id: learning.zephyr-docs.api-source-reference.page-790
title: sip_svc_proto.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__proto_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第790章\_sip\_svc\_proto.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__proto_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__proto_8h.html)。

## 790.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00021"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="foldopen00041"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="foldopen00047"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="foldopen00050"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="foldopen00053"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00132"></a>
<a id="foldopen00133"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00176"></a>
<a id="foldopen00177"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astructsip__svc__request_html"></a>
<a id="astructsip__svc__request_html_a0b70942fc037346bb5ee051484c21745"></a>
<a id="astructsip__svc__request_html_a35198a51b070fb2acf76458568204ec1"></a>
<a id="astructsip__svc__request_html_a3b41176de28f042510d5ca5fc9c4678e"></a>
<a id="astructsip__svc__request_html_a67c7626f24035b9cdfef24193e2442c6"></a>
<a id="astructsip__svc__request_html_a6cd5c3cf895daad0c600544a903f2eb8"></a>
<a id="astructsip__svc__request_html_a8d827ae174a2b8f11b50c7e6f31c3708"></a>
<a id="astructsip__svc__request_html_a95e4d0bb03bfca90ea78fc19c581ef7f"></a>
<a id="astructsip__svc__request_html_a9b4cc837fbb958e93a900b58b2ea3a75"></a>
<a id="astructsip__svc__request_html_aa20d78ab299064e8d4b304f4165bfdf2"></a>
<a id="astructsip__svc__request_html_aa8c71f7af00dd3195d49c04df5cb3509"></a>
<a id="astructsip__svc__request_html_af20b0881ec14973d7a6b79f3b146dc7a"></a>
<a id="astructsip__svc__request_html_aff7c782bc6690ef134db4e4d999189a7"></a>
<a id="astructsip__svc__response_html"></a>
<a id="astructsip__svc__response_html_a2e8373be61b16ac4f4d013103539cceb"></a>
<a id="astructsip__svc__response_html_a4f413e152dc2ef463140499164c3e410"></a>
<a id="astructsip__svc__response_html_a5b8a49d292e45ecdd81920c30b650c10"></a>
<a id="astructsip__svc__response_html_a992b3f936866852633569f9c8d37d6a0"></a>
<a id="astructsip__svc__response_html_aac8bb11e4661e59cbce0d6b5d50a0820"></a>
<a id="astructsip__svc__response_html_ab2a3ed6ec283ef83a2ad8ea8eea421be"></a>
<a id="astructsip__svc__response_html_abfb0f411524209388f79f35a82031e79"></a>
<a id="astructsip__svc__response_html_af973d08da13a7dcecf344f3f9d6f118e"></a>

```c
/*
 * Copyright (c) 2023, Intel Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_SIP_SVC_PROTO_H_
#define ZEPHYR_INCLUDE_SIP_SVC_PROTO_H_


#define SIP_SVC_ID_INVALID 0xFFFFFFFF


#define SIP_SVC_PROTO_VER 0x0

#define SIP_SVC_PROTO_HEADER_CODE_OFFSET 0
#define SIP_SVC_PROTO_HEADER_CODE_MASK   0xFFFF

#define SIP_SVC_PROTO_HEADER_TRANS_ID_OFFSET 16
#define SIP_SVC_PROTO_HEADER_TRANS_ID_MASK   0xFF

#define SIP_SVC_PROTO_HEADER_VER_OFFSET 30
#define SIP_SVC_PROTO_HEADER_VER_MASK   0x3

#define SIP_SVC_PROTO_HEADER(code, trans_id)                                                       \
        ((((code)&SIP_SVC_PROTO_HEADER_CODE_MASK) << SIP_SVC_PROTO_HEADER_CODE_OFFSET) |           \
         (((trans_id)&SIP_SVC_PROTO_HEADER_TRANS_ID_MASK)                                          \
          << SIP_SVC_PROTO_HEADER_TRANS_ID_OFFSET) |                                               \
         ((SIP_SVC_PROTO_VER & SIP_SVC_PROTO_HEADER_VER_MASK) << SIP_SVC_PROTO_HEADER_VER_OFFSET))

#define SIP_SVC_PROTO_HEADER_GET_CODE(header)                                                      \
        (((header) >> SIP_SVC_PROTO_HEADER_CODE_OFFSET) & SIP_SVC_PROTO_HEADER_CODE_MASK)

#define SIP_SVC_PROTO_HEADER_GET_TRANS_ID(header)                                                  \
        (((header) >> SIP_SVC_PROTO_HEADER_TRANS_ID_OFFSET) & SIP_SVC_PROTO_HEADER_TRANS_ID_MASK)

#define SIP_SVC_PROTO_HEADER_SET_TRANS_ID(header, trans_id)                                        \
        (header) &= ~(SIP_SVC_PROTO_HEADER_TRANS_ID_MASK << SIP_SVC_PROTO_HEADER_TRANS_ID_OFFSET); \
        (header) |= (((trans_id)&SIP_SVC_PROTO_HEADER_TRANS_ID_MASK)                               \
                     << SIP_SVC_PROTO_HEADER_TRANS_ID_OFFSET);


#define SIP_SVC_PROTO_CMD_SYNC  0x0
#define SIP_SVC_PROTO_CMD_ASYNC 0x1
#define SIP_SVC_PROTO_CMD_MAX   SIP_SVC_PROTO_CMD_ASYNC


#define SIP_SVC_PROTO_STATUS_OK          0x0
#define SIP_SVC_PROTO_STATUS_UNKNOWN     0xFFFF
#define SIP_SVC_PROTO_STATUS_BUSY        0x1
#define SIP_SVC_PROTO_STATUS_REJECT      0x2
#define SIP_SVC_PROTO_STATUS_NO_RESPONSE 0x3
#define SIP_SVC_PROTO_STATUS_ERROR       0x4


struct sip_svc_request {
        uint32_t header;
        unsigned long a0;
        unsigned long a1;
        unsigned long a2;
        unsigned long a3;
        unsigned long a4;
        unsigned long a5;
        unsigned long a6;
        unsigned long a7;
        uint64_t resp_data_addr;
        uint32_t resp_data_size;
        void *priv_data;
};


struct sip_svc_response {
        uint32_t header;
        unsigned long a0;
        unsigned long a1;
        unsigned long a2;
        unsigned long a3;
        uint64_t resp_data_addr;
        uint32_t resp_data_size;
        void *priv_data;
};

#endif /* ZEPHYR_INCLUDE_SIP_SVC_PROTO_H_ */
```

## 790.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023, Intel Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 188 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_SIP_SVC_PROTO_H_`。

## 790.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/sip__svc__proto_8h.html)
- [sip_svc_request](../platform_security_model_reference/P056_sip_svc_request_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [header](../platform_security_model_reference/P056_sip_svc_request_结构体.md#aa8c71f7af00dd3195d49c04df5cb3509)
- [a0](../platform_security_model_reference/P056_sip_svc_request_结构体.md#a95e4d0bb03bfca90ea78fc19c581ef7f)
- [a1](../platform_security_model_reference/P056_sip_svc_request_结构体.md#a3b41176de28f042510d5ca5fc9c4678e)
- [a2](../platform_security_model_reference/P056_sip_svc_request_结构体.md#aa20d78ab299064e8d4b304f4165bfdf2)
- [a3](../platform_security_model_reference/P056_sip_svc_request_结构体.md#a6cd5c3cf895daad0c600544a903f2eb8)
- [a4](../platform_security_model_reference/P056_sip_svc_request_结构体.md#a8d827ae174a2b8f11b50c7e6f31c3708)
- [a5](../platform_security_model_reference/P056_sip_svc_request_结构体.md#a67c7626f24035b9cdfef24193e2442c6)
- [a6](../platform_security_model_reference/P056_sip_svc_request_结构体.md#a35198a51b070fb2acf76458568204ec1)
- [a7](../platform_security_model_reference/P056_sip_svc_request_结构体.md#af20b0881ec14973d7a6b79f3b146dc7a)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [resp_data_addr](../platform_security_model_reference/P056_sip_svc_request_结构体.md#a9b4cc837fbb958e93a900b58b2ea3a75)
- [resp_data_size](../platform_security_model_reference/P056_sip_svc_request_结构体.md#aff7c782bc6690ef134db4e4d999189a7)
- [priv_data](../platform_security_model_reference/P056_sip_svc_request_结构体.md#a0b70942fc037346bb5ee051484c21745)
- [sip_svc_response](../platform_security_model_reference/P057_sip_svc_response_结构体.md)
- [header](../platform_security_model_reference/P057_sip_svc_response_结构体.md#ab2a3ed6ec283ef83a2ad8ea8eea421be)
- [a0](../platform_security_model_reference/P057_sip_svc_response_结构体.md#a4f413e152dc2ef463140499164c3e410)
- [a1](../platform_security_model_reference/P057_sip_svc_response_结构体.md#abfb0f411524209388f79f35a82031e79)
- [a2](../platform_security_model_reference/P057_sip_svc_response_结构体.md#af973d08da13a7dcecf344f3f9d6f118e)
- [a3](../platform_security_model_reference/P057_sip_svc_response_结构体.md#aac8bb11e4661e59cbce0d6b5d50a0820)
- [resp_data_addr](../platform_security_model_reference/P057_sip_svc_response_结构体.md#a5b8a49d292e45ecdd81920c30b650c10)
- [resp_data_size](../platform_security_model_reference/P057_sip_svc_response_结构体.md#a2e8373be61b16ac4f4d013103539cceb)
- [priv_data](../platform_security_model_reference/P057_sip_svc_response_结构体.md#a992b3f936866852633569f9c8d37d6a0)
- [sip_svc_request::priv_data](../platform_security_model_reference/P056_sip_svc_request_结构体.md#a0b70942fc037346bb5ee051484c21745)
- [sip_svc_request::a6](../platform_security_model_reference/P056_sip_svc_request_结构体.md#a35198a51b070fb2acf76458568204ec1)
- [sip_svc_request::a1](../platform_security_model_reference/P056_sip_svc_request_结构体.md#a3b41176de28f042510d5ca5fc9c4678e)
- [sip_svc_request::a5](../platform_security_model_reference/P056_sip_svc_request_结构体.md#a67c7626f24035b9cdfef24193e2442c6)
- [sip_svc_request::a3](../platform_security_model_reference/P056_sip_svc_request_结构体.md#a6cd5c3cf895daad0c600544a903f2eb8)
- [sip_svc_request::a4](../platform_security_model_reference/P056_sip_svc_request_结构体.md#a8d827ae174a2b8f11b50c7e6f31c3708)
- [sip_svc_request::a0](../platform_security_model_reference/P056_sip_svc_request_结构体.md#a95e4d0bb03bfca90ea78fc19c581ef7f)
- [sip_svc_request::resp_data_addr](../platform_security_model_reference/P056_sip_svc_request_结构体.md#a9b4cc837fbb958e93a900b58b2ea3a75)
- [sip_svc_request::a2](../platform_security_model_reference/P056_sip_svc_request_结构体.md#aa20d78ab299064e8d4b304f4165bfdf2)
- [sip_svc_request::header](../platform_security_model_reference/P056_sip_svc_request_结构体.md#aa8c71f7af00dd3195d49c04df5cb3509)
- [sip_svc_request::a7](../platform_security_model_reference/P056_sip_svc_request_结构体.md#af20b0881ec14973d7a6b79f3b146dc7a)
- [sip_svc_request::resp_data_size](../platform_security_model_reference/P056_sip_svc_request_结构体.md#aff7c782bc6690ef134db4e4d999189a7)
- [sip_svc_response::resp_data_size](../platform_security_model_reference/P057_sip_svc_response_结构体.md#a2e8373be61b16ac4f4d013103539cceb)
- [sip_svc_response::a0](../platform_security_model_reference/P057_sip_svc_response_结构体.md#a4f413e152dc2ef463140499164c3e410)
- [sip_svc_response::resp_data_addr](../platform_security_model_reference/P057_sip_svc_response_结构体.md#a5b8a49d292e45ecdd81920c30b650c10)
- [sip_svc_response::priv_data](../platform_security_model_reference/P057_sip_svc_response_结构体.md#a992b3f936866852633569f9c8d37d6a0)
- [sip_svc_response::a3](../platform_security_model_reference/P057_sip_svc_response_结构体.md#aac8bb11e4661e59cbce0d6b5d50a0820)
- [sip_svc_response::header](../platform_security_model_reference/P057_sip_svc_response_结构体.md#ab2a3ed6ec283ef83a2ad8ea8eea421be)
- [sip_svc_response::a1](../platform_security_model_reference/P057_sip_svc_response_结构体.md#abfb0f411524209388f79f35a82031e79)
- [sip_svc_response::a2](../platform_security_model_reference/P057_sip_svc_response_结构体.md#af973d08da13a7dcecf344f3f9d6f118e)

---

[上一章](P789_sip_svc_driver.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P791_siwx91x-clock.h_源码浏览.md)
