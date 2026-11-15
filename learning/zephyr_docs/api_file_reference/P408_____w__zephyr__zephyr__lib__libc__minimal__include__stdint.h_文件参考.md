---
id: learning.zephyr-docs.api-file-reference.page-408
title: ____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第408章\_\_\_\_\_w\_\_zephyr\_\_zephyr\_\_lib\_\_libc\_\_minimal\_\_include\_\_stdint.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 408.1\_宏定义（Macros）

<a id="r_aaf7f29f45f1a513b4748a4e5014ddf6a"></a>

```c
#define INT8_MAX __INT8_MAX__
```

相关声明：[INT8_MAX](#aaf7f29f45f1a513b4748a4e5014ddf6a)。

<a id="r_ac58f2c111cc9989c86db2a7dc4fd84ca"></a>

```c
#define INT16_MAX __INT16_MAX__
```

相关声明：[INT16_MAX](#ac58f2c111cc9989c86db2a7dc4fd84ca)。

<a id="r_a181807730d4a375f848ba139813ce04f"></a>

```c
#define INT32_MAX __INT32_MAX__
```

相关声明：[INT32_MAX](#a181807730d4a375f848ba139813ce04f)。

<a id="r_ad0d744f05898e32d01f73f8af3cd2071"></a>

```c
#define INT64_MAX __INT64_MAX__
```

相关声明：[INT64_MAX](#ad0d744f05898e32d01f73f8af3cd2071)。

<a id="r_a022b9b0a3564d786244a4631847c37a3"></a>

```c
#define INTMAX_MAX __INT64_MAX__
```

相关声明：[INTMAX_MAX](#a022b9b0a3564d786244a4631847c37a3)。

<a id="r_aadcf2a81af243df333b31efa6461ab8e"></a>

```c
#define INT8_MIN (-INT8_MAX - 1)
```

相关声明：[INT8_MIN](#aadcf2a81af243df333b31efa6461ab8e)、[INT8_MAX](#aaf7f29f45f1a513b4748a4e5014ddf6a)。

<a id="r_ad4e9955955b27624963643eac448118a"></a>

```c
#define INT16_MIN (-INT16_MAX - 1)
```

相关声明：[INT16_MIN](#ad4e9955955b27624963643eac448118a)、[INT16_MAX](#ac58f2c111cc9989c86db2a7dc4fd84ca)。

<a id="r_a688eb21a22db27c2b2bd5836943cdcbe"></a>

```c
#define INT32_MIN (-INT32_MAX - 1)
```

相关声明：[INT32_MIN](#a688eb21a22db27c2b2bd5836943cdcbe)、[INT32_MAX](#a181807730d4a375f848ba139813ce04f)。

<a id="r_ab21f12f372f67b8ff0aa3432336ede67"></a>

```c
#define INT64_MIN (-INT64_MAX - 1LL)
```

相关声明：[INT64_MIN](#ab21f12f372f67b8ff0aa3432336ede67)、[INT64_MAX](#ad0d744f05898e32d01f73f8af3cd2071)。

<a id="r_aeb4e270a084ee26fe73e799861bd0252"></a>

```c
#define UINT8_MAX __UINT8_MAX__
```

相关声明：[UINT8_MAX](#aeb4e270a084ee26fe73e799861bd0252)。

<a id="r_a3ea490c9b3617d4479bd80ef93cd5602"></a>

```c
#define UINT16_MAX __UINT16_MAX__
```

相关声明：[UINT16_MAX](#a3ea490c9b3617d4479bd80ef93cd5602)。

<a id="r_ab5eb23180f7cc12b7d6c04a8ec067fdd"></a>

```c
#define UINT32_MAX __UINT32_MAX__
```

相关声明：[UINT32_MAX](#ab5eb23180f7cc12b7d6c04a8ec067fdd)。

<a id="r_a30654b4b67d97c42ca3f9b6052dda916"></a>

```c
#define UINT64_MAX __UINT64_MAX__
```

相关声明：[UINT64_MAX](#a30654b4b67d97c42ca3f9b6052dda916)。

<a id="r_aa54fd5210434219e9027bfa0f0e325c8"></a>

```c
#define UINTMAX_MAX __UINT64_MAX__
```

相关声明：[UINTMAX_MAX](#aa54fd5210434219e9027bfa0f0e325c8)。

<a id="r_acbcdb3bee0f5f904da5df8de69a80ca3"></a>

```c
#define INT_FAST8_MAX __INT_FAST8_MAX__
```

相关声明：[INT_FAST8_MAX](#acbcdb3bee0f5f904da5df8de69a80ca3)。

<a id="r_a2fd35d0ea091e04caec504ff0042cf00"></a>

```c
#define INT_FAST16_MAX __INT_FAST16_MAX__
```

相关声明：[INT_FAST16_MAX](#a2fd35d0ea091e04caec504ff0042cf00)。

<a id="r_ac96fa0f41b19e89f109e4f9913ca6635"></a>

```c
#define INT_FAST32_MAX __INT_FAST32_MAX__
```

相关声明：[INT_FAST32_MAX](#ac96fa0f41b19e89f109e4f9913ca6635)。

<a id="r_a13c95cf9c209d8daacb36cbf0d5ba275"></a>

```c
#define INT_FAST64_MAX __INT_FAST64_MAX__
```

相关声明：[INT_FAST64_MAX](#a13c95cf9c209d8daacb36cbf0d5ba275)。

<a id="r_aad8fb982cb19143efd5ee9a1a7a89390"></a>

```c
#define INT_FAST8_MIN (-INT_FAST8_MAX - 1)
```

相关声明：[INT_FAST8_MIN](#aad8fb982cb19143efd5ee9a1a7a89390)、[INT_FAST8_MAX](#acbcdb3bee0f5f904da5df8de69a80ca3)。

<a id="r_a169460a4e2a79138723d68d99372d958"></a>

```c
#define INT_FAST16_MIN (-INT_FAST16_MAX - 1)
```

相关声明：[INT_FAST16_MIN](#a169460a4e2a79138723d68d99372d958)、[INT_FAST16_MAX](#a2fd35d0ea091e04caec504ff0042cf00)。

<a id="r_ad93df1652ed0635513d5efe4f1219926"></a>

```c
#define INT_FAST32_MIN (-INT_FAST32_MAX - 1)
```

相关声明：[INT_FAST32_MIN](#ad93df1652ed0635513d5efe4f1219926)、[INT_FAST32_MAX](#ac96fa0f41b19e89f109e4f9913ca6635)。

<a id="r_a50f0fdcb00ea2500cec0f3d6d45c36f3"></a>

```c
#define INT_FAST64_MIN (-INT_FAST64_MAX - 1LL)
```

相关声明：[INT_FAST64_MIN](#a50f0fdcb00ea2500cec0f3d6d45c36f3)、[INT_FAST64_MAX](#a13c95cf9c209d8daacb36cbf0d5ba275)。

<a id="r_a2c6f97ea2d76d0cf6260c84046cdb44e"></a>

```c
#define UINT_FAST8_MAX __UINT_FAST8_MAX__
```

相关声明：[UINT_FAST8_MAX](#a2c6f97ea2d76d0cf6260c84046cdb44e)。

<a id="r_aed28ca63d9b222f6f1377358fe73a183"></a>

```c
#define UINT_FAST16_MAX __UINT_FAST16_MAX__
```

相关声明：[UINT_FAST16_MAX](#aed28ca63d9b222f6f1377358fe73a183)。

<a id="r_ad51246a178143208b2db3315efd21c45"></a>

```c
#define UINT_FAST32_MAX __UINT_FAST32_MAX__
```

相关声明：[UINT_FAST32_MAX](#ad51246a178143208b2db3315efd21c45)。

<a id="r_aeb74410af7781bc84b5f64ae7a8f4a17"></a>

```c
#define UINT_FAST64_MAX __UINT_FAST64_MAX__
```

相关声明：[UINT_FAST64_MAX](#aeb74410af7781bc84b5f64ae7a8f4a17)。

<a id="r_aa05109908fb2770f632d2b646b9f85bf"></a>

```c
#define INT_LEAST8_MAX __INT_LEAST8_MAX__
```

相关声明：[INT_LEAST8_MAX](#aa05109908fb2770f632d2b646b9f85bf)。

<a id="r_a7eb2a8e2a1c65d6c9ad0f86154890baa"></a>

```c
#define INT_LEAST16_MAX __INT_LEAST16_MAX__
```

相关声明：[INT_LEAST16_MAX](#a7eb2a8e2a1c65d6c9ad0f86154890baa)。

<a id="r_a5618711a0a54f722190a3a1219e278c2"></a>

```c
#define INT_LEAST32_MAX __INT_LEAST32_MAX__
```

相关声明：[INT_LEAST32_MAX](#a5618711a0a54f722190a3a1219e278c2)。

<a id="r_a35d0f98a2e507fd1be779d49da92724e"></a>

```c
#define INT_LEAST64_MAX __INT_LEAST64_MAX__
```

相关声明：[INT_LEAST64_MAX](#a35d0f98a2e507fd1be779d49da92724e)。

<a id="r_a3e986cad833f63f420962ff60eda87e5"></a>

```c
#define INT_LEAST8_MIN (-INT_LEAST8_MAX - 1)
```

相关声明：[INT_LEAST8_MIN](#a3e986cad833f63f420962ff60eda87e5)、[INT_LEAST8_MAX](#aa05109908fb2770f632d2b646b9f85bf)。

<a id="r_a1f91bfd5820c2f27af3d260fc75813e1"></a>

```c
#define INT_LEAST16_MIN (-INT_LEAST16_MAX - 1)
```

相关声明：[INT_LEAST16_MIN](#a1f91bfd5820c2f27af3d260fc75813e1)、[INT_LEAST16_MAX](#a7eb2a8e2a1c65d6c9ad0f86154890baa)。

<a id="r_a2360a536116dd734820a6b5b3d560ce7"></a>

```c
#define INT_LEAST32_MIN (-INT_LEAST32_MAX - 1)
```

相关声明：[INT_LEAST32_MIN](#a2360a536116dd734820a6b5b3d560ce7)、[INT_LEAST32_MAX](#a5618711a0a54f722190a3a1219e278c2)。

<a id="r_ac12b4f6966b57ad82feb683b284b4060"></a>

```c
#define INT_LEAST64_MIN (-INT_LEAST64_MAX - 1LL)
```

相关声明：[INT_LEAST64_MIN](#ac12b4f6966b57ad82feb683b284b4060)、[INT_LEAST64_MAX](#a35d0f98a2e507fd1be779d49da92724e)。

<a id="r_a2a80bde77ee1698d0f42f334adad4f2b"></a>

```c
#define UINT_LEAST8_MAX __UINT_LEAST8_MAX__
```

相关声明：[UINT_LEAST8_MAX](#a2a80bde77ee1698d0f42f334adad4f2b)。

<a id="r_a6ef6a1a518bbf516ca8b0180b11c358f"></a>

```c
#define UINT_LEAST16_MAX __UINT_LEAST16_MAX__
```

相关声明：[UINT_LEAST16_MAX](#a6ef6a1a518bbf516ca8b0180b11c358f)。

<a id="r_a70cad8bacc9a6db301e1cdc86cc8d571"></a>

```c
#define UINT_LEAST32_MAX __UINT_LEAST32_MAX__
```

相关声明：[UINT_LEAST32_MAX](#a70cad8bacc9a6db301e1cdc86cc8d571)。

<a id="r_aab530113fa96e280e49c3c138b0f917d"></a>

```c
#define UINT_LEAST64_MAX __UINT_LEAST64_MAX__
```

相关声明：[UINT_LEAST64_MAX](#aab530113fa96e280e49c3c138b0f917d)。

<a id="r_a9e5742f2bae4a5283431a3c03499e3a9"></a>

```c
#define INTPTR_MAX __INTPTR_MAX__
```

相关声明：[INTPTR_MAX](#a9e5742f2bae4a5283431a3c03499e3a9)。

<a id="r_a2aaa6d3aa1d7d1e0e326955aa24db752"></a>

```c
#define INTPTR_MIN (-INTPTR_MAX - 1)
```

相关声明：[INTPTR_MIN](#a2aaa6d3aa1d7d1e0e326955aa24db752)、[INTPTR_MAX](#a9e5742f2bae4a5283431a3c03499e3a9)。

<a id="r_ab2355300ea19395357e62d780f4dd073"></a>

```c
#define UINTPTR_MAX __UINTPTR_MAX__
```

相关声明：[UINTPTR_MAX](#ab2355300ea19395357e62d780f4dd073)。

<a id="r_add2ef7bffac19cfdd1f4b5495409672f"></a>

```c
#define PTRDIFF_MAX __PTRDIFF_MAX__
```

相关声明：[PTRDIFF_MAX](#add2ef7bffac19cfdd1f4b5495409672f)。

<a id="r_ad9b88ba2fb858f98b50b38e49875d90e"></a>

```c
#define PTRDIFF_MIN (-PTRDIFF_MAX - 1)
```

相关声明：[PTRDIFF_MIN](#ad9b88ba2fb858f98b50b38e49875d90e)、[PTRDIFF_MAX](#add2ef7bffac19cfdd1f4b5495409672f)。

<a id="r_a3c75bb398badb69c7577b21486f9963f"></a>

```c
#define SIZE_MAX __SIZE_MAX__
```

相关声明：[SIZE_MAX](#a3c75bb398badb69c7577b21486f9963f)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 408.2\_类型定义（Typedefs）

<a id="r_accbd6432732c88ad6adc5365800433b6"></a>

```c
typedef __INT8_TYPE__ int8_t
```

相关声明：[int8_t](#accbd6432732c88ad6adc5365800433b6)。

<a id="r_afe270aee8d96ad7f279a4020b9d58bdf"></a>

```c
typedef __INT16_TYPE__ int16_t
```

相关声明：[int16_t](#afe270aee8d96ad7f279a4020b9d58bdf)。

<a id="r_a0c18914b3041c2f583aba76f418399c2"></a>

```c
typedef __INT32_TYPE__ int32_t
```

相关声明：[int32_t](#a0c18914b3041c2f583aba76f418399c2)。

<a id="r_ac714c0d2c1a4adb10e73cab29623314b"></a>

```c
typedef __INT64_TYPE__ int64_t
```

相关声明：[int64_t](#ac714c0d2c1a4adb10e73cab29623314b)。

<a id="r_a9d6c1dc12f73927ba41516de04a5fdb8"></a>

```c
typedef __INT64_TYPE__ intmax_t
```

相关声明：[intmax_t](#a9d6c1dc12f73927ba41516de04a5fdb8)。

<a id="r_a98f573ff8187ff09c9594a3f2af7be0d"></a>

```c
typedef __INT_FAST8_TYPE__ int_fast8_t
```

相关声明：[int_fast8_t](#a98f573ff8187ff09c9594a3f2af7be0d)。

<a id="r_a888269be199d49b7f40006aaafa5a350"></a>

```c
typedef __INT_FAST16_TYPE__ int_fast16_t
```

相关声明：[int_fast16_t](#a888269be199d49b7f40006aaafa5a350)。

<a id="r_a530ba8ffc89f6393d2d0e2fb2db38b54"></a>

```c
typedef __INT_FAST32_TYPE__ int_fast32_t
```

相关声明：[int_fast32_t](#a530ba8ffc89f6393d2d0e2fb2db38b54)。

<a id="r_abcdb0a9f6e7d139ad4f521ab8f4efdc0"></a>

```c
typedef __INT_FAST64_TYPE__ int_fast64_t
```

相关声明：[int_fast64_t](#abcdb0a9f6e7d139ad4f521ab8f4efdc0)。

<a id="r_adb5f4bf8afa3bee9e4da1bb9daf4908d"></a>

```c
typedef __INT_LEAST8_TYPE__ int_least8_t
```

相关声明：[int_least8_t](#adb5f4bf8afa3bee9e4da1bb9daf4908d)。

<a id="r_a3a4bc1e426626e17f6a6e0f64decec56"></a>

```c
typedef __INT_LEAST16_TYPE__ int_least16_t
```

相关声明：[int_least16_t](#a3a4bc1e426626e17f6a6e0f64decec56)。

<a id="r_a4462f62ae74ff8172526401354d2fc9b"></a>

```c
typedef __INT_LEAST32_TYPE__ int_least32_t
```

相关声明：[int_least32_t](#a4462f62ae74ff8172526401354d2fc9b)。

<a id="r_a8a5003442318117c64d16d6f32f64f37"></a>

```c
typedef __INT_LEAST64_TYPE__ int_least64_t
```

相关声明：[int_least64_t](#a8a5003442318117c64d16d6f32f64f37)。

<a id="r_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>

```c
typedef __UINT8_TYPE__ uint8_t
```

相关声明：[uint8_t](#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_a5debae8b2a1ec20a6694c0c443ee399e"></a>

```c
typedef __UINT16_TYPE__ uint16_t
```

相关声明：[uint16_t](#a5debae8b2a1ec20a6694c0c443ee399e)。

<a id="r_a0a8582351ac627ee8bde2973c825e47f"></a>

```c
typedef __UINT32_TYPE__ uint32_t
```

相关声明：[uint32_t](#a0a8582351ac627ee8bde2973c825e47f)。

<a id="r_a2095b9bffea4b2656950c6c0419edbf1"></a>

```c
typedef __UINT64_TYPE__ uint64_t
```

相关声明：[uint64_t](#a2095b9bffea4b2656950c6c0419edbf1)。

<a id="r_aac7deaa1633720ec64bd432bbc31af40"></a>

```c
typedef __UINT64_TYPE__ uintmax_t
```

相关声明：[uintmax_t](#aac7deaa1633720ec64bd432bbc31af40)。

<a id="r_a2464ed69ccd3fd2b3b4c93cb78f6fa20"></a>

```c
typedef __UINT_FAST8_TYPE__ uint_fast8_t
```

相关声明：[uint_fast8_t](#a2464ed69ccd3fd2b3b4c93cb78f6fa20)。

<a id="r_aaabed6e034edb01c259c003894d7f7c8"></a>

```c
typedef __UINT_FAST16_TYPE__ uint_fast16_t
```

相关声明：[uint_fast16_t](#aaabed6e034edb01c259c003894d7f7c8)。

<a id="r_aa44ff507c3d9a49e27fac64e9fadf062"></a>

```c
typedef __UINT_FAST32_TYPE__ uint_fast32_t
```

相关声明：[uint_fast32_t](#aa44ff507c3d9a49e27fac64e9fadf062)。

<a id="r_a62c711f66c6d29c81429aeafdc4bc592"></a>

```c
typedef __UINT_FAST64_TYPE__ uint_fast64_t
```

相关声明：[uint_fast64_t](#a62c711f66c6d29c81429aeafdc4bc592)。

<a id="r_a61d44370ed65907c324edad5e8d34632"></a>

```c
typedef __UINT_LEAST8_TYPE__ uint_least8_t
```

相关声明：[uint_least8_t](#a61d44370ed65907c324edad5e8d34632)。

<a id="r_a1a01d6a4e68e435471be2ae8db7e8fdc"></a>

```c
typedef __UINT_LEAST16_TYPE__ uint_least16_t
```

相关声明：[uint_least16_t](#a1a01d6a4e68e435471be2ae8db7e8fdc)。

<a id="r_a678494ae5435d8904e7972c94618e774"></a>

```c
typedef __UINT_LEAST32_TYPE__ uint_least32_t
```

相关声明：[uint_least32_t](#a678494ae5435d8904e7972c94618e774)。

<a id="r_aba0cb5638c172422eb4a7555a143fbbc"></a>

```c
typedef __UINT_LEAST64_TYPE__ uint_least64_t
```

相关声明：[uint_least64_t](#aba0cb5638c172422eb4a7555a143fbbc)。

<a id="r_a0bd5dec00e345e69027427f8621d6a6c"></a>

```c
typedef __INTPTR_TYPE__ intptr_t
```

相关声明：[intptr_t](#a0bd5dec00e345e69027427f8621d6a6c)。

<a id="r_a4788399d1d0b37ccf098a7da82254808"></a>

```c
typedef __UINTPTR_TYPE__ uintptr_t
```

相关声明：[uintptr_t](#a4788399d1d0b37ccf098a7da82254808)。

## 408.3\_详细说明（Detailed Documentation）

<a id="ac58f2c111cc9989c86db2a7dc4fd84ca"></a>

### `INT16_MAX`

```c
#define INT16_MAX __INT16_MAX__
```

<a id="ad4e9955955b27624963643eac448118a"></a>

### `INT16_MIN`

```c
#define INT16_MIN (-INT16_MAX - 1)
```

<a id="a181807730d4a375f848ba139813ce04f"></a>

### `INT32_MAX`

```c
#define INT32_MAX __INT32_MAX__
```

<a id="a688eb21a22db27c2b2bd5836943cdcbe"></a>

### `INT32_MIN`

```c
#define INT32_MIN (-INT32_MAX - 1)
```

<a id="ad0d744f05898e32d01f73f8af3cd2071"></a>

### `INT64_MAX`

```c
#define INT64_MAX __INT64_MAX__
```

<a id="ab21f12f372f67b8ff0aa3432336ede67"></a>

### `INT64_MIN`

```c
#define INT64_MIN (-INT64_MAX - 1LL)
```

<a id="aaf7f29f45f1a513b4748a4e5014ddf6a"></a>

### `INT8_MAX`

```c
#define INT8_MAX __INT8_MAX__
```

<a id="aadcf2a81af243df333b31efa6461ab8e"></a>

### `INT8_MIN`

```c
#define INT8_MIN (-INT8_MAX - 1)
```

<a id="a2fd35d0ea091e04caec504ff0042cf00"></a>

### `INT_FAST16_MAX`

```c
#define INT_FAST16_MAX __INT_FAST16_MAX__
```

<a id="a169460a4e2a79138723d68d99372d958"></a>

### `INT_FAST16_MIN`

```c
#define INT_FAST16_MIN (-INT_FAST16_MAX - 1)
```

<a id="ac96fa0f41b19e89f109e4f9913ca6635"></a>

### `INT_FAST32_MAX`

```c
#define INT_FAST32_MAX __INT_FAST32_MAX__
```

<a id="ad93df1652ed0635513d5efe4f1219926"></a>

### `INT_FAST32_MIN`

```c
#define INT_FAST32_MIN (-INT_FAST32_MAX - 1)
```

<a id="a13c95cf9c209d8daacb36cbf0d5ba275"></a>

### `INT_FAST64_MAX`

```c
#define INT_FAST64_MAX __INT_FAST64_MAX__
```

<a id="a50f0fdcb00ea2500cec0f3d6d45c36f3"></a>

### `INT_FAST64_MIN`

```c
#define INT_FAST64_MIN (-INT_FAST64_MAX - 1LL)
```

<a id="acbcdb3bee0f5f904da5df8de69a80ca3"></a>

### `INT_FAST8_MAX`

```c
#define INT_FAST8_MAX __INT_FAST8_MAX__
```

<a id="aad8fb982cb19143efd5ee9a1a7a89390"></a>

### `INT_FAST8_MIN`

```c
#define INT_FAST8_MIN (-INT_FAST8_MAX - 1)
```

<a id="a7eb2a8e2a1c65d6c9ad0f86154890baa"></a>

### `INT_LEAST16_MAX`

```c
#define INT_LEAST16_MAX __INT_LEAST16_MAX__
```

<a id="a1f91bfd5820c2f27af3d260fc75813e1"></a>

### `INT_LEAST16_MIN`

```c
#define INT_LEAST16_MIN (-INT_LEAST16_MAX - 1)
```

<a id="a5618711a0a54f722190a3a1219e278c2"></a>

### `INT_LEAST32_MAX`

```c
#define INT_LEAST32_MAX __INT_LEAST32_MAX__
```

<a id="a2360a536116dd734820a6b5b3d560ce7"></a>

### `INT_LEAST32_MIN`

```c
#define INT_LEAST32_MIN (-INT_LEAST32_MAX - 1)
```

<a id="a35d0f98a2e507fd1be779d49da92724e"></a>

### `INT_LEAST64_MAX`

```c
#define INT_LEAST64_MAX __INT_LEAST64_MAX__
```

<a id="ac12b4f6966b57ad82feb683b284b4060"></a>

### `INT_LEAST64_MIN`

```c
#define INT_LEAST64_MIN (-INT_LEAST64_MAX - 1LL)
```

<a id="aa05109908fb2770f632d2b646b9f85bf"></a>

### `INT_LEAST8_MAX`

```c
#define INT_LEAST8_MAX __INT_LEAST8_MAX__
```

<a id="a3e986cad833f63f420962ff60eda87e5"></a>

### `INT_LEAST8_MIN`

```c
#define INT_LEAST8_MIN (-INT_LEAST8_MAX - 1)
```

<a id="a022b9b0a3564d786244a4631847c37a3"></a>

### `INTMAX_MAX`

```c
#define INTMAX_MAX __INT64_MAX__
```

<a id="a9e5742f2bae4a5283431a3c03499e3a9"></a>

### `INTPTR_MAX`

```c
#define INTPTR_MAX __INTPTR_MAX__
```

<a id="a2aaa6d3aa1d7d1e0e326955aa24db752"></a>

### `INTPTR_MIN`

```c
#define INTPTR_MIN (-INTPTR_MAX - 1)
```

<a id="add2ef7bffac19cfdd1f4b5495409672f"></a>

### `PTRDIFF_MAX`

```c
#define PTRDIFF_MAX __PTRDIFF_MAX__
```

<a id="ad9b88ba2fb858f98b50b38e49875d90e"></a>

### `PTRDIFF_MIN`

```c
#define PTRDIFF_MIN (-PTRDIFF_MAX - 1)
```

<a id="a3c75bb398badb69c7577b21486f9963f"></a>

### `SIZE_MAX`

```c
#define SIZE_MAX __SIZE_MAX__
```

<a id="a3ea490c9b3617d4479bd80ef93cd5602"></a>

### `UINT16_MAX`

```c
#define UINT16_MAX __UINT16_MAX__
```

<a id="ab5eb23180f7cc12b7d6c04a8ec067fdd"></a>

### `UINT32_MAX`

```c
#define UINT32_MAX __UINT32_MAX__
```

<a id="a30654b4b67d97c42ca3f9b6052dda916"></a>

### `UINT64_MAX`

```c
#define UINT64_MAX __UINT64_MAX__
```

<a id="aeb4e270a084ee26fe73e799861bd0252"></a>

### `UINT8_MAX`

```c
#define UINT8_MAX __UINT8_MAX__
```

<a id="aed28ca63d9b222f6f1377358fe73a183"></a>

### `UINT_FAST16_MAX`

```c
#define UINT_FAST16_MAX __UINT_FAST16_MAX__
```

<a id="ad51246a178143208b2db3315efd21c45"></a>

### `UINT_FAST32_MAX`

```c
#define UINT_FAST32_MAX __UINT_FAST32_MAX__
```

<a id="aeb74410af7781bc84b5f64ae7a8f4a17"></a>

### `UINT_FAST64_MAX`

```c
#define UINT_FAST64_MAX __UINT_FAST64_MAX__
```

<a id="a2c6f97ea2d76d0cf6260c84046cdb44e"></a>

### `UINT_FAST8_MAX`

```c
#define UINT_FAST8_MAX __UINT_FAST8_MAX__
```

<a id="a6ef6a1a518bbf516ca8b0180b11c358f"></a>

### `UINT_LEAST16_MAX`

```c
#define UINT_LEAST16_MAX __UINT_LEAST16_MAX__
```

<a id="a70cad8bacc9a6db301e1cdc86cc8d571"></a>

### `UINT_LEAST32_MAX`

```c
#define UINT_LEAST32_MAX __UINT_LEAST32_MAX__
```

<a id="aab530113fa96e280e49c3c138b0f917d"></a>

### `UINT_LEAST64_MAX`

```c
#define UINT_LEAST64_MAX __UINT_LEAST64_MAX__
```

<a id="a2a80bde77ee1698d0f42f334adad4f2b"></a>

### `UINT_LEAST8_MAX`

```c
#define UINT_LEAST8_MAX __UINT_LEAST8_MAX__
```

<a id="aa54fd5210434219e9027bfa0f0e325c8"></a>

### `UINTMAX_MAX`

```c
#define UINTMAX_MAX __UINT64_MAX__
```

<a id="ab2355300ea19395357e62d780f4dd073"></a>

### `UINTPTR_MAX`

```c
#define UINTPTR_MAX __UINTPTR_MAX__
```

<a id="afe270aee8d96ad7f279a4020b9d58bdf"></a>

### `int16_t`

```c
typedef __INT16_TYPE__ int16_t
```

<a id="a0c18914b3041c2f583aba76f418399c2"></a>

### `int32_t`

```c
typedef __INT32_TYPE__ int32_t
```

<a id="ac714c0d2c1a4adb10e73cab29623314b"></a>

### `int64_t`

```c
typedef __INT64_TYPE__ int64_t
```

<a id="accbd6432732c88ad6adc5365800433b6"></a>

### `int8_t`

```c
typedef __INT8_TYPE__ int8_t
```

<a id="a888269be199d49b7f40006aaafa5a350"></a>

### `int_fast16_t`

```c
typedef __INT_FAST16_TYPE__ int_fast16_t
```

<a id="a530ba8ffc89f6393d2d0e2fb2db38b54"></a>

### `int_fast32_t`

```c
typedef __INT_FAST32_TYPE__ int_fast32_t
```

<a id="abcdb0a9f6e7d139ad4f521ab8f4efdc0"></a>

### `int_fast64_t`

```c
typedef __INT_FAST64_TYPE__ int_fast64_t
```

<a id="a98f573ff8187ff09c9594a3f2af7be0d"></a>

### `int_fast8_t`

```c
typedef __INT_FAST8_TYPE__ int_fast8_t
```

<a id="a3a4bc1e426626e17f6a6e0f64decec56"></a>

### `int_least16_t`

```c
typedef __INT_LEAST16_TYPE__ int_least16_t
```

<a id="a4462f62ae74ff8172526401354d2fc9b"></a>

### `int_least32_t`

```c
typedef __INT_LEAST32_TYPE__ int_least32_t
```

<a id="a8a5003442318117c64d16d6f32f64f37"></a>

### `int_least64_t`

```c
typedef __INT_LEAST64_TYPE__ int_least64_t
```

<a id="adb5f4bf8afa3bee9e4da1bb9daf4908d"></a>

### `int_least8_t`

```c
typedef __INT_LEAST8_TYPE__ int_least8_t
```

<a id="a9d6c1dc12f73927ba41516de04a5fdb8"></a>

### `intmax_t`

```c
typedef __INT64_TYPE__ intmax_t
```

<a id="a0bd5dec00e345e69027427f8621d6a6c"></a>

### `intptr_t`

```c
typedef __INTPTR_TYPE__ intptr_t
```

<a id="a5debae8b2a1ec20a6694c0c443ee399e"></a>

### `uint16_t`

```c
typedef __UINT16_TYPE__ uint16_t
```

<a id="a0a8582351ac627ee8bde2973c825e47f"></a>

### `uint32_t`

```c
typedef __UINT32_TYPE__ uint32_t
```

<a id="a2095b9bffea4b2656950c6c0419edbf1"></a>

### `uint64_t`

```c
typedef __UINT64_TYPE__ uint64_t
```

<a id="a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>

### `uint8_t`

```c
typedef __UINT8_TYPE__ uint8_t
```

<a id="aaabed6e034edb01c259c003894d7f7c8"></a>

### `uint_fast16_t`

```c
typedef __UINT_FAST16_TYPE__ uint_fast16_t
```

<a id="aa44ff507c3d9a49e27fac64e9fadf062"></a>

### `uint_fast32_t`

```c
typedef __UINT_FAST32_TYPE__ uint_fast32_t
```

<a id="a62c711f66c6d29c81429aeafdc4bc592"></a>

### `uint_fast64_t`

```c
typedef __UINT_FAST64_TYPE__ uint_fast64_t
```

<a id="a2464ed69ccd3fd2b3b4c93cb78f6fa20"></a>

### `uint_fast8_t`

```c
typedef __UINT_FAST8_TYPE__ uint_fast8_t
```

<a id="a1a01d6a4e68e435471be2ae8db7e8fdc"></a>

### `uint_least16_t`

```c
typedef __UINT_LEAST16_TYPE__ uint_least16_t
```

<a id="a678494ae5435d8904e7972c94618e774"></a>

### `uint_least32_t`

```c
typedef __UINT_LEAST32_TYPE__ uint_least32_t
```

<a id="aba0cb5638c172422eb4a7555a143fbbc"></a>

### `uint_least64_t`

```c
typedef __UINT_LEAST64_TYPE__ uint_least64_t
```

<a id="a61d44370ed65907c324edad5e8d34632"></a>

### `uint_least8_t`

```c
typedef __UINT_LEAST8_TYPE__ uint_least8_t
```

<a id="aac7deaa1633720ec64bd432bbc31af40"></a>

### `uintmax_t`

```c
typedef __UINT64_TYPE__ uintmax_t
```

<a id="a4788399d1d0b37ccf098a7da82254808"></a>

### `uintptr_t`

```c
typedef __UINTPTR_TYPE__ uintptr_t
```


## 408.4\_原页交叉引用（Cross References）

- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P409_____w__zephyr__zephyr__lib__libc__minimal__include__stdio.h_文件参考.md)
