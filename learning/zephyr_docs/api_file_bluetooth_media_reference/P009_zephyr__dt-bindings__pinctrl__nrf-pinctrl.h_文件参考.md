---
id: learning.zephyr-docs.api-file-bluetooth-media-reference.page-9
title: zephyr__dt-bindings__pinctrl__nrf-pinctrl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nrf-pinctrl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_nrf-pinctrl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/nrf-pinctrl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 9.1\_宏定义（Macros）

<a id="r_a43d0a0ad6e574456a2b69ab5354ccef4"></a>

```c
#define NRF_PSEL(fun, port, pin)
```

相关声明：[NRF_PSEL](#a43d0a0ad6e574456a2b69ab5354ccef4)。

构造 nRF psels 属性条目（Property Entry）的工具宏。

<a id="r_a2e414bdc5912c0e0abc349d5362520bd"></a>

```c
#define NRF_PSEL_DISCONNECTED(fun)
```

相关声明：[NRF_PSEL_DISCONNECTED](#a2e414bdc5912c0e0abc349d5362520bd)。

引脚断开（Disconnected）时，构造 nRF psels 属性条目的工具宏。

<a id="define-members-0"></a>

### nRF引脚配置位域位置与掩码（nRF pin configuration bit field positions and masks.）

<a id="r_a10272aaefd0f103c15ae28ce8ef76987"></a>

```c
#define NRF_FUN_POS 24U
```

相关声明：[NRF_FUN_POS](#a10272aaefd0f103c15ae28ce8ef76987)。

功能字段（Function Field）的位位置。

<a id="r_ae3f5b1848b0c00547eff520f22ede922"></a>

```c
#define NRF_FUN_MSK 0xFFU
```

相关声明：[NRF_FUN_MSK](#ae3f5b1848b0c00547eff520f22ede922)。

功能字段（Function Field）的掩码。

<a id="r_a9203c68fb293d5eec889a8729b5f52b3"></a>

```c
#define NRF_GPD_FAST_ACTIVE1_POS 18U
```

相关声明：[NRF_GPD_FAST_ACTIVE1_POS](#a9203c68fb293d5eec889a8729b5f52b3)。

GPD FAST ACTIVE1 的位位置（Position）。

<a id="r_a1211c8c57f411a7676023c61cc986095"></a>

```c
#define NRF_GPD_FAST_ACTIVE1_MSK 0x1U
```

相关声明：[NRF_GPD_FAST_ACTIVE1_MSK](#a1211c8c57f411a7676023c61cc986095)。

GPD FAST ACTIVE1 的掩码（Mask）。

<a id="r_a1ddd10f13ce7524c777f02a2d96ed727"></a>

```c
#define NRF_CLOCKPIN_ENABLE_POS 17U
```

相关声明：[NRF_CLOCKPIN_ENABLE_POS](#a1ddd10f13ce7524c777f02a2d96ed727)。

clockpin 使能字段（Enable Field）的位位置。

<a id="r_af596f5bff44b420017fe9d0bb1260753"></a>

```c
#define NRF_CLOCKPIN_ENABLE_MSK 0x1U
```

相关声明：[NRF_CLOCKPIN_ENABLE_MSK](#af596f5bff44b420017fe9d0bb1260753)。

clockpin 使能字段（Enable Field）的掩码。

<a id="r_aa13cd70c54db20407bfaef944ea10329"></a>

```c
#define NRF_INVERT_POS 16U
```

相关声明：[NRF_INVERT_POS](#aa13cd70c54db20407bfaef944ea10329)。

反相字段（Invert Field）的位位置。

<a id="r_a1a5cca24fa65f0ea64e8927e9d12ff43"></a>

```c
#define NRF_INVERT_MSK 0x1U
```

相关声明：[NRF_INVERT_MSK](#a1a5cca24fa65f0ea64e8927e9d12ff43)。

反相字段（Invert Field）的掩码。

<a id="r_a97dce1e8b63e4054f23c1daa0ddd6327"></a>

```c
#define NRF_LP_POS 15U
```

相关声明：[NRF_LP_POS](#a97dce1e8b63e4054f23c1daa0ddd6327)。

低功耗字段（Low Power Field）的位位置。

<a id="r_a67b7d47eed25086ebbe5db508c85ff7b"></a>

```c
#define NRF_LP_MSK 0x1U
```

相关声明：[NRF_LP_MSK](#a67b7d47eed25086ebbe5db508c85ff7b)。

低功耗字段（Low Power Field）的掩码。

<a id="r_ae8b94074f18659a2767e0f7f1aa1c73f"></a>

```c
#define NRF_DRIVE_POS 11U
```

相关声明：[NRF_DRIVE_POS](#ae8b94074f18659a2767e0f7f1aa1c73f)。

驱动配置字段（Drive Configuration Field）的位位置。

<a id="r_a86d4555acfb553f6bad1562743cf357c"></a>

```c
#define NRF_DRIVE_MSK 0xFU
```

相关声明：[NRF_DRIVE_MSK](#a86d4555acfb553f6bad1562743cf357c)。

驱动配置字段（Drive Configuration Field）的掩码。

<a id="r_a0fac117bc7a2f45638ce462527cb8daa"></a>

```c
#define NRF_PULL_POS 9U
```

相关声明：[NRF_PULL_POS](#a0fac117bc7a2f45638ce462527cb8daa)。

上下拉配置字段（Pull Configuration Field）的位位置。

<a id="r_a3900fd72d44feeefef9aa73c909a2396"></a>

```c
#define NRF_PULL_MSK 0x3U
```

相关声明：[NRF_PULL_MSK](#a3900fd72d44feeefef9aa73c909a2396)。

上下拉配置字段（Pull Configuration Field）的掩码。

<a id="r_aa057ad8de2dea12959f51a293a929367"></a>

```c
#define NRF_PIN_POS 0U
```

相关声明：[NRF_PIN_POS](#aa057ad8de2dea12959f51a293a929367)。

引脚字段（Pin Field）的位位置。

<a id="r_a8f60ab83a5325691eb0d976ae1f70295"></a>

```c
#define NRF_PIN_MSK 0x1FFU
```

相关声明：[NRF_PIN_MSK](#a8f60ab83a5325691eb0d976ae1f70295)。

引脚字段（Pin Field）的掩码。

<a id="define-members-1"></a>

### nRF引脚控制的引脚功能（nRF pinctrl pin functions.）

<a id="r_a9550ec0625d3e702c41d79cdf633bf9b"></a>

```c
#define NRF_FUN_UART_TX 0U
```

相关声明：[NRF_FUN_UART_TX](#a9550ec0625d3e702c41d79cdf633bf9b)。

UART 发送（TX）。

<a id="r_ad7865c58ddd2d7686482fa2f92a330f8"></a>

```c
#define NRF_FUN_UART_RX 1U
```

相关声明：[NRF_FUN_UART_RX](#ad7865c58ddd2d7686482fa2f92a330f8)。

UART 接收（RX）。

<a id="r_aa2ea1399ee3dff5019adf462b9cb09b8"></a>

```c
#define NRF_FUN_UART_RTS 2U
```

相关声明：[NRF_FUN_UART_RTS](#aa2ea1399ee3dff5019adf462b9cb09b8)。

UART 请求发送（RTS）。

<a id="r_a595b5f913921466ec87c58657709c800"></a>

```c
#define NRF_FUN_UART_CTS 3U
```

相关声明：[NRF_FUN_UART_CTS](#a595b5f913921466ec87c58657709c800)。

UART 清除发送（CTS）。

<a id="r_a2594557c5e765d65ea7627c5c49e07d6"></a>

```c
#define NRF_FUN_SPIM_SCK 4U
```

相关声明：[NRF_FUN_SPIM_SCK](#a2594557c5e765d65ea7627c5c49e07d6)。

SPI 主机（Master）串行时钟（SCK）。

<a id="r_a2e96ea48e6a9e707b76b846536a687cb"></a>

```c
#define NRF_FUN_SPIM_MOSI 5U
```

相关声明：[NRF_FUN_SPIM_MOSI](#a2e96ea48e6a9e707b76b846536a687cb)。

SPI 主机（Master）主出从入（MOSI）。

<a id="r_afca36f99d1c1a9e17e4949f18206490a"></a>

```c
#define NRF_FUN_SPIM_MISO 6U
```

相关声明：[NRF_FUN_SPIM_MISO](#afca36f99d1c1a9e17e4949f18206490a)。

SPI 主机（Master）主入从出（MISO）。

<a id="r_a9906fedc9c9667be7a84c66443f01772"></a>

```c
#define NRF_FUN_SPIS_SCK 7U
```

相关声明：[NRF_FUN_SPIS_SCK](#a9906fedc9c9667be7a84c66443f01772)。

SPI 从机（Slave）串行时钟（SCK）。

<a id="r_a016ffb10db008be19f494e7098096109"></a>

```c
#define NRF_FUN_SPIS_MOSI 8U
```

相关声明：[NRF_FUN_SPIS_MOSI](#a016ffb10db008be19f494e7098096109)。

SPI 从机（Slave）主出从入（MOSI）。

<a id="r_aa480a4b96df9c4521d744de7d9a72e1f"></a>

```c
#define NRF_FUN_SPIS_MISO 9U
```

相关声明：[NRF_FUN_SPIS_MISO](#aa480a4b96df9c4521d744de7d9a72e1f)。

SPI 从机（Slave）主入从出（MISO）。

<a id="r_a6591844a0ce9f0297f917abb2f87c259"></a>

```c
#define NRF_FUN_SPIS_CSN 10U
```

相关声明：[NRF_FUN_SPIS_CSN](#a6591844a0ce9f0297f917abb2f87c259)。

SPI 从机（Slave）低有效片选（CSN）。

<a id="r_aa26e18840b9cc780f35a1c237f24f8f8"></a>

```c
#define NRF_FUN_TWIM_SCL 11U
```

相关声明：[NRF_FUN_TWIM_SCL](#aa26e18840b9cc780f35a1c237f24f8f8)。

TWI 主机（Master）时钟线（SCL）。

<a id="r_a7f0dcd38287a5e8c2e55145e43a57628"></a>

```c
#define NRF_FUN_TWIM_SDA 12U
```

相关声明：[NRF_FUN_TWIM_SDA](#a7f0dcd38287a5e8c2e55145e43a57628)。

TWI 主机（Master）数据线（SDA）。

<a id="r_aae874d5eb9da322f9766c9546c565db2"></a>

```c
#define NRF_FUN_I2S_SCK_M 13U
```

相关声明：[NRF_FUN_I2S_SCK_M](#aae874d5eb9da322f9766c9546c565db2)。

主机模式（Master Mode）下的 I2S 串行时钟（SCK）。

<a id="r_aa791b4bf51162aff1f6cfbc374af826b"></a>

```c
#define NRF_FUN_I2S_SCK_S 14U
```

相关声明：[NRF_FUN_I2S_SCK_S](#aa791b4bf51162aff1f6cfbc374af826b)。

从机模式（Slave Mode）下的 I2S 串行时钟（SCK）。

<a id="r_a8aeef372eba5608f6fa06c3e592bfe69"></a>

```c
#define NRF_FUN_I2S_LRCK_M 15U
```

相关声明：[NRF_FUN_I2S_LRCK_M](#a8aeef372eba5608f6fa06c3e592bfe69)。

主机模式（Master Mode）下的 I2S 左右声道时钟（LRCK）。

<a id="r_aacf6b96aad472ee6423552c80936c375"></a>

```c
#define NRF_FUN_I2S_LRCK_S 16U
```

相关声明：[NRF_FUN_I2S_LRCK_S](#aacf6b96aad472ee6423552c80936c375)。

从机模式（Slave Mode）下的 I2S 左右声道时钟（LRCK）。

<a id="r_ad943106dbd772562b2cca1d063c10456"></a>

```c
#define NRF_FUN_I2S_SDIN 17U
```

相关声明：[NRF_FUN_I2S_SDIN](#ad943106dbd772562b2cca1d063c10456)。

I2S 串行数据输入（SDIN）。

<a id="r_af2966d1e579895b18331480c42145f2f"></a>

```c
#define NRF_FUN_I2S_SDOUT 18U
```

相关声明：[NRF_FUN_I2S_SDOUT](#af2966d1e579895b18331480c42145f2f)。

I2S 串行数据输出（SDOUT）。

<a id="r_a6de3f8d978d2aa864c12410ff3a78741"></a>

```c
#define NRF_FUN_I2S_MCK 19U
```

相关声明：[NRF_FUN_I2S_MCK](#a6de3f8d978d2aa864c12410ff3a78741)。

I2S 主时钟（MCK）。

<a id="r_a5ceee799b932f1b71366bda816cde19a"></a>

```c
#define NRF_FUN_PDM_CLK 20U
```

相关声明：[NRF_FUN_PDM_CLK](#a5ceee799b932f1b71366bda816cde19a)。

PDM 时钟（CLK）。

<a id="r_af8f0c9a76b28fe19a5c4552386b6cd30"></a>

```c
#define NRF_FUN_PDM_DIN 21U
```

相关声明：[NRF_FUN_PDM_DIN](#af8f0c9a76b28fe19a5c4552386b6cd30)。

PDM 数据输入（DIN）。

<a id="r_a9cf56eb616791c1bf79a15de6e11e270"></a>

```c
#define NRF_FUN_PWM_OUT0 22U
```

相关声明：[NRF_FUN_PWM_OUT0](#a9cf56eb616791c1bf79a15de6e11e270)。

PWM 输出0（OUT0）。

<a id="r_a9668fd12e95380431659e5edaa62cf65"></a>

```c
#define NRF_FUN_PWM_OUT1 23U
```

相关声明：[NRF_FUN_PWM_OUT1](#a9668fd12e95380431659e5edaa62cf65)。

PWM 输出1（OUT1）。

<a id="r_a4d9b8e2aba25457f1e688b71a8bcf235"></a>

```c
#define NRF_FUN_PWM_OUT2 24U
```

相关声明：[NRF_FUN_PWM_OUT2](#a4d9b8e2aba25457f1e688b71a8bcf235)。

PWM 输出2（OUT2）。

<a id="r_a79e863ca96b4e14c6eb0367b7b50bd32"></a>

```c
#define NRF_FUN_PWM_OUT3 25U
```

相关声明：[NRF_FUN_PWM_OUT3](#a79e863ca96b4e14c6eb0367b7b50bd32)。

PWM 输出3（OUT3）。

<a id="r_af07b0671c04b3318ad4f6e81f9b02f9b"></a>

```c
#define NRF_FUN_QDEC_A 26U
```

相关声明：[NRF_FUN_QDEC_A](#af07b0671c04b3318ad4f6e81f9b02f9b)。

QDEC A 相（A）。

<a id="r_a3da455a7ac5e260ff25e867212b4b026"></a>

```c
#define NRF_FUN_QDEC_B 27U
```

相关声明：[NRF_FUN_QDEC_B](#a3da455a7ac5e260ff25e867212b4b026)。

QDEC B 相（B）。

<a id="r_a0b4431b76b7c264167fe48294cb5eb3d"></a>

```c
#define NRF_FUN_QDEC_LED 28U
```

相关声明：[NRF_FUN_QDEC_LED](#a0b4431b76b7c264167fe48294cb5eb3d)。

QDEC LED 信号（LED）。

<a id="r_a8504018d0dddd49c009ee8db7f6aa559"></a>

```c
#define NRF_FUN_QSPI_SCK 29U
```

相关声明：[NRF_FUN_QSPI_SCK](#a8504018d0dddd49c009ee8db7f6aa559)。

QSPI 串行时钟（SCK）。

<a id="r_a2ec92b450cc6f75121879950a7a2f750"></a>

```c
#define NRF_FUN_QSPI_CSN 30U
```

相关声明：[NRF_FUN_QSPI_CSN](#a2ec92b450cc6f75121879950a7a2f750)。

QSPI 低有效片选（CSN）。

<a id="r_a97a03ba41e0a1bafe6d44868baf62b21"></a>

```c
#define NRF_FUN_QSPI_IO0 31U
```

相关声明：[NRF_FUN_QSPI_IO0](#a97a03ba41e0a1bafe6d44868baf62b21)。

QSPI 输入输出0（IO0）。

<a id="r_a4a87c54c51d9ab5e602a62f9ec70e98e"></a>

```c
#define NRF_FUN_QSPI_IO1 32U
```

相关声明：[NRF_FUN_QSPI_IO1](#a4a87c54c51d9ab5e602a62f9ec70e98e)。

QSPI 输入输出1（IO1）。

<a id="r_a0bd9c69689a0ec5c88eb4d50ff1c73dd"></a>

```c
#define NRF_FUN_QSPI_IO2 33U
```

相关声明：[NRF_FUN_QSPI_IO2](#a0bd9c69689a0ec5c88eb4d50ff1c73dd)。

QSPI 输入输出2（IO2）。

<a id="r_aaf2c957da80884f0a8d442da64da8b92"></a>

```c
#define NRF_FUN_QSPI_IO3 34U
```

相关声明：[NRF_FUN_QSPI_IO3](#aaf2c957da80884f0a8d442da64da8b92)。

QSPI 输入输出3（IO3）。

<a id="r_a77453afa40269edfcdc2039a5c2a98e2"></a>

```c
#define NRF_FUN_MSPI_SCK NRF_FUN_QSPI_SCK
```

相关声明：[NRF_FUN_MSPI_SCK](#a77453afa40269edfcdc2039a5c2a98e2)、[NRF_FUN_QSPI_SCK](#a8504018d0dddd49c009ee8db7f6aa559)。

MSPI 串行时钟（SCK）。

<a id="r_a3d70a426c4c0deac34eb9f36bd0df63e"></a>

```c
#define NRF_FUN_MSPI_CSN NRF_FUN_QSPI_CSN
```

相关声明：[NRF_FUN_MSPI_CSN](#a3d70a426c4c0deac34eb9f36bd0df63e)、[NRF_FUN_QSPI_CSN](#a2ec92b450cc6f75121879950a7a2f750)。

MSPI 低有效片选（CSN）。

<a id="r_a076c99fe48544f8c9e98927b5e10fb93"></a>

```c
#define NRF_FUN_MSPI_IO0 NRF_FUN_QSPI_IO0
```

相关声明：[NRF_FUN_MSPI_IO0](#a076c99fe48544f8c9e98927b5e10fb93)、[NRF_FUN_QSPI_IO0](#a97a03ba41e0a1bafe6d44868baf62b21)。

MSPI 输入输出0（IO0）。

<a id="r_a1d57b9cdd49669e67f86307e4b51d700"></a>

```c
#define NRF_FUN_MSPI_IO1 NRF_FUN_QSPI_IO1
```

相关声明：[NRF_FUN_MSPI_IO1](#a1d57b9cdd49669e67f86307e4b51d700)、[NRF_FUN_QSPI_IO1](#a4a87c54c51d9ab5e602a62f9ec70e98e)。

MSPI 输入输出1（IO1）。

<a id="r_ad18416245f40aee50fd970c7b1a31ace"></a>

```c
#define NRF_FUN_MSPI_IO2 NRF_FUN_QSPI_IO2
```

相关声明：[NRF_FUN_MSPI_IO2](#ad18416245f40aee50fd970c7b1a31ace)、[NRF_FUN_QSPI_IO2](#a0bd9c69689a0ec5c88eb4d50ff1c73dd)。

MSPI 输入输出2（IO2）。

<a id="r_a4d5395d0e61119185d3c71228045a333"></a>

```c
#define NRF_FUN_MSPI_IO3 NRF_FUN_QSPI_IO3
```

相关声明：[NRF_FUN_MSPI_IO3](#a4d5395d0e61119185d3c71228045a333)、[NRF_FUN_QSPI_IO3](#aaf2c957da80884f0a8d442da64da8b92)。

MSPI 输入输出3（IO3）。

<a id="r_a9e02aa751912dd3e3ad3964bd2e92b1b"></a>

```c
#define NRF_FUN_EXMIF_CK 35U
```

相关声明：[NRF_FUN_EXMIF_CK](#a9e02aa751912dd3e3ad3964bd2e92b1b)。

EXMIF 时钟（CK）。

<a id="r_afe37cd483f85609e7f82044995c7245d"></a>

```c
#define NRF_FUN_EXMIF_DQ0 36U
```

相关声明：[NRF_FUN_EXMIF_DQ0](#afe37cd483f85609e7f82044995c7245d)。

EXMIF 数据0（DQ0）。

<a id="r_ab58883df980cf4e61b1d74a473a58563"></a>

```c
#define NRF_FUN_EXMIF_DQ1 37U
```

相关声明：[NRF_FUN_EXMIF_DQ1](#ab58883df980cf4e61b1d74a473a58563)。

EXMIF 数据1（DQ1）。

<a id="r_ad358c9ec0f07e70cfc11313c4f09073c"></a>

```c
#define NRF_FUN_EXMIF_DQ2 38U
```

相关声明：[NRF_FUN_EXMIF_DQ2](#ad358c9ec0f07e70cfc11313c4f09073c)。

EXMIF 数据2（DQ2）。

<a id="r_ac7ef6d6a949d228bdaf5635ae5182262"></a>

```c
#define NRF_FUN_EXMIF_DQ3 39U
```

相关声明：[NRF_FUN_EXMIF_DQ3](#ac7ef6d6a949d228bdaf5635ae5182262)。

EXMIF 数据3（DQ3）。

<a id="r_ab74f922a6687ddc1fce33b8f508064b7"></a>

```c
#define NRF_FUN_EXMIF_DQ4 40U
```

相关声明：[NRF_FUN_EXMIF_DQ4](#ab74f922a6687ddc1fce33b8f508064b7)。

EXMIF 数据4（DQ4）。

<a id="r_a144b60ce024fadb107e19de376f2077c"></a>

```c
#define NRF_FUN_EXMIF_DQ5 41U
```

相关声明：[NRF_FUN_EXMIF_DQ5](#a144b60ce024fadb107e19de376f2077c)。

EXMIF 数据5（DQ5）。

<a id="r_a8eb7a3680c93054ed76d1d6603ee9425"></a>

```c
#define NRF_FUN_EXMIF_DQ6 42U
```

相关声明：[NRF_FUN_EXMIF_DQ6](#a8eb7a3680c93054ed76d1d6603ee9425)。

EXMIF 数据6（DQ6）。

<a id="r_a8cc2db3d1d971145411645135a29bf18"></a>

```c
#define NRF_FUN_EXMIF_DQ7 43U
```

相关声明：[NRF_FUN_EXMIF_DQ7](#a8cc2db3d1d971145411645135a29bf18)。

EXMIF 数据7（DQ7）。

<a id="r_a25571f907b7d808c6d757c2b273287d3"></a>

```c
#define NRF_FUN_EXMIF_CS0 44U
```

相关声明：[NRF_FUN_EXMIF_CS0](#a25571f907b7d808c6d757c2b273287d3)。

EXMIF 片选0（CS0）。

<a id="r_aa80dee2db548ab0ba3de943046ff24af"></a>

```c
#define NRF_FUN_EXMIF_CS1 45U
```

相关声明：[NRF_FUN_EXMIF_CS1](#aa80dee2db548ab0ba3de943046ff24af)。

EXMIF 片选1（CS1）。

<a id="r_a34338fa4c8ab9e606bdc00d8cfe288ef"></a>

```c
#define NRF_FUN_CAN_TX 46U
```

相关声明：[NRF_FUN_CAN_TX](#a34338fa4c8ab9e606bdc00d8cfe288ef)。

CAN 发送（TX）。

<a id="r_a55a2841880cd17f8d8a6ff5fb67ec71b"></a>

```c
#define NRF_FUN_CAN_RX 47U
```

相关声明：[NRF_FUN_CAN_RX](#a55a2841880cd17f8d8a6ff5fb67ec71b)。

CAN 接收（RX）。

<a id="r_a991d00b1a2fafff3f5f1a107d1c92b28"></a>

```c
#define NRF_FUN_TWIS_SCL 48U
```

相关声明：[NRF_FUN_TWIS_SCL](#a991d00b1a2fafff3f5f1a107d1c92b28)。

TWIS 时钟线（SCL）。

<a id="r_ae680ea89fa8da33f4bee9f3d30ea3c66"></a>

```c
#define NRF_FUN_TWIS_SDA 49U
```

相关声明：[NRF_FUN_TWIS_SDA](#ae680ea89fa8da33f4bee9f3d30ea3c66)。

TWIS 数据线（SDA）。

<a id="r_ad95c35e659797da017ae8bfd9f436968"></a>

```c
#define NRF_FUN_EXMIF_RWDS 50U
```

相关声明：[NRF_FUN_EXMIF_RWDS](#ad95c35e659797da017ae8bfd9f436968)。

EXMIF 读写数据选通（RWDS）。

<a id="r_a06ece4c8604d693297d063bbc236c084"></a>

```c
#define NRF_FUN_GRTC_CLKOUT_FAST 55U
```

相关声明：[NRF_FUN_GRTC_CLKOUT_FAST](#a06ece4c8604d693297d063bbc236c084)。

全局实时时钟（GRTC）的快速时钟输出（Fast Clock Output）。

<a id="r_a7c0fb8d0cd3a5557b3ac9ee7c7ebeffa"></a>

```c
#define NRF_FUN_GRTC_CLKOUT_32K 56U
```

相关声明：[NRF_FUN_GRTC_CLKOUT_32K](#a7c0fb8d0cd3a5557b3ac9ee7c7ebeffa)。

全局实时时钟（GRTC）的慢速时钟输出（Slow Clock Output）。

<a id="r_aa65eb5cf16a9f5963fb7feb0d6dfe4d7"></a>

```c
#define NRF_FUN_TDM_SCK_M 71U
```

相关声明：[NRF_FUN_TDM_SCK_M](#aa65eb5cf16a9f5963fb7feb0d6dfe4d7)。

主机模式（Master Mode）下的 TDM 串行时钟（SCK）。

<a id="r_a1c8af5882b6779bcd652f82a8c18670d"></a>

```c
#define NRF_FUN_TDM_SCK_S 72U
```

相关声明：[NRF_FUN_TDM_SCK_S](#a1c8af5882b6779bcd652f82a8c18670d)。

从机模式（Slave Mode）下的 TDM 串行时钟（SCK）。

<a id="r_a821a1d39a3d2272b75089b1aacb26d84"></a>

```c
#define NRF_FUN_TDM_FSYNC_M 73U
```

相关声明：[NRF_FUN_TDM_FSYNC_M](#a821a1d39a3d2272b75089b1aacb26d84)。

主机模式（Master Mode）下的 TDM 左右声道时钟（LRCK）。

<a id="r_a37860ffd62afc5eaf6822f6aeb5e1bbd"></a>

```c
#define NRF_FUN_TDM_FSYNC_S 74U
```

相关声明：[NRF_FUN_TDM_FSYNC_S](#a37860ffd62afc5eaf6822f6aeb5e1bbd)。

从机模式（Slave Mode）下的 TDM 左右声道时钟（LRCK）。

<a id="r_adb1ccccd147874be2ce018dcdb5a88d3"></a>

```c
#define NRF_FUN_TDM_SDIN 75U
```

相关声明：[NRF_FUN_TDM_SDIN](#adb1ccccd147874be2ce018dcdb5a88d3)。

TDM 串行数据输入（SDIN）。

<a id="r_af4c5c8cda1519cf93d4fb1e37d145606"></a>

```c
#define NRF_FUN_TDM_SDOUT 76U
```

相关声明：[NRF_FUN_TDM_SDOUT](#af4c5c8cda1519cf93d4fb1e37d145606)。

TDM 串行数据输出（SDOUT）。

<a id="r_a849b917fb8c2b9e748a3ec486ecf8bf3"></a>

```c
#define NRF_FUN_TDM_MCK 77U
```

相关声明：[NRF_FUN_TDM_MCK](#a849b917fb8c2b9e748a3ec486ecf8bf3)。

TDM 主时钟（MCK）。

<a id="r_abfb8add9dd9733dec7ec3fd4778bedef"></a>

```c
#define NRF_FUN_SPIM_CSN 78U
```

相关声明：[NRF_FUN_SPIM_CSN](#abfb8add9dd9733dec7ec3fd4778bedef)。

SPI 主机（Master）低有效片选（CSN）。

<a id="r_a3a0f3b0767d50af33baa72aafea35bf4"></a>

```c
#define NRF_FUN_TPIU_CLOCK 79U
```

相关声明：[NRF_FUN_TPIU_CLOCK](#a3a0f3b0767d50af33baa72aafea35bf4)。

TPIU 时钟（CLOCK）。

<a id="r_af222affe067ff3831047317f6f235b90"></a>

```c
#define NRF_FUN_TPIU_DATA0 80U
```

相关声明：[NRF_FUN_TPIU_DATA0](#af222affe067ff3831047317f6f235b90)。

TPIU 数据0（DATA0）。

<a id="r_a43fb9667a4e056b0b191005d9f9bc076"></a>

```c
#define NRF_FUN_TPIU_DATA1 81U
```

相关声明：[NRF_FUN_TPIU_DATA1](#a43fb9667a4e056b0b191005d9f9bc076)。

TPIU 数据1（DATA1）。

<a id="r_a644de40a031de6278822c6353684d9ab"></a>

```c
#define NRF_FUN_TPIU_DATA2 82U
```

相关声明：[NRF_FUN_TPIU_DATA2](#a644de40a031de6278822c6353684d9ab)。

TPIU 数据2（DATA2）。

<a id="r_a485fe3f7c0da98e674a961e70873ed2f"></a>

```c
#define NRF_FUN_TPIU_DATA3 83U
```

相关声明：[NRF_FUN_TPIU_DATA3](#a485fe3f7c0da98e674a961e70873ed2f)。

TPIU 数据3（DATA3）。

<a id="define-members-2"></a>

### nRF引脚控制输出驱动（nRF pinctrl output drive.）

<a id="r_a9a9ec0027e98f277a8ad72edc9783ca8"></a>

```c
#define NRF_DRIVE_S0S1 0U
```

相关声明：[NRF_DRIVE_S0S1](#a9a9ec0027e98f277a8ad72edc9783ca8)。

逻辑 0 为标准驱动，逻辑 1 为标准驱动（Standard Drive）。

<a id="r_a76555393e7124f333e0ec19414c2a6d5"></a>

```c
#define NRF_DRIVE_H0S1 1U
```

相关声明：[NRF_DRIVE_H0S1](#a76555393e7124f333e0ec19414c2a6d5)。

逻辑 0 为高驱动（High Drive），逻辑 1 为标准驱动（Standard Drive）。

<a id="r_abc3f7122815fc04db4c4eede3cfd713c"></a>

```c
#define NRF_DRIVE_S0H1 2U
```

相关声明：[NRF_DRIVE_S0H1](#abc3f7122815fc04db4c4eede3cfd713c)。

逻辑 0 为标准驱动（Standard Drive），逻辑 1 为高驱动（High Drive）。

<a id="r_a7f65712ab98608dbcdf438a57b651f4b"></a>

```c
#define NRF_DRIVE_H0H1 3U
```

相关声明：[NRF_DRIVE_H0H1](#a7f65712ab98608dbcdf438a57b651f4b)。

逻辑 0 为高驱动，逻辑 1 为高驱动（High Drive）。

<a id="r_ac97de2448f9b56d04bfb07f57c86eee9"></a>

```c
#define NRF_DRIVE_D0S1 4U
```

相关声明：[NRF_DRIVE_D0S1](#ac97de2448f9b56d04bfb07f57c86eee9)。

逻辑 0 断开（Disconnect），逻辑 1 为标准驱动（Standard Drive）。

<a id="r_a74f65220ebf6c8633b7023191bed55e8"></a>

```c
#define NRF_DRIVE_D0H1 5U
```

相关声明：[NRF_DRIVE_D0H1](#a74f65220ebf6c8633b7023191bed55e8)。

逻辑 0 断开（Disconnect），逻辑 1 为高驱动（High Drive）。

<a id="r_aa12e26bef363bd9953791445bd2132d8"></a>

```c
#define NRF_DRIVE_S0D1 6U
```

相关声明：[NRF_DRIVE_S0D1](#aa12e26bef363bd9953791445bd2132d8)。

逻辑 0 为标准驱动（Standard Drive），逻辑 1 断开（Disconnect）。

<a id="r_ab83a7803e7f9155d31f9f3e4373de2c2"></a>

```c
#define NRF_DRIVE_H0D1 7U
```

相关声明：[NRF_DRIVE_H0D1](#ab83a7803e7f9155d31f9f3e4373de2c2)。

逻辑 0 为高驱动（High Drive），逻辑 1 断开（Disconnect）。

<a id="r_a164af8cb0a188d21664987deec25946d"></a>

```c
#define NRF_DRIVE_E0E1 8U
```

相关声明：[NRF_DRIVE_E0E1](#a164af8cb0a188d21664987deec25946d)。

逻辑 0 为超高驱动，逻辑 1 为超高驱动（Extra High Drive）。

<a id="define-members-3"></a>

### nRF引脚控制上下拉（nRF pinctrl pull-up/down.）

注意：这些值与 nrf_gpio_pin_pull_t 常量匹配。

<a id="r_ada4d270f356ec03b6686aeabdb71f860"></a>

```c
#define NRF_PULL_NONE 0U
```

相关声明：[NRF_PULL_NONE](#ada4d270f356ec03b6686aeabdb71f860)。

上拉禁用（Pull-up Disabled）。

<a id="r_aca067a8a69d212ccacd9482953fc2893"></a>

```c
#define NRF_PULL_DOWN 1U
```

相关声明：[NRF_PULL_DOWN](#aca067a8a69d212ccacd9482953fc2893)。

启用下拉（Pull-down）。

<a id="r_a60062185ecdd8b8552ae00398213c7f7"></a>

```c
#define NRF_PULL_UP 3U
```

相关声明：[NRF_PULL_UP](#a60062185ecdd8b8552ae00398213c7f7)。

启用上拉（Pull-up）。

<a id="define-members-4"></a>

### nRF引脚控制低功耗模式（nRF pinctrl low power mode.）

<a id="r_aab29e9a98303f1d57c249362a4b062b0"></a>

```c
#define NRF_LP_DISABLE 0U
```

相关声明：[NRF_LP_DISABLE](#aab29e9a98303f1d57c249362a4b062b0)。

`input`（输入）。

<a id="r_a965ede26fa596ef7dd3ca62e0e9626a0"></a>

```c
#define NRF_LP_ENABLE 1U
```

相关声明：[NRF_LP_ENABLE](#a965ede26fa596ef7dd3ca62e0e9626a0)。

`output`（输出）。

<a id="define-members-5"></a>

### nRF引脚控制的断开引脚表示辅助宏（nRF pinctrl helpers to indicate disconnected pins.）

<a id="r_a1354873c8f0bcb226fc4d5fabb06b837"></a>

```c
#define NRF_PIN_DISCONNECTED NRF_PIN_MSK
```

相关声明：[NRF_PIN_DISCONNECTED](#a1354873c8f0bcb226fc4d5fabb06b837)、[NRF_PIN_MSK](#a8f60ab83a5325691eb0d976ae1f70295)。

指示引脚已断开（Disconnected）。

## 9.2\_详细说明（Detailed Documentation）

<a id="af596f5bff44b420017fe9d0bb1260753"></a>

### `NRF_CLOCKPIN_ENABLE_MSK`

```c
#define NRF_CLOCKPIN_ENABLE_MSK 0x1U
```

clockpin 使能字段（Enable Field）的掩码。

<a id="a1ddd10f13ce7524c777f02a2d96ed727"></a>

### `NRF_CLOCKPIN_ENABLE_POS`

```c
#define NRF_CLOCKPIN_ENABLE_POS 17U
```

clockpin 使能字段（Enable Field）的位位置。

<a id="a74f65220ebf6c8633b7023191bed55e8"></a>

### `NRF_DRIVE_D0H1`

```c
#define NRF_DRIVE_D0H1 5U
```

逻辑 0 断开（Disconnect），逻辑 1 为高驱动（High Drive）。

<a id="ac97de2448f9b56d04bfb07f57c86eee9"></a>

### `NRF_DRIVE_D0S1`

```c
#define NRF_DRIVE_D0S1 4U
```

逻辑 0 断开（Disconnect），逻辑 1 为标准驱动（Standard Drive）。

<a id="a164af8cb0a188d21664987deec25946d"></a>

### `NRF_DRIVE_E0E1`

```c
#define NRF_DRIVE_E0E1 8U
```

逻辑 0 为超高驱动，逻辑 1 为超高驱动（Extra High Drive）。

<a id="ab83a7803e7f9155d31f9f3e4373de2c2"></a>

### `NRF_DRIVE_H0D1`

```c
#define NRF_DRIVE_H0D1 7U
```

逻辑 0 为高驱动（High Drive），逻辑 1 断开（Disconnect）。

<a id="a7f65712ab98608dbcdf438a57b651f4b"></a>

### `NRF_DRIVE_H0H1`

```c
#define NRF_DRIVE_H0H1 3U
```

逻辑 0 为高驱动，逻辑 1 为高驱动（High Drive）。

<a id="a76555393e7124f333e0ec19414c2a6d5"></a>

### `NRF_DRIVE_H0S1`

```c
#define NRF_DRIVE_H0S1 1U
```

逻辑 0 为高驱动（High Drive），逻辑 1 为标准驱动（Standard Drive）。

<a id="a86d4555acfb553f6bad1562743cf357c"></a>

### `NRF_DRIVE_MSK`

```c
#define NRF_DRIVE_MSK 0xFU
```

驱动配置字段（Drive Configuration Field）的掩码。

<a id="ae8b94074f18659a2767e0f7f1aa1c73f"></a>

### `NRF_DRIVE_POS`

```c
#define NRF_DRIVE_POS 11U
```

驱动配置字段（Drive Configuration Field）的位位置。

<a id="aa12e26bef363bd9953791445bd2132d8"></a>

### `NRF_DRIVE_S0D1`

```c
#define NRF_DRIVE_S0D1 6U
```

逻辑 0 为标准驱动（Standard Drive），逻辑 1 断开（Disconnect）。

<a id="abc3f7122815fc04db4c4eede3cfd713c"></a>

### `NRF_DRIVE_S0H1`

```c
#define NRF_DRIVE_S0H1 2U
```

逻辑 0 为标准驱动（Standard Drive），逻辑 1 为高驱动（High Drive）。

<a id="a9a9ec0027e98f277a8ad72edc9783ca8"></a>

### `NRF_DRIVE_S0S1`

```c
#define NRF_DRIVE_S0S1 0U
```

逻辑 0 为标准驱动，逻辑 1 为标准驱动（Standard Drive）。

<a id="a55a2841880cd17f8d8a6ff5fb67ec71b"></a>

### `NRF_FUN_CAN_RX`

```c
#define NRF_FUN_CAN_RX 47U
```

CAN 接收（RX）。

<a id="a34338fa4c8ab9e606bdc00d8cfe288ef"></a>

### `NRF_FUN_CAN_TX`

```c
#define NRF_FUN_CAN_TX 46U
```

CAN 发送（TX）。

<a id="a9e02aa751912dd3e3ad3964bd2e92b1b"></a>

### `NRF_FUN_EXMIF_CK`

```c
#define NRF_FUN_EXMIF_CK 35U
```

EXMIF 时钟（CK）。

<a id="a25571f907b7d808c6d757c2b273287d3"></a>

### `NRF_FUN_EXMIF_CS0`

```c
#define NRF_FUN_EXMIF_CS0 44U
```

EXMIF 片选0（CS0）。

<a id="aa80dee2db548ab0ba3de943046ff24af"></a>

### `NRF_FUN_EXMIF_CS1`

```c
#define NRF_FUN_EXMIF_CS1 45U
```

EXMIF 片选1（CS1）。

<a id="afe37cd483f85609e7f82044995c7245d"></a>

### `NRF_FUN_EXMIF_DQ0`

```c
#define NRF_FUN_EXMIF_DQ0 36U
```

EXMIF 数据0（DQ0）。

<a id="ab58883df980cf4e61b1d74a473a58563"></a>

### `NRF_FUN_EXMIF_DQ1`

```c
#define NRF_FUN_EXMIF_DQ1 37U
```

EXMIF 数据1（DQ1）。

<a id="ad358c9ec0f07e70cfc11313c4f09073c"></a>

### `NRF_FUN_EXMIF_DQ2`

```c
#define NRF_FUN_EXMIF_DQ2 38U
```

EXMIF 数据2（DQ2）。

<a id="ac7ef6d6a949d228bdaf5635ae5182262"></a>

### `NRF_FUN_EXMIF_DQ3`

```c
#define NRF_FUN_EXMIF_DQ3 39U
```

EXMIF 数据3（DQ3）。

<a id="ab74f922a6687ddc1fce33b8f508064b7"></a>

### `NRF_FUN_EXMIF_DQ4`

```c
#define NRF_FUN_EXMIF_DQ4 40U
```

EXMIF 数据4（DQ4）。

<a id="a144b60ce024fadb107e19de376f2077c"></a>

### `NRF_FUN_EXMIF_DQ5`

```c
#define NRF_FUN_EXMIF_DQ5 41U
```

EXMIF 数据5（DQ5）。

<a id="a8eb7a3680c93054ed76d1d6603ee9425"></a>

### `NRF_FUN_EXMIF_DQ6`

```c
#define NRF_FUN_EXMIF_DQ6 42U
```

EXMIF 数据6（DQ6）。

<a id="a8cc2db3d1d971145411645135a29bf18"></a>

### `NRF_FUN_EXMIF_DQ7`

```c
#define NRF_FUN_EXMIF_DQ7 43U
```

EXMIF 数据7（DQ7）。

<a id="ad95c35e659797da017ae8bfd9f436968"></a>

### `NRF_FUN_EXMIF_RWDS`

```c
#define NRF_FUN_EXMIF_RWDS 50U
```

EXMIF 读写数据选通（RWDS）。

<a id="a7c0fb8d0cd3a5557b3ac9ee7c7ebeffa"></a>

### `NRF_FUN_GRTC_CLKOUT_32K`

```c
#define NRF_FUN_GRTC_CLKOUT_32K 56U
```

全局实时时钟（GRTC）的慢速时钟输出（Slow Clock Output）。

<a id="a06ece4c8604d693297d063bbc236c084"></a>

### `NRF_FUN_GRTC_CLKOUT_FAST`

```c
#define NRF_FUN_GRTC_CLKOUT_FAST 55U
```

全局实时时钟（GRTC）的快速时钟输出（Fast Clock Output）。

<a id="a8aeef372eba5608f6fa06c3e592bfe69"></a>

### `NRF_FUN_I2S_LRCK_M`

```c
#define NRF_FUN_I2S_LRCK_M 15U
```

主机模式（Master Mode）下的 I2S 左右声道时钟（LRCK）。

<a id="aacf6b96aad472ee6423552c80936c375"></a>

### `NRF_FUN_I2S_LRCK_S`

```c
#define NRF_FUN_I2S_LRCK_S 16U
```

从机模式（Slave Mode）下的 I2S 左右声道时钟（LRCK）。

<a id="a6de3f8d978d2aa864c12410ff3a78741"></a>

### `NRF_FUN_I2S_MCK`

```c
#define NRF_FUN_I2S_MCK 19U
```

I2S 主时钟（MCK）。

<a id="aae874d5eb9da322f9766c9546c565db2"></a>

### `NRF_FUN_I2S_SCK_M`

```c
#define NRF_FUN_I2S_SCK_M 13U
```

主机模式（Master Mode）下的 I2S 串行时钟（SCK）。

<a id="aa791b4bf51162aff1f6cfbc374af826b"></a>

### `NRF_FUN_I2S_SCK_S`

```c
#define NRF_FUN_I2S_SCK_S 14U
```

从机模式（Slave Mode）下的 I2S 串行时钟（SCK）。

<a id="ad943106dbd772562b2cca1d063c10456"></a>

### `NRF_FUN_I2S_SDIN`

```c
#define NRF_FUN_I2S_SDIN 17U
```

I2S 串行数据输入（SDIN）。

<a id="af2966d1e579895b18331480c42145f2f"></a>

### `NRF_FUN_I2S_SDOUT`

```c
#define NRF_FUN_I2S_SDOUT 18U
```

I2S 串行数据输出（SDOUT）。

<a id="ae3f5b1848b0c00547eff520f22ede922"></a>

### `NRF_FUN_MSK`

```c
#define NRF_FUN_MSK 0xFFU
```

功能字段（Function Field）的掩码。

<a id="a3d70a426c4c0deac34eb9f36bd0df63e"></a>

### `NRF_FUN_MSPI_CSN`

```c
#define NRF_FUN_MSPI_CSN NRF_FUN_QSPI_CSN
```

MSPI 低有效片选（CSN）。

<a id="a076c99fe48544f8c9e98927b5e10fb93"></a>

### `NRF_FUN_MSPI_IO0`

```c
#define NRF_FUN_MSPI_IO0 NRF_FUN_QSPI_IO0
```

MSPI 输入输出0（IO0）。

<a id="a1d57b9cdd49669e67f86307e4b51d700"></a>

### `NRF_FUN_MSPI_IO1`

```c
#define NRF_FUN_MSPI_IO1 NRF_FUN_QSPI_IO1
```

MSPI 输入输出1（IO1）。

<a id="ad18416245f40aee50fd970c7b1a31ace"></a>

### `NRF_FUN_MSPI_IO2`

```c
#define NRF_FUN_MSPI_IO2 NRF_FUN_QSPI_IO2
```

MSPI 输入输出2（IO2）。

<a id="a4d5395d0e61119185d3c71228045a333"></a>

### `NRF_FUN_MSPI_IO3`

```c
#define NRF_FUN_MSPI_IO3 NRF_FUN_QSPI_IO3
```

MSPI 输入输出3（IO3）。

<a id="a77453afa40269edfcdc2039a5c2a98e2"></a>

### `NRF_FUN_MSPI_SCK`

```c
#define NRF_FUN_MSPI_SCK NRF_FUN_QSPI_SCK
```

MSPI 串行时钟（SCK）。

<a id="a5ceee799b932f1b71366bda816cde19a"></a>

### `NRF_FUN_PDM_CLK`

```c
#define NRF_FUN_PDM_CLK 20U
```

PDM 时钟（CLK）。

<a id="af8f0c9a76b28fe19a5c4552386b6cd30"></a>

### `NRF_FUN_PDM_DIN`

```c
#define NRF_FUN_PDM_DIN 21U
```

PDM 数据输入（DIN）。

<a id="a10272aaefd0f103c15ae28ce8ef76987"></a>

### `NRF_FUN_POS`

```c
#define NRF_FUN_POS 24U
```

功能字段（Function Field）的位位置。

<a id="a9cf56eb616791c1bf79a15de6e11e270"></a>

### `NRF_FUN_PWM_OUT0`

```c
#define NRF_FUN_PWM_OUT0 22U
```

PWM 输出0（OUT0）。

<a id="a9668fd12e95380431659e5edaa62cf65"></a>

### `NRF_FUN_PWM_OUT1`

```c
#define NRF_FUN_PWM_OUT1 23U
```

PWM 输出1（OUT1）。

<a id="a4d9b8e2aba25457f1e688b71a8bcf235"></a>

### `NRF_FUN_PWM_OUT2`

```c
#define NRF_FUN_PWM_OUT2 24U
```

PWM 输出2（OUT2）。

<a id="a79e863ca96b4e14c6eb0367b7b50bd32"></a>

### `NRF_FUN_PWM_OUT3`

```c
#define NRF_FUN_PWM_OUT3 25U
```

PWM 输出3（OUT3）。

<a id="af07b0671c04b3318ad4f6e81f9b02f9b"></a>

### `NRF_FUN_QDEC_A`

```c
#define NRF_FUN_QDEC_A 26U
```

QDEC A 相（A）。

<a id="a3da455a7ac5e260ff25e867212b4b026"></a>

### `NRF_FUN_QDEC_B`

```c
#define NRF_FUN_QDEC_B 27U
```

QDEC B 相（B）。

<a id="a0b4431b76b7c264167fe48294cb5eb3d"></a>

### `NRF_FUN_QDEC_LED`

```c
#define NRF_FUN_QDEC_LED 28U
```

QDEC LED 信号（LED）。

<a id="a2ec92b450cc6f75121879950a7a2f750"></a>

### `NRF_FUN_QSPI_CSN`

```c
#define NRF_FUN_QSPI_CSN 30U
```

QSPI 低有效片选（CSN）。

<a id="a97a03ba41e0a1bafe6d44868baf62b21"></a>

### `NRF_FUN_QSPI_IO0`

```c
#define NRF_FUN_QSPI_IO0 31U
```

QSPI 输入输出0（IO0）。

<a id="a4a87c54c51d9ab5e602a62f9ec70e98e"></a>

### `NRF_FUN_QSPI_IO1`

```c
#define NRF_FUN_QSPI_IO1 32U
```

QSPI 输入输出1（IO1）。

<a id="a0bd9c69689a0ec5c88eb4d50ff1c73dd"></a>

### `NRF_FUN_QSPI_IO2`

```c
#define NRF_FUN_QSPI_IO2 33U
```

QSPI 输入输出2（IO2）。

<a id="aaf2c957da80884f0a8d442da64da8b92"></a>

### `NRF_FUN_QSPI_IO3`

```c
#define NRF_FUN_QSPI_IO3 34U
```

QSPI 输入输出3（IO3）。

<a id="a8504018d0dddd49c009ee8db7f6aa559"></a>

### `NRF_FUN_QSPI_SCK`

```c
#define NRF_FUN_QSPI_SCK 29U
```

QSPI 串行时钟（SCK）。

<a id="abfb8add9dd9733dec7ec3fd4778bedef"></a>

### `NRF_FUN_SPIM_CSN`

```c
#define NRF_FUN_SPIM_CSN 78U
```

SPI 主机（Master）低有效片选（CSN）。

<a id="afca36f99d1c1a9e17e4949f18206490a"></a>

### `NRF_FUN_SPIM_MISO`

```c
#define NRF_FUN_SPIM_MISO 6U
```

SPI 主机（Master）主入从出（MISO）。

<a id="a2e96ea48e6a9e707b76b846536a687cb"></a>

### `NRF_FUN_SPIM_MOSI`

```c
#define NRF_FUN_SPIM_MOSI 5U
```

SPI 主机（Master）主出从入（MOSI）。

<a id="a2594557c5e765d65ea7627c5c49e07d6"></a>

### `NRF_FUN_SPIM_SCK`

```c
#define NRF_FUN_SPIM_SCK 4U
```

SPI 主机（Master）串行时钟（SCK）。

<a id="a6591844a0ce9f0297f917abb2f87c259"></a>

### `NRF_FUN_SPIS_CSN`

```c
#define NRF_FUN_SPIS_CSN 10U
```

SPI 从机（Slave）低有效片选（CSN）。

<a id="aa480a4b96df9c4521d744de7d9a72e1f"></a>

### `NRF_FUN_SPIS_MISO`

```c
#define NRF_FUN_SPIS_MISO 9U
```

SPI 从机（Slave）主入从出（MISO）。

<a id="a016ffb10db008be19f494e7098096109"></a>

### `NRF_FUN_SPIS_MOSI`

```c
#define NRF_FUN_SPIS_MOSI 8U
```

SPI 从机（Slave）主出从入（MOSI）。

<a id="a9906fedc9c9667be7a84c66443f01772"></a>

### `NRF_FUN_SPIS_SCK`

```c
#define NRF_FUN_SPIS_SCK 7U
```

SPI 从机（Slave）串行时钟（SCK）。

<a id="a821a1d39a3d2272b75089b1aacb26d84"></a>

### `NRF_FUN_TDM_FSYNC_M`

```c
#define NRF_FUN_TDM_FSYNC_M 73U
```

主机模式（Master Mode）下的 TDM 左右声道时钟（LRCK）。

<a id="a37860ffd62afc5eaf6822f6aeb5e1bbd"></a>

### `NRF_FUN_TDM_FSYNC_S`

```c
#define NRF_FUN_TDM_FSYNC_S 74U
```

从机模式（Slave Mode）下的 TDM 左右声道时钟（LRCK）。

<a id="a849b917fb8c2b9e748a3ec486ecf8bf3"></a>

### `NRF_FUN_TDM_MCK`

```c
#define NRF_FUN_TDM_MCK 77U
```

TDM 主时钟（MCK）。

<a id="aa65eb5cf16a9f5963fb7feb0d6dfe4d7"></a>

### `NRF_FUN_TDM_SCK_M`

```c
#define NRF_FUN_TDM_SCK_M 71U
```

主机模式（Master Mode）下的 TDM 串行时钟（SCK）。

<a id="a1c8af5882b6779bcd652f82a8c18670d"></a>

### `NRF_FUN_TDM_SCK_S`

```c
#define NRF_FUN_TDM_SCK_S 72U
```

从机模式（Slave Mode）下的 TDM 串行时钟（SCK）。

<a id="adb1ccccd147874be2ce018dcdb5a88d3"></a>

### `NRF_FUN_TDM_SDIN`

```c
#define NRF_FUN_TDM_SDIN 75U
```

TDM 串行数据输入（SDIN）。

<a id="af4c5c8cda1519cf93d4fb1e37d145606"></a>

### `NRF_FUN_TDM_SDOUT`

```c
#define NRF_FUN_TDM_SDOUT 76U
```

TDM 串行数据输出（SDOUT）。

<a id="a3a0f3b0767d50af33baa72aafea35bf4"></a>

### `NRF_FUN_TPIU_CLOCK`

```c
#define NRF_FUN_TPIU_CLOCK 79U
```

TPIU 时钟（CLOCK）。

<a id="af222affe067ff3831047317f6f235b90"></a>

### `NRF_FUN_TPIU_DATA0`

```c
#define NRF_FUN_TPIU_DATA0 80U
```

TPIU 数据0（DATA0）。

<a id="a43fb9667a4e056b0b191005d9f9bc076"></a>

### `NRF_FUN_TPIU_DATA1`

```c
#define NRF_FUN_TPIU_DATA1 81U
```

TPIU 数据1（DATA1）。

<a id="a644de40a031de6278822c6353684d9ab"></a>

### `NRF_FUN_TPIU_DATA2`

```c
#define NRF_FUN_TPIU_DATA2 82U
```

TPIU 数据2（DATA2）。

<a id="a485fe3f7c0da98e674a961e70873ed2f"></a>

### `NRF_FUN_TPIU_DATA3`

```c
#define NRF_FUN_TPIU_DATA3 83U
```

TPIU 数据3（DATA3）。

<a id="aa26e18840b9cc780f35a1c237f24f8f8"></a>

### `NRF_FUN_TWIM_SCL`

```c
#define NRF_FUN_TWIM_SCL 11U
```

TWI 主机（Master）时钟线（SCL）。

<a id="a7f0dcd38287a5e8c2e55145e43a57628"></a>

### `NRF_FUN_TWIM_SDA`

```c
#define NRF_FUN_TWIM_SDA 12U
```

TWI 主机（Master）数据线（SDA）。

<a id="a991d00b1a2fafff3f5f1a107d1c92b28"></a>

### `NRF_FUN_TWIS_SCL`

```c
#define NRF_FUN_TWIS_SCL 48U
```

TWIS 时钟线（SCL）。

<a id="ae680ea89fa8da33f4bee9f3d30ea3c66"></a>

### `NRF_FUN_TWIS_SDA`

```c
#define NRF_FUN_TWIS_SDA 49U
```

TWIS 数据线（SDA）。

<a id="a595b5f913921466ec87c58657709c800"></a>

### `NRF_FUN_UART_CTS`

```c
#define NRF_FUN_UART_CTS 3U
```

UART 清除发送（CTS）。

<a id="aa2ea1399ee3dff5019adf462b9cb09b8"></a>

### `NRF_FUN_UART_RTS`

```c
#define NRF_FUN_UART_RTS 2U
```

UART 请求发送（RTS）。

<a id="ad7865c58ddd2d7686482fa2f92a330f8"></a>

### `NRF_FUN_UART_RX`

```c
#define NRF_FUN_UART_RX 1U
```

UART 接收（RX）。

<a id="a9550ec0625d3e702c41d79cdf633bf9b"></a>

### `NRF_FUN_UART_TX`

```c
#define NRF_FUN_UART_TX 0U
```

UART 发送（TX）。

<a id="a1211c8c57f411a7676023c61cc986095"></a>

### `NRF_GPD_FAST_ACTIVE1_MSK`

```c
#define NRF_GPD_FAST_ACTIVE1_MSK 0x1U
```

GPD FAST ACTIVE1 的掩码（Mask）。

<a id="a9203c68fb293d5eec889a8729b5f52b3"></a>

### `NRF_GPD_FAST_ACTIVE1_POS`

```c
#define NRF_GPD_FAST_ACTIVE1_POS 18U
```

GPD FAST ACTIVE1 的位位置（Position）。

<a id="a1a5cca24fa65f0ea64e8927e9d12ff43"></a>

### `NRF_INVERT_MSK`

```c
#define NRF_INVERT_MSK 0x1U
```

反相字段（Invert Field）的掩码。

<a id="aa13cd70c54db20407bfaef944ea10329"></a>

### `NRF_INVERT_POS`

```c
#define NRF_INVERT_POS 16U
```

反相字段（Invert Field）的位位置。

<a id="aab29e9a98303f1d57c249362a4b062b0"></a>

### `NRF_LP_DISABLE`

```c
#define NRF_LP_DISABLE 0U
```

`input`（输入）。

<a id="a965ede26fa596ef7dd3ca62e0e9626a0"></a>

### `NRF_LP_ENABLE`

```c
#define NRF_LP_ENABLE 1U
```

`output`（输出）。

<a id="a67b7d47eed25086ebbe5db508c85ff7b"></a>

### `NRF_LP_MSK`

```c
#define NRF_LP_MSK 0x1U
```

低功耗字段（Low Power Field）的掩码。

<a id="a97dce1e8b63e4054f23c1daa0ddd6327"></a>

### `NRF_LP_POS`

```c
#define NRF_LP_POS 15U
```

低功耗字段（Low Power Field）的位位置。

<a id="a1354873c8f0bcb226fc4d5fabb06b837"></a>

### `NRF_PIN_DISCONNECTED`

```c
#define NRF_PIN_DISCONNECTED NRF_PIN_MSK
```

指示引脚已断开（Disconnected）。

<a id="a8f60ab83a5325691eb0d976ae1f70295"></a>

### `NRF_PIN_MSK`

```c
#define NRF_PIN_MSK 0x1FFU
```

引脚字段（Pin Field）的掩码。

<a id="aa057ad8de2dea12959f51a293a929367"></a>

### `NRF_PIN_POS`

```c
#define NRF_PIN_POS 0U
```

引脚字段（Pin Field）的位位置。

<a id="a43d0a0ad6e574456a2b69ab5354ccef4"></a>

### `NRF_PSEL`

```c
#define NRF_PSEL ( fun, port, pin )
```

展开值（Value）：

```c
((((((port) * 32U) + (pin)) & NRF_PIN_MSK) << NRF_PIN_POS) |                   \
 ((NRF_FUN_ ## fun & NRF_FUN_MSK) << NRF_FUN_POS))
```

构造 nRF psels 属性条目（Property Entry）的工具宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fun` | 引脚功能配置（Pin Function Configuration），参见 NRF_FUN_{name} 宏。 |
| `port` | 端口（Port）：0 或 15。

> 译注：原文写为“0 or 15”，此处按原文保留。 |
| `pin` | 引脚（Pin）：0～31。 |

<a id="a2e414bdc5912c0e0abc349d5362520bd"></a>

### `NRF_PSEL_DISCONNECTED`

```c
#define NRF_PSEL_DISCONNECTED ( fun)
```

展开值（Value）：

```c
(NRF_PIN_DISCONNECTED |                                                        \
 ((NRF_FUN_ ## fun & NRF_FUN_MSK) << NRF_FUN_POS))
```

引脚断开（Disconnected）时，构造 nRF psels 属性条目的工具宏。

当 Zephyr 之前运行的代码，例如引导加载程序（Bootloader），配置了一些随后需要断开的引脚时，此功能可能有用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fun` | 引脚功能配置（Pin Function Configuration），参见 NRF_FUN_{name} 宏。 |

<a id="aca067a8a69d212ccacd9482953fc2893"></a>

### `NRF_PULL_DOWN`

```c
#define NRF_PULL_DOWN 1U
```

启用下拉（Pull-down）。

<a id="a3900fd72d44feeefef9aa73c909a2396"></a>

### `NRF_PULL_MSK`

```c
#define NRF_PULL_MSK 0x3U
```

上下拉配置字段（Pull Configuration Field）的掩码。

<a id="ada4d270f356ec03b6686aeabdb71f860"></a>

### `NRF_PULL_NONE`

```c
#define NRF_PULL_NONE 0U
```

上拉禁用（Pull-up Disabled）。

<a id="a0fac117bc7a2f45638ce462527cb8daa"></a>

### `NRF_PULL_POS`

```c
#define NRF_PULL_POS 9U
```

上下拉配置字段（Pull Configuration Field）的位位置。

<a id="a60062185ecdd8b8552ae00398213c7f7"></a>

### `NRF_PULL_UP`

```c
#define NRF_PULL_UP 3U
```

启用上拉（Pull-up）。


## 9.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_supplement_reference/P132_nrf-pinctrl.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="anrf-pinctrl_8h_html_a10272aaefd0f103c15ae28ce8ef76987"></a>
<a id="anrf-pinctrl_8h_html_a8f60ab83a5325691eb0d976ae1f70295"></a>
<a id="anrf-pinctrl_8h_html_aa057ad8de2dea12959f51a293a929367"></a>
<a id="anrf-pinctrl_8h_html_ae3f5b1848b0c00547eff520f22ede922"></a>
<a id="anrf-pinctrl_8h_html_a1354873c8f0bcb226fc4d5fabb06b837"></a>

---

[上一章](P008_zephyr__net__mii.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P010_zephyr__dt-bindings__clock-monitor__nxp-freqme.h_文件参考.md)
