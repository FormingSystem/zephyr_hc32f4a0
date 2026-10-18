---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-82
title: sdhc_host_caps_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsdhc__host__caps.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第82章\_sdhc\_host\_caps\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsdhc__host__caps.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

SD主控制器（Host Controller）的能力。

```c
#include <zephyr/drivers/sdhc.h>
```

<a id="details"></a>

SD 主机控制器能力（Capabilities）。这些能力标志应由 SDHC 驱动通过 `sdhc_get_host_props` API 设置。标志经过紧凑排列，与 SD 协会（SD Association）标准规范中的能力寄存器相匹配。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 82.1\_数据成员（Data Fields）

<a id="r_a3a57e12aa8f53ad1c1fb44696622f587"></a>

```c
unsigned int timeout_clk_freq: 6
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[timeout_clk_freq](#a3a57e12aa8f53ad1c1fb44696622f587)。

超时时钟频率（Timeout clock frequency）。

<a id="r_a8af558ed3b7af437f1782aea9ee6794e"></a>

```c
unsigned int timeout_clk_unit: 1
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[timeout_clk_unit](#a8af558ed3b7af437f1782aea9ee6794e)。

超时时钟单位。

<a id="r_a20ada015fecce002d233fefac5c4ead4"></a>

```c
unsigned int sd_base_clk: 8
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[sd_base_clk](#a20ada015fecce002d233fefac5c4ead4)。

SD 基础时钟频率（Base clock frequency）。

<a id="r_a97dbad3360b56a44fb1ab0d77aa90bc4"></a>

```c
unsigned int max_blk_len: 2
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[max_blk_len](#a97dbad3360b56a44fb1ab0d77aa90bc4)。

最大块长度。

<a id="r_ad09f103fc8ce341d25e1f824e97bd665"></a>

```c
unsigned int bus_8_bit_support: 1
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[bus_8_bit_support](#ad09f103fc8ce341d25e1f824e97bd665)。

是否支持嵌入式设备的 8 位模式。

<a id="r_acfa1c5e96f2afeab40185a1ef37d7efb"></a>

```c
unsigned int adma_2_support: 1
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[adma_2_support](#acfa1c5e96f2afeab40185a1ef37d7efb)。

是否支持高级 DMA 2（ADMA2）。

<a id="r_aaec0cd01cc4e8bf334e5c3ee151d5d98"></a>

```c
unsigned int high_spd_support: 1
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[high_spd_support](#aaec0cd01cc4e8bf334e5c3ee151d5d98)。

是否支持高速模式（High speed）。

<a id="r_a22f2877854669589f0483cf91e504df6"></a>

```c
unsigned int sdma_support: 1
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[sdma_support](#a22f2877854669589f0483cf91e504df6)。

是否支持 SDMA。

<a id="r_af343879ebc21f5c2d57ffa962dacb796"></a>

```c
unsigned int suspend_res_support: 1
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[suspend_res_support](#af343879ebc21f5c2d57ffa962dacb796)。

是否支持挂起/恢复（Suspend/Resume）。

<a id="r_ac6e2eb088ed7d7c3f3f5011ad55ba543"></a>

```c
unsigned int vol_330_support: 1
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[vol_330_support](#ac6e2eb088ed7d7c3f3f5011ad55ba543)。

是否支持 3.3 V 电压。

<a id="r_a7fdf6832fbcc9dce7e20ee87d9063665"></a>

```c
unsigned int vol_300_support: 1
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[vol_300_support](#a7fdf6832fbcc9dce7e20ee87d9063665)。

是否支持 3.0 V 电压。

<a id="r_aa39ef2d70314dbf2517bd3df6fbd4694"></a>

```c
unsigned int vol_180_support: 1
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[vol_180_support](#aa39ef2d70314dbf2517bd3df6fbd4694)。

是否支持 1.8 V 电压。

<a id="r_ad8e4ca0d2fb39486b469224218d2eb7b"></a>

```c
unsigned int address_64_bit_support_v4: 1
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[address_64_bit_support_v4](#ad8e4ca0d2fb39486b469224218d2eb7b)。

是否支持 V4 的 64 位系统地址。

<a id="r_a0f33c7e168ade12675795d2c0d5b5ea2"></a>

```c
unsigned int address_64_bit_support_v3: 1
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[address_64_bit_support_v3](#a0f33c7e168ade12675795d2c0d5b5ea2)。

是否支持 V3 的 64 位系统地址。

<a id="r_a6fa0525ee3b2a0313cc9b83dc820b831"></a>

```c
unsigned int sdio_async_interrupt_support: 1
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[sdio_async_interrupt_support](#a6fa0525ee3b2a0313cc9b83dc820b831)。

是否支持异步中断（Asynchronous interrupt）。

<a id="r_a3231007bc5fcc731e97236b29333f7ee"></a>

```c
unsigned int slot_type: 2
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[slot_type](#a3231007bc5fcc731e97236b29333f7ee)。

插槽类型（Slot type）。

<a id="r_a63dabbc7c24dc41c8103be81ee6e673f"></a>

```c
unsigned int sdr50_support: 1
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[sdr50_support](#a63dabbc7c24dc41c8103be81ee6e673f)。

是否支持 SDR50。

<a id="r_a3e6f73ea9df9c207cddda31de45621be"></a>

```c
unsigned int sdr104_support: 1
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[sdr104_support](#a3e6f73ea9df9c207cddda31de45621be)。

是否支持 SDR104。

<a id="r_aa22adb0079aa3864df4461d841852684"></a>

```c
unsigned int ddr50_support: 1
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[ddr50_support](#aa22adb0079aa3864df4461d841852684)。

是否支持 DDR50。

<a id="r_a146c7403d7ecbbffbd6aa0c1c4fad1b5"></a>

```c
unsigned int uhs_2_support: 1
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[uhs_2_support](#a146c7403d7ecbbffbd6aa0c1c4fad1b5)。

是否支持超高速 II（UHS-II）。

<a id="r_a43086e5bc5d6384b8eb0709c1cf1756e"></a>

```c
unsigned int drv_type_a_support: 1
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[drv_type_a_support](#a43086e5bc5d6384b8eb0709c1cf1756e)。

是否支持 A 型驱动（Driver type A）。

<a id="r_aafcfb75fd131430df0a372e6ac2c8b34"></a>

```c
unsigned int drv_type_c_support: 1
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[drv_type_c_support](#aafcfb75fd131430df0a372e6ac2c8b34)。

是否支持 C 型驱动（Driver type C）。

<a id="r_ad2c9e66bbd9a442d872fd559fd7a833c"></a>

```c
unsigned int drv_type_d_support: 1
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[drv_type_d_support](#ad2c9e66bbd9a442d872fd559fd7a833c)。

是否支持 D 型驱动（Driver type D）。

<a id="r_ab7a145bf44747d7d9e68ff743520cc2c"></a>

```c
unsigned int retune_timer_count: 4
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[retune_timer_count](#ab7a145bf44747d7d9e68ff743520cc2c)。

重新调谐（Re-tuning）的计时器计数。

<a id="r_ac54a191e04ff6c266390d1fb8d4f84d3"></a>

```c
unsigned int sdr50_needs_tuning: 1
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[sdr50_needs_tuning](#ac54a191e04ff6c266390d1fb8d4f84d3)。

是否为 SDR50 使用调谐。

<a id="r_a48680d522d417e68ec3371b3831faa01"></a>

```c
unsigned int retuning_mode: 2
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[retuning_mode](#a48680d522d417e68ec3371b3831faa01)。

重新调谐模式。

<a id="r_afffade3ad661ead23ed0f74b770172ff"></a>

```c
unsigned int clk_multiplier: 8
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[clk_multiplier](#afffade3ad661ead23ed0f74b770172ff)。

时钟倍频系数（Clock multiplier）。

<a id="r_a90a90218bcd866cbfae2354c5b0af3de"></a>

```c
unsigned int adma3_support: 1
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[adma3_support](#a90a90218bcd866cbfae2354c5b0af3de)。

是否支持 ADMA3。

<a id="r_a2f5d5859cbe06ab449f95c0a108c2250"></a>

```c
unsigned int vdd2_180_support: 1
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[vdd2_180_support](#a2f5d5859cbe06ab449f95c0a108c2250)。

是否支持 1.8 V 的 VDD2。

## 82.2\_详细说明（Detailed Documentation）

<a id="a0f33c7e168ade12675795d2c0d5b5ea2"></a>

### `address_64_bit_support_v3`

```c
unsigned int sdhc_host_caps::address_64_bit_support_v3
```

是否支持 V3 的 64 位系统地址。

<a id="ad8e4ca0d2fb39486b469224218d2eb7b"></a>

### `address_64_bit_support_v4`

```c
unsigned int sdhc_host_caps::address_64_bit_support_v4
```

是否支持 V4 的 64 位系统地址。

<a id="a90a90218bcd866cbfae2354c5b0af3de"></a>

### `adma3_support`

```c
unsigned int sdhc_host_caps::adma3_support
```

是否支持 ADMA3。

<a id="acfa1c5e96f2afeab40185a1ef37d7efb"></a>

### `adma_2_support`

```c
unsigned int sdhc_host_caps::adma_2_support
```

是否支持高级 DMA 2（ADMA2）。

<a id="ad09f103fc8ce341d25e1f824e97bd665"></a>

### `bus_8_bit_support`

```c
unsigned int sdhc_host_caps::bus_8_bit_support
```

是否支持嵌入式设备的 8 位模式。

<a id="afffade3ad661ead23ed0f74b770172ff"></a>

### `clk_multiplier`

```c
unsigned int sdhc_host_caps::clk_multiplier
```

时钟倍频系数（Clock multiplier）。

<a id="aa22adb0079aa3864df4461d841852684"></a>

### `ddr50_support`

```c
unsigned int sdhc_host_caps::ddr50_support
```

是否支持 DDR50。

<a id="a43086e5bc5d6384b8eb0709c1cf1756e"></a>

### `drv_type_a_support`

```c
unsigned int sdhc_host_caps::drv_type_a_support
```

是否支持 A 型驱动（Driver type A）。

<a id="aafcfb75fd131430df0a372e6ac2c8b34"></a>

### `drv_type_c_support`

```c
unsigned int sdhc_host_caps::drv_type_c_support
```

是否支持 C 型驱动（Driver type C）。

<a id="ad2c9e66bbd9a442d872fd559fd7a833c"></a>

### `drv_type_d_support`

```c
unsigned int sdhc_host_caps::drv_type_d_support
```

是否支持 D 型驱动（Driver type D）。

<a id="aaec0cd01cc4e8bf334e5c3ee151d5d98"></a>

### `high_spd_support`

```c
unsigned int sdhc_host_caps::high_spd_support
```

是否支持高速模式（High speed）。

<a id="a97dbad3360b56a44fb1ab0d77aa90bc4"></a>

### `max_blk_len`

```c
unsigned int sdhc_host_caps::max_blk_len
```

最大块长度。

<a id="ab7a145bf44747d7d9e68ff743520cc2c"></a>

### `retune_timer_count`

```c
unsigned int sdhc_host_caps::retune_timer_count
```

重新调谐（Re-tuning）的计时器计数。

<a id="a48680d522d417e68ec3371b3831faa01"></a>

### `retuning_mode`

```c
unsigned int sdhc_host_caps::retuning_mode
```

重新调谐模式。

<a id="a20ada015fecce002d233fefac5c4ead4"></a>

### `sd_base_clk`

```c
unsigned int sdhc_host_caps::sd_base_clk
```

SD 基础时钟频率（Base clock frequency）。

<a id="a6fa0525ee3b2a0313cc9b83dc820b831"></a>

### `sdio_async_interrupt_support`

```c
unsigned int sdhc_host_caps::sdio_async_interrupt_support
```

是否支持异步中断（Asynchronous interrupt）。

<a id="a22f2877854669589f0483cf91e504df6"></a>

### `sdma_support`

```c
unsigned int sdhc_host_caps::sdma_support
```

是否支持 SDMA。

<a id="a3e6f73ea9df9c207cddda31de45621be"></a>

### `sdr104_support`

```c
unsigned int sdhc_host_caps::sdr104_support
```

是否支持 SDR104。

<a id="ac54a191e04ff6c266390d1fb8d4f84d3"></a>

### `sdr50_needs_tuning`

```c
unsigned int sdhc_host_caps::sdr50_needs_tuning
```

是否为 SDR50 使用调谐。

<a id="a63dabbc7c24dc41c8103be81ee6e673f"></a>

### `sdr50_support`

```c
unsigned int sdhc_host_caps::sdr50_support
```

是否支持 SDR50。

<a id="a3231007bc5fcc731e97236b29333f7ee"></a>

### `slot_type`

```c
unsigned int sdhc_host_caps::slot_type
```

插槽类型（Slot type）。

<a id="af343879ebc21f5c2d57ffa962dacb796"></a>

### `suspend_res_support`

```c
unsigned int sdhc_host_caps::suspend_res_support
```

是否支持挂起/恢复（Suspend/Resume）。

<a id="a3a57e12aa8f53ad1c1fb44696622f587"></a>

### `timeout_clk_freq`

```c
unsigned int sdhc_host_caps::timeout_clk_freq
```

超时时钟频率（Timeout clock frequency）。

<a id="a8af558ed3b7af437f1782aea9ee6794e"></a>

### `timeout_clk_unit`

```c
unsigned int sdhc_host_caps::timeout_clk_unit
```

超时时钟单位。

<a id="a146c7403d7ecbbffbd6aa0c1c4fad1b5"></a>

### `uhs_2_support`

```c
unsigned int sdhc_host_caps::uhs_2_support
```

是否支持超高速 II（UHS-II）。

<a id="a2f5d5859cbe06ab449f95c0a108c2250"></a>

### `vdd2_180_support`

```c
unsigned int sdhc_host_caps::vdd2_180_support
```

是否支持 1.8 V 的 VDD2。

<a id="aa39ef2d70314dbf2517bd3df6fbd4694"></a>

### `vol_180_support`

```c
unsigned int sdhc_host_caps::vol_180_support
```

是否支持 1.8 V 电压。

<a id="a7fdf6832fbcc9dce7e20ee87d9063665"></a>

### `vol_300_support`

```c
unsigned int sdhc_host_caps::vol_300_support
```

是否支持 3.0 V 电压。

<a id="ac6e2eb088ed7d7c3f3f5011ad55ba543"></a>

### `vol_330_support`

```c
unsigned int sdhc_host_caps::vol_330_support
```

是否支持 3.3 V 电压。

本数据类型文档由以下文件生成：

- `zephyr/drivers/sdhc.h`

## 82.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sdhc.h](https://docs.zephyrproject.org/latest/doxygen/html/sdhc_8h_source.html)
- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)
- [sdhc_get_host_props](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#gab55cf88ae79e5aa9e2110b298048df8e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P081_sdhc_driver_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P083_sdhc_host_props_结构体.md)
