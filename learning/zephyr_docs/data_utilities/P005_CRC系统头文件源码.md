---
id: learning.zephyr-docs.data-utilities.page-5
title: CRC系统头文件源码
kind: reference
status: maintained
domains: [zephyr, data, development]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sys_2crc_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_CRC系统头文件源码

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/sys_2crc_8h_source.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 5.1\_阅读说明

译注：完整保留官方 Doxygen 源码浏览页展示的代码，仅移除展示行号、还原不换行空格并清除行尾空白。原网页本身省略了部分文档注释，原行号存在跳跃；这里不是另行下载的完整原始头文件。接口中文说明见[头文件参考](P004_CRC系统头文件.md)。

## 5.2\_源码展示

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
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
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00047"></a>
<a id="l00055"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00082"></a>
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
<a id="foldopen00106"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00173"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="foldopen00273"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00315"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="l00354"></a>
<a id="l00355"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00383"></a>
<a id="l00384"></a>
<a id="l00397"></a>
<a id="l00398"></a>
<a id="l00412"></a>
<a id="l00413"></a>
<a id="l00427"></a>
<a id="l00428"></a>
<a id="l00446"></a>
<a id="l00447"></a>
<a id="l00448"></a>
<a id="l00457"></a>
<a id="l00458"></a>
<a id="l00470"></a>
<a id="l00471"></a>
<a id="l00481"></a>
<a id="l00482"></a>
<a id="foldopen00505"></a>
<a id="l00505"></a>
<a id="l00506"></a>
<a id="l00507"></a>
<a id="l00508"></a>
<a id="l00509"></a>
<a id="l00510"></a>
<a id="l00511"></a>
<a id="l00512"></a>
<a id="l00513"></a>
<a id="l00514"></a>
<a id="l00515"></a>
<a id="l00516"></a>
<a id="l00517"></a>
<a id="l00518"></a>
<a id="l00519"></a>
<a id="l00520"></a>
<a id="l00521"></a>
<a id="l00522"></a>
<a id="l00523"></a>
<a id="l00524"></a>
<a id="l00525"></a>
<a id="l00526"></a>
<a id="l00527"></a>
<a id="l00528"></a>
<a id="l00529"></a>
<a id="l00530"></a>
<a id="l00531"></a>
<a id="l00532"></a>
<a id="l00533"></a>
<a id="l00534"></a>
<a id="l00535"></a>
<a id="l00536"></a>
<a id="l00537"></a>
<a id="l00538"></a>
<a id="l00539"></a>
<a id="l00540"></a>
<a id="l00541"></a>
<a id="l00542"></a>
<a id="l00543"></a>
<a id="l00544"></a>
<a id="l00545"></a>
<a id="l00546"></a>
<a id="l00547"></a>
<a id="l00548"></a>
<a id="l00549"></a>
<a id="l00550"></a>
<a id="l00551"></a>
<a id="l00552"></a>
<a id="l00553"></a>
<a id="l00554"></a>
<a id="l00555"></a>
<a id="l00556"></a>
<a id="l00557"></a>
<a id="l00561"></a>
<a id="l00562"></a>
<a id="l00563"></a>
<a id="l00564"></a>
<a id="l00565"></a>
<a id="l00566"></a>
<a id="agroup__crc_html_ga04c2e17fed50a5e272d26a83426e9a57"></a>
<a id="agroup__crc_html_ga1169005fd900b2787035044eeea38af1"></a>
<a id="agroup__crc_html_ga17476d4af14603e322986ef603ce8530"></a>
<a id="agroup__crc_html_ga204a779aa0c1a152763ea8edc6fc3a8c"></a>
<a id="agroup__crc_html_ga322365098ec65bde3d55b0c059896668"></a>
<a id="agroup__crc_html_ga4458d7743f9a3394fb68cddcc100e456"></a>
<a id="agroup__crc_html_ga4523b3cf8dbc05ea44258d1652fbb969"></a>
<a id="agroup__crc_html_ga5502729e443496719de338e8b6692ac1"></a>
<a id="agroup__crc_html_ga5d7f493210e56fb18b8199c9d8a17f33"></a>
<a id="agroup__crc_html_ga74fa5608612c629291d15bc00b1c411c"></a>
<a id="agroup__crc_html_ga7a8f4387a2d0163165557446d018f041"></a>
<a id="agroup__crc_html_ga88d510b3958aee0990ca345aba260bc1"></a>
<a id="agroup__crc_html_ga8f5d481856e8d473772a6a417adedda7"></a>
<a id="agroup__crc_html_ga9a925de71cd0255a22c769dc4b130da5"></a>
<a id="agroup__crc_html_gaa614e73ee7484ca0424fa7d14a54bbb6"></a>
<a id="agroup__crc_html_gaac3ac50c029b656f5cc070e6c742601a"></a>
<a id="agroup__crc_html_gaba2e753d07e6b17b5330ee56aa48962d"></a>
<a id="agroup__crc_html_gabc40e4ffd6da1175eb8ee8573a527edd"></a>
<a id="agroup__crc_html_gaccbcb5b80cf8deaac252474ecc6d9914"></a>
<a id="agroup__crc_html_gaebe7a9494dec69568b4f5cc95bf0fac2"></a>
<a id="agroup__crc_html_gaee8a8a5c17b530efe9b331c5af97e2c8"></a>
<a id="agroup__crc_html_gafc24e79ed7f978f5bb813091ef318982"></a>
<a id="agroup__crc_html_ggabc40e4ffd6da1175eb8ee8573a527edda218e7d92cae035c594e267fb0ed0ae6a"></a>
<a id="agroup__crc_html_ggabc40e4ffd6da1175eb8ee8573a527edda27369d6d16d5fdf2a44111924c019e11"></a>
<a id="agroup__crc_html_ggabc40e4ffd6da1175eb8ee8573a527edda3a8effe9651199c20669daf033bbe59f"></a>
<a id="agroup__crc_html_ggabc40e4ffd6da1175eb8ee8573a527edda3fdbd9451fc39959f46714a2f46ca42c"></a>
<a id="agroup__crc_html_ggabc40e4ffd6da1175eb8ee8573a527edda4036b6c556c8aa1307c1ff7ff1626148"></a>
<a id="agroup__crc_html_ggabc40e4ffd6da1175eb8ee8573a527edda4a5e69eba1f74c0bd028356c9fb0f1f6"></a>
<a id="agroup__crc_html_ggabc40e4ffd6da1175eb8ee8573a527edda5d04a93660d113893b7cc27ba48ba25b"></a>
<a id="agroup__crc_html_ggabc40e4ffd6da1175eb8ee8573a527edda852cb403a2665ed279b28679f11567d8"></a>
<a id="agroup__crc_html_ggabc40e4ffd6da1175eb8ee8573a527eddac7805fb845479f192a855292bdb03f43"></a>
<a id="agroup__crc_html_ggabc40e4ffd6da1175eb8ee8573a527eddacdf0c4de024efc53edd374ad22c6da30"></a>
<a id="agroup__crc_html_ggabc40e4ffd6da1175eb8ee8573a527eddad0cba27d3a1347c21fc34cfd3aa0eab5"></a>
<a id="agroup__crc_html_ggabc40e4ffd6da1175eb8ee8573a527eddae00c2275c0a5ac47b64c221feadfc3eb"></a>
<a id="agroup__crc_html_ggabc40e4ffd6da1175eb8ee8573a527eddae06f6bdc6b6e1e4c16b21c358e807ca6"></a>
<a id="agroup__crc_html_ggabc40e4ffd6da1175eb8ee8573a527eddaecf71323e57da8d4f7e45d154b1059d8"></a>
<a id="agroup__crc_html_ggabc40e4ffd6da1175eb8ee8573a527eddaef5caa552f890f4c7e887dfe1a06bc22"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="asys_2crc_8h_html_a9075e7134000a6fd75ea81b0c2b0218b"></a>

```c
/*
 * Copyright (c) 2018 Workaround GmbH.
 * Copyright (c) 2017 Intel Corporation.
 * Copyright (c) 2017 Nordic Semiconductor ASA
 * Copyright (c) 2015 Runtime Inc
 * Copyright (c) 2018 Google LLC.
 * Copyright (c) 2022 Meta
 * Copyright (c) 2024 Intercreate, Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_SYS_CRC_H_
#define ZEPHYR_INCLUDE_SYS_CRC_H_

#include <zephyr/types.h>
#include <stdbool.h>
#include <stddef.h>

#include <zephyr/sys/__assert.h>

#ifdef __cplusplus
extern "C" {
#endif

/* Initial value expected to be used at the beginning of the crc8_ccitt
 * computation.
 */
#define CRC8_CCITT_INITIAL_VALUE 0xFF
#define CRC8_ROHC_INITIAL_VALUE  0xFF

/* Initial value expected to be used at the beginning of the OpenPGP CRC-24 computation. */
#define CRC24_PGP_INITIAL_VALUE 0x00B704CEU
/*
 * The CRC-24 value is stored on a 32-bit value, only the 3 least significant bytes
 * are meaningful. Use the following mask to only keep the CRC-24 value.
 */
#define CRC24_FINAL_VALUE_MASK 0x00FFFFFFU




#define CRC4_POLY 0x3

#define CRC4_REFLECT_POLY 0xC

#define CRC7_BE_POLY 0x09

#define CRC8_POLY 0x07

#define CRC8_REFLECT_POLY 0xE0

#define CRC16_POLY 0x8005

#define CRC16_REFLECT_POLY 0xA001

#define CRC16_CCITT_POLY 0x1021

#define CRC24_PGP_POLY 0x01864CFBU

#define CRC32_IEEE_POLY 0x04C11DB7U

#define CRC32C_POLY 0x1EDC6F41U

#define CRC32K_4_2_POLY 0x93A409EBU


enum crc_type {
        CRC4,
        CRC4_TI,
        CRC7_BE,
        CRC8,
        CRC8_CCITT,
        CRC8_ROHC,
        CRC16,
        CRC16_ANSI,
        CRC16_CCITT,
        CRC16_ITU_T,
        CRC24_PGP,
        CRC32_C,
        CRC32_IEEE,
        CRC32_K_4_2,
        CRC32_MPEG2,
};

uint16_t crc16(uint16_t poly, uint16_t seed, const uint8_t *src, size_t len);

uint16_t crc16_reflect(uint16_t poly, uint16_t seed, const uint8_t *src, size_t len);
uint8_t crc8(const uint8_t *src, size_t len, uint8_t polynomial, uint8_t initial_value,
             bool reversed);

uint16_t crc16_ccitt(uint16_t seed, const uint8_t *src, size_t len);

uint16_t crc16_itu_t(uint16_t seed, const uint8_t *src, size_t len);

static inline uint16_t crc16_ansi(const uint8_t *src, size_t len)
{
        return crc16_reflect(0xA001, 0xffff, src, len);
}

uint32_t crc32_ieee(const uint8_t *data, size_t len);

uint32_t crc32_ieee_update(uint32_t crc, const uint8_t *data, size_t len);

uint32_t crc32_c(uint32_t crc, const uint8_t *data,
                 size_t len, bool first_pkt, bool last_pkt);

uint32_t crc32_k_4_2_update(uint32_t crc, const uint8_t *data, size_t len);

uint32_t crc32_mpeg2(const uint8_t *data, size_t len);

uint32_t crc32_mpeg2_update(uint32_t crc, const uint8_t *data, size_t len);

uint8_t crc8_ccitt(uint8_t initial_value, const void *buf, size_t len);

uint8_t crc8_rohc(uint8_t initial_value, const void *buf, size_t len);

uint8_t crc7_be(uint8_t seed, const uint8_t *src, size_t len);

uint8_t crc4_ti(uint8_t seed, const uint8_t *src, size_t len);

uint8_t crc4(const uint8_t *src, size_t len, uint8_t polynomial, uint8_t initial_value,
             bool reversed);

uint32_t crc24_pgp(const uint8_t *data, size_t len);

uint32_t crc24_pgp_update(uint32_t crc, const uint8_t *data, size_t len);

uint32_t crc24q_rtcm3(const uint8_t *data, size_t len);

static inline uint32_t crc_by_type(enum crc_type type, const uint8_t *src, size_t len,
                                   uint32_t seed, uint32_t poly, bool reflect, bool first,
                                   bool last)
{
        switch (type) {
        case CRC4:
                return crc4(src, len, poly, seed, reflect);
        case CRC4_TI:
                return crc4_ti(seed, src, len);
        case CRC7_BE:
                return crc7_be(seed, src, len);
        case CRC8:
                return crc8(src, len, poly, seed, reflect);
        case CRC8_CCITT:
                return crc8_ccitt(seed, src, len);
        case CRC8_ROHC:
                return crc8_rohc(seed, src, len);
        case CRC16:
                if (reflect) {
                        return crc16_reflect(poly, seed, src, len);
                } else {
                        return crc16(poly, seed, src, len);
                }
        case CRC16_ANSI:
                return crc16_ansi(src, len);
        case CRC16_CCITT:
                return crc16_ccitt(seed, src, len);
        case CRC16_ITU_T:
                return crc16_itu_t(seed, src, len);
        case CRC24_PGP: {
                uint32_t crc = crc24_pgp_update(seed, src, len);

                if (last) {
                        crc &= CRC24_FINAL_VALUE_MASK;
                }
                return crc;
        }
        case CRC32_C:
                return crc32_c(seed, src, len, first, last);
        case CRC32_IEEE:
                return crc32_ieee_update(seed, src, len);
        case CRC32_K_4_2:
                return crc32_k_4_2_update(seed, src, len);
        case CRC32_MPEG2:
                return crc32_mpeg2_update(seed, src, len);
        default:
                break;
        }

        __ASSERT_NO_MSG(false);
        return -1;
}


#ifdef __cplusplus
}
#endif

#endif
```

## 5.3\_源码注释译文

版权声明分别为：2018年 Workaround GmbH；2017年 Intel Corporation；2017年 Nordic Semiconductor ASA；2015年 Runtime Inc；2018年 Google LLC；2022年 Meta；2024年 Intercreate, Inc.。SPDX许可标识为 Apache-2.0。原法律声明完整保留。

其余普通注释依次说明：crc8_ccitt 计算开始时应使用的初始值；OpenPGP CRC-24 计算开始时应使用的初始值；CRC-24 保存在32位数值中，但仅最低3个字节有意义，使用给出的掩码可只保留 CRC-24 值。

## 5.4\_源码对照与相关阅读

译注：本仓库的[系统CRC头文件](../../../include/zephyr/sys/crc.h)和[CRC实现目录](../../../subsys/crc)可作源码跟踪。硬件驱动另见[CRC驱动接口](../hardware/P038_CRC驱动接口参考.md)。

[CRC概览](P001_CRC子系统概览.md) · [CRC计算接口](P003_CRC计算接口.md) · [系统头文件](P004_CRC系统头文件.md)。

本地引用从本文按相对路径解析，不绑定盘符或用户名；仓库版本不自动等同于官方 latest。本轮未执行 CRC 程序、随机性测试或熵源验证。

[上一章](P004_CRC系统头文件.md) · [返回大纲](大纲.md) · [下一章](P006_随机数生成.md)
