---
id: learning.zephyr-docs.device-power-control-model-reference.page-13
title: gpio_cmsdk_ahb_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structgpio__cmsdk__ahb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_gpio\_cmsdk\_ahb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structgpio__cmsdk__ahb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/drivers/gpio/gpio_cmsdk_ahb.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 13.1\_数据成员（Data Fields）

<a id="r_accd586d346c6588ae93fc409159fa368"></a>

```c
volatile uint32_t data
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[data](#accd586d346c6588ae93fc409159fa368)。

<a id="r_af548def1b32a28d043b4bbfdddc29662"></a>

```c
volatile uint32_t dataout
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[dataout](#af548def1b32a28d043b4bbfdddc29662)。

<a id="r_a995563a125b425a4633f4d25ccaff0cd"></a>

```c
volatile uint32_t reserved0 [2]
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[reserved0](#a995563a125b425a4633f4d25ccaff0cd)。

<a id="r_ac5de9ecb2427bdf0dfc78099253ce2de"></a>

```c
volatile uint32_t outenableset
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[outenableset](#ac5de9ecb2427bdf0dfc78099253ce2de)。

<a id="r_a20babd83013581d8273570c5b63658b4"></a>

```c
volatile uint32_t outenableclr
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[outenableclr](#a20babd83013581d8273570c5b63658b4)。

<a id="r_a5f70dc42911502ff96254f44ff385caa"></a>

```c
volatile uint32_t altfuncset
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[altfuncset](#a5f70dc42911502ff96254f44ff385caa)。

<a id="r_a325a85d7d5fa3830ee9a7e922bed08ae"></a>

```c
volatile uint32_t altfuncclr
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[altfuncclr](#a325a85d7d5fa3830ee9a7e922bed08ae)。

<a id="r_a5c79dd58c92ee471c86cf420a02a3afb"></a>

```c
volatile uint32_t intenset
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[intenset](#a5c79dd58c92ee471c86cf420a02a3afb)。

<a id="r_a83a77418db66bd89bae093533a168617"></a>

```c
volatile uint32_t intenclr
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[intenclr](#a83a77418db66bd89bae093533a168617)。

<a id="r_abf5caf8e369d4629aabe935f63bd8f7e"></a>

```c
volatile uint32_t inttypeset
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[inttypeset](#abf5caf8e369d4629aabe935f63bd8f7e)。

<a id="r_af54ff4e5327fa86546166df38f76d3df"></a>

```c
volatile uint32_t inttypeclr
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[inttypeclr](#af54ff4e5327fa86546166df38f76d3df)。

<a id="r_af76e1a0e03e7a1373a4029f9865a1abb"></a>

```c
volatile uint32_t intpolset
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[intpolset](#af76e1a0e03e7a1373a4029f9865a1abb)。

<a id="r_addc9f323303ed2888a047a54ff2d2092"></a>

```c
volatile uint32_t intpolclr
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[intpolclr](#addc9f323303ed2888a047a54ff2d2092)。

```c
union {
```

<a id="r_afc0281c8b3b4714cb627005694c9da70"></a>

```c
volatile uint32_t intstatus
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[intstatus](#a5bc3851b26cb0340208f4b93ef475042)。

<a id="r_ac6107e00602da509cc30427223cd4cdf"></a>

```c
volatile uint32_t intclear
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[intclear](#aa3a3638d45f9dddd4f122b8081ac46cf)。

<a id="r_ab1490ee6715fafdce3c67a2c5990b236"></a>

```c
};
```

<a id="r_ae8c9c5c849a45f86b84b21266eaca8af"></a>

```c
volatile uint32_t reserved1 [241]
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[reserved1](#ae8c9c5c849a45f86b84b21266eaca8af)。

<a id="r_a1cb9a3456c4e3c7a65c5132052f4605a"></a>

```c
volatile uint32_t lb_masked [256]
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[lb_masked](#a1cb9a3456c4e3c7a65c5132052f4605a)。

<a id="r_aece662b5260db9a8b43fc61ebd7a288c"></a>

```c
volatile uint32_t ub_masked [256]
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[ub_masked](#aece662b5260db9a8b43fc61ebd7a288c)。

## 13.2\_详细说明（Detailed Documentation）

<a id="ab1490ee6715fafdce3c67a2c5990b236"></a>

### `[union]`

```c
union { ... } gpio_cmsdk_ahb
```

<a id="a325a85d7d5fa3830ee9a7e922bed08ae"></a>

### `altfuncclr`

```c
volatile uint32_t gpio_cmsdk_ahb::altfuncclr
```

<a id="a5f70dc42911502ff96254f44ff385caa"></a>

### `altfuncset`

```c
volatile uint32_t gpio_cmsdk_ahb::altfuncset
```

<a id="accd586d346c6588ae93fc409159fa368"></a>

### `data`

```c
volatile uint32_t gpio_cmsdk_ahb::data
```

<a id="af548def1b32a28d043b4bbfdddc29662"></a>

### `dataout`

```c
volatile uint32_t gpio_cmsdk_ahb::dataout
```

<a id="aa3a3638d45f9dddd4f122b8081ac46cf"></a>

### `intclear`

```c
volatile uint32_t gpio_cmsdk_ahb::intclear
```

<a id="a83a77418db66bd89bae093533a168617"></a>

### `intenclr`

```c
volatile uint32_t gpio_cmsdk_ahb::intenclr
```

<a id="a5c79dd58c92ee471c86cf420a02a3afb"></a>

### `intenset`

```c
volatile uint32_t gpio_cmsdk_ahb::intenset
```

<a id="addc9f323303ed2888a047a54ff2d2092"></a>

### `intpolclr`

```c
volatile uint32_t gpio_cmsdk_ahb::intpolclr
```

<a id="af76e1a0e03e7a1373a4029f9865a1abb"></a>

### `intpolset`

```c
volatile uint32_t gpio_cmsdk_ahb::intpolset
```

<a id="a5bc3851b26cb0340208f4b93ef475042"></a>

### `intstatus`

```c
volatile uint32_t gpio_cmsdk_ahb::intstatus
```

<a id="af54ff4e5327fa86546166df38f76d3df"></a>

### `inttypeclr`

```c
volatile uint32_t gpio_cmsdk_ahb::inttypeclr
```

<a id="abf5caf8e369d4629aabe935f63bd8f7e"></a>

### `inttypeset`

```c
volatile uint32_t gpio_cmsdk_ahb::inttypeset
```

<a id="a1cb9a3456c4e3c7a65c5132052f4605a"></a>

### `lb_masked`

```c
volatile uint32_t gpio_cmsdk_ahb::lb_masked[256]
```

<a id="a20babd83013581d8273570c5b63658b4"></a>

### `outenableclr`

```c
volatile uint32_t gpio_cmsdk_ahb::outenableclr
```

<a id="ac5de9ecb2427bdf0dfc78099253ce2de"></a>

### `outenableset`

```c
volatile uint32_t gpio_cmsdk_ahb::outenableset
```

<a id="a995563a125b425a4633f4d25ccaff0cd"></a>

### `reserved0`

```c
volatile uint32_t gpio_cmsdk_ahb::reserved0[2]
```

<a id="ae8c9c5c849a45f86b84b21266eaca8af"></a>

### `reserved1`

```c
volatile uint32_t gpio_cmsdk_ahb::reserved1[241]
```

<a id="aece662b5260db9a8b43fc61ebd7a288c"></a>

### `ub_masked`

```c
volatile uint32_t gpio_cmsdk_ahb::ub_masked[256]
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/gpio/gpio_cmsdk_ahb.h`

## 13.3\_原页交叉引用（Cross References）

- [zephyr/drivers/gpio/gpio_cmsdk_ahb.h](https://docs.zephyrproject.org/latest/doxygen/html/gpio__cmsdk__ahb_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [gpio_cmsdk_ahb](P013_gpio_cmsdk_ahb_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P012_gpio_acpi_res_结构体.md) · [返回大纲](大纲.md) · [下一章](P014_gpio_ra_callback_结构体.md)
