---
id: learning.zephyr-docs.api-file-usb-network-reference.page-3
title: zephyr__dt-bindings__clock__amebadplus_clock.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/amebadplus__clock_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_zephyr\_\_dt-bindings\_\_clock\_\_amebadplus\_clock.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/amebadplus__clock_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Realtek Amebadplus时钟的设备树绑定（Devicetree Bindings）。

查看此文件的源码。

<a id="details"></a>

Realtek Amebadplus时钟的设备树绑定（Devicetree Bindings）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 常开域时钟（AON Domain Clocks）

<a id="r_addc3bc2c9372ac83316911fc48d132b4"></a>

```c
#define AMEBA_ATIM_CLK 1
```

相关声明：[AMEBA_ATIM_CLK](#addc3bc2c9372ac83316911fc48d132b4)。

AON 域（Domain）中的 ATIM 时钟（Clock）。

<a id="r_a9f089feea64d395b53ec91451346889d"></a>

```c
#define AMEBA_RTC_CLK 2
```

相关声明：[AMEBA_RTC_CLK](#a9f089feea64d395b53ec91451346889d)。

AON 域（Domain）中的 RTC 时钟（Clock）。

<a id="define-members-1"></a>

### SYSON 域时钟（SYSON Domain Clocks）

<a id="r_a523f7ac5827b17a56f7940c18481abb8"></a>

```c
#define AMEBA_PWM0_CLK 3
```

相关声明：[AMEBA_PWM0_CLK](#a523f7ac5827b17a56f7940c18481abb8)。

SYSON 域（Domain）中的 PWM0 时钟（Clock）。

<a id="r_a580af7f35de2aa6faaf2210784887baf"></a>

```c
#define AMEBA_PWM1_CLK 4
```

相关声明：[AMEBA_PWM1_CLK](#a580af7f35de2aa6faaf2210784887baf)。

SYSON 域（Domain）中的 PWM1 时钟（Clock）。

<a id="r_a7792fde84e7acfbeb941ebb4fa5f696e"></a>

```c
#define AMEBA_HTIM0_CLK 5
```

相关声明：[AMEBA_HTIM0_CLK](#a7792fde84e7acfbeb941ebb4fa5f696e)。

SYSON 域（Domain）中的 HTIM0 时钟（Clock）。

<a id="r_a886720ba1e95f0b4a4754eb315b2a270"></a>

```c
#define AMEBA_HTIM1_CLK 6
```

相关声明：[AMEBA_HTIM1_CLK](#a886720ba1e95f0b4a4754eb315b2a270)。

SYSON 域（Domain）中的 HTIM1 时钟（Clock）。

<a id="r_a8f7e7a6493ce0d8db53a5446c588f3d4"></a>

```c
#define AMEBA_LEDC_CLK 7
```

相关声明：[AMEBA_LEDC_CLK](#a8f7e7a6493ce0d8db53a5446c588f3d4)。

SYSON 域（Domain）中的 LEDC 时钟（Clock）。

<a id="r_a36ebf3e1fd6ac0092aab3589d14d20b3"></a>

```c
#define AMEBA_UART0_CLK 8
```

相关声明：[AMEBA_UART0_CLK](#a36ebf3e1fd6ac0092aab3589d14d20b3)。

SYSON 域（Domain）中的 UART0 时钟（Clock）。

<a id="r_a8df46e7a94c9ccd5174aab94c9531e7e"></a>

```c
#define AMEBA_UART1_CLK 9
```

相关声明：[AMEBA_UART1_CLK](#a8df46e7a94c9ccd5174aab94c9531e7e)。

SYSON 域（Domain）中的 UART1 时钟（Clock）。

<a id="r_a32eaddcc095242263b580d0b736eef53"></a>

```c
#define AMEBA_UART2_CLK 10
```

相关声明：[AMEBA_UART2_CLK](#a32eaddcc095242263b580d0b736eef53)。

SYSON 域（Domain）中的 UART2 时钟（Clock）。

<a id="r_a996962b9c7b1dd32421226bde07184c1"></a>

```c
#define AMEBA_LOGUART_CLK 11
```

相关声明：[AMEBA_LOGUART_CLK](#a996962b9c7b1dd32421226bde07184c1)。

SYSON 域（Domain）中的 LOGUART 时钟（Clock）。

<a id="r_aef91aa4146dafae99bef8ef9478f8a15"></a>

```c
#define AMEBA_DTIM_CLK 12
```

相关声明：[AMEBA_DTIM_CLK](#aef91aa4146dafae99bef8ef9478f8a15)。

SYSON 域（Domain）中的 DTIM 时钟（Clock）。

<a id="r_a790dbb7ace4f63eb2a68de13c4dac8ef"></a>

```c
#define AMEBA_ADC_CLK 13
```

相关声明：[AMEBA_ADC_CLK](#a790dbb7ace4f63eb2a68de13c4dac8ef)。

SYSON 域（Domain）中的 ADC 时钟（Clock）。

<a id="r_a060a938a705823c18de0ce9133c0a99d"></a>

```c
#define AMEBA_GPIO_CLK 14
```

相关声明：[AMEBA_GPIO_CLK](#a060a938a705823c18de0ce9133c0a99d)。

SYSON 域（Domain）中的 GPIO 时钟（Clock）。

<a id="r_ab3149be5245573521f4bb7e551e625e7"></a>

```c
#define AMEBA_LTIM0_CLK 15
```

相关声明：[AMEBA_LTIM0_CLK](#ab3149be5245573521f4bb7e551e625e7)。

SYSON 域（Domain）中的 LTIM0 时钟（Clock）。

<a id="r_a776ea52d9a1f082f7037bd2b01a0d4bb"></a>

```c
#define AMEBA_LTIM1_CLK 16
```

相关声明：[AMEBA_LTIM1_CLK](#a776ea52d9a1f082f7037bd2b01a0d4bb)。

SYSON 域（Domain）中的 LTIM1 时钟（Clock）。

<a id="r_a832779b2dc473e221ba4a4b813807dbc"></a>

```c
#define AMEBA_LTIM2_CLK 17
```

相关声明：[AMEBA_LTIM2_CLK](#a832779b2dc473e221ba4a4b813807dbc)。

SYSON 域（Domain）中的 LTIM2 时钟（Clock）。

<a id="r_a371d8e766d052283c390868989cc9283"></a>

```c
#define AMEBA_LTIM3_CLK 18
```

相关声明：[AMEBA_LTIM3_CLK](#a371d8e766d052283c390868989cc9283)。

SYSON 域（Domain）中的 LTIM3 时钟（Clock）。

<a id="r_a9c2241936d9f61aa68f61f1d1e270870"></a>

```c
#define AMEBA_LTIM4_CLK 19
```

相关声明：[AMEBA_LTIM4_CLK](#a9c2241936d9f61aa68f61f1d1e270870)。

SYSON 域（Domain）中的 LTIM4 时钟（Clock）。

<a id="r_ab5b0d934d7a784ccce21ad84d6559bfa"></a>

```c
#define AMEBA_LTIM5_CLK 20
```

相关声明：[AMEBA_LTIM5_CLK](#ab5b0d934d7a784ccce21ad84d6559bfa)。

SYSON 域（Domain）中的 LTIM5 时钟（Clock）。

<a id="r_a6e18da23aa07580b3cd81c6a20d2dce2"></a>

```c
#define AMEBA_LTIM6_CLK 21
```

相关声明：[AMEBA_LTIM6_CLK](#a6e18da23aa07580b3cd81c6a20d2dce2)。

SYSON 域（Domain）中的 LTIM6 时钟（Clock）。

<a id="r_a6c0d56f6b7abc587971020ec06d12a77"></a>

```c
#define AMEBA_LTIM7_CLK 22
```

相关声明：[AMEBA_LTIM7_CLK](#a6c0d56f6b7abc587971020ec06d12a77)。

SYSON 域（Domain）中的 LTIM7 时钟（Clock）。

<a id="r_a24b192e5fb6291e88af8274a52c7af18"></a>

```c
#define AMEBA_PTIM0_CLK 23
```

相关声明：[AMEBA_PTIM0_CLK](#a24b192e5fb6291e88af8274a52c7af18)。

SYSON 域（Domain）中的 PTIM0 时钟（Clock）。

<a id="r_a4ac4664b0e6f6af828ebf6d719a91b28"></a>

```c
#define AMEBA_PTIM1_CLK 24
```

相关声明：[AMEBA_PTIM1_CLK](#a4ac4664b0e6f6af828ebf6d719a91b28)。

SYSON 域（Domain）中的 PTIM1 时钟（Clock）。

<a id="r_ad2318a02565100eee1cb633744db9dd0"></a>

```c
#define AMEBA_KSCAN_CLK 25
```

相关声明：[AMEBA_KSCAN_CLK](#ad2318a02565100eee1cb633744db9dd0)。

SYSON 域（Domain）中的 KSCAN 时钟（Clock）。

<a id="define-members-2"></a>

### SoC 域时钟（SoC Domain Clocks）

<a id="r_a3bb4d8911bd65c48f5c958f4bcd88a40"></a>

```c
#define AMEBA_DMAC_CLK 26
```

相关声明：[AMEBA_DMAC_CLK](#a3bb4d8911bd65c48f5c958f4bcd88a40)。

SoC 域（Domain）中的 DMAC 时钟（Clock）。

<a id="r_aa18a82f87588818e5b7e37a851ccd423"></a>

```c
#define AMEBA_SDIO_CLK 27
```

相关声明：[AMEBA_SDIO_CLK](#aa18a82f87588818e5b7e37a851ccd423)。

SoC 域（Domain）中的 SDIO 时钟（Clock）。

<a id="r_a44689e534b5693fe964e45f04ec3af3a"></a>

```c
#define AMEBA_SPI0_CLK 28
```

相关声明：[AMEBA_SPI0_CLK](#a44689e534b5693fe964e45f04ec3af3a)。

SoC 域（Domain）中的 SPI0 时钟（Clock）。

<a id="r_a1997336af677a35e15d1402aed065ee6"></a>

```c
#define AMEBA_SPI1_CLK 29
```

相关声明：[AMEBA_SPI1_CLK](#a1997336af677a35e15d1402aed065ee6)。

SoC 域（Domain）中的 SPI1 时钟（Clock）。

<a id="r_a9811b8e45cdc63a1dee22ff4ecce6fb5"></a>

```c
#define AMEBA_USB_CLK 30
```

相关声明：[AMEBA_USB_CLK](#a9811b8e45cdc63a1dee22ff4ecce6fb5)。

SoC 域（Domain）中的 USB 时钟（Clock）。

<a id="r_ad32629d31a567d5d134e421cd527253a"></a>

```c
#define AMEBA_FLASH_CLK 31
```

相关声明：[AMEBA_FLASH_CLK](#ad32629d31a567d5d134e421cd527253a)。

SoC 域（Domain）中的闪存时钟（Flash Clock）。

<a id="r_a2d6f84861d9ceff804149347a06e796b"></a>

```c
#define AMEBA_PSRAM_CLK 32
```

相关声明：[AMEBA_PSRAM_CLK](#a2d6f84861d9ceff804149347a06e796b)。

SoC 域（Domain）中的 PSRAM 时钟（Clock）。

<a id="r_ae123e8df6cb6c584da9eb41d2dec9c4e"></a>

```c
#define AMEBA_SPORT0_CLK 33
```

相关声明：[AMEBA_SPORT0_CLK](#ae123e8df6cb6c584da9eb41d2dec9c4e)。

SoC 域（Domain）中的 SPORT0 时钟（Clock）。

<a id="r_a4196280bae37b3405b303b713107a50a"></a>

```c
#define AMEBA_SPORT1_CLK 34
```

相关声明：[AMEBA_SPORT1_CLK](#a4196280bae37b3405b303b713107a50a)。

SoC 域（Domain）中的 SPORT1 时钟（Clock）。

<a id="r_adfb9684f04c1a52a9ba0ed6c9545d045"></a>

```c
#define AMEBA_AC_CLK 35
```

相关声明：[AMEBA_AC_CLK](#adfb9684f04c1a52a9ba0ed6c9545d045)。

SoC 域（Domain）中的 AC 时钟（Clock）。

<a id="r_aed01c7bc1553e9902a27bf7318245d99"></a>

```c
#define AMEBA_IRDA_CLK 36
```

相关声明：[AMEBA_IRDA_CLK](#aed01c7bc1553e9902a27bf7318245d99)。

SoC 域（Domain）中的 IRDA 时钟（Clock）。

<a id="r_ac293b0216f849f4bffd50253b0df9fd7"></a>

```c
#define AMEBA_I2C0_CLK 37
```

相关声明：[AMEBA_I2C0_CLK](#ac293b0216f849f4bffd50253b0df9fd7)。

SoC 域（Domain）中的 I2C0 时钟（Clock）。

<a id="r_ae8a2efe5f489463a64db00003edf8c58"></a>

```c
#define AMEBA_I2C1_CLK 38
```

相关声明：[AMEBA_I2C1_CLK](#ae8a2efe5f489463a64db00003edf8c58)。

SoC 域（Domain）中的 I2C1 时钟（Clock）。

<a id="r_ae7e4292f7a91fb471d32b0fd36b8384f"></a>

```c
#define AMEBA_TRNG_CLK 39
```

相关声明：[AMEBA_TRNG_CLK](#ae7e4292f7a91fb471d32b0fd36b8384f)。

SoC 域（Domain）中的 TRNG 时钟（Clock）。

<a id="define-members-3"></a>

### 杂项时钟（Misc Clocks）

<a id="r_ad3f1e380b1e407166b21646cde8e145f"></a>

```c
#define AMEBA_BTON_CLK 40
```

相关声明：[AMEBA_BTON_CLK](#ad3f1e380b1e407166b21646cde8e145f)。

BTON 时钟（Clock）。

<a id="r_a13aff4f0d9cb48d2e58b0525b9f96853"></a>

```c
#define AMEBA_AES_CLK 42
```

相关声明：[AMEBA_AES_CLK](#a13aff4f0d9cb48d2e58b0525b9f96853)。

杂项域（Misc Domain）中的 AES 时钟（Clock）。

<a id="r_a9ce69f2fdf39f6eb6b2dfdebc6b35fae"></a>

```c
#define AMEBA_CLK_MAX 43 /* clk idx max */
```

相关声明：[AMEBA_CLK_MAX](#a9ce69f2fdf39f6eb6b2dfdebc6b35fae)、[max](../numeric_reference/P001_最小最大值与限幅宏参考.md#affe776513b24d84b39af8ab0930fef7f)。

最大时钟索引（Maximum Clock Index），比最后一个有效索引大 1。

<a id="define-members-4"></a>

### 外设时钟辅助宏（Peripheral Clock Helper Macros）

<a id="r_a5892f2668cc892817f59230643162ee4"></a>

```c
#define AMEBA_NUMERICAL_PERIPH(name, n)
```

相关声明：[AMEBA_NUMERICAL_PERIPH](#a5892f2668cc892817f59230643162ee4)。

为带数字后缀的外设定义时钟条目（Clock Entry）。

<a id="r_a47ccaa9d57758ebac1885d09d6067af1"></a>

```c
#define AMEBA_SINGLE_PERIPH(name)
```

相关声明：[AMEBA_SINGLE_PERIPH](#a47ccaa9d57758ebac1885d09d6067af1)。

为只有一个实例的外设定义时钟条目（Clock Entry）。

<a id="r_a89ef5e4da90cb6459240ea4f998c61c5"></a>

```c
#define AMEBA_LTIM_PERIPHS
```

相关声明：[AMEBA_LTIM_PERIPHS](#a89ef5e4da90cb6459240ea4f998c61c5)。

LTIM 时钟外设映射（Clock Peripheral Mapping）。

<a id="r_a497ef8d62b1db3ec4d9f8b27c0b1aa22"></a>

```c
#define AMEBA_PTIM_PERIPHS
```

相关声明：[AMEBA_PTIM_PERIPHS](#a497ef8d62b1db3ec4d9f8b27c0b1aa22)。

PTIM 时钟外设映射（Clock Peripheral Mapping）。

<a id="r_a9a0c99a81816161def16ba0f969c159d"></a>

```c
#define AMEBA_SPI_PERIPHS
```

相关声明：[AMEBA_SPI_PERIPHS](#a9a0c99a81816161def16ba0f969c159d)。

SPI 时钟外设映射（Clock Peripheral Mappings）。

<a id="r_a854f2eee8cff49b0c00a400e4295f7e5"></a>

```c
#define AMEBA_SPORT_PERIPHS
```

相关声明：[AMEBA_SPORT_PERIPHS](#a854f2eee8cff49b0c00a400e4295f7e5)。

SPORT 时钟外设映射（Clock Peripheral Mapping）。

<a id="r_ab55bb29f8a5c2a0fd1dba45d0c9f4910"></a>

```c
#define AMEBA_I2C_PERIPHS
```

相关声明：[AMEBA_I2C_PERIPHS](#ab55bb29f8a5c2a0fd1dba45d0c9f4910)。

I2C 时钟外设映射（Clock Peripheral Mappings）。

<a id="r_a7a3e89aeca0afde7c5c5350e75f289eb"></a>

```c
#define AMEBA_PWM_PERIPHS
```

相关声明：[AMEBA_PWM_PERIPHS](#a7a3e89aeca0afde7c5c5350e75f289eb)。

PWM 时钟外设映射（Clock Peripheral Mapping）。

<a id="r_a15bb72de50884608e12cd39e47f9cfb1"></a>

```c
#define AMEBA_HTIM_PERIPHS
```

相关声明：[AMEBA_HTIM_PERIPHS](#a15bb72de50884608e12cd39e47f9cfb1)。

HTIM 时钟外设映射（Clock Peripheral Mapping）。

<a id="r_a7b90187464653d7b1e83e0fd01c21e2f"></a>

```c
#define AMEBA_UART_PERIPHS
```

相关声明：[AMEBA_UART_PERIPHS](#a7b90187464653d7b1e83e0fd01c21e2f)。

UART 时钟外设映射（Clock Peripheral Mappings）。

<a id="r_a1020076bac0b7d227c73d4482c95ebd0"></a>

```c
#define AMEBA_LOGUART_PERIPHS AMEBA_SINGLE_PERIPH(LOGUART) /* AMEBA_LOGUART_CLK */
```

相关声明：[AMEBA_LOGUART_PERIPHS](#a1020076bac0b7d227c73d4482c95ebd0)、[AMEBA_SINGLE_PERIPH](#a47ccaa9d57758ebac1885d09d6067af1)、[AMEBA_LOGUART_CLK](#a996962b9c7b1dd32421226bde07184c1)。

LOGUART 时钟外设映射（Clock Peripheral Mapping）。

<a id="r_aa6c9d573d5557d360896d2f36e146c22"></a>

```c
#define AMEBA_KSCAN_PERIPHS AMEBA_SINGLE_PERIPH(KSCAN) /* AMEBA_KSCAN_CLK */
```

相关声明：[AMEBA_KSCAN_PERIPHS](#aa6c9d573d5557d360896d2f36e146c22)、[AMEBA_SINGLE_PERIPH](#a47ccaa9d57758ebac1885d09d6067af1)、[AMEBA_KSCAN_CLK](#ad2318a02565100eee1cb633744db9dd0)。

KSCAN 时钟外设映射（Clock Peripheral Mapping）。

<a id="r_a7cb7d3ae836430c96cf1e80e1e2db9a0"></a>

```c
#define AMEBA_DMAC_PERIPHS AMEBA_SINGLE_PERIPH(DMAC) /* AMEBA_DMAC_CLK */
```

相关声明：[AMEBA_DMAC_PERIPHS](#a7cb7d3ae836430c96cf1e80e1e2db9a0)、[AMEBA_SINGLE_PERIPH](#a47ccaa9d57758ebac1885d09d6067af1)、[AMEBA_DMAC_CLK](#a3bb4d8911bd65c48f5c958f4bcd88a40)。

DMAC 时钟外设映射（Clock Peripheral Mapping）。

<a id="r_a88adc3ccf84373a1800d945a5ac1779e"></a>

```c
#define AMEBA_SDIO_PERIPHS AMEBA_SINGLE_PERIPH(SDIO) /* AMEBA_SDIO_CLK */
```

相关声明：[AMEBA_SDIO_PERIPHS](#a88adc3ccf84373a1800d945a5ac1779e)、[AMEBA_SINGLE_PERIPH](#a47ccaa9d57758ebac1885d09d6067af1)、[AMEBA_SDIO_CLK](#aa18a82f87588818e5b7e37a851ccd423)。

SDIO 时钟外设映射（Clock Peripheral Mapping）。

<a id="r_abdb58697292aa67f3fa8d4ea383991f7"></a>

```c
#define AMEBA_USB_PERIPHS AMEBA_SINGLE_PERIPH(USB) /* AMEBA_USB_CLK */
```

相关声明：[AMEBA_USB_PERIPHS](#abdb58697292aa67f3fa8d4ea383991f7)、[AMEBA_SINGLE_PERIPH](#a47ccaa9d57758ebac1885d09d6067af1)、[AMEBA_USB_CLK](#a9811b8e45cdc63a1dee22ff4ecce6fb5)。

USB 时钟外设映射（Clock Peripheral Mapping）。

<a id="r_a9f7681b1b804b2d916095739bd45825b"></a>

```c
#define AMEBA_FLASH_PERIPHS AMEBA_SINGLE_PERIPH(FLASH) /* AMEBA_FLASH_CLK */
```

相关声明：[AMEBA_FLASH_PERIPHS](#a9f7681b1b804b2d916095739bd45825b)、[AMEBA_SINGLE_PERIPH](#a47ccaa9d57758ebac1885d09d6067af1)、[AMEBA_FLASH_CLK](#ad32629d31a567d5d134e421cd527253a)。

闪存时钟外设映射（Flash Clock Peripheral Mapping）。

<a id="r_ae0fb2795cbc68a3c66aaff30bb47d77d"></a>

```c
#define AMEBA_PSRAM_PERIPHS AMEBA_SINGLE_PERIPH(PSRAM) /* AMEBA_PSRAM_CLK */
```

相关声明：[AMEBA_PSRAM_PERIPHS](#ae0fb2795cbc68a3c66aaff30bb47d77d)、[AMEBA_SINGLE_PERIPH](#a47ccaa9d57758ebac1885d09d6067af1)、[AMEBA_PSRAM_CLK](#a2d6f84861d9ceff804149347a06e796b)。

PSRAM 时钟外设映射（Clock Peripheral Mapping）。

<a id="r_a34387480634e9dcb974121c2344c2b14"></a>

```c
#define AMEBA_AC_PERIPHS AMEBA_SINGLE_PERIPH(AC) /* AMEBA_AC_CLK */
```

相关声明：[AMEBA_AC_PERIPHS](#a34387480634e9dcb974121c2344c2b14)、[AMEBA_SINGLE_PERIPH](#a47ccaa9d57758ebac1885d09d6067af1)、[AMEBA_AC_CLK](#adfb9684f04c1a52a9ba0ed6c9545d045)。

AC 时钟外设映射（Clock Peripheral Mapping）。

<a id="r_a004ed7273840b3daef2a9f276d7dada6"></a>

```c
#define AMEBA_IRDA_PERIPHS AMEBA_SINGLE_PERIPH(IRDA) /* AMEBA_IRDA_CLK */
```

相关声明：[AMEBA_IRDA_PERIPHS](#a004ed7273840b3daef2a9f276d7dada6)、[AMEBA_SINGLE_PERIPH](#a47ccaa9d57758ebac1885d09d6067af1)、[AMEBA_IRDA_CLK](#aed01c7bc1553e9902a27bf7318245d99)。

IRDA 时钟外设映射（Clock Peripheral Mapping）。

<a id="r_af978b5a1294b2542ff6bcee9b33fae58"></a>

```c
#define AMEBA_TRNG_PERIPHS AMEBA_SINGLE_PERIPH(TRNG) /* AMEBA_TRNG_CLK */
```

相关声明：[AMEBA_TRNG_PERIPHS](#af978b5a1294b2542ff6bcee9b33fae58)、[AMEBA_SINGLE_PERIPH](#a47ccaa9d57758ebac1885d09d6067af1)、[AMEBA_TRNG_CLK](#ae7e4292f7a91fb471d32b0fd36b8384f)。

TRNG 时钟外设映射（Clock Peripheral Mapping）。

<a id="r_a5d786480113fc750e578c92f33ae09cb"></a>

```c
#define AMEBA_RTC_PERIPHS AMEBA_SINGLE_PERIPH(RTC) /* AMEBA_RTC_CLK */
```

相关声明：[AMEBA_RTC_PERIPHS](#a5d786480113fc750e578c92f33ae09cb)、[AMEBA_SINGLE_PERIPH](#a47ccaa9d57758ebac1885d09d6067af1)、[AMEBA_RTC_CLK](#a9f089feea64d395b53ec91451346889d)。

RTC 时钟外设映射（Clock Peripheral Mapping）。

<a id="r_a8908b3477a3151478e28d20da5bc761d"></a>

```c
#define AMEBA_LEDC_PERIPHS AMEBA_SINGLE_PERIPH(LEDC) /* AMEBA_LEDC_CLK */
```

相关声明：[AMEBA_LEDC_PERIPHS](#a8908b3477a3151478e28d20da5bc761d)、[AMEBA_SINGLE_PERIPH](#a47ccaa9d57758ebac1885d09d6067af1)、[AMEBA_LEDC_CLK](#a8f7e7a6493ce0d8db53a5446c588f3d4)。

LEDC 时钟外设映射（Clock Peripheral Mapping）。

<a id="r_a9bb810d952e1a240d9f6ff3d1f62e22c"></a>

```c
#define AMEBA_ADC_PERIPHS AMEBA_SINGLE_PERIPH(ADC) /* AMEBA_ADC_CLK */
```

相关声明：[AMEBA_ADC_PERIPHS](#a9bb810d952e1a240d9f6ff3d1f62e22c)、[AMEBA_SINGLE_PERIPH](#a47ccaa9d57758ebac1885d09d6067af1)、[AMEBA_ADC_CLK](#a790dbb7ace4f63eb2a68de13c4dac8ef)。

ADC 时钟外设映射（Clock Peripheral Mapping）。

<a id="r_af7bbf5921d40aed8bb5c92e38b8f5987"></a>

```c
#define AMEBA_GPIO_PERIPHS AMEBA_SINGLE_PERIPH(GPIO) /* AMEBA_GPIO_CLK */
```

相关声明：[AMEBA_GPIO_PERIPHS](#af7bbf5921d40aed8bb5c92e38b8f5987)、[AMEBA_SINGLE_PERIPH](#a47ccaa9d57758ebac1885d09d6067af1)、[AMEBA_GPIO_CLK](#a060a938a705823c18de0ce9133c0a99d)。

GPIO 时钟外设映射（Clock Peripheral Mapping）。

<a id="r_aed8c7c32be8f3c7f3aff181bfd2a4f92"></a>

```c
#define AMEBA_BTON_PERIPHS AMEBA_SINGLE_PERIPH(BTON) /* AMEBA_BTON_CLK */
```

相关声明：[AMEBA_BTON_PERIPHS](#aed8c7c32be8f3c7f3aff181bfd2a4f92)、[AMEBA_SINGLE_PERIPH](#a47ccaa9d57758ebac1885d09d6067af1)、[AMEBA_BTON_CLK](#ad3f1e380b1e407166b21646cde8e145f)。

BTON 时钟外设映射（Clock Peripheral Mapping）。

<a id="r_a7373bf9f717e1250e7a52b64d373aadc"></a>

```c
#define AMEBA_CORE_PERIPHS
```

相关声明：[AMEBA_CORE_PERIPHS](#a7373bf9f717e1250e7a52b64d373aadc)。

汇总的核心外设时钟映射（Aggregated Core Peripheral Clock Mappings）。

## 3.2\_详细说明（Detailed Documentation）

<a id="adfb9684f04c1a52a9ba0ed6c9545d045"></a>

### `AMEBA_AC_CLK`

```c
#define AMEBA_AC_CLK 35
```

SoC 域（Domain）中的 AC 时钟（Clock）。

<a id="a34387480634e9dcb974121c2344c2b14"></a>

### `AMEBA_AC_PERIPHS`

```c
#define AMEBA_AC_PERIPHS AMEBA_SINGLE_PERIPH(AC) /* AMEBA_AC_CLK */
```

AC 时钟外设映射（Clock Peripheral Mapping）。

<a id="a790dbb7ace4f63eb2a68de13c4dac8ef"></a>

### `AMEBA_ADC_CLK`

```c
#define AMEBA_ADC_CLK 13
```

SYSON 域（Domain）中的 ADC 时钟（Clock）。

<a id="a9bb810d952e1a240d9f6ff3d1f62e22c"></a>

### `AMEBA_ADC_PERIPHS`

```c
#define AMEBA_ADC_PERIPHS AMEBA_SINGLE_PERIPH(ADC) /* AMEBA_ADC_CLK */
```

ADC 时钟外设映射（Clock Peripheral Mapping）。

<a id="a13aff4f0d9cb48d2e58b0525b9f96853"></a>

### `AMEBA_AES_CLK`

```c
#define AMEBA_AES_CLK 42
```

杂项域（Misc Domain）中的 AES 时钟（Clock）。

<a id="addc3bc2c9372ac83316911fc48d132b4"></a>

### `AMEBA_ATIM_CLK`

```c
#define AMEBA_ATIM_CLK 1
```

AON 域（Domain）中的 ATIM 时钟（Clock）。

<a id="ad3f1e380b1e407166b21646cde8e145f"></a>

### `AMEBA_BTON_CLK`

```c
#define AMEBA_BTON_CLK 40
```

BTON 时钟（Clock）。

<a id="aed8c7c32be8f3c7f3aff181bfd2a4f92"></a>

### `AMEBA_BTON_PERIPHS`

```c
#define AMEBA_BTON_PERIPHS AMEBA_SINGLE_PERIPH(BTON) /* AMEBA_BTON_CLK */
```

BTON 时钟外设映射（Clock Peripheral Mapping）。

<a id="a9ce69f2fdf39f6eb6b2dfdebc6b35fae"></a>

### `AMEBA_CLK_MAX`

```c
#define AMEBA_CLK_MAX 43 /* clk idx max */
```

最大时钟索引（Maximum Clock Index），比最后一个有效索引大 1。

<a id="a7373bf9f717e1250e7a52b64d373aadc"></a>

### `AMEBA_CORE_PERIPHS`

```c
#define AMEBA_CORE_PERIPHS
```

展开值（Value）：

```c
AMEBA_RTC_PERIPHS                                                                  \
AMEBA_PWM_PERIPHS                                                                  \
AMEBA_HTIM_PERIPHS                                                                 \
AMEBA_LEDC_PERIPHS                                                                 \
AMEBA_UART_PERIPHS                                                                 \
AMEBA_LOGUART_PERIPHS                                                              \
AMEBA_ADC_PERIPHS                                                                  \
AMEBA_GPIO_PERIPHS                                                                 \
AMEBA_LTIM_PERIPHS                                                                 \
AMEBA_PTIM_PERIPHS                                                                 \
AMEBA_KSCAN_PERIPHS                                                                \
AMEBA_DMAC_PERIPHS                                                                 \
AMEBA_SDIO_PERIPHS                                                                 \
AMEBA_SPI_PERIPHS                                                                  \
AMEBA_USB_PERIPHS                                                                  \
AMEBA_FLASH_PERIPHS                                                                \
AMEBA_SPORT_PERIPHS                                                                \
AMEBA_AC_PERIPHS                                                                   \
AMEBA_I2C_PERIPHS                                                                  \
AMEBA_TRNG_PERIPHS                                                                 \
AMEBA_BTON_PERIPHS
```

汇总的核心外设时钟映射（Aggregated Core Peripheral Clock Mappings）。

本宏展开为时钟控制实现（Clock Control Implementation）所使用的全部核心外设的映射。

<a id="a3bb4d8911bd65c48f5c958f4bcd88a40"></a>

### `AMEBA_DMAC_CLK`

```c
#define AMEBA_DMAC_CLK 26
```

SoC 域（Domain）中的 DMAC 时钟（Clock）。

<a id="a7cb7d3ae836430c96cf1e80e1e2db9a0"></a>

### `AMEBA_DMAC_PERIPHS`

```c
#define AMEBA_DMAC_PERIPHS AMEBA_SINGLE_PERIPH(DMAC) /* AMEBA_DMAC_CLK */
```

DMAC 时钟外设映射（Clock Peripheral Mapping）。

<a id="aef91aa4146dafae99bef8ef9478f8a15"></a>

### `AMEBA_DTIM_CLK`

```c
#define AMEBA_DTIM_CLK 12
```

SYSON 域（Domain）中的 DTIM 时钟（Clock）。

<a id="ad32629d31a567d5d134e421cd527253a"></a>

### `AMEBA_FLASH_CLK`

```c
#define AMEBA_FLASH_CLK 31
```

SoC 域（Domain）中的闪存时钟（Flash Clock）。

<a id="a9f7681b1b804b2d916095739bd45825b"></a>

### `AMEBA_FLASH_PERIPHS`

```c
#define AMEBA_FLASH_PERIPHS AMEBA_SINGLE_PERIPH(FLASH) /* AMEBA_FLASH_CLK */
```

闪存时钟外设映射（Flash Clock Peripheral Mapping）。

<a id="a060a938a705823c18de0ce9133c0a99d"></a>

### `AMEBA_GPIO_CLK`

```c
#define AMEBA_GPIO_CLK 14
```

SYSON 域（Domain）中的 GPIO 时钟（Clock）。

<a id="af7bbf5921d40aed8bb5c92e38b8f5987"></a>

### `AMEBA_GPIO_PERIPHS`

```c
#define AMEBA_GPIO_PERIPHS AMEBA_SINGLE_PERIPH(GPIO) /* AMEBA_GPIO_CLK */
```

GPIO 时钟外设映射（Clock Peripheral Mapping）。

<a id="a7792fde84e7acfbeb941ebb4fa5f696e"></a>

### `AMEBA_HTIM0_CLK`

```c
#define AMEBA_HTIM0_CLK 5
```

SYSON 域（Domain）中的 HTIM0 时钟（Clock）。

<a id="a886720ba1e95f0b4a4754eb315b2a270"></a>

### `AMEBA_HTIM1_CLK`

```c
#define AMEBA_HTIM1_CLK 6
```

SYSON 域（Domain）中的 HTIM1 时钟（Clock）。

<a id="a15bb72de50884608e12cd39e47f9cfb1"></a>

### `AMEBA_HTIM_PERIPHS`

```c
#define AMEBA_HTIM_PERIPHS
```

展开值（Value）：

```c
AMEBA_NUMERICAL_PERIPH(HTIM, 0) /* AMEBA_HTIM0_CLK */                              \
AMEBA_NUMERICAL_PERIPH(HTIM, 1) /* AMEBA_HTIM1_CLK */
```

HTIM 时钟外设映射（Clock Peripheral Mapping）。

<a id="ac293b0216f849f4bffd50253b0df9fd7"></a>

### `AMEBA_I2C0_CLK`

```c
#define AMEBA_I2C0_CLK 37
```

SoC 域（Domain）中的 I2C0 时钟（Clock）。

<a id="ae8a2efe5f489463a64db00003edf8c58"></a>

### `AMEBA_I2C1_CLK`

```c
#define AMEBA_I2C1_CLK 38
```

SoC 域（Domain）中的 I2C1 时钟（Clock）。

<a id="ab55bb29f8a5c2a0fd1dba45d0c9f4910"></a>

### `AMEBA_I2C_PERIPHS`

```c
#define AMEBA_I2C_PERIPHS
```

展开值（Value）：

```c
AMEBA_NUMERICAL_PERIPH(I2C, 0) /* AMEBA_I2C0_CLK */                                \
AMEBA_NUMERICAL_PERIPH(I2C, 1) /* AMEBA_I2C1_CLK */
```

I2C 时钟外设映射（Clock Peripheral Mappings）。

<a id="aed01c7bc1553e9902a27bf7318245d99"></a>

### `AMEBA_IRDA_CLK`

```c
#define AMEBA_IRDA_CLK 36
```

SoC 域（Domain）中的 IRDA 时钟（Clock）。

<a id="a004ed7273840b3daef2a9f276d7dada6"></a>

### `AMEBA_IRDA_PERIPHS`

```c
#define AMEBA_IRDA_PERIPHS AMEBA_SINGLE_PERIPH(IRDA) /* AMEBA_IRDA_CLK */
```

IRDA 时钟外设映射（Clock Peripheral Mapping）。

<a id="ad2318a02565100eee1cb633744db9dd0"></a>

### `AMEBA_KSCAN_CLK`

```c
#define AMEBA_KSCAN_CLK 25
```

SYSON 域（Domain）中的 KSCAN 时钟（Clock）。

<a id="aa6c9d573d5557d360896d2f36e146c22"></a>

### `AMEBA_KSCAN_PERIPHS`

```c
#define AMEBA_KSCAN_PERIPHS AMEBA_SINGLE_PERIPH(KSCAN) /* AMEBA_KSCAN_CLK */
```

KSCAN 时钟外设映射（Clock Peripheral Mapping）。

<a id="a8f7e7a6493ce0d8db53a5446c588f3d4"></a>

### `AMEBA_LEDC_CLK`

```c
#define AMEBA_LEDC_CLK 7
```

SYSON 域（Domain）中的 LEDC 时钟（Clock）。

<a id="a8908b3477a3151478e28d20da5bc761d"></a>

### `AMEBA_LEDC_PERIPHS`

```c
#define AMEBA_LEDC_PERIPHS AMEBA_SINGLE_PERIPH(LEDC) /* AMEBA_LEDC_CLK */
```

LEDC 时钟外设映射（Clock Peripheral Mapping）。

<a id="a996962b9c7b1dd32421226bde07184c1"></a>

### `AMEBA_LOGUART_CLK`

```c
#define AMEBA_LOGUART_CLK 11
```

SYSON 域（Domain）中的 LOGUART 时钟（Clock）。

<a id="a1020076bac0b7d227c73d4482c95ebd0"></a>

### `AMEBA_LOGUART_PERIPHS`

```c
#define AMEBA_LOGUART_PERIPHS AMEBA_SINGLE_PERIPH(LOGUART) /* AMEBA_LOGUART_CLK */
```

LOGUART 时钟外设映射（Clock Peripheral Mapping）。

<a id="ab3149be5245573521f4bb7e551e625e7"></a>

### `AMEBA_LTIM0_CLK`

```c
#define AMEBA_LTIM0_CLK 15
```

SYSON 域（Domain）中的 LTIM0 时钟（Clock）。

<a id="a776ea52d9a1f082f7037bd2b01a0d4bb"></a>

### `AMEBA_LTIM1_CLK`

```c
#define AMEBA_LTIM1_CLK 16
```

SYSON 域（Domain）中的 LTIM1 时钟（Clock）。

<a id="a832779b2dc473e221ba4a4b813807dbc"></a>

### `AMEBA_LTIM2_CLK`

```c
#define AMEBA_LTIM2_CLK 17
```

SYSON 域（Domain）中的 LTIM2 时钟（Clock）。

<a id="a371d8e766d052283c390868989cc9283"></a>

### `AMEBA_LTIM3_CLK`

```c
#define AMEBA_LTIM3_CLK 18
```

SYSON 域（Domain）中的 LTIM3 时钟（Clock）。

<a id="a9c2241936d9f61aa68f61f1d1e270870"></a>

### `AMEBA_LTIM4_CLK`

```c
#define AMEBA_LTIM4_CLK 19
```

SYSON 域（Domain）中的 LTIM4 时钟（Clock）。

<a id="ab5b0d934d7a784ccce21ad84d6559bfa"></a>

### `AMEBA_LTIM5_CLK`

```c
#define AMEBA_LTIM5_CLK 20
```

SYSON 域（Domain）中的 LTIM5 时钟（Clock）。

<a id="a6e18da23aa07580b3cd81c6a20d2dce2"></a>

### `AMEBA_LTIM6_CLK`

```c
#define AMEBA_LTIM6_CLK 21
```

SYSON 域（Domain）中的 LTIM6 时钟（Clock）。

<a id="a6c0d56f6b7abc587971020ec06d12a77"></a>

### `AMEBA_LTIM7_CLK`

```c
#define AMEBA_LTIM7_CLK 22
```

SYSON 域（Domain）中的 LTIM7 时钟（Clock）。

<a id="a89ef5e4da90cb6459240ea4f998c61c5"></a>

### `AMEBA_LTIM_PERIPHS`

```c
#define AMEBA_LTIM_PERIPHS
```

展开值（Value）：

```c
AMEBA_NUMERICAL_PERIPH(LTIM, 0) /* AMEBA_LTIM0_CLK */                              \
AMEBA_NUMERICAL_PERIPH(LTIM, 1) /* AMEBA_LTIM1_CLK */                              \
AMEBA_NUMERICAL_PERIPH(LTIM, 2) /* AMEBA_LTIM2_CLK */                              \
AMEBA_NUMERICAL_PERIPH(LTIM, 3) /* AMEBA_LTIM3_CLK */                              \
AMEBA_NUMERICAL_PERIPH(LTIM, 4) /* AMEBA_LTIM4_CLK */                              \
AMEBA_NUMERICAL_PERIPH(LTIM, 5) /* AMEBA_LTIM5_CLK */                              \
AMEBA_NUMERICAL_PERIPH(LTIM, 6) /* AMEBA_LTIM6_CLK */                              \
AMEBA_NUMERICAL_PERIPH(LTIM, 7) /* AMEBA_LTIM7_CLK */
```

LTIM 时钟外设映射（Clock Peripheral Mapping）。

<a id="a5892f2668cc892817f59230643162ee4"></a>

### `AMEBA_NUMERICAL_PERIPH`

```c
#define AMEBA_NUMERICAL_PERIPH ( name, n )
```

展开值（Value）：

```c
[AMEBA_##name##n##_CLK] = {                                                        \
        .parent = AMEBA_RCC_NO_PARENT,                                             \
        .cke = APBPeriph_##name##n##_CLOCK,                                        \
        .fen = APBPeriph_##name##n,                                                \
},
```

为带数字后缀的外设定义时钟条目（Clock Entry）。

用于带索引的外设（Peripheral），例如 SPI0、SPI1、UART0。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 外设基本名称（Peripheral Base Name）。 |
| `n` | 外设索引（Peripheral Index）。 |

<a id="a2d6f84861d9ceff804149347a06e796b"></a>

### `AMEBA_PSRAM_CLK`

```c
#define AMEBA_PSRAM_CLK 32
```

SoC 域（Domain）中的 PSRAM 时钟（Clock）。

<a id="ae0fb2795cbc68a3c66aaff30bb47d77d"></a>

### `AMEBA_PSRAM_PERIPHS`

```c
#define AMEBA_PSRAM_PERIPHS AMEBA_SINGLE_PERIPH(PSRAM) /* AMEBA_PSRAM_CLK */
```

PSRAM 时钟外设映射（Clock Peripheral Mapping）。

<a id="a24b192e5fb6291e88af8274a52c7af18"></a>

### `AMEBA_PTIM0_CLK`

```c
#define AMEBA_PTIM0_CLK 23
```

SYSON 域（Domain）中的 PTIM0 时钟（Clock）。

<a id="a4ac4664b0e6f6af828ebf6d719a91b28"></a>

### `AMEBA_PTIM1_CLK`

```c
#define AMEBA_PTIM1_CLK 24
```

SYSON 域（Domain）中的 PTIM1 时钟（Clock）。

<a id="a497ef8d62b1db3ec4d9f8b27c0b1aa22"></a>

### `AMEBA_PTIM_PERIPHS`

```c
#define AMEBA_PTIM_PERIPHS
```

展开值（Value）：

```c
AMEBA_NUMERICAL_PERIPH(PTIM, 0) /* AMEBA_PTIM0_CLK */                              \
AMEBA_NUMERICAL_PERIPH(PTIM, 1) /* AMEBA_PTIM1_CLK */
```

PTIM 时钟外设映射（Clock Peripheral Mapping）。

<a id="a523f7ac5827b17a56f7940c18481abb8"></a>

### `AMEBA_PWM0_CLK`

```c
#define AMEBA_PWM0_CLK 3
```

SYSON 域（Domain）中的 PWM0 时钟（Clock）。

<a id="a580af7f35de2aa6faaf2210784887baf"></a>

### `AMEBA_PWM1_CLK`

```c
#define AMEBA_PWM1_CLK 4
```

SYSON 域（Domain）中的 PWM1 时钟（Clock）。

<a id="a7a3e89aeca0afde7c5c5350e75f289eb"></a>

### `AMEBA_PWM_PERIPHS`

```c
#define AMEBA_PWM_PERIPHS
```

展开值（Value）：

```c
AMEBA_NUMERICAL_PERIPH(PWM, 0) /* AMEBA_PWM0_CLK */                                \
AMEBA_NUMERICAL_PERIPH(PWM, 1) /* AMEBA_PWM1_CLK */
```

PWM 时钟外设映射（Clock Peripheral Mapping）。

<a id="a9f089feea64d395b53ec91451346889d"></a>

### `AMEBA_RTC_CLK`

```c
#define AMEBA_RTC_CLK 2
```

AON 域（Domain）中的 RTC 时钟（Clock）。

<a id="a5d786480113fc750e578c92f33ae09cb"></a>

### `AMEBA_RTC_PERIPHS`

```c
#define AMEBA_RTC_PERIPHS AMEBA_SINGLE_PERIPH(RTC) /* AMEBA_RTC_CLK */
```

RTC 时钟外设映射（Clock Peripheral Mapping）。

<a id="aa18a82f87588818e5b7e37a851ccd423"></a>

### `AMEBA_SDIO_CLK`

```c
#define AMEBA_SDIO_CLK 27
```

SoC 域（Domain）中的 SDIO 时钟（Clock）。

<a id="a88adc3ccf84373a1800d945a5ac1779e"></a>

### `AMEBA_SDIO_PERIPHS`

```c
#define AMEBA_SDIO_PERIPHS AMEBA_SINGLE_PERIPH(SDIO) /* AMEBA_SDIO_CLK */
```

SDIO 时钟外设映射（Clock Peripheral Mapping）。

<a id="a47ccaa9d57758ebac1885d09d6067af1"></a>

### `AMEBA_SINGLE_PERIPH`

```c
#define AMEBA_SINGLE_PERIPH ( name)
```

展开值（Value）：

```c
[AMEBA_##name##_CLK] = {                                                           \
        .parent = AMEBA_RCC_NO_PARENT,                                             \
        .cke = APBPeriph_##name##_CLOCK,                                           \
        .fen = APBPeriph_##name,                                                   \
},
```

为只有一个实例的外设定义时钟条目（Clock Entry）。

用于只有一个实例的外设（Peripheral），例如 DMAC、SDIO、USB、TRNG 等。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 外设名称（Peripheral Name）。 |

<a id="a44689e534b5693fe964e45f04ec3af3a"></a>

### `AMEBA_SPI0_CLK`

```c
#define AMEBA_SPI0_CLK 28
```

SoC 域（Domain）中的 SPI0 时钟（Clock）。

<a id="a1997336af677a35e15d1402aed065ee6"></a>

### `AMEBA_SPI1_CLK`

```c
#define AMEBA_SPI1_CLK 29
```

SoC 域（Domain）中的 SPI1 时钟（Clock）。

<a id="a9a0c99a81816161def16ba0f969c159d"></a>

### `AMEBA_SPI_PERIPHS`

```c
#define AMEBA_SPI_PERIPHS
```

展开值（Value）：

```c
AMEBA_NUMERICAL_PERIPH(SPI, 0) /* AMEBA_SPI0_CLK */                                \
AMEBA_NUMERICAL_PERIPH(SPI, 1) /* AMEBA_SPI1_CLK */
```

SPI 时钟外设映射（Clock Peripheral Mappings）。

<a id="ae123e8df6cb6c584da9eb41d2dec9c4e"></a>

### `AMEBA_SPORT0_CLK`

```c
#define AMEBA_SPORT0_CLK 33
```

SoC 域（Domain）中的 SPORT0 时钟（Clock）。

<a id="a4196280bae37b3405b303b713107a50a"></a>

### `AMEBA_SPORT1_CLK`

```c
#define AMEBA_SPORT1_CLK 34
```

SoC 域（Domain）中的 SPORT1 时钟（Clock）。

<a id="a854f2eee8cff49b0c00a400e4295f7e5"></a>

### `AMEBA_SPORT_PERIPHS`

```c
#define AMEBA_SPORT_PERIPHS
```

展开值（Value）：

```c
AMEBA_NUMERICAL_PERIPH(SPORT, 0) /* AMEBA_SPORT0_CLK */                            \
AMEBA_NUMERICAL_PERIPH(SPORT, 1) /* AMEBA_SPORT1_CLK */
```

SPORT 时钟外设映射（Clock Peripheral Mapping）。

<a id="ae7e4292f7a91fb471d32b0fd36b8384f"></a>

### `AMEBA_TRNG_CLK`

```c
#define AMEBA_TRNG_CLK 39
```

SoC 域（Domain）中的 TRNG 时钟（Clock）。

<a id="af978b5a1294b2542ff6bcee9b33fae58"></a>

### `AMEBA_TRNG_PERIPHS`

```c
#define AMEBA_TRNG_PERIPHS AMEBA_SINGLE_PERIPH(TRNG) /* AMEBA_TRNG_CLK */
```

TRNG 时钟外设映射（Clock Peripheral Mapping）。

<a id="a36ebf3e1fd6ac0092aab3589d14d20b3"></a>

### `AMEBA_UART0_CLK`

```c
#define AMEBA_UART0_CLK 8
```

SYSON 域（Domain）中的 UART0 时钟（Clock）。

<a id="a8df46e7a94c9ccd5174aab94c9531e7e"></a>

### `AMEBA_UART1_CLK`

```c
#define AMEBA_UART1_CLK 9
```

SYSON 域（Domain）中的 UART1 时钟（Clock）。

<a id="a32eaddcc095242263b580d0b736eef53"></a>

### `AMEBA_UART2_CLK`

```c
#define AMEBA_UART2_CLK 10
```

SYSON 域（Domain）中的 UART2 时钟（Clock）。

<a id="a7b90187464653d7b1e83e0fd01c21e2f"></a>

### `AMEBA_UART_PERIPHS`

```c
#define AMEBA_UART_PERIPHS
```

展开值（Value）：

```c
AMEBA_NUMERICAL_PERIPH(UART, 0) /* AMEBA_UART0_CLK */                              \
AMEBA_NUMERICAL_PERIPH(UART, 1) /* AMEBA_UART1_CLK */                              \
AMEBA_NUMERICAL_PERIPH(UART, 2) /* AMEBA_UART2_CLK */
```

UART 时钟外设映射（Clock Peripheral Mappings）。

<a id="a9811b8e45cdc63a1dee22ff4ecce6fb5"></a>

### `AMEBA_USB_CLK`

```c
#define AMEBA_USB_CLK 30
```

SoC 域（Domain）中的 USB 时钟（Clock）。

<a id="abdb58697292aa67f3fa8d4ea383991f7"></a>

### `AMEBA_USB_PERIPHS`

```c
#define AMEBA_USB_PERIPHS AMEBA_SINGLE_PERIPH(USB) /* AMEBA_USB_CLK */
```

USB 时钟外设映射（Clock Peripheral Mapping）。


## 3.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_http_wifi_reference/P002_amebadplus_clock.h_源码浏览.md)
- [max](../numeric_reference/P001_最小最大值与限幅宏参考.md#affe776513b24d84b39af8ab0930fef7f)
- [AMEBA_NUMERICAL_PERIPH](P002_zephyr__dt-bindings__clock__amebad_clock.h_文件参考.md#a5892f2668cc892817f59230643162ee4)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="aamebad__clock_8h_html_a5892f2668cc892817f59230643162ee4"></a>

---

[上一章](P002_zephyr__dt-bindings__clock__amebad_clock.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P004_zephyr__dt-bindings__clock__amebag2_clock.h_文件参考.md)
