---
id: learning.zephyr-docs.api-file-management-reference.page-27
title: zephyr__dt-bindings__pinctrl__lpc11u6x-pinctrl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lpc11u6x-pinctrl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第27章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_lpc11u6x-pinctrl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/lpc11u6x-pinctrl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 27.1\_宏定义（Macros）

<a id="r_ab08f72eae45dd5656aeca24c346c8626"></a>

```c
#define IOCON_FUNC0 0
```

相关声明：[IOCON_FUNC0](#ab08f72eae45dd5656aeca24c346c8626)。

标准数字 I/O 引脚的引脚控制寄存器（pin control register）：

<a id="r_ab6449233bd56957c684b9ad694606e3a"></a>

```c
#define IOCON_FUNC1 1
```

相关声明：[IOCON_FUNC1](#ab6449233bd56957c684b9ad694606e3a)。

<a id="r_a43ebb7abf055ce2491fbba5ef72f6fc7"></a>

```c
#define IOCON_FUNC2 2
```

相关声明：[IOCON_FUNC2](#a43ebb7abf055ce2491fbba5ef72f6fc7)。

<a id="r_ace4708e511b3aa9c352600604331bec0"></a>

```c
#define IOCON_FUNC3 3
```

相关声明：[IOCON_FUNC3](#ace4708e511b3aa9c352600604331bec0)。

<a id="r_ac621b96a2bd1ee57a83ff1af98287a8d"></a>

```c
#define IOCON_FUNC4 4
```

相关声明：[IOCON_FUNC4](#ac621b96a2bd1ee57a83ff1af98287a8d)。

<a id="r_a0f9630599f40a3f96a5887c7e65508a9"></a>

```c
#define IOCON_FUNC5 5
```

相关声明：[IOCON_FUNC5](#a0f9630599f40a3f96a5887c7e65508a9)。

<a id="r_afc593aafe607c88c52864ecb7586ffe9"></a>

```c
#define IOCON_MODE_INACT (0 << 3) /* No pull resistor. */
```

相关声明：[IOCON_MODE_INACT](#afc593aafe607c88c52864ecb7586ffe9)。

<a id="r_a270261df49234519bfd09e076dfcec6c"></a>

```c
#define IOCON_MODE_PULLDOWN (1 << 3) /* Enable pull-down resistor. */
```

相关声明：[IOCON_MODE_PULLDOWN](#a270261df49234519bfd09e076dfcec6c)。

<a id="r_ad8fe947d8e7076d6cec01a5b30261141"></a>

```c
#define IOCON_MODE_PULLUP (2 << 3) /* Enable Pull-up resistor. */
```

相关声明：[IOCON_MODE_PULLUP](#ad8fe947d8e7076d6cec01a5b30261141)。

<a id="r_a53d705841cc362c6f43ffc1370d71726"></a>

```c
#define IOCON_MODE_REPEATER (3 << 3) /* Repeater mode. */
```

相关声明：[IOCON_MODE_REPEATER](#a53d705841cc362c6f43ffc1370d71726)。

<a id="r_afb7c408ac1f52b7b7e46fde3061fe0b7"></a>

```c
#define IOCON_HYS_EN (1 << 5) /* Enable hysteresis. */
```

相关声明：[IOCON_HYS_EN](#afb7c408ac1f52b7b7e46fde3061fe0b7)。

<a id="r_ae1fd1faa316f6c3108b499928f8c9922"></a>

```c
#define IOCON_INV_EN (1 << 6) /* Invert input polarity. */
```

相关声明：[IOCON_INV_EN](#ae1fd1faa316f6c3108b499928f8c9922)。

<a id="r_a9a3d4f3e281c382f795b9a769073d4e4"></a>

```c
#define IOCON_ADMODE_EN (0 << 7) /* Enable analog input mode. */
```

相关声明：[IOCON_ADMODE_EN](#a9a3d4f3e281c382f795b9a769073d4e4)。

<a id="r_a516e9d9bc7b1f3aaefd9d09c6ece74d2"></a>

```c
#define IOCON_DIGMODE_EN (1 << 7) /* Enable digital I/O mode. */
```

相关声明：[IOCON_DIGMODE_EN](#a516e9d9bc7b1f3aaefd9d09c6ece74d2)。

<a id="r_a5a141a4fd02a8a7204cb251e1815b2ff"></a>

```c
#define IOCON_FILTR_DIS (1 << 8) /* Disable noise filtering. */
```

相关声明：[IOCON_FILTR_DIS](#a5a141a4fd02a8a7204cb251e1815b2ff)。

<a id="r_aa7dd24866523506919c8f3fa7a8614a8"></a>

```c
#define IOCON_SFI2C_EN (0 << 8) /* I2C standard mode / Fast-mode. */
```

相关声明：[IOCON_SFI2C_EN](#aa7dd24866523506919c8f3fa7a8614a8)。

<a id="r_a897f505b779e01014e235f1d73745787"></a>

```c
#define IOCON_STDI2C_EN (1 << 8) /* GPIO functionality. */
```

相关声明：[IOCON_STDI2C_EN](#a897f505b779e01014e235f1d73745787)。

<a id="r_a5454c9c23da82b9db63d63866d054989"></a>

```c
#define IOCON_FASTI2C_EN (2 << 8) /* I2C Fast-mode Plus. */
```

相关声明：[IOCON_FASTI2C_EN](#a5454c9c23da82b9db63d63866d054989)。

<a id="r_a226b54f672e61a7a2d2893d9ef8cbc9c"></a>

```c
#define IOCON_OPENDRAIN_EN (1 << 10) /* Enable open-drain mode. */
```

相关声明：[IOCON_OPENDRAIN_EN](#a226b54f672e61a7a2d2893d9ef8cbc9c)、[open](../api_file_reference/P112_zephyr__posix__fcntl.h_文件参考.md#ac843f2e35e60c3bbf1da47d84306f29b)。

<a id="r_a05f3ba263e98d5ee980f1604e5bb901c"></a>

```c
#define IOCON_S_MODE_0CLK (0 << 11) /* No input filter. */
```

相关声明：[IOCON_S_MODE_0CLK](#a05f3ba263e98d5ee980f1604e5bb901c)。

<a id="r_a7148355cde16d13476362ff1c1bc1668"></a>

```c
#define IOCON_S_MODE_1CLK (1 << 11)
```

相关声明：[IOCON_S_MODE_1CLK](#a7148355cde16d13476362ff1c1bc1668)。

<a id="r_a87827c87941a76ce73118c65afb439f5"></a>

```c
#define IOCON_S_MODE_2CLK (2 << 11)
```

相关声明：[IOCON_S_MODE_2CLK](#a87827c87941a76ce73118c65afb439f5)。

<a id="r_a54dba7082ab18b6a15eea0a87c119a71"></a>

```c
#define IOCON_S_MODE_3CLK (3 << 11)
```

相关声明：[IOCON_S_MODE_3CLK](#a54dba7082ab18b6a15eea0a87c119a71)。

<a id="r_a32dad85c69cde862614f7dc694de25e1"></a>

```c
#define IOCON_CLKDIV0 (0 << 13)
```

相关声明：[IOCON_CLKDIV0](#a32dad85c69cde862614f7dc694de25e1)。

<a id="r_a9cf0243a32cce57e52c3b3931979a0c4"></a>

```c
#define IOCON_CLKDIV1 (1 << 13)
```

相关声明：[IOCON_CLKDIV1](#a9cf0243a32cce57e52c3b3931979a0c4)。

<a id="r_a05aed1b2f2679b3bb56a1bdc08e032a1"></a>

```c
#define IOCON_CLKDIV2 (2 << 13)
```

相关声明：[IOCON_CLKDIV2](#a05aed1b2f2679b3bb56a1bdc08e032a1)。

<a id="r_a96b9d2b722278cdc733ddec36aca82b8"></a>

```c
#define IOCON_CLKDIV3 (3 << 13)
```

相关声明：[IOCON_CLKDIV3](#a96b9d2b722278cdc733ddec36aca82b8)。

<a id="r_a293173c3047155fd78ba45a0f4e464f5"></a>

```c
#define IOCON_CLKDIV4 (4 << 13)
```

相关声明：[IOCON_CLKDIV4](#a293173c3047155fd78ba45a0f4e464f5)。

<a id="r_aecba1dab2a9cb8c19052ab56c7efbc6d"></a>

```c
#define IOCON_CLKDIV5 (5 << 13)
```

相关声明：[IOCON_CLKDIV5](#aecba1dab2a9cb8c19052ab56c7efbc6d)。

<a id="r_a25f5cc1afc44889d9e77b62923135411"></a>

```c
#define IOCON_CLKDIV6 (6 << 13)
```

相关声明：[IOCON_CLKDIV6](#a25f5cc1afc44889d9e77b62923135411)。

<a id="r_a3c281dcff389739802d68c2fc59d608e"></a>

```c
#define IOCON_MUX(offset, type, mux)
```

相关声明：[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)。

<a id="r_a9ae60793668890cd0dc2117dc64f02ba"></a>

```c
#define IOCON_TYPE_D 0x0
```

相关声明：[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a6c16820a5170feb2c133f82216318bbb"></a>

```c
#define IOCON_TYPE_I 0x1
```

相关声明：[IOCON_TYPE_I](#a6c16820a5170feb2c133f82216318bbb)。

<a id="r_afd7386a10a00b7f0cfbb44d6ceb66df3"></a>

```c
#define IOCON_TYPE_A 0x2
```

相关声明：[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_abd7869399ab5c12219c1d7e06885e391"></a>

```c
#define RESET_PIO0_0 IOCON_MUX(0, IOCON_TYPE_D, 0) /* PIO0_0 */
```

相关声明：[RESET_PIO0_0](#abd7869399ab5c12219c1d7e06885e391)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_aa1d6732f64540461cae792821ac7b2d6"></a>

```c
#define PIO0_0_PIO0_0 IOCON_MUX(0, IOCON_TYPE_D, 1) /* PIO0_0 */
```

相关声明：[PIO0_0_PIO0_0](#aa1d6732f64540461cae792821ac7b2d6)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_ab44c7ff7f772892dbb66149d8064ba04"></a>

```c
#define PIO0_1_PIO0_1 IOCON_MUX(1, IOCON_TYPE_D, 0) /* PIO0_1 */
```

相关声明：[PIO0_1_PIO0_1](#ab44c7ff7f772892dbb66149d8064ba04)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a4d2452db92940671b276775adec24700"></a>

```c
#define CLKOUT_PIO0_1 IOCON_MUX(1, IOCON_TYPE_D, 1) /* PIO0_1 */
```

相关声明：[CLKOUT_PIO0_1](#a4d2452db92940671b276775adec24700)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_aa6fbfccc166375429d6c720684686a24"></a>

```c
#define CT32B0_MAT2_PIO0_1 IOCON_MUX(1, IOCON_TYPE_D, 2) /* PIO0_1 */
```

相关声明：[CT32B0_MAT2_PIO0_1](#aa6fbfccc166375429d6c720684686a24)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a827fea9b1eb5d3d16dbb1f95bd06b40e"></a>

```c
#define USB_FTOGGLE_PIO0_1 IOCON_MUX(1, IOCON_TYPE_D, 3) /* PIO0_1 */
```

相关声明：[USB_FTOGGLE_PIO0_1](#a827fea9b1eb5d3d16dbb1f95bd06b40e)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_ab5a06c37a003d97135fc0da7c9949f60"></a>

```c
#define PIO0_2_PIO0_2 IOCON_MUX(2, IOCON_TYPE_D, 0) /* PIO0_2 */
```

相关声明：[PIO0_2_PIO0_2](#ab5a06c37a003d97135fc0da7c9949f60)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a883806b472afb21f170006c620fe2b2d"></a>

```c
#define SSP0_SSEL_PIO0_2 IOCON_MUX(2, IOCON_TYPE_D, 1) /* PIO0_2 */
```

相关声明：[SSP0_SSEL_PIO0_2](#a883806b472afb21f170006c620fe2b2d)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a2c44ad39551919eaf469137d3d37f78b"></a>

```c
#define CT16B0_CAP0_PIO0_2 IOCON_MUX(2, IOCON_TYPE_D, 2) /* PIO0_2 */
```

相关声明：[CT16B0_CAP0_PIO0_2](#a2c44ad39551919eaf469137d3d37f78b)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a497b4217421b6854a707201765ff12a8"></a>

```c
#define R_0_PIO0_2 IOCON_MUX(2, IOCON_TYPE_D, 3) /* PIO0_2 */
```

相关声明：[R_0_PIO0_2](#a497b4217421b6854a707201765ff12a8)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a89f6d1689c8672f14033a31543ced43a"></a>

```c
#define PIO0_3_PIO0_3 IOCON_MUX(3, IOCON_TYPE_D, 0) /* PIO0_3 */
```

相关声明：[PIO0_3_PIO0_3](#a89f6d1689c8672f14033a31543ced43a)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a410001d990fb8424e9f6d75f6a7f2c67"></a>

```c
#define USB_VBUS_PIO0_3 IOCON_MUX(3, IOCON_TYPE_D, 1) /* PIO0_3 */
```

相关声明：[USB_VBUS_PIO0_3](#a410001d990fb8424e9f6d75f6a7f2c67)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a54242b6862e052d7d1c2ee998b6d3927"></a>

```c
#define R_1_PIO0_3 IOCON_MUX(3, IOCON_TYPE_D, 2) /* PIO0_3 */
```

相关声明：[R_1_PIO0_3](#a54242b6862e052d7d1c2ee998b6d3927)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a017c42b9bbbacfbbd9310b3f1a918a66"></a>

```c
#define PIO0_4_PIO0_4 IOCON_MUX(4, IOCON_TYPE_I, 0) /* PIO0_4 */
```

相关声明：[PIO0_4_PIO0_4](#a017c42b9bbbacfbbd9310b3f1a918a66)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_I](#a6c16820a5170feb2c133f82216318bbb)。

<a id="r_af03e2705d8630f60521f853e9b4b1d61"></a>

```c
#define I2C0_SCL_PIO0_4 IOCON_MUX(4, IOCON_TYPE_I, 1) /* PIO0_4 */
```

相关声明：[I2C0_SCL_PIO0_4](#af03e2705d8630f60521f853e9b4b1d61)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_I](#a6c16820a5170feb2c133f82216318bbb)。

<a id="r_ab0e34b062fd26c27d29891c77d8542a0"></a>

```c
#define R_2_PIO0_4 IOCON_MUX(4, IOCON_TYPE_I, 2) /* PIO0_4 */
```

相关声明：[R_2_PIO0_4](#ab0e34b062fd26c27d29891c77d8542a0)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_I](#a6c16820a5170feb2c133f82216318bbb)。

<a id="r_aa0fe8d6e7a4f69dd54980143f92df7ab"></a>

```c
#define PIO0_5_PIO0_5 IOCON_MUX(5, IOCON_TYPE_I, 0) /* PIO0_5 */
```

相关声明：[PIO0_5_PIO0_5](#aa0fe8d6e7a4f69dd54980143f92df7ab)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_I](#a6c16820a5170feb2c133f82216318bbb)。

<a id="r_a7a30f5f10c3c59925e18d0526fa94431"></a>

```c
#define I2C0_SDA_PIO0_5 IOCON_MUX(5, IOCON_TYPE_I, 1) /* PIO0_5 */
```

相关声明：[I2C0_SDA_PIO0_5](#a7a30f5f10c3c59925e18d0526fa94431)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_I](#a6c16820a5170feb2c133f82216318bbb)。

<a id="r_a372339383fc7d4d6e70965b744c10e48"></a>

```c
#define R_3_PIO0_5 IOCON_MUX(5, IOCON_TYPE_I, 2) /* PIO0_5 */
```

相关声明：[R_3_PIO0_5](#a372339383fc7d4d6e70965b744c10e48)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_I](#a6c16820a5170feb2c133f82216318bbb)。

<a id="r_a50ab17a232562ebc41deb8238de35f20"></a>

```c
#define PIO0_6_PIO0_6 IOCON_MUX(6, IOCON_TYPE_D, 0) /* PIO0_6 */
```

相关声明：[PIO0_6_PIO0_6](#a50ab17a232562ebc41deb8238de35f20)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a0d784ee93461dd2f05beeb7c9cfa46b7"></a>

```c
#define R_PIO0_6 IOCON_MUX(6, IOCON_TYPE_D, 1) /* PIO0_6 */
```

相关声明：[R_PIO0_6](#a0d784ee93461dd2f05beeb7c9cfa46b7)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a632c9844b7638e69f8846b845dce32f7"></a>

```c
#define SSP0_SCK_PIO0_6 IOCON_MUX(6, IOCON_TYPE_D, 2) /* PIO0_6 */
```

相关声明：[SSP0_SCK_PIO0_6](#a632c9844b7638e69f8846b845dce32f7)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a49f11eb792f5b0a7ecf80aeaa82291e2"></a>

```c
#define R_4_PIO0_6 IOCON_MUX(6, IOCON_TYPE_D, 3) /* PIO0_6 */
```

相关声明：[R_4_PIO0_6](#a49f11eb792f5b0a7ecf80aeaa82291e2)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a95b8cc1a76a6097556568f4554bf4e3f"></a>

```c
#define PIO0_7_PIO0_7 IOCON_MUX(7, IOCON_TYPE_D, 0) /* PIO0_7 */
```

相关声明：[PIO0_7_PIO0_7](#a95b8cc1a76a6097556568f4554bf4e3f)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_aad418e1711b045ea50806d464c92fbcf"></a>

```c
#define U0_CTS_PIO0_7 IOCON_MUX(7, IOCON_TYPE_D, 1) /* PIO0_7 */
```

相关声明：[U0_CTS_PIO0_7](#aad418e1711b045ea50806d464c92fbcf)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_aea308935da9604f8bdfea4d58959e518"></a>

```c
#define R_5_PIO0_7 IOCON_MUX(7, IOCON_TYPE_D, 2) /* PIO0_7 */
```

相关声明：[R_5_PIO0_7](#aea308935da9604f8bdfea4d58959e518)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a747ec67e7cb403d747b9f57429b71983"></a>

```c
#define I2C1_SCL_PIO0_7 IOCON_MUX(7, IOCON_TYPE_D, 3) /* PIO0_7 */
```

相关声明：[I2C1_SCL_PIO0_7](#a747ec67e7cb403d747b9f57429b71983)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a9e4b255125ef44e2de5c77743b4010ee"></a>

```c
#define PIO0_8_PIO0_8 IOCON_MUX(8, IOCON_TYPE_D, 0) /* PIO0_8 */
```

相关声明：[PIO0_8_PIO0_8](#a9e4b255125ef44e2de5c77743b4010ee)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a1d448d4e7bfeed79bc6e3fb14947afa7"></a>

```c
#define SSP0_MISO_PIO0_8 IOCON_MUX(8, IOCON_TYPE_D, 1) /* PIO0_8 */
```

相关声明：[SSP0_MISO_PIO0_8](#a1d448d4e7bfeed79bc6e3fb14947afa7)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_ad3f05ac410ca8c36aa81a57b635c1bb5"></a>

```c
#define CT16B0_MAT0_PIO0_8 IOCON_MUX(8, IOCON_TYPE_D, 2) /* PIO0_8 */
```

相关声明：[CT16B0_MAT0_PIO0_8](#ad3f05ac410ca8c36aa81a57b635c1bb5)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a8feac8b8845786a001a5dedbd2c749cd"></a>

```c
#define R_6_PIO0_8 IOCON_MUX(8, IOCON_TYPE_D, 3) /* PIO0_8 */
```

相关声明：[R_6_PIO0_8](#a8feac8b8845786a001a5dedbd2c749cd)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a0db63ca26d440f3bc24a48d39fbfcc4b"></a>

```c
#define PIO0_9_PIO0_9 IOCON_MUX(9, IOCON_TYPE_D, 0) /* PIO0_9 */
```

相关声明：[PIO0_9_PIO0_9](#a0db63ca26d440f3bc24a48d39fbfcc4b)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_af1a1f4c533ae4806d692aff574334ebf"></a>

```c
#define SSP0_MOSI_PIO0_9 IOCON_MUX(9, IOCON_TYPE_D, 1) /* PIO0_9 */
```

相关声明：[SSP0_MOSI_PIO0_9](#af1a1f4c533ae4806d692aff574334ebf)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a8f50532277b4b0b30b926e1f67a31cf1"></a>

```c
#define CT16B0_MAT1_PIO0_9 IOCON_MUX(9, IOCON_TYPE_D, 2) /* PIO0_9 */
```

相关声明：[CT16B0_MAT1_PIO0_9](#a8f50532277b4b0b30b926e1f67a31cf1)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_add1b38cd0b4e6b4557b5feeb39df424e"></a>

```c
#define R_7_PIO0_9 IOCON_MUX(9, IOCON_TYPE_D, 3) /* PIO0_9 */
```

相关声明：[R_7_PIO0_9](#add1b38cd0b4e6b4557b5feeb39df424e)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a9694c0dc682d5d6be38b963226aaef3c"></a>

```c
#define SWCLK_PIO0_10 IOCON_MUX(10, IOCON_TYPE_D, 0) /* PIO0_10 */
```

相关声明：[SWCLK_PIO0_10](#a9694c0dc682d5d6be38b963226aaef3c)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a0b09489a89b80784605cddcc430914d6"></a>

```c
#define PIO0_10_PIO0_10 IOCON_MUX(10, IOCON_TYPE_D, 1) /* PIO0_10 */
```

相关声明：[PIO0_10_PIO0_10](#a0b09489a89b80784605cddcc430914d6)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_ad68005dc04bde783a05f6c47da6dc4ef"></a>

```c
#define SSP0_SCK_PIO0_10 IOCON_MUX(10, IOCON_TYPE_D, 2) /* PIO0_10 */
```

相关声明：[SSP0_SCK_PIO0_10](#ad68005dc04bde783a05f6c47da6dc4ef)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_adca5657fc469b0f579f7a42f94ca5261"></a>

```c
#define CT16B0_MAT2_PIO0_10 IOCON_MUX(10, IOCON_TYPE_D, 3) /* PIO0_10 */
```

相关声明：[CT16B0_MAT2_PIO0_10](#adca5657fc469b0f579f7a42f94ca5261)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_afbfb770c4372aadbdb6f5c18d399e17e"></a>

```c
#define TDI_PIO0_11 IOCON_MUX(11, IOCON_TYPE_A, 0) /* PIO0_11 */
```

相关声明：[TDI_PIO0_11](#afbfb770c4372aadbdb6f5c18d399e17e)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_a157b55ccf1883066cc9217629366b809"></a>

```c
#define PIO0_11_PIO0_11 IOCON_MUX(11, IOCON_TYPE_A, 1) /* PIO0_11 */
```

相关声明：[PIO0_11_PIO0_11](#a157b55ccf1883066cc9217629366b809)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_abfeca937f748f0b54ee4178c072ed1f5"></a>

```c
#define ADC_9_PIO0_11 IOCON_MUX(11, IOCON_TYPE_A, 2) /* PIO0_11 */
```

相关声明：[ADC_9_PIO0_11](#abfeca937f748f0b54ee4178c072ed1f5)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_a005db7665d634e68c56b59a3cb5b456d"></a>

```c
#define CT32B0_MAT3_PIO0_11 IOCON_MUX(11, IOCON_TYPE_A, 3) /* PIO0_11 */
```

相关声明：[CT32B0_MAT3_PIO0_11](#a005db7665d634e68c56b59a3cb5b456d)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_aaa87da84c9da4433539b55b513ab932b"></a>

```c
#define U1_RTS_PIO0_11 IOCON_MUX(11, IOCON_TYPE_A, 4) /* PIO0_11 */
```

相关声明：[U1_RTS_PIO0_11](#aaa87da84c9da4433539b55b513ab932b)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_a3c5e8df87f093df6858f6ceb7e33e5ec"></a>

```c
#define U1_SCLK_PIO0_11 IOCON_MUX(11, IOCON_TYPE_A, 5) /* PIO0_11 */
```

相关声明：[U1_SCLK_PIO0_11](#a3c5e8df87f093df6858f6ceb7e33e5ec)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_a8e608b93b683519cda35d166e08ab587"></a>

```c
#define TMS_PIO0_12 IOCON_MUX(12, IOCON_TYPE_A, 0) /* PIO0_12 */
```

相关声明：[TMS_PIO0_12](#a8e608b93b683519cda35d166e08ab587)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_ab4b3327e260eccbcccf80f0c1904ac56"></a>

```c
#define PIO0_12_PIO0_12 IOCON_MUX(12, IOCON_TYPE_A, 1) /* PIO0_12 */
```

相关声明：[PIO0_12_PIO0_12](#ab4b3327e260eccbcccf80f0c1904ac56)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_ae9f30a9545a11701304231e5efb707a5"></a>

```c
#define ADC_8_PIO0_12 IOCON_MUX(12, IOCON_TYPE_A, 2) /* PIO0_12 */
```

相关声明：[ADC_8_PIO0_12](#ae9f30a9545a11701304231e5efb707a5)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_a7b28030377332811f795cd1462bf631f"></a>

```c
#define CT32B1_CAP0_PIO0_12 IOCON_MUX(12, IOCON_TYPE_A, 3) /* PIO0_12 */
```

相关声明：[CT32B1_CAP0_PIO0_12](#a7b28030377332811f795cd1462bf631f)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_ac58b55301756d90dcbfac6264df577b2"></a>

```c
#define U1_CTS_PIO0_12 IOCON_MUX(12, IOCON_TYPE_A, 4) /* PIO0_12 */
```

相关声明：[U1_CTS_PIO0_12](#ac58b55301756d90dcbfac6264df577b2)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_a51f64447bf880601691ffe859d0f1964"></a>

```c
#define PIO0_12_PIO0_12 IOCON_MUX(12, IOCON_TYPE_A, 5) /* PIO0_12 */
```

相关声明：[PIO0_12_PIO0_12](#a51f64447bf880601691ffe859d0f1964)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_ace1983c57935ab76096a42fa0d9af286"></a>

```c
#define TDO_PIO0_13 IOCON_MUX(13, IOCON_TYPE_A, 0) /* PIO0_13 */
```

相关声明：[TDO_PIO0_13](#ace1983c57935ab76096a42fa0d9af286)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_af1f156f6bca42a308c3d154ce6033f5a"></a>

```c
#define PIO0_13_PIO0_13 IOCON_MUX(13, IOCON_TYPE_A, 1) /* PIO0_13 */
```

相关声明：[PIO0_13_PIO0_13](#af1f156f6bca42a308c3d154ce6033f5a)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_a706b80599c77ce5212b2359187d3fab1"></a>

```c
#define ADC_7_PIO0_13 IOCON_MUX(13, IOCON_TYPE_A, 2) /* PIO0_13 */
```

相关声明：[ADC_7_PIO0_13](#a706b80599c77ce5212b2359187d3fab1)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_af55d0700864a68532d8b253344160ebf"></a>

```c
#define CT32B1_MAT0_PIO0_13 IOCON_MUX(13, IOCON_TYPE_A, 3) /* PIO0_13 */
```

相关声明：[CT32B1_MAT0_PIO0_13](#af55d0700864a68532d8b253344160ebf)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_a3eb45ad4dd10da96ed90153ef3b53665"></a>

```c
#define U1_RXD_PIO0_13 IOCON_MUX(13, IOCON_TYPE_A, 4) /* PIO0_13 */
```

相关声明：[U1_RXD_PIO0_13](#a3eb45ad4dd10da96ed90153ef3b53665)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_a8d40f087b829a11db51c16ab2181995c"></a>

```c
#define PIO0_13_PIO0_13 IOCON_MUX(13, IOCON_TYPE_A, 5) /* PIO0_13 */
```

相关声明：[PIO0_13_PIO0_13](#a8d40f087b829a11db51c16ab2181995c)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_ad8c652abc5c8558f9312bd0ea201d7fc"></a>

```c
#define TRST_PIO0_14 IOCON_MUX(14, IOCON_TYPE_A, 0) /* PIO0_14 */
```

相关声明：[TRST_PIO0_14](#ad8c652abc5c8558f9312bd0ea201d7fc)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_a692e4e1765be1cbca9897691a6bfbc39"></a>

```c
#define PIO0_14_PIO0_14 IOCON_MUX(14, IOCON_TYPE_A, 1) /* PIO0_14 */
```

相关声明：[PIO0_14_PIO0_14](#a692e4e1765be1cbca9897691a6bfbc39)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_ae6c3bb89b08367707e91bb00d3f55da5"></a>

```c
#define ADC_6_PIO0_14 IOCON_MUX(14, IOCON_TYPE_A, 2) /* PIO0_14 */
```

相关声明：[ADC_6_PIO0_14](#ae6c3bb89b08367707e91bb00d3f55da5)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_acc4bcbd80fa3306bfa4ab8a4d3023c34"></a>

```c
#define CT32B1_MAT1_PIO0_14 IOCON_MUX(14, IOCON_TYPE_A, 3) /* PIO0_14 */
```

相关声明：[CT32B1_MAT1_PIO0_14](#acc4bcbd80fa3306bfa4ab8a4d3023c34)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_a567bb0593686aa6552e868caeb623532"></a>

```c
#define U1_TXD_PIO0_14 IOCON_MUX(14, IOCON_TYPE_A, 4) /* PIO0_14 */
```

相关声明：[U1_TXD_PIO0_14](#a567bb0593686aa6552e868caeb623532)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_a0b65345797054d59564518f73eee1602"></a>

```c
#define SWDIO_PIO0_15 IOCON_MUX(15, IOCON_TYPE_A, 0) /* PIO0_15 */
```

相关声明：[SWDIO_PIO0_15](#a0b65345797054d59564518f73eee1602)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_a59a92f1c63f7eb548a19f555cfe0208e"></a>

```c
#define PIO0_15_PIO0_15 IOCON_MUX(15, IOCON_TYPE_A, 1) /* PIO0_15 */
```

相关声明：[PIO0_15_PIO0_15](#a59a92f1c63f7eb548a19f555cfe0208e)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_af92fd1b534c099ad808403a199cad8a0"></a>

```c
#define ADC_3_PIO0_15 IOCON_MUX(15, IOCON_TYPE_A, 2) /* PIO0_15 */
```

相关声明：[ADC_3_PIO0_15](#af92fd1b534c099ad808403a199cad8a0)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_ac5ed12914616e50cac147b251291d3f6"></a>

```c
#define CT32B1_MAT2_PIO0_15 IOCON_MUX(15, IOCON_TYPE_A, 3) /* PIO0_15 */
```

相关声明：[CT32B1_MAT2_PIO0_15](#ac5ed12914616e50cac147b251291d3f6)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_a285bf9c6e5c1b7bfc8ada6ececbe466e"></a>

```c
#define WAKEUP_PIO0_16 IOCON_MUX(16, IOCON_TYPE_A, 0) /* PIO0_16 */
```

相关声明：[WAKEUP_PIO0_16](#a285bf9c6e5c1b7bfc8ada6ececbe466e)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_aa4a10249e5ee8e04ce01f62864476727"></a>

```c
#define PIO0_16_PIO0_16 IOCON_MUX(16, IOCON_TYPE_A, 1) /* PIO0_16 */
```

相关声明：[PIO0_16_PIO0_16](#aa4a10249e5ee8e04ce01f62864476727)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_a21eeb0732f5d35d747f63db3eac9cfad"></a>

```c
#define ADC_2_PIO0_16 IOCON_MUX(16, IOCON_TYPE_A, 2) /* PIO0_16 */
```

相关声明：[ADC_2_PIO0_16](#a21eeb0732f5d35d747f63db3eac9cfad)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_a26ecf5bab459bde9bbb64ff5a019b09a"></a>

```c
#define CT32B1_MAT3_PIO0_16 IOCON_MUX(16, IOCON_TYPE_A, 3) /* PIO0_16 */
```

相关声明：[CT32B1_MAT3_PIO0_16](#a26ecf5bab459bde9bbb64ff5a019b09a)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_a58df208f71b6efffed28bbabddf45f41"></a>

```c
#define R_8_PIO0_16 IOCON_MUX(16, IOCON_TYPE_A, 4) /* PIO0_16 */
```

相关声明：[R_8_PIO0_16](#a58df208f71b6efffed28bbabddf45f41)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_a34451e215c47228b8337d0aed0c2c929"></a>

```c
#define PIO0_17_PIO0_17 IOCON_MUX(17, IOCON_TYPE_D, 0) /* PIO0_17 */
```

相关声明：[PIO0_17_PIO0_17](#a34451e215c47228b8337d0aed0c2c929)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_ad946bbd06292183b7bdcd8db7d93d980"></a>

```c
#define U0_RTS_PIO0_17 IOCON_MUX(17, IOCON_TYPE_D, 1) /* PIO0_17 */
```

相关声明：[U0_RTS_PIO0_17](#ad946bbd06292183b7bdcd8db7d93d980)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_afa844a06c34eb41b114b49aac65d5eb1"></a>

```c
#define CT32B0_CAP0_PIO0_17 IOCON_MUX(17, IOCON_TYPE_D, 2) /* PIO0_17 */
```

相关声明：[CT32B0_CAP0_PIO0_17](#afa844a06c34eb41b114b49aac65d5eb1)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a5f911210bf444c31df578680aa92ba9e"></a>

```c
#define U0_SCLK_PIO0_17 IOCON_MUX(17, IOCON_TYPE_D, 3) /* PIO0_17 */
```

相关声明：[U0_SCLK_PIO0_17](#a5f911210bf444c31df578680aa92ba9e)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a87d216855b3f78407343517d639cd75c"></a>

```c
#define PIO0_18_PIO0_18 IOCON_MUX(18, IOCON_TYPE_D, 0) /* PIO0_18 */
```

相关声明：[PIO0_18_PIO0_18](#a87d216855b3f78407343517d639cd75c)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a22d6493688b04414c7dc732d43f4c0f2"></a>

```c
#define U0_RXD_PIO0_18 IOCON_MUX(18, IOCON_TYPE_D, 1) /* PIO0_18 */
```

相关声明：[U0_RXD_PIO0_18](#a22d6493688b04414c7dc732d43f4c0f2)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a099d0dca10dd8ac2762ac340473a798b"></a>

```c
#define CT32B0_MAT0_PIO0_18 IOCON_MUX(18, IOCON_TYPE_D, 2) /* PIO0_18 */
```

相关声明：[CT32B0_MAT0_PIO0_18](#a099d0dca10dd8ac2762ac340473a798b)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a83757ba41e5c8ff4a04384a6f59550e1"></a>

```c
#define PIO0_19_PIO0_19 IOCON_MUX(19, IOCON_TYPE_D, 0) /* PIO0_19 */
```

相关声明：[PIO0_19_PIO0_19](#a83757ba41e5c8ff4a04384a6f59550e1)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a602172b5fe5dde4f7064ea152914e3b4"></a>

```c
#define U0_TXD_PIO0_19 IOCON_MUX(19, IOCON_TYPE_D, 1) /* PIO0_19 */
```

相关声明：[U0_TXD_PIO0_19](#a602172b5fe5dde4f7064ea152914e3b4)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a579df8a29d7f50a93ae328c1aec9385a"></a>

```c
#define CT32B0_MAT1_PIO0_19 IOCON_MUX(19, IOCON_TYPE_D, 2) /* PIO0_19 */
```

相关声明：[CT32B0_MAT1_PIO0_19](#a579df8a29d7f50a93ae328c1aec9385a)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a28a9784674717e3617070ed87923a1f1"></a>

```c
#define PIO0_20_PIO0_20 IOCON_MUX(20, IOCON_TYPE_D, 0) /* PIO0_20 */
```

相关声明：[PIO0_20_PIO0_20](#a28a9784674717e3617070ed87923a1f1)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_aa7942f15263a5a5c36bd4513da5223c2"></a>

```c
#define CT16B1_CAP0_PIO0_20 IOCON_MUX(20, IOCON_TYPE_D, 1) /* PIO0_20 */
```

相关声明：[CT16B1_CAP0_PIO0_20](#aa7942f15263a5a5c36bd4513da5223c2)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a9fc4de327d564720e61a338e4a5d3b5b"></a>

```c
#define U2_RXD_PIO0_20 IOCON_MUX(20, IOCON_TYPE_D, 2) /* PIO0_20 */
```

相关声明：[U2_RXD_PIO0_20](#a9fc4de327d564720e61a338e4a5d3b5b)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_abfb5b6fa233853dc18ed899fa4418b1b"></a>

```c
#define PIO0_21_PIO0_21 IOCON_MUX(21, IOCON_TYPE_D, 0) /* PIO0_21 */
```

相关声明：[PIO0_21_PIO0_21](#abfb5b6fa233853dc18ed899fa4418b1b)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a91549c703ace01d5e5cd3f5477ec156e"></a>

```c
#define CT16B1_MAT0_PIO0_21 IOCON_MUX(21, IOCON_TYPE_D, 1) /* PIO0_21 */
```

相关声明：[CT16B1_MAT0_PIO0_21](#a91549c703ace01d5e5cd3f5477ec156e)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_aaec77c9670e3e88d00641020ec0d47d6"></a>

```c
#define SSP1_MOSI_PIO0_21 IOCON_MUX(21, IOCON_TYPE_D, 2) /* PIO0_21 */
```

相关声明：[SSP1_MOSI_PIO0_21](#aaec77c9670e3e88d00641020ec0d47d6)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a9df3dda1a040239ee21e73c813659ccd"></a>

```c
#define PIO0_22_PIO0_22 IOCON_MUX(22, IOCON_TYPE_A, 0) /* PIO0_22 */
```

相关声明：[PIO0_22_PIO0_22](#a9df3dda1a040239ee21e73c813659ccd)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_aafede8fcd15e8bfe236e95c9a7b49b96"></a>

```c
#define ADC_11_PIO0_22 IOCON_MUX(22, IOCON_TYPE_A, 1) /* PIO0_22 */
```

相关声明：[ADC_11_PIO0_22](#aafede8fcd15e8bfe236e95c9a7b49b96)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_a2630aa1a98d13baf6f04f78f005bf704"></a>

```c
#define CT16B1_CAP1_PIO0_22 IOCON_MUX(22, IOCON_TYPE_A, 2) /* PIO0_22 */
```

相关声明：[CT16B1_CAP1_PIO0_22](#a2630aa1a98d13baf6f04f78f005bf704)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_a783a183d806cac03c7db41096bae4272"></a>

```c
#define SSP1_MISO_PIO0_22 IOCON_MUX(22, IOCON_TYPE_A, 3) /* PIO0_22 */
```

相关声明：[SSP1_MISO_PIO0_22](#a783a183d806cac03c7db41096bae4272)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_a07878c04e96b6472f26d3760a42ac212"></a>

```c
#define PIO0_23_PIO0_23 IOCON_MUX(23, IOCON_TYPE_A, 0) /* PIO0_23 */
```

相关声明：[PIO0_23_PIO0_23](#a07878c04e96b6472f26d3760a42ac212)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_ab00e7a1a150e2e1c9b45d86c850a4a0b"></a>

```c
#define ADC_1_PIO0_23 IOCON_MUX(23, IOCON_TYPE_A, 1) /* PIO0_23 */
```

相关声明：[ADC_1_PIO0_23](#ab00e7a1a150e2e1c9b45d86c850a4a0b)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_ab0d0d78534d6cc1d4cee77b3eee84114"></a>

```c
#define R_9_PIO0_23 IOCON_MUX(23, IOCON_TYPE_A, 2) /* PIO0_23 */
```

相关声明：[R_9_PIO0_23](#ab0d0d78534d6cc1d4cee77b3eee84114)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_a1b2efba93021237e6fd7e3e276fef4e5"></a>

```c
#define U0_RI_PIO0_23 IOCON_MUX(23, IOCON_TYPE_A, 3) /* PIO0_23 */
```

相关声明：[U0_RI_PIO0_23](#a1b2efba93021237e6fd7e3e276fef4e5)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_a0a3ad1a37c02adc62dbae966523e6d4c"></a>

```c
#define SSP1_SSEL_PIO0_23 IOCON_MUX(23, IOCON_TYPE_A, 4) /* PIO0_23 */
```

相关声明：[SSP1_SSEL_PIO0_23](#a0a3ad1a37c02adc62dbae966523e6d4c)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_ac68053b619744fbf1c1f17f7b08cf580"></a>

```c
#define PIO1_0_PIO1_0 IOCON_MUX(24, IOCON_TYPE_D, 0) /* PIO1_0 */
```

相关声明：[PIO1_0_PIO1_0](#ac68053b619744fbf1c1f17f7b08cf580)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a5ee6340e6fe3b732b6d49bbef6c90155"></a>

```c
#define CT32B1_MAT0_PIO1_0 IOCON_MUX(24, IOCON_TYPE_D, 1) /* PIO1_0 */
```

相关声明：[CT32B1_MAT0_PIO1_0](#a5ee6340e6fe3b732b6d49bbef6c90155)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a1ac3960333408442de9bd74e694595de"></a>

```c
#define R_10_PIO1_0 IOCON_MUX(24, IOCON_TYPE_D, 2) /* PIO1_0 */
```

相关声明：[R_10_PIO1_0](#a1ac3960333408442de9bd74e694595de)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a4319b4d5227cd2a7ff75de78a422a870"></a>

```c
#define U2_TXD_PIO1_0 IOCON_MUX(24, IOCON_TYPE_D, 3) /* PIO1_0 */
```

相关声明：[U2_TXD_PIO1_0](#a4319b4d5227cd2a7ff75de78a422a870)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a299fee16f12cef2f585e132548ba3b72"></a>

```c
#define PIO1_1_PIO1_1 IOCON_MUX(25, IOCON_TYPE_D, 0) /* PIO1_1 */
```

相关声明：[PIO1_1_PIO1_1](#a299fee16f12cef2f585e132548ba3b72)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_afb61298e6db2c507f6090a86566edc91"></a>

```c
#define CT32B1_MAT1_PIO1_1 IOCON_MUX(25, IOCON_TYPE_D, 1) /* PIO1_1 */
```

相关声明：[CT32B1_MAT1_PIO1_1](#afb61298e6db2c507f6090a86566edc91)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_aaae95bceef30b054294e7a7eed2d68a4"></a>

```c
#define R_11_PIO1_1 IOCON_MUX(25, IOCON_TYPE_D, 2) /* PIO1_1 */
```

相关声明：[R_11_PIO1_1](#aaae95bceef30b054294e7a7eed2d68a4)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a7a17c6326f865f7eee09ec236ce12216"></a>

```c
#define U0_DTR_PIO1_1 IOCON_MUX(25, IOCON_TYPE_D, 3) /* PIO1_1 */
```

相关声明：[U0_DTR_PIO1_1](#a7a17c6326f865f7eee09ec236ce12216)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a5265479414c8dd9845e6aa5213eda99e"></a>

```c
#define PIO1_2_PIO1_2 IOCON_MUX(26, IOCON_TYPE_D, 0) /* PIO1_2 */
```

相关声明：[PIO1_2_PIO1_2](#a5265479414c8dd9845e6aa5213eda99e)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_ab158e092af2c6ad056cc6f4d298c1951"></a>

```c
#define CT32B1_MAT2_PIO1_2 IOCON_MUX(26, IOCON_TYPE_D, 1) /* PIO1_2 */
```

相关声明：[CT32B1_MAT2_PIO1_2](#ab158e092af2c6ad056cc6f4d298c1951)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_ac7bd9d42184bd9175925b2e789d4e0f8"></a>

```c
#define R_12_PIO1_2 IOCON_MUX(26, IOCON_TYPE_D, 2) /* PIO1_2 */
```

相关声明：[R_12_PIO1_2](#ac7bd9d42184bd9175925b2e789d4e0f8)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a4af77ea4a454643946504e10d249edcc"></a>

```c
#define U1_RXD_PIO1_2 IOCON_MUX(26, IOCON_TYPE_D, 3) /* PIO1_2 */
```

相关声明：[U1_RXD_PIO1_2](#a4af77ea4a454643946504e10d249edcc)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a2d403da5360929eed6c833567c415fe5"></a>

```c
#define PIO1_3_PIO1_3 IOCON_MUX(27, IOCON_TYPE_A, 0) /* PIO1_3 */
```

相关声明：[PIO1_3_PIO1_3](#a2d403da5360929eed6c833567c415fe5)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_a7edf5d0d95f5fa253b03ccc77447ed9a"></a>

```c
#define CT32B1_MAT3_PIO1_3 IOCON_MUX(27, IOCON_TYPE_A, 1) /* PIO1_3 */
```

相关声明：[CT32B1_MAT3_PIO1_3](#a7edf5d0d95f5fa253b03ccc77447ed9a)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_a1f35a5b9268e09e3ff279d0d7b27e8d9"></a>

```c
#define R_13_PIO1_3 IOCON_MUX(27, IOCON_TYPE_A, 2) /* PIO1_3 */
```

相关声明：[R_13_PIO1_3](#a1f35a5b9268e09e3ff279d0d7b27e8d9)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_ae63879080611307c152e569946e7a7ae"></a>

```c
#define I2C1_SDA_PIO1_3 IOCON_MUX(27, IOCON_TYPE_A, 3) /* PIO1_3 */
```

相关声明：[I2C1_SDA_PIO1_3](#ae63879080611307c152e569946e7a7ae)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_ac4f0bd23dfc3f744220cadb6949d4e1f"></a>

```c
#define ADC_5_PIO1_3 IOCON_MUX(27, IOCON_TYPE_A, 4) /* PIO1_3 */
```

相关声明：[ADC_5_PIO1_3](#ac4f0bd23dfc3f744220cadb6949d4e1f)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_aecf77d09221ba70819899708b4ad74a8"></a>

```c
#define PIO1_4_PIO1_4 IOCON_MUX(28, IOCON_TYPE_D, 0) /* PIO1_4 */
```

相关声明：[PIO1_4_PIO1_4](#aecf77d09221ba70819899708b4ad74a8)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a54bfd60ff58b0148b6848f8b2982442e"></a>

```c
#define CT32B1_CAP0_PIO1_4 IOCON_MUX(28, IOCON_TYPE_D, 1) /* PIO1_4 */
```

相关声明：[CT32B1_CAP0_PIO1_4](#a54bfd60ff58b0148b6848f8b2982442e)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_aaba8b00d104b3163f0c7cee32b91cf1e"></a>

```c
#define R_14_PIO1_4 IOCON_MUX(28, IOCON_TYPE_D, 2) /* PIO1_4 */
```

相关声明：[R_14_PIO1_4](#aaba8b00d104b3163f0c7cee32b91cf1e)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a0a7cdf5fa1cae307725c7cf8742cc599"></a>

```c
#define U0_DSR_PIO1_4 IOCON_MUX(28, IOCON_TYPE_D, 3) /* PIO1_4 */
```

相关声明：[U0_DSR_PIO1_4](#a0a7cdf5fa1cae307725c7cf8742cc599)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_ab070530de6c3105054206c5a526f5730"></a>

```c
#define PIO1_5_PIO1_5 IOCON_MUX(29, IOCON_TYPE_D, 0) /* PIO1_5 */
```

相关声明：[PIO1_5_PIO1_5](#ab070530de6c3105054206c5a526f5730)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a1ab5d0cd48d5ade99b0a6e4fc8bc9f68"></a>

```c
#define CT32B1_CAP1_PIO1_5 IOCON_MUX(29, IOCON_TYPE_D, 1) /* PIO1_5 */
```

相关声明：[CT32B1_CAP1_PIO1_5](#a1ab5d0cd48d5ade99b0a6e4fc8bc9f68)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_adcccebfaed3f6f65e12a4052ff04fdcd"></a>

```c
#define R_15_PIO1_5 IOCON_MUX(29, IOCON_TYPE_D, 2) /* PIO1_5 */
```

相关声明：[R_15_PIO1_5](#adcccebfaed3f6f65e12a4052ff04fdcd)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a0abbdcaf023079f9181f260779ced50e"></a>

```c
#define U0_DCD_PIO1_5 IOCON_MUX(29, IOCON_TYPE_D, 3) /* PIO1_5 */
```

相关声明：[U0_DCD_PIO1_5](#a0abbdcaf023079f9181f260779ced50e)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_af6b1804a5aefa54e7a3c4dba33394805"></a>

```c
#define PIO1_6_PIO1_6 IOCON_MUX(30, IOCON_TYPE_D, 0) /* PIO1_6 */
```

相关声明：[PIO1_6_PIO1_6](#af6b1804a5aefa54e7a3c4dba33394805)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a9f77fd7bcd00d7bc4e179cb3c3db622e"></a>

```c
#define R_16_PIO1_6 IOCON_MUX(30, IOCON_TYPE_D, 1) /* PIO1_6 */
```

相关声明：[R_16_PIO1_6](#a9f77fd7bcd00d7bc4e179cb3c3db622e)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a48ac3c0096037bbe64d92b2d2b0e621f"></a>

```c
#define U2_RXD_PIO1_6 IOCON_MUX(30, IOCON_TYPE_D, 2) /* PIO1_6 */
```

相关声明：[U2_RXD_PIO1_6](#a48ac3c0096037bbe64d92b2d2b0e621f)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a01c2a127b550f1c904cf747a2351c006"></a>

```c
#define CT32B0_CAP1_PIO1_6 IOCON_MUX(30, IOCON_TYPE_D, 3) /* PIO1_6 */
```

相关声明：[CT32B0_CAP1_PIO1_6](#a01c2a127b550f1c904cf747a2351c006)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_ab77050cd6c5323ede0c6ce3f52f4f83e"></a>

```c
#define PIO1_7_PIO1_7 IOCON_MUX(31, IOCON_TYPE_D, 0) /* PIO1_7 */
```

相关声明：[PIO1_7_PIO1_7](#ab77050cd6c5323ede0c6ce3f52f4f83e)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a2478b21ed3999f9fb27e1ddcc555383f"></a>

```c
#define R_17_PIO1_7 IOCON_MUX(31, IOCON_TYPE_D, 1) /* PIO1_7 */
```

相关声明：[R_17_PIO1_7](#a2478b21ed3999f9fb27e1ddcc555383f)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a23bb3cc2ede010588651fede510df3db"></a>

```c
#define U2_CTS_PIO1_7 IOCON_MUX(31, IOCON_TYPE_D, 2) /* PIO1_7 */
```

相关声明：[U2_CTS_PIO1_7](#a23bb3cc2ede010588651fede510df3db)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a6673a36d9b33d563295063f73c466b58"></a>

```c
#define CT16B1_CAP0_PIO1_7 IOCON_MUX(31, IOCON_TYPE_D, 3) /* PIO1_7 */
```

相关声明：[CT16B1_CAP0_PIO1_7](#a6673a36d9b33d563295063f73c466b58)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a5eb361e081a52918777d89f61c0a26fa"></a>

```c
#define PIO1_8_PIO1_8 IOCON_MUX(32, IOCON_TYPE_D, 0) /* PIO1_8 */
```

相关声明：[PIO1_8_PIO1_8](#a5eb361e081a52918777d89f61c0a26fa)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a01a390f0311638bc09569b06839fb7dd"></a>

```c
#define R_18_PIO1_8 IOCON_MUX(32, IOCON_TYPE_D, 1) /* PIO1_8 */
```

相关声明：[R_18_PIO1_8](#a01a390f0311638bc09569b06839fb7dd)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a253fad10b49809895c3f27ec3e51a567"></a>

```c
#define U1_TXD_PIO1_8 IOCON_MUX(32, IOCON_TYPE_D, 2) /* PIO1_8 */
```

相关声明：[U1_TXD_PIO1_8](#a253fad10b49809895c3f27ec3e51a567)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a598b61d037bfcacc335bf0996a477843"></a>

```c
#define CT16B0_CAP0_PIO1_8 IOCON_MUX(32, IOCON_TYPE_D, 3) /* PIO1_8 */
```

相关声明：[CT16B0_CAP0_PIO1_8](#a598b61d037bfcacc335bf0996a477843)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a75ab800970f73ac0177aaf8139ba8739"></a>

```c
#define PIO1_9_PIO1_9 IOCON_MUX(33, IOCON_TYPE_A, 0) /* PIO1_9 */
```

相关声明：[PIO1_9_PIO1_9](#a75ab800970f73ac0177aaf8139ba8739)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_a5ec91d14ec34a2080c1d857e1fd6f572"></a>

```c
#define U0_CTS_PIO1_9 IOCON_MUX(33, IOCON_TYPE_A, 1) /* PIO1_9 */
```

相关声明：[U0_CTS_PIO1_9](#a5ec91d14ec34a2080c1d857e1fd6f572)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_a9db77081025e9907d1d90cf993d8a028"></a>

```c
#define CT16B1_MAT1_PIO1_9 IOCON_MUX(33, IOCON_TYPE_A, 2) /* PIO1_9 */
```

相关声明：[CT16B1_MAT1_PIO1_9](#a9db77081025e9907d1d90cf993d8a028)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_a03ce0c70811dc7195ee48649532f2ebd"></a>

```c
#define ADC_0_PIO1_9 IOCON_MUX(33, IOCON_TYPE_A, 3) /* PIO1_9 */
```

相关声明：[ADC_0_PIO1_9](#a03ce0c70811dc7195ee48649532f2ebd)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_a037f6a357a5bbea0dc0cb9902c94c846"></a>

```c
#define PIO1_10_PIO1_10 IOCON_MUX(34, IOCON_TYPE_D, 0) /* PIO1_10 */
```

相关声明：[PIO1_10_PIO1_10](#a037f6a357a5bbea0dc0cb9902c94c846)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a2f2957c1a43d63106ce2d61678103f62"></a>

```c
#define U2_RTS_PIO1_10 IOCON_MUX(34, IOCON_TYPE_D, 1) /* PIO1_10 */
```

相关声明：[U2_RTS_PIO1_10](#a2f2957c1a43d63106ce2d61678103f62)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_ac7236d26fd68c0be4b0f80e7ac6614cd"></a>

```c
#define U2_SCLK_PIO1_10 IOCON_MUX(34, IOCON_TYPE_D, 2) /* PIO1_10 */
```

相关声明：[U2_SCLK_PIO1_10](#ac7236d26fd68c0be4b0f80e7ac6614cd)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_abd7606b5f7f902397d6c2ab8fedfd2b3"></a>

```c
#define CT16B1_MAT0_PIO1_10 IOCON_MUX(34, IOCON_TYPE_D, 3) /* PIO1_10 */
```

相关声明：[CT16B1_MAT0_PIO1_10](#abd7606b5f7f902397d6c2ab8fedfd2b3)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a97b3bfd02acef68ffc82952e49bd03fe"></a>

```c
#define PIO1_11_PIO1_11 IOCON_MUX(35, IOCON_TYPE_D, 0) /* PIO1_11 */
```

相关声明：[PIO1_11_PIO1_11](#a97b3bfd02acef68ffc82952e49bd03fe)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_abd5321e5d55560fb0927e8a26027d001"></a>

```c
#define I2C1_SCL_PIO1_11 IOCON_MUX(35, IOCON_TYPE_D, 1) /* PIO1_11 */
```

相关声明：[I2C1_SCL_PIO1_11](#abd5321e5d55560fb0927e8a26027d001)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_ad0ae914ba48296f972618dee04cc6490"></a>

```c
#define CT16B0_MAT2_PIO1_11 IOCON_MUX(35, IOCON_TYPE_D, 2) /* PIO1_11 */
```

相关声明：[CT16B0_MAT2_PIO1_11](#ad0ae914ba48296f972618dee04cc6490)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_aa43f68879f82d124e3d1da1b1a4bee16"></a>

```c
#define U0_RI_PIO1_11 IOCON_MUX(35, IOCON_TYPE_D, 3) /* PIO1_11 */
```

相关声明：[U0_RI_PIO1_11](#aa43f68879f82d124e3d1da1b1a4bee16)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a896bd464fd196266a8862fde369e899b"></a>

```c
#define PIO1_12_PIO1_12 IOCON_MUX(36, IOCON_TYPE_D, 0) /* PIO1_12 */
```

相关声明：[PIO1_12_PIO1_12](#a896bd464fd196266a8862fde369e899b)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a0bc3c1d34d0bc7a92543edd4e743905f"></a>

```c
#define SSP0_MOSI_PIO1_12 IOCON_MUX(36, IOCON_TYPE_D, 1) /* PIO1_12 */
```

相关声明：[SSP0_MOSI_PIO1_12](#a0bc3c1d34d0bc7a92543edd4e743905f)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a5b8fcd82c3feca9ed3dfbd2f905b4a74"></a>

```c
#define CT16B0_MAT1_PIO1_12 IOCON_MUX(36, IOCON_TYPE_D, 2) /* PIO1_12 */
```

相关声明：[CT16B0_MAT1_PIO1_12](#a5b8fcd82c3feca9ed3dfbd2f905b4a74)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_abe8e17586c29617e61a2671408e84637"></a>

```c
#define R_21_PIO1_12 IOCON_MUX(36, IOCON_TYPE_D, 3) /* PIO1_12 */
```

相关声明：[R_21_PIO1_12](#abe8e17586c29617e61a2671408e84637)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_ad2d3d8b8bb3a17fab2dc03850b9934e6"></a>

```c
#define PIO1_13_PIO1_13 IOCON_MUX(37, IOCON_TYPE_D, 0) /* PIO1_13 */
```

相关声明：[PIO1_13_PIO1_13](#ad2d3d8b8bb3a17fab2dc03850b9934e6)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_ad00e6299050aceda961b3b6af7a78f79"></a>

```c
#define U1_CTS_PIO1_13 IOCON_MUX(37, IOCON_TYPE_D, 1) /* PIO1_13 */
```

相关声明：[U1_CTS_PIO1_13](#ad00e6299050aceda961b3b6af7a78f79)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a504a57a6c6e3014ed4df4320736c7713"></a>

```c
#define SCT0_OUT3_PIO1_13 IOCON_MUX(37, IOCON_TYPE_D, 2) /* PIO1_13 */
```

相关声明：[SCT0_OUT3_PIO1_13](#a504a57a6c6e3014ed4df4320736c7713)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a8613dd791e9ddf76c84d12c9f25f31ed"></a>

```c
#define R_22_PIO1_13 IOCON_MUX(37, IOCON_TYPE_D, 3) /* PIO1_13 */
```

相关声明：[R_22_PIO1_13](#a8613dd791e9ddf76c84d12c9f25f31ed)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_aec627d88659627216048116352084463"></a>

```c
#define PIO1_14_PIO1_14 IOCON_MUX(38, IOCON_TYPE_D, 0) /* PIO1_14 */
```

相关声明：[PIO1_14_PIO1_14](#aec627d88659627216048116352084463)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_aa478831aabf3f70f44dc83be779f29df"></a>

```c
#define I2C1_SDA_PIO1_14 IOCON_MUX(38, IOCON_TYPE_D, 1) /* PIO1_14 */
```

相关声明：[I2C1_SDA_PIO1_14](#aa478831aabf3f70f44dc83be779f29df)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a7e9fefa7d3b24bcf91c2af8143934e1b"></a>

```c
#define CT32B1_MAT2_PIO1_14 IOCON_MUX(38, IOCON_TYPE_D, 2) /* PIO1_14 */
```

相关声明：[CT32B1_MAT2_PIO1_14](#a7e9fefa7d3b24bcf91c2af8143934e1b)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a75b2a3bdcdc904bce2ed4641fd77d36f"></a>

```c
#define R_23_PIO1_14 IOCON_MUX(38, IOCON_TYPE_D, 3) /* PIO1_14 */
```

相关声明：[R_23_PIO1_14](#a75b2a3bdcdc904bce2ed4641fd77d36f)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_ad430442be04fb9768354a29392aa3150"></a>

```c
#define PIO1_15_PIO1_15 IOCON_MUX(39, IOCON_TYPE_D, 0) /* PIO1_15 */
```

相关声明：[PIO1_15_PIO1_15](#ad430442be04fb9768354a29392aa3150)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_acc0fec039c618cf46e788bfb6f651cfe"></a>

```c
#define SSP0_SSEL_PIO1_15 IOCON_MUX(39, IOCON_TYPE_D, 1) /* PIO1_15 */
```

相关声明：[SSP0_SSEL_PIO1_15](#acc0fec039c618cf46e788bfb6f651cfe)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_af960ef8b39ccd08fbe57d0fb2808507a"></a>

```c
#define CT32B1_MAT3_PIO1_15 IOCON_MUX(39, IOCON_TYPE_D, 2) /* PIO1_15 */
```

相关声明：[CT32B1_MAT3_PIO1_15](#af960ef8b39ccd08fbe57d0fb2808507a)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a31607e58141be4451603b21142dc2b78"></a>

```c
#define R_24_PIO1_15 IOCON_MUX(39, IOCON_TYPE_D, 3) /* PIO1_15 */
```

相关声明：[R_24_PIO1_15](#a31607e58141be4451603b21142dc2b78)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a890647261f0d13600177b8da109e7f80"></a>

```c
#define PIO1_16_PIO1_16 IOCON_MUX(40, IOCON_TYPE_D, 0) /* PIO1_16 */
```

相关声明：[PIO1_16_PIO1_16](#a890647261f0d13600177b8da109e7f80)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_adb527bbcf8d059c9bfccdf29f3ac4aa5"></a>

```c
#define SSP0_MISO_PIO1_16 IOCON_MUX(40, IOCON_TYPE_D, 1) /* PIO1_16 */
```

相关声明：[SSP0_MISO_PIO1_16](#adb527bbcf8d059c9bfccdf29f3ac4aa5)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_acead3031fd80d06b2f87cf0ad8e9e8e2"></a>

```c
#define CT16B0_MAT0_PIO1_16 IOCON_MUX(40, IOCON_TYPE_D, 2) /* PIO1_16 */
```

相关声明：[CT16B0_MAT0_PIO1_16](#acead3031fd80d06b2f87cf0ad8e9e8e2)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_afbf96bb8cc6cf2f8f56ac0f48de55a9d"></a>

```c
#define R_25_PIO1_16 IOCON_MUX(40, IOCON_TYPE_D, 3) /* PIO1_16 */
```

相关声明：[R_25_PIO1_16](#afbf96bb8cc6cf2f8f56ac0f48de55a9d)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_ab7c4014e4c5aff2215d00bfbfcdca7c6"></a>

```c
#define PIO1_17_PIO1_17 IOCON_MUX(41, IOCON_TYPE_D, 0) /* PIO1_17 */
```

相关声明：[PIO1_17_PIO1_17](#ab7c4014e4c5aff2215d00bfbfcdca7c6)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a27237240e4f0c84be58ac4a40915b30b"></a>

```c
#define CT16B0_CAP2_PIO1_17 IOCON_MUX(41, IOCON_TYPE_D, 1) /* PIO1_17 */
```

相关声明：[CT16B0_CAP2_PIO1_17](#a27237240e4f0c84be58ac4a40915b30b)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a974de383ed91f1e80b6e67ab95f627d3"></a>

```c
#define U0_RXD_PIO1_17 IOCON_MUX(41, IOCON_TYPE_D, 2) /* PIO1_17 */
```

相关声明：[U0_RXD_PIO1_17](#a974de383ed91f1e80b6e67ab95f627d3)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a485ea3b9fe56406e22a835ad8101ca2a"></a>

```c
#define R_26_PIO1_17 IOCON_MUX(41, IOCON_TYPE_D, 3) /* PIO1_17 */
```

相关声明：[R_26_PIO1_17](#a485ea3b9fe56406e22a835ad8101ca2a)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_abd5742cad3a656c0cca0a02ec6b41acf"></a>

```c
#define PIO1_18_PIO1_18 IOCON_MUX(42, IOCON_TYPE_D, 0) /* PIO1_18 */
```

相关声明：[PIO1_18_PIO1_18](#abd5742cad3a656c0cca0a02ec6b41acf)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_af2925353ca8342deac5cc6c47623b40c"></a>

```c
#define CT16B1_CAP1_PIO1_18 IOCON_MUX(42, IOCON_TYPE_D, 1) /* PIO1_18 */
```

相关声明：[CT16B1_CAP1_PIO1_18](#af2925353ca8342deac5cc6c47623b40c)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a15cb6f2cf2ca2ba9b04b54b490e2c88b"></a>

```c
#define U0_TXD_PIO1_18 IOCON_MUX(42, IOCON_TYPE_D, 2) /* PIO1_18 */
```

相关声明：[U0_TXD_PIO1_18](#a15cb6f2cf2ca2ba9b04b54b490e2c88b)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a7a373b17b448fdd55c2b0b4e88750d38"></a>

```c
#define R_27_PIO1_18 IOCON_MUX(42, IOCON_TYPE_D, 3) /* PIO1_18 */
```

相关声明：[R_27_PIO1_18](#a7a373b17b448fdd55c2b0b4e88750d38)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_ae56e1309f5dfaff815c892ef0e1ed2b9"></a>

```c
#define PIO1_19_PIO1_19 IOCON_MUX(43, IOCON_TYPE_D, 0) /* PIO1_19 */
```

相关声明：[PIO1_19_PIO1_19](#ae56e1309f5dfaff815c892ef0e1ed2b9)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a14b9435d73cf7890108f3f7e929154e7"></a>

```c
#define U2_CTS_PIO1_19 IOCON_MUX(43, IOCON_TYPE_D, 1) /* PIO1_19 */
```

相关声明：[U2_CTS_PIO1_19](#a14b9435d73cf7890108f3f7e929154e7)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_ac19819cd774abe2a0597247136804d2e"></a>

```c
#define SCT0_OUT0_PIO1_19 IOCON_MUX(43, IOCON_TYPE_D, 2) /* PIO1_19 */
```

相关声明：[SCT0_OUT0_PIO1_19](#ac19819cd774abe2a0597247136804d2e)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a1a87c8b465b4539dee7d82dcf0067d5b"></a>

```c
#define R_28_PIO1_19 IOCON_MUX(43, IOCON_TYPE_D, 3) /* PIO1_19 */
```

相关声明：[R_28_PIO1_19](#a1a87c8b465b4539dee7d82dcf0067d5b)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_adea5f43202f54b478043589ea1d4b1e1"></a>

```c
#define PIO1_20_PIO1_20 IOCON_MUX(44, IOCON_TYPE_D, 0) /* PIO1_20 */
```

相关声明：[PIO1_20_PIO1_20](#adea5f43202f54b478043589ea1d4b1e1)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a3ed819b62c0253666670f98230fb6194"></a>

```c
#define U0_DSR_PIO1_20 IOCON_MUX(44, IOCON_TYPE_D, 1) /* PIO1_20 */
```

相关声明：[U0_DSR_PIO1_20](#a3ed819b62c0253666670f98230fb6194)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_af998519da9f4ffd89b606b0261f95a1e"></a>

```c
#define SSP1_SCK_PIO1_20 IOCON_MUX(44, IOCON_TYPE_D, 2) /* PIO1_20 */
```

相关声明：[SSP1_SCK_PIO1_20](#af998519da9f4ffd89b606b0261f95a1e)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a55e45a077e426ae5e06508b66d899c4c"></a>

```c
#define CT16B0_MAT0_PIO1_20 IOCON_MUX(44, IOCON_TYPE_D, 3) /* PIO1_20 */
```

相关声明：[CT16B0_MAT0_PIO1_20](#a55e45a077e426ae5e06508b66d899c4c)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a0c6805b1f84117dee5e66f091818d9ca"></a>

```c
#define PIO1_21_PIO1_21 IOCON_MUX(45, IOCON_TYPE_D, 0) /* PIO1_21 */
```

相关声明：[PIO1_21_PIO1_21](#a0c6805b1f84117dee5e66f091818d9ca)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_aaf239310ed5db40a24ca15cc7f48ed2b"></a>

```c
#define U0_DCD_PIO1_21 IOCON_MUX(45, IOCON_TYPE_D, 1) /* PIO1_21 */
```

相关声明：[U0_DCD_PIO1_21](#aaf239310ed5db40a24ca15cc7f48ed2b)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_af44b09e3f6bf4ac86fae8f257a0620c6"></a>

```c
#define SSP1_MISO_PIO1_21 IOCON_MUX(45, IOCON_TYPE_D, 2) /* PIO1_21 */
```

相关声明：[SSP1_MISO_PIO1_21](#af44b09e3f6bf4ac86fae8f257a0620c6)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a1ef21fd46fa25d46c8eb7b8881f4b08c"></a>

```c
#define CT16B0_CAP1_PIO1_21 IOCON_MUX(45, IOCON_TYPE_D, 3) /* PIO1_21 */
```

相关声明：[CT16B0_CAP1_PIO1_21](#a1ef21fd46fa25d46c8eb7b8881f4b08c)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a689cbb1bd742d803a7d512f5be6c4cfb"></a>

```c
#define PIO1_22_PIO1_22 IOCON_MUX(46, IOCON_TYPE_A, 0) /* PIO1_22 */
```

相关声明：[PIO1_22_PIO1_22](#a689cbb1bd742d803a7d512f5be6c4cfb)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_aa39927fc00dacde807c16c4044fa62b5"></a>

```c
#define SSP1_MOSI_PIO1_22 IOCON_MUX(46, IOCON_TYPE_A, 1) /* PIO1_22 */
```

相关声明：[SSP1_MOSI_PIO1_22](#aa39927fc00dacde807c16c4044fa62b5)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_a39a31d62e31f796e3a54f43056577675"></a>

```c
#define CT32B1_CAP1_PIO1_22 IOCON_MUX(46, IOCON_TYPE_A, 2) /* PIO1_22 */
```

相关声明：[CT32B1_CAP1_PIO1_22](#a39a31d62e31f796e3a54f43056577675)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_a9686cbbd0389bec5c771f2776f05cde7"></a>

```c
#define ADC_4_PIO1_22 IOCON_MUX(46, IOCON_TYPE_A, 3) /* PIO1_22 */
```

相关声明：[ADC_4_PIO1_22](#a9686cbbd0389bec5c771f2776f05cde7)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_adfbe0b94e760582fccaa92f88f41d1f4"></a>

```c
#define R_29_PIO1_22 IOCON_MUX(46, IOCON_TYPE_A, 4) /* PIO1_22 */
```

相关声明：[R_29_PIO1_22](#adfbe0b94e760582fccaa92f88f41d1f4)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_ab15b87098dc679562fcd0eb74aa8c761"></a>

```c
#define PIO1_23_PIO1_23 IOCON_MUX(47, IOCON_TYPE_D, 0) /* PIO1_23 */
```

相关声明：[PIO1_23_PIO1_23](#ab15b87098dc679562fcd0eb74aa8c761)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_aa168a44ff47701e1e090bc95de4b4601"></a>

```c
#define CT16B1_MAT1_PIO1_23 IOCON_MUX(47, IOCON_TYPE_D, 1) /* PIO1_23 */
```

相关声明：[CT16B1_MAT1_PIO1_23](#aa168a44ff47701e1e090bc95de4b4601)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a241d8f9f8546f68c66e490a4f42951ca"></a>

```c
#define SSP1_SSEL_PIO1_23 IOCON_MUX(47, IOCON_TYPE_D, 2) /* PIO1_23 */
```

相关声明：[SSP1_SSEL_PIO1_23](#a241d8f9f8546f68c66e490a4f42951ca)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_adbafcde4cb5f052835ed790774e91a67"></a>

```c
#define U2_TXD_PIO1_23 IOCON_MUX(47, IOCON_TYPE_D, 3) /* PIO1_23 */
```

相关声明：[U2_TXD_PIO1_23](#adbafcde4cb5f052835ed790774e91a67)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a86877f01c21462c697dcdf1163ef2057"></a>

```c
#define PIO1_24_PIO1_24 IOCON_MUX(48, IOCON_TYPE_D, 0) /* PIO1_24 */
```

相关声明：[PIO1_24_PIO1_24](#a86877f01c21462c697dcdf1163ef2057)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_aa5758ecd3938aa9210fad9e6a291fb54"></a>

```c
#define CT32B0_MAT0_PIO1_24 IOCON_MUX(48, IOCON_TYPE_D, 1) /* PIO1_24 */
```

相关声明：[CT32B0_MAT0_PIO1_24](#aa5758ecd3938aa9210fad9e6a291fb54)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_ae7f01370d20cb64565a5e0d17190f11c"></a>

```c
#define I2C1_SDA_PIO1_24 IOCON_MUX(48, IOCON_TYPE_D, 2) /* PIO1_24 */
```

相关声明：[I2C1_SDA_PIO1_24](#ae7f01370d20cb64565a5e0d17190f11c)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_ad1f94b842d9d03ecfd95521ad4fc50ef"></a>

```c
#define PIO1_25_PIO1_25 IOCON_MUX(49, IOCON_TYPE_D, 0) /* PIO1_25 */
```

相关声明：[PIO1_25_PIO1_25](#ad1f94b842d9d03ecfd95521ad4fc50ef)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_afc6ec4baef4bad621e4d62ae945a1163"></a>

```c
#define U2_RTS_PIO1_25 IOCON_MUX(49, IOCON_TYPE_D, 1) /* PIO1_25 */
```

相关声明：[U2_RTS_PIO1_25](#afc6ec4baef4bad621e4d62ae945a1163)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a784ceb0c6b7772018f082fcd508cba4f"></a>

```c
#define U2_SCLK_PIO1_25 IOCON_MUX(49, IOCON_TYPE_D, 2) /* PIO1_25 */
```

相关声明：[U2_SCLK_PIO1_25](#a784ceb0c6b7772018f082fcd508cba4f)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_add2cbf06dc14447e4661ce8a3de45f2f"></a>

```c
#define SCT0_IN0_PIO1_25 IOCON_MUX(49, IOCON_TYPE_D, 3) /* PIO1_25 */
```

相关声明：[SCT0_IN0_PIO1_25](#add2cbf06dc14447e4661ce8a3de45f2f)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a387b44f72acc4eb20b382da8f076d195"></a>

```c
#define R_30_PIO1_25 IOCON_MUX(49, IOCON_TYPE_D, 4) /* PIO1_25 */
```

相关声明：[R_30_PIO1_25](#a387b44f72acc4eb20b382da8f076d195)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a6b8c76bf4eb6a9e621363bbd7862a3c5"></a>

```c
#define PIO1_26_PIO1_26 IOCON_MUX(50, IOCON_TYPE_D, 0) /* PIO1_26 */
```

相关声明：[PIO1_26_PIO1_26](#a6b8c76bf4eb6a9e621363bbd7862a3c5)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a1733e97cfa0bb66c7717450596b0cfea"></a>

```c
#define CT32B0_MAT2_PIO1_26 IOCON_MUX(50, IOCON_TYPE_D, 1) /* PIO1_26 */
```

相关声明：[CT32B0_MAT2_PIO1_26](#a1733e97cfa0bb66c7717450596b0cfea)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a3cc2c9440f957296aa32d4636b2d6130"></a>

```c
#define U0_RXD_PIO1_26 IOCON_MUX(50, IOCON_TYPE_D, 2) /* PIO1_26 */
```

相关声明：[U0_RXD_PIO1_26](#a3cc2c9440f957296aa32d4636b2d6130)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_ab0411bc0f8b6654e0f7bb8259cb47e7e"></a>

```c
#define R_19_PIO1_26 IOCON_MUX(50, IOCON_TYPE_D, 3) /* PIO1_26 */
```

相关声明：[R_19_PIO1_26](#ab0411bc0f8b6654e0f7bb8259cb47e7e)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_ac22ea9cd9fdb0dcf4125628fd41ad4e2"></a>

```c
#define PIO1_27_PIO1_27 IOCON_MUX(51, IOCON_TYPE_D, 0) /* PIO1_27 */
```

相关声明：[PIO1_27_PIO1_27](#ac22ea9cd9fdb0dcf4125628fd41ad4e2)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_ac2a89c71d21325e0e64cd8a3d8c4ebdc"></a>

```c
#define CT32B0_MAT3_PIO1_27 IOCON_MUX(51, IOCON_TYPE_D, 1) /* PIO1_27 */
```

相关声明：[CT32B0_MAT3_PIO1_27](#ac2a89c71d21325e0e64cd8a3d8c4ebdc)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_aef4522554340d95f52f21f6896d121c6"></a>

```c
#define U0_TXD_PIO1_27 IOCON_MUX(51, IOCON_TYPE_D, 2) /* PIO1_27 */
```

相关声明：[U0_TXD_PIO1_27](#aef4522554340d95f52f21f6896d121c6)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a629bba740c1f829a7401dbe6972b155e"></a>

```c
#define R_20_PIO1_27 IOCON_MUX(51, IOCON_TYPE_D, 3) /* PIO1_27 */
```

相关声明：[R_20_PIO1_27](#a629bba740c1f829a7401dbe6972b155e)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_adc98f945f54727aa26fb4bb5acccb1b2"></a>

```c
#define SSP1_SCK_PIO1_27 IOCON_MUX(51, IOCON_TYPE_D, 4) /* PIO1_27 */
```

相关声明：[SSP1_SCK_PIO1_27](#adc98f945f54727aa26fb4bb5acccb1b2)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_ae45e38efb89456519fd29191d1bfd41e"></a>

```c
#define PIO1_28_PIO1_28 IOCON_MUX(52, IOCON_TYPE_D, 0) /* PIO1_28 */
```

相关声明：[PIO1_28_PIO1_28](#ae45e38efb89456519fd29191d1bfd41e)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_acbc5db1dfeb27c0e9e9c37760876aa7f"></a>

```c
#define CT32B0_CAP0_PIO1_28 IOCON_MUX(52, IOCON_TYPE_D, 1) /* PIO1_28 */
```

相关声明：[CT32B0_CAP0_PIO1_28](#acbc5db1dfeb27c0e9e9c37760876aa7f)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a2eb7dfc050a7afad6630db88a430ffa4"></a>

```c
#define U0_SCLK_PIO1_28 IOCON_MUX(52, IOCON_TYPE_D, 2) /* PIO1_28 */
```

相关声明：[U0_SCLK_PIO1_28](#a2eb7dfc050a7afad6630db88a430ffa4)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a030246ec2f49c51f0ea088ed565d0f6d"></a>

```c
#define U0_RTS_PIO1_28 IOCON_MUX(52, IOCON_TYPE_D, 3) /* PIO1_28 */
```

相关声明：[U0_RTS_PIO1_28](#a030246ec2f49c51f0ea088ed565d0f6d)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a07775fe074a265e8594cc0f1bc3c4553"></a>

```c
#define PIO1_29_PIO1_29 IOCON_MUX(53, IOCON_TYPE_A, 0) /* PIO1_29 */
```

相关声明：[PIO1_29_PIO1_29](#a07775fe074a265e8594cc0f1bc3c4553)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_afa406dcc3b4ce8853b38782aaee8b34c"></a>

```c
#define SSP0_SCK_PIO1_29 IOCON_MUX(53, IOCON_TYPE_A, 1) /* PIO1_29 */
```

相关声明：[SSP0_SCK_PIO1_29](#afa406dcc3b4ce8853b38782aaee8b34c)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_a8c9a3e151294c9fab0c8ef47d0f0e4fe"></a>

```c
#define CT32B0_CAP1_PIO1_29 IOCON_MUX(53, IOCON_TYPE_A, 2) /* PIO1_29 */
```

相关声明：[CT32B0_CAP1_PIO1_29](#a8c9a3e151294c9fab0c8ef47d0f0e4fe)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_affc255b3a5b093927b05ec78056090fa"></a>

```c
#define U0_DTRn_PIO1_29 IOCON_MUX(53, IOCON_TYPE_A, 3) /* PIO1_29 */
```

相关声明：[U0_DTRn_PIO1_29](#affc255b3a5b093927b05ec78056090fa)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_a15dfb4021a3db0723c8918d89840f569"></a>

```c
#define ADC_10_PIO1_29 IOCON_MUX(53, IOCON_TYPE_A, 4) /* PIO1_29 */
```

相关声明：[ADC_10_PIO1_29](#a15dfb4021a3db0723c8918d89840f569)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_a0452698f8cda9677cc606f6e8386f0c5"></a>

```c
#define PIO1_30_PIO1_30 IOCON_MUX(54, IOCON_TYPE_D, 0) /* PIO1_30 */
```

相关声明：[PIO1_30_PIO1_30](#a0452698f8cda9677cc606f6e8386f0c5)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a8edcf1fdf2dd40db40fc0e3bb226c868"></a>

```c
#define I2C1_SCL_PIO1_30 IOCON_MUX(54, IOCON_TYPE_D, 1) /* PIO1_30 */
```

相关声明：[I2C1_SCL_PIO1_30](#a8edcf1fdf2dd40db40fc0e3bb226c868)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a92bceca4249eed78de2037929325bc58"></a>

```c
#define SCT0_IN3_PIO1_30 IOCON_MUX(54, IOCON_TYPE_D, 2) /* PIO1_30 */
```

相关声明：[SCT0_IN3_PIO1_30](#a92bceca4249eed78de2037929325bc58)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a85192c0b77e70e515a9165852d221208"></a>

```c
#define R_31_PIO1_30 IOCON_MUX(54, IOCON_TYPE_D, 3) /* PIO1_30 */
```

相关声明：[R_31_PIO1_30](#a85192c0b77e70e515a9165852d221208)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_ae459ff2b755df0e5a22378e59fb1ccbc"></a>

```c
#define PIO1_31_PIO1_31 IOCON_MUX(55, IOCON_TYPE_D, 0) /* PIO1_31 */
```

相关声明：[PIO1_31_PIO1_31](#ae459ff2b755df0e5a22378e59fb1ccbc)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a5fafd0c519a03d1f678c7f1c6c3b34ed"></a>

```c
#define PIO2_0_PIO2_0 IOCON_MUX(60, IOCON_TYPE_A, 0) /* PIO2_0 */
```

相关声明：[PIO2_0_PIO2_0](#a5fafd0c519a03d1f678c7f1c6c3b34ed)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_a5f3bfb1721c59d5800bcdf187dbddeb1"></a>

```c
#define XTALIN_PIO2_0 IOCON_MUX(60, IOCON_TYPE_A, 1) /* PIO2_0 */
```

相关声明：[XTALIN_PIO2_0](#a5f3bfb1721c59d5800bcdf187dbddeb1)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_ab18db336e17b21d3e1864f47fbfe211b"></a>

```c
#define PIO2_1_PIO2_1 IOCON_MUX(61, IOCON_TYPE_A, 0) /* PIO2_1 */
```

相关声明：[PIO2_1_PIO2_1](#ab18db336e17b21d3e1864f47fbfe211b)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_a8c1b112e94052158ccefdda7c023d9e0"></a>

```c
#define XTALOUT_PIO2_1 IOCON_MUX(61, IOCON_TYPE_A, 1) /* PIO2_1 */
```

相关声明：[XTALOUT_PIO2_1](#a8c1b112e94052158ccefdda7c023d9e0)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_A](#afd7386a10a00b7f0cfbb44d6ceb66df3)。

<a id="r_a5ee88fb076ffc8f05c54ffa403976fa4"></a>

```c
#define PIO2_2_PIO2_2 IOCON_MUX(63, IOCON_TYPE_D, 0) /* PIO2_2 */
```

相关声明：[PIO2_2_PIO2_2](#a5ee88fb076ffc8f05c54ffa403976fa4)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_aa079f73f9150780aabd8e2cc2325c465"></a>

```c
#define U3_RTS_PIO2_2 IOCON_MUX(63, IOCON_TYPE_D, 1) /* PIO2_2 */
```

相关声明：[U3_RTS_PIO2_2](#aa079f73f9150780aabd8e2cc2325c465)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_ab257d298276dc7d42c7c4ccfbde4b2fe"></a>

```c
#define U3_SCLK_PIO2_2 IOCON_MUX(63, IOCON_TYPE_D, 2) /* PIO2_2 */
```

相关声明：[U3_SCLK_PIO2_2](#ab257d298276dc7d42c7c4ccfbde4b2fe)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_adf678074b20d6e433bd2d9e9fb13681e"></a>

```c
#define SCT0_OUT1_PIO2_2 IOCON_MUX(63, IOCON_TYPE_D, 3) /* PIO2_2 */
```

相关声明：[SCT0_OUT1_PIO2_2](#adf678074b20d6e433bd2d9e9fb13681e)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_ab76b9f2a58719e0cbd557e5b3019861d"></a>

```c
#define PIO2_3_PIO2_3 IOCON_MUX(64, IOCON_TYPE_D, 0) /* PIO2_3 */
```

相关声明：[PIO2_3_PIO2_3](#ab76b9f2a58719e0cbd557e5b3019861d)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a330a0f6bb26f2a8d1881433d42251d88"></a>

```c
#define U3_RXD_PIO2_3 IOCON_MUX(64, IOCON_TYPE_D, 1) /* PIO2_3 */
```

相关声明：[U3_RXD_PIO2_3](#a330a0f6bb26f2a8d1881433d42251d88)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a54da6ec8f7f08351101969ebdbc6d7f9"></a>

```c
#define CT32B0_MAT1_PIO2_3 IOCON_MUX(64, IOCON_TYPE_D, 2) /* PIO2_3 */
```

相关声明：[CT32B0_MAT1_PIO2_3](#a54da6ec8f7f08351101969ebdbc6d7f9)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_aec83c87cf4c5c7a6cd72370978c5f3ab"></a>

```c
#define PIO2_4_PIO2_4 IOCON_MUX(65, IOCON_TYPE_D, 0) /* PIO2_4 */
```

相关声明：[PIO2_4_PIO2_4](#aec83c87cf4c5c7a6cd72370978c5f3ab)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a69efa41cce2c5e868b790df9bb2f2fe5"></a>

```c
#define U3_TXD_PIO2_4 IOCON_MUX(65, IOCON_TYPE_D, 1) /* PIO2_4 */
```

相关声明：[U3_TXD_PIO2_4](#a69efa41cce2c5e868b790df9bb2f2fe5)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a42c6c88c505fdd8101ff9abaa61c7896"></a>

```c
#define CT32B0_MAT2_PIO2_4 IOCON_MUX(65, IOCON_TYPE_D, 2) /* PIO2_4 */
```

相关声明：[CT32B0_MAT2_PIO2_4](#a42c6c88c505fdd8101ff9abaa61c7896)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_abd48058e2c15f74525c6354cf245db73"></a>

```c
#define PIO2_5_PIO2_5 IOCON_MUX(66, IOCON_TYPE_D, 0) /* PIO2_5 */
```

相关声明：[PIO2_5_PIO2_5](#abd48058e2c15f74525c6354cf245db73)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a478a19515c027a5282b061de7a201317"></a>

```c
#define U3_CTS_PIO2_5 IOCON_MUX(66, IOCON_TYPE_D, 1) /* PIO2_5 */
```

相关声明：[U3_CTS_PIO2_5](#a478a19515c027a5282b061de7a201317)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a73d3caf803f8a4df930c63cf4fe3f37c"></a>

```c
#define SCT0_IN1_PIO2_5 IOCON_MUX(66, IOCON_TYPE_D, 2) /* PIO2_5 */
```

相关声明：[SCT0_IN1_PIO2_5](#a73d3caf803f8a4df930c63cf4fe3f37c)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a180b0de4ca0603c2e171c869a52f7580"></a>

```c
#define PIO2_6_PIO2_6 IOCON_MUX(67, IOCON_TYPE_D, 0) /* PIO2_6 */
```

相关声明：[PIO2_6_PIO2_6](#a180b0de4ca0603c2e171c869a52f7580)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_ab9a1ba400672c6486a0f8647164a1397"></a>

```c
#define U1_RTS_PIO2_6 IOCON_MUX(67, IOCON_TYPE_D, 1) /* PIO2_6 */
```

相关声明：[U1_RTS_PIO2_6](#ab9a1ba400672c6486a0f8647164a1397)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a3885a451ceef59f37c8cb470aa3c23d0"></a>

```c
#define U1_SCLK_PIO2_6 IOCON_MUX(67, IOCON_TYPE_D, 2) /* PIO2_6 */
```

相关声明：[U1_SCLK_PIO2_6](#a3885a451ceef59f37c8cb470aa3c23d0)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_ae14001bfffc9a00d61caf9647a3527f0"></a>

```c
#define SCT0_IN2_PIO2_6 IOCON_MUX(67, IOCON_TYPE_D, 3) /* PIO2_6 */
```

相关声明：[SCT0_IN2_PIO2_6](#ae14001bfffc9a00d61caf9647a3527f0)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a7e1cd4171f323202a5b67bb1e9363732"></a>

```c
#define PIO2_7_PIO2_7 IOCON_MUX(68, IOCON_TYPE_D, 0) /* PIO2_7 */
```

相关声明：[PIO2_7_PIO2_7](#a7e1cd4171f323202a5b67bb1e9363732)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a6f00dd7928fb37ed72b08f0ce57ee03c"></a>

```c
#define SSP0_SCK_PIO2_7 IOCON_MUX(68, IOCON_TYPE_D, 1) /* PIO2_7 */
```

相关声明：[SSP0_SCK_PIO2_7](#a6f00dd7928fb37ed72b08f0ce57ee03c)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a41199c507951e02ae2aad6b1b94a2aa5"></a>

```c
#define SCT0_OUT2_PIO2_7 IOCON_MUX(68, IOCON_TYPE_D, 2) /* PIO2_7 */
```

相关声明：[SCT0_OUT2_PIO2_7](#a41199c507951e02ae2aad6b1b94a2aa5)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_aa423ccac69367faeaee101c4ca4d411a"></a>

```c
#define PIO2_8_PIO2_8 IOCON_MUX(69, IOCON_TYPE_D, 0) /* PIO2_8 */
```

相关声明：[PIO2_8_PIO2_8](#aa423ccac69367faeaee101c4ca4d411a)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_af4e4c1f8972faff68d459b159c385dd2"></a>

```c
#define SCT1_IN0_PIO2_8 IOCON_MUX(69, IOCON_TYPE_D, 1) /* PIO2_8 */
```

相关声明：[SCT1_IN0_PIO2_8](#af4e4c1f8972faff68d459b159c385dd2)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_aa849da24aea3e3d29c43cc8f7264b434"></a>

```c
#define PIO2_9_PIO2_9 IOCON_MUX(70, IOCON_TYPE_D, 0) /* PIO2_9 */
```

相关声明：[PIO2_9_PIO2_9](#aa849da24aea3e3d29c43cc8f7264b434)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_afd99a1f94ac011c63fbb8a9a9db511da"></a>

```c
#define SCT1_IN1_PIO2_9 IOCON_MUX(70, IOCON_TYPE_D, 1) /* PIO2_9 */
```

相关声明：[SCT1_IN1_PIO2_9](#afd99a1f94ac011c63fbb8a9a9db511da)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a2471788decdf2d9119ca1245ddc77981"></a>

```c
#define PIO2_10_PIO2_10 IOCON_MUX(71, IOCON_TYPE_D, 0) /* PIO2_10 */
```

相关声明：[PIO2_10_PIO2_10](#a2471788decdf2d9119ca1245ddc77981)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a531b7e88f7193b4ce754081685e6d23f"></a>

```c
#define U4_RTS_PIO2_10 IOCON_MUX(71, IOCON_TYPE_D, 1) /* PIO2_10 */
```

相关声明：[U4_RTS_PIO2_10](#a531b7e88f7193b4ce754081685e6d23f)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a34a74c9cc41c9839ee54dccf1aaa9ad7"></a>

```c
#define U4_SCLK_PIO2_10 IOCON_MUX(71, IOCON_TYPE_D, 2) /* PIO2_10 */
```

相关声明：[U4_SCLK_PIO2_10](#a34a74c9cc41c9839ee54dccf1aaa9ad7)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a25f558f2d23c6a973da481216a331047"></a>

```c
#define PIO2_11_PIO2_11 IOCON_MUX(72, IOCON_TYPE_D, 0) /* PIO2_11 */
```

相关声明：[PIO2_11_PIO2_11](#a25f558f2d23c6a973da481216a331047)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_aaabe5ad6b984f52723df7c958e043cd2"></a>

```c
#define U4_RXD_PIO2_11 IOCON_MUX(72, IOCON_TYPE_D, 1) /* PIO2_11 */
```

相关声明：[U4_RXD_PIO2_11](#aaabe5ad6b984f52723df7c958e043cd2)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a55b8398b79ab94885c5b1a266cc96b67"></a>

```c
#define PIO2_12_PIO2_12 IOCON_MUX(73, IOCON_TYPE_D, 0) /* PIO2_12 */
```

相关声明：[PIO2_12_PIO2_12](#a55b8398b79ab94885c5b1a266cc96b67)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_aa676078e9cc9a7dbb114e9e39bbdee07"></a>

```c
#define U4_TXD_PIO2_12 IOCON_MUX(73, IOCON_TYPE_D, 1) /* PIO2_12 */
```

相关声明：[U4_TXD_PIO2_12](#aa676078e9cc9a7dbb114e9e39bbdee07)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_aad0ffb60a10d384eec0c88137e9f5049"></a>

```c
#define PIO2_13_PIO2_13 IOCON_MUX(74, IOCON_TYPE_D, 0) /* PIO2_13 */
```

相关声明：[PIO2_13_PIO2_13](#aad0ffb60a10d384eec0c88137e9f5049)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a2481a40bdab053f1d25e6fd4daeb90cc"></a>

```c
#define U4_CTS_PIO2_13 IOCON_MUX(74, IOCON_TYPE_D, 1) /* PIO2_13 */
```

相关声明：[U4_CTS_PIO2_13](#a2481a40bdab053f1d25e6fd4daeb90cc)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a4d600902f1f7cfa6d6d7a15dad9fa47e"></a>

```c
#define PIO2_14_PIO2_14 IOCON_MUX(75, IOCON_TYPE_D, 0) /* PIO2_14 */
```

相关声明：[PIO2_14_PIO2_14](#a4d600902f1f7cfa6d6d7a15dad9fa47e)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a372dcaa75ccd7aea049ae958f41e9332"></a>

```c
#define SCT1_IN2_PIO2_14 IOCON_MUX(75, IOCON_TYPE_D, 1) /* PIO2_14 */
```

相关声明：[SCT1_IN2_PIO2_14](#a372dcaa75ccd7aea049ae958f41e9332)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a4247567257584b93a079dde0636a8d82"></a>

```c
#define PIO2_15_PIO2_15 IOCON_MUX(76, IOCON_TYPE_D, 0) /* PIO2_15 */
```

相关声明：[PIO2_15_PIO2_15](#a4247567257584b93a079dde0636a8d82)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_ad4ea56df396ac4cab517d5bd7b735f5c"></a>

```c
#define SCT1_IN3_PIO2_15 IOCON_MUX(76, IOCON_TYPE_D, 1) /* PIO2_15 */
```

相关声明：[SCT1_IN3_PIO2_15](#ad4ea56df396ac4cab517d5bd7b735f5c)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a68ae2af37b444a788e82cbdd59a9518e"></a>

```c
#define PIO2_16_PIO2_16 IOCON_MUX(77, IOCON_TYPE_D, 0) /* PIO2_16 */
```

相关声明：[PIO2_16_PIO2_16](#a68ae2af37b444a788e82cbdd59a9518e)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_affe7ba3bec6cfd4b2bba3533ea8cbd66"></a>

```c
#define SCT1_OUT0_PIO2_16 IOCON_MUX(77, IOCON_TYPE_D, 1) /* PIO2_16 */
```

相关声明：[SCT1_OUT0_PIO2_16](#affe7ba3bec6cfd4b2bba3533ea8cbd66)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_aafd4249d51198bee34d7f03275b70bc6"></a>

```c
#define PIO2_17_PIO2_17 IOCON_MUX(78, IOCON_TYPE_D, 0) /* PIO2_17 */
```

相关声明：[PIO2_17_PIO2_17](#aafd4249d51198bee34d7f03275b70bc6)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a2e3304361cf9766f08c764fac50ef9bc"></a>

```c
#define SCT1_OUT1_PIO2_17 IOCON_MUX(78, IOCON_TYPE_D, 1) /* PIO2_17 */
```

相关声明：[SCT1_OUT1_PIO2_17](#a2e3304361cf9766f08c764fac50ef9bc)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_ab01949c5d3a85a0acb2266d7c4e71b8a"></a>

```c
#define PIO2_18_PIO2_18 IOCON_MUX(79, IOCON_TYPE_D, 0) /* PIO2_18 */
```

相关声明：[PIO2_18_PIO2_18](#ab01949c5d3a85a0acb2266d7c4e71b8a)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_af2c8a7e95a4a2f63e1f86ed9aa83a76f"></a>

```c
#define SCT1_OUT2_PIO2_18 IOCON_MUX(79, IOCON_TYPE_D, 1) /* PIO2_18 */
```

相关声明：[SCT1_OUT2_PIO2_18](#af2c8a7e95a4a2f63e1f86ed9aa83a76f)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a10046d3d553609d2e46568d31bcbd22b"></a>

```c
#define PIO2_19_PIO2_19 IOCON_MUX(80, IOCON_TYPE_D, 0) /* PIO2_19 */
```

相关声明：[PIO2_19_PIO2_19](#a10046d3d553609d2e46568d31bcbd22b)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a89409cbd5a036dd7ff5c5a868eef4521"></a>

```c
#define SCT1_OUT3_PIO2_19 IOCON_MUX(80, IOCON_TYPE_D, 1) /* PIO2_19 */
```

相关声明：[SCT1_OUT3_PIO2_19](#a89409cbd5a036dd7ff5c5a868eef4521)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a379470de275ec9e879c6a7da55dc81e2"></a>

```c
#define PIO2_20_PIO2_20 IOCON_MUX(81, IOCON_TYPE_D, 0) /* PIO2_20 */
```

相关声明：[PIO2_20_PIO2_20](#a379470de275ec9e879c6a7da55dc81e2)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a8cc6a3d1353183ec7277fbb88a405961"></a>

```c
#define PIO2_21_PIO2_21 IOCON_MUX(82, IOCON_TYPE_D, 0) /* PIO2_21 */
```

相关声明：[PIO2_21_PIO2_21](#a8cc6a3d1353183ec7277fbb88a405961)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_a12640000bfec871e24fff6deaa5cdd08"></a>

```c
#define PIO2_22_PIO2_22 IOCON_MUX(83, IOCON_TYPE_D, 0) /* PIO2_22 */
```

相关声明：[PIO2_22_PIO2_22](#a12640000bfec871e24fff6deaa5cdd08)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

<a id="r_ab78b84af5278ada6d4c31bbc85928899"></a>

```c
#define PIO2_23_PIO2_23 IOCON_MUX(84, IOCON_TYPE_D, 0) /* PIO2_23 */
```

相关声明：[PIO2_23_PIO2_23](#ab78b84af5278ada6d4c31bbc85928899)、[IOCON_MUX](#a3c281dcff389739802d68c2fc59d608e)、[IOCON_TYPE_D](#a9ae60793668890cd0dc2117dc64f02ba)。

## 27.2\_详细说明（Detailed Documentation）

<a id="a03ce0c70811dc7195ee48649532f2ebd"></a>

### `ADC_0_PIO1_9`

```c
#define ADC_0_PIO1_9 IOCON_MUX(33, IOCON_TYPE_A, 3) /* PIO1_9 */
```

<a id="a15dfb4021a3db0723c8918d89840f569"></a>

### `ADC_10_PIO1_29`

```c
#define ADC_10_PIO1_29 IOCON_MUX(53, IOCON_TYPE_A, 4) /* PIO1_29 */
```

<a id="aafede8fcd15e8bfe236e95c9a7b49b96"></a>

### `ADC_11_PIO0_22`

```c
#define ADC_11_PIO0_22 IOCON_MUX(22, IOCON_TYPE_A, 1) /* PIO0_22 */
```

<a id="ab00e7a1a150e2e1c9b45d86c850a4a0b"></a>

### `ADC_1_PIO0_23`

```c
#define ADC_1_PIO0_23 IOCON_MUX(23, IOCON_TYPE_A, 1) /* PIO0_23 */
```

<a id="a21eeb0732f5d35d747f63db3eac9cfad"></a>

### `ADC_2_PIO0_16`

```c
#define ADC_2_PIO0_16 IOCON_MUX(16, IOCON_TYPE_A, 2) /* PIO0_16 */
```

<a id="af92fd1b534c099ad808403a199cad8a0"></a>

### `ADC_3_PIO0_15`

```c
#define ADC_3_PIO0_15 IOCON_MUX(15, IOCON_TYPE_A, 2) /* PIO0_15 */
```

<a id="a9686cbbd0389bec5c771f2776f05cde7"></a>

### `ADC_4_PIO1_22`

```c
#define ADC_4_PIO1_22 IOCON_MUX(46, IOCON_TYPE_A, 3) /* PIO1_22 */
```

<a id="ac4f0bd23dfc3f744220cadb6949d4e1f"></a>

### `ADC_5_PIO1_3`

```c
#define ADC_5_PIO1_3 IOCON_MUX(27, IOCON_TYPE_A, 4) /* PIO1_3 */
```

<a id="ae6c3bb89b08367707e91bb00d3f55da5"></a>

### `ADC_6_PIO0_14`

```c
#define ADC_6_PIO0_14 IOCON_MUX(14, IOCON_TYPE_A, 2) /* PIO0_14 */
```

<a id="a706b80599c77ce5212b2359187d3fab1"></a>

### `ADC_7_PIO0_13`

```c
#define ADC_7_PIO0_13 IOCON_MUX(13, IOCON_TYPE_A, 2) /* PIO0_13 */
```

<a id="ae9f30a9545a11701304231e5efb707a5"></a>

### `ADC_8_PIO0_12`

```c
#define ADC_8_PIO0_12 IOCON_MUX(12, IOCON_TYPE_A, 2) /* PIO0_12 */
```

<a id="abfeca937f748f0b54ee4178c072ed1f5"></a>

### `ADC_9_PIO0_11`

```c
#define ADC_9_PIO0_11 IOCON_MUX(11, IOCON_TYPE_A, 2) /* PIO0_11 */
```

<a id="a4d2452db92940671b276775adec24700"></a>

### `CLKOUT_PIO0_1`

```c
#define CLKOUT_PIO0_1 IOCON_MUX(1, IOCON_TYPE_D, 1) /* PIO0_1 */
```

<a id="a2c44ad39551919eaf469137d3d37f78b"></a>

### `CT16B0_CAP0_PIO0_2`

```c
#define CT16B0_CAP0_PIO0_2 IOCON_MUX(2, IOCON_TYPE_D, 2) /* PIO0_2 */
```

<a id="a598b61d037bfcacc335bf0996a477843"></a>

### `CT16B0_CAP0_PIO1_8`

```c
#define CT16B0_CAP0_PIO1_8 IOCON_MUX(32, IOCON_TYPE_D, 3) /* PIO1_8 */
```

<a id="a1ef21fd46fa25d46c8eb7b8881f4b08c"></a>

### `CT16B0_CAP1_PIO1_21`

```c
#define CT16B0_CAP1_PIO1_21 IOCON_MUX(45, IOCON_TYPE_D, 3) /* PIO1_21 */
```

<a id="a27237240e4f0c84be58ac4a40915b30b"></a>

### `CT16B0_CAP2_PIO1_17`

```c
#define CT16B0_CAP2_PIO1_17 IOCON_MUX(41, IOCON_TYPE_D, 1) /* PIO1_17 */
```

<a id="ad3f05ac410ca8c36aa81a57b635c1bb5"></a>

### `CT16B0_MAT0_PIO0_8`

```c
#define CT16B0_MAT0_PIO0_8 IOCON_MUX(8, IOCON_TYPE_D, 2) /* PIO0_8 */
```

<a id="acead3031fd80d06b2f87cf0ad8e9e8e2"></a>

### `CT16B0_MAT0_PIO1_16`

```c
#define CT16B0_MAT0_PIO1_16 IOCON_MUX(40, IOCON_TYPE_D, 2) /* PIO1_16 */
```

<a id="a55e45a077e426ae5e06508b66d899c4c"></a>

### `CT16B0_MAT0_PIO1_20`

```c
#define CT16B0_MAT0_PIO1_20 IOCON_MUX(44, IOCON_TYPE_D, 3) /* PIO1_20 */
```

<a id="a8f50532277b4b0b30b926e1f67a31cf1"></a>

### `CT16B0_MAT1_PIO0_9`

```c
#define CT16B0_MAT1_PIO0_9 IOCON_MUX(9, IOCON_TYPE_D, 2) /* PIO0_9 */
```

<a id="a5b8fcd82c3feca9ed3dfbd2f905b4a74"></a>

### `CT16B0_MAT1_PIO1_12`

```c
#define CT16B0_MAT1_PIO1_12 IOCON_MUX(36, IOCON_TYPE_D, 2) /* PIO1_12 */
```

<a id="adca5657fc469b0f579f7a42f94ca5261"></a>

### `CT16B0_MAT2_PIO0_10`

```c
#define CT16B0_MAT2_PIO0_10 IOCON_MUX(10, IOCON_TYPE_D, 3) /* PIO0_10 */
```

<a id="ad0ae914ba48296f972618dee04cc6490"></a>

### `CT16B0_MAT2_PIO1_11`

```c
#define CT16B0_MAT2_PIO1_11 IOCON_MUX(35, IOCON_TYPE_D, 2) /* PIO1_11 */
```

<a id="aa7942f15263a5a5c36bd4513da5223c2"></a>

### `CT16B1_CAP0_PIO0_20`

```c
#define CT16B1_CAP0_PIO0_20 IOCON_MUX(20, IOCON_TYPE_D, 1) /* PIO0_20 */
```

<a id="a6673a36d9b33d563295063f73c466b58"></a>

### `CT16B1_CAP0_PIO1_7`

```c
#define CT16B1_CAP0_PIO1_7 IOCON_MUX(31, IOCON_TYPE_D, 3) /* PIO1_7 */
```

<a id="a2630aa1a98d13baf6f04f78f005bf704"></a>

### `CT16B1_CAP1_PIO0_22`

```c
#define CT16B1_CAP1_PIO0_22 IOCON_MUX(22, IOCON_TYPE_A, 2) /* PIO0_22 */
```

<a id="af2925353ca8342deac5cc6c47623b40c"></a>

### `CT16B1_CAP1_PIO1_18`

```c
#define CT16B1_CAP1_PIO1_18 IOCON_MUX(42, IOCON_TYPE_D, 1) /* PIO1_18 */
```

<a id="a91549c703ace01d5e5cd3f5477ec156e"></a>

### `CT16B1_MAT0_PIO0_21`

```c
#define CT16B1_MAT0_PIO0_21 IOCON_MUX(21, IOCON_TYPE_D, 1) /* PIO0_21 */
```

<a id="abd7606b5f7f902397d6c2ab8fedfd2b3"></a>

### `CT16B1_MAT0_PIO1_10`

```c
#define CT16B1_MAT0_PIO1_10 IOCON_MUX(34, IOCON_TYPE_D, 3) /* PIO1_10 */
```

<a id="aa168a44ff47701e1e090bc95de4b4601"></a>

### `CT16B1_MAT1_PIO1_23`

```c
#define CT16B1_MAT1_PIO1_23 IOCON_MUX(47, IOCON_TYPE_D, 1) /* PIO1_23 */
```

<a id="a9db77081025e9907d1d90cf993d8a028"></a>

### `CT16B1_MAT1_PIO1_9`

```c
#define CT16B1_MAT1_PIO1_9 IOCON_MUX(33, IOCON_TYPE_A, 2) /* PIO1_9 */
```

<a id="afa844a06c34eb41b114b49aac65d5eb1"></a>

### `CT32B0_CAP0_PIO0_17`

```c
#define CT32B0_CAP0_PIO0_17 IOCON_MUX(17, IOCON_TYPE_D, 2) /* PIO0_17 */
```

<a id="acbc5db1dfeb27c0e9e9c37760876aa7f"></a>

### `CT32B0_CAP0_PIO1_28`

```c
#define CT32B0_CAP0_PIO1_28 IOCON_MUX(52, IOCON_TYPE_D, 1) /* PIO1_28 */
```

<a id="a8c9a3e151294c9fab0c8ef47d0f0e4fe"></a>

### `CT32B0_CAP1_PIO1_29`

```c
#define CT32B0_CAP1_PIO1_29 IOCON_MUX(53, IOCON_TYPE_A, 2) /* PIO1_29 */
```

<a id="a01c2a127b550f1c904cf747a2351c006"></a>

### `CT32B0_CAP1_PIO1_6`

```c
#define CT32B0_CAP1_PIO1_6 IOCON_MUX(30, IOCON_TYPE_D, 3) /* PIO1_6 */
```

<a id="a099d0dca10dd8ac2762ac340473a798b"></a>

### `CT32B0_MAT0_PIO0_18`

```c
#define CT32B0_MAT0_PIO0_18 IOCON_MUX(18, IOCON_TYPE_D, 2) /* PIO0_18 */
```

<a id="aa5758ecd3938aa9210fad9e6a291fb54"></a>

### `CT32B0_MAT0_PIO1_24`

```c
#define CT32B0_MAT0_PIO1_24 IOCON_MUX(48, IOCON_TYPE_D, 1) /* PIO1_24 */
```

<a id="a579df8a29d7f50a93ae328c1aec9385a"></a>

### `CT32B0_MAT1_PIO0_19`

```c
#define CT32B0_MAT1_PIO0_19 IOCON_MUX(19, IOCON_TYPE_D, 2) /* PIO0_19 */
```

<a id="a54da6ec8f7f08351101969ebdbc6d7f9"></a>

### `CT32B0_MAT1_PIO2_3`

```c
#define CT32B0_MAT1_PIO2_3 IOCON_MUX(64, IOCON_TYPE_D, 2) /* PIO2_3 */
```

<a id="aa6fbfccc166375429d6c720684686a24"></a>

### `CT32B0_MAT2_PIO0_1`

```c
#define CT32B0_MAT2_PIO0_1 IOCON_MUX(1, IOCON_TYPE_D, 2) /* PIO0_1 */
```

<a id="a1733e97cfa0bb66c7717450596b0cfea"></a>

### `CT32B0_MAT2_PIO1_26`

```c
#define CT32B0_MAT2_PIO1_26 IOCON_MUX(50, IOCON_TYPE_D, 1) /* PIO1_26 */
```

<a id="a42c6c88c505fdd8101ff9abaa61c7896"></a>

### `CT32B0_MAT2_PIO2_4`

```c
#define CT32B0_MAT2_PIO2_4 IOCON_MUX(65, IOCON_TYPE_D, 2) /* PIO2_4 */
```

<a id="a005db7665d634e68c56b59a3cb5b456d"></a>

### `CT32B0_MAT3_PIO0_11`

```c
#define CT32B0_MAT3_PIO0_11 IOCON_MUX(11, IOCON_TYPE_A, 3) /* PIO0_11 */
```

<a id="ac2a89c71d21325e0e64cd8a3d8c4ebdc"></a>

### `CT32B0_MAT3_PIO1_27`

```c
#define CT32B0_MAT3_PIO1_27 IOCON_MUX(51, IOCON_TYPE_D, 1) /* PIO1_27 */
```

<a id="a7b28030377332811f795cd1462bf631f"></a>

### `CT32B1_CAP0_PIO0_12`

```c
#define CT32B1_CAP0_PIO0_12 IOCON_MUX(12, IOCON_TYPE_A, 3) /* PIO0_12 */
```

<a id="a54bfd60ff58b0148b6848f8b2982442e"></a>

### `CT32B1_CAP0_PIO1_4`

```c
#define CT32B1_CAP0_PIO1_4 IOCON_MUX(28, IOCON_TYPE_D, 1) /* PIO1_4 */
```

<a id="a39a31d62e31f796e3a54f43056577675"></a>

### `CT32B1_CAP1_PIO1_22`

```c
#define CT32B1_CAP1_PIO1_22 IOCON_MUX(46, IOCON_TYPE_A, 2) /* PIO1_22 */
```

<a id="a1ab5d0cd48d5ade99b0a6e4fc8bc9f68"></a>

### `CT32B1_CAP1_PIO1_5`

```c
#define CT32B1_CAP1_PIO1_5 IOCON_MUX(29, IOCON_TYPE_D, 1) /* PIO1_5 */
```

<a id="af55d0700864a68532d8b253344160ebf"></a>

### `CT32B1_MAT0_PIO0_13`

```c
#define CT32B1_MAT0_PIO0_13 IOCON_MUX(13, IOCON_TYPE_A, 3) /* PIO0_13 */
```

<a id="a5ee6340e6fe3b732b6d49bbef6c90155"></a>

### `CT32B1_MAT0_PIO1_0`

```c
#define CT32B1_MAT0_PIO1_0 IOCON_MUX(24, IOCON_TYPE_D, 1) /* PIO1_0 */
```

<a id="acc4bcbd80fa3306bfa4ab8a4d3023c34"></a>

### `CT32B1_MAT1_PIO0_14`

```c
#define CT32B1_MAT1_PIO0_14 IOCON_MUX(14, IOCON_TYPE_A, 3) /* PIO0_14 */
```

<a id="afb61298e6db2c507f6090a86566edc91"></a>

### `CT32B1_MAT1_PIO1_1`

```c
#define CT32B1_MAT1_PIO1_1 IOCON_MUX(25, IOCON_TYPE_D, 1) /* PIO1_1 */
```

<a id="ac5ed12914616e50cac147b251291d3f6"></a>

### `CT32B1_MAT2_PIO0_15`

```c
#define CT32B1_MAT2_PIO0_15 IOCON_MUX(15, IOCON_TYPE_A, 3) /* PIO0_15 */
```

<a id="a7e9fefa7d3b24bcf91c2af8143934e1b"></a>

### `CT32B1_MAT2_PIO1_14`

```c
#define CT32B1_MAT2_PIO1_14 IOCON_MUX(38, IOCON_TYPE_D, 2) /* PIO1_14 */
```

<a id="ab158e092af2c6ad056cc6f4d298c1951"></a>

### `CT32B1_MAT2_PIO1_2`

```c
#define CT32B1_MAT2_PIO1_2 IOCON_MUX(26, IOCON_TYPE_D, 1) /* PIO1_2 */
```

<a id="a26ecf5bab459bde9bbb64ff5a019b09a"></a>

### `CT32B1_MAT3_PIO0_16`

```c
#define CT32B1_MAT3_PIO0_16 IOCON_MUX(16, IOCON_TYPE_A, 3) /* PIO0_16 */
```

<a id="af960ef8b39ccd08fbe57d0fb2808507a"></a>

### `CT32B1_MAT3_PIO1_15`

```c
#define CT32B1_MAT3_PIO1_15 IOCON_MUX(39, IOCON_TYPE_D, 2) /* PIO1_15 */
```

<a id="a7edf5d0d95f5fa253b03ccc77447ed9a"></a>

### `CT32B1_MAT3_PIO1_3`

```c
#define CT32B1_MAT3_PIO1_3 IOCON_MUX(27, IOCON_TYPE_A, 1) /* PIO1_3 */
```

<a id="af03e2705d8630f60521f853e9b4b1d61"></a>

### `I2C0_SCL_PIO0_4`

```c
#define I2C0_SCL_PIO0_4 IOCON_MUX(4, IOCON_TYPE_I, 1) /* PIO0_4 */
```

<a id="a7a30f5f10c3c59925e18d0526fa94431"></a>

### `I2C0_SDA_PIO0_5`

```c
#define I2C0_SDA_PIO0_5 IOCON_MUX(5, IOCON_TYPE_I, 1) /* PIO0_5 */
```

<a id="a747ec67e7cb403d747b9f57429b71983"></a>

### `I2C1_SCL_PIO0_7`

```c
#define I2C1_SCL_PIO0_7 IOCON_MUX(7, IOCON_TYPE_D, 3) /* PIO0_7 */
```

<a id="abd5321e5d55560fb0927e8a26027d001"></a>

### `I2C1_SCL_PIO1_11`

```c
#define I2C1_SCL_PIO1_11 IOCON_MUX(35, IOCON_TYPE_D, 1) /* PIO1_11 */
```

<a id="a8edcf1fdf2dd40db40fc0e3bb226c868"></a>

### `I2C1_SCL_PIO1_30`

```c
#define I2C1_SCL_PIO1_30 IOCON_MUX(54, IOCON_TYPE_D, 1) /* PIO1_30 */
```

<a id="aa478831aabf3f70f44dc83be779f29df"></a>

### `I2C1_SDA_PIO1_14`

```c
#define I2C1_SDA_PIO1_14 IOCON_MUX(38, IOCON_TYPE_D, 1) /* PIO1_14 */
```

<a id="ae7f01370d20cb64565a5e0d17190f11c"></a>

### `I2C1_SDA_PIO1_24`

```c
#define I2C1_SDA_PIO1_24 IOCON_MUX(48, IOCON_TYPE_D, 2) /* PIO1_24 */
```

<a id="ae63879080611307c152e569946e7a7ae"></a>

### `I2C1_SDA_PIO1_3`

```c
#define I2C1_SDA_PIO1_3 IOCON_MUX(27, IOCON_TYPE_A, 3) /* PIO1_3 */
```

<a id="a9a3d4f3e281c382f795b9a769073d4e4"></a>

### `IOCON_ADMODE_EN`

```c
#define IOCON_ADMODE_EN (0 << 7) /* Enable analog input mode. */
```

<a id="a32dad85c69cde862614f7dc694de25e1"></a>

### `IOCON_CLKDIV0`

```c
#define IOCON_CLKDIV0 (0 << 13)
```

<a id="a9cf0243a32cce57e52c3b3931979a0c4"></a>

### `IOCON_CLKDIV1`

```c
#define IOCON_CLKDIV1 (1 << 13)
```

<a id="a05aed1b2f2679b3bb56a1bdc08e032a1"></a>

### `IOCON_CLKDIV2`

```c
#define IOCON_CLKDIV2 (2 << 13)
```

<a id="a96b9d2b722278cdc733ddec36aca82b8"></a>

### `IOCON_CLKDIV3`

```c
#define IOCON_CLKDIV3 (3 << 13)
```

<a id="a293173c3047155fd78ba45a0f4e464f5"></a>

### `IOCON_CLKDIV4`

```c
#define IOCON_CLKDIV4 (4 << 13)
```

<a id="aecba1dab2a9cb8c19052ab56c7efbc6d"></a>

### `IOCON_CLKDIV5`

```c
#define IOCON_CLKDIV5 (5 << 13)
```

<a id="a25f5cc1afc44889d9e77b62923135411"></a>

### `IOCON_CLKDIV6`

```c
#define IOCON_CLKDIV6 (6 << 13)
```

<a id="a516e9d9bc7b1f3aaefd9d09c6ece74d2"></a>

### `IOCON_DIGMODE_EN`

```c
#define IOCON_DIGMODE_EN (1 << 7) /* Enable digital I/O mode. */
```

<a id="a5454c9c23da82b9db63d63866d054989"></a>

### `IOCON_FASTI2C_EN`

```c
#define IOCON_FASTI2C_EN (2 << 8) /* I2C Fast-mode Plus. */
```

<a id="a5a141a4fd02a8a7204cb251e1815b2ff"></a>

### `IOCON_FILTR_DIS`

```c
#define IOCON_FILTR_DIS (1 << 8) /* Disable noise filtering. */
```

<a id="ab08f72eae45dd5656aeca24c346c8626"></a>

### `IOCON_FUNC0`

```c
#define IOCON_FUNC0 0
```

标准数字 I/O 引脚的引脚控制寄存器（pin control register）：

`[0:2]`：功能（function）；`[3:4]`：模式（mode）；`[5]`：迟滞（hysteresis）；`[6]`：输入反相（invert input）；`[7:9]`：保留；`[10]`：开漏模式（open-drain mode）；`[11:12]`：数字滤波采样模式（digital filter sample mode）；`[13:15]`：时钟除数（clock divisor）；`[16:31]`：保留。

数字／模拟 I/O 引脚的控制寄存器（control registers）：

`[0:2]`：功能（function）；`[3:4]`：模式（mode）；`[5]`：迟滞（hysteresis）；`[6]`：输入反相（invert input）；`[7]`：模拟模式（analog mode）；`[8]`：输入毛刺滤波器（input glitch filter）；`[9]`：保留；`[10]`：开漏模式（open-drain mode）；`[11:12]`：数字滤波采样模式（digital filter sample mode）；`[13:15]`：时钟除数（clock divisor）；`[16:31]`：保留。

开漏 I/O 引脚（I2C）的控制寄存器：

`[0:2]`：功能（function）；`[3:7]`：保留；`[8:9]`：I2C 模式；`[10]`：保留；`[11:12]`：数字滤波采样模式（digital filter sample mode）；`[13:15]`：时钟除数（clock divisor）；`[16:31]`：保留。

<a id="ab6449233bd56957c684b9ad694606e3a"></a>

### `IOCON_FUNC1`

```c
#define IOCON_FUNC1 1
```

<a id="a43ebb7abf055ce2491fbba5ef72f6fc7"></a>

### `IOCON_FUNC2`

```c
#define IOCON_FUNC2 2
```

<a id="ace4708e511b3aa9c352600604331bec0"></a>

### `IOCON_FUNC3`

```c
#define IOCON_FUNC3 3
```

<a id="ac621b96a2bd1ee57a83ff1af98287a8d"></a>

### `IOCON_FUNC4`

```c
#define IOCON_FUNC4 4
```

<a id="a0f9630599f40a3f96a5887c7e65508a9"></a>

### `IOCON_FUNC5`

```c
#define IOCON_FUNC5 5
```

<a id="afb7c408ac1f52b7b7e46fde3061fe0b7"></a>

### `IOCON_HYS_EN`

```c
#define IOCON_HYS_EN (1 << 5) /* Enable hysteresis. */
```

<a id="ae1fd1faa316f6c3108b499928f8c9922"></a>

### `IOCON_INV_EN`

```c
#define IOCON_INV_EN (1 << 6) /* Invert input polarity. */
```

<a id="afc593aafe607c88c52864ecb7586ffe9"></a>

### `IOCON_MODE_INACT`

```c
#define IOCON_MODE_INACT (0 << 3) /* No pull resistor. */
```

<a id="a270261df49234519bfd09e076dfcec6c"></a>

### `IOCON_MODE_PULLDOWN`

```c
#define IOCON_MODE_PULLDOWN (1 << 3) /* Enable pull-down resistor. */
```

<a id="ad8fe947d8e7076d6cec01a5b30261141"></a>

### `IOCON_MODE_PULLUP`

```c
#define IOCON_MODE_PULLUP (2 << 3) /* Enable Pull-up resistor. */
```

<a id="a53d705841cc362c6f43ffc1370d71726"></a>

### `IOCON_MODE_REPEATER`

```c
#define IOCON_MODE_REPEATER (3 << 3) /* Repeater mode. */
```

<a id="a3c281dcff389739802d68c2fc59d608e"></a>

### `IOCON_MUX`

```c
#define IOCON_MUX ( offset, type, mux )
```

展开值（Value）：

```c
(((offset & 0xFFF) << 20) |             \
(((type) & 0x3) << 18) |                \
(((mux) & 0xF) << 0))
```

<a id="a226b54f672e61a7a2d2893d9ef8cbc9c"></a>

### `IOCON_OPENDRAIN_EN`

```c
#define IOCON_OPENDRAIN_EN (1 << 10) /* Enable open-drain mode. */
```

<a id="a05f3ba263e98d5ee980f1604e5bb901c"></a>

### `IOCON_S_MODE_0CLK`

```c
#define IOCON_S_MODE_0CLK (0 << 11) /* No input filter. */
```

<a id="a7148355cde16d13476362ff1c1bc1668"></a>

### `IOCON_S_MODE_1CLK`

```c
#define IOCON_S_MODE_1CLK (1 << 11)
```

<a id="a87827c87941a76ce73118c65afb439f5"></a>

### `IOCON_S_MODE_2CLK`

```c
#define IOCON_S_MODE_2CLK (2 << 11)
```

<a id="a54dba7082ab18b6a15eea0a87c119a71"></a>

### `IOCON_S_MODE_3CLK`

```c
#define IOCON_S_MODE_3CLK (3 << 11)
```

<a id="aa7dd24866523506919c8f3fa7a8614a8"></a>

### `IOCON_SFI2C_EN`

```c
#define IOCON_SFI2C_EN (0 << 8) /* I2C standard mode / Fast-mode. */
```

<a id="a897f505b779e01014e235f1d73745787"></a>

### `IOCON_STDI2C_EN`

```c
#define IOCON_STDI2C_EN (1 << 8) /* GPIO functionality. */
```

<a id="afd7386a10a00b7f0cfbb44d6ceb66df3"></a>

### `IOCON_TYPE_A`

```c
#define IOCON_TYPE_A 0x2
```

<a id="a9ae60793668890cd0dc2117dc64f02ba"></a>

### `IOCON_TYPE_D`

```c
#define IOCON_TYPE_D 0x0
```

<a id="a6c16820a5170feb2c133f82216318bbb"></a>

### `IOCON_TYPE_I`

```c
#define IOCON_TYPE_I 0x1
```

<a id="aa1d6732f64540461cae792821ac7b2d6"></a>

### `PIO0_0_PIO0_0`

```c
#define PIO0_0_PIO0_0 IOCON_MUX(0, IOCON_TYPE_D, 1) /* PIO0_0 */
```

<a id="a0b09489a89b80784605cddcc430914d6"></a>

### `PIO0_10_PIO0_10`

```c
#define PIO0_10_PIO0_10 IOCON_MUX(10, IOCON_TYPE_D, 1) /* PIO0_10 */
```

<a id="a157b55ccf1883066cc9217629366b809"></a>

### `PIO0_11_PIO0_11`

```c
#define PIO0_11_PIO0_11 IOCON_MUX(11, IOCON_TYPE_A, 1) /* PIO0_11 */
```

<a id="a51f64447bf880601691ffe859d0f1964"></a>

### `PIO0_12_PIO0_12 [1/2]`

```c
#define PIO0_12_PIO0_12 IOCON_MUX(12, IOCON_TYPE_A, 5) /* PIO0_12 */
```

<a id="ab4b3327e260eccbcccf80f0c1904ac56"></a>

### `PIO0_12_PIO0_12 [2/2]`

```c
#define PIO0_12_PIO0_12 IOCON_MUX(12, IOCON_TYPE_A, 1) /* PIO0_12 */
```

<a id="a8d40f087b829a11db51c16ab2181995c"></a>

### `PIO0_13_PIO0_13 [1/2]`

```c
#define PIO0_13_PIO0_13 IOCON_MUX(13, IOCON_TYPE_A, 5) /* PIO0_13 */
```

<a id="af1f156f6bca42a308c3d154ce6033f5a"></a>

### `PIO0_13_PIO0_13 [2/2]`

```c
#define PIO0_13_PIO0_13 IOCON_MUX(13, IOCON_TYPE_A, 1) /* PIO0_13 */
```

<a id="a692e4e1765be1cbca9897691a6bfbc39"></a>

### `PIO0_14_PIO0_14`

```c
#define PIO0_14_PIO0_14 IOCON_MUX(14, IOCON_TYPE_A, 1) /* PIO0_14 */
```

<a id="a59a92f1c63f7eb548a19f555cfe0208e"></a>

### `PIO0_15_PIO0_15`

```c
#define PIO0_15_PIO0_15 IOCON_MUX(15, IOCON_TYPE_A, 1) /* PIO0_15 */
```

<a id="aa4a10249e5ee8e04ce01f62864476727"></a>

### `PIO0_16_PIO0_16`

```c
#define PIO0_16_PIO0_16 IOCON_MUX(16, IOCON_TYPE_A, 1) /* PIO0_16 */
```

<a id="a34451e215c47228b8337d0aed0c2c929"></a>

### `PIO0_17_PIO0_17`

```c
#define PIO0_17_PIO0_17 IOCON_MUX(17, IOCON_TYPE_D, 0) /* PIO0_17 */
```

<a id="a87d216855b3f78407343517d639cd75c"></a>

### `PIO0_18_PIO0_18`

```c
#define PIO0_18_PIO0_18 IOCON_MUX(18, IOCON_TYPE_D, 0) /* PIO0_18 */
```

<a id="a83757ba41e5c8ff4a04384a6f59550e1"></a>

### `PIO0_19_PIO0_19`

```c
#define PIO0_19_PIO0_19 IOCON_MUX(19, IOCON_TYPE_D, 0) /* PIO0_19 */
```

<a id="ab44c7ff7f772892dbb66149d8064ba04"></a>

### `PIO0_1_PIO0_1`

```c
#define PIO0_1_PIO0_1 IOCON_MUX(1, IOCON_TYPE_D, 0) /* PIO0_1 */
```

<a id="a28a9784674717e3617070ed87923a1f1"></a>

### `PIO0_20_PIO0_20`

```c
#define PIO0_20_PIO0_20 IOCON_MUX(20, IOCON_TYPE_D, 0) /* PIO0_20 */
```

<a id="abfb5b6fa233853dc18ed899fa4418b1b"></a>

### `PIO0_21_PIO0_21`

```c
#define PIO0_21_PIO0_21 IOCON_MUX(21, IOCON_TYPE_D, 0) /* PIO0_21 */
```

<a id="a9df3dda1a040239ee21e73c813659ccd"></a>

### `PIO0_22_PIO0_22`

```c
#define PIO0_22_PIO0_22 IOCON_MUX(22, IOCON_TYPE_A, 0) /* PIO0_22 */
```

<a id="a07878c04e96b6472f26d3760a42ac212"></a>

### `PIO0_23_PIO0_23`

```c
#define PIO0_23_PIO0_23 IOCON_MUX(23, IOCON_TYPE_A, 0) /* PIO0_23 */
```

<a id="ab5a06c37a003d97135fc0da7c9949f60"></a>

### `PIO0_2_PIO0_2`

```c
#define PIO0_2_PIO0_2 IOCON_MUX(2, IOCON_TYPE_D, 0) /* PIO0_2 */
```

<a id="a89f6d1689c8672f14033a31543ced43a"></a>

### `PIO0_3_PIO0_3`

```c
#define PIO0_3_PIO0_3 IOCON_MUX(3, IOCON_TYPE_D, 0) /* PIO0_3 */
```

<a id="a017c42b9bbbacfbbd9310b3f1a918a66"></a>

### `PIO0_4_PIO0_4`

```c
#define PIO0_4_PIO0_4 IOCON_MUX(4, IOCON_TYPE_I, 0) /* PIO0_4 */
```

<a id="aa0fe8d6e7a4f69dd54980143f92df7ab"></a>

### `PIO0_5_PIO0_5`

```c
#define PIO0_5_PIO0_5 IOCON_MUX(5, IOCON_TYPE_I, 0) /* PIO0_5 */
```

<a id="a50ab17a232562ebc41deb8238de35f20"></a>

### `PIO0_6_PIO0_6`

```c
#define PIO0_6_PIO0_6 IOCON_MUX(6, IOCON_TYPE_D, 0) /* PIO0_6 */
```

<a id="a95b8cc1a76a6097556568f4554bf4e3f"></a>

### `PIO0_7_PIO0_7`

```c
#define PIO0_7_PIO0_7 IOCON_MUX(7, IOCON_TYPE_D, 0) /* PIO0_7 */
```

<a id="a9e4b255125ef44e2de5c77743b4010ee"></a>

### `PIO0_8_PIO0_8`

```c
#define PIO0_8_PIO0_8 IOCON_MUX(8, IOCON_TYPE_D, 0) /* PIO0_8 */
```

<a id="a0db63ca26d440f3bc24a48d39fbfcc4b"></a>

### `PIO0_9_PIO0_9`

```c
#define PIO0_9_PIO0_9 IOCON_MUX(9, IOCON_TYPE_D, 0) /* PIO0_9 */
```

<a id="ac68053b619744fbf1c1f17f7b08cf580"></a>

### `PIO1_0_PIO1_0`

```c
#define PIO1_0_PIO1_0 IOCON_MUX(24, IOCON_TYPE_D, 0) /* PIO1_0 */
```

<a id="a037f6a357a5bbea0dc0cb9902c94c846"></a>

### `PIO1_10_PIO1_10`

```c
#define PIO1_10_PIO1_10 IOCON_MUX(34, IOCON_TYPE_D, 0) /* PIO1_10 */
```

<a id="a97b3bfd02acef68ffc82952e49bd03fe"></a>

### `PIO1_11_PIO1_11`

```c
#define PIO1_11_PIO1_11 IOCON_MUX(35, IOCON_TYPE_D, 0) /* PIO1_11 */
```

<a id="a896bd464fd196266a8862fde369e899b"></a>

### `PIO1_12_PIO1_12`

```c
#define PIO1_12_PIO1_12 IOCON_MUX(36, IOCON_TYPE_D, 0) /* PIO1_12 */
```

<a id="ad2d3d8b8bb3a17fab2dc03850b9934e6"></a>

### `PIO1_13_PIO1_13`

```c
#define PIO1_13_PIO1_13 IOCON_MUX(37, IOCON_TYPE_D, 0) /* PIO1_13 */
```

<a id="aec627d88659627216048116352084463"></a>

### `PIO1_14_PIO1_14`

```c
#define PIO1_14_PIO1_14 IOCON_MUX(38, IOCON_TYPE_D, 0) /* PIO1_14 */
```

<a id="ad430442be04fb9768354a29392aa3150"></a>

### `PIO1_15_PIO1_15`

```c
#define PIO1_15_PIO1_15 IOCON_MUX(39, IOCON_TYPE_D, 0) /* PIO1_15 */
```

<a id="a890647261f0d13600177b8da109e7f80"></a>

### `PIO1_16_PIO1_16`

```c
#define PIO1_16_PIO1_16 IOCON_MUX(40, IOCON_TYPE_D, 0) /* PIO1_16 */
```

<a id="ab7c4014e4c5aff2215d00bfbfcdca7c6"></a>

### `PIO1_17_PIO1_17`

```c
#define PIO1_17_PIO1_17 IOCON_MUX(41, IOCON_TYPE_D, 0) /* PIO1_17 */
```

<a id="abd5742cad3a656c0cca0a02ec6b41acf"></a>

### `PIO1_18_PIO1_18`

```c
#define PIO1_18_PIO1_18 IOCON_MUX(42, IOCON_TYPE_D, 0) /* PIO1_18 */
```

<a id="ae56e1309f5dfaff815c892ef0e1ed2b9"></a>

### `PIO1_19_PIO1_19`

```c
#define PIO1_19_PIO1_19 IOCON_MUX(43, IOCON_TYPE_D, 0) /* PIO1_19 */
```

<a id="a299fee16f12cef2f585e132548ba3b72"></a>

### `PIO1_1_PIO1_1`

```c
#define PIO1_1_PIO1_1 IOCON_MUX(25, IOCON_TYPE_D, 0) /* PIO1_1 */
```

<a id="adea5f43202f54b478043589ea1d4b1e1"></a>

### `PIO1_20_PIO1_20`

```c
#define PIO1_20_PIO1_20 IOCON_MUX(44, IOCON_TYPE_D, 0) /* PIO1_20 */
```

<a id="a0c6805b1f84117dee5e66f091818d9ca"></a>

### `PIO1_21_PIO1_21`

```c
#define PIO1_21_PIO1_21 IOCON_MUX(45, IOCON_TYPE_D, 0) /* PIO1_21 */
```

<a id="a689cbb1bd742d803a7d512f5be6c4cfb"></a>

### `PIO1_22_PIO1_22`

```c
#define PIO1_22_PIO1_22 IOCON_MUX(46, IOCON_TYPE_A, 0) /* PIO1_22 */
```

<a id="ab15b87098dc679562fcd0eb74aa8c761"></a>

### `PIO1_23_PIO1_23`

```c
#define PIO1_23_PIO1_23 IOCON_MUX(47, IOCON_TYPE_D, 0) /* PIO1_23 */
```

<a id="a86877f01c21462c697dcdf1163ef2057"></a>

### `PIO1_24_PIO1_24`

```c
#define PIO1_24_PIO1_24 IOCON_MUX(48, IOCON_TYPE_D, 0) /* PIO1_24 */
```

<a id="ad1f94b842d9d03ecfd95521ad4fc50ef"></a>

### `PIO1_25_PIO1_25`

```c
#define PIO1_25_PIO1_25 IOCON_MUX(49, IOCON_TYPE_D, 0) /* PIO1_25 */
```

<a id="a6b8c76bf4eb6a9e621363bbd7862a3c5"></a>

### `PIO1_26_PIO1_26`

```c
#define PIO1_26_PIO1_26 IOCON_MUX(50, IOCON_TYPE_D, 0) /* PIO1_26 */
```

<a id="ac22ea9cd9fdb0dcf4125628fd41ad4e2"></a>

### `PIO1_27_PIO1_27`

```c
#define PIO1_27_PIO1_27 IOCON_MUX(51, IOCON_TYPE_D, 0) /* PIO1_27 */
```

<a id="ae45e38efb89456519fd29191d1bfd41e"></a>

### `PIO1_28_PIO1_28`

```c
#define PIO1_28_PIO1_28 IOCON_MUX(52, IOCON_TYPE_D, 0) /* PIO1_28 */
```

<a id="a07775fe074a265e8594cc0f1bc3c4553"></a>

### `PIO1_29_PIO1_29`

```c
#define PIO1_29_PIO1_29 IOCON_MUX(53, IOCON_TYPE_A, 0) /* PIO1_29 */
```

<a id="a5265479414c8dd9845e6aa5213eda99e"></a>

### `PIO1_2_PIO1_2`

```c
#define PIO1_2_PIO1_2 IOCON_MUX(26, IOCON_TYPE_D, 0) /* PIO1_2 */
```

<a id="a0452698f8cda9677cc606f6e8386f0c5"></a>

### `PIO1_30_PIO1_30`

```c
#define PIO1_30_PIO1_30 IOCON_MUX(54, IOCON_TYPE_D, 0) /* PIO1_30 */
```

<a id="ae459ff2b755df0e5a22378e59fb1ccbc"></a>

### `PIO1_31_PIO1_31`

```c
#define PIO1_31_PIO1_31 IOCON_MUX(55, IOCON_TYPE_D, 0) /* PIO1_31 */
```

<a id="a2d403da5360929eed6c833567c415fe5"></a>

### `PIO1_3_PIO1_3`

```c
#define PIO1_3_PIO1_3 IOCON_MUX(27, IOCON_TYPE_A, 0) /* PIO1_3 */
```

<a id="aecf77d09221ba70819899708b4ad74a8"></a>

### `PIO1_4_PIO1_4`

```c
#define PIO1_4_PIO1_4 IOCON_MUX(28, IOCON_TYPE_D, 0) /* PIO1_4 */
```

<a id="ab070530de6c3105054206c5a526f5730"></a>

### `PIO1_5_PIO1_5`

```c
#define PIO1_5_PIO1_5 IOCON_MUX(29, IOCON_TYPE_D, 0) /* PIO1_5 */
```

<a id="af6b1804a5aefa54e7a3c4dba33394805"></a>

### `PIO1_6_PIO1_6`

```c
#define PIO1_6_PIO1_6 IOCON_MUX(30, IOCON_TYPE_D, 0) /* PIO1_6 */
```

<a id="ab77050cd6c5323ede0c6ce3f52f4f83e"></a>

### `PIO1_7_PIO1_7`

```c
#define PIO1_7_PIO1_7 IOCON_MUX(31, IOCON_TYPE_D, 0) /* PIO1_7 */
```

<a id="a5eb361e081a52918777d89f61c0a26fa"></a>

### `PIO1_8_PIO1_8`

```c
#define PIO1_8_PIO1_8 IOCON_MUX(32, IOCON_TYPE_D, 0) /* PIO1_8 */
```

<a id="a75ab800970f73ac0177aaf8139ba8739"></a>

### `PIO1_9_PIO1_9`

```c
#define PIO1_9_PIO1_9 IOCON_MUX(33, IOCON_TYPE_A, 0) /* PIO1_9 */
```

<a id="a5fafd0c519a03d1f678c7f1c6c3b34ed"></a>

### `PIO2_0_PIO2_0`

```c
#define PIO2_0_PIO2_0 IOCON_MUX(60, IOCON_TYPE_A, 0) /* PIO2_0 */
```

<a id="a2471788decdf2d9119ca1245ddc77981"></a>

### `PIO2_10_PIO2_10`

```c
#define PIO2_10_PIO2_10 IOCON_MUX(71, IOCON_TYPE_D, 0) /* PIO2_10 */
```

<a id="a25f558f2d23c6a973da481216a331047"></a>

### `PIO2_11_PIO2_11`

```c
#define PIO2_11_PIO2_11 IOCON_MUX(72, IOCON_TYPE_D, 0) /* PIO2_11 */
```

<a id="a55b8398b79ab94885c5b1a266cc96b67"></a>

### `PIO2_12_PIO2_12`

```c
#define PIO2_12_PIO2_12 IOCON_MUX(73, IOCON_TYPE_D, 0) /* PIO2_12 */
```

<a id="aad0ffb60a10d384eec0c88137e9f5049"></a>

### `PIO2_13_PIO2_13`

```c
#define PIO2_13_PIO2_13 IOCON_MUX(74, IOCON_TYPE_D, 0) /* PIO2_13 */
```

<a id="a4d600902f1f7cfa6d6d7a15dad9fa47e"></a>

### `PIO2_14_PIO2_14`

```c
#define PIO2_14_PIO2_14 IOCON_MUX(75, IOCON_TYPE_D, 0) /* PIO2_14 */
```

<a id="a4247567257584b93a079dde0636a8d82"></a>

### `PIO2_15_PIO2_15`

```c
#define PIO2_15_PIO2_15 IOCON_MUX(76, IOCON_TYPE_D, 0) /* PIO2_15 */
```

<a id="a68ae2af37b444a788e82cbdd59a9518e"></a>

### `PIO2_16_PIO2_16`

```c
#define PIO2_16_PIO2_16 IOCON_MUX(77, IOCON_TYPE_D, 0) /* PIO2_16 */
```

<a id="aafd4249d51198bee34d7f03275b70bc6"></a>

### `PIO2_17_PIO2_17`

```c
#define PIO2_17_PIO2_17 IOCON_MUX(78, IOCON_TYPE_D, 0) /* PIO2_17 */
```

<a id="ab01949c5d3a85a0acb2266d7c4e71b8a"></a>

### `PIO2_18_PIO2_18`

```c
#define PIO2_18_PIO2_18 IOCON_MUX(79, IOCON_TYPE_D, 0) /* PIO2_18 */
```

<a id="a10046d3d553609d2e46568d31bcbd22b"></a>

### `PIO2_19_PIO2_19`

```c
#define PIO2_19_PIO2_19 IOCON_MUX(80, IOCON_TYPE_D, 0) /* PIO2_19 */
```

<a id="ab18db336e17b21d3e1864f47fbfe211b"></a>

### `PIO2_1_PIO2_1`

```c
#define PIO2_1_PIO2_1 IOCON_MUX(61, IOCON_TYPE_A, 0) /* PIO2_1 */
```

<a id="a379470de275ec9e879c6a7da55dc81e2"></a>

### `PIO2_20_PIO2_20`

```c
#define PIO2_20_PIO2_20 IOCON_MUX(81, IOCON_TYPE_D, 0) /* PIO2_20 */
```

<a id="a8cc6a3d1353183ec7277fbb88a405961"></a>

### `PIO2_21_PIO2_21`

```c
#define PIO2_21_PIO2_21 IOCON_MUX(82, IOCON_TYPE_D, 0) /* PIO2_21 */
```

<a id="a12640000bfec871e24fff6deaa5cdd08"></a>

### `PIO2_22_PIO2_22`

```c
#define PIO2_22_PIO2_22 IOCON_MUX(83, IOCON_TYPE_D, 0) /* PIO2_22 */
```

<a id="ab78b84af5278ada6d4c31bbc85928899"></a>

### `PIO2_23_PIO2_23`

```c
#define PIO2_23_PIO2_23 IOCON_MUX(84, IOCON_TYPE_D, 0) /* PIO2_23 */
```

<a id="a5ee88fb076ffc8f05c54ffa403976fa4"></a>

### `PIO2_2_PIO2_2`

```c
#define PIO2_2_PIO2_2 IOCON_MUX(63, IOCON_TYPE_D, 0) /* PIO2_2 */
```

<a id="ab76b9f2a58719e0cbd557e5b3019861d"></a>

### `PIO2_3_PIO2_3`

```c
#define PIO2_3_PIO2_3 IOCON_MUX(64, IOCON_TYPE_D, 0) /* PIO2_3 */
```

<a id="aec83c87cf4c5c7a6cd72370978c5f3ab"></a>

### `PIO2_4_PIO2_4`

```c
#define PIO2_4_PIO2_4 IOCON_MUX(65, IOCON_TYPE_D, 0) /* PIO2_4 */
```

<a id="abd48058e2c15f74525c6354cf245db73"></a>

### `PIO2_5_PIO2_5`

```c
#define PIO2_5_PIO2_5 IOCON_MUX(66, IOCON_TYPE_D, 0) /* PIO2_5 */
```

<a id="a180b0de4ca0603c2e171c869a52f7580"></a>

### `PIO2_6_PIO2_6`

```c
#define PIO2_6_PIO2_6 IOCON_MUX(67, IOCON_TYPE_D, 0) /* PIO2_6 */
```

<a id="a7e1cd4171f323202a5b67bb1e9363732"></a>

### `PIO2_7_PIO2_7`

```c
#define PIO2_7_PIO2_7 IOCON_MUX(68, IOCON_TYPE_D, 0) /* PIO2_7 */
```

<a id="aa423ccac69367faeaee101c4ca4d411a"></a>

### `PIO2_8_PIO2_8`

```c
#define PIO2_8_PIO2_8 IOCON_MUX(69, IOCON_TYPE_D, 0) /* PIO2_8 */
```

<a id="aa849da24aea3e3d29c43cc8f7264b434"></a>

### `PIO2_9_PIO2_9`

```c
#define PIO2_9_PIO2_9 IOCON_MUX(70, IOCON_TYPE_D, 0) /* PIO2_9 */
```

<a id="a497b4217421b6854a707201765ff12a8"></a>

### `R_0_PIO0_2`

```c
#define R_0_PIO0_2 IOCON_MUX(2, IOCON_TYPE_D, 3) /* PIO0_2 */
```

<a id="a1ac3960333408442de9bd74e694595de"></a>

### `R_10_PIO1_0`

```c
#define R_10_PIO1_0 IOCON_MUX(24, IOCON_TYPE_D, 2) /* PIO1_0 */
```

<a id="aaae95bceef30b054294e7a7eed2d68a4"></a>

### `R_11_PIO1_1`

```c
#define R_11_PIO1_1 IOCON_MUX(25, IOCON_TYPE_D, 2) /* PIO1_1 */
```

<a id="ac7bd9d42184bd9175925b2e789d4e0f8"></a>

### `R_12_PIO1_2`

```c
#define R_12_PIO1_2 IOCON_MUX(26, IOCON_TYPE_D, 2) /* PIO1_2 */
```

<a id="a1f35a5b9268e09e3ff279d0d7b27e8d9"></a>

### `R_13_PIO1_3`

```c
#define R_13_PIO1_3 IOCON_MUX(27, IOCON_TYPE_A, 2) /* PIO1_3 */
```

<a id="aaba8b00d104b3163f0c7cee32b91cf1e"></a>

### `R_14_PIO1_4`

```c
#define R_14_PIO1_4 IOCON_MUX(28, IOCON_TYPE_D, 2) /* PIO1_4 */
```

<a id="adcccebfaed3f6f65e12a4052ff04fdcd"></a>

### `R_15_PIO1_5`

```c
#define R_15_PIO1_5 IOCON_MUX(29, IOCON_TYPE_D, 2) /* PIO1_5 */
```

<a id="a9f77fd7bcd00d7bc4e179cb3c3db622e"></a>

### `R_16_PIO1_6`

```c
#define R_16_PIO1_6 IOCON_MUX(30, IOCON_TYPE_D, 1) /* PIO1_6 */
```

<a id="a2478b21ed3999f9fb27e1ddcc555383f"></a>

### `R_17_PIO1_7`

```c
#define R_17_PIO1_7 IOCON_MUX(31, IOCON_TYPE_D, 1) /* PIO1_7 */
```

<a id="a01a390f0311638bc09569b06839fb7dd"></a>

### `R_18_PIO1_8`

```c
#define R_18_PIO1_8 IOCON_MUX(32, IOCON_TYPE_D, 1) /* PIO1_8 */
```

<a id="ab0411bc0f8b6654e0f7bb8259cb47e7e"></a>

### `R_19_PIO1_26`

```c
#define R_19_PIO1_26 IOCON_MUX(50, IOCON_TYPE_D, 3) /* PIO1_26 */
```

<a id="a54242b6862e052d7d1c2ee998b6d3927"></a>

### `R_1_PIO0_3`

```c
#define R_1_PIO0_3 IOCON_MUX(3, IOCON_TYPE_D, 2) /* PIO0_3 */
```

<a id="a629bba740c1f829a7401dbe6972b155e"></a>

### `R_20_PIO1_27`

```c
#define R_20_PIO1_27 IOCON_MUX(51, IOCON_TYPE_D, 3) /* PIO1_27 */
```

<a id="abe8e17586c29617e61a2671408e84637"></a>

### `R_21_PIO1_12`

```c
#define R_21_PIO1_12 IOCON_MUX(36, IOCON_TYPE_D, 3) /* PIO1_12 */
```

<a id="a8613dd791e9ddf76c84d12c9f25f31ed"></a>

### `R_22_PIO1_13`

```c
#define R_22_PIO1_13 IOCON_MUX(37, IOCON_TYPE_D, 3) /* PIO1_13 */
```

<a id="a75b2a3bdcdc904bce2ed4641fd77d36f"></a>

### `R_23_PIO1_14`

```c
#define R_23_PIO1_14 IOCON_MUX(38, IOCON_TYPE_D, 3) /* PIO1_14 */
```

<a id="a31607e58141be4451603b21142dc2b78"></a>

### `R_24_PIO1_15`

```c
#define R_24_PIO1_15 IOCON_MUX(39, IOCON_TYPE_D, 3) /* PIO1_15 */
```

<a id="afbf96bb8cc6cf2f8f56ac0f48de55a9d"></a>

### `R_25_PIO1_16`

```c
#define R_25_PIO1_16 IOCON_MUX(40, IOCON_TYPE_D, 3) /* PIO1_16 */
```

<a id="a485ea3b9fe56406e22a835ad8101ca2a"></a>

### `R_26_PIO1_17`

```c
#define R_26_PIO1_17 IOCON_MUX(41, IOCON_TYPE_D, 3) /* PIO1_17 */
```

<a id="a7a373b17b448fdd55c2b0b4e88750d38"></a>

### `R_27_PIO1_18`

```c
#define R_27_PIO1_18 IOCON_MUX(42, IOCON_TYPE_D, 3) /* PIO1_18 */
```

<a id="a1a87c8b465b4539dee7d82dcf0067d5b"></a>

### `R_28_PIO1_19`

```c
#define R_28_PIO1_19 IOCON_MUX(43, IOCON_TYPE_D, 3) /* PIO1_19 */
```

<a id="adfbe0b94e760582fccaa92f88f41d1f4"></a>

### `R_29_PIO1_22`

```c
#define R_29_PIO1_22 IOCON_MUX(46, IOCON_TYPE_A, 4) /* PIO1_22 */
```

<a id="ab0e34b062fd26c27d29891c77d8542a0"></a>

### `R_2_PIO0_4`

```c
#define R_2_PIO0_4 IOCON_MUX(4, IOCON_TYPE_I, 2) /* PIO0_4 */
```

<a id="a387b44f72acc4eb20b382da8f076d195"></a>

### `R_30_PIO1_25`

```c
#define R_30_PIO1_25 IOCON_MUX(49, IOCON_TYPE_D, 4) /* PIO1_25 */
```

<a id="a85192c0b77e70e515a9165852d221208"></a>

### `R_31_PIO1_30`

```c
#define R_31_PIO1_30 IOCON_MUX(54, IOCON_TYPE_D, 3) /* PIO1_30 */
```

<a id="a372339383fc7d4d6e70965b744c10e48"></a>

### `R_3_PIO0_5`

```c
#define R_3_PIO0_5 IOCON_MUX(5, IOCON_TYPE_I, 2) /* PIO0_5 */
```

<a id="a49f11eb792f5b0a7ecf80aeaa82291e2"></a>

### `R_4_PIO0_6`

```c
#define R_4_PIO0_6 IOCON_MUX(6, IOCON_TYPE_D, 3) /* PIO0_6 */
```

<a id="aea308935da9604f8bdfea4d58959e518"></a>

### `R_5_PIO0_7`

```c
#define R_5_PIO0_7 IOCON_MUX(7, IOCON_TYPE_D, 2) /* PIO0_7 */
```

<a id="a8feac8b8845786a001a5dedbd2c749cd"></a>

### `R_6_PIO0_8`

```c
#define R_6_PIO0_8 IOCON_MUX(8, IOCON_TYPE_D, 3) /* PIO0_8 */
```

<a id="add1b38cd0b4e6b4557b5feeb39df424e"></a>

### `R_7_PIO0_9`

```c
#define R_7_PIO0_9 IOCON_MUX(9, IOCON_TYPE_D, 3) /* PIO0_9 */
```

<a id="a58df208f71b6efffed28bbabddf45f41"></a>

### `R_8_PIO0_16`

```c
#define R_8_PIO0_16 IOCON_MUX(16, IOCON_TYPE_A, 4) /* PIO0_16 */
```

<a id="ab0d0d78534d6cc1d4cee77b3eee84114"></a>

### `R_9_PIO0_23`

```c
#define R_9_PIO0_23 IOCON_MUX(23, IOCON_TYPE_A, 2) /* PIO0_23 */
```

<a id="a0d784ee93461dd2f05beeb7c9cfa46b7"></a>

### `R_PIO0_6`

```c
#define R_PIO0_6 IOCON_MUX(6, IOCON_TYPE_D, 1) /* PIO0_6 */
```

<a id="abd7869399ab5c12219c1d7e06885e391"></a>

### `RESET_PIO0_0`

```c
#define RESET_PIO0_0 IOCON_MUX(0, IOCON_TYPE_D, 0) /* PIO0_0 */
```

<a id="add2cbf06dc14447e4661ce8a3de45f2f"></a>

### `SCT0_IN0_PIO1_25`

```c
#define SCT0_IN0_PIO1_25 IOCON_MUX(49, IOCON_TYPE_D, 3) /* PIO1_25 */
```

<a id="a73d3caf803f8a4df930c63cf4fe3f37c"></a>

### `SCT0_IN1_PIO2_5`

```c
#define SCT0_IN1_PIO2_5 IOCON_MUX(66, IOCON_TYPE_D, 2) /* PIO2_5 */
```

<a id="ae14001bfffc9a00d61caf9647a3527f0"></a>

### `SCT0_IN2_PIO2_6`

```c
#define SCT0_IN2_PIO2_6 IOCON_MUX(67, IOCON_TYPE_D, 3) /* PIO2_6 */
```

<a id="a92bceca4249eed78de2037929325bc58"></a>

### `SCT0_IN3_PIO1_30`

```c
#define SCT0_IN3_PIO1_30 IOCON_MUX(54, IOCON_TYPE_D, 2) /* PIO1_30 */
```

<a id="ac19819cd774abe2a0597247136804d2e"></a>

### `SCT0_OUT0_PIO1_19`

```c
#define SCT0_OUT0_PIO1_19 IOCON_MUX(43, IOCON_TYPE_D, 2) /* PIO1_19 */
```

<a id="adf678074b20d6e433bd2d9e9fb13681e"></a>

### `SCT0_OUT1_PIO2_2`

```c
#define SCT0_OUT1_PIO2_2 IOCON_MUX(63, IOCON_TYPE_D, 3) /* PIO2_2 */
```

<a id="a41199c507951e02ae2aad6b1b94a2aa5"></a>

### `SCT0_OUT2_PIO2_7`

```c
#define SCT0_OUT2_PIO2_7 IOCON_MUX(68, IOCON_TYPE_D, 2) /* PIO2_7 */
```

<a id="a504a57a6c6e3014ed4df4320736c7713"></a>

### `SCT0_OUT3_PIO1_13`

```c
#define SCT0_OUT3_PIO1_13 IOCON_MUX(37, IOCON_TYPE_D, 2) /* PIO1_13 */
```

<a id="af4e4c1f8972faff68d459b159c385dd2"></a>

### `SCT1_IN0_PIO2_8`

```c
#define SCT1_IN0_PIO2_8 IOCON_MUX(69, IOCON_TYPE_D, 1) /* PIO2_8 */
```

<a id="afd99a1f94ac011c63fbb8a9a9db511da"></a>

### `SCT1_IN1_PIO2_9`

```c
#define SCT1_IN1_PIO2_9 IOCON_MUX(70, IOCON_TYPE_D, 1) /* PIO2_9 */
```

<a id="a372dcaa75ccd7aea049ae958f41e9332"></a>

### `SCT1_IN2_PIO2_14`

```c
#define SCT1_IN2_PIO2_14 IOCON_MUX(75, IOCON_TYPE_D, 1) /* PIO2_14 */
```

<a id="ad4ea56df396ac4cab517d5bd7b735f5c"></a>

### `SCT1_IN3_PIO2_15`

```c
#define SCT1_IN3_PIO2_15 IOCON_MUX(76, IOCON_TYPE_D, 1) /* PIO2_15 */
```

<a id="affe7ba3bec6cfd4b2bba3533ea8cbd66"></a>

### `SCT1_OUT0_PIO2_16`

```c
#define SCT1_OUT0_PIO2_16 IOCON_MUX(77, IOCON_TYPE_D, 1) /* PIO2_16 */
```

<a id="a2e3304361cf9766f08c764fac50ef9bc"></a>

### `SCT1_OUT1_PIO2_17`

```c
#define SCT1_OUT1_PIO2_17 IOCON_MUX(78, IOCON_TYPE_D, 1) /* PIO2_17 */
```

<a id="af2c8a7e95a4a2f63e1f86ed9aa83a76f"></a>

### `SCT1_OUT2_PIO2_18`

```c
#define SCT1_OUT2_PIO2_18 IOCON_MUX(79, IOCON_TYPE_D, 1) /* PIO2_18 */
```

<a id="a89409cbd5a036dd7ff5c5a868eef4521"></a>

### `SCT1_OUT3_PIO2_19`

```c
#define SCT1_OUT3_PIO2_19 IOCON_MUX(80, IOCON_TYPE_D, 1) /* PIO2_19 */
```

<a id="a1d448d4e7bfeed79bc6e3fb14947afa7"></a>

### `SSP0_MISO_PIO0_8`

```c
#define SSP0_MISO_PIO0_8 IOCON_MUX(8, IOCON_TYPE_D, 1) /* PIO0_8 */
```

<a id="adb527bbcf8d059c9bfccdf29f3ac4aa5"></a>

### `SSP0_MISO_PIO1_16`

```c
#define SSP0_MISO_PIO1_16 IOCON_MUX(40, IOCON_TYPE_D, 1) /* PIO1_16 */
```

<a id="af1a1f4c533ae4806d692aff574334ebf"></a>

### `SSP0_MOSI_PIO0_9`

```c
#define SSP0_MOSI_PIO0_9 IOCON_MUX(9, IOCON_TYPE_D, 1) /* PIO0_9 */
```

<a id="a0bc3c1d34d0bc7a92543edd4e743905f"></a>

### `SSP0_MOSI_PIO1_12`

```c
#define SSP0_MOSI_PIO1_12 IOCON_MUX(36, IOCON_TYPE_D, 1) /* PIO1_12 */
```

<a id="ad68005dc04bde783a05f6c47da6dc4ef"></a>

### `SSP0_SCK_PIO0_10`

```c
#define SSP0_SCK_PIO0_10 IOCON_MUX(10, IOCON_TYPE_D, 2) /* PIO0_10 */
```

<a id="a632c9844b7638e69f8846b845dce32f7"></a>

### `SSP0_SCK_PIO0_6`

```c
#define SSP0_SCK_PIO0_6 IOCON_MUX(6, IOCON_TYPE_D, 2) /* PIO0_6 */
```

<a id="afa406dcc3b4ce8853b38782aaee8b34c"></a>

### `SSP0_SCK_PIO1_29`

```c
#define SSP0_SCK_PIO1_29 IOCON_MUX(53, IOCON_TYPE_A, 1) /* PIO1_29 */
```

<a id="a6f00dd7928fb37ed72b08f0ce57ee03c"></a>

### `SSP0_SCK_PIO2_7`

```c
#define SSP0_SCK_PIO2_7 IOCON_MUX(68, IOCON_TYPE_D, 1) /* PIO2_7 */
```

<a id="a883806b472afb21f170006c620fe2b2d"></a>

### `SSP0_SSEL_PIO0_2`

```c
#define SSP0_SSEL_PIO0_2 IOCON_MUX(2, IOCON_TYPE_D, 1) /* PIO0_2 */
```

<a id="acc0fec039c618cf46e788bfb6f651cfe"></a>

### `SSP0_SSEL_PIO1_15`

```c
#define SSP0_SSEL_PIO1_15 IOCON_MUX(39, IOCON_TYPE_D, 1) /* PIO1_15 */
```

<a id="a783a183d806cac03c7db41096bae4272"></a>

### `SSP1_MISO_PIO0_22`

```c
#define SSP1_MISO_PIO0_22 IOCON_MUX(22, IOCON_TYPE_A, 3) /* PIO0_22 */
```

<a id="af44b09e3f6bf4ac86fae8f257a0620c6"></a>

### `SSP1_MISO_PIO1_21`

```c
#define SSP1_MISO_PIO1_21 IOCON_MUX(45, IOCON_TYPE_D, 2) /* PIO1_21 */
```

<a id="aaec77c9670e3e88d00641020ec0d47d6"></a>

### `SSP1_MOSI_PIO0_21`

```c
#define SSP1_MOSI_PIO0_21 IOCON_MUX(21, IOCON_TYPE_D, 2) /* PIO0_21 */
```

<a id="aa39927fc00dacde807c16c4044fa62b5"></a>

### `SSP1_MOSI_PIO1_22`

```c
#define SSP1_MOSI_PIO1_22 IOCON_MUX(46, IOCON_TYPE_A, 1) /* PIO1_22 */
```

<a id="af998519da9f4ffd89b606b0261f95a1e"></a>

### `SSP1_SCK_PIO1_20`

```c
#define SSP1_SCK_PIO1_20 IOCON_MUX(44, IOCON_TYPE_D, 2) /* PIO1_20 */
```

<a id="adc98f945f54727aa26fb4bb5acccb1b2"></a>

### `SSP1_SCK_PIO1_27`

```c
#define SSP1_SCK_PIO1_27 IOCON_MUX(51, IOCON_TYPE_D, 4) /* PIO1_27 */
```

<a id="a0a3ad1a37c02adc62dbae966523e6d4c"></a>

### `SSP1_SSEL_PIO0_23`

```c
#define SSP1_SSEL_PIO0_23 IOCON_MUX(23, IOCON_TYPE_A, 4) /* PIO0_23 */
```

<a id="a241d8f9f8546f68c66e490a4f42951ca"></a>

### `SSP1_SSEL_PIO1_23`

```c
#define SSP1_SSEL_PIO1_23 IOCON_MUX(47, IOCON_TYPE_D, 2) /* PIO1_23 */
```

<a id="a9694c0dc682d5d6be38b963226aaef3c"></a>

### `SWCLK_PIO0_10`

```c
#define SWCLK_PIO0_10 IOCON_MUX(10, IOCON_TYPE_D, 0) /* PIO0_10 */
```

<a id="a0b65345797054d59564518f73eee1602"></a>

### `SWDIO_PIO0_15`

```c
#define SWDIO_PIO0_15 IOCON_MUX(15, IOCON_TYPE_A, 0) /* PIO0_15 */
```

<a id="afbfb770c4372aadbdb6f5c18d399e17e"></a>

### `TDI_PIO0_11`

```c
#define TDI_PIO0_11 IOCON_MUX(11, IOCON_TYPE_A, 0) /* PIO0_11 */
```

<a id="ace1983c57935ab76096a42fa0d9af286"></a>

### `TDO_PIO0_13`

```c
#define TDO_PIO0_13 IOCON_MUX(13, IOCON_TYPE_A, 0) /* PIO0_13 */
```

<a id="a8e608b93b683519cda35d166e08ab587"></a>

### `TMS_PIO0_12`

```c
#define TMS_PIO0_12 IOCON_MUX(12, IOCON_TYPE_A, 0) /* PIO0_12 */
```

<a id="ad8c652abc5c8558f9312bd0ea201d7fc"></a>

### `TRST_PIO0_14`

```c
#define TRST_PIO0_14 IOCON_MUX(14, IOCON_TYPE_A, 0) /* PIO0_14 */
```

<a id="aad418e1711b045ea50806d464c92fbcf"></a>

### `U0_CTS_PIO0_7`

```c
#define U0_CTS_PIO0_7 IOCON_MUX(7, IOCON_TYPE_D, 1) /* PIO0_7 */
```

<a id="a5ec91d14ec34a2080c1d857e1fd6f572"></a>

### `U0_CTS_PIO1_9`

```c
#define U0_CTS_PIO1_9 IOCON_MUX(33, IOCON_TYPE_A, 1) /* PIO1_9 */
```

<a id="aaf239310ed5db40a24ca15cc7f48ed2b"></a>

### `U0_DCD_PIO1_21`

```c
#define U0_DCD_PIO1_21 IOCON_MUX(45, IOCON_TYPE_D, 1) /* PIO1_21 */
```

<a id="a0abbdcaf023079f9181f260779ced50e"></a>

### `U0_DCD_PIO1_5`

```c
#define U0_DCD_PIO1_5 IOCON_MUX(29, IOCON_TYPE_D, 3) /* PIO1_5 */
```

<a id="a3ed819b62c0253666670f98230fb6194"></a>

### `U0_DSR_PIO1_20`

```c
#define U0_DSR_PIO1_20 IOCON_MUX(44, IOCON_TYPE_D, 1) /* PIO1_20 */
```

<a id="a0a7cdf5fa1cae307725c7cf8742cc599"></a>

### `U0_DSR_PIO1_4`

```c
#define U0_DSR_PIO1_4 IOCON_MUX(28, IOCON_TYPE_D, 3) /* PIO1_4 */
```

<a id="a7a17c6326f865f7eee09ec236ce12216"></a>

### `U0_DTR_PIO1_1`

```c
#define U0_DTR_PIO1_1 IOCON_MUX(25, IOCON_TYPE_D, 3) /* PIO1_1 */
```

<a id="affc255b3a5b093927b05ec78056090fa"></a>

### `U0_DTRn_PIO1_29`

```c
#define U0_DTRn_PIO1_29 IOCON_MUX(53, IOCON_TYPE_A, 3) /* PIO1_29 */
```

<a id="a1b2efba93021237e6fd7e3e276fef4e5"></a>

### `U0_RI_PIO0_23`

```c
#define U0_RI_PIO0_23 IOCON_MUX(23, IOCON_TYPE_A, 3) /* PIO0_23 */
```

<a id="aa43f68879f82d124e3d1da1b1a4bee16"></a>

### `U0_RI_PIO1_11`

```c
#define U0_RI_PIO1_11 IOCON_MUX(35, IOCON_TYPE_D, 3) /* PIO1_11 */
```

<a id="ad946bbd06292183b7bdcd8db7d93d980"></a>

### `U0_RTS_PIO0_17`

```c
#define U0_RTS_PIO0_17 IOCON_MUX(17, IOCON_TYPE_D, 1) /* PIO0_17 */
```

<a id="a030246ec2f49c51f0ea088ed565d0f6d"></a>

### `U0_RTS_PIO1_28`

```c
#define U0_RTS_PIO1_28 IOCON_MUX(52, IOCON_TYPE_D, 3) /* PIO1_28 */
```

<a id="a22d6493688b04414c7dc732d43f4c0f2"></a>

### `U0_RXD_PIO0_18`

```c
#define U0_RXD_PIO0_18 IOCON_MUX(18, IOCON_TYPE_D, 1) /* PIO0_18 */
```

<a id="a974de383ed91f1e80b6e67ab95f627d3"></a>

### `U0_RXD_PIO1_17`

```c
#define U0_RXD_PIO1_17 IOCON_MUX(41, IOCON_TYPE_D, 2) /* PIO1_17 */
```

<a id="a3cc2c9440f957296aa32d4636b2d6130"></a>

### `U0_RXD_PIO1_26`

```c
#define U0_RXD_PIO1_26 IOCON_MUX(50, IOCON_TYPE_D, 2) /* PIO1_26 */
```

<a id="a5f911210bf444c31df578680aa92ba9e"></a>

### `U0_SCLK_PIO0_17`

```c
#define U0_SCLK_PIO0_17 IOCON_MUX(17, IOCON_TYPE_D, 3) /* PIO0_17 */
```

<a id="a2eb7dfc050a7afad6630db88a430ffa4"></a>

### `U0_SCLK_PIO1_28`

```c
#define U0_SCLK_PIO1_28 IOCON_MUX(52, IOCON_TYPE_D, 2) /* PIO1_28 */
```

<a id="a602172b5fe5dde4f7064ea152914e3b4"></a>

### `U0_TXD_PIO0_19`

```c
#define U0_TXD_PIO0_19 IOCON_MUX(19, IOCON_TYPE_D, 1) /* PIO0_19 */
```

<a id="a15cb6f2cf2ca2ba9b04b54b490e2c88b"></a>

### `U0_TXD_PIO1_18`

```c
#define U0_TXD_PIO1_18 IOCON_MUX(42, IOCON_TYPE_D, 2) /* PIO1_18 */
```

<a id="aef4522554340d95f52f21f6896d121c6"></a>

### `U0_TXD_PIO1_27`

```c
#define U0_TXD_PIO1_27 IOCON_MUX(51, IOCON_TYPE_D, 2) /* PIO1_27 */
```

<a id="ac58b55301756d90dcbfac6264df577b2"></a>

### `U1_CTS_PIO0_12`

```c
#define U1_CTS_PIO0_12 IOCON_MUX(12, IOCON_TYPE_A, 4) /* PIO0_12 */
```

<a id="ad00e6299050aceda961b3b6af7a78f79"></a>

### `U1_CTS_PIO1_13`

```c
#define U1_CTS_PIO1_13 IOCON_MUX(37, IOCON_TYPE_D, 1) /* PIO1_13 */
```

<a id="aaa87da84c9da4433539b55b513ab932b"></a>

### `U1_RTS_PIO0_11`

```c
#define U1_RTS_PIO0_11 IOCON_MUX(11, IOCON_TYPE_A, 4) /* PIO0_11 */
```

<a id="ab9a1ba400672c6486a0f8647164a1397"></a>

### `U1_RTS_PIO2_6`

```c
#define U1_RTS_PIO2_6 IOCON_MUX(67, IOCON_TYPE_D, 1) /* PIO2_6 */
```

<a id="a3eb45ad4dd10da96ed90153ef3b53665"></a>

### `U1_RXD_PIO0_13`

```c
#define U1_RXD_PIO0_13 IOCON_MUX(13, IOCON_TYPE_A, 4) /* PIO0_13 */
```

<a id="a4af77ea4a454643946504e10d249edcc"></a>

### `U1_RXD_PIO1_2`

```c
#define U1_RXD_PIO1_2 IOCON_MUX(26, IOCON_TYPE_D, 3) /* PIO1_2 */
```

<a id="a3c5e8df87f093df6858f6ceb7e33e5ec"></a>

### `U1_SCLK_PIO0_11`

```c
#define U1_SCLK_PIO0_11 IOCON_MUX(11, IOCON_TYPE_A, 5) /* PIO0_11 */
```

<a id="a3885a451ceef59f37c8cb470aa3c23d0"></a>

### `U1_SCLK_PIO2_6`

```c
#define U1_SCLK_PIO2_6 IOCON_MUX(67, IOCON_TYPE_D, 2) /* PIO2_6 */
```

<a id="a567bb0593686aa6552e868caeb623532"></a>

### `U1_TXD_PIO0_14`

```c
#define U1_TXD_PIO0_14 IOCON_MUX(14, IOCON_TYPE_A, 4) /* PIO0_14 */
```

<a id="a253fad10b49809895c3f27ec3e51a567"></a>

### `U1_TXD_PIO1_8`

```c
#define U1_TXD_PIO1_8 IOCON_MUX(32, IOCON_TYPE_D, 2) /* PIO1_8 */
```

<a id="a14b9435d73cf7890108f3f7e929154e7"></a>

### `U2_CTS_PIO1_19`

```c
#define U2_CTS_PIO1_19 IOCON_MUX(43, IOCON_TYPE_D, 1) /* PIO1_19 */
```

<a id="a23bb3cc2ede010588651fede510df3db"></a>

### `U2_CTS_PIO1_7`

```c
#define U2_CTS_PIO1_7 IOCON_MUX(31, IOCON_TYPE_D, 2) /* PIO1_7 */
```

<a id="a2f2957c1a43d63106ce2d61678103f62"></a>

### `U2_RTS_PIO1_10`

```c
#define U2_RTS_PIO1_10 IOCON_MUX(34, IOCON_TYPE_D, 1) /* PIO1_10 */
```

<a id="afc6ec4baef4bad621e4d62ae945a1163"></a>

### `U2_RTS_PIO1_25`

```c
#define U2_RTS_PIO1_25 IOCON_MUX(49, IOCON_TYPE_D, 1) /* PIO1_25 */
```

<a id="a9fc4de327d564720e61a338e4a5d3b5b"></a>

### `U2_RXD_PIO0_20`

```c
#define U2_RXD_PIO0_20 IOCON_MUX(20, IOCON_TYPE_D, 2) /* PIO0_20 */
```

<a id="a48ac3c0096037bbe64d92b2d2b0e621f"></a>

### `U2_RXD_PIO1_6`

```c
#define U2_RXD_PIO1_6 IOCON_MUX(30, IOCON_TYPE_D, 2) /* PIO1_6 */
```

<a id="ac7236d26fd68c0be4b0f80e7ac6614cd"></a>

### `U2_SCLK_PIO1_10`

```c
#define U2_SCLK_PIO1_10 IOCON_MUX(34, IOCON_TYPE_D, 2) /* PIO1_10 */
```

<a id="a784ceb0c6b7772018f082fcd508cba4f"></a>

### `U2_SCLK_PIO1_25`

```c
#define U2_SCLK_PIO1_25 IOCON_MUX(49, IOCON_TYPE_D, 2) /* PIO1_25 */
```

<a id="a4319b4d5227cd2a7ff75de78a422a870"></a>

### `U2_TXD_PIO1_0`

```c
#define U2_TXD_PIO1_0 IOCON_MUX(24, IOCON_TYPE_D, 3) /* PIO1_0 */
```

<a id="adbafcde4cb5f052835ed790774e91a67"></a>

### `U2_TXD_PIO1_23`

```c
#define U2_TXD_PIO1_23 IOCON_MUX(47, IOCON_TYPE_D, 3) /* PIO1_23 */
```

<a id="a478a19515c027a5282b061de7a201317"></a>

### `U3_CTS_PIO2_5`

```c
#define U3_CTS_PIO2_5 IOCON_MUX(66, IOCON_TYPE_D, 1) /* PIO2_5 */
```

<a id="aa079f73f9150780aabd8e2cc2325c465"></a>

### `U3_RTS_PIO2_2`

```c
#define U3_RTS_PIO2_2 IOCON_MUX(63, IOCON_TYPE_D, 1) /* PIO2_2 */
```

<a id="a330a0f6bb26f2a8d1881433d42251d88"></a>

### `U3_RXD_PIO2_3`

```c
#define U3_RXD_PIO2_3 IOCON_MUX(64, IOCON_TYPE_D, 1) /* PIO2_3 */
```

<a id="ab257d298276dc7d42c7c4ccfbde4b2fe"></a>

### `U3_SCLK_PIO2_2`

```c
#define U3_SCLK_PIO2_2 IOCON_MUX(63, IOCON_TYPE_D, 2) /* PIO2_2 */
```

<a id="a69efa41cce2c5e868b790df9bb2f2fe5"></a>

### `U3_TXD_PIO2_4`

```c
#define U3_TXD_PIO2_4 IOCON_MUX(65, IOCON_TYPE_D, 1) /* PIO2_4 */
```

<a id="a2481a40bdab053f1d25e6fd4daeb90cc"></a>

### `U4_CTS_PIO2_13`

```c
#define U4_CTS_PIO2_13 IOCON_MUX(74, IOCON_TYPE_D, 1) /* PIO2_13 */
```

<a id="a531b7e88f7193b4ce754081685e6d23f"></a>

### `U4_RTS_PIO2_10`

```c
#define U4_RTS_PIO2_10 IOCON_MUX(71, IOCON_TYPE_D, 1) /* PIO2_10 */
```

<a id="aaabe5ad6b984f52723df7c958e043cd2"></a>

### `U4_RXD_PIO2_11`

```c
#define U4_RXD_PIO2_11 IOCON_MUX(72, IOCON_TYPE_D, 1) /* PIO2_11 */
```

<a id="a34a74c9cc41c9839ee54dccf1aaa9ad7"></a>

### `U4_SCLK_PIO2_10`

```c
#define U4_SCLK_PIO2_10 IOCON_MUX(71, IOCON_TYPE_D, 2) /* PIO2_10 */
```

<a id="aa676078e9cc9a7dbb114e9e39bbdee07"></a>

### `U4_TXD_PIO2_12`

```c
#define U4_TXD_PIO2_12 IOCON_MUX(73, IOCON_TYPE_D, 1) /* PIO2_12 */
```

<a id="a827fea9b1eb5d3d16dbb1f95bd06b40e"></a>

### `USB_FTOGGLE_PIO0_1`

```c
#define USB_FTOGGLE_PIO0_1 IOCON_MUX(1, IOCON_TYPE_D, 3) /* PIO0_1 */
```

<a id="a410001d990fb8424e9f6d75f6a7f2c67"></a>

### `USB_VBUS_PIO0_3`

```c
#define USB_VBUS_PIO0_3 IOCON_MUX(3, IOCON_TYPE_D, 1) /* PIO0_3 */
```

<a id="a285bf9c6e5c1b7bfc8ada6ececbe466e"></a>

### `WAKEUP_PIO0_16`

```c
#define WAKEUP_PIO0_16 IOCON_MUX(16, IOCON_TYPE_A, 0) /* PIO0_16 */
```

<a id="a5f3bfb1721c59d5800bcdf187dbddeb1"></a>

### `XTALIN_PIO2_0`

```c
#define XTALIN_PIO2_0 IOCON_MUX(60, IOCON_TYPE_A, 1) /* PIO2_0 */
```

<a id="a8c1b112e94052158ccefdda7c023d9e0"></a>

### `XTALOUT_PIO2_1`

```c
#define XTALOUT_PIO2_1 IOCON_MUX(61, IOCON_TYPE_A, 1) /* PIO2_1 */
```


## 27.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/lpc11u6x-pinctrl_8h_source.html)
- [open](../api_file_reference/P112_zephyr__posix__fcntl.h_文件参考.md#ac843f2e35e60c3bbf1da47d84306f29b)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P026_zephyr__bluetooth__audio__lc3.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P028_zephyr__display__mb_display.h_文件参考.md)
