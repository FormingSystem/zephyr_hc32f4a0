---
id: learning.zephyr-docs.api-file-runtime-reference.page-59
title: zephyr__dt-bindings__pinctrl__smartbond-pinctrl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/smartbond-pinctrl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第59章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_smartbond-pinctrl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/smartbond-pinctrl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 59.1\_宏定义（Macros）

<a id="r_a7089e1e95fff22ba99344704b7f731b7"></a>

```c
#define SMARTBOND_FUNC_GPIO 0
```

相关声明：[SMARTBOND_FUNC_GPIO](#a7089e1e95fff22ba99344704b7f731b7)。

引脚功能定义（Pin Function Definitions）。

<a id="r_a6ed07d7b66f1b82356a972237319ac9b"></a>

```c
#define SMARTBOND_FUNC_UART_RX 1
```

相关声明：[SMARTBOND_FUNC_UART_RX](#a6ed07d7b66f1b82356a972237319ac9b)。

<a id="r_a5dfe9979613105acf742ea4c64afb8f2"></a>

```c
#define SMARTBOND_FUNC_UART_TX 2
```

相关声明：[SMARTBOND_FUNC_UART_TX](#a5dfe9979613105acf742ea4c64afb8f2)。

<a id="r_ad9b9d93fd00717dba1a32feac99a760a"></a>

```c
#define SMARTBOND_FUNC_UART2_RX 3
```

相关声明：[SMARTBOND_FUNC_UART2_RX](#ad9b9d93fd00717dba1a32feac99a760a)。

<a id="r_ab8dc0782b4c39f9f04bffbd68e201b07"></a>

```c
#define SMARTBOND_FUNC_UART2_TX 4
```

相关声明：[SMARTBOND_FUNC_UART2_TX](#ab8dc0782b4c39f9f04bffbd68e201b07)。

<a id="r_a28291720995487ed1909701d27bb6608"></a>

```c
#define SMARTBOND_FUNC_UART2_CTSN 5
```

相关声明：[SMARTBOND_FUNC_UART2_CTSN](#a28291720995487ed1909701d27bb6608)。

<a id="r_aea2618531f8eca9f53a66df1c2e40cbe"></a>

```c
#define SMARTBOND_FUNC_UART2_RTSN 6
```

相关声明：[SMARTBOND_FUNC_UART2_RTSN](#aea2618531f8eca9f53a66df1c2e40cbe)。

<a id="r_a5b3943d551d13bdd36407145262a56f9"></a>

```c
#define SMARTBOND_FUNC_UART3_RX 7
```

相关声明：[SMARTBOND_FUNC_UART3_RX](#a5b3943d551d13bdd36407145262a56f9)。

<a id="r_aa0d293e2a1c45c9f4a8b33b81d0efe09"></a>

```c
#define SMARTBOND_FUNC_UART3_TX 8
```

相关声明：[SMARTBOND_FUNC_UART3_TX](#aa0d293e2a1c45c9f4a8b33b81d0efe09)。

<a id="r_ab78ba1d4ce9f4551480a8245439607f2"></a>

```c
#define SMARTBOND_FUNC_UART3_CTSN 9
```

相关声明：[SMARTBOND_FUNC_UART3_CTSN](#ab78ba1d4ce9f4551480a8245439607f2)。

<a id="r_a34305c8d6c03afebd72736e274f34c86"></a>

```c
#define SMARTBOND_FUNC_UART3_RTSN 10
```

相关声明：[SMARTBOND_FUNC_UART3_RTSN](#a34305c8d6c03afebd72736e274f34c86)。

<a id="r_acf912059ad7e32d8241f6c7881c4cb28"></a>

```c
#define SMARTBOND_FUNC_ISO_CLK 11
```

相关声明：[SMARTBOND_FUNC_ISO_CLK](#acf912059ad7e32d8241f6c7881c4cb28)。

<a id="r_aac93ef7075ed12f86b829bd705c7400a"></a>

```c
#define SMARTBOND_FUNC_ISO_DATA 12
```

相关声明：[SMARTBOND_FUNC_ISO_DATA](#aac93ef7075ed12f86b829bd705c7400a)。

<a id="r_a43277e708883b30efd1fa2360801c9ea"></a>

```c
#define SMARTBOND_FUNC_SPI_DI 13
```

相关声明：[SMARTBOND_FUNC_SPI_DI](#a43277e708883b30efd1fa2360801c9ea)。

<a id="r_a64d7cd483d90e3b1102243c191d189eb"></a>

```c
#define SMARTBOND_FUNC_SPI_DO 14
```

相关声明：[SMARTBOND_FUNC_SPI_DO](#a64d7cd483d90e3b1102243c191d189eb)。

<a id="r_a7b9f3eec74e21b5b2aaef12c234bea64"></a>

```c
#define SMARTBOND_FUNC_SPI_CLK 15
```

相关声明：[SMARTBOND_FUNC_SPI_CLK](#a7b9f3eec74e21b5b2aaef12c234bea64)。

<a id="r_a41d2f9824fb7d591b61482431b39d049"></a>

```c
#define SMARTBOND_FUNC_SPI_EN 16
```

相关声明：[SMARTBOND_FUNC_SPI_EN](#a41d2f9824fb7d591b61482431b39d049)。

<a id="r_acab6331b3ee09ed93b7963c9e3c4e0e7"></a>

```c
#define SMARTBOND_FUNC_SPI2_DI 17
```

相关声明：[SMARTBOND_FUNC_SPI2_DI](#acab6331b3ee09ed93b7963c9e3c4e0e7)。

<a id="r_ae0282ae5f03793c9c8af9d7affeefe23"></a>

```c
#define SMARTBOND_FUNC_SPI2_DO 18
```

相关声明：[SMARTBOND_FUNC_SPI2_DO](#ae0282ae5f03793c9c8af9d7affeefe23)。

<a id="r_abb67eca8ba3b48ab5436a4609f1a633f"></a>

```c
#define SMARTBOND_FUNC_SPI2_CLK 19
```

相关声明：[SMARTBOND_FUNC_SPI2_CLK](#abb67eca8ba3b48ab5436a4609f1a633f)。

<a id="r_abe46de2948d1c93a938511a78f7a762f"></a>

```c
#define SMARTBOND_FUNC_SPI2_EN 20
```

相关声明：[SMARTBOND_FUNC_SPI2_EN](#abe46de2948d1c93a938511a78f7a762f)。

<a id="r_a5b5f41a1016d0430196ee473cbc7a2c5"></a>

```c
#define SMARTBOND_FUNC_I2C_SCL 21
```

相关声明：[SMARTBOND_FUNC_I2C_SCL](#a5b5f41a1016d0430196ee473cbc7a2c5)。

<a id="r_a3a8535069c0b427b0f970248563739fe"></a>

```c
#define SMARTBOND_FUNC_I2C_SDA 22
```

相关声明：[SMARTBOND_FUNC_I2C_SDA](#a3a8535069c0b427b0f970248563739fe)。

<a id="r_ada4dba2404b4f79eb57ad2a8865c94e4"></a>

```c
#define SMARTBOND_FUNC_I2C2_SCL 23
```

相关声明：[SMARTBOND_FUNC_I2C2_SCL](#ada4dba2404b4f79eb57ad2a8865c94e4)。

<a id="r_ac456dcf0d16f720e6f19459eb11f7ef3"></a>

```c
#define SMARTBOND_FUNC_I2C2_SDA 24
```

相关声明：[SMARTBOND_FUNC_I2C2_SDA](#ac456dcf0d16f720e6f19459eb11f7ef3)。

<a id="r_a5613a9d97ed91227f724e632cd3a995a"></a>

```c
#define SMARTBOND_FUNC_USB_SOF 25
```

相关声明：[SMARTBOND_FUNC_USB_SOF](#a5613a9d97ed91227f724e632cd3a995a)。

<a id="r_a93ae4c46ba7233a074cae8a9750e3246"></a>

```c
#define SMARTBOND_FUNC_ADC 26
```

相关声明：[SMARTBOND_FUNC_ADC](#a93ae4c46ba7233a074cae8a9750e3246)。

<a id="r_af55696a1a2c476841085901eb030bf06"></a>

```c
#define SMARTBOND_FUNC_USB 27
```

相关声明：[SMARTBOND_FUNC_USB](#af55696a1a2c476841085901eb030bf06)。

<a id="r_aa8f8d6b30ff693e02863aebce0fda1f7"></a>

```c
#define SMARTBOND_FUNC_PCM_DI 28
```

相关声明：[SMARTBOND_FUNC_PCM_DI](#aa8f8d6b30ff693e02863aebce0fda1f7)。

<a id="r_a8d2af85827bae92e3323ae7af6795d39"></a>

```c
#define SMARTBOND_FUNC_PCM_DO 29
```

相关声明：[SMARTBOND_FUNC_PCM_DO](#a8d2af85827bae92e3323ae7af6795d39)。

<a id="r_a0350a10a2a18f35042eb1d1380d06e71"></a>

```c
#define SMARTBOND_FUNC_PCM_FSC 30
```

相关声明：[SMARTBOND_FUNC_PCM_FSC](#a0350a10a2a18f35042eb1d1380d06e71)。

<a id="r_ab966d361e29c0a4bec64edb8f1f13fcd"></a>

```c
#define SMARTBOND_FUNC_PCM_CLK 31
```

相关声明：[SMARTBOND_FUNC_PCM_CLK](#ab966d361e29c0a4bec64edb8f1f13fcd)。

<a id="r_a41038d013590b0fa06e0009071e77913"></a>

```c
#define SMARTBOND_FUNC_PDM_DATA 32
```

相关声明：[SMARTBOND_FUNC_PDM_DATA](#a41038d013590b0fa06e0009071e77913)。

<a id="r_a9c6dc0a72667b6659761fb900e6cb74e"></a>

```c
#define SMARTBOND_FUNC_PDM_CLK 33
```

相关声明：[SMARTBOND_FUNC_PDM_CLK](#a9c6dc0a72667b6659761fb900e6cb74e)。

<a id="r_a10e19e7f0d69a912341211e18d88d9fb"></a>

```c
#define SMARTBOND_FUNC_COEX_EXT_ACT 34
```

相关声明：[SMARTBOND_FUNC_COEX_EXT_ACT](#a10e19e7f0d69a912341211e18d88d9fb)。

<a id="r_a7e470cb7f8deb22199ac0fb2ec7e6867"></a>

```c
#define SMARTBOND_FUNC_COEX_SMART_ACT 35
```

相关声明：[SMARTBOND_FUNC_COEX_SMART_ACT](#a7e470cb7f8deb22199ac0fb2ec7e6867)。

<a id="r_a17ad842b2c1dfa9f7d2cf8ec9ec67589"></a>

```c
#define SMARTBOND_FUNC_COEX_SMART_PRI 36
```

相关声明：[SMARTBOND_FUNC_COEX_SMART_PRI](#a17ad842b2c1dfa9f7d2cf8ec9ec67589)。

<a id="r_ada643666dd9d0e7423c01b1852d01e08"></a>

```c
#define SMARTBOND_FUNC_PORT0_DCF 37
```

相关声明：[SMARTBOND_FUNC_PORT0_DCF](#ada643666dd9d0e7423c01b1852d01e08)。

<a id="r_a633ffca67ab63d296c82588a16717ecd"></a>

```c
#define SMARTBOND_FUNC_PORT1_DCF 38
```

相关声明：[SMARTBOND_FUNC_PORT1_DCF](#a633ffca67ab63d296c82588a16717ecd)。

<a id="r_ae269c4303f7cbb595d015805870d489a"></a>

```c
#define SMARTBOND_FUNC_PORT2_DCF 39
```

相关声明：[SMARTBOND_FUNC_PORT2_DCF](#ae269c4303f7cbb595d015805870d489a)。

<a id="r_aee13677eb591c737d9aa87a56d5ab60e"></a>

```c
#define SMARTBOND_FUNC_PORT3_DCF 40
```

相关声明：[SMARTBOND_FUNC_PORT3_DCF](#aee13677eb591c737d9aa87a56d5ab60e)。

<a id="r_a575776c065bdf0795f03931ef32a8014"></a>

```c
#define SMARTBOND_FUNC_PORT4_DCF 41
```

相关声明：[SMARTBOND_FUNC_PORT4_DCF](#a575776c065bdf0795f03931ef32a8014)。

<a id="r_adf15b25b1e76a63945454870bf8a5880"></a>

```c
#define SMARTBOND_FUNC_CLOCK 42
```

相关声明：[SMARTBOND_FUNC_CLOCK](#adf15b25b1e76a63945454870bf8a5880)。

<a id="r_a2710985bfb03536edebe925e42701372"></a>

```c
#define SMARTBOND_FUNC_PG 43
```

相关声明：[SMARTBOND_FUNC_PG](#a2710985bfb03536edebe925e42701372)。

<a id="r_a7131a57cb82a1fc7dff9e626dfaed3fa"></a>

```c
#define SMARTBOND_FUNC_LCD 44
```

相关声明：[SMARTBOND_FUNC_LCD](#a7131a57cb82a1fc7dff9e626dfaed3fa)。

<a id="r_ac101bc374eb5a717b7bf8188683c2f2e"></a>

```c
#define SMARTBOND_FUNC_LCD_SPI_DC 45
```

相关声明：[SMARTBOND_FUNC_LCD_SPI_DC](#ac101bc374eb5a717b7bf8188683c2f2e)。

<a id="r_a02d15016a20227a7470db3ce37b32ae9"></a>

```c
#define SMARTBOND_FUNC_LCD_SPI_DO 46
```

相关声明：[SMARTBOND_FUNC_LCD_SPI_DO](#a02d15016a20227a7470db3ce37b32ae9)。

<a id="r_ae17f0095eb1536bf0f477618d7f7d074"></a>

```c
#define SMARTBOND_FUNC_LCD_SPI_CLK 47
```

相关声明：[SMARTBOND_FUNC_LCD_SPI_CLK](#ae17f0095eb1536bf0f477618d7f7d074)。

<a id="r_af7e0123b209509f766bdee6fd5473456"></a>

```c
#define SMARTBOND_FUNC_LCD_SPI_EN 48
```

相关声明：[SMARTBOND_FUNC_LCD_SPI_EN](#af7e0123b209509f766bdee6fd5473456)。

<a id="r_afe4022d7379a973034954b15e838f90c"></a>

```c
#define SMARTBOND_FUNC_TIM_PWM 49
```

相关声明：[SMARTBOND_FUNC_TIM_PWM](#afe4022d7379a973034954b15e838f90c)。

<a id="r_a107f8c0c3a54d5fb01efa35f31edc6f9"></a>

```c
#define SMARTBOND_FUNC_TIM2_PWM 50
```

相关声明：[SMARTBOND_FUNC_TIM2_PWM](#a107f8c0c3a54d5fb01efa35f31edc6f9)。

<a id="r_aa569b7d607bb41d6cc856e177aa2aff9"></a>

```c
#define SMARTBOND_FUNC_TIM_1SHOT 51
```

相关声明：[SMARTBOND_FUNC_TIM_1SHOT](#aa569b7d607bb41d6cc856e177aa2aff9)。

<a id="r_af9ed3f5a6c23379de2cdc58ce2856e66"></a>

```c
#define SMARTBOND_FUNC_TIM2_1SHOT 52
```

相关声明：[SMARTBOND_FUNC_TIM2_1SHOT](#af9ed3f5a6c23379de2cdc58ce2856e66)。

<a id="r_a5a613b7538c4ae1252375f36f71128c4"></a>

```c
#define SMARTBOND_FUNC_TIM3_PWM 53
```

相关声明：[SMARTBOND_FUNC_TIM3_PWM](#a5a613b7538c4ae1252375f36f71128c4)。

<a id="r_a4aee45714b4104a48e1bebbcae2a1660"></a>

```c
#define SMARTBOND_FUNC_TIM4_PWM 54
```

相关声明：[SMARTBOND_FUNC_TIM4_PWM](#a4aee45714b4104a48e1bebbcae2a1660)。

<a id="r_a50e52287199ec82f928e24e9d12fa97b"></a>

```c
#define SMARTBOND_PINMUX_PIN_POS 0
```

相关声明：[SMARTBOND_PINMUX_PIN_POS](#a50e52287199ec82f928e24e9d12fa97b)。

引脚复用（Pinmux）中位位置（Bit Positions）和位掩码（Bit Masks）的定义。

<a id="r_ae48f1167f7190d6acc13d1890ec6f141"></a>

```c
#define SMARTBOND_PINMUX_PIN_MASK 0x1f
```

相关声明：[SMARTBOND_PINMUX_PIN_MASK](#ae48f1167f7190d6acc13d1890ec6f141)。

<a id="r_ab4cec4ecf671814e804cb3ad18236ac4"></a>

```c
#define SMARTBOND_PINMUX_PORT_POS 5
```

相关声明：[SMARTBOND_PINMUX_PORT_POS](#ab4cec4ecf671814e804cb3ad18236ac4)。

<a id="r_a8e82ad973c84c8b36240821fda17c07b"></a>

```c
#define SMARTBOND_PINMUX_PORT_MASK 0x01
```

相关声明：[SMARTBOND_PINMUX_PORT_MASK](#a8e82ad973c84c8b36240821fda17c07b)。

<a id="r_a0ed3e3f31e62d585a48fdfa04decf854"></a>

```c
#define SMARTBOND_PINMUX_FUNC_POS 6
```

相关声明：[SMARTBOND_PINMUX_FUNC_POS](#a0ed3e3f31e62d585a48fdfa04decf854)。

<a id="r_a4dae490f035db9e564d95cb62ceb101c"></a>

```c
#define SMARTBOND_PINMUX_FUNC_MASK 0xff
```

相关声明：[SMARTBOND_PINMUX_FUNC_MASK](#a4dae490f035db9e564d95cb62ceb101c)。

<a id="r_a66c942c39b093b0dbd3d174d6265600c"></a>

```c
#define SMARTBOND_PINMUX(func, port, pin)
```

相关声明：[SMARTBOND_PINMUX](#a66c942c39b093b0dbd3d174d6265600c)。

创建引脚复用配置（Pinmux）的工具宏（Utility Macro）。

## 59.2\_详细说明（Detailed Documentation）

<a id="a93ae4c46ba7233a074cae8a9750e3246"></a>

### `SMARTBOND_FUNC_ADC`

```c
#define SMARTBOND_FUNC_ADC 26
```

<a id="adf15b25b1e76a63945454870bf8a5880"></a>

### `SMARTBOND_FUNC_CLOCK`

```c
#define SMARTBOND_FUNC_CLOCK 42
```

<a id="a10e19e7f0d69a912341211e18d88d9fb"></a>

### `SMARTBOND_FUNC_COEX_EXT_ACT`

```c
#define SMARTBOND_FUNC_COEX_EXT_ACT 34
```

<a id="a7e470cb7f8deb22199ac0fb2ec7e6867"></a>

### `SMARTBOND_FUNC_COEX_SMART_ACT`

```c
#define SMARTBOND_FUNC_COEX_SMART_ACT 35
```

<a id="a17ad842b2c1dfa9f7d2cf8ec9ec67589"></a>

### `SMARTBOND_FUNC_COEX_SMART_PRI`

```c
#define SMARTBOND_FUNC_COEX_SMART_PRI 36
```

<a id="a7089e1e95fff22ba99344704b7f731b7"></a>

### `SMARTBOND_FUNC_GPIO`

```c
#define SMARTBOND_FUNC_GPIO 0
```

引脚功能定义（Pin Function Definitions）。

<a id="ada4dba2404b4f79eb57ad2a8865c94e4"></a>

### `SMARTBOND_FUNC_I2C2_SCL`

```c
#define SMARTBOND_FUNC_I2C2_SCL 23
```

<a id="ac456dcf0d16f720e6f19459eb11f7ef3"></a>

### `SMARTBOND_FUNC_I2C2_SDA`

```c
#define SMARTBOND_FUNC_I2C2_SDA 24
```

<a id="a5b5f41a1016d0430196ee473cbc7a2c5"></a>

### `SMARTBOND_FUNC_I2C_SCL`

```c
#define SMARTBOND_FUNC_I2C_SCL 21
```

<a id="a3a8535069c0b427b0f970248563739fe"></a>

### `SMARTBOND_FUNC_I2C_SDA`

```c
#define SMARTBOND_FUNC_I2C_SDA 22
```

<a id="acf912059ad7e32d8241f6c7881c4cb28"></a>

### `SMARTBOND_FUNC_ISO_CLK`

```c
#define SMARTBOND_FUNC_ISO_CLK 11
```

<a id="aac93ef7075ed12f86b829bd705c7400a"></a>

### `SMARTBOND_FUNC_ISO_DATA`

```c
#define SMARTBOND_FUNC_ISO_DATA 12
```

<a id="a7131a57cb82a1fc7dff9e626dfaed3fa"></a>

### `SMARTBOND_FUNC_LCD`

```c
#define SMARTBOND_FUNC_LCD 44
```

<a id="ae17f0095eb1536bf0f477618d7f7d074"></a>

### `SMARTBOND_FUNC_LCD_SPI_CLK`

```c
#define SMARTBOND_FUNC_LCD_SPI_CLK 47
```

<a id="ac101bc374eb5a717b7bf8188683c2f2e"></a>

### `SMARTBOND_FUNC_LCD_SPI_DC`

```c
#define SMARTBOND_FUNC_LCD_SPI_DC 45
```

<a id="a02d15016a20227a7470db3ce37b32ae9"></a>

### `SMARTBOND_FUNC_LCD_SPI_DO`

```c
#define SMARTBOND_FUNC_LCD_SPI_DO 46
```

<a id="af7e0123b209509f766bdee6fd5473456"></a>

### `SMARTBOND_FUNC_LCD_SPI_EN`

```c
#define SMARTBOND_FUNC_LCD_SPI_EN 48
```

<a id="ab966d361e29c0a4bec64edb8f1f13fcd"></a>

### `SMARTBOND_FUNC_PCM_CLK`

```c
#define SMARTBOND_FUNC_PCM_CLK 31
```

<a id="aa8f8d6b30ff693e02863aebce0fda1f7"></a>

### `SMARTBOND_FUNC_PCM_DI`

```c
#define SMARTBOND_FUNC_PCM_DI 28
```

<a id="a8d2af85827bae92e3323ae7af6795d39"></a>

### `SMARTBOND_FUNC_PCM_DO`

```c
#define SMARTBOND_FUNC_PCM_DO 29
```

<a id="a0350a10a2a18f35042eb1d1380d06e71"></a>

### `SMARTBOND_FUNC_PCM_FSC`

```c
#define SMARTBOND_FUNC_PCM_FSC 30
```

<a id="a9c6dc0a72667b6659761fb900e6cb74e"></a>

### `SMARTBOND_FUNC_PDM_CLK`

```c
#define SMARTBOND_FUNC_PDM_CLK 33
```

<a id="a41038d013590b0fa06e0009071e77913"></a>

### `SMARTBOND_FUNC_PDM_DATA`

```c
#define SMARTBOND_FUNC_PDM_DATA 32
```

<a id="a2710985bfb03536edebe925e42701372"></a>

### `SMARTBOND_FUNC_PG`

```c
#define SMARTBOND_FUNC_PG 43
```

<a id="ada643666dd9d0e7423c01b1852d01e08"></a>

### `SMARTBOND_FUNC_PORT0_DCF`

```c
#define SMARTBOND_FUNC_PORT0_DCF 37
```

<a id="a633ffca67ab63d296c82588a16717ecd"></a>

### `SMARTBOND_FUNC_PORT1_DCF`

```c
#define SMARTBOND_FUNC_PORT1_DCF 38
```

<a id="ae269c4303f7cbb595d015805870d489a"></a>

### `SMARTBOND_FUNC_PORT2_DCF`

```c
#define SMARTBOND_FUNC_PORT2_DCF 39
```

<a id="aee13677eb591c737d9aa87a56d5ab60e"></a>

### `SMARTBOND_FUNC_PORT3_DCF`

```c
#define SMARTBOND_FUNC_PORT3_DCF 40
```

<a id="a575776c065bdf0795f03931ef32a8014"></a>

### `SMARTBOND_FUNC_PORT4_DCF`

```c
#define SMARTBOND_FUNC_PORT4_DCF 41
```

<a id="abb67eca8ba3b48ab5436a4609f1a633f"></a>

### `SMARTBOND_FUNC_SPI2_CLK`

```c
#define SMARTBOND_FUNC_SPI2_CLK 19
```

<a id="acab6331b3ee09ed93b7963c9e3c4e0e7"></a>

### `SMARTBOND_FUNC_SPI2_DI`

```c
#define SMARTBOND_FUNC_SPI2_DI 17
```

<a id="ae0282ae5f03793c9c8af9d7affeefe23"></a>

### `SMARTBOND_FUNC_SPI2_DO`

```c
#define SMARTBOND_FUNC_SPI2_DO 18
```

<a id="abe46de2948d1c93a938511a78f7a762f"></a>

### `SMARTBOND_FUNC_SPI2_EN`

```c
#define SMARTBOND_FUNC_SPI2_EN 20
```

<a id="a7b9f3eec74e21b5b2aaef12c234bea64"></a>

### `SMARTBOND_FUNC_SPI_CLK`

```c
#define SMARTBOND_FUNC_SPI_CLK 15
```

<a id="a43277e708883b30efd1fa2360801c9ea"></a>

### `SMARTBOND_FUNC_SPI_DI`

```c
#define SMARTBOND_FUNC_SPI_DI 13
```

<a id="a64d7cd483d90e3b1102243c191d189eb"></a>

### `SMARTBOND_FUNC_SPI_DO`

```c
#define SMARTBOND_FUNC_SPI_DO 14
```

<a id="a41d2f9824fb7d591b61482431b39d049"></a>

### `SMARTBOND_FUNC_SPI_EN`

```c
#define SMARTBOND_FUNC_SPI_EN 16
```

<a id="af9ed3f5a6c23379de2cdc58ce2856e66"></a>

### `SMARTBOND_FUNC_TIM2_1SHOT`

```c
#define SMARTBOND_FUNC_TIM2_1SHOT 52
```

<a id="a107f8c0c3a54d5fb01efa35f31edc6f9"></a>

### `SMARTBOND_FUNC_TIM2_PWM`

```c
#define SMARTBOND_FUNC_TIM2_PWM 50
```

<a id="a5a613b7538c4ae1252375f36f71128c4"></a>

### `SMARTBOND_FUNC_TIM3_PWM`

```c
#define SMARTBOND_FUNC_TIM3_PWM 53
```

<a id="a4aee45714b4104a48e1bebbcae2a1660"></a>

### `SMARTBOND_FUNC_TIM4_PWM`

```c
#define SMARTBOND_FUNC_TIM4_PWM 54
```

<a id="aa569b7d607bb41d6cc856e177aa2aff9"></a>

### `SMARTBOND_FUNC_TIM_1SHOT`

```c
#define SMARTBOND_FUNC_TIM_1SHOT 51
```

<a id="afe4022d7379a973034954b15e838f90c"></a>

### `SMARTBOND_FUNC_TIM_PWM`

```c
#define SMARTBOND_FUNC_TIM_PWM 49
```

<a id="a28291720995487ed1909701d27bb6608"></a>

### `SMARTBOND_FUNC_UART2_CTSN`

```c
#define SMARTBOND_FUNC_UART2_CTSN 5
```

<a id="aea2618531f8eca9f53a66df1c2e40cbe"></a>

### `SMARTBOND_FUNC_UART2_RTSN`

```c
#define SMARTBOND_FUNC_UART2_RTSN 6
```

<a id="ad9b9d93fd00717dba1a32feac99a760a"></a>

### `SMARTBOND_FUNC_UART2_RX`

```c
#define SMARTBOND_FUNC_UART2_RX 3
```

<a id="ab8dc0782b4c39f9f04bffbd68e201b07"></a>

### `SMARTBOND_FUNC_UART2_TX`

```c
#define SMARTBOND_FUNC_UART2_TX 4
```

<a id="ab78ba1d4ce9f4551480a8245439607f2"></a>

### `SMARTBOND_FUNC_UART3_CTSN`

```c
#define SMARTBOND_FUNC_UART3_CTSN 9
```

<a id="a34305c8d6c03afebd72736e274f34c86"></a>

### `SMARTBOND_FUNC_UART3_RTSN`

```c
#define SMARTBOND_FUNC_UART3_RTSN 10
```

<a id="a5b3943d551d13bdd36407145262a56f9"></a>

### `SMARTBOND_FUNC_UART3_RX`

```c
#define SMARTBOND_FUNC_UART3_RX 7
```

<a id="aa0d293e2a1c45c9f4a8b33b81d0efe09"></a>

### `SMARTBOND_FUNC_UART3_TX`

```c
#define SMARTBOND_FUNC_UART3_TX 8
```

<a id="a6ed07d7b66f1b82356a972237319ac9b"></a>

### `SMARTBOND_FUNC_UART_RX`

```c
#define SMARTBOND_FUNC_UART_RX 1
```

<a id="a5dfe9979613105acf742ea4c64afb8f2"></a>

### `SMARTBOND_FUNC_UART_TX`

```c
#define SMARTBOND_FUNC_UART_TX 2
```

<a id="af55696a1a2c476841085901eb030bf06"></a>

### `SMARTBOND_FUNC_USB`

```c
#define SMARTBOND_FUNC_USB 27
```

<a id="a5613a9d97ed91227f724e632cd3a995a"></a>

### `SMARTBOND_FUNC_USB_SOF`

```c
#define SMARTBOND_FUNC_USB_SOF 25
```

<a id="a66c942c39b093b0dbd3d174d6265600c"></a>

### `SMARTBOND_PINMUX`

```c
#define SMARTBOND_PINMUX ( func, port, pin )
```

展开值（Value）：

```c
(((SMARTBOND_FUNC_ ## func) << SMARTBOND_PINMUX_FUNC_POS) |     \
 ((port) << SMARTBOND_PINMUX_PORT_POS) |                        \
 (pin) << SMARTBOND_PINMUX_PIN_POS)
```

创建引脚复用配置（Pinmux）的工具宏（Utility Macro）。

<a id="a4dae490f035db9e564d95cb62ceb101c"></a>

### `SMARTBOND_PINMUX_FUNC_MASK`

```c
#define SMARTBOND_PINMUX_FUNC_MASK 0xff
```

<a id="a0ed3e3f31e62d585a48fdfa04decf854"></a>

### `SMARTBOND_PINMUX_FUNC_POS`

```c
#define SMARTBOND_PINMUX_FUNC_POS 6
```

<a id="ae48f1167f7190d6acc13d1890ec6f141"></a>

### `SMARTBOND_PINMUX_PIN_MASK`

```c
#define SMARTBOND_PINMUX_PIN_MASK 0x1f
```

<a id="a50e52287199ec82f928e24e9d12fa97b"></a>

### `SMARTBOND_PINMUX_PIN_POS`

```c
#define SMARTBOND_PINMUX_PIN_POS 0
```

引脚复用（Pinmux）中位位置（Bit Positions）和位掩码（Bit Masks）的定义。

<a id="a8e82ad973c84c8b36240821fda17c07b"></a>

### `SMARTBOND_PINMUX_PORT_MASK`

```c
#define SMARTBOND_PINMUX_PORT_MASK 0x01
```

<a id="ab4cec4ecf671814e804cb3ad18236ac4"></a>

### `SMARTBOND_PINMUX_PORT_POS`

```c
#define SMARTBOND_PINMUX_PORT_POS 5
```


## 59.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P792_smartbond-pinctrl.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="asmartbond-pinctrl_8h_html_a0ed3e3f31e62d585a48fdfa04decf854"></a>
<a id="asmartbond-pinctrl_8h_html_a50e52287199ec82f928e24e9d12fa97b"></a>
<a id="asmartbond-pinctrl_8h_html_ab4cec4ecf671814e804cb3ad18236ac4"></a>

---

[上一章](P058_zephyr__dt-bindings__pinctrl__rts5817_pinctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P060_zephyr__mgmt__mcumgr__transport__smp_udp.h_文件参考.md)
