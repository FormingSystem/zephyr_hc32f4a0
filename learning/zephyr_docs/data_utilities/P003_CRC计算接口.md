---
id: learning.zephyr-docs.data-utilities.page-3
title: CRC计算接口
kind: reference
status: maintained
domains: [zephyr, data, development]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__crc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_CRC计算接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__crc.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 3.1\_概述

循环冗余校验（Cyclic Redundancy Check，CRC）计算接口。原文标注：自1.8版本起提供（Since），接口版本（Version）为1.0.0。

```c
#include <zephyr/sys/crc.h>
```

译注：位反射（Reflection）表示按位反转的处理；种子、反射、多项式和最终异或（Final XOR）共同确定具体变体。CRC 名称中的 ANSI、IEEE、ITU-T／CCITT 等标识沿用原命名，应以本页参数说明确认算法，而非只按简称推断。

## 3.2\_CRC16\_CCITT\_POLY

<a id="ga85565a7b9f1ec670c38e569c48d585ca"></a>
<a id="r_ga85565a7b9f1ec670c38e569c48d585ca"></a>

```c
#define CRC16_CCITT_POLY 0x1021
```

```c
#include <zephyr/sys/crc.h>
```

CRC16_CCITT/CRC16_ITU_T 多项式（Polynomial）。


## 3.3\_CRC16\_POLY

<a id="ga1c4dbf04065186cf7222c6a31efbde75"></a>
<a id="r_ga1c4dbf04065186cf7222c6a31efbde75"></a>

```c
#define CRC16_POLY 0x8005
```

```c
#include <zephyr/sys/crc.h>
```

[`CRC16`](#ggabc40e4ffd6da1175eb8ee8573a527edda27369d6d16d5fdf2a44111924c019e11) 多项式（Polynomial）。


## 3.4\_CRC16\_REFLECT\_POLY

<a id="gaa3cd24daeb5039bf1bf0bfaf8a4194bc"></a>
<a id="r_gaa3cd24daeb5039bf1bf0bfaf8a4194bc"></a>

```c
#define CRC16_REFLECT_POLY 0xA001
```

```c
#include <zephyr/sys/crc.h>
```

[`CRC16_ANSI`](#ggabc40e4ffd6da1175eb8ee8573a527edda4a5e69eba1f74c0bd028356c9fb0f1f6) 多项式（Polynomial）。


## 3.5\_CRC24\_PGP\_POLY

<a id="ga9b6ca908d2643229cd8c4880630817c3"></a>
<a id="r_ga9b6ca908d2643229cd8c4880630817c3"></a>

```c
#define CRC24_PGP_POLY 0x01864CFBU
```

```c
#include <zephyr/sys/crc.h>
```

[`CRC24_PGP`](#ggabc40e4ffd6da1175eb8ee8573a527eddac7805fb845479f192a855292bdb03f43) 多项式（Polynomial）。


## 3.6\_CRC32\_IEEE\_POLY

<a id="gaa42328266fdb99a24af0ecbd0f824289"></a>
<a id="r_gaa42328266fdb99a24af0ecbd0f824289"></a>

```c
#define CRC32_IEEE_POLY 0x04C11DB7U
```

```c
#include <zephyr/sys/crc.h>
```

[`CRC32_IEEE`](#ggabc40e4ffd6da1175eb8ee8573a527eddaecf71323e57da8d4f7e45d154b1059d8) 多项式（Polynomial）。


## 3.7\_CRC32C\_POLY

<a id="gaac41b271c0867fbdf5168a195ffc7693"></a>
<a id="r_gaac41b271c0867fbdf5168a195ffc7693"></a>

```c
#define CRC32C_POLY 0x1EDC6F41U
```

```c
#include <zephyr/sys/crc.h>
```

`CRC32C` 多项式（Polynomial）。


## 3.8\_CRC32K\_4\_2\_POLY

<a id="gaff63e6fa586116d92a5b5469ed22dcac"></a>
<a id="r_gaff63e6fa586116d92a5b5469ed22dcac"></a>

```c
#define CRC32K_4_2_POLY 0x93A409EBU
```

```c
#include <zephyr/sys/crc.h>
```

[`CRC32_K_4_2`](#ggabc40e4ffd6da1175eb8ee8573a527edda5d04a93660d113893b7cc27ba48ba25b) 多项式（Polynomial）。


## 3.9\_CRC4\_POLY

<a id="gabb5b050bda10c098420e9caeb06cf7c9"></a>
<a id="r_gabb5b050bda10c098420e9caeb06cf7c9"></a>

```c
#define CRC4_POLY 0x3
```

```c
#include <zephyr/sys/crc.h>
```

CRC 多项式定义（Polynomial Definitions）。

[`CRC4`](#ggabc40e4ffd6da1175eb8ee8573a527eddaef5caa552f890f4c7e887dfe1a06bc22) 多项式（Polynomial）。


## 3.10\_CRC4\_REFLECT\_POLY

<a id="ga22b1223f74a42065e1338a84a6adbf99"></a>
<a id="r_ga22b1223f74a42065e1338a84a6adbf99"></a>

```c
#define CRC4_REFLECT_POLY 0xC
```

```c
#include <zephyr/sys/crc.h>
```

[`CRC4_TI`](#ggabc40e4ffd6da1175eb8ee8573a527edda3a8effe9651199c20669daf033bbe59f) 多项式（Polynomial）。


## 3.11\_CRC7\_BE\_POLY

<a id="ga6f1d5ac13908ed2ab9863d8e985671c3"></a>
<a id="r_ga6f1d5ac13908ed2ab9863d8e985671c3"></a>

```c
#define CRC7_BE_POLY 0x09
```

```c
#include <zephyr/sys/crc.h>
```

[`CRC7_BE`](#ggabc40e4ffd6da1175eb8ee8573a527edda218e7d92cae035c594e267fb0ed0ae6a) 多项式（Polynomial）。


## 3.12\_CRC8\_POLY

<a id="gab38a1fd08a57ee1e0a425103725741d4"></a>
<a id="r_gab38a1fd08a57ee1e0a425103725741d4"></a>

```c
#define CRC8_POLY 0x07
```

```c
#include <zephyr/sys/crc.h>
```

[`CRC8`](#ggabc40e4ffd6da1175eb8ee8573a527edda852cb403a2665ed279b28679f11567d8) 多项式（Polynomial）。


## 3.13\_CRC8\_REFLECT\_POLY

<a id="gab675a99a70abaaa1e62aee413ca5ad7c"></a>
<a id="r_gab675a99a70abaaa1e62aee413ca5ad7c"></a>

```c
#define CRC8_REFLECT_POLY 0xE0
```

```c
#include <zephyr/sys/crc.h>
```

`CRC8_REFLECT` 多项式（Polynomial）。


## 3.14\_crc\_type

<a id="gabc40e4ffd6da1175eb8ee8573a527edd"></a>
<a id="r_gabc40e4ffd6da1175eb8ee8573a527edd"></a>

```c
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
```

```c
#include <zephyr/sys/crc.h>
```

CRC 算法枚举（Algorithm Enumeration）。

这些枚举值用于 CRC 分派函数（Dispatch Function）。


**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `CRC4` | 使用 [`crc4`](#ga4458d7743f9a3394fb68cddcc100e456)。 |
| `CRC4_TI` | 使用 [`crc4_ti`](#ga322365098ec65bde3d55b0c059896668)。 |
| `CRC7_BE` | 使用 [`crc7_be`](#ga1169005fd900b2787035044eeea38af1)。 |
| `CRC8` | 使用 [`crc8`](#gaa614e73ee7484ca0424fa7d14a54bbb6)。 |
| `CRC8_CCITT` | 使用 [`crc8_ccitt`](#ga9a925de71cd0255a22c769dc4b130da5)。 |
| `CRC8_ROHC` | 使用 [`crc8_rohc`](#ga7a8f4387a2d0163165557446d018f041)。 |
| `CRC16` | 使用 [`crc16`](#ga204a779aa0c1a152763ea8edc6fc3a8c)。 |
| `CRC16_ANSI` | 使用 [`crc16_ansi`](#gaac3ac50c029b656f5cc070e6c742601a)。 |
| `CRC16_CCITT` | 使用 [`crc16_ccitt`](#ga74fa5608612c629291d15bc00b1c411c)。 |
| `CRC16_ITU_T` | 使用 [`crc16_itu_t`](#ga5502729e443496719de338e8b6692ac1)。 |
| `CRC24_PGP` | 使用 [`crc24_pgp`](#gaebe7a9494dec69568b4f5cc95bf0fac2)。 |
| `CRC32_C` | 使用 [`crc32_c`](#ga88d510b3958aee0990ca345aba260bc1)。 |
| `CRC32_IEEE` | 使用 [`crc32_ieee`](#gafc24e79ed7f978f5bb813091ef318982)。 |
| `CRC32_K_4_2` | 使用 [`crc32_k_4_2_update`](#gaba2e753d07e6b17b5330ee56aa48962d)。 |
| `CRC32_MPEG2` | 使用 [`crc32_mpeg2`](#gaee8a8a5c17b530efe9b331c5af97e2c8)。 |

## 3.15\_crc16()

<a id="ga204a779aa0c1a152763ea8edc6fc3a8c"></a>
<a id="r_ga204a779aa0c1a152763ea8edc6fc3a8c"></a>

```c
uint16_t crc16 ( uint16_t poly, uint16_t seed, const uint8_t * src, size_t len )
```

```c
#include <zephyr/sys/crc.h>
```

计算 CRC-16 的通用函数，不对输入或输出进行位反射（Reflection）。

传入输入地址、输入长度、多项式和初始值以计算 CRC-16。复杂度为 `O(n*8)`，其中 n 为缓冲区长度。不执行位反射。


**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `poly` | 使用的多项式，省略最高次项 x^16 的系数。 |
| `seed` | CRC 计算的初始值（Initial Value）。 |
| `src` | 计算所用的输入字节。 |
| `len` | 输入长度，单位为字节。 |

**原文注意（Note）**：若要使用基于多项式 0x1021 的 CRC，[`crc16_itu_t`](#ga5502729e443496719de338e8b6692ac1)() 更快，因此推荐使用它。

**返回（Returns）**：返回计算得到的 [`CRC16`](#ggabc40e4ffd6da1175eb8ee8573a527edda27369d6d16d5fdf2a44111924c019e11) 值，不进行任何最终异或（XOR）处理。

## 3.16\_crc16\_ansi()

<a id="gaac3ac50c029b656f5cc070e6c742601a"></a>
<a id="r_gaac3ac50c029b656f5cc070e6c742601a"></a>

```c
static inline uint16_t crc16_ansi ( const uint8_t * src, size_t len )
```

```c
#include <zephyr/sys/crc.h>
```

计算 CRC-16 的 ANSI（或 Modbus）变体。

CRC-16 的 ANSI 变体使用多项式 0x8005，反射形式为 0xA001，初始值设为 0xffff。


**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `src` | 计算所用的输入字节。 |
| `len` | 输入长度，单位为字节。 |

**返回（Returns）**：返回计算得到的 [`CRC16`](#ggabc40e4ffd6da1175eb8ee8573a527edda27369d6d16d5fdf2a44111924c019e11) 值。

## 3.17\_crc16\_ccitt()

<a id="ga74fa5608612c629291d15bc00b1c411c"></a>
<a id="r_ga74fa5608612c629291d15bc00b1c411c"></a>

```c
uint16_t crc16_ccitt ( uint16_t seed, const uint8_t * src, size_t len )
```

```c
#include <zephyr/sys/crc.h>
```

以多项式 0x1021 计算缓冲区校验和（Checksum），对输入和输出均作位反射。

此函数可计算采用多项式 0x1021、且要求对输入和输出均进行位反射的 CRC。它是一个快速变体，时间复杂度为 `O(n)`，其中 n 为输入缓冲区长度。

根据提供的初始种子（Initial Seed）以及与最终 CRC 进行异或的值，本函数可计算下列校验和及其他变体：

参见 ITU-T 建议 V.41（1988年11月）。

- CRC-16/CCITT, CRC-16/CCITT-TRUE, CRC-16/KERMIT [变体资料](https://reveng.sourceforge.io/crc-catalogue/16.htm#crc.cat.crc-16-kermit) 初始种子： 0x0000, 输出异或值： 0x0000。
- CRC-16/X-25, CRC-16/IBM-SDLC, CRC-16/ISO-HDLC [变体资料](https://reveng.sourceforge.io/crc-catalogue/16.htm#crc.cat.crc-16-ibm-sdlc) 初始种子： 0xffff, 输出异或值： 0xffff。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `seed` | CRC 的种子值。 |
| `src` | 计算所用的输入字节。 |
| `len` | 输入长度，单位为字节。 |

**原文注意（Note）**：跨多个不连续数据块计算 CRC 时，使用第 N-1 块的返回值作为第 N 块的种子。

**返回（Returns）**：返回计算得到的 [`CRC16`](#ggabc40e4ffd6da1175eb8ee8573a527edda27369d6d16d5fdf2a44111924c019e11) 值，不进行任何最终异或（XOR）处理。

## 3.18\_crc16\_itu\_t()

<a id="ga5502729e443496719de338e8b6692ac1"></a>
<a id="r_ga5502729e443496719de338e8b6692ac1"></a>

```c
uint16_t crc16_itu_t ( uint16_t seed, const uint8_t * src, size_t len )
```

```c
#include <zephyr/sys/crc.h>
```

以多项式 0x1021 计算缓冲区校验和，不对输入或输出作位反射。

此函数可计算采用多项式 0x1021、且输入和输出均不进行位反射的 CRC。它是一个快速变体，时间复杂度为 `O(n)`，其中 n 为输入缓冲区长度。

根据提供的初始种子（Initial Seed）以及与最终 CRC 进行异或的值，本函数可计算下列校验和及其他变体：

参见 ITU-T 建议 V.41（1988年11月），采用最高有效位优先（Most Significant Bit First，MSB-`first`）。

- CRC-16/XMODEM, CRC-16/ACORN, CRC-16/LTE [变体资料](https://reveng.sourceforge.io/crc-catalogue/16.htm#crc.cat.crc-16-xmodem) 初始种子： 0x0000, 输出异或值： 0x0000。
- CRC16/CCITT-FALSE, CRC-16/IBM-3740, CRC-16/AUTOSAR [变体资料](https://reveng.sourceforge.io/crc-catalogue/16.htm#crc.cat.crc-16-ibm-3740) 初始种子： 0xffff, 输出异或值： 0x0000。
- CRC-16/GSM [变体资料](https://reveng.sourceforge.io/crc-catalogue/16.htm#crc.cat.crc-16-gsm) 初始种子： 0x0000, 输出异或值： 0xffff。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `seed` | CRC 的种子值。 |
| `src` | 计算所用的输入字节。 |
| `len` | 输入长度，单位为字节。 |

**原文注意（Note）**：跨多个不连续数据块计算 CRC 时，使用第 N-1 块的返回值作为第 N 块的种子。

**返回（Returns）**：返回计算得到的 [`CRC16`](#ggabc40e4ffd6da1175eb8ee8573a527edda27369d6d16d5fdf2a44111924c019e11) 值，不进行任何最终异或（XOR）处理。

## 3.19\_crc16\_reflect()

<a id="gaccbcb5b80cf8deaac252474ecc6d9914"></a>
<a id="r_gaccbcb5b80cf8deaac252474ecc6d9914"></a>

```c
uint16_t crc16_reflect ( uint16_t poly, uint16_t seed, const uint8_t * src, size_t len )
```

```c
#include <zephyr/sys/crc.h>
```

计算 CRC-16 的通用函数，对输入和输出均作位反射。

传入输入地址、输入长度、多项式和初始值以计算 CRC-16。复杂度为 `O(n*8)`，其中 n 为缓冲区长度。输入和输出均进行位反射。

根据提供的初始种子（Initial Seed）以及与最终 CRC 进行异或的值，本函数可计算下列校验和及其他变体：

- CRC-16/ANSI, CRC-16/MODBUS, CRC-16/USB, CRC-16/IBM [变体资料](https://reveng.sourceforge.io/crc-catalogue/16.htm#crc.cat.crc-16-modbus) 多项式： 0x8005 (0xA001) 初始种子： 0xffff, 输出异或值： 0x0000。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `poly` | 使用的多项式，省略最高次项 x^16 的系数。注意必须传入反射形式，例如 CRC-16-MODBUS 应使用 0xA001，而非 0x8005。 |
| `seed` | CRC 计算的初始值（Initial Value）。 |
| `src` | 计算所用的输入字节。 |
| `len` | 输入长度，单位为字节。 |

**原文注意（Note）**：若要使用基于多项式 0x1021 的 CRC，[`crc16_ccitt`](#ga74fa5608612c629291d15bc00b1c411c)() 更快，因此推荐使用它。

**返回（Returns）**：返回计算得到的 [`CRC16`](#ggabc40e4ffd6da1175eb8ee8573a527edda27369d6d16d5fdf2a44111924c019e11) 值，不进行任何最终异或（XOR）处理。

> 译注：原文把 ANSI、MODBUS、USB、IBM 等名称列在同一条目中；本函数可通过不同种子和最终异或值计算不同变体，不能据这一并列写法断言它们的全部参数相同。列出的链接指向 MODBUS 条目。

## 3.20\_crc24\_pgp()

<a id="gaebe7a9494dec69568b4f5cc95bf0fac2"></a>
<a id="r_gaebe7a9494dec69568b4f5cc95bf0fac2"></a>

```c
uint32_t crc24_pgp ( const uint8_t * data, size_t len )
```

```c
#include <zephyr/sys/crc.h>
```

生成 RFC 4880 第6.1节定义的 OpenPGP CRC-24 校验和。


**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `data` | 要计算 CRC 的数据指针。 |
| `len` | 数据长度，单位为字节。 |

**返回（Returns）**：返回 CRC-24 值。

## 3.21\_crc24\_pgp\_update()

<a id="ga4523b3cf8dbc05ea44258d1652fbb969"></a>
<a id="r_ga4523b3cf8dbc05ea44258d1652fbb969"></a>

```c
uint32_t crc24_pgp_update ( uint32_t crc, const uint8_t * data, size_t len )
```

```c
#include <zephyr/sys/crc.h>
```

更新 OpenPGP CRC-24 校验和。


**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `crc（原页显示 CRC）` | 要更新的 CRC-24 校验和。多次调用之间必须使用完整32位 CRC 值，不要通过掩码仅保留低24位。 |
| `data` | 要计算 CRC 的数据指针。 |
| `len` | 数据长度，单位为字节。 |

**返回（Returns）**：返回 CRC-24 值。处理完最后一个数据缓冲区后，使用 `CRC24_FINAL_VALUE_MASK` 掩码，只保留 CRC 结果中有意义的24位。

> 译注：中间状态要保留完整32位，只有全部数据处理结束后才应用 `CRC24_FINAL_VALUE_MASK`；过早截断会破坏后续更新。

## 3.22\_crc24q\_rtcm3()

<a id="ga04c2e17fed50a5e272d26a83426e9a57"></a>
<a id="r_ga04c2e17fed50a5e272d26a83426e9a57"></a>

```c
uint32_t crc24q_rtcm3 ( const uint8_t * data, size_t len )
```

```c
#include <zephyr/sys/crc.h>
```

计算 RTCM3 的 `CRC24Q` 帧校验和（Frame Checksum）。


**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] data` | RTCM3 帧。 |
| `[in] len` | 帧长度，单位为字节。 |

**返回（Returns）**：若数据帧包含校验和且校验匹配，则返回 0；若数据帧不包含校验和，则返回计算结果。

## 3.23\_crc32\_c()

<a id="ga88d510b3958aee0990ca345aba260bc1"></a>
<a id="r_ga88d510b3958aee0990ca345aba260bc1"></a>

```c
uint32_t crc32_c ( uint32_t crc, const uint8_t * data, size_t len, bool first_pkt, bool last_pkt )
```

```c
#include <zephyr/sys/crc.h>
```

计算 `CRC32C`（Castagnoli）校验和。


**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `crc（原页显示 CRC）` | 要更新的 `CRC32C` 校验和。 |
| `data` | 要计算 CRC 的数据指针。 |
| `len` | 数据长度。 |
| `first_pkt` | 是否为数据流中的第一个分组（Packet）。 |
| `last_pkt` | 是否为数据流中的最后一个分组。 |

**返回（Returns）**：返回 `CRC32` 值。

## 3.24\_crc32\_ieee()

<a id="gafc24e79ed7f978f5bb813091ef318982"></a>
<a id="r_gafc24e79ed7f978f5bb813091ef318982"></a>

```c
uint32_t crc32_ieee ( const uint8_t * data, size_t len )
```

```c
#include <zephyr/sys/crc.h>
```

生成符合 IEEE 的 `CRC32` 校验和。


**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `data` | 要计算 CRC 的数据指针。 |
| `len` | 数据长度。 |

**返回（Returns）**：返回 `CRC32` 值。

## 3.25\_crc32\_ieee\_update()

<a id="ga17476d4af14603e322986ef603ce8530"></a>
<a id="r_ga17476d4af14603e322986ef603ce8530"></a>

```c
uint32_t crc32_ieee_update ( uint32_t crc, const uint8_t * data, size_t len )
```

```c
#include <zephyr/sys/crc.h>
```

更新符合 IEEE 的 `CRC32` 校验和。


**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `crc（原页显示 CRC）` | 要更新的 `CRC32` 校验和。 |
| `data` | 要计算 CRC 的数据指针。 |
| `len` | 数据长度。 |

**返回（Returns）**：返回 `CRC32` 值。

## 3.26\_crc32\_k\_4\_2\_update()

<a id="gaba2e753d07e6b17b5330ee56aa48962d"></a>
<a id="r_gaba2e753d07e6b17b5330ee56aa48962d"></a>

```c
uint32_t crc32_k_4_2_update ( uint32_t crc, const uint8_t * data, size_t len )
```

```c
#include <zephyr/sys/crc.h>
```

更新 CRC-32K/4.2（*op，Koopman）校验和。

它在数据长度不超过 2,147,483,615 位时具有良好的 HD=4 校验能力，在不超过 6,167 位时达到 HD=5/6。

汉明距离（Hamming Distance，HD）及相关属性：

参考：[Koopman的CRC32资料](https://users.ece.cmu.edu/~koopman/crc/crc32.html)。

- 多项式：0x93a409eb。
- 输入反射（Reflect-in）：false。
- 初始值（Xor-in）：由调用者通过 crc 参数提供，可以使用 0xFFFFFFFF。
- 输出反射（Reflect-out）：false。
- 输出异或（Xor-out）：0。
- HD=4，数据长度 2,147,483,615 位。
- HD=5，数据长度 6,167 位。
- HD=6，数据长度 6,167 位。
- HD=7，数据长度 148 位。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `crc（原页显示 CRC）` | 要更新的 `CRC32` 校验和。 |
| `data` | 要计算 CRC 的数据指针。 |
| `len` | 数据长度。 |

**返回（Returns）**：返回 `CRC32` 值。

## 3.27\_crc32\_mpeg2()

<a id="gaee8a8a5c17b530efe9b331c5af97e2c8"></a>
<a id="r_gaee8a8a5c17b530efe9b331c5af97e2c8"></a>

```c
uint32_t crc32_mpeg2 ( const uint8_t * data, size_t len )
```

```c
#include <zephyr/sys/crc.h>
```

生成 CRC-32/MPEG-2 校验和。

使用多项式 0x04C11DB7 和初始值 0xFFFFFFFF，不反射输入或输出，也不作最终异或，即 CRC-32/MPEG-2。等价于以 `crc` 为 0xFFFFFFFF 调用 [`crc32_mpeg2_update`](#ga8f5d481856e8d473772a6a417adedda7)。


**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `data` | 要计算 CRC 的数据指针。 |
| `len` | 数据长度。 |

**返回（Returns）**：返回 CRC-32 值。

## 3.28\_crc32\_mpeg2\_update()

<a id="ga8f5d481856e8d473772a6a417adedda7"></a>
<a id="r_ga8f5d481856e8d473772a6a417adedda7"></a>

```c
uint32_t crc32_mpeg2_update ( uint32_t crc, const uint8_t * data, size_t len )
```

```c
#include <zephyr/sys/crc.h>
```

更新 CRC-32/MPEG-2 校验和。

使用多项式 0x04C11DB7，以最高有效位优先形式计算 CRC-32，不反射输入或输出，也不作最终异或。首次调用将 `crc` 设为 0xFFFFFFFF，即可得到标准 CRC-32/MPEG-2 值。


**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `crc（原页显示 CRC）` | 要更新的 CRC-32 校验和；首次调用使用 0xFFFFFFFF，以匹配 CRC-32/MPEG-2。 |
| `data` | 要计算 CRC 的数据指针。 |
| `len` | 数据长度。 |

**返回（Returns）**：返回 CRC-32 值。

## 3.29\_crc4()

<a id="ga4458d7743f9a3394fb68cddcc100e456"></a>
<a id="r_ga4458d7743f9a3394fb68cddcc100e456"></a>

```c
uint8_t crc4 ( const uint8_t * src, size_t len, uint8_t polynomial, uint8_t initial_value, bool reversed )
```

```c
#include <zephyr/sys/crc.h>
```

计算 CRC-4 的通用函数。

传入输入地址、输入长度、多项式和初始值以计算 CRC-4。输入缓冲区须按完整字节对齐；保证结果的最高4位为零。


**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `src` | 计算所用的输入字节。 |
| `len` | 输入长度，单位为字节。 |
| `polynomial` | 使用的多项式，省略最高次项 x^4 的系数。 |
| `initial_value` | CRC 计算的初始值（Initial Value）。 |
| `reversed` | 是否使用位反射／反转形式（Reflected / Reversed）。 |

**返回（Returns）**：返回计算得到的 [`CRC4`](#ggabc40e4ffd6da1175eb8ee8573a527eddaef5caa552f890f4c7e887dfe1a06bc22) 值。

> 译注：此处的完整字节要求属于输入数据粒度；原文没有提出额外的4字节或8字节地址对齐要求。

## 3.30\_crc4\_ti()

<a id="ga322365098ec65bde3d55b0c059896668"></a>
<a id="r_ga322365098ec65bde3d55b0c059896668"></a>

```c
uint8_t crc4_ti ( uint8_t seed, const uint8_t * src, size_t len )
```

```c
#include <zephyr/sys/crc.h>
```

计算缓冲区的 CRC-4 校验和。

供 TMAG5170 传感器使用。多项式为 0x03，不作位反射。CRC 结果的最高4位为零。


**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `seed` | CRC 的种子值。 |
| `src` | 计算所用的输入字节。 |
| `len` | 输入长度，单位为字节。 |

**返回（Returns）**：返回计算得到的 [`CRC4`](#ggabc40e4ffd6da1175eb8ee8573a527eddaef5caa552f890f4c7e887dfe1a06bc22) 值。

## 3.31\_crc7\_be()

<a id="ga1169005fd900b2787035044eeea38af1"></a>
<a id="r_ga1169005fd900b2787035044eeea38af1"></a>

```c
uint8_t crc7_be ( uint8_t seed, const uint8_t * src, size_t len )
```

```c
#include <zephyr/sys/crc.h>
```

计算缓冲区的 CRC-7 校验和。

参见 JESD84-A441。此算法用于多媒体卡（MultiMediaCard，MMC）协议，使用多项式 0x09，不作位反射。CRC 左对齐，因此结果的 bit 7 对应 CRC 的 bit 6。


**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `seed` | CRC 的种子值。 |
| `src` | 计算所用的输入字节。 |
| `len` | 输入长度，单位为字节。 |

**返回（Returns）**：返回计算得到的 `CRC7` 值。

## 3.32\_crc8()

<a id="gaa614e73ee7484ca0424fa7d14a54bbb6"></a>
<a id="r_gaa614e73ee7484ca0424fa7d14a54bbb6"></a>

```c
uint8_t crc8 ( const uint8_t * src, size_t len, uint8_t polynomial, uint8_t initial_value, bool reversed )
```

```c
#include <zephyr/sys/crc.h>
```

计算 CRC-8 的通用函数。

传入输入地址、输入长度、多项式和初始值以计算 CRC-8。


**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `src` | 计算所用的输入字节。 |
| `len` | 输入长度，单位为字节。 |
| `polynomial` | 使用的多项式，省略最高次项 x^8 的系数。 |
| `initial_value` | CRC 计算的初始值（Initial Value）。 |
| `reversed` | 是否使用位反射／反转形式（Reflected / Reversed）。 |

**返回（Returns）**：返回计算得到的 [`CRC8`](#ggabc40e4ffd6da1175eb8ee8573a527edda852cb403a2665ed279b28679f11567d8) 值。

## 3.33\_crc8\_ccitt()

<a id="ga9a925de71cd0255a22c769dc4b130da5"></a>
<a id="r_ga9a925de71cd0255a22c769dc4b130da5"></a>

```c
uint8_t crc8_ccitt ( uint8_t initial_value, const void * buf, size_t len )
```

```c
#include <zephyr/sys/crc.h>
```

计算 CRC-8 的 CCITT 变体。

常规 CRC-8 CCITT 变体使用多项式 0x07。


**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `initial_value` | CRC 计算的初始值（Initial Value）。 |
| `buf` | 计算所用的输入字节。 |
| `len` | 输入长度，单位为字节。 |

**返回（Returns）**：返回计算得到的 [`CRC8`](#ggabc40e4ffd6da1175eb8ee8573a527edda852cb403a2665ed279b28679f11567d8) 值。

## 3.34\_crc8\_rohc()

<a id="ga7a8f4387a2d0163165557446d018f041"></a>
<a id="r_ga7a8f4387a2d0163165557446d018f041"></a>

```c
uint8_t crc8_rohc ( uint8_t initial_value, const void * buf, size_t len )
```

```c
#include <zephyr/sys/crc.h>
```

计算 CRC-8 的 ROHC 变体。

CRC-8 的鲁棒报头压缩（Robust Header Compression，ROHC）变体，使用多项式 0x07，并作位反射。


**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `initial_value` | CRC 计算的初始值（Initial Value）。 |
| `buf` | 计算所用的输入字节。 |
| `len` | 输入长度，单位为字节。 |

**返回（Returns）**：返回计算得到的 [`CRC8`](#ggabc40e4ffd6da1175eb8ee8573a527edda852cb403a2665ed279b28679f11567d8) 值。

## 3.35\_crc\_by\_type()

<a id="ga5d7f493210e56fb18b8199c9d8a17f33"></a>
<a id="r_ga5d7f493210e56fb18b8199c9d8a17f33"></a>

```c
static inline uint32_t crc_by_type ( enum crc_type type, const uint8_t * src, size_t len, uint32_t seed, uint32_t poly, bool reflect, bool first, bool last )
```

```c
#include <zephyr/sys/crc.h>
```

以通用方式计算 CRC 校验和。

这是一个分派函数，按 `type` 调用具体 CRC 例程。

对于7、8、16和24位 CRC，`seed` 与 `poly` 的有效值应通过最低有效字节（Least-significant Bytes）传入。

同样，对于7、8、16和24位 CRC，有效结果保存在返回值的最低有效字节中。


**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `type` | 要使用的 CRC 算法。 |
| `src` | 计算所用的输入字节。 |
| `len` | 输入长度，单位为字节。 |
| `seed` | 种子，或待更新的既有 CRC 值。 |
| `poly` | 使用的多项式，省略最高次项系数。 |
| `reflect` | 是否使用位反射／反转形式（Reflected / Reversed）。 |
| `first` | 是否为数据流中的第一个分组（Packet）。 |
| `last` | 是否为数据流中的最后一个分组。 |

**返回（Returns）**：以 `uint32_t` 返回计算得到的 CRC 值。

> 译注：此接口按 `type` 分派，不能假定每个分支都会使用所有通用参数。可查看同批源码浏览页中的 switch；例如 [`CRC16_ANSI`](#ggabc40e4ffd6da1175eb8ee8573a527edda4a5e69eba1f74c0bd028356c9fb0f1f6) 直接调用其固定初始值封装。

## 3.36\_源码对照与相关阅读

译注：本仓库的[系统CRC头文件](../../../include/zephyr/sys/crc.h)和[CRC实现目录](../../../subsys/crc)可作源码跟踪。硬件驱动另见[CRC驱动接口](../hardware/P038_CRC驱动接口参考.md)。

[CRC概览](P001_CRC子系统概览.md) · [CRC计算接口](P003_CRC计算接口.md) · [系统头文件](P004_CRC系统头文件.md)。

本地引用从本文按相对路径解析，不绑定盘符或用户名；仓库版本不自动等同于官方 latest。本轮未执行 CRC 程序、随机性测试或熵源验证。

<a id="header-enum-members"></a>
<a id="enum-members"></a>
<a id="header-func-members"></a>
<a id="func-members"></a>
<a id="CRC_POLYNOMIAL"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggabc40e4ffd6da1175eb8ee8573a527eddaef5caa552f890f4c7e887dfe1a06bc22"></a>
<a id="ggabc40e4ffd6da1175eb8ee8573a527edda3a8effe9651199c20669daf033bbe59f"></a>
<a id="ggabc40e4ffd6da1175eb8ee8573a527edda218e7d92cae035c594e267fb0ed0ae6a"></a>
<a id="ggabc40e4ffd6da1175eb8ee8573a527edda852cb403a2665ed279b28679f11567d8"></a>
<a id="ggabc40e4ffd6da1175eb8ee8573a527eddae00c2275c0a5ac47b64c221feadfc3eb"></a>
<a id="ggabc40e4ffd6da1175eb8ee8573a527eddad0cba27d3a1347c21fc34cfd3aa0eab5"></a>
<a id="ggabc40e4ffd6da1175eb8ee8573a527edda27369d6d16d5fdf2a44111924c019e11"></a>
<a id="ggabc40e4ffd6da1175eb8ee8573a527edda4a5e69eba1f74c0bd028356c9fb0f1f6"></a>
<a id="ggabc40e4ffd6da1175eb8ee8573a527eddacdf0c4de024efc53edd374ad22c6da30"></a>
<a id="ggabc40e4ffd6da1175eb8ee8573a527edda3fdbd9451fc39959f46714a2f46ca42c"></a>
<a id="ggabc40e4ffd6da1175eb8ee8573a527eddac7805fb845479f192a855292bdb03f43"></a>
<a id="ggabc40e4ffd6da1175eb8ee8573a527edda4036b6c556c8aa1307c1ff7ff1626148"></a>
<a id="ggabc40e4ffd6da1175eb8ee8573a527eddaecf71323e57da8d4f7e45d154b1059d8"></a>
<a id="ggabc40e4ffd6da1175eb8ee8573a527edda5d04a93660d113893b7cc27ba48ba25b"></a>
<a id="ggabc40e4ffd6da1175eb8ee8573a527eddae06f6bdc6b6e1e4c16b21c358e807ca6"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

[上一章](P002_CRC子系统示例.md) · [返回大纲](大纲.md) · [下一章](P004_CRC系统头文件.md)
