---
id: learning.zephyr-docs.clock-cmsis-model-reference.page-8
title: clock_mchp_subsys_dfll48m_config_结构体
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structclock__mchp__subsys__dfll48m__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_clock\_mchp\_subsys\_dfll48m\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structclock__mchp__subsys__dfll48m__config.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

48 MHz 数字锁频环（Digital Frequency-Locked Loop，DFLL）配置结构体。

```c
#include <zephyr/drivers/clock_control/mchp_clock_pic32ck_sg_gc.h>
```

<a id="details"></a>

48 MHz 数字锁频环（Digital Frequency-Locked Loop，DFLL）配置结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 8.1\_数据成员（Data Fields）

<a id="r_a8b5dca59c164a9c785fc763ed97dbcbd"></a>

```c
bool on_demand_en
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[on_demand_en](#a8b5dca59c164a9c785fc763ed97dbcbd)。

外设请求将振荡器用作时钟源时，配置振荡器开启。

<a id="r_a5f06274d52ac9a342f62361bb6451cc3"></a>

```c
bool closed_loop_en
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[closed_loop_en](#a5f06274d52ac9a342f62361bb6451cc3)。

启用开环运行（Open-loop Operation）。

<a id="r_af9b0a365f56ef718b2bb74e460f74df9"></a>

```c
enum clock_mchp_gclkgen src
```

相关声明：[clock_mchp_gclkgen](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cz__ca.html#gaab34442b0d6c171691ae299675542777)、[src](#af9b0a365f56ef718b2bb74e460f74df9)。

参考源时钟选择（Reference Source Clock Selection）。

<a id="r_a0056a9d73d353a31c5c6303e4f96fa1d"></a>

```c
uint16_t multiply_factor
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[multiply_factor](#a0056a9d73d353a31c5c6303e4f96fa1d)。

确定 `CLK_DFLL48M` 输出频率与 `CLK_DFLL48M_REF` 输入频率的比值，范围为 0–65535。

## 8.2\_详细说明（Detailed Documentation）

<a id="a5f06274d52ac9a342f62361bb6451cc3"></a>

### `closed_loop_en`

```c
bool clock_mchp_subsys_dfll48m_config::closed_loop_en
```

启用开环运行（Open-loop Operation）。

启用闭环运行（Closed-loop Operation）。

<a id="a0056a9d73d353a31c5c6303e4f96fa1d"></a>

### `multiply_factor`

```c
uint16_t clock_mchp_subsys_dfll48m_config::multiply_factor
```

确定 `CLK_DFLL48M` 输出频率与 `CLK_DFLL48M_REF` 输入频率的比值，范围为 0–65535。

<a id="a8b5dca59c164a9c785fc763ed97dbcbd"></a>

### `on_demand_en`

```c
bool clock_mchp_subsys_dfll48m_config::on_demand_en
```

外设请求将振荡器用作时钟源时，配置振荡器开启。

<a id="af9b0a365f56ef718b2bb74e460f74df9"></a>

### `src`

```c
enum clock_mchp_gclkgen clock_mchp_subsys_dfll48m_config::src
```

参考源时钟选择（Reference Source Clock Selection）。

本结构体文档由以下文件生成：

- `zephyr/drivers/clock_control/mchp_clock_pic32ck_sg_gc.h`
- `zephyr/drivers/clock_control/mchp_clock_pic32cm_sg_gc.h`
- `zephyr/drivers/clock_control/mchp_clock_pic32cz_ca.h`

## 8.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/mchp_clock_pic32ck_sg_gc.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32ck__sg__gc_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [clock_mchp_gclkgen](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mchp__pic32cz__ca.html#gaab34442b0d6c171691ae299675542777)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [mchp_clock_pic32cm_sg_gc.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cm__sg__gc_8h_source.html)
- [mchp_clock_pic32cz_ca.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__clock__pic32cz__ca_8h_source.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P007_clock_control_rx_subsys_cfg_结构体.md) · [返回大纲](大纲.md) · [下一章](P009_clock_mchp_subsys_dfll_config_结构体.md)
