---
id: learning.zephyr-docs.device-power-control-model-reference.page-90
title: st_transfer_info_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structst__transfer__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第90章\_st\_transfer\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structst__transfer__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

传输信息（Transfer Information）结构。

```c
#include <zephyr/drivers/misc/renesas_rx_dtc/renesas_rx_dtc.h>
```

<a id="details"></a>

传输信息（Transfer Information）结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 90.1\_数据成员（Data Fields）

```c
union {
```

```c
struct {
```

<a id="r_ae375284d663701f6a2db5f36ebcee5f9"></a>

```c
unsigned int: 16
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[int](#a0f204801dac4e90a7a15b42ab80f4a25)。

<a id="r_a400d28bdaab5334a427b19d844d3ccc9"></a>

```c
transfer_addr_mode_t dest_addr_mode: 2
```

相关声明：[transfer_addr_mode_t](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#ae69bf278e293c26a27b5752894ea3678)、[dest_addr_mode](#a1df273b66e7b94cfa7a66acd867f7fc1)。

目的地址模式（Destination address mode）。

<a id="r_aeab5c8fab25dacde01a0153d361aa294"></a>

```c
transfer_repeat_area_t repeat_area: 1
```

相关声明：[transfer_repeat_area_t](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#af5ab2f4c329bd42eb7893a1aece381f5)、[repeat_area](#a54be0eab840afa257b9fb5e3c407e676)。

目的地址模式（Destination address mode）。

<a id="r_a2f1cb31accc3d317dadad465a41153f2"></a>

```c
transfer_irq_t irq: 1
```

相关声明：[transfer_irq_t](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#ad550861b5af9e2d116b03ddc440f6c35)、[irq](#ac862423e3f7bbe27210483f695416ce4)。

IRQ 类型。

<a id="r_af727b74a2c2ff86fef7a508fc1cc402e"></a>

```c
transfer_chain_mode_t chain_mode: 2
```

相关声明：[transfer_chain_mode_t](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#a1c9f7b59f5fcfeaeb6e528c2b3b067ff)、[chain_mode](#ad8cd2bd49b28519e6ed2bd0e23799f9e)。

链模式（Chain mode）。

<a id="r_aad2efa0c0acd8a3df516cb37285d5679"></a>

```c
transfer_addr_mode_t src_addr_mode: 2
```

相关声明：[transfer_addr_mode_t](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#ae69bf278e293c26a27b5752894ea3678)、[src_addr_mode](#a1562895c38866a2a76fe760a8edf9960)。

源地址模式（Source address mode）。

<a id="r_a580dbe883e4e22bae6b9883bff29ed43"></a>

```c
transfer_size_t size: 2
```

相关声明：[transfer_size_t](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#ada156bb47034b335a8e57d7cdff02238)、[size](#aaec02eb51bd25b81f5d71d19d917ddd6)。

传输数据大小。

<a id="r_af8726ca1d65407f1ee7917d636cfa473"></a>

```c
transfer_mode_t mode: 2
```

相关声明：[transfer_mode_t](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#aea0db2ddbbc3831666b0bf2bb4cc0fb5)、[mode](#adb22c126009e9e1c4a366c73a0bc7198)。

传输模式。

<a id="r_ad5fe6b44d9776bffa64f7b9cd232105d"></a>

```c
} transfer_settings_word_b
```

相关声明：[transfer_settings_word_b](#a49575b1bace4cee0c2eacf7925b3e670)。

<a id="r_aa224e9ef0d9e02e843d1eb715ab812a7"></a>

```c
uint32_t transfer_settings_word
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[transfer_settings_word](#af8d76658b3b39b9fa26169fdced6f48d)。

原始设置（Raw settings）。

<a id="r_ab828e9d1dff347411194ff931e5f4e32"></a>

```c
};
```

<a id="r_a7f7b11076c155d42b2965694c9697799"></a>

```c
void const *volatile p_src
```

相关声明：[p_src](#a7f7b11076c155d42b2965694c9697799)。

源地址。

<a id="r_ab9c64e2333ad51986d13bb9e5c0d17ab"></a>

```c
void *volatile p_dest
```

相关声明：[p_dest](#ab9c64e2333ad51986d13bb9e5c0d17ab)。

目的地址（Destination Address）。

<a id="r_abbeeb3232253a9556e2773559fead24b"></a>

```c
volatile uint16_t num_blocks
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[num_blocks](#abbeeb3232253a9556e2773559fead24b)。

块数。

<a id="r_ae8a814a11a9ba0af8452c1ef813551a0"></a>

```c
volatile uint16_t length
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[length](#ae8a814a11a9ba0af8452c1ef813551a0)。

传输长度。

## 90.2\_详细说明（Detailed Documentation）

<a id="ab828e9d1dff347411194ff931e5f4e32"></a>

### `[union]`

```c
union { ... } st_transfer_info
```

<a id="ad8cd2bd49b28519e6ed2bd0e23799f9e"></a>

### `chain_mode`

```c
transfer_chain_mode_t st_transfer_info::chain_mode
```

链模式（Chain mode）。

<a id="a1df273b66e7b94cfa7a66acd867f7fc1"></a>

### `dest_addr_mode`

```c
transfer_addr_mode_t st_transfer_info::dest_addr_mode
```

目的地址模式（Destination address mode）。

<a id="a0f204801dac4e90a7a15b42ab80f4a25"></a>

### `int`

```c
unsigned st_transfer_info::int
```

<a id="ac862423e3f7bbe27210483f695416ce4"></a>

### `irq`

```c
transfer_irq_t st_transfer_info::irq
```

IRQ 类型。

<a id="ae8a814a11a9ba0af8452c1ef813551a0"></a>

### `length`

```c
volatile uint16_t st_transfer_info::length
```

传输长度。

<a id="adb22c126009e9e1c4a366c73a0bc7198"></a>

### `mode`

```c
transfer_mode_t st_transfer_info::mode
```

传输模式。

<a id="abbeeb3232253a9556e2773559fead24b"></a>

### `num_blocks`

```c
volatile uint16_t st_transfer_info::num_blocks
```

块数。

<a id="ab9c64e2333ad51986d13bb9e5c0d17ab"></a>

### `p_dest`

```c
void* volatile st_transfer_info::p_dest
```

目的地址（Destination Address）。

<a id="a7f7b11076c155d42b2965694c9697799"></a>

### `p_src`

```c
void const* volatile st_transfer_info::p_src
```

源地址。

<a id="a54be0eab840afa257b9fb5e3c407e676"></a>

### `repeat_area`

```c
transfer_repeat_area_t st_transfer_info::repeat_area
```

目的地址模式（Destination address mode）。

<a id="aaec02eb51bd25b81f5d71d19d917ddd6"></a>

### `size`

```c
transfer_size_t st_transfer_info::size
```

传输数据大小。

<a id="a1562895c38866a2a76fe760a8edf9960"></a>

### `src_addr_mode`

```c
transfer_addr_mode_t st_transfer_info::src_addr_mode
```

源地址模式（Source address mode）。

<a id="af8d76658b3b39b9fa26169fdced6f48d"></a>

### `transfer_settings_word`

```c
uint32_t st_transfer_info::transfer_settings_word
```

原始设置（Raw settings）。

<a id="a49575b1bace4cee0c2eacf7925b3e670"></a>

### `[struct]`

```c
struct { ... } st_transfer_info::transfer_settings_word_b
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/misc/renesas_rx_dtc/renesas_rx_dtc.h`

## 90.3\_原页交叉引用（Cross References）

- [zephyr/drivers/misc/renesas_rx_dtc/renesas_rx_dtc.h](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h_source.html)
- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)
- [transfer_addr_mode_t](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#ae69bf278e293c26a27b5752894ea3678)
- [transfer_repeat_area_t](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#af5ab2f4c329bd42eb7893a1aece381f5)
- [transfer_irq_t](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#ad550861b5af9e2d116b03ddc440f6c35)
- [transfer_chain_mode_t](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#a1c9f7b59f5fcfeaeb6e528c2b3b067ff)
- [transfer_size_t](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#ada156bb47034b335a8e57d7cdff02238)
- [transfer_mode_t](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html#aea0db2ddbbc3831666b0bf2bb4cc0fb5)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [st_transfer_info](P090_st_transfer_info_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P089_silabs_siwx91x_clock_control_pll_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P091_st_transfer_properties_结构体.md)
