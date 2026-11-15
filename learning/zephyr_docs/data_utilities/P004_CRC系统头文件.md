---
id: learning.zephyr-docs.data-utilities.page-4
title: CRC系统头文件
kind: reference
status: maintained
domains: [zephyr, data, development]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sys_2crc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_CRC系统头文件

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/sys_2crc_8h.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 4.1\_概述

CRC 计算函数（CRC Computation Function）头文件。

```c
#include <zephyr/types.h>
#include <stdbool.h>
#include <stddef.h>
#include <zephyr/sys/__assert.h>
```

[查看源码浏览译页](P005_CRC系统头文件源码.md)。

## 4.2\_声明与简介

<a id="r_a95b298c826cf96507e7b11a49c75b2cf"></a>

```c
#define CRC8_CCITT_INITIAL_VALUE 0xFF
```

[详细说明](#a95b298c826cf96507e7b11a49c75b2cf)。

<a id="r_a81e9e87b5f1705b252429981f49608ee"></a>

```c
#define CRC8_ROHC_INITIAL_VALUE 0xFF
```

[详细说明](#a81e9e87b5f1705b252429981f49608ee)。

<a id="r_a0f92c37af2ac3af5cbea2c2f259d0639"></a>

```c
#define CRC24_PGP_INITIAL_VALUE 0x00B704CEU
```

[详细说明](#a0f92c37af2ac3af5cbea2c2f259d0639)。

<a id="r_a9075e7134000a6fd75ea81b0c2b0218b"></a>

```c
#define CRC24_FINAL_VALUE_MASK 0x00FFFFFFU
```

[详细说明](#a9075e7134000a6fd75ea81b0c2b0218b)。

<a id="r_gabb5b050bda10c098420e9caeb06cf7c9"></a>

```c
#define CRC4_POLY 0x3
```

CRC 多项式定义（Polynomial Definitions）。

[详细说明](P003_CRC计算接口.md#gabb5b050bda10c098420e9caeb06cf7c9)。

<a id="r_ga22b1223f74a42065e1338a84a6adbf99"></a>

```c
#define CRC4_REFLECT_POLY 0xC
```

[`CRC4_TI`](P003_CRC计算接口.md#ggabc40e4ffd6da1175eb8ee8573a527edda3a8effe9651199c20669daf033bbe59f) 多项式（Polynomial）。

[详细说明](P003_CRC计算接口.md#ga22b1223f74a42065e1338a84a6adbf99)。

<a id="r_ga6f1d5ac13908ed2ab9863d8e985671c3"></a>

```c
#define CRC7_BE_POLY 0x09
```

[`CRC7_BE`](P003_CRC计算接口.md#ggabc40e4ffd6da1175eb8ee8573a527edda218e7d92cae035c594e267fb0ed0ae6a) 多项式（Polynomial）。

[详细说明](P003_CRC计算接口.md#ga6f1d5ac13908ed2ab9863d8e985671c3)。

<a id="r_gab38a1fd08a57ee1e0a425103725741d4"></a>

```c
#define CRC8_POLY 0x07
```

[`CRC8`](P003_CRC计算接口.md#ggabc40e4ffd6da1175eb8ee8573a527edda852cb403a2665ed279b28679f11567d8) 多项式（Polynomial）。

[详细说明](P003_CRC计算接口.md#gab38a1fd08a57ee1e0a425103725741d4)。

<a id="r_gab675a99a70abaaa1e62aee413ca5ad7c"></a>

```c
#define CRC8_REFLECT_POLY 0xE0
```

`CRC8_REFLECT` 多项式（Polynomial）。

[详细说明](P003_CRC计算接口.md#gab675a99a70abaaa1e62aee413ca5ad7c)。

<a id="r_ga1c4dbf04065186cf7222c6a31efbde75"></a>

```c
#define CRC16_POLY 0x8005
```

[`CRC16`](P003_CRC计算接口.md#ggabc40e4ffd6da1175eb8ee8573a527edda27369d6d16d5fdf2a44111924c019e11) 多项式（Polynomial）。

[详细说明](P003_CRC计算接口.md#ga1c4dbf04065186cf7222c6a31efbde75)。

<a id="r_gaa3cd24daeb5039bf1bf0bfaf8a4194bc"></a>

```c
#define CRC16_REFLECT_POLY 0xA001
```

[`CRC16_ANSI`](P003_CRC计算接口.md#ggabc40e4ffd6da1175eb8ee8573a527edda4a5e69eba1f74c0bd028356c9fb0f1f6) 多项式（Polynomial）。

[详细说明](P003_CRC计算接口.md#gaa3cd24daeb5039bf1bf0bfaf8a4194bc)。

<a id="r_ga85565a7b9f1ec670c38e569c48d585ca"></a>

```c
#define CRC16_CCITT_POLY 0x1021
```

CRC16_CCITT/CRC16_ITU_T 多项式（Polynomial）。

[详细说明](P003_CRC计算接口.md#ga85565a7b9f1ec670c38e569c48d585ca)。

<a id="r_ga9b6ca908d2643229cd8c4880630817c3"></a>

```c
#define CRC24_PGP_POLY 0x01864CFBU
```

[`CRC24_PGP`](P003_CRC计算接口.md#ggabc40e4ffd6da1175eb8ee8573a527eddac7805fb845479f192a855292bdb03f43) 多项式（Polynomial）。

[详细说明](P003_CRC计算接口.md#ga9b6ca908d2643229cd8c4880630817c3)。

<a id="r_gaa42328266fdb99a24af0ecbd0f824289"></a>

```c
#define CRC32_IEEE_POLY 0x04C11DB7U
```

[`CRC32_IEEE`](P003_CRC计算接口.md#ggabc40e4ffd6da1175eb8ee8573a527eddaecf71323e57da8d4f7e45d154b1059d8) 多项式（Polynomial）。

[详细说明](P003_CRC计算接口.md#gaa42328266fdb99a24af0ecbd0f824289)。

<a id="r_gaac41b271c0867fbdf5168a195ffc7693"></a>

```c
#define CRC32C_POLY 0x1EDC6F41U
```

`CRC32C` 多项式（Polynomial）。

[详细说明](P003_CRC计算接口.md#gaac41b271c0867fbdf5168a195ffc7693)。

<a id="r_gaff63e6fa586116d92a5b5469ed22dcac"></a>

```c
#define CRC32K_4_2_POLY 0x93A409EBU
```

[`CRC32_K_4_2`](P003_CRC计算接口.md#ggabc40e4ffd6da1175eb8ee8573a527edda5d04a93660d113893b7cc27ba48ba25b) 多项式（Polynomial）。

[详细说明](P003_CRC计算接口.md#gaff63e6fa586116d92a5b5469ed22dcac)。

## 4.3\_声明与简介

<a id="r_gabc40e4ffd6da1175eb8ee8573a527edd"></a>

```c
enum crc_type { CRC4 , CRC4_TI , CRC7_BE , CRC8 , CRC8_CCITT , CRC8_ROHC , CRC16 , CRC16_ANSI , CRC16_CCITT , CRC16_ITU_T , CRC24_PGP , CRC32_C , CRC32_IEEE , CRC32_K_4_2 , CRC32_MPEG2 }
```

CRC 算法枚举（Algorithm Enumeration）。

[详细说明](P003_CRC计算接口.md#gabc40e4ffd6da1175eb8ee8573a527edd)。

## 4.4\_声明与简介

<a id="r_ga204a779aa0c1a152763ea8edc6fc3a8c"></a>

```c
uint16_t crc16 (uint16_t poly, uint16_t seed, const uint8_t *src, size_t len)
```

计算 CRC-16 的通用函数，不对输入或输出进行位反射（Reflection）。

[详细说明](P003_CRC计算接口.md#ga204a779aa0c1a152763ea8edc6fc3a8c)。

<a id="r_gaccbcb5b80cf8deaac252474ecc6d9914"></a>

```c
uint16_t crc16_reflect (uint16_t poly, uint16_t seed, const uint8_t *src, size_t len)
```

计算 CRC-16 的通用函数，对输入和输出均作位反射。

[详细说明](P003_CRC计算接口.md#gaccbcb5b80cf8deaac252474ecc6d9914)。

<a id="r_gaa614e73ee7484ca0424fa7d14a54bbb6"></a>

```c
uint8_t crc8 (const uint8_t *src, size_t len, uint8_t polynomial, uint8_t initial_value, bool reversed)
```

计算 CRC-8 的通用函数。

[详细说明](P003_CRC计算接口.md#gaa614e73ee7484ca0424fa7d14a54bbb6)。

<a id="r_ga74fa5608612c629291d15bc00b1c411c"></a>

```c
uint16_t crc16_ccitt (uint16_t seed, const uint8_t *src, size_t len)
```

以多项式 0x1021 计算缓冲区校验和（Checksum），对输入和输出均作位反射。

[详细说明](P003_CRC计算接口.md#ga74fa5608612c629291d15bc00b1c411c)。

<a id="r_ga5502729e443496719de338e8b6692ac1"></a>

```c
uint16_t crc16_itu_t (uint16_t seed, const uint8_t *src, size_t len)
```

以多项式 0x1021 计算缓冲区校验和，不对输入或输出作位反射。

[详细说明](P003_CRC计算接口.md#ga5502729e443496719de338e8b6692ac1)。

<a id="r_gaac3ac50c029b656f5cc070e6c742601a"></a>

```c
static uint16_t crc16_ansi (const uint8_t *src, size_t len)
```

计算 CRC-16 的 ANSI（或 Modbus）变体。

[详细说明](P003_CRC计算接口.md#gaac3ac50c029b656f5cc070e6c742601a)。

<a id="r_gafc24e79ed7f978f5bb813091ef318982"></a>

```c
uint32_t crc32_ieee (const uint8_t *data, size_t len)
```

生成符合 IEEE 的 `CRC32` 校验和。

[详细说明](P003_CRC计算接口.md#gafc24e79ed7f978f5bb813091ef318982)。

<a id="r_ga17476d4af14603e322986ef603ce8530"></a>

```c
uint32_t crc32_ieee_update (uint32_t crc, const uint8_t *data, size_t len)
```

更新符合 IEEE 的 `CRC32` 校验和。

[详细说明](P003_CRC计算接口.md#ga17476d4af14603e322986ef603ce8530)。

<a id="r_ga88d510b3958aee0990ca345aba260bc1"></a>

```c
uint32_t crc32_c (uint32_t crc, const uint8_t *data, size_t len, bool first_pkt, bool last_pkt)
```

计算 `CRC32C`（Castagnoli）校验和。

[详细说明](P003_CRC计算接口.md#ga88d510b3958aee0990ca345aba260bc1)。

<a id="r_gaba2e753d07e6b17b5330ee56aa48962d"></a>

```c
uint32_t crc32_k_4_2_update (uint32_t crc, const uint8_t *data, size_t len)
```

更新 CRC-32K/4.2（*op，Koopman）校验和。

[详细说明](P003_CRC计算接口.md#gaba2e753d07e6b17b5330ee56aa48962d)。

<a id="r_gaee8a8a5c17b530efe9b331c5af97e2c8"></a>

```c
uint32_t crc32_mpeg2 (const uint8_t *data, size_t len)
```

生成 CRC-32/MPEG-2 校验和。

[详细说明](P003_CRC计算接口.md#gaee8a8a5c17b530efe9b331c5af97e2c8)。

<a id="r_ga8f5d481856e8d473772a6a417adedda7"></a>

```c
uint32_t crc32_mpeg2_update (uint32_t crc, const uint8_t *data, size_t len)
```

更新 CRC-32/MPEG-2 校验和。

[详细说明](P003_CRC计算接口.md#ga8f5d481856e8d473772a6a417adedda7)。

<a id="r_ga9a925de71cd0255a22c769dc4b130da5"></a>

```c
uint8_t crc8_ccitt (uint8_t initial_value, const void *buf, size_t len)
```

计算 CRC-8 的 CCITT 变体。

[详细说明](P003_CRC计算接口.md#ga9a925de71cd0255a22c769dc4b130da5)。

<a id="r_ga7a8f4387a2d0163165557446d018f041"></a>

```c
uint8_t crc8_rohc (uint8_t initial_value, const void *buf, size_t len)
```

计算 CRC-8 的 ROHC 变体。

[详细说明](P003_CRC计算接口.md#ga7a8f4387a2d0163165557446d018f041)。

<a id="r_ga1169005fd900b2787035044eeea38af1"></a>

```c
uint8_t crc7_be (uint8_t seed, const uint8_t *src, size_t len)
```

计算缓冲区的 CRC-7 校验和。

[详细说明](P003_CRC计算接口.md#ga1169005fd900b2787035044eeea38af1)。

<a id="r_ga322365098ec65bde3d55b0c059896668"></a>

```c
uint8_t crc4_ti (uint8_t seed, const uint8_t *src, size_t len)
```

计算缓冲区的 CRC-4 校验和。

[详细说明](P003_CRC计算接口.md#ga322365098ec65bde3d55b0c059896668)。

<a id="r_ga4458d7743f9a3394fb68cddcc100e456"></a>

```c
uint8_t crc4 (const uint8_t *src, size_t len, uint8_t polynomial, uint8_t initial_value, bool reversed)
```

计算 CRC-4 的通用函数。

[详细说明](P003_CRC计算接口.md#ga4458d7743f9a3394fb68cddcc100e456)。

<a id="r_gaebe7a9494dec69568b4f5cc95bf0fac2"></a>

```c
uint32_t crc24_pgp (const uint8_t *data, size_t len)
```

生成 RFC 4880 第6.1节定义的 OpenPGP CRC-24 校验和。

[详细说明](P003_CRC计算接口.md#gaebe7a9494dec69568b4f5cc95bf0fac2)。

<a id="r_ga4523b3cf8dbc05ea44258d1652fbb969"></a>

```c
uint32_t crc24_pgp_update (uint32_t crc, const uint8_t *data, size_t len)
```

更新 OpenPGP CRC-24 校验和。

[详细说明](P003_CRC计算接口.md#ga4523b3cf8dbc05ea44258d1652fbb969)。

<a id="r_ga04c2e17fed50a5e272d26a83426e9a57"></a>

```c
uint32_t crc24q_rtcm3 (const uint8_t *data, size_t len)
```

计算 RTCM3 的 `CRC24Q` 帧校验和（Frame Checksum）。

[详细说明](P003_CRC计算接口.md#ga04c2e17fed50a5e272d26a83426e9a57)。

<a id="r_ga5d7f493210e56fb18b8199c9d8a17f33"></a>

```c
static uint32_t crc_by_type (enum crc_type type, const uint8_t *src, size_t len, uint32_t seed, uint32_t poly, bool reflect, bool first, bool last)
```

以通用方式计算 CRC 校验和。

[详细说明](P003_CRC计算接口.md#ga5d7f493210e56fb18b8199c9d8a17f33)。

## 4.5\_CRC24\_FINAL\_VALUE\_MASK

<a id="a9075e7134000a6fd75ea81b0c2b0218b"></a>

```c
#define CRC24_FINAL_VALUE_MASK 0x00FFFFFFU
```


原页未提供额外说明。

## 4.6\_CRC24\_PGP\_INITIAL\_VALUE

<a id="a0f92c37af2ac3af5cbea2c2f259d0639"></a>

```c
#define CRC24_PGP_INITIAL_VALUE 0x00B704CEU
```


原页未提供额外说明。

## 4.7\_CRC8\_CCITT\_INITIAL\_VALUE

<a id="a95b298c826cf96507e7b11a49c75b2cf"></a>

```c
#define CRC8_CCITT_INITIAL_VALUE 0xFF
```


原页未提供额外说明。

## 4.8\_CRC8\_ROHC\_INITIAL\_VALUE

<a id="a81e9e87b5f1705b252429981f49608ee"></a>

```c
#define CRC8_ROHC_INITIAL_VALUE 0xFF
```


原页未提供额外说明。

## 4.9\_源码对照与相关阅读

译注：本仓库的[系统CRC头文件](../../../include/zephyr/sys/crc.h)和[CRC实现目录](../../../subsys/crc)可作源码跟踪。硬件驱动另见[CRC驱动接口](../hardware/P038_CRC驱动接口参考.md)。

[CRC概览](P001_CRC子系统概览.md) · [CRC计算接口](P003_CRC计算接口.md) · [系统头文件](P004_CRC系统头文件.md)。

本地引用从本文按相对路径解析，不绑定盘符或用户名；仓库版本不自动等同于官方 latest。本轮未执行 CRC 程序、随机性测试或熵源验证。

<a id="header-define-members"></a>
<a id="define-members"></a>
<a id="define-members-0"></a>
<a id="CRC_POLYNOMIAL"></a>
<a id="header-enum-members"></a>
<a id="enum-members"></a>
<a id="header-func-members"></a>
<a id="func-members"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

[上一章](P003_CRC计算接口.md) · [返回大纲](大纲.md) · [下一章](P005_CRC系统头文件源码.md)
