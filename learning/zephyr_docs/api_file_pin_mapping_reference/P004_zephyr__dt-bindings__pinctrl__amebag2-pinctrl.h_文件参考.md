---
id: learning.zephyr-docs.api-file-pin-mapping-reference.page-4
title: zephyr__dt-bindings__pinctrl__amebag2-pinctrl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/amebag2-pinctrl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_amebag2-pinctrl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/amebag2-pinctrl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Realtek AmebaG2的引脚控制设备树绑定（Pinctrl Devicetree Bindings）。

查看此文件的源码。

<a id="details"></a>

Realtek AmebaG2的引脚控制设备树绑定（Pinctrl Devicetree Bindings）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 4.1\_宏定义（Macros）

<a id="r_a01f0e522a7c41526681b766c7ac7ce1f"></a>

```c
#define AMEBA_PORT_PIN(port, line)
```

相关声明：[AMEBA_PORT_PIN](#a01f0e522a7c41526681b766c7ac7ce1f)。

编码端口（Port）和引脚编号（Pin Number）。

<a id="r_a71d265adf87eb5aa7e991bf0dd6c142f"></a>

```c
#define AMEBA_PINMUX(port, line, funcid)
```

相关声明：[AMEBA_PINMUX](#a71d265adf87eb5aa7e991bf0dd6c142f)。

编码引脚复用配置（Pinmux Configuration）。

<a id="define-members-0"></a>

### 引脚复用功能定义（Pinmux Function Definitions）

<a id="r_a1a770820da1c7f81c4925cd6a6fab8f4"></a>

```c
#define AMEBA_GPIO 0
```

相关声明：[AMEBA_GPIO](#a1a770820da1c7f81c4925cd6a6fab8f4)。

GPIO 功能（GPIO Function）。

<a id="r_a43b82c67e7ed46c4d7504354b89766a2"></a>

```c
#define AMEBA_LOG_UART 1
```

相关声明：[AMEBA_LOG_UART](#a43b82c67e7ed46c4d7504354b89766a2)。

日志 UART 功能（Log UART Function）。

<a id="r_add660cc0a513fed62fe5d5e2ec12e5a7"></a>

```c
#define AMEBA_SPIC0_FLASH 2
```

相关声明：[AMEBA_SPIC0_FLASH](#add660cc0a513fed62fe5d5e2ec12e5a7)。

SPIC0 闪存 功能（SPIC0 Flash Function）。

<a id="r_a5eb4f7828f8f9aab06d02ba35f4daf6f"></a>

```c
#define AMEBA_SPIC1_FLASH 3
```

相关声明：[AMEBA_SPIC1_FLASH](#a5eb4f7828f8f9aab06d02ba35f4daf6f)。

SPIC1 闪存 功能（SPIC1 Flash Function）。

<a id="r_a97aa1778f7670f03bc30a9cc156c3da1"></a>

```c
#define AMEBA_SPIC1_PSRAM 4
```

相关声明：[AMEBA_SPIC1_PSRAM](#a97aa1778f7670f03bc30a9cc156c3da1)。

SPIC1 PSRAM 功能（SPIC1 PSRAM Function）。

<a id="r_acb023403125750639b0d02171607c2ad"></a>

```c
#define AMEBA_ADC 5
```

相关声明：[AMEBA_ADC](#acb023403125750639b0d02171607c2ad)。

ADC 功能（ADC Function）。

<a id="r_a1eeebd2f73559939b681db6e912def28"></a>

```c
#define AMEBA_CAP_TOUCH 5
```

相关声明：[AMEBA_CAP_TOUCH](#a1eeebd2f73559939b681db6e912def28)。

电容触摸 功能（Cap touch Function）。

<a id="r_aee7136959068c9606180a95716bed0ac"></a>

```c
#define AMEBA_TSSI 6
```

相关声明：[AMEBA_TSSI](#aee7136959068c9606180a95716bed0ac)。

TSSI 功能（TSSI Function）。

<a id="r_adfeeeb74cd0157b09992ec5e5f4e5397"></a>

```c
#define AMEBA_USB 7
```

相关声明：[AMEBA_USB](#adfeeeb74cd0157b09992ec5e5f4e5397)。

USB 功能（USB Function）。

<a id="r_aa2b51dc869def95632ff6cb06bcfd9f7"></a>

```c
#define AMEBA_RMII 8
```

相关声明：[AMEBA_RMII](#aa2b51dc869def95632ff6cb06bcfd9f7)。

RMII 功能（RMII Function）。

<a id="r_a83fa3b6f04ec93e0d9c31a7f9d7bf1d8"></a>

```c
#define AMEBA_SPI0 9
```

相关声明：[AMEBA_SPI0](#a83fa3b6f04ec93e0d9c31a7f9d7bf1d8)。

SPI0 功能（SPI0 Function）。

<a id="r_a428dd6e6aba093c0553141dd15c88c3c"></a>

```c
#define AMEBA_SPI1 10
```

相关声明：[AMEBA_SPI1](#a428dd6e6aba093c0553141dd15c88c3c)。

SPI1 功能（SPI1 Function）。

<a id="r_a0d8fdf8ef3539a8cfe2b6e57f8e5db8d"></a>

```c
#define AMEBA_SWD 11
```

相关声明：[AMEBA_SWD](#a0d8fdf8ef3539a8cfe2b6e57f8e5db8d)。

SWD 功能（SWD Function）。

<a id="r_ad454ea614c16b6b153df1ec4d135ed44"></a>

```c
#define AMEBA_SDIO_MST 12
```

相关声明：[AMEBA_SDIO_MST](#ad454ea614c16b6b153df1ec4d135ed44)。

SDIO 主机 功能（SDIO Master Function）。

<a id="r_a073da65535e6499cebdefd70812fc9eb"></a>

```c
#define AMEBA_SDIO_SLV 13
```

相关声明：[AMEBA_SDIO_SLV](#a073da65535e6499cebdefd70812fc9eb)。

SDIO 从机 功能（SDIO Slave Function）。

<a id="r_aafdc733867a4ab1a0d16429679b19cba"></a>

```c
#define AMEBA_SIC 14
```

相关声明：[AMEBA_SIC](#aafdc733867a4ab1a0d16429679b19cba)。

SIC 功能（SIC Function）。

<a id="r_a6808b0d69603d73741df35aa2ccf9166"></a>

```c
#define AMEBA_BT_IO 15
```

相关声明：[AMEBA_BT_IO](#a6808b0d69603d73741df35aa2ccf9166)。

BT IO 功能（BT IO Function）。

<a id="r_a71f0921f7c7ccd5e272cb66733dfa994"></a>

```c
#define AMEBA_BT 16
```

相关声明：[AMEBA_BT](#a71f0921f7c7ccd5e272cb66733dfa994)。

BT 功能（BT Function）。

<a id="r_a98d7af9e28bf21c740207cffde3550db"></a>

```c
#define AMEBA_DEBUG 17
```

相关声明：[AMEBA_DEBUG](#a98d7af9e28bf21c740207cffde3550db)。

调试 功能（Debug Function）。

<a id="r_a24a9be29f490ac4b2425b8f0c96fd0f9"></a>

```c
#define AMEBA_I2S0_BCLK 32
```

相关声明：[AMEBA_I2S0_BCLK](#a24a9be29f490ac4b2425b8f0c96fd0f9)。

I2S0 BCLK 功能（I2S0 BCLK Function）。

<a id="r_a712d64cdb749070056bd158553370eae"></a>

```c
#define AMEBA_I2S0_MCLK 33
```

相关声明：[AMEBA_I2S0_MCLK](#a712d64cdb749070056bd158553370eae)。

I2S0 MCLK 功能（I2S0 MCLK Function）。

<a id="r_a51d16562267051569c14c05358115cb4"></a>

```c
#define AMEBA_I2S0_WS 34
```

相关声明：[AMEBA_I2S0_WS](#a51d16562267051569c14c05358115cb4)。

I2S0 WS 功能（I2S0 WS Function）。

<a id="r_ac224c5d98fcda932f1dd56e119ea8c8f"></a>

```c
#define AMEBA_I2S0_DIO0 35
```

相关声明：[AMEBA_I2S0_DIO0](#ac224c5d98fcda932f1dd56e119ea8c8f)。

I2S0 DIO0 功能（I2S0 DIO0 Function）。

<a id="r_a6d15583c82ed66abfd8879cd1b83bc85"></a>

```c
#define AMEBA_I2S0_DIO1 36
```

相关声明：[AMEBA_I2S0_DIO1](#a6d15583c82ed66abfd8879cd1b83bc85)。

I2S0 DIO1 功能（I2S0 DIO1 Function）。

<a id="r_a167ee959e13888da0a0a6aff7620f756"></a>

```c
#define AMEBA_I2S0_DIO2 37
```

相关声明：[AMEBA_I2S0_DIO2](#a167ee959e13888da0a0a6aff7620f756)。

I2S0 DIO2 功能（I2S0 DIO2 Function）。

<a id="r_a430fc7f6f6e9703f7fb425b173d5fd6c"></a>

```c
#define AMEBA_I2S0_DIO3 38
```

相关声明：[AMEBA_I2S0_DIO3](#a430fc7f6f6e9703f7fb425b173d5fd6c)。

I2S0 DIO3 功能（I2S0 DIO3 Function）。

<a id="r_aeb425651bfda5d70a67b31d9ff993ce6"></a>

```c
#define AMEBA_LCD_RGB_DCLK 39
```

相关声明：[AMEBA_LCD_RGB_DCLK](#aeb425651bfda5d70a67b31d9ff993ce6)。

LCD RGB DCLK 功能（LCD RGB DCLK Function）。

<a id="r_a74e42f027f3c4d2fdccc5216439bebfd"></a>

```c
#define AMEBA_LCD_MCU_WR 39
```

相关声明：[AMEBA_LCD_MCU_WR](#a74e42f027f3c4d2fdccc5216439bebfd)。

LCD MCU WR 功能（LCD MCU WR Function）。

<a id="r_a4733ac89dec3ce6b414bd3f723613423"></a>

```c
#define AMEBA_LCD_RGB_DE 40
```

相关声明：[AMEBA_LCD_RGB_DE](#a4733ac89dec3ce6b414bd3f723613423)。

LCD RGB DE 功能（LCD RGB DE Function）。

<a id="r_a67ebf980b33b1eb7edb396e15414f789"></a>

```c
#define AMEBA_LCD_MCU_CSX 40
```

相关声明：[AMEBA_LCD_MCU_CSX](#a67ebf980b33b1eb7edb396e15414f789)。

LCD MCU CSX 功能（LCD MCU CSX Function）。

<a id="r_a4c640e0e2cff9f3c58d94b1a7295ff5a"></a>

```c
#define AMEBA_LCD_RGB_HSYNC 41
```

相关声明：[AMEBA_LCD_RGB_HSYNC](#a4c640e0e2cff9f3c58d94b1a7295ff5a)。

LCD RGB HSYNC 功能（LCD RGB HSYNC Function）。

<a id="r_a7cd81428627c9112288ab7a6bce3add0"></a>

```c
#define AMEBA_LCD_MCU_RD 41
```

相关声明：[AMEBA_LCD_MCU_RD](#a7cd81428627c9112288ab7a6bce3add0)。

LCD MCU RD 功能（LCD MCU RD Function）。

<a id="r_a26033b3b3357c9f4a946e8f374a59c93"></a>

```c
#define AMEBA_LCD_RGB_TE 42
```

相关声明：[AMEBA_LCD_RGB_TE](#a26033b3b3357c9f4a946e8f374a59c93)。

LCD RGB TE 功能（LCD RGB TE Function）。

<a id="r_ac8eee74cbade1b05f9ade91f8be7289e"></a>

```c
#define AMEBA_LCD_MCU_TE 42
```

相关声明：[AMEBA_LCD_MCU_TE](#ac8eee74cbade1b05f9ade91f8be7289e)。

LCD MCU TE 功能（LCD MCU TE Function）。

<a id="r_a03c6b203d24c41dc0d586878404b7a10"></a>

```c
#define AMEBA_LCD_RGB_VSYNC 43
```

相关声明：[AMEBA_LCD_RGB_VSYNC](#a03c6b203d24c41dc0d586878404b7a10)。

LCD RGB VSYNC 功能（LCD RGB VSYNC Function）。

<a id="r_a4747387279e003279756db7395680c3d"></a>

```c
#define AMEBA_LCD_MCU_VSYNC 43
```

相关声明：[AMEBA_LCD_MCU_VSYNC](#a4747387279e003279756db7395680c3d)。

LCD MCU VSYNC 功能（LCD MCU VSYNC Function）。

<a id="r_a7884bd076393839950198adb7fe8d766"></a>

```c
#define AMEBA_LCD_MCU_DCX 44
```

相关声明：[AMEBA_LCD_MCU_DCX](#a7884bd076393839950198adb7fe8d766)。

LCD MCU DCX 功能（LCD MCU DCX Function）。

<a id="r_a522133bb5b0c6febe4ea66506a4b1a87"></a>

```c
#define AMEBA_LCD_D0 45
```

相关声明：[AMEBA_LCD_D0](#a522133bb5b0c6febe4ea66506a4b1a87)。

LCD D0 功能（LCD D0 Function）。

<a id="r_a4823b1d9d83c32705a25f108ba017409"></a>

```c
#define AMEBA_LCD_D1 46
```

相关声明：[AMEBA_LCD_D1](#a4823b1d9d83c32705a25f108ba017409)。

LCD D1 功能（LCD D1 Function）。

<a id="r_a61b5ceec7d442cc66041b3c6b802ca21"></a>

```c
#define AMEBA_LCD_D2 47
```

相关声明：[AMEBA_LCD_D2](#a61b5ceec7d442cc66041b3c6b802ca21)。

LCD D2 功能（LCD D2 Function）。

<a id="r_a07c845ba6b75e8c2ab5aba37601f1683"></a>

```c
#define AMEBA_LCD_D3 48
```

相关声明：[AMEBA_LCD_D3](#a07c845ba6b75e8c2ab5aba37601f1683)。

LCD D3 功能（LCD D3 Function）。

<a id="r_a32e6399fffd99f6987df5583b9cc9a47"></a>

```c
#define AMEBA_LCD_D4 49
```

相关声明：[AMEBA_LCD_D4](#a32e6399fffd99f6987df5583b9cc9a47)。

LCD D4 功能（LCD D4 Function）。

<a id="r_aa555f1c733a42d9507c9a96dfb187929"></a>

```c
#define AMEBA_LCD_D5 50
```

相关声明：[AMEBA_LCD_D5](#aa555f1c733a42d9507c9a96dfb187929)。

LCD D5 功能（LCD D5 Function）。

<a id="r_a3bf439831ceafadcd790046b4bf9330d"></a>

```c
#define AMEBA_LCD_D6 51
```

相关声明：[AMEBA_LCD_D6](#a3bf439831ceafadcd790046b4bf9330d)。

LCD D6 功能（LCD D6 Function）。

<a id="r_ab54a5c4ccf324e8219dfbd8ced921935"></a>

```c
#define AMEBA_LCD_D7 52
```

相关声明：[AMEBA_LCD_D7](#ab54a5c4ccf324e8219dfbd8ced921935)。

LCD D7 功能（LCD D7 Function）。

<a id="r_a9cb563e0a3071f12726146ff4d421b38"></a>

```c
#define AMEBA_LCD_D8 53
```

相关声明：[AMEBA_LCD_D8](#a9cb563e0a3071f12726146ff4d421b38)。

LCD D8 功能（LCD D8 Function）。

<a id="r_a249d2a18cdaf957777075fa5a8b5866d"></a>

```c
#define AMEBA_LCD_D9 54
```

相关声明：[AMEBA_LCD_D9](#a249d2a18cdaf957777075fa5a8b5866d)。

LCD D9 功能（LCD D9 Function）。

<a id="r_afa69b39698293897870b9b5a059a8a5b"></a>

```c
#define AMEBA_LCD_D10 55
```

相关声明：[AMEBA_LCD_D10](#afa69b39698293897870b9b5a059a8a5b)。

LCD D10 功能（LCD D10 Function）。

<a id="r_aa03bee3a3fa1833aa9ca390332f3f090"></a>

```c
#define AMEBA_LCD_D11 56
```

相关声明：[AMEBA_LCD_D11](#aa03bee3a3fa1833aa9ca390332f3f090)。

LCD D11 功能（LCD D11 Function）。

<a id="r_aabe467e62f38135cd57f230c3a4170b0"></a>

```c
#define AMEBA_LCD_D12 57
```

相关声明：[AMEBA_LCD_D12](#aabe467e62f38135cd57f230c3a4170b0)。

LCD D12 功能（LCD D12 Function）。

<a id="r_a003b0dbf7f5a6566ed601bcf2b7667a7"></a>

```c
#define AMEBA_LCD_D13 58
```

相关声明：[AMEBA_LCD_D13](#a003b0dbf7f5a6566ed601bcf2b7667a7)。

LCD D13 功能（LCD D13 Function）。

<a id="r_a11f6d88a06999e17ef85c3f6d00abe5a"></a>

```c
#define AMEBA_LCD_D14 59
```

相关声明：[AMEBA_LCD_D14](#a11f6d88a06999e17ef85c3f6d00abe5a)。

LCD D14 功能（LCD D14 Function）。

<a id="r_af6af66abdbef26731863b9a39c9d8c73"></a>

```c
#define AMEBA_LCD_D15 60
```

相关声明：[AMEBA_LCD_D15](#af6af66abdbef26731863b9a39c9d8c73)。

LCD D15 功能（LCD D15 Function）。

<a id="r_a6538dedaeda74bea11dcc0ce1dc3b489"></a>

```c
#define AMEBA_LCD_D16 61
```

相关声明：[AMEBA_LCD_D16](#a6538dedaeda74bea11dcc0ce1dc3b489)。

LCD D16 功能（LCD D16 Function）。

<a id="r_a24209ab9d918529a909a475dcac4329d"></a>

```c
#define AMEBA_LCD_D17 62
```

相关声明：[AMEBA_LCD_D17](#a24209ab9d918529a909a475dcac4329d)。

LCD D17 功能（LCD D17 Function）。

<a id="r_a58d51bcd1c04166df3452a75d54b2232"></a>

```c
#define AMEBA_LCD_D18 63
```

相关声明：[AMEBA_LCD_D18](#a58d51bcd1c04166df3452a75d54b2232)。

LCD D18 功能（LCD D18 Function）。

<a id="r_a3e0bf2ec675e3c723927ed1ccd76c24a"></a>

```c
#define AMEBA_LCD_D19 64
```

相关声明：[AMEBA_LCD_D19](#a3e0bf2ec675e3c723927ed1ccd76c24a)。

LCD D19 功能（LCD D19 Function）。

<a id="r_a7bf6d2c2fa4fcd4f6547eb2430626070"></a>

```c
#define AMEBA_LCD_D20 65
```

相关声明：[AMEBA_LCD_D20](#a7bf6d2c2fa4fcd4f6547eb2430626070)。

LCD D20 功能（LCD D20 Function）。

<a id="r_a0589309be4f51562dd98342d59ef4de1"></a>

```c
#define AMEBA_LCD_D21 66
```

相关声明：[AMEBA_LCD_D21](#a0589309be4f51562dd98342d59ef4de1)。

LCD D21 功能（LCD D21 Function）。

<a id="r_a4f080cb41949b5f6f5d24d735ad9ac3e"></a>

```c
#define AMEBA_LCD_D22 67
```

相关声明：[AMEBA_LCD_D22](#a4f080cb41949b5f6f5d24d735ad9ac3e)。

LCD D22 功能（LCD D22 Function）。

<a id="r_a7008524284eed0ce1011022f830c6f22"></a>

```c
#define AMEBA_LCD_D23 68
```

相关声明：[AMEBA_LCD_D23](#a7008524284eed0ce1011022f830c6f22)。

LCD D23 功能（LCD D23 Function）。

<a id="r_a39c84a6ed19b96cc4980d31f557c493c"></a>

```c
#define AMEBA_SD_M_CLK 69
```

相关声明：[AMEBA_SD_M_CLK](#a39c84a6ed19b96cc4980d31f557c493c)。

SD 主机 CLK 功能（SD Master CLK Function）。

<a id="r_ae46eb76cd70842fb715b75d8269034d8"></a>

```c
#define AMEBA_SD_M_CMD 70
```

相关声明：[AMEBA_SD_M_CMD](#ae46eb76cd70842fb715b75d8269034d8)。

SD 主机 CMD 功能（SD Master CMD Function）。

<a id="r_a92352131ed031d614fe21d6ca22371ba"></a>

```c
#define AMEBA_SD_M_D0 71
```

相关声明：[AMEBA_SD_M_D0](#a92352131ed031d614fe21d6ca22371ba)。

SD 主机 D0 功能（SD Master D0 Function）。

<a id="r_a5570335f0e6b73bad8b4a664a9a8de80"></a>

```c
#define AMEBA_SD_M_D1 72
```

相关声明：[AMEBA_SD_M_D1](#a5570335f0e6b73bad8b4a664a9a8de80)。

SD 主机 D1 功能（SD Master D1 Function）。

<a id="r_a5525b6c4902920e81b0106ce570427c8"></a>

```c
#define AMEBA_SD_M_D2 73
```

相关声明：[AMEBA_SD_M_D2](#a5525b6c4902920e81b0106ce570427c8)。

SD 主机 D2 功能（SD Master D2 Function）。

<a id="r_a7fb12e214c0c750f019caa5998c2db43"></a>

```c
#define AMEBA_SD_M_D3 74
```

相关声明：[AMEBA_SD_M_D3](#a7fb12e214c0c750f019caa5998c2db43)。

SD 主机 D3 功能（SD Master D3 Function）。

<a id="r_a44689e534b5693fe964e45f04ec3af3a"></a>

```c
#define AMEBA_SPI0_CLK 75
```

相关声明：[AMEBA_SPI0_CLK](#a44689e534b5693fe964e45f04ec3af3a)。

SPI0 CLK 功能（SPI0 CLK Function）。

<a id="r_a2567e8fa1c77f607059df8a0d4e7b4a6"></a>

```c
#define AMEBA_SPI0_MISO 76
```

相关声明：[AMEBA_SPI0_MISO](#a2567e8fa1c77f607059df8a0d4e7b4a6)。

SPI0 MISO 功能（SPI0 MISO Function）。

<a id="r_a39e2d93a67ddf5a86546681800896466"></a>

```c
#define AMEBA_SPI0_MOSI 77
```

相关声明：[AMEBA_SPI0_MOSI](#a39e2d93a67ddf5a86546681800896466)。

SPI0 MOSI 功能（SPI0 MOSI Function）。

<a id="r_a6acad25a5a57a0199ee5ce1612862f26"></a>

```c
#define AMEBA_SPI0_CS 78
```

相关声明：[AMEBA_SPI0_CS](#a6acad25a5a57a0199ee5ce1612862f26)。

SPI0 CS 功能（SPI0 CS Function）。

<a id="r_a1997336af677a35e15d1402aed065ee6"></a>

```c
#define AMEBA_SPI1_CLK 79
```

相关声明：[AMEBA_SPI1_CLK](#a1997336af677a35e15d1402aed065ee6)。

SPI1 CLK 功能（SPI1 CLK Function）。

<a id="r_ab40628d9a44f82362da70ab685c41cee"></a>

```c
#define AMEBA_SPI1_MISO 80
```

相关声明：[AMEBA_SPI1_MISO](#ab40628d9a44f82362da70ab685c41cee)。

SPI1 MISO 功能（SPI1 MISO Function）。

<a id="r_ab9a8e9f5f8c3160a04998960c61e8b4d"></a>

```c
#define AMEBA_SPI1_MOSI 81
```

相关声明：[AMEBA_SPI1_MOSI](#ab9a8e9f5f8c3160a04998960c61e8b4d)。

SPI1 MOSI 功能（SPI1 MOSI Function）。

<a id="r_a9113912d0b976fd5539fbd003e83d85f"></a>

```c
#define AMEBA_SPI1_CS 82
```

相关声明：[AMEBA_SPI1_CS](#a9113912d0b976fd5539fbd003e83d85f)。

SPI1 CS 功能（SPI1 CS Function）。

<a id="r_a467cc815f93d3f13a2329e7ff5ee5ef4"></a>

```c
#define AMEBA_SWD_CLK 83
```

相关声明：[AMEBA_SWD_CLK](#a467cc815f93d3f13a2329e7ff5ee5ef4)。

SWD CLK 功能（SWD CLK Function）。

<a id="r_aef189b30132fe99c6410a9067570dd74"></a>

```c
#define AMEBA_SWD_DAT 84
```

相关声明：[AMEBA_SWD_DAT](#aef189b30132fe99c6410a9067570dd74)。

SWD DAT 功能（SWD DAT Function）。

<a id="r_a5544c01a480ae8ab721f846aedeac3a2"></a>

```c
#define AMEBA_DMIC_CLK 85
```

相关声明：[AMEBA_DMIC_CLK](#a5544c01a480ae8ab721f846aedeac3a2)。

DMIC CLK 功能（DMIC CLK Function）。

<a id="r_ac8a69ac2c1bfea15838a8a5da7ea3d1b"></a>

```c
#define AMEBA_DMIC_DATA 86
```

相关声明：[AMEBA_DMIC_DATA](#ac8a69ac2c1bfea15838a8a5da7ea3d1b)。

DMIC DATA 功能（DMIC DATA Function）。

<a id="r_abc19934502147fb9f1bd455edbe99c6f"></a>

```c
#define AMEBA_LED_SCL 87
```

相关声明：[AMEBA_LED_SCL](#abc19934502147fb9f1bd455edbe99c6f)。

LED SCL 功能（LED SCL Function）。

<a id="r_a0076f516b73ad3761de70f1a88d7747f"></a>

```c
#define AMEBA_LED_SDA 88
```

相关声明：[AMEBA_LED_SDA](#a0076f516b73ad3761de70f1a88d7747f)。

LED SDA 功能（LED SDA Function）。

<a id="r_a45b715ce9be8df9c8693cb4349b7f0da"></a>

```c
#define AMEBA_I2C0_SCL 89
```

相关声明：[AMEBA_I2C0_SCL](#a45b715ce9be8df9c8693cb4349b7f0da)。

I2C0 SCL 功能（I2C0 SCL Function）。

<a id="r_a1adbe2f3d191e115cd29c73b8d726272"></a>

```c
#define AMEBA_I2C0_SDA 90
```

相关声明：[AMEBA_I2C0_SDA](#a1adbe2f3d191e115cd29c73b8d726272)。

I2C0 SDA 功能（I2C0 SDA Function）。

<a id="r_a6cd3bf525d23b4224b1238d3b0c5fcde"></a>

```c
#define AMEBA_I2C1_SCL 91
```

相关声明：[AMEBA_I2C1_SCL](#a6cd3bf525d23b4224b1238d3b0c5fcde)。

I2C1 SCL 功能（I2C1 SCL Function）。

<a id="r_a88e9123211493809fdd23078928905de"></a>

```c
#define AMEBA_I2C1_SDA 92
```

相关声明：[AMEBA_I2C1_SDA](#a88e9123211493809fdd23078928905de)。

I2C1 SDA 功能（I2C1 SDA Function）。

<a id="r_aeb3029bd84e2ba794cc3e4c9239a4427"></a>

```c
#define AMEBA_RMII_MDIO 93
```

相关声明：[AMEBA_RMII_MDIO](#aeb3029bd84e2ba794cc3e4c9239a4427)。

RMII MDIO 功能（RMII MDIO Function）。

<a id="r_a69b87577f31c6a8516c8790724390dc9"></a>

```c
#define AMEBA_RMII_MDC 94
```

相关声明：[AMEBA_RMII_MDC](#a69b87577f31c6a8516c8790724390dc9)。

RMII MDC 功能（RMII MDC Function）。

<a id="r_a74d6af9b061345287512018abbe6cdc0"></a>

```c
#define AMEBA_UART0_TXD 95
```

相关声明：[AMEBA_UART0_TXD](#a74d6af9b061345287512018abbe6cdc0)。

UART0 TXD 功能（UART0 TXD Function）。

<a id="r_aa93af39fe6c222c908a7642f5a4349a8"></a>

```c
#define AMEBA_UART0_RXD 96
```

相关声明：[AMEBA_UART0_RXD](#aa93af39fe6c222c908a7642f5a4349a8)。

UART0 RXD 功能（UART0 RXD Function）。

<a id="r_aec676f180cd6c8ebde85b78984953106"></a>

```c
#define AMEBA_UART0_CTS 97
```

相关声明：[AMEBA_UART0_CTS](#aec676f180cd6c8ebde85b78984953106)。

UART0 CTS 功能（UART0 CTS Function）。

<a id="r_aa6ee6a2d6312b5a92db53caf4424490e"></a>

```c
#define AMEBA_UART0_RTS 98
```

相关声明：[AMEBA_UART0_RTS](#aa6ee6a2d6312b5a92db53caf4424490e)。

UART0 RTS 功能（UART0 RTS Function）。

<a id="r_a5264a7b7b4e1dc4e66abf649d6fbf398"></a>

```c
#define AMEBA_UART1_TXD 99
```

相关声明：[AMEBA_UART1_TXD](#a5264a7b7b4e1dc4e66abf649d6fbf398)。

UART1 TXD 功能（UART1 TXD Function）。

<a id="r_a76f722879ffac4f94f543ebfc514fb7f"></a>

```c
#define AMEBA_UART1_RXD 100
```

相关声明：[AMEBA_UART1_RXD](#a76f722879ffac4f94f543ebfc514fb7f)。

UART1 RXD 功能（UART1 RXD Function）。

<a id="r_a8eb069f61c95598413fb9cda6304b287"></a>

```c
#define AMEBA_UART2_TXD 101
```

相关声明：[AMEBA_UART2_TXD](#a8eb069f61c95598413fb9cda6304b287)。

UART2 TXD 功能（UART2 TXD Function）。

<a id="r_a8b9308171579c28194d890a90cdf68be"></a>

```c
#define AMEBA_UART2_RXD 102
```

相关声明：[AMEBA_UART2_RXD](#a8b9308171579c28194d890a90cdf68be)。

UART2 RXD 功能（UART2 RXD Function）。

<a id="r_a75bcfb713ccf540f3a1ccc04310ce081"></a>

```c
#define AMEBA_UART3_TXD 103
```

相关声明：[AMEBA_UART3_TXD](#a75bcfb713ccf540f3a1ccc04310ce081)。

UART3 TXD 功能（UART3 TXD Function）。

<a id="r_a0510afb83840c5ca8f8b92ee4f921985"></a>

```c
#define AMEBA_UART3_RXD 104
```

相关声明：[AMEBA_UART3_RXD](#a0510afb83840c5ca8f8b92ee4f921985)。

UART3 RXD 功能（UART3 RXD Function）。

<a id="r_a4394a28c38006ed0f0d2b362632a8e7a"></a>

```c
#define AMEBA_UART3_CTS 105
```

相关声明：[AMEBA_UART3_CTS](#a4394a28c38006ed0f0d2b362632a8e7a)。

UART3 CTS 功能（UART3 CTS Function）。

<a id="r_a137f035812f7f6b433f8f5aa859f14f7"></a>

```c
#define AMEBA_UART3_RTS 106
```

相关声明：[AMEBA_UART3_RTS](#a137f035812f7f6b433f8f5aa859f14f7)。

UART3 RTS 功能（UART3 RTS Function）。

<a id="r_a655397fd1f1fdde9fd9e41ea6d9d6c9a"></a>

```c
#define AMEBA_A2C0_TX 107
```

相关声明：[AMEBA_A2C0_TX](#a655397fd1f1fdde9fd9e41ea6d9d6c9a)。

A2C0 TX 功能（A2C0 TX Function）。

<a id="r_a48c3334b193c21955ab18fb355dcee8d"></a>

```c
#define AMEBA_A2C0_RX 108
```

相关声明：[AMEBA_A2C0_RX](#a48c3334b193c21955ab18fb355dcee8d)。

A2C0 RX 功能（A2C0 RX Function）。

<a id="r_a269535ef782896bb7b41f961065e338a"></a>

```c
#define AMEBA_A2C1_TX 109
```

相关声明：[AMEBA_A2C1_TX](#a269535ef782896bb7b41f961065e338a)。

A2C1 TX 功能（A2C1 TX Function）。

<a id="r_aa2d9dd58029452815de9606ae6206449"></a>

```c
#define AMEBA_A2C1_RX 110
```

相关声明：[AMEBA_A2C1_RX](#aa2d9dd58029452815de9606ae6206449)。

A2C1 RX 功能（A2C1 RX Function）。

<a id="r_a6c7416aabd5fbef8375014ebfe78a981"></a>

```c
#define AMEBA_TIM4_PWM0 111
```

相关声明：[AMEBA_TIM4_PWM0](#a6c7416aabd5fbef8375014ebfe78a981)。

TIM4 PWM0 功能（TIM4 PWM0 Function）。

<a id="r_aa59f0387d111a5d68c4676fbe128de0f"></a>

```c
#define AMEBA_TIM4_PWM1 112
```

相关声明：[AMEBA_TIM4_PWM1](#aa59f0387d111a5d68c4676fbe128de0f)。

TIM4 PWM1 功能（TIM4 PWM1 Function）。

<a id="r_ad860612ef34db0d934ab76c72214cd8e"></a>

```c
#define AMEBA_TIM4_PWM2 113
```

相关声明：[AMEBA_TIM4_PWM2](#ad860612ef34db0d934ab76c72214cd8e)。

TIM4 PWM2 功能（TIM4 PWM2 Function）。

<a id="r_af3aeda37971aeba0315a5f4fd7bc4ebd"></a>

```c
#define AMEBA_TIM4_PWM3 114
```

相关声明：[AMEBA_TIM4_PWM3](#af3aeda37971aeba0315a5f4fd7bc4ebd)。

TIM4 PWM3 功能（TIM4 PWM3 Function）。

<a id="r_a5c52baeaed161b8ef556a187981b7e80"></a>

```c
#define AMEBA_TIM5_PWM0 115
```

相关声明：[AMEBA_TIM5_PWM0](#a5c52baeaed161b8ef556a187981b7e80)。

TIM5 PWM0 功能（TIM5 PWM0 Function）。

<a id="r_a7b4e237c60289cbcc99894bf98e52477"></a>

```c
#define AMEBA_TIM5_PWM1 116
```

相关声明：[AMEBA_TIM5_PWM1](#a7b4e237c60289cbcc99894bf98e52477)。

TIM5 PWM1 功能（TIM5 PWM1 Function）。

<a id="r_afcc1a8262a0ccca9f6b0f7477ba67d7e"></a>

```c
#define AMEBA_TIM5_PWM2 117
```

相关声明：[AMEBA_TIM5_PWM2](#afcc1a8262a0ccca9f6b0f7477ba67d7e)。

TIM5 PWM2 功能（TIM5 PWM2 Function）。

<a id="r_ac586bce59c5b8f195ccc9f8aae7b27dc"></a>

```c
#define AMEBA_TIM5_PWM3 118
```

相关声明：[AMEBA_TIM5_PWM3](#ac586bce59c5b8f195ccc9f8aae7b27dc)。

TIM5 PWM3 功能（TIM5 PWM3 Function）。

<a id="r_a5cdcb434a1f8922549f6816b278583ef"></a>

```c
#define AMEBA_TIM6_PWM0 119
```

相关声明：[AMEBA_TIM6_PWM0](#a5cdcb434a1f8922549f6816b278583ef)。

TIM6 PWM0 功能（TIM6 PWM0 Function）。

<a id="r_a952c05d9e2f7e6f06c7bf9bcee7a676c"></a>

```c
#define AMEBA_TIM6_PWM1 120
```

相关声明：[AMEBA_TIM6_PWM1](#a952c05d9e2f7e6f06c7bf9bcee7a676c)。

TIM6 PWM1 功能（TIM6 PWM1 Function）。

<a id="r_a6ef12eb463248efa12c3e8badedb6fb0"></a>

```c
#define AMEBA_TIM6_PWM2 121
```

相关声明：[AMEBA_TIM6_PWM2](#a6ef12eb463248efa12c3e8badedb6fb0)。

TIM6 PWM2 功能（TIM6 PWM2 Function）。

<a id="r_afc4dd0f4e44ce23eb8a9956e290d27e1"></a>

```c
#define AMEBA_TIM6_PWM3 122
```

相关声明：[AMEBA_TIM6_PWM3](#afc4dd0f4e44ce23eb8a9956e290d27e1)。

TIM6 PWM3 功能（TIM6 PWM3 Function）。

<a id="r_ae420d4b69fd99ce575d8a558331e5559"></a>

```c
#define AMEBA_TIM7_PWM0 123
```

相关声明：[AMEBA_TIM7_PWM0](#ae420d4b69fd99ce575d8a558331e5559)。

TIM7 PWM0 功能（TIM7 PWM0 Function）。

<a id="r_af31d12ae9898ac82b88ce39d4af404ab"></a>

```c
#define AMEBA_TIM7_PWM1 124
```

相关声明：[AMEBA_TIM7_PWM1](#af31d12ae9898ac82b88ce39d4af404ab)。

TIM7 PWM1 功能（TIM7 PWM1 Function）。

<a id="r_aa9957c6d05d0768adfea4f58b3f8f734"></a>

```c
#define AMEBA_TIM7_PWM2 125
```

相关声明：[AMEBA_TIM7_PWM2](#aa9957c6d05d0768adfea4f58b3f8f734)。

TIM7 PWM2 功能（TIM7 PWM2 Function）。

<a id="r_aceafb2a9130502bf8dd1173042d21d85"></a>

```c
#define AMEBA_TIM7_PWM3 126
```

相关声明：[AMEBA_TIM7_PWM3](#aceafb2a9130502bf8dd1173042d21d85)。

TIM7 PWM3 功能（TIM7 PWM3 Function）。

<a id="r_a01bf7068e563442cebfb3e3b89eeaa06"></a>

```c
#define AMEBA_PWM_TIM4_TRIG 127
```

相关声明：[AMEBA_PWM_TIM4_TRIG](#a01bf7068e563442cebfb3e3b89eeaa06)。

PWM TIM4 TRIG 功能（PWM TIM4 TRIG Function）。

<a id="r_a3c9c4522b23ad6bc272ed44396a19d42"></a>

```c
#define AMEBA_PWM_TIM5_TRIG 128
```

相关声明：[AMEBA_PWM_TIM5_TRIG](#a3c9c4522b23ad6bc272ed44396a19d42)。

PWM TIM5 TRIG 功能（PWM TIM5 TRIG Function）。

<a id="r_a9711556f3eff1bbece11e5d4b277bf08"></a>

```c
#define AMEBA_PWM_TIM6_TRIG 129
```

相关声明：[AMEBA_PWM_TIM6_TRIG](#a9711556f3eff1bbece11e5d4b277bf08)。

PWM TIM6 TRIG 功能（PWM TIM6 TRIG Function）。

<a id="r_a4d10f56f621b79ff862f95c6c567268a"></a>

```c
#define AMEBA_PWM_TIM7_TRIG 130
```

相关声明：[AMEBA_PWM_TIM7_TRIG](#a4d10f56f621b79ff862f95c6c567268a)。

PWM TIM7 TRIG 功能（PWM TIM7 TRIG Function）。

<a id="r_ad159617e6e0318e8413d676d82517410"></a>

```c
#define AMEBA_CAPT_TIM8_TRIG 131
```

相关声明：[AMEBA_CAPT_TIM8_TRIG](#ad159617e6e0318e8413d676d82517410)。

CAPT TIM8 TRIG 功能（CAPT TIM8 TRIG Function）。

<a id="r_a654f82f22bb941b39469479e968bc8b0"></a>

```c
#define AMEBA_IR_TX 132
```

相关声明：[AMEBA_IR_TX](#a654f82f22bb941b39469479e968bc8b0)。

IR TX 功能（IR TX Function）。

<a id="r_a3136f2fc775bb63f80203ca8859627b2"></a>

```c
#define AMEBA_IR_RX 133
```

相关声明：[AMEBA_IR_RX](#a3136f2fc775bb63f80203ca8859627b2)。

IR RX 功能（IR RX Function）。

<a id="r_a68b89ba7a1c6bb19d56008fc82011cd6"></a>

```c
#define AMEBA_ANT_SEL_P 134
```

相关声明：[AMEBA_ANT_SEL_P](#a68b89ba7a1c6bb19d56008fc82011cd6)。

ANT SEL P 功能（ANT SEL P Function）。

<a id="r_a9efd0095ab6c1d29852092b780d74f3d"></a>

```c
#define AMEBA_ANT_SEL_N 135
```

相关声明：[AMEBA_ANT_SEL_N](#a9efd0095ab6c1d29852092b780d74f3d)。

ANT SEL N 功能（ANT SEL N Function）。

<a id="r_abcbee3b4e1ad4597b2b96910d2a86a98"></a>

```c
#define AMEBA_TRSW_P 136
```

相关声明：[AMEBA_TRSW_P](#abcbee3b4e1ad4597b2b96910d2a86a98)。

TRSW P 功能（TRSW P Function）。

<a id="r_abd3853ac7c1179df89a64923fdc64037"></a>

```c
#define AMEBA_TRSW_N 137
```

相关声明：[AMEBA_TRSW_N](#abd3853ac7c1179df89a64923fdc64037)。

TRSW N 功能（TRSW N Function）。

<a id="r_a899ab9c180ed23f35c159081123b970f"></a>

```c
#define AMEBA_PA_EN0 138
```

相关声明：[AMEBA_PA_EN0](#a899ab9c180ed23f35c159081123b970f)。

PA EN0 功能（PA EN0 Function）。

<a id="r_a1f0ea4a9e9ba14f3d7a43fde010475d8"></a>

```c
#define AMEBA_LNA_EN0 139
```

相关声明：[AMEBA_LNA_EN0](#a1f0ea4a9e9ba14f3d7a43fde010475d8)。

LNA EN0 功能（LNA EN0 Function）。

<a id="r_ab2d53a2028960a3d243718b2c8b2e068"></a>

```c
#define AMEBA_PA_EN1 140
```

相关声明：[AMEBA_PA_EN1](#ab2d53a2028960a3d243718b2c8b2e068)。

PA EN1 功能（PA EN1 Function）。

<a id="r_abab14c1999f9e158514a3f230165402b"></a>

```c
#define AMEBA_LNA_EN1 141
```

相关声明：[AMEBA_LNA_EN1](#abab14c1999f9e158514a3f230165402b)。

LNA EN1 功能（LNA EN1 Function）。

<a id="r_a56af273054464fb778e144aafc6e7737"></a>

```c
#define AMEBA_BT_CLK_REQ 142
```

相关声明：[AMEBA_BT_CLK_REQ](#a56af273054464fb778e144aafc6e7737)。

BT CLK REQ 功能（BT CLK REQ Function）。

<a id="r_a92cd123103ff092048b8f56290010431"></a>

```c
#define AMEBA_WLAN_ACT 143
```

相关声明：[AMEBA_WLAN_ACT](#a92cd123103ff092048b8f56290010431)。

WLAN ACT 功能（WLAN ACT Function）。

<a id="r_a693a90316d8213cc23a7f903d435087f"></a>

```c
#define AMEBA_BT_ACT 144
```

相关声明：[AMEBA_BT_ACT](#a693a90316d8213cc23a7f903d435087f)。

BT ACT 功能（BT ACT Function）。

<a id="r_ab44411e03a49e48e55964b719593b251"></a>

```c
#define AMEBA_BT_STE 145
```

相关声明：[AMEBA_BT_STE](#ab44411e03a49e48e55964b719593b251)。

BT STE 功能（BT STE Function）。

<a id="r_ad553fa6b1094b91af8b9fbf230f57e06"></a>

```c
#define AMEBA_BT_CK 146
```

相关声明：[AMEBA_BT_CK](#ad553fa6b1094b91af8b9fbf230f57e06)。

BT CK 功能（BT CK Function）。

<a id="r_a52052e6f01e49f0edfcbd2c57300ffdb"></a>

```c
#define AMEBA_ZB_REQ 147
```

相关声明：[AMEBA_ZB_REQ](#a52052e6f01e49f0edfcbd2c57300ffdb)。

ZB REQ 功能（ZB REQ Function）。

<a id="r_a6720be2fe65055f8a56f0d5634ad1822"></a>

```c
#define AMEBA_ZB_GRANT 148
```

相关声明：[AMEBA_ZB_GRANT](#a6720be2fe65055f8a56f0d5634ad1822)。

ZB GRANT 功能（ZB GRANT Function）。

<a id="r_ad8dd8552461df7cba8cda72fa02af8bd"></a>

```c
#define AMEBA_ZB_PRI 149
```

相关声明：[AMEBA_ZB_PRI](#ad8dd8552461df7cba8cda72fa02af8bd)。

ZB PRI 功能（ZB PRI Function）。

<a id="r_a54ad7724e5d8978c50408bfecaa9fd7a"></a>

```c
#define AMEBA_BT_ANT_SW0 150
```

相关声明：[AMEBA_BT_ANT_SW0](#a54ad7724e5d8978c50408bfecaa9fd7a)。

BT ANT SW0 功能（BT ANT SW0 Function）。

<a id="r_a2605386e83160c6ecd94f955ed64cfea"></a>

```c
#define AMEBA_BT_ANT_SW1 151
```

相关声明：[AMEBA_BT_ANT_SW1](#a2605386e83160c6ecd94f955ed64cfea)。

BT ANT SW1 功能（BT ANT SW1 Function）。

<a id="r_a208bdad0215544c4238b60eb3309fb56"></a>

```c
#define AMEBA_BT_ANT_SW2 152
```

相关声明：[AMEBA_BT_ANT_SW2](#a208bdad0215544c4238b60eb3309fb56)。

BT ANT SW2 功能（BT ANT SW2 Function）。

<a id="r_a85da026d355e23447feff5ab189efe34"></a>

```c
#define AMEBA_BT_ANT_SW3 153
```

相关声明：[AMEBA_BT_ANT_SW3](#a85da026d355e23447feff5ab189efe34)。

BT ANT SW3 功能（BT ANT SW3 Function）。

<a id="r_aa23f667d96ee60da294d724be807687b"></a>

```c
#define AMEBA_EXT_CLK50M_IN 154
```

相关声明：[AMEBA_EXT_CLK50M_IN](#aa23f667d96ee60da294d724be807687b)。

EXT CLK50M IN 功能（EXT CLK50M IN Function）。

<a id="r_ad6b461da618e8b97bb8b169153cd41fd"></a>

```c
#define AMEBA_EXT_CLK_OUT 155
```

相关声明：[AMEBA_EXT_CLK_OUT](#ad6b461da618e8b97bb8b169153cd41fd)。

EXT CLK OUT 功能（EXT CLK OUT Function）。

<a id="r_a7e308adb3b91184da493a706c1b382ec"></a>

```c
#define AMEBA_UART_LOG_RXD 156
```

相关声明：[AMEBA_UART_LOG_RXD](#a7e308adb3b91184da493a706c1b382ec)。

UART LOG RXD 功能（UART LOG RXD Function）。

<a id="r_a4aafb8bb1e2a9a080ee96c7f9d97a631"></a>

```c
#define AMEBA_UART_LOG_TXD 157
```

相关声明：[AMEBA_UART_LOG_TXD](#a4aafb8bb1e2a9a080ee96c7f9d97a631)。

UART LOG TXD 功能（UART LOG TXD Function）。

<a id="r_a3de45b5f99b4f7e89e53c103f38f7e60"></a>

```c
#define AMEBA_SIC_CLK 158
```

相关声明：[AMEBA_SIC_CLK](#a3de45b5f99b4f7e89e53c103f38f7e60)。

SIC CLK 功能（SIC CLK Function）。

<a id="r_a8575e3f6a28a480ec58e1f2898737599"></a>

```c
#define AMEBA_SIC_DAT 159
```

相关声明：[AMEBA_SIC_DAT](#a8575e3f6a28a480ec58e1f2898737599)。

SIC DAT 功能（SIC DAT Function）。

<a id="r_ada4cd0c3bf304e3441ae3d4c53f97bd0"></a>

```c
#define AMEBA_BT_FWLOG 160
```

相关声明：[AMEBA_BT_FWLOG](#ada4cd0c3bf304e3441ae3d4c53f97bd0)。

BT FWLOG 功能（BT FWLOG Function）。

<a id="r_af476627e27dfc377bdeb785450c1e45e"></a>

```c
#define AMEBA_BT_I2C_SDA 161
```

相关声明：[AMEBA_BT_I2C_SDA](#af476627e27dfc377bdeb785450c1e45e)。

BT I2C SDA 功能（BT I2C SDA Function）。

<a id="r_a052da9b2818c166df17290f199cce741"></a>

```c
#define AMEBA_BT_I2C_SCL 162
```

相关声明：[AMEBA_BT_I2C_SCL](#a052da9b2818c166df17290f199cce741)。

BT I2C SCL 功能（BT I2C SCL Function）。

## 4.2\_详细说明（Detailed Documentation）

<a id="a48c3334b193c21955ab18fb355dcee8d"></a>

### `AMEBA_A2C0_RX`

```c
#define AMEBA_A2C0_RX 108
```

A2C0 RX 功能（A2C0 RX Function）。

<a id="a655397fd1f1fdde9fd9e41ea6d9d6c9a"></a>

### `AMEBA_A2C0_TX`

```c
#define AMEBA_A2C0_TX 107
```

A2C0 TX 功能（A2C0 TX Function）。

<a id="aa2d9dd58029452815de9606ae6206449"></a>

### `AMEBA_A2C1_RX`

```c
#define AMEBA_A2C1_RX 110
```

A2C1 RX 功能（A2C1 RX Function）。

<a id="a269535ef782896bb7b41f961065e338a"></a>

### `AMEBA_A2C1_TX`

```c
#define AMEBA_A2C1_TX 109
```

A2C1 TX 功能（A2C1 TX Function）。

<a id="acb023403125750639b0d02171607c2ad"></a>

### `AMEBA_ADC`

```c
#define AMEBA_ADC 5
```

ADC 功能（ADC Function）。

<a id="a9efd0095ab6c1d29852092b780d74f3d"></a>

### `AMEBA_ANT_SEL_N`

```c
#define AMEBA_ANT_SEL_N 135
```

ANT SEL N 功能（ANT SEL N Function）。

<a id="a68b89ba7a1c6bb19d56008fc82011cd6"></a>

### `AMEBA_ANT_SEL_P`

```c
#define AMEBA_ANT_SEL_P 134
```

ANT SEL P 功能（ANT SEL P Function）。

<a id="a71f0921f7c7ccd5e272cb66733dfa994"></a>

### `AMEBA_BT`

```c
#define AMEBA_BT 16
```

BT 功能（BT Function）。

<a id="a693a90316d8213cc23a7f903d435087f"></a>

### `AMEBA_BT_ACT`

```c
#define AMEBA_BT_ACT 144
```

BT ACT 功能（BT ACT Function）。

<a id="a54ad7724e5d8978c50408bfecaa9fd7a"></a>

### `AMEBA_BT_ANT_SW0`

```c
#define AMEBA_BT_ANT_SW0 150
```

BT ANT SW0 功能（BT ANT SW0 Function）。

<a id="a2605386e83160c6ecd94f955ed64cfea"></a>

### `AMEBA_BT_ANT_SW1`

```c
#define AMEBA_BT_ANT_SW1 151
```

BT ANT SW1 功能（BT ANT SW1 Function）。

<a id="a208bdad0215544c4238b60eb3309fb56"></a>

### `AMEBA_BT_ANT_SW2`

```c
#define AMEBA_BT_ANT_SW2 152
```

BT ANT SW2 功能（BT ANT SW2 Function）。

<a id="a85da026d355e23447feff5ab189efe34"></a>

### `AMEBA_BT_ANT_SW3`

```c
#define AMEBA_BT_ANT_SW3 153
```

BT ANT SW3 功能（BT ANT SW3 Function）。

<a id="ad553fa6b1094b91af8b9fbf230f57e06"></a>

### `AMEBA_BT_CK`

```c
#define AMEBA_BT_CK 146
```

BT CK 功能（BT CK Function）。

<a id="a56af273054464fb778e144aafc6e7737"></a>

### `AMEBA_BT_CLK_REQ`

```c
#define AMEBA_BT_CLK_REQ 142
```

BT CLK REQ 功能（BT CLK REQ Function）。

<a id="ada4cd0c3bf304e3441ae3d4c53f97bd0"></a>

### `AMEBA_BT_FWLOG`

```c
#define AMEBA_BT_FWLOG 160
```

BT FWLOG 功能（BT FWLOG Function）。

<a id="a052da9b2818c166df17290f199cce741"></a>

### `AMEBA_BT_I2C_SCL`

```c
#define AMEBA_BT_I2C_SCL 162
```

BT I2C SCL 功能（BT I2C SCL Function）。

<a id="af476627e27dfc377bdeb785450c1e45e"></a>

### `AMEBA_BT_I2C_SDA`

```c
#define AMEBA_BT_I2C_SDA 161
```

BT I2C SDA 功能（BT I2C SDA Function）。

<a id="a6808b0d69603d73741df35aa2ccf9166"></a>

### `AMEBA_BT_IO`

```c
#define AMEBA_BT_IO 15
```

BT IO 功能（BT IO Function）。

<a id="ab44411e03a49e48e55964b719593b251"></a>

### `AMEBA_BT_STE`

```c
#define AMEBA_BT_STE 145
```

BT STE 功能（BT STE Function）。

<a id="a1eeebd2f73559939b681db6e912def28"></a>

### `AMEBA_CAP_TOUCH`

```c
#define AMEBA_CAP_TOUCH 5
```

电容触摸 功能（Cap touch Function）。

<a id="ad159617e6e0318e8413d676d82517410"></a>

### `AMEBA_CAPT_TIM8_TRIG`

```c
#define AMEBA_CAPT_TIM8_TRIG 131
```

CAPT TIM8 TRIG 功能（CAPT TIM8 TRIG Function）。

<a id="a98d7af9e28bf21c740207cffde3550db"></a>

### `AMEBA_DEBUG`

```c
#define AMEBA_DEBUG 17
```

调试 功能（Debug Function）。

<a id="a5544c01a480ae8ab721f846aedeac3a2"></a>

### `AMEBA_DMIC_CLK`

```c
#define AMEBA_DMIC_CLK 85
```

DMIC CLK 功能（DMIC CLK Function）。

<a id="ac8a69ac2c1bfea15838a8a5da7ea3d1b"></a>

### `AMEBA_DMIC_DATA`

```c
#define AMEBA_DMIC_DATA 86
```

DMIC DATA 功能（DMIC DATA Function）。

<a id="aa23f667d96ee60da294d724be807687b"></a>

### `AMEBA_EXT_CLK50M_IN`

```c
#define AMEBA_EXT_CLK50M_IN 154
```

EXT CLK50M IN 功能（EXT CLK50M IN Function）。

<a id="ad6b461da618e8b97bb8b169153cd41fd"></a>

### `AMEBA_EXT_CLK_OUT`

```c
#define AMEBA_EXT_CLK_OUT 155
```

EXT CLK OUT 功能（EXT CLK OUT Function）。

<a id="a1a770820da1c7f81c4925cd6a6fab8f4"></a>

### `AMEBA_GPIO`

```c
#define AMEBA_GPIO 0
```

GPIO 功能（GPIO Function）。

<a id="a45b715ce9be8df9c8693cb4349b7f0da"></a>

### `AMEBA_I2C0_SCL`

```c
#define AMEBA_I2C0_SCL 89
```

I2C0 SCL 功能（I2C0 SCL Function）。

<a id="a1adbe2f3d191e115cd29c73b8d726272"></a>

### `AMEBA_I2C0_SDA`

```c
#define AMEBA_I2C0_SDA 90
```

I2C0 SDA 功能（I2C0 SDA Function）。

<a id="a6cd3bf525d23b4224b1238d3b0c5fcde"></a>

### `AMEBA_I2C1_SCL`

```c
#define AMEBA_I2C1_SCL 91
```

I2C1 SCL 功能（I2C1 SCL Function）。

<a id="a88e9123211493809fdd23078928905de"></a>

### `AMEBA_I2C1_SDA`

```c
#define AMEBA_I2C1_SDA 92
```

I2C1 SDA 功能（I2C1 SDA Function）。

<a id="a24a9be29f490ac4b2425b8f0c96fd0f9"></a>

### `AMEBA_I2S0_BCLK`

```c
#define AMEBA_I2S0_BCLK 32
```

I2S0 BCLK 功能（I2S0 BCLK Function）。

<a id="ac224c5d98fcda932f1dd56e119ea8c8f"></a>

### `AMEBA_I2S0_DIO0`

```c
#define AMEBA_I2S0_DIO0 35
```

I2S0 DIO0 功能（I2S0 DIO0 Function）。

<a id="a6d15583c82ed66abfd8879cd1b83bc85"></a>

### `AMEBA_I2S0_DIO1`

```c
#define AMEBA_I2S0_DIO1 36
```

I2S0 DIO1 功能（I2S0 DIO1 Function）。

<a id="a167ee959e13888da0a0a6aff7620f756"></a>

### `AMEBA_I2S0_DIO2`

```c
#define AMEBA_I2S0_DIO2 37
```

I2S0 DIO2 功能（I2S0 DIO2 Function）。

<a id="a430fc7f6f6e9703f7fb425b173d5fd6c"></a>

### `AMEBA_I2S0_DIO3`

```c
#define AMEBA_I2S0_DIO3 38
```

I2S0 DIO3 功能（I2S0 DIO3 Function）。

<a id="a712d64cdb749070056bd158553370eae"></a>

### `AMEBA_I2S0_MCLK`

```c
#define AMEBA_I2S0_MCLK 33
```

I2S0 MCLK 功能（I2S0 MCLK Function）。

<a id="a51d16562267051569c14c05358115cb4"></a>

### `AMEBA_I2S0_WS`

```c
#define AMEBA_I2S0_WS 34
```

I2S0 WS 功能（I2S0 WS Function）。

<a id="a3136f2fc775bb63f80203ca8859627b2"></a>

### `AMEBA_IR_RX`

```c
#define AMEBA_IR_RX 133
```

IR RX 功能（IR RX Function）。

<a id="a654f82f22bb941b39469479e968bc8b0"></a>

### `AMEBA_IR_TX`

```c
#define AMEBA_IR_TX 132
```

IR TX 功能（IR TX Function）。

<a id="a522133bb5b0c6febe4ea66506a4b1a87"></a>

### `AMEBA_LCD_D0`

```c
#define AMEBA_LCD_D0 45
```

LCD D0 功能（LCD D0 Function）。

<a id="a4823b1d9d83c32705a25f108ba017409"></a>

### `AMEBA_LCD_D1`

```c
#define AMEBA_LCD_D1 46
```

LCD D1 功能（LCD D1 Function）。

<a id="afa69b39698293897870b9b5a059a8a5b"></a>

### `AMEBA_LCD_D10`

```c
#define AMEBA_LCD_D10 55
```

LCD D10 功能（LCD D10 Function）。

<a id="aa03bee3a3fa1833aa9ca390332f3f090"></a>

### `AMEBA_LCD_D11`

```c
#define AMEBA_LCD_D11 56
```

LCD D11 功能（LCD D11 Function）。

<a id="aabe467e62f38135cd57f230c3a4170b0"></a>

### `AMEBA_LCD_D12`

```c
#define AMEBA_LCD_D12 57
```

LCD D12 功能（LCD D12 Function）。

<a id="a003b0dbf7f5a6566ed601bcf2b7667a7"></a>

### `AMEBA_LCD_D13`

```c
#define AMEBA_LCD_D13 58
```

LCD D13 功能（LCD D13 Function）。

<a id="a11f6d88a06999e17ef85c3f6d00abe5a"></a>

### `AMEBA_LCD_D14`

```c
#define AMEBA_LCD_D14 59
```

LCD D14 功能（LCD D14 Function）。

<a id="af6af66abdbef26731863b9a39c9d8c73"></a>

### `AMEBA_LCD_D15`

```c
#define AMEBA_LCD_D15 60
```

LCD D15 功能（LCD D15 Function）。

<a id="a6538dedaeda74bea11dcc0ce1dc3b489"></a>

### `AMEBA_LCD_D16`

```c
#define AMEBA_LCD_D16 61
```

LCD D16 功能（LCD D16 Function）。

<a id="a24209ab9d918529a909a475dcac4329d"></a>

### `AMEBA_LCD_D17`

```c
#define AMEBA_LCD_D17 62
```

LCD D17 功能（LCD D17 Function）。

<a id="a58d51bcd1c04166df3452a75d54b2232"></a>

### `AMEBA_LCD_D18`

```c
#define AMEBA_LCD_D18 63
```

LCD D18 功能（LCD D18 Function）。

<a id="a3e0bf2ec675e3c723927ed1ccd76c24a"></a>

### `AMEBA_LCD_D19`

```c
#define AMEBA_LCD_D19 64
```

LCD D19 功能（LCD D19 Function）。

<a id="a61b5ceec7d442cc66041b3c6b802ca21"></a>

### `AMEBA_LCD_D2`

```c
#define AMEBA_LCD_D2 47
```

LCD D2 功能（LCD D2 Function）。

<a id="a7bf6d2c2fa4fcd4f6547eb2430626070"></a>

### `AMEBA_LCD_D20`

```c
#define AMEBA_LCD_D20 65
```

LCD D20 功能（LCD D20 Function）。

<a id="a0589309be4f51562dd98342d59ef4de1"></a>

### `AMEBA_LCD_D21`

```c
#define AMEBA_LCD_D21 66
```

LCD D21 功能（LCD D21 Function）。

<a id="a4f080cb41949b5f6f5d24d735ad9ac3e"></a>

### `AMEBA_LCD_D22`

```c
#define AMEBA_LCD_D22 67
```

LCD D22 功能（LCD D22 Function）。

<a id="a7008524284eed0ce1011022f830c6f22"></a>

### `AMEBA_LCD_D23`

```c
#define AMEBA_LCD_D23 68
```

LCD D23 功能（LCD D23 Function）。

<a id="a07c845ba6b75e8c2ab5aba37601f1683"></a>

### `AMEBA_LCD_D3`

```c
#define AMEBA_LCD_D3 48
```

LCD D3 功能（LCD D3 Function）。

<a id="a32e6399fffd99f6987df5583b9cc9a47"></a>

### `AMEBA_LCD_D4`

```c
#define AMEBA_LCD_D4 49
```

LCD D4 功能（LCD D4 Function）。

<a id="aa555f1c733a42d9507c9a96dfb187929"></a>

### `AMEBA_LCD_D5`

```c
#define AMEBA_LCD_D5 50
```

LCD D5 功能（LCD D5 Function）。

<a id="a3bf439831ceafadcd790046b4bf9330d"></a>

### `AMEBA_LCD_D6`

```c
#define AMEBA_LCD_D6 51
```

LCD D6 功能（LCD D6 Function）。

<a id="ab54a5c4ccf324e8219dfbd8ced921935"></a>

### `AMEBA_LCD_D7`

```c
#define AMEBA_LCD_D7 52
```

LCD D7 功能（LCD D7 Function）。

<a id="a9cb563e0a3071f12726146ff4d421b38"></a>

### `AMEBA_LCD_D8`

```c
#define AMEBA_LCD_D8 53
```

LCD D8 功能（LCD D8 Function）。

<a id="a249d2a18cdaf957777075fa5a8b5866d"></a>

### `AMEBA_LCD_D9`

```c
#define AMEBA_LCD_D9 54
```

LCD D9 功能（LCD D9 Function）。

<a id="a67ebf980b33b1eb7edb396e15414f789"></a>

### `AMEBA_LCD_MCU_CSX`

```c
#define AMEBA_LCD_MCU_CSX 40
```

LCD MCU CSX 功能（LCD MCU CSX Function）。

<a id="a7884bd076393839950198adb7fe8d766"></a>

### `AMEBA_LCD_MCU_DCX`

```c
#define AMEBA_LCD_MCU_DCX 44
```

LCD MCU DCX 功能（LCD MCU DCX Function）。

<a id="a7cd81428627c9112288ab7a6bce3add0"></a>

### `AMEBA_LCD_MCU_RD`

```c
#define AMEBA_LCD_MCU_RD 41
```

LCD MCU RD 功能（LCD MCU RD Function）。

<a id="ac8eee74cbade1b05f9ade91f8be7289e"></a>

### `AMEBA_LCD_MCU_TE`

```c
#define AMEBA_LCD_MCU_TE 42
```

LCD MCU TE 功能（LCD MCU TE Function）。

<a id="a4747387279e003279756db7395680c3d"></a>

### `AMEBA_LCD_MCU_VSYNC`

```c
#define AMEBA_LCD_MCU_VSYNC 43
```

LCD MCU VSYNC 功能（LCD MCU VSYNC Function）。

<a id="a74e42f027f3c4d2fdccc5216439bebfd"></a>

### `AMEBA_LCD_MCU_WR`

```c
#define AMEBA_LCD_MCU_WR 39
```

LCD MCU WR 功能（LCD MCU WR Function）。

<a id="aeb425651bfda5d70a67b31d9ff993ce6"></a>

### `AMEBA_LCD_RGB_DCLK`

```c
#define AMEBA_LCD_RGB_DCLK 39
```

LCD RGB DCLK 功能（LCD RGB DCLK Function）。

<a id="a4733ac89dec3ce6b414bd3f723613423"></a>

### `AMEBA_LCD_RGB_DE`

```c
#define AMEBA_LCD_RGB_DE 40
```

LCD RGB DE 功能（LCD RGB DE Function）。

<a id="a4c640e0e2cff9f3c58d94b1a7295ff5a"></a>

### `AMEBA_LCD_RGB_HSYNC`

```c
#define AMEBA_LCD_RGB_HSYNC 41
```

LCD RGB HSYNC 功能（LCD RGB HSYNC Function）。

<a id="a26033b3b3357c9f4a946e8f374a59c93"></a>

### `AMEBA_LCD_RGB_TE`

```c
#define AMEBA_LCD_RGB_TE 42
```

LCD RGB TE 功能（LCD RGB TE Function）。

<a id="a03c6b203d24c41dc0d586878404b7a10"></a>

### `AMEBA_LCD_RGB_VSYNC`

```c
#define AMEBA_LCD_RGB_VSYNC 43
```

LCD RGB VSYNC 功能（LCD RGB VSYNC Function）。

<a id="abc19934502147fb9f1bd455edbe99c6f"></a>

### `AMEBA_LED_SCL`

```c
#define AMEBA_LED_SCL 87
```

LED SCL 功能（LED SCL Function）。

<a id="a0076f516b73ad3761de70f1a88d7747f"></a>

### `AMEBA_LED_SDA`

```c
#define AMEBA_LED_SDA 88
```

LED SDA 功能（LED SDA Function）。

<a id="a1f0ea4a9e9ba14f3d7a43fde010475d8"></a>

### `AMEBA_LNA_EN0`

```c
#define AMEBA_LNA_EN0 139
```

LNA EN0 功能（LNA EN0 Function）。

<a id="abab14c1999f9e158514a3f230165402b"></a>

### `AMEBA_LNA_EN1`

```c
#define AMEBA_LNA_EN1 141
```

LNA EN1 功能（LNA EN1 Function）。

<a id="a43b82c67e7ed46c4d7504354b89766a2"></a>

### `AMEBA_LOG_UART`

```c
#define AMEBA_LOG_UART 1
```

日志 UART 功能（Log UART Function）。

<a id="a899ab9c180ed23f35c159081123b970f"></a>

### `AMEBA_PA_EN0`

```c
#define AMEBA_PA_EN0 138
```

PA EN0 功能（PA EN0 Function）。

<a id="ab2d53a2028960a3d243718b2c8b2e068"></a>

### `AMEBA_PA_EN1`

```c
#define AMEBA_PA_EN1 140
```

PA EN1 功能（PA EN1 Function）。

<a id="a71d265adf87eb5aa7e991bf0dd6c142f"></a>

### `AMEBA_PINMUX`

```c
#define AMEBA_PINMUX ( port, line, funcid )
```

展开值（Value）：

```c
(((AMEBA_PORT_PIN(port, line)) << 8) | (funcid))
```

编码引脚复用配置（Pinmux Configuration）。

格式（Format）：位 [14:13] 为端口（Port），位 [12:8] 为引脚（Pin），位 [7:0] 为功能标识符（Function ID）。

<a id="a01f0e522a7c41526681b766c7ac7ce1f"></a>

### `AMEBA_PORT_PIN`

```c
#define AMEBA_PORT_PIN ( port, line )
```

展开值（Value）：

```c
((((port) - 'A') << 5) + (line))
```

编码端口（Port）和引脚编号（Pin Number）。

<a id="a01bf7068e563442cebfb3e3b89eeaa06"></a>

### `AMEBA_PWM_TIM4_TRIG`

```c
#define AMEBA_PWM_TIM4_TRIG 127
```

PWM TIM4 TRIG 功能（PWM TIM4 TRIG Function）。

<a id="a3c9c4522b23ad6bc272ed44396a19d42"></a>

### `AMEBA_PWM_TIM5_TRIG`

```c
#define AMEBA_PWM_TIM5_TRIG 128
```

PWM TIM5 TRIG 功能（PWM TIM5 TRIG Function）。

<a id="a9711556f3eff1bbece11e5d4b277bf08"></a>

### `AMEBA_PWM_TIM6_TRIG`

```c
#define AMEBA_PWM_TIM6_TRIG 129
```

PWM TIM6 TRIG 功能（PWM TIM6 TRIG Function）。

<a id="a4d10f56f621b79ff862f95c6c567268a"></a>

### `AMEBA_PWM_TIM7_TRIG`

```c
#define AMEBA_PWM_TIM7_TRIG 130
```

PWM TIM7 TRIG 功能（PWM TIM7 TRIG Function）。

<a id="aa2b51dc869def95632ff6cb06bcfd9f7"></a>

### `AMEBA_RMII`

```c
#define AMEBA_RMII 8
```

RMII 功能（RMII Function）。

<a id="a69b87577f31c6a8516c8790724390dc9"></a>

### `AMEBA_RMII_MDC`

```c
#define AMEBA_RMII_MDC 94
```

RMII MDC 功能（RMII MDC Function）。

<a id="aeb3029bd84e2ba794cc3e4c9239a4427"></a>

### `AMEBA_RMII_MDIO`

```c
#define AMEBA_RMII_MDIO 93
```

RMII MDIO 功能（RMII MDIO Function）。

<a id="a39c84a6ed19b96cc4980d31f557c493c"></a>

### `AMEBA_SD_M_CLK`

```c
#define AMEBA_SD_M_CLK 69
```

SD 主机 CLK 功能（SD Master CLK Function）。

<a id="ae46eb76cd70842fb715b75d8269034d8"></a>

### `AMEBA_SD_M_CMD`

```c
#define AMEBA_SD_M_CMD 70
```

SD 主机 CMD 功能（SD Master CMD Function）。

<a id="a92352131ed031d614fe21d6ca22371ba"></a>

### `AMEBA_SD_M_D0`

```c
#define AMEBA_SD_M_D0 71
```

SD 主机 D0 功能（SD Master D0 Function）。

<a id="a5570335f0e6b73bad8b4a664a9a8de80"></a>

### `AMEBA_SD_M_D1`

```c
#define AMEBA_SD_M_D1 72
```

SD 主机 D1 功能（SD Master D1 Function）。

<a id="a5525b6c4902920e81b0106ce570427c8"></a>

### `AMEBA_SD_M_D2`

```c
#define AMEBA_SD_M_D2 73
```

SD 主机 D2 功能（SD Master D2 Function）。

<a id="a7fb12e214c0c750f019caa5998c2db43"></a>

### `AMEBA_SD_M_D3`

```c
#define AMEBA_SD_M_D3 74
```

SD 主机 D3 功能（SD Master D3 Function）。

<a id="ad454ea614c16b6b153df1ec4d135ed44"></a>

### `AMEBA_SDIO_MST`

```c
#define AMEBA_SDIO_MST 12
```

SDIO 主机 功能（SDIO Master Function）。

<a id="a073da65535e6499cebdefd70812fc9eb"></a>

### `AMEBA_SDIO_SLV`

```c
#define AMEBA_SDIO_SLV 13
```

SDIO 从机 功能（SDIO Slave Function）。

<a id="aafdc733867a4ab1a0d16429679b19cba"></a>

### `AMEBA_SIC`

```c
#define AMEBA_SIC 14
```

SIC 功能（SIC Function）。

<a id="a3de45b5f99b4f7e89e53c103f38f7e60"></a>

### `AMEBA_SIC_CLK`

```c
#define AMEBA_SIC_CLK 158
```

SIC CLK 功能（SIC CLK Function）。

<a id="a8575e3f6a28a480ec58e1f2898737599"></a>

### `AMEBA_SIC_DAT`

```c
#define AMEBA_SIC_DAT 159
```

SIC DAT 功能（SIC DAT Function）。

<a id="a83fa3b6f04ec93e0d9c31a7f9d7bf1d8"></a>

### `AMEBA_SPI0`

```c
#define AMEBA_SPI0 9
```

SPI0 功能（SPI0 Function）。

<a id="a44689e534b5693fe964e45f04ec3af3a"></a>

### `AMEBA_SPI0_CLK`

```c
#define AMEBA_SPI0_CLK 75
```

SPI0 CLK 功能（SPI0 CLK Function）。

<a id="a6acad25a5a57a0199ee5ce1612862f26"></a>

### `AMEBA_SPI0_CS`

```c
#define AMEBA_SPI0_CS 78
```

SPI0 CS 功能（SPI0 CS Function）。

<a id="a2567e8fa1c77f607059df8a0d4e7b4a6"></a>

### `AMEBA_SPI0_MISO`

```c
#define AMEBA_SPI0_MISO 76
```

SPI0 MISO 功能（SPI0 MISO Function）。

<a id="a39e2d93a67ddf5a86546681800896466"></a>

### `AMEBA_SPI0_MOSI`

```c
#define AMEBA_SPI0_MOSI 77
```

SPI0 MOSI 功能（SPI0 MOSI Function）。

<a id="a428dd6e6aba093c0553141dd15c88c3c"></a>

### `AMEBA_SPI1`

```c
#define AMEBA_SPI1 10
```

SPI1 功能（SPI1 Function）。

<a id="a1997336af677a35e15d1402aed065ee6"></a>

### `AMEBA_SPI1_CLK`

```c
#define AMEBA_SPI1_CLK 79
```

SPI1 CLK 功能（SPI1 CLK Function）。

<a id="a9113912d0b976fd5539fbd003e83d85f"></a>

### `AMEBA_SPI1_CS`

```c
#define AMEBA_SPI1_CS 82
```

SPI1 CS 功能（SPI1 CS Function）。

<a id="ab40628d9a44f82362da70ab685c41cee"></a>

### `AMEBA_SPI1_MISO`

```c
#define AMEBA_SPI1_MISO 80
```

SPI1 MISO 功能（SPI1 MISO Function）。

<a id="ab9a8e9f5f8c3160a04998960c61e8b4d"></a>

### `AMEBA_SPI1_MOSI`

```c
#define AMEBA_SPI1_MOSI 81
```

SPI1 MOSI 功能（SPI1 MOSI Function）。

<a id="add660cc0a513fed62fe5d5e2ec12e5a7"></a>

### `AMEBA_SPIC0_FLASH`

```c
#define AMEBA_SPIC0_FLASH 2
```

SPIC0 闪存 功能（SPIC0 Flash Function）。

<a id="a5eb4f7828f8f9aab06d02ba35f4daf6f"></a>

### `AMEBA_SPIC1_FLASH`

```c
#define AMEBA_SPIC1_FLASH 3
```

SPIC1 闪存 功能（SPIC1 Flash Function）。

<a id="a97aa1778f7670f03bc30a9cc156c3da1"></a>

### `AMEBA_SPIC1_PSRAM`

```c
#define AMEBA_SPIC1_PSRAM 4
```

SPIC1 PSRAM 功能（SPIC1 PSRAM Function）。

<a id="a0d8fdf8ef3539a8cfe2b6e57f8e5db8d"></a>

### `AMEBA_SWD`

```c
#define AMEBA_SWD 11
```

SWD 功能（SWD Function）。

<a id="a467cc815f93d3f13a2329e7ff5ee5ef4"></a>

### `AMEBA_SWD_CLK`

```c
#define AMEBA_SWD_CLK 83
```

SWD CLK 功能（SWD CLK Function）。

<a id="aef189b30132fe99c6410a9067570dd74"></a>

### `AMEBA_SWD_DAT`

```c
#define AMEBA_SWD_DAT 84
```

SWD DAT 功能（SWD DAT Function）。

<a id="a6c7416aabd5fbef8375014ebfe78a981"></a>

### `AMEBA_TIM4_PWM0`

```c
#define AMEBA_TIM4_PWM0 111
```

TIM4 PWM0 功能（TIM4 PWM0 Function）。

<a id="aa59f0387d111a5d68c4676fbe128de0f"></a>

### `AMEBA_TIM4_PWM1`

```c
#define AMEBA_TIM4_PWM1 112
```

TIM4 PWM1 功能（TIM4 PWM1 Function）。

<a id="ad860612ef34db0d934ab76c72214cd8e"></a>

### `AMEBA_TIM4_PWM2`

```c
#define AMEBA_TIM4_PWM2 113
```

TIM4 PWM2 功能（TIM4 PWM2 Function）。

<a id="af3aeda37971aeba0315a5f4fd7bc4ebd"></a>

### `AMEBA_TIM4_PWM3`

```c
#define AMEBA_TIM4_PWM3 114
```

TIM4 PWM3 功能（TIM4 PWM3 Function）。

<a id="a5c52baeaed161b8ef556a187981b7e80"></a>

### `AMEBA_TIM5_PWM0`

```c
#define AMEBA_TIM5_PWM0 115
```

TIM5 PWM0 功能（TIM5 PWM0 Function）。

<a id="a7b4e237c60289cbcc99894bf98e52477"></a>

### `AMEBA_TIM5_PWM1`

```c
#define AMEBA_TIM5_PWM1 116
```

TIM5 PWM1 功能（TIM5 PWM1 Function）。

<a id="afcc1a8262a0ccca9f6b0f7477ba67d7e"></a>

### `AMEBA_TIM5_PWM2`

```c
#define AMEBA_TIM5_PWM2 117
```

TIM5 PWM2 功能（TIM5 PWM2 Function）。

<a id="ac586bce59c5b8f195ccc9f8aae7b27dc"></a>

### `AMEBA_TIM5_PWM3`

```c
#define AMEBA_TIM5_PWM3 118
```

TIM5 PWM3 功能（TIM5 PWM3 Function）。

<a id="a5cdcb434a1f8922549f6816b278583ef"></a>

### `AMEBA_TIM6_PWM0`

```c
#define AMEBA_TIM6_PWM0 119
```

TIM6 PWM0 功能（TIM6 PWM0 Function）。

<a id="a952c05d9e2f7e6f06c7bf9bcee7a676c"></a>

### `AMEBA_TIM6_PWM1`

```c
#define AMEBA_TIM6_PWM1 120
```

TIM6 PWM1 功能（TIM6 PWM1 Function）。

<a id="a6ef12eb463248efa12c3e8badedb6fb0"></a>

### `AMEBA_TIM6_PWM2`

```c
#define AMEBA_TIM6_PWM2 121
```

TIM6 PWM2 功能（TIM6 PWM2 Function）。

<a id="afc4dd0f4e44ce23eb8a9956e290d27e1"></a>

### `AMEBA_TIM6_PWM3`

```c
#define AMEBA_TIM6_PWM3 122
```

TIM6 PWM3 功能（TIM6 PWM3 Function）。

<a id="ae420d4b69fd99ce575d8a558331e5559"></a>

### `AMEBA_TIM7_PWM0`

```c
#define AMEBA_TIM7_PWM0 123
```

TIM7 PWM0 功能（TIM7 PWM0 Function）。

<a id="af31d12ae9898ac82b88ce39d4af404ab"></a>

### `AMEBA_TIM7_PWM1`

```c
#define AMEBA_TIM7_PWM1 124
```

TIM7 PWM1 功能（TIM7 PWM1 Function）。

<a id="aa9957c6d05d0768adfea4f58b3f8f734"></a>

### `AMEBA_TIM7_PWM2`

```c
#define AMEBA_TIM7_PWM2 125
```

TIM7 PWM2 功能（TIM7 PWM2 Function）。

<a id="aceafb2a9130502bf8dd1173042d21d85"></a>

### `AMEBA_TIM7_PWM3`

```c
#define AMEBA_TIM7_PWM3 126
```

TIM7 PWM3 功能（TIM7 PWM3 Function）。

<a id="abd3853ac7c1179df89a64923fdc64037"></a>

### `AMEBA_TRSW_N`

```c
#define AMEBA_TRSW_N 137
```

TRSW N 功能（TRSW N Function）。

<a id="abcbee3b4e1ad4597b2b96910d2a86a98"></a>

### `AMEBA_TRSW_P`

```c
#define AMEBA_TRSW_P 136
```

TRSW P 功能（TRSW P Function）。

<a id="aee7136959068c9606180a95716bed0ac"></a>

### `AMEBA_TSSI`

```c
#define AMEBA_TSSI 6
```

TSSI 功能（TSSI Function）。

<a id="aec676f180cd6c8ebde85b78984953106"></a>

### `AMEBA_UART0_CTS`

```c
#define AMEBA_UART0_CTS 97
```

UART0 CTS 功能（UART0 CTS Function）。

<a id="aa6ee6a2d6312b5a92db53caf4424490e"></a>

### `AMEBA_UART0_RTS`

```c
#define AMEBA_UART0_RTS 98
```

UART0 RTS 功能（UART0 RTS Function）。

<a id="aa93af39fe6c222c908a7642f5a4349a8"></a>

### `AMEBA_UART0_RXD`

```c
#define AMEBA_UART0_RXD 96
```

UART0 RXD 功能（UART0 RXD Function）。

<a id="a74d6af9b061345287512018abbe6cdc0"></a>

### `AMEBA_UART0_TXD`

```c
#define AMEBA_UART0_TXD 95
```

UART0 TXD 功能（UART0 TXD Function）。

<a id="a76f722879ffac4f94f543ebfc514fb7f"></a>

### `AMEBA_UART1_RXD`

```c
#define AMEBA_UART1_RXD 100
```

UART1 RXD 功能（UART1 RXD Function）。

<a id="a5264a7b7b4e1dc4e66abf649d6fbf398"></a>

### `AMEBA_UART1_TXD`

```c
#define AMEBA_UART1_TXD 99
```

UART1 TXD 功能（UART1 TXD Function）。

<a id="a8b9308171579c28194d890a90cdf68be"></a>

### `AMEBA_UART2_RXD`

```c
#define AMEBA_UART2_RXD 102
```

UART2 RXD 功能（UART2 RXD Function）。

<a id="a8eb069f61c95598413fb9cda6304b287"></a>

### `AMEBA_UART2_TXD`

```c
#define AMEBA_UART2_TXD 101
```

UART2 TXD 功能（UART2 TXD Function）。

<a id="a4394a28c38006ed0f0d2b362632a8e7a"></a>

### `AMEBA_UART3_CTS`

```c
#define AMEBA_UART3_CTS 105
```

UART3 CTS 功能（UART3 CTS Function）。

<a id="a137f035812f7f6b433f8f5aa859f14f7"></a>

### `AMEBA_UART3_RTS`

```c
#define AMEBA_UART3_RTS 106
```

UART3 RTS 功能（UART3 RTS Function）。

<a id="a0510afb83840c5ca8f8b92ee4f921985"></a>

### `AMEBA_UART3_RXD`

```c
#define AMEBA_UART3_RXD 104
```

UART3 RXD 功能（UART3 RXD Function）。

<a id="a75bcfb713ccf540f3a1ccc04310ce081"></a>

### `AMEBA_UART3_TXD`

```c
#define AMEBA_UART3_TXD 103
```

UART3 TXD 功能（UART3 TXD Function）。

<a id="a7e308adb3b91184da493a706c1b382ec"></a>

### `AMEBA_UART_LOG_RXD`

```c
#define AMEBA_UART_LOG_RXD 156
```

UART LOG RXD 功能（UART LOG RXD Function）。

<a id="a4aafb8bb1e2a9a080ee96c7f9d97a631"></a>

### `AMEBA_UART_LOG_TXD`

```c
#define AMEBA_UART_LOG_TXD 157
```

UART LOG TXD 功能（UART LOG TXD Function）。

<a id="adfeeeb74cd0157b09992ec5e5f4e5397"></a>

### `AMEBA_USB`

```c
#define AMEBA_USB 7
```

USB 功能（USB Function）。

<a id="a92cd123103ff092048b8f56290010431"></a>

### `AMEBA_WLAN_ACT`

```c
#define AMEBA_WLAN_ACT 143
```

WLAN ACT 功能（WLAN ACT Function）。

<a id="a6720be2fe65055f8a56f0d5634ad1822"></a>

### `AMEBA_ZB_GRANT`

```c
#define AMEBA_ZB_GRANT 148
```

ZB GRANT 功能（ZB GRANT Function）。

<a id="ad8dd8552461df7cba8cda72fa02af8bd"></a>

### `AMEBA_ZB_PRI`

```c
#define AMEBA_ZB_PRI 149
```

ZB PRI 功能（ZB PRI Function）。

<a id="a52052e6f01e49f0edfcbd2c57300ffdb"></a>

### `AMEBA_ZB_REQ`

```c
#define AMEBA_ZB_REQ 147
```

ZB REQ 功能（ZB REQ Function）。


## 4.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P029_amebag2-pinctrl.h_源码浏览.md)
- [AMEBA_PORT_PIN](../api_file_reference/P011_zephyr__dt-bindings__pinctrl__amebad-pinctrl.h_文件参考.md#a01f0e522a7c41526681b766c7ac7ce1f)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="aamebad-pinctrl_8h_html_a01f0e522a7c41526681b766c7ac7ce1f"></a>

---

[上一章](P003_zephyr__dt-bindings__pinctrl__alif-ensemble-pinctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P005_zephyr__dt-bindings__pinctrl__esp32p4-gpio-sigmap.h_文件参考.md)
