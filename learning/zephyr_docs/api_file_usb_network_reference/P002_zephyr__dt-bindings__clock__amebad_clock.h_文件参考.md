---
id: learning.zephyr-docs.api-file-usb-network-reference.page-2
title: zephyr__dt-bindings__clock__amebad_clock.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/amebad__clock_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_zephyr\_\_dt-bindings\_\_clock\_\_amebad\_clock.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/amebad__clock_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Realtek Amebad时钟的设备树绑定（Devicetree Bindings）。

查看此文件的源码。

<a id="details"></a>

Realtek Amebad时钟的设备树绑定（Devicetree Bindings）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 常开域时钟（AON Domain Clocks）

<a id="r_addc3bc2c9372ac83316911fc48d132b4"></a>

```c
#define AMEBA_ATIM_CLK 0
```

相关声明：[AMEBA_ATIM_CLK](#addc3bc2c9372ac83316911fc48d132b4)。

AON 域（Domain）中的 ATIM 时钟（Clock）。

<a id="r_a9f089feea64d395b53ec91451346889d"></a>

```c
#define AMEBA_RTC_CLK 1
```

相关声明：[AMEBA_RTC_CLK](#a9f089feea64d395b53ec91451346889d)。

AON 域（Domain）中的 RTC 时钟（Clock）。

<a id="define-members-1"></a>

### SYSON 域时钟（SYSON Domain Clocks）

<a id="r_a523f7ac5827b17a56f7940c18481abb8"></a>

```c
#define AMEBA_PWM0_CLK 2
```

相关声明：[AMEBA_PWM0_CLK](#a523f7ac5827b17a56f7940c18481abb8)。

SYSON 域（Domain）中的 PWM0 时钟（Clock）。

<a id="r_a36ebf3e1fd6ac0092aab3589d14d20b3"></a>

```c
#define AMEBA_UART0_CLK 3
```

相关声明：[AMEBA_UART0_CLK](#a36ebf3e1fd6ac0092aab3589d14d20b3)。

SYSON 域（Domain）中的 UART0 时钟（Clock）。

<a id="r_a996962b9c7b1dd32421226bde07184c1"></a>

```c
#define AMEBA_LOGUART_CLK 4
```

相关声明：[AMEBA_LOGUART_CLK](#a996962b9c7b1dd32421226bde07184c1)。

SYSON 域（Domain）中的 LOGUART 时钟（Clock）。

<a id="r_a820d2fec9e6e7a757335cb97e5748f06"></a>

```c
#define AMEBA_UART3_CLK 5
```

相关声明：[AMEBA_UART3_CLK](#a820d2fec9e6e7a757335cb97e5748f06)。

SYSON 域（Domain）中的 UART3 时钟（Clock）。

<a id="r_a790dbb7ace4f63eb2a68de13c4dac8ef"></a>

```c
#define AMEBA_ADC_CLK 6
```

相关声明：[AMEBA_ADC_CLK](#a790dbb7ace4f63eb2a68de13c4dac8ef)。

SYSON 域（Domain）中的 ADC 时钟（Clock）。

<a id="r_a060a938a705823c18de0ce9133c0a99d"></a>

```c
#define AMEBA_GPIO_CLK 7
```

相关声明：[AMEBA_GPIO_CLK](#a060a938a705823c18de0ce9133c0a99d)。

SYSON 域（Domain）中的 GPIO 时钟（Clock）。

<a id="r_ab3149be5245573521f4bb7e551e625e7"></a>

```c
#define AMEBA_LTIM0_CLK 8
```

相关声明：[AMEBA_LTIM0_CLK](#ab3149be5245573521f4bb7e551e625e7)。

SYSON 域（Domain）中的 LTIM0 时钟（Clock）。

<a id="r_a776ea52d9a1f082f7037bd2b01a0d4bb"></a>

```c
#define AMEBA_LTIM1_CLK 9
```

相关声明：[AMEBA_LTIM1_CLK](#a776ea52d9a1f082f7037bd2b01a0d4bb)。

SYSON 域（Domain）中的 LTIM1 时钟（Clock）。

<a id="r_a832779b2dc473e221ba4a4b813807dbc"></a>

```c
#define AMEBA_LTIM2_CLK 10
```

相关声明：[AMEBA_LTIM2_CLK](#a832779b2dc473e221ba4a4b813807dbc)。

SYSON 域（Domain）中的 LTIM2 时钟（Clock）。

<a id="r_a371d8e766d052283c390868989cc9283"></a>

```c
#define AMEBA_LTIM3_CLK 11
```

相关声明：[AMEBA_LTIM3_CLK](#a371d8e766d052283c390868989cc9283)。

SYSON 域（Domain）中的 LTIM3 时钟（Clock）。

<a id="define-members-2"></a>

### SoC 域时钟（SoC Domain Clocks）

<a id="r_a23f2311464ddfe56f20e91fad94c5492"></a>

```c
#define AMEBA_PERI_HCLK 12
```

相关声明：[AMEBA_PERI_HCLK](#a23f2311464ddfe56f20e91fad94c5492)。

SoC 域（Domain）中的外设 HCLK（Peripheral HCLK）。

<a id="r_ae0ec3320a2378824f3af9c4aaed9689f"></a>

```c
#define AMEBA_GDMA0_CLK 13
```

相关声明：[AMEBA_GDMA0_CLK](#ae0ec3320a2378824f3af9c4aaed9689f)。

SoC 域（Domain）中的 GDMA0 时钟（Clock）。

<a id="r_a44689e534b5693fe964e45f04ec3af3a"></a>

```c
#define AMEBA_SPI0_CLK 14
```

相关声明：[AMEBA_SPI0_CLK](#a44689e534b5693fe964e45f04ec3af3a)。

SoC 域（Domain）中的 SPI0 时钟（Clock）。

<a id="r_a1997336af677a35e15d1402aed065ee6"></a>

```c
#define AMEBA_SPI1_CLK 15
```

相关声明：[AMEBA_SPI1_CLK](#a1997336af677a35e15d1402aed065ee6)。

SoC 域（Domain）中的 SPI1 时钟（Clock）。

<a id="r_ad32629d31a567d5d134e421cd527253a"></a>

```c
#define AMEBA_FLASH_CLK 16
```

相关声明：[AMEBA_FLASH_CLK](#ad32629d31a567d5d134e421cd527253a)。

SoC 域（Domain）中的闪存时钟（Flash Clock）。

<a id="r_a2d6f84861d9ceff804149347a06e796b"></a>

```c
#define AMEBA_PSRAM_CLK 17
```

相关声明：[AMEBA_PSRAM_CLK](#a2d6f84861d9ceff804149347a06e796b)。

SoC 域（Domain）中的 PSRAM 时钟（Clock）。

<a id="r_ac293b0216f849f4bffd50253b0df9fd7"></a>

```c
#define AMEBA_I2C0_CLK 18
```

相关声明：[AMEBA_I2C0_CLK](#ac293b0216f849f4bffd50253b0df9fd7)。

SoC 域（Domain）中的 I2C0 时钟（Clock）。

<a id="r_a37db8ed6566f8d47b4e6c1e3a536775d"></a>

```c
#define AMEBA_PRNG_CLK 19
```

相关声明：[AMEBA_PRNG_CLK](#a37db8ed6566f8d47b4e6c1e3a536775d)。

SoC 域（Domain）中的 PRNG 时钟（Clock）。

<a id="r_a9ce69f2fdf39f6eb6b2dfdebc6b35fae"></a>

```c
#define AMEBA_CLK_MAX 20 /* clk idx max */
```

相关声明：[AMEBA_CLK_MAX](#a9ce69f2fdf39f6eb6b2dfdebc6b35fae)、[max](../numeric_reference/P001_最小最大值与限幅宏参考.md#affe776513b24d84b39af8ab0930fef7f)。

最大时钟索引（Maximum Clock Index），比最后一个有效索引大 1。

<a id="define-members-3"></a>

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

<a id="r_a19d44435f2d7130c8ab41c13df6972f8"></a>

```c
#define AMEBA_REMAP_PERIPH(clk_index, remap_name)
```

相关声明：[AMEBA_REMAP_PERIPH](#a19d44435f2d7130c8ab41c13df6972f8)。

为名称经过重映射的外设定义时钟条目（Clock Entry）。

<a id="r_a89ef5e4da90cb6459240ea4f998c61c5"></a>

```c
#define AMEBA_LTIM_PERIPHS
```

相关声明：[AMEBA_LTIM_PERIPHS](#a89ef5e4da90cb6459240ea4f998c61c5)。

LTIM 时钟到 GTIMER 外设的映射（Clock Mapping）。

<a id="r_a7a3e89aeca0afde7c5c5350e75f289eb"></a>

```c
#define AMEBA_PWM_PERIPHS AMEBA_REMAP_PERIPH(AMEBA_PWM0_CLK, GTIMER)
```

相关声明：[AMEBA_PWM_PERIPHS](#a7a3e89aeca0afde7c5c5350e75f289eb)、[AMEBA_REMAP_PERIPH](#a19d44435f2d7130c8ab41c13df6972f8)、[AMEBA_PWM0_CLK](#a523f7ac5827b17a56f7940c18481abb8)。

PWM 时钟到 GTIMER 外设的映射（Clock Mapping）。

<a id="r_a9a0c99a81816161def16ba0f969c159d"></a>

```c
#define AMEBA_SPI_PERIPHS
```

相关声明：[AMEBA_SPI_PERIPHS](#a9a0c99a81816161def16ba0f969c159d)。

SPI 时钟外设映射（Clock Peripheral Mappings）。

<a id="r_ab55bb29f8a5c2a0fd1dba45d0c9f4910"></a>

```c
#define AMEBA_I2C_PERIPHS AMEBA_NUMERICAL_PERIPH(I2C, 0) /* AMEBA_I2C0_CLK */
```

相关声明：[AMEBA_I2C_PERIPHS](#ab55bb29f8a5c2a0fd1dba45d0c9f4910)、[AMEBA_NUMERICAL_PERIPH](#a5892f2668cc892817f59230643162ee4)、[AMEBA_I2C0_CLK](#ac293b0216f849f4bffd50253b0df9fd7)。

I2C 时钟外设映射（Clock Peripheral Mappings）。

<a id="r_a7b90187464653d7b1e83e0fd01c21e2f"></a>

```c
#define AMEBA_UART_PERIPHS
```

相关声明：[AMEBA_UART_PERIPHS](#a7b90187464653d7b1e83e0fd01c21e2f)。

UART 时钟外设映射（Clock Peripheral Mappings）。

<a id="r_a81a24118682991a81a7de59501e5812b"></a>

```c
#define AMEBA_GDMA0_PERIPHS AMEBA_SINGLE_PERIPH(GDMA0) /* AMEBA_GDMA0_CLK */
```

相关声明：[AMEBA_GDMA0_PERIPHS](#a81a24118682991a81a7de59501e5812b)、[AMEBA_SINGLE_PERIPH](#a47ccaa9d57758ebac1885d09d6067af1)、[AMEBA_GDMA0_CLK](#ae0ec3320a2378824f3af9c4aaed9689f)。

GDMA0 时钟外设映射（Clock Peripheral Mapping）。

<a id="r_ae0fb2795cbc68a3c66aaff30bb47d77d"></a>

```c
#define AMEBA_PSRAM_PERIPHS AMEBA_SINGLE_PERIPH(PSRAM) /* AMEBA_PSRAM_CLK */
```

相关声明：[AMEBA_PSRAM_PERIPHS](#ae0fb2795cbc68a3c66aaff30bb47d77d)、[AMEBA_SINGLE_PERIPH](#a47ccaa9d57758ebac1885d09d6067af1)、[AMEBA_PSRAM_CLK](#a2d6f84861d9ceff804149347a06e796b)。

PSRAM 时钟外设映射（Clock Peripheral Mapping）。

<a id="r_a5d786480113fc750e578c92f33ae09cb"></a>

```c
#define AMEBA_RTC_PERIPHS AMEBA_SINGLE_PERIPH(RTC) /* AMEBA_RTC_CLK */
```

相关声明：[AMEBA_RTC_PERIPHS](#a5d786480113fc750e578c92f33ae09cb)、[AMEBA_SINGLE_PERIPH](#a47ccaa9d57758ebac1885d09d6067af1)、[AMEBA_RTC_CLK](#a9f089feea64d395b53ec91451346889d)。

RTC 时钟外设映射（Clock Peripheral Mapping）。

<a id="r_a1020076bac0b7d227c73d4482c95ebd0"></a>

```c
#define AMEBA_LOGUART_PERIPHS AMEBA_REMAP_PERIPH(AMEBA_LOGUART_CLK, NULL)
```

相关声明：[AMEBA_LOGUART_PERIPHS](#a1020076bac0b7d227c73d4482c95ebd0)、[AMEBA_REMAP_PERIPH](#a19d44435f2d7130c8ab41c13df6972f8)、[AMEBA_LOGUART_CLK](#a996962b9c7b1dd32421226bde07184c1)。

LOGUART 时钟外设映射（Clock Peripheral Mapping）。

<a id="r_a9f7681b1b804b2d916095739bd45825b"></a>

```c
#define AMEBA_FLASH_PERIPHS AMEBA_REMAP_PERIPH(AMEBA_FLASH_CLK, NULL)
```

相关声明：[AMEBA_FLASH_PERIPHS](#a9f7681b1b804b2d916095739bd45825b)、[AMEBA_REMAP_PERIPH](#a19d44435f2d7130c8ab41c13df6972f8)、[AMEBA_FLASH_CLK](#ad32629d31a567d5d134e421cd527253a)。

闪存时钟外设映射（Flash Clock Peripheral Mapping）。

<a id="r_af7bbf5921d40aed8bb5c92e38b8f5987"></a>

```c
#define AMEBA_GPIO_PERIPHS AMEBA_REMAP_PERIPH(AMEBA_GPIO_CLK, NULL)
```

相关声明：[AMEBA_GPIO_PERIPHS](#af7bbf5921d40aed8bb5c92e38b8f5987)、[AMEBA_REMAP_PERIPH](#a19d44435f2d7130c8ab41c13df6972f8)、[AMEBA_GPIO_CLK](#a060a938a705823c18de0ce9133c0a99d)。

GPIO 时钟外设映射（Clock Peripheral Mapping）。

<a id="r_a9bb810d952e1a240d9f6ff3d1f62e22c"></a>

```c
#define AMEBA_ADC_PERIPHS AMEBA_REMAP_PERIPH(AMEBA_ADC_CLK, NULL)
```

相关声明：[AMEBA_ADC_PERIPHS](#a9bb810d952e1a240d9f6ff3d1f62e22c)、[AMEBA_REMAP_PERIPH](#a19d44435f2d7130c8ab41c13df6972f8)、[AMEBA_ADC_CLK](#a790dbb7ace4f63eb2a68de13c4dac8ef)。

ADC 时钟外设映射（Clock Peripheral Mapping）。

<a id="r_a59abad25eab1eab1dc5b97055ed140a4"></a>

```c
#define AMEBA_PRNG_PERIPHS AMEBA_REMAP_PERIPH(AMEBA_PRNG_CLK, NULL)
```

相关声明：[AMEBA_PRNG_PERIPHS](#a59abad25eab1eab1dc5b97055ed140a4)、[AMEBA_REMAP_PERIPH](#a19d44435f2d7130c8ab41c13df6972f8)、[AMEBA_PRNG_CLK](#a37db8ed6566f8d47b4e6c1e3a536775d)。

PRNG 时钟外设映射（Clock Peripheral Mapping）。

<a id="r_ae499eda9d017f36f20baa4007166fd5e"></a>

```c
#define APBPeriph_NULL_CLOCK APBPeriph_CLOCK_NULL
```

相关声明：[APBPeriph_NULL_CLOCK](#ae499eda9d017f36f20baa4007166fd5e)。

空 APB 外设时钟定义（Null APB Peripheral Clock Definition）。

<a id="r_a7373bf9f717e1250e7a52b64d373aadc"></a>

```c
#define AMEBA_CORE_PERIPHS
```

相关声明：[AMEBA_CORE_PERIPHS](#a7373bf9f717e1250e7a52b64d373aadc)。

汇总的核心外设时钟映射（Aggregated Core Peripheral Clock Mappings）。

## 2.2\_详细说明（Detailed Documentation）

<a id="a790dbb7ace4f63eb2a68de13c4dac8ef"></a>

### `AMEBA_ADC_CLK`

```c
#define AMEBA_ADC_CLK 6
```

SYSON 域（Domain）中的 ADC 时钟（Clock）。

<a id="a9bb810d952e1a240d9f6ff3d1f62e22c"></a>

### `AMEBA_ADC_PERIPHS`

```c
#define AMEBA_ADC_PERIPHS AMEBA_REMAP_PERIPH(AMEBA_ADC_CLK, NULL)
```

ADC 时钟外设映射（Clock Peripheral Mapping）。

<a id="addc3bc2c9372ac83316911fc48d132b4"></a>

### `AMEBA_ATIM_CLK`

```c
#define AMEBA_ATIM_CLK 0
```

AON 域（Domain）中的 ATIM 时钟（Clock）。

<a id="a9ce69f2fdf39f6eb6b2dfdebc6b35fae"></a>

### `AMEBA_CLK_MAX`

```c
#define AMEBA_CLK_MAX 20 /* clk idx max */
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
AMEBA_UART_PERIPHS                                                                 \
AMEBA_LOGUART_PERIPHS                                                              \
AMEBA_ADC_PERIPHS                                                                  \
AMEBA_GPIO_PERIPHS                                                                 \
AMEBA_LTIM_PERIPHS                                                                 \
AMEBA_GDMA0_PERIPHS                                                                \
AMEBA_SPI_PERIPHS                                                                  \
AMEBA_FLASH_PERIPHS                                                                \
AMEBA_I2C_PERIPHS                                                                  \
AMEBA_PRNG_PERIPHS
```

汇总的核心外设时钟映射（Aggregated Core Peripheral Clock Mappings）。

本宏展开为时钟控制实现（Clock Control Implementation）所使用的全部核心外设的映射。

<a id="ad32629d31a567d5d134e421cd527253a"></a>

### `AMEBA_FLASH_CLK`

```c
#define AMEBA_FLASH_CLK 16
```

SoC 域（Domain）中的闪存时钟（Flash Clock）。

<a id="a9f7681b1b804b2d916095739bd45825b"></a>

### `AMEBA_FLASH_PERIPHS`

```c
#define AMEBA_FLASH_PERIPHS AMEBA_REMAP_PERIPH(AMEBA_FLASH_CLK, NULL)
```

闪存时钟外设映射（Flash Clock Peripheral Mapping）。

<a id="ae0ec3320a2378824f3af9c4aaed9689f"></a>

### `AMEBA_GDMA0_CLK`

```c
#define AMEBA_GDMA0_CLK 13
```

SoC 域（Domain）中的 GDMA0 时钟（Clock）。

<a id="a81a24118682991a81a7de59501e5812b"></a>

### `AMEBA_GDMA0_PERIPHS`

```c
#define AMEBA_GDMA0_PERIPHS AMEBA_SINGLE_PERIPH(GDMA0) /* AMEBA_GDMA0_CLK */
```

GDMA0 时钟外设映射（Clock Peripheral Mapping）。

<a id="a060a938a705823c18de0ce9133c0a99d"></a>

### `AMEBA_GPIO_CLK`

```c
#define AMEBA_GPIO_CLK 7
```

SYSON 域（Domain）中的 GPIO 时钟（Clock）。

<a id="af7bbf5921d40aed8bb5c92e38b8f5987"></a>

### `AMEBA_GPIO_PERIPHS`

```c
#define AMEBA_GPIO_PERIPHS AMEBA_REMAP_PERIPH(AMEBA_GPIO_CLK, NULL)
```

GPIO 时钟外设映射（Clock Peripheral Mapping）。

<a id="ac293b0216f849f4bffd50253b0df9fd7"></a>

### `AMEBA_I2C0_CLK`

```c
#define AMEBA_I2C0_CLK 18
```

SoC 域（Domain）中的 I2C0 时钟（Clock）。

<a id="ab55bb29f8a5c2a0fd1dba45d0c9f4910"></a>

### `AMEBA_I2C_PERIPHS`

```c
#define AMEBA_I2C_PERIPHS AMEBA_NUMERICAL_PERIPH(I2C, 0) /* AMEBA_I2C0_CLK */
```

I2C 时钟外设映射（Clock Peripheral Mappings）。

<a id="a996962b9c7b1dd32421226bde07184c1"></a>

### `AMEBA_LOGUART_CLK`

```c
#define AMEBA_LOGUART_CLK 4
```

SYSON 域（Domain）中的 LOGUART 时钟（Clock）。

<a id="a1020076bac0b7d227c73d4482c95ebd0"></a>

### `AMEBA_LOGUART_PERIPHS`

```c
#define AMEBA_LOGUART_PERIPHS AMEBA_REMAP_PERIPH(AMEBA_LOGUART_CLK, NULL)
```

LOGUART 时钟外设映射（Clock Peripheral Mapping）。

待办（TODO）：在 KM0 中启用。

<a id="ab3149be5245573521f4bb7e551e625e7"></a>

### `AMEBA_LTIM0_CLK`

```c
#define AMEBA_LTIM0_CLK 8
```

SYSON 域（Domain）中的 LTIM0 时钟（Clock）。

<a id="a776ea52d9a1f082f7037bd2b01a0d4bb"></a>

### `AMEBA_LTIM1_CLK`

```c
#define AMEBA_LTIM1_CLK 9
```

SYSON 域（Domain）中的 LTIM1 时钟（Clock）。

<a id="a832779b2dc473e221ba4a4b813807dbc"></a>

### `AMEBA_LTIM2_CLK`

```c
#define AMEBA_LTIM2_CLK 10
```

SYSON 域（Domain）中的 LTIM2 时钟（Clock）。

<a id="a371d8e766d052283c390868989cc9283"></a>

### `AMEBA_LTIM3_CLK`

```c
#define AMEBA_LTIM3_CLK 11
```

SYSON 域（Domain）中的 LTIM3 时钟（Clock）。

<a id="a89ef5e4da90cb6459240ea4f998c61c5"></a>

### `AMEBA_LTIM_PERIPHS`

```c
#define AMEBA_LTIM_PERIPHS
```

展开值（Value）：

```c
AMEBA_REMAP_PERIPH(AMEBA_LTIM0_CLK, GTIMER)                                        \
AMEBA_REMAP_PERIPH(AMEBA_LTIM1_CLK, GTIMER)                                        \
AMEBA_REMAP_PERIPH(AMEBA_LTIM2_CLK, GTIMER)                                        \
AMEBA_REMAP_PERIPH(AMEBA_LTIM3_CLK, GTIMER)
```

LTIM 时钟到 GTIMER 外设的映射（Clock Mapping）。

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

<a id="a23f2311464ddfe56f20e91fad94c5492"></a>

### `AMEBA_PERI_HCLK`

```c
#define AMEBA_PERI_HCLK 12
```

SoC 域（Domain）中的外设 HCLK（Peripheral HCLK）。

<a id="a37db8ed6566f8d47b4e6c1e3a536775d"></a>

### `AMEBA_PRNG_CLK`

```c
#define AMEBA_PRNG_CLK 19
```

SoC 域（Domain）中的 PRNG 时钟（Clock）。

<a id="a59abad25eab1eab1dc5b97055ed140a4"></a>

### `AMEBA_PRNG_PERIPHS`

```c
#define AMEBA_PRNG_PERIPHS AMEBA_REMAP_PERIPH(AMEBA_PRNG_CLK, NULL)
```

PRNG 时钟外设映射（Clock Peripheral Mapping）。

<a id="a2d6f84861d9ceff804149347a06e796b"></a>

### `AMEBA_PSRAM_CLK`

```c
#define AMEBA_PSRAM_CLK 17
```

SoC 域（Domain）中的 PSRAM 时钟（Clock）。

<a id="ae0fb2795cbc68a3c66aaff30bb47d77d"></a>

### `AMEBA_PSRAM_PERIPHS`

```c
#define AMEBA_PSRAM_PERIPHS AMEBA_SINGLE_PERIPH(PSRAM) /* AMEBA_PSRAM_CLK */
```

PSRAM 时钟外设映射（Clock Peripheral Mapping）。

<a id="a523f7ac5827b17a56f7940c18481abb8"></a>

### `AMEBA_PWM0_CLK`

```c
#define AMEBA_PWM0_CLK 2
```

SYSON 域（Domain）中的 PWM0 时钟（Clock）。

<a id="a7a3e89aeca0afde7c5c5350e75f289eb"></a>

### `AMEBA_PWM_PERIPHS`

```c
#define AMEBA_PWM_PERIPHS AMEBA_REMAP_PERIPH(AMEBA_PWM0_CLK, GTIMER)
```

PWM 时钟到 GTIMER 外设的映射（Clock Mapping）。

<a id="a19d44435f2d7130c8ab41c13df6972f8"></a>

### `AMEBA_REMAP_PERIPH`

```c
#define AMEBA_REMAP_PERIPH ( clk_index, remap_name )
```

展开值（Value）：

```c
[clk_index] = {                                                                    \
        .parent = AMEBA_RCC_NO_PARENT,                                             \
        .cke = APBPeriph_##remap_name##_CLOCK,                                     \
        .fen = APBPeriph_##remap_name,                                             \
},
```

为名称经过重映射的外设定义时钟条目（Clock Entry）。

用于时钟索引（Clock Index）映射到另一外设名称的情形。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `clk_index` | 时钟索引（Clock Index）。 |
| `remap_name` | 目标外设名称（Target Peripheral Name）。 |

<a id="a9f089feea64d395b53ec91451346889d"></a>

### `AMEBA_RTC_CLK`

```c
#define AMEBA_RTC_CLK 1
```

AON 域（Domain）中的 RTC 时钟（Clock）。

<a id="a5d786480113fc750e578c92f33ae09cb"></a>

### `AMEBA_RTC_PERIPHS`

```c
#define AMEBA_RTC_PERIPHS AMEBA_SINGLE_PERIPH(RTC) /* AMEBA_RTC_CLK */
```

RTC 时钟外设映射（Clock Peripheral Mapping）。

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

用于只有一个实例的外设（Peripheral），例如 GDMA0、PSRAM、RTC。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 外设名称（Peripheral Name）。 |

<a id="a44689e534b5693fe964e45f04ec3af3a"></a>

### `AMEBA_SPI0_CLK`

```c
#define AMEBA_SPI0_CLK 14
```

SoC 域（Domain）中的 SPI0 时钟（Clock）。

<a id="a1997336af677a35e15d1402aed065ee6"></a>

### `AMEBA_SPI1_CLK`

```c
#define AMEBA_SPI1_CLK 15
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

<a id="a36ebf3e1fd6ac0092aab3589d14d20b3"></a>

### `AMEBA_UART0_CLK`

```c
#define AMEBA_UART0_CLK 3
```

SYSON 域（Domain）中的 UART0 时钟（Clock）。

<a id="a820d2fec9e6e7a757335cb97e5748f06"></a>

### `AMEBA_UART3_CLK`

```c
#define AMEBA_UART3_CLK 5
```

SYSON 域（Domain）中的 UART3 时钟（Clock）。

<a id="a7b90187464653d7b1e83e0fd01c21e2f"></a>

### `AMEBA_UART_PERIPHS`

```c
#define AMEBA_UART_PERIPHS
```

展开值（Value）：

```c
AMEBA_NUMERICAL_PERIPH(UART, 0) /* AMEBA_UART0_CLK */                              \
AMEBA_NUMERICAL_PERIPH(UART, 3) /* AMEBA_UART3_CLK */
```

UART 时钟外设映射（Clock Peripheral Mappings）。

<a id="ae499eda9d017f36f20baa4007166fd5e"></a>

### `APBPeriph_NULL_CLOCK`

```c
#define APBPeriph_NULL_CLOCK APBPeriph_CLOCK_NULL
```

空 APB 外设时钟定义（Null APB Peripheral Clock Definition）。

用作无效或未使用的 APB 时钟的占位符（Placeholder）。


## 2.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_transport_clock_reference/P001_amebad_clock.h_源码浏览.md)
- [max](../numeric_reference/P001_最小最大值与限幅宏参考.md#affe776513b24d84b39af8ab0930fef7f)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="aamebad__clock_8h_html_a19d44435f2d7130c8ab41c13df6972f8"></a>
<a id="aamebad__clock_8h_html_a371d8e766d052283c390868989cc9283"></a>
<a id="aamebad__clock_8h_html_a776ea52d9a1f082f7037bd2b01a0d4bb"></a>
<a id="aamebad__clock_8h_html_a832779b2dc473e221ba4a4b813807dbc"></a>
<a id="aamebad__clock_8h_html_ab3149be5245573521f4bb7e551e625e7"></a>
<a id="aamebad__clock_8h_html_a5892f2668cc892817f59230643162ee4"></a>

---

[上一章](P001_zephyr__dt-bindings__clock__alif-clocks-common.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P003_zephyr__dt-bindings__clock__amebadplus_clock.h_文件参考.md)
