---
id: learning.zephyr-docs.api-file-runtime-reference.page-58
title: zephyr__dt-bindings__pinctrl__rts5817_pinctrl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rts5817__pinctrl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第58章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_rts5817\_pinctrl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/rts5817__pinctrl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 58.1\_宏定义（Macros）

<a id="r_a0d86d3cc7149941efefca544d9d09687"></a>

```c
#define RTS_FP_PIN_SHIFT 0U
```

相关声明：[RTS_FP_PIN_SHIFT](#a0d86d3cc7149941efefca544d9d09687)。

字段（Fields）：

<a id="r_a6df72421fd2cdd02f6ec00915032bd55"></a>

```c
#define RTS_FP_PIN_MASK 0xFFU
```

相关声明：[RTS_FP_PIN_MASK](#a6df72421fd2cdd02f6ec00915032bd55)。

<a id="r_ad283968ce392871c140457e387567990"></a>

```c
#define RTS_FP_FUNC_SHIFT 8U
```

相关声明：[RTS_FP_FUNC_SHIFT](#ad283968ce392871c140457e387567990)。

<a id="r_a11be88b633bb336cea17e4aef3ba28b7"></a>

```c
#define RTS_FP_FUNC_MASK 0x1FU
```

相关声明：[RTS_FP_FUNC_MASK](#a11be88b633bb336cea17e4aef3ba28b7)。

<a id="r_a060a29a5272edf0e2ace85166ef11e02"></a>

```c
#define RTS_FP_PINMUX(pin, func)
```

相关声明：[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)。

<a id="r_a00a4b2c0c53fae16f519272161662406"></a>

```c
#define RTS_FP_PINMUX_PIN(__pin)
```

相关声明：[RTS_FP_PINMUX_PIN](#a00a4b2c0c53fae16f519272161662406)。

<a id="r_a0b34a17b7f64971b88e2a769f2aa1945"></a>

```c
#define RTS_FP_PINMUX_FUNC(__pin)
```

相关声明：[RTS_FP_PINMUX_FUNC](#a0b34a17b7f64971b88e2a769f2aa1945)。

<a id="r_a3f88bee83fa4766ff2051db077ea6cf4"></a>

```c
#define IO_POWER_1V8 0
```

相关声明：[IO_POWER_1V8](#a3f88bee83fa4766ff2051db077ea6cf4)。

<a id="r_a8d8bfbd5ed75971ac5aff402386c66ff"></a>

```c
#define IO_POWER_3V3 1
```

相关声明：[IO_POWER_3V3](#a8d8bfbd5ed75971ac5aff402386c66ff)。

<a id="r_a389918abc357193b470dbe1a4be0e930"></a>

```c
#define RTS_FP_PIN_FUNC0 0
```

相关声明：[RTS_FP_PIN_FUNC0](#a389918abc357193b470dbe1a4be0e930)。

<a id="r_ac54191d52494ba993c22403ef3ef5a54"></a>

```c
#define RTS_FP_PIN_FUNC1 1
```

相关声明：[RTS_FP_PIN_FUNC1](#ac54191d52494ba993c22403ef3ef5a54)。

<a id="r_a1cab4441342ecb8f20fd51edaef4f0ed"></a>

```c
#define RTS_FP_PIN_FUNC2 2
```

相关声明：[RTS_FP_PIN_FUNC2](#a1cab4441342ecb8f20fd51edaef4f0ed)。

<a id="r_ae802eb7552ed8f1654220895d34019f7"></a>

```c
#define RTS_FP_PIN_FUNC3 3
```

相关声明：[RTS_FP_PIN_FUNC3](#ae802eb7552ed8f1654220895d34019f7)。

<a id="r_acfc7c39167fa068fb091289a1862f6af"></a>

```c
#define RTS_FP_PIN_FUNC4 4
```

相关声明：[RTS_FP_PIN_FUNC4](#acfc7c39167fa068fb091289a1862f6af)。

<a id="r_a0471cb41a9ba24e43d06509935fed060"></a>

```c
#define RTS_FP_PIN_FUNC5 5
```

相关声明：[RTS_FP_PIN_FUNC5](#a0471cb41a9ba24e43d06509935fed060)。

<a id="r_a3d60b76983b5a76fe63a264f6371941c"></a>

```c
#define RTS_FP_PIN_FUNC6 6
```

相关声明：[RTS_FP_PIN_FUNC6](#a3d60b76983b5a76fe63a264f6371941c)。

<a id="r_ac2bd93b428d003c7db4a2fdac6feec49"></a>

```c
#define RTS_FP_PIN_FUNC7 7
```

相关声明：[RTS_FP_PIN_FUNC7](#ac2bd93b428d003c7db4a2fdac6feec49)。

<a id="r_a2b0318fe330590ca569bb9c7d97b1d9b"></a>

```c
#define RTS_FP_PIN_CACHE_CS1 0
```

相关声明：[RTS_FP_PIN_CACHE_CS1](#a2b0318fe330590ca569bb9c7d97b1d9b)。

<a id="r_aef95bc38c6da3249d13fe573f709c650"></a>

```c
#define RTS_FP_PIN_CACHE_MISO 1
```

相关声明：[RTS_FP_PIN_CACHE_MISO](#aef95bc38c6da3249d13fe573f709c650)。

<a id="r_a2335415d2667631c695c26d6fe65bf7a"></a>

```c
#define RTS_FP_PIN_CACHE_MOSI 2
```

相关声明：[RTS_FP_PIN_CACHE_MOSI](#a2335415d2667631c695c26d6fe65bf7a)。

<a id="r_a5ec21db03582cb1c40014d50f39739ea"></a>

```c
#define RTS_FP_PIN_CACHE_SCK 3
```

相关声明：[RTS_FP_PIN_CACHE_SCK](#a5ec21db03582cb1c40014d50f39739ea)。

<a id="r_a6f58a20107979e2ae576f4f9c8806299"></a>

```c
#define RTS_FP_PIN_CACHE_WP 4
```

相关声明：[RTS_FP_PIN_CACHE_WP](#a6f58a20107979e2ae576f4f9c8806299)。

<a id="r_a9e1fb15c389442fdb5e6e36188392b30"></a>

```c
#define RTS_FP_PIN_CACHE_HOLD 5
```

相关声明：[RTS_FP_PIN_CACHE_HOLD](#a9e1fb15c389442fdb5e6e36188392b30)。

<a id="r_aff5cb40d8aa7f9871f51eeae3715583a"></a>

```c
#define RTS_FP_PIN_CACHE_CS2 6
```

相关声明：[RTS_FP_PIN_CACHE_CS2](#aff5cb40d8aa7f9871f51eeae3715583a)。

<a id="r_a6c731bd08a3916ab5a4805cf47498c81"></a>

```c
#define RTS_FP_PIN_SNR_MISO 7
```

相关声明：[RTS_FP_PIN_SNR_MISO](#a6c731bd08a3916ab5a4805cf47498c81)。

<a id="r_a7776a699ad9f44b2e3804347d97781c9"></a>

```c
#define RTS_FP_PIN_SNR_MOSI 8
```

相关声明：[RTS_FP_PIN_SNR_MOSI](#a7776a699ad9f44b2e3804347d97781c9)。

<a id="r_a64d5158ec376452339d4201b5a02a317"></a>

```c
#define RTS_FP_PIN_SNR_CLK 9
```

相关声明：[RTS_FP_PIN_SNR_CLK](#a64d5158ec376452339d4201b5a02a317)。

<a id="r_aac420b01f8d7ac6e331d2c928246d856"></a>

```c
#define RTS_FP_PIN_SSI_M_MISO 10
```

相关声明：[RTS_FP_PIN_SSI_M_MISO](#aac420b01f8d7ac6e331d2c928246d856)。

<a id="r_a48a0f5b8da7f20eeb13eee4f891f340d"></a>

```c
#define RTS_FP_PIN_SSI_M_MOSI 11
```

相关声明：[RTS_FP_PIN_SSI_M_MOSI](#a48a0f5b8da7f20eeb13eee4f891f340d)。

<a id="r_a96bb7de76d6998603362dec377eedbf1"></a>

```c
#define RTS_FP_PIN_SSI_M_CS 12
```

相关声明：[RTS_FP_PIN_SSI_M_CS](#a96bb7de76d6998603362dec377eedbf1)。

<a id="r_ab369f3cf67ec5ab599e3fc5b12c292e2"></a>

```c
#define RTS_FP_PIN_SSI_M_SCK 13
```

相关声明：[RTS_FP_PIN_SSI_M_SCK](#ab369f3cf67ec5ab599e3fc5b12c292e2)。

<a id="r_aa7cd95a7032cd1e78381fe7de8bab92c"></a>

```c
#define RTS_FP_PIN_SCL0 14
```

相关声明：[RTS_FP_PIN_SCL0](#aa7cd95a7032cd1e78381fe7de8bab92c)。

<a id="r_a2c6652775ced1755e87c8bf62078073c"></a>

```c
#define RTS_FP_PIN_SDA0 15
```

相关声明：[RTS_FP_PIN_SDA0](#a2c6652775ced1755e87c8bf62078073c)。

<a id="r_af622afcdf9071172c1eab379e6138a3e"></a>

```c
#define RTS_FP_PIN_SCL2 16
```

相关声明：[RTS_FP_PIN_SCL2](#af622afcdf9071172c1eab379e6138a3e)。

<a id="r_a7ed6aaffa10de7aa8ce5ae4f5dbaf0f5"></a>

```c
#define RTS_FP_PIN_SDA2 17
```

相关声明：[RTS_FP_PIN_SDA2](#a7ed6aaffa10de7aa8ce5ae4f5dbaf0f5)。

<a id="r_ad45589e3484d938e683d77b42c1d7b36"></a>

```c
#define RTS_FP_PIN_SCL1 18
```

相关声明：[RTS_FP_PIN_SCL1](#ad45589e3484d938e683d77b42c1d7b36)。

<a id="r_aca4f6d25271a46ba6bf27ff788950249"></a>

```c
#define RTS_FP_PIN_SDA1 19
```

相关声明：[RTS_FP_PIN_SDA1](#aca4f6d25271a46ba6bf27ff788950249)。

<a id="r_a50e0ea545de7c8889ab802c3146f3a68"></a>

```c
#define RTS_FP_PIN_SSI_S_MISO 20
```

相关声明：[RTS_FP_PIN_SSI_S_MISO](#a50e0ea545de7c8889ab802c3146f3a68)。

<a id="r_a15cd9ee6ce0eeb63fdd27a69df1e5dce"></a>

```c
#define RTS_FP_PIN_SSI_S_MOSI 21
```

相关声明：[RTS_FP_PIN_SSI_S_MOSI](#a15cd9ee6ce0eeb63fdd27a69df1e5dce)。

<a id="r_abd4ba76ad633336cb77b014de0a2ba27"></a>

```c
#define RTS_FP_PIN_SSI_S_CS 22
```

相关声明：[RTS_FP_PIN_SSI_S_CS](#abd4ba76ad633336cb77b014de0a2ba27)。

<a id="r_abeaea6bddcc2c78c8fb87899d747a404"></a>

```c
#define RTS_FP_PIN_SSI_S_SCK 23
```

相关声明：[RTS_FP_PIN_SSI_S_SCK](#abeaea6bddcc2c78c8fb87899d747a404)。

<a id="r_a63cdabfe86d0e1ecf52ee35fef0ae416"></a>

```c
#define RTS_FP_PIN_GPIO14 24
```

相关声明：[RTS_FP_PIN_GPIO14](#a63cdabfe86d0e1ecf52ee35fef0ae416)。

<a id="r_a31d8161b0bb58684e62c0f141fb4b154"></a>

```c
#define RTS_FP_PIN_GPIO15 25
```

相关声明：[RTS_FP_PIN_GPIO15](#a31d8161b0bb58684e62c0f141fb4b154)。

<a id="r_afc0d14eb037e42b83a6432ffcb235cb5"></a>

```c
#define RTS_FP_PIN_AL0 26
```

相关声明：[RTS_FP_PIN_AL0](#afc0d14eb037e42b83a6432ffcb235cb5)。

<a id="r_a39612eeda5cd0c8c627a62da63af4385"></a>

```c
#define RTS_FP_PIN_AL1 27
```

相关声明：[RTS_FP_PIN_AL1](#a39612eeda5cd0c8c627a62da63af4385)。

<a id="r_a608daa00bb6a3fa59c7b92f4daf7fffc"></a>

```c
#define RTS_FP_PIN_AL2 28
```

相关声明：[RTS_FP_PIN_AL2](#a608daa00bb6a3fa59c7b92f4daf7fffc)。

<a id="r_a06c3a4d8fb8e37c72de299a84db39c3c"></a>

```c
#define RTS_FP_PIN_SNR_RST 29
```

相关声明：[RTS_FP_PIN_SNR_RST](#a06c3a4d8fb8e37c72de299a84db39c3c)。

<a id="r_a909360dbc52ba4280c63a8b78250b9e4"></a>

```c
#define RTS_FP_PIN_SNR_CS 30
```

相关声明：[RTS_FP_PIN_SNR_CS](#a909360dbc52ba4280c63a8b78250b9e4)。

<a id="r_a84cc3e4898c14b364662bc7f59e32017"></a>

```c
#define RTS_FP_PIN_SNR_GPIO 31
```

相关声明：[RTS_FP_PIN_SNR_GPIO](#a84cc3e4898c14b364662bc7f59e32017)。

<a id="r_a4a47f85eebe15efad333c93cea938002"></a>

```c
#define P_CACHE_CS2_F_CACHE_CS2 RTS_FP_PINMUX(CACHE_CS2, FUNC0)
```

相关声明：[P_CACHE_CS2_F_CACHE_CS2](#a4a47f85eebe15efad333c93cea938002)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC0](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#aa3ba064ba85ae0da9c55e7cdb8ea09b3)。

<a id="r_a7eb42e20cd04a06edba01c6acbe19ab8"></a>

```c
#define P_CACHE_CS2_F_GPIO RTS_FP_PINMUX(CACHE_CS2, FUNC1)
```

相关声明：[P_CACHE_CS2_F_GPIO](#a7eb42e20cd04a06edba01c6acbe19ab8)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC1](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a3f9b8eb1b4789fef1da73f4eb041ddfc)。

<a id="r_a914dd84fdf371645f287b5d1a8c9ba37"></a>

```c
#define P_SNR_MISO_F_SNR_MISO RTS_FP_PINMUX(SNR_MISO, FUNC0)
```

相关声明：[P_SNR_MISO_F_SNR_MISO](#a914dd84fdf371645f287b5d1a8c9ba37)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC0](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#aa3ba064ba85ae0da9c55e7cdb8ea09b3)。

<a id="r_a779b627f86b1a99c58bf49d26743975e"></a>

```c
#define P_SNR_MOSI_F_SNR_MOSI RTS_FP_PINMUX(SNR_MOSI, FUNC0)
```

相关声明：[P_SNR_MOSI_F_SNR_MOSI](#a779b627f86b1a99c58bf49d26743975e)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC0](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#aa3ba064ba85ae0da9c55e7cdb8ea09b3)。

<a id="r_a5893a9757ab75b5f1f584e05e6fb9987"></a>

```c
#define P_SNR_CLK_F_SNR_CLK RTS_FP_PINMUX(SNR_CLK, FUNC0)
```

相关声明：[P_SNR_CLK_F_SNR_CLK](#a5893a9757ab75b5f1f584e05e6fb9987)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC0](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#aa3ba064ba85ae0da9c55e7cdb8ea09b3)。

<a id="r_a968286abd075ea533eb5123465bf7e3b"></a>

```c
#define P_SSI_M_MISO_F_GPIO RTS_FP_PINMUX(SSI_M_MISO, FUNC0)
```

相关声明：[P_SSI_M_MISO_F_GPIO](#a968286abd075ea533eb5123465bf7e3b)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC0](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#aa3ba064ba85ae0da9c55e7cdb8ea09b3)。

<a id="r_a92872d21a8eba753b68e00be5bf01bec"></a>

```c
#define P_SSI_M_MISO_F_PWM RTS_FP_PINMUX(SSI_M_MISO, FUNC1)
```

相关声明：[P_SSI_M_MISO_F_PWM](#a92872d21a8eba753b68e00be5bf01bec)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC1](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a3f9b8eb1b4789fef1da73f4eb041ddfc)。

<a id="r_a2517cac1b8f241397a2b2fbf663202c6"></a>

```c
#define P_SSI_M_MISO_F_SSI_M_MISO RTS_FP_PINMUX(SSI_M_MISO, FUNC2)
```

相关声明：[P_SSI_M_MISO_F_SSI_M_MISO](#a2517cac1b8f241397a2b2fbf663202c6)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC2](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a0e8023a25dd46655b8eda5b0476ba169)。

<a id="r_a7d1f9550df66688ebc7ff27745faf26e"></a>

```c
#define P_SSI_M_MISO_F_SSI_S_MISO RTS_FP_PINMUX(SSI_M_MISO, FUNC3)
```

相关声明：[P_SSI_M_MISO_F_SSI_S_MISO](#a7d1f9550df66688ebc7ff27745faf26e)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC3](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#adeea02cdf0e8b64c27b6fad4d2b3b2b5)。

<a id="r_a42722a2eeff4605fb27ed2f52ae8f7a2"></a>

```c
#define P_SSI_M_MISO_F_UART1_RX RTS_FP_PINMUX(SSI_M_MISO, FUNC4)
```

相关声明：[P_SSI_M_MISO_F_UART1_RX](#a42722a2eeff4605fb27ed2f52ae8f7a2)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC4](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a769e96bef0ce818be7aa2cb0a0a67753)。

<a id="r_ae880b656172f0d138384ab32e19d1c3a"></a>

```c
#define P_SSI_M_MISO_F_ASIC_DBG RTS_FP_PINMUX(SSI_M_MISO, FUNC5)
```

相关声明：[P_SSI_M_MISO_F_ASIC_DBG](#ae880b656172f0d138384ab32e19d1c3a)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)。

<a id="r_ab6b546dc3736b9fa71ce5a5ebb0b704b"></a>

```c
#define P_SSI_M_MOSI_F_GPIO RTS_FP_PINMUX(SSI_M_MOSI, FUNC0)
```

相关声明：[P_SSI_M_MOSI_F_GPIO](#ab6b546dc3736b9fa71ce5a5ebb0b704b)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC0](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#aa3ba064ba85ae0da9c55e7cdb8ea09b3)。

<a id="r_a89b0219e15bfda208c88db5cd141255e"></a>

```c
#define P_SSI_M_MOSI_F_PWM RTS_FP_PINMUX(SSI_M_MOSI, FUNC1)
```

相关声明：[P_SSI_M_MOSI_F_PWM](#a89b0219e15bfda208c88db5cd141255e)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC1](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a3f9b8eb1b4789fef1da73f4eb041ddfc)。

<a id="r_a9ab848f2fa4474b22e427f2f5075fbc8"></a>

```c
#define P_SSI_M_MOSI_F_SSI_M_MOSI RTS_FP_PINMUX(SSI_M_MOSI, FUNC2)
```

相关声明：[P_SSI_M_MOSI_F_SSI_M_MOSI](#a9ab848f2fa4474b22e427f2f5075fbc8)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC2](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a0e8023a25dd46655b8eda5b0476ba169)。

<a id="r_aaeffb9cfea32f6dd9c549267f5490ce3"></a>

```c
#define P_SSI_M_MOSI_F_SSI_S_MOSI RTS_FP_PINMUX(SSI_M_MOSI, FUNC3)
```

相关声明：[P_SSI_M_MOSI_F_SSI_S_MOSI](#aaeffb9cfea32f6dd9c549267f5490ce3)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC3](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#adeea02cdf0e8b64c27b6fad4d2b3b2b5)。

<a id="r_ada4225e71fba9d763e0f5cf75dfad2d8"></a>

```c
#define P_SSI_M_MOSI_F_UART1_TX RTS_FP_PINMUX(SSI_M_MOSI, FUNC4)
```

相关声明：[P_SSI_M_MOSI_F_UART1_TX](#ada4225e71fba9d763e0f5cf75dfad2d8)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC4](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a769e96bef0ce818be7aa2cb0a0a67753)。

<a id="r_a537c46eca39aa4680b9025461aeaef8f"></a>

```c
#define P_SSI_M_MOSI_F_ASIC_DBG RTS_FP_PINMUX(SSI_M_MOSI, FUNC5)
```

相关声明：[P_SSI_M_MOSI_F_ASIC_DBG](#a537c46eca39aa4680b9025461aeaef8f)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)。

<a id="r_a1b8df3dc04c88e49c732058aa79b7ca8"></a>

```c
#define P_SSI_M_CS_F_GPIO RTS_FP_PINMUX(SSI_M_CS, FUNC0)
```

相关声明：[P_SSI_M_CS_F_GPIO](#a1b8df3dc04c88e49c732058aa79b7ca8)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC0](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#aa3ba064ba85ae0da9c55e7cdb8ea09b3)。

<a id="r_abe22111b99c9ed5063d882f77c0370ed"></a>

```c
#define P_SSI_M_CS_F_PWM RTS_FP_PINMUX(SSI_M_CS, FUNC1)
```

相关声明：[P_SSI_M_CS_F_PWM](#abe22111b99c9ed5063d882f77c0370ed)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC1](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a3f9b8eb1b4789fef1da73f4eb041ddfc)。

<a id="r_a3bd6788c2f836f3f2a905405b89b9514"></a>

```c
#define P_SSI_M_CS_F_SSI_M_CS RTS_FP_PINMUX(SSI_M_CS, FUNC2)
```

相关声明：[P_SSI_M_CS_F_SSI_M_CS](#a3bd6788c2f836f3f2a905405b89b9514)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC2](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a0e8023a25dd46655b8eda5b0476ba169)。

<a id="r_ac2fb549fcec7dcb6ceb79ad0e9943715"></a>

```c
#define P_SSI_M_CS_F_SSI_S_CS RTS_FP_PINMUX(SSI_M_CS, FUNC3)
```

相关声明：[P_SSI_M_CS_F_SSI_S_CS](#ac2fb549fcec7dcb6ceb79ad0e9943715)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC3](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#adeea02cdf0e8b64c27b6fad4d2b3b2b5)。

<a id="r_a51e3b5f76120bf89a15a6d6c3aba216a"></a>

```c
#define P_SSI_M_CS_F_UART1_RTS RTS_FP_PINMUX(SSI_M_CS, FUNC4)
```

相关声明：[P_SSI_M_CS_F_UART1_RTS](#a51e3b5f76120bf89a15a6d6c3aba216a)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC4](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a769e96bef0ce818be7aa2cb0a0a67753)。

<a id="r_ab65122ace4f82cc49f316c4ba934460c"></a>

```c
#define P_SSI_M_CS_F_ASIC_DBG RTS_FP_PINMUX(SSI_M_CS, FUNC5)
```

相关声明：[P_SSI_M_CS_F_ASIC_DBG](#ab65122ace4f82cc49f316c4ba934460c)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)。

<a id="r_a6753107bb0c65ac4a225679fdd88a0ad"></a>

```c
#define P_SSI_M_SCK_F_GPIO RTS_FP_PINMUX(SSI_M_SCK, FUNC0)
```

相关声明：[P_SSI_M_SCK_F_GPIO](#a6753107bb0c65ac4a225679fdd88a0ad)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC0](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#aa3ba064ba85ae0da9c55e7cdb8ea09b3)。

<a id="r_a6f5f7429a5c3f63cce754fe14ff555a3"></a>

```c
#define P_SSI_M_SCK_F_PWM RTS_FP_PINMUX(SSI_M_SCK, FUNC1)
```

相关声明：[P_SSI_M_SCK_F_PWM](#a6f5f7429a5c3f63cce754fe14ff555a3)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC1](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a3f9b8eb1b4789fef1da73f4eb041ddfc)。

<a id="r_a5d532948f33f7a6408a2e4399bec62c5"></a>

```c
#define P_SSI_M_SCK_F_SSI_M_CLK RTS_FP_PINMUX(SSI_M_SCK, FUNC2)
```

相关声明：[P_SSI_M_SCK_F_SSI_M_CLK](#a5d532948f33f7a6408a2e4399bec62c5)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC2](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a0e8023a25dd46655b8eda5b0476ba169)。

<a id="r_a600061a60422801354dfe023947aef25"></a>

```c
#define P_SSI_M_SCK_F_SSI_S_CLK RTS_FP_PINMUX(SSI_M_SCK, FUNC3)
```

相关声明：[P_SSI_M_SCK_F_SSI_S_CLK](#a600061a60422801354dfe023947aef25)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC3](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#adeea02cdf0e8b64c27b6fad4d2b3b2b5)。

<a id="r_a91d430908b44ac2875063711acdf0ec7"></a>

```c
#define P_SSI_M_SCK_F_UART1_CTS RTS_FP_PINMUX(SSI_M_SCK, FUNC4)
```

相关声明：[P_SSI_M_SCK_F_UART1_CTS](#a91d430908b44ac2875063711acdf0ec7)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC4](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a769e96bef0ce818be7aa2cb0a0a67753)。

<a id="r_a8a484b24f884fa4fa9d1194e42e4fe86"></a>

```c
#define P_SSI_M_SCK_F_ASIC_DBG RTS_FP_PINMUX(SSI_M_SCK, FUNC5)
```

相关声明：[P_SSI_M_SCK_F_ASIC_DBG](#a8a484b24f884fa4fa9d1194e42e4fe86)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)。

<a id="r_a93c9fb1eaf95898cef5e6eea63443575"></a>

```c
#define P_SCL0_F_GPIO RTS_FP_PINMUX(SCL0, FUNC0)
```

相关声明：[P_SCL0_F_GPIO](#a93c9fb1eaf95898cef5e6eea63443575)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC0](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#aa3ba064ba85ae0da9c55e7cdb8ea09b3)。

<a id="r_a2b13a1131d870210c1444b6bdc314723"></a>

```c
#define P_SCL0_F_PWM RTS_FP_PINMUX(SCL0, FUNC1)
```

相关声明：[P_SCL0_F_PWM](#a2b13a1131d870210c1444b6bdc314723)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC1](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a3f9b8eb1b4789fef1da73f4eb041ddfc)。

<a id="r_a1150a31f7f74337c32a72c3686fb4276"></a>

```c
#define P_SCL0_F_I2C0_SCL RTS_FP_PINMUX(SCL0, FUNC2)
```

相关声明：[P_SCL0_F_I2C0_SCL](#a1150a31f7f74337c32a72c3686fb4276)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC2](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a0e8023a25dd46655b8eda5b0476ba169)。

<a id="r_aa0dcb4dc8ab00ed5fa6f1b9f0f40abd2"></a>

```c
#define P_SCL0_F_UART0_RX RTS_FP_PINMUX(SCL0, FUNC3)
```

相关声明：[P_SCL0_F_UART0_RX](#aa0dcb4dc8ab00ed5fa6f1b9f0f40abd2)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC3](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#adeea02cdf0e8b64c27b6fad4d2b3b2b5)。

<a id="r_a83b71fc16500ad9496e808929d61afd6"></a>

```c
#define P_SCL0_F_SWD_CLK RTS_FP_PINMUX(SCL0, FUNC4)
```

相关声明：[P_SCL0_F_SWD_CLK](#a83b71fc16500ad9496e808929d61afd6)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC4](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a769e96bef0ce818be7aa2cb0a0a67753)。

<a id="r_a11be314cdaeaad0a19e63fd90f31b535"></a>

```c
#define P_SCL0_F_ASIC_DBG RTS_FP_PINMUX(SCL0, FUNC5)
```

相关声明：[P_SCL0_F_ASIC_DBG](#a11be314cdaeaad0a19e63fd90f31b535)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)。

<a id="r_ad1f8b3436416a1ad6e86064501b74383"></a>

```c
#define P_SDA0_F_GPIO RTS_FP_PINMUX(SDA0, FUNC0)
```

相关声明：[P_SDA0_F_GPIO](#ad1f8b3436416a1ad6e86064501b74383)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC0](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#aa3ba064ba85ae0da9c55e7cdb8ea09b3)。

<a id="r_a12ab555c5c3c87aa1dc94d347464d37c"></a>

```c
#define P_SDA0_F_PWM RTS_FP_PINMUX(SDA0, FUNC1)
```

相关声明：[P_SDA0_F_PWM](#a12ab555c5c3c87aa1dc94d347464d37c)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC1](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a3f9b8eb1b4789fef1da73f4eb041ddfc)。

<a id="r_a38ea3d58ce7c2c62fb152c49a6af1608"></a>

```c
#define P_SDA0_F_I2C0_SDA RTS_FP_PINMUX(SDA0, FUNC2)
```

相关声明：[P_SDA0_F_I2C0_SDA](#a38ea3d58ce7c2c62fb152c49a6af1608)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC2](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a0e8023a25dd46655b8eda5b0476ba169)。

<a id="r_a763fb20b5c481b93e632de8c462f2ae1"></a>

```c
#define P_SDA0_F_UART0_TX RTS_FP_PINMUX(SDA0, FUNC3)
```

相关声明：[P_SDA0_F_UART0_TX](#a763fb20b5c481b93e632de8c462f2ae1)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC3](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#adeea02cdf0e8b64c27b6fad4d2b3b2b5)。

<a id="r_aea565a7fa29340c602c53ffa37bd1b28"></a>

```c
#define P_SDA0_F_SWD_DAT RTS_FP_PINMUX(SDA0, FUNC4)
```

相关声明：[P_SDA0_F_SWD_DAT](#aea565a7fa29340c602c53ffa37bd1b28)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC4](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a769e96bef0ce818be7aa2cb0a0a67753)。

<a id="r_a2b31a4f06153e67068c00c394f6bb9e8"></a>

```c
#define P_SDA0_F_ASIC_DBG RTS_FP_PINMUX(SDA0, FUNC5)
```

相关声明：[P_SDA0_F_ASIC_DBG](#a2b31a4f06153e67068c00c394f6bb9e8)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)。

<a id="r_a4db1ceeef550d16b57ba72da2ab41a84"></a>

```c
#define P_SCL2_F_GPIO RTS_FP_PINMUX(SCL2, FUNC0)
```

相关声明：[P_SCL2_F_GPIO](#a4db1ceeef550d16b57ba72da2ab41a84)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC0](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#aa3ba064ba85ae0da9c55e7cdb8ea09b3)。

<a id="r_a4b3322fcabc5b65b002c1ee689df6406"></a>

```c
#define P_SCL2_F_PWM RTS_FP_PINMUX(SCL2, FUNC1)
```

相关声明：[P_SCL2_F_PWM](#a4b3322fcabc5b65b002c1ee689df6406)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC1](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a3f9b8eb1b4789fef1da73f4eb041ddfc)。

<a id="r_ae75b90a3e6a35554b5ae701f3119c9d7"></a>

```c
#define P_SCL2_F_I2C2_SCL RTS_FP_PINMUX(SCL2, FUNC2)
```

相关声明：[P_SCL2_F_I2C2_SCL](#ae75b90a3e6a35554b5ae701f3119c9d7)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC2](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a0e8023a25dd46655b8eda5b0476ba169)。

<a id="r_a872027642e6de4b8f8e9a5512aadd987"></a>

```c
#define P_SCL2_F_UART0_RX RTS_FP_PINMUX(SCL2, FUNC3)
```

相关声明：[P_SCL2_F_UART0_RX](#a872027642e6de4b8f8e9a5512aadd987)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC3](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#adeea02cdf0e8b64c27b6fad4d2b3b2b5)。

<a id="r_af96067068920171ec2ab22a87a1c936c"></a>

```c
#define P_SCL2_F_SWD_CLK RTS_FP_PINMUX(SCL2, FUNC4)
```

相关声明：[P_SCL2_F_SWD_CLK](#af96067068920171ec2ab22a87a1c936c)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC4](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a769e96bef0ce818be7aa2cb0a0a67753)。

<a id="r_a281bb69027ca60f1a429a4053fd5ad46"></a>

```c
#define P_SCL2_F_ASIC_DBG RTS_FP_PINMUX(SCL2, FUNC5)
```

相关声明：[P_SCL2_F_ASIC_DBG](#a281bb69027ca60f1a429a4053fd5ad46)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)。

<a id="r_ada97ecb5a1d5a96d284ab3a8504fe5a0"></a>

```c
#define P_SDA2_F_GPIO RTS_FP_PINMUX(SDA2, FUNC0)
```

相关声明：[P_SDA2_F_GPIO](#ada97ecb5a1d5a96d284ab3a8504fe5a0)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC0](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#aa3ba064ba85ae0da9c55e7cdb8ea09b3)。

<a id="r_af9da47bd61d0407339bd91322e32b7ed"></a>

```c
#define P_SDA2_F_PWM RTS_FP_PINMUX(SDA2, FUNC1)
```

相关声明：[P_SDA2_F_PWM](#af9da47bd61d0407339bd91322e32b7ed)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC1](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a3f9b8eb1b4789fef1da73f4eb041ddfc)。

<a id="r_a19cbf93bdf3c372ea6c0f90170c5f79a"></a>

```c
#define P_SDA2_F_I2C2_SDA RTS_FP_PINMUX(SDA2, FUNC2)
```

相关声明：[P_SDA2_F_I2C2_SDA](#a19cbf93bdf3c372ea6c0f90170c5f79a)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC2](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a0e8023a25dd46655b8eda5b0476ba169)。

<a id="r_ac3c53cf3f39b8b853ad9c347eb3af01e"></a>

```c
#define P_SDA2_F_UART0_TX RTS_FP_PINMUX(SDA2, FUNC3)
```

相关声明：[P_SDA2_F_UART0_TX](#ac3c53cf3f39b8b853ad9c347eb3af01e)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC3](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#adeea02cdf0e8b64c27b6fad4d2b3b2b5)。

<a id="r_a5fc2cf735abde2b818f4fe7be6a63136"></a>

```c
#define P_SDA2_F_SWD_DAT RTS_FP_PINMUX(SDA2, FUNC4)
```

相关声明：[P_SDA2_F_SWD_DAT](#a5fc2cf735abde2b818f4fe7be6a63136)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC4](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a769e96bef0ce818be7aa2cb0a0a67753)。

<a id="r_a7b421307c769dd48518866f2277da78d"></a>

```c
#define P_SDA2_F_ASIC_DBG RTS_FP_PINMUX(SDA2, FUNC5)
```

相关声明：[P_SDA2_F_ASIC_DBG](#a7b421307c769dd48518866f2277da78d)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)。

<a id="r_ae613d7ae922cdda329e394247acfcedf"></a>

```c
#define P_SCL1_F_GPIO RTS_FP_PINMUX(SCL1, FUNC0)
```

相关声明：[P_SCL1_F_GPIO](#ae613d7ae922cdda329e394247acfcedf)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC0](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#aa3ba064ba85ae0da9c55e7cdb8ea09b3)。

<a id="r_a6c812b17fafe4a766bb0ade88f9d4f07"></a>

```c
#define P_SCL1_F_PWM RTS_FP_PINMUX(SCL1, FUNC1)
```

相关声明：[P_SCL1_F_PWM](#a6c812b17fafe4a766bb0ade88f9d4f07)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC1](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a3f9b8eb1b4789fef1da73f4eb041ddfc)。

<a id="r_aa7264cbb291a6b0f6b6f74052a6a7c02"></a>

```c
#define P_SCL1_F_I2C1_SCL RTS_FP_PINMUX(SCL1, FUNC2)
```

相关声明：[P_SCL1_F_I2C1_SCL](#aa7264cbb291a6b0f6b6f74052a6a7c02)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC2](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a0e8023a25dd46655b8eda5b0476ba169)。

<a id="r_a506f4b9df4725e1a39e9945bb82ffbbf"></a>

```c
#define P_SCL1_F_JTAG_TCK RTS_FP_PINMUX(SCL1, FUNC4)
```

相关声明：[P_SCL1_F_JTAG_TCK](#a506f4b9df4725e1a39e9945bb82ffbbf)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC4](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a769e96bef0ce818be7aa2cb0a0a67753)。

<a id="r_a3de25c1c2e567fce3f0b6478aa97ff68"></a>

```c
#define P_SDA1_F_GPIO RTS_FP_PINMUX(SDA1, FUNC0)
```

相关声明：[P_SDA1_F_GPIO](#a3de25c1c2e567fce3f0b6478aa97ff68)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC0](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#aa3ba064ba85ae0da9c55e7cdb8ea09b3)。

<a id="r_abc0cf4a117b468ac20c8d27f04c14d0b"></a>

```c
#define P_SDA1_F_PWM RTS_FP_PINMUX(SDA1, FUNC1)
```

相关声明：[P_SDA1_F_PWM](#abc0cf4a117b468ac20c8d27f04c14d0b)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC1](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a3f9b8eb1b4789fef1da73f4eb041ddfc)。

<a id="r_a504506040440518430691da469e31e3a"></a>

```c
#define P_SDA1_F_I2C1_SDA RTS_FP_PINMUX(SDA1, FUNC2)
```

相关声明：[P_SDA1_F_I2C1_SDA](#a504506040440518430691da469e31e3a)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC2](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a0e8023a25dd46655b8eda5b0476ba169)。

<a id="r_a68abee9633dea12c63bb27fc511b4594"></a>

```c
#define P_SDA1_F_JTAG_TMS RTS_FP_PINMUX(SDA1, FUNC4)
```

相关声明：[P_SDA1_F_JTAG_TMS](#a68abee9633dea12c63bb27fc511b4594)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC4](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a769e96bef0ce818be7aa2cb0a0a67753)。

<a id="r_aafb6a04bc4558f1d2b77a3d3b7009f3d"></a>

```c
#define P_SSI_S_MISO_F_GPIO RTS_FP_PINMUX(SSI_S_MISO, FUNC0)
```

相关声明：[P_SSI_S_MISO_F_GPIO](#aafb6a04bc4558f1d2b77a3d3b7009f3d)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC0](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#aa3ba064ba85ae0da9c55e7cdb8ea09b3)。

<a id="r_aa349cf8c8bdc46a4df88a17963b7c0d3"></a>

```c
#define P_SSI_S_MISO_F_PWM RTS_FP_PINMUX(SSI_S_MISO, FUNC1)
```

相关声明：[P_SSI_S_MISO_F_PWM](#aa349cf8c8bdc46a4df88a17963b7c0d3)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC1](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a3f9b8eb1b4789fef1da73f4eb041ddfc)。

<a id="r_aa5581988a5d84c779af1e9ce47c53a05"></a>

```c
#define P_SSI_S_MISO_F_SSI_S_MISO RTS_FP_PINMUX(SSI_S_MISO, FUNC2)
```

相关声明：[P_SSI_S_MISO_F_SSI_S_MISO](#aa5581988a5d84c779af1e9ce47c53a05)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC2](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a0e8023a25dd46655b8eda5b0476ba169)。

<a id="r_a6169c33982837b7d5890cd0ede361717"></a>

```c
#define P_SSI_S_MISO_F_UART1_RX RTS_FP_PINMUX(SSI_S_MISO, FUNC3)
```

相关声明：[P_SSI_S_MISO_F_UART1_RX](#a6169c33982837b7d5890cd0ede361717)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC3](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#adeea02cdf0e8b64c27b6fad4d2b3b2b5)。

<a id="r_a7185e30c7b57434d2730d7c4b4c095e2"></a>

```c
#define P_SSI_S_MISO_F_JTAG_TDI RTS_FP_PINMUX(SSI_S_MISO, FUNC4)
```

相关声明：[P_SSI_S_MISO_F_JTAG_TDI](#a7185e30c7b57434d2730d7c4b4c095e2)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC4](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a769e96bef0ce818be7aa2cb0a0a67753)。

<a id="r_ac76aa51cd1c264bd35ad8eaefa0f4152"></a>

```c
#define P_SSI_S_MOSI_F_GPIO RTS_FP_PINMUX(SSI_S_MOSI, FUNC0)
```

相关声明：[P_SSI_S_MOSI_F_GPIO](#ac76aa51cd1c264bd35ad8eaefa0f4152)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC0](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#aa3ba064ba85ae0da9c55e7cdb8ea09b3)。

<a id="r_a4fd2db61a823de36465d656a7b2ad16c"></a>

```c
#define P_SSI_S_MOSI_F_PWM RTS_FP_PINMUX(SSI_S_MOSI, FUNC1)
```

相关声明：[P_SSI_S_MOSI_F_PWM](#a4fd2db61a823de36465d656a7b2ad16c)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC1](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a3f9b8eb1b4789fef1da73f4eb041ddfc)。

<a id="r_a36b7e921b0f7d45d955f49636c7ae744"></a>

```c
#define P_SSI_S_MOSI_F_SSI_S_MOSI RTS_FP_PINMUX(SSI_S_MOSI, FUNC2)
```

相关声明：[P_SSI_S_MOSI_F_SSI_S_MOSI](#a36b7e921b0f7d45d955f49636c7ae744)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC2](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a0e8023a25dd46655b8eda5b0476ba169)。

<a id="r_a13a6d30507cab03e10e1ba439ba68cfd"></a>

```c
#define P_SSI_S_MOSI_F_UART1_TX RTS_FP_PINMUX(SSI_S_MOSI, FUNC3)
```

相关声明：[P_SSI_S_MOSI_F_UART1_TX](#a13a6d30507cab03e10e1ba439ba68cfd)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC3](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#adeea02cdf0e8b64c27b6fad4d2b3b2b5)。

<a id="r_a4a49ae67ccde030c1269ec1123590cf7"></a>

```c
#define P_SSI_S_MOSI_F_JTAG_TRST RTS_FP_PINMUX(SSI_S_MOSI, FUNC4)
```

相关声明：[P_SSI_S_MOSI_F_JTAG_TRST](#a4a49ae67ccde030c1269ec1123590cf7)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC4](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a769e96bef0ce818be7aa2cb0a0a67753)。

<a id="r_ada3dd817c2e6f26dfcc7e9422bf42a72"></a>

```c
#define P_SSI_S_CS_F_GPIO RTS_FP_PINMUX(SSI_S_CS, FUNC0)
```

相关声明：[P_SSI_S_CS_F_GPIO](#ada3dd817c2e6f26dfcc7e9422bf42a72)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC0](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#aa3ba064ba85ae0da9c55e7cdb8ea09b3)。

<a id="r_aabff8435f8d81d4ee92bfc37833434d8"></a>

```c
#define P_SSI_S_CS_F_PWM RTS_FP_PINMUX(SSI_S_CS, FUNC1)
```

相关声明：[P_SSI_S_CS_F_PWM](#aabff8435f8d81d4ee92bfc37833434d8)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC1](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a3f9b8eb1b4789fef1da73f4eb041ddfc)。

<a id="r_a7209d0d1913807b5e222dd7bf5f12985"></a>

```c
#define P_SSI_S_CS_F_SSI_S_CS RTS_FP_PINMUX(SSI_S_CS, FUNC2)
```

相关声明：[P_SSI_S_CS_F_SSI_S_CS](#a7209d0d1913807b5e222dd7bf5f12985)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC2](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a0e8023a25dd46655b8eda5b0476ba169)。

<a id="r_a3b6ef57f5f78e4d61cb3295f9304688e"></a>

```c
#define P_SSI_S_CS_F_UART1_RTS RTS_FP_PINMUX(SSI_S_CS, FUNC3)
```

相关声明：[P_SSI_S_CS_F_UART1_RTS](#a3b6ef57f5f78e4d61cb3295f9304688e)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC3](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#adeea02cdf0e8b64c27b6fad4d2b3b2b5)。

<a id="r_ad401a54a361406fc58b03776f3a3c1d8"></a>

```c
#define P_SSI_S_CS_F_JTAG_TDO RTS_FP_PINMUX(SSI_S_CS, FUNC4)
```

相关声明：[P_SSI_S_CS_F_JTAG_TDO](#ad401a54a361406fc58b03776f3a3c1d8)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC4](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a769e96bef0ce818be7aa2cb0a0a67753)。

<a id="r_aaa48da5bbc9c147ad1ea190d75d16dd4"></a>

```c
#define P_SSI_S_SCK_F_GPIO RTS_FP_PINMUX(SSI_S_SCK, FUNC0)
```

相关声明：[P_SSI_S_SCK_F_GPIO](#aaa48da5bbc9c147ad1ea190d75d16dd4)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC0](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#aa3ba064ba85ae0da9c55e7cdb8ea09b3)。

<a id="r_a6dc8d96f02dcdd7c1f79102a24672ec4"></a>

```c
#define P_SSI_S_SCK_F_PWM RTS_FP_PINMUX(SSI_S_SCK, FUNC1)
```

相关声明：[P_SSI_S_SCK_F_PWM](#a6dc8d96f02dcdd7c1f79102a24672ec4)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC1](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a3f9b8eb1b4789fef1da73f4eb041ddfc)。

<a id="r_a75cf8a0c3ff31fc7d71a2f3532dc6540"></a>

```c
#define P_SSI_S_SCK_F_SSI_S_CLK RTS_FP_PINMUX(SSI_S_SCK, FUNC2)
```

相关声明：[P_SSI_S_SCK_F_SSI_S_CLK](#a75cf8a0c3ff31fc7d71a2f3532dc6540)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC2](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a0e8023a25dd46655b8eda5b0476ba169)。

<a id="r_a546660a1370c7fc8ead8b87bee1bb914"></a>

```c
#define P_SSI_S_SCK_F_UART1_CTS RTS_FP_PINMUX(SSI_S_SCK, FUNC3)
```

相关声明：[P_SSI_S_SCK_F_UART1_CTS](#a546660a1370c7fc8ead8b87bee1bb914)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC3](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#adeea02cdf0e8b64c27b6fad4d2b3b2b5)。

<a id="r_af027eee52f05e8e5fe9bedcca40e9e61"></a>

```c
#define P_GPIO14_F_GPIO RTS_FP_PINMUX(GPIO14, FUNC0)
```

相关声明：[P_GPIO14_F_GPIO](#af027eee52f05e8e5fe9bedcca40e9e61)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC0](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#aa3ba064ba85ae0da9c55e7cdb8ea09b3)。

<a id="r_ae051a3e37c4f9221ee582830b6a80227"></a>

```c
#define P_GPIO14_F_PWM RTS_FP_PINMUX(GPIO14, FUNC1)
```

相关声明：[P_GPIO14_F_PWM](#ae051a3e37c4f9221ee582830b6a80227)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC1](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a3f9b8eb1b4789fef1da73f4eb041ddfc)。

<a id="r_a51c1cd05aa234df667a7c14a597e1f95"></a>

```c
#define P_GPIO14_F_UART0_RX RTS_FP_PINMUX(GPIO14, FUNC2)
```

相关声明：[P_GPIO14_F_UART0_RX](#a51c1cd05aa234df667a7c14a597e1f95)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC2](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a0e8023a25dd46655b8eda5b0476ba169)。

<a id="r_a7146167cbb87493d5d02441f57da7230"></a>

```c
#define P_GPIO15_F_GPIO RTS_FP_PINMUX(GPIO15, FUNC0)
```

相关声明：[P_GPIO15_F_GPIO](#a7146167cbb87493d5d02441f57da7230)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC0](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#aa3ba064ba85ae0da9c55e7cdb8ea09b3)。

<a id="r_ad27d2523cacbdc691954266441c8602b"></a>

```c
#define P_GPIO15_F_PWM RTS_FP_PINMUX(GPIO15, FUNC1)
```

相关声明：[P_GPIO15_F_PWM](#ad27d2523cacbdc691954266441c8602b)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC1](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a3f9b8eb1b4789fef1da73f4eb041ddfc)。

<a id="r_a29f7714b5ac4a23932d4578e6f9b5f66"></a>

```c
#define P_GPIO15_F_UART0_TX RTS_FP_PINMUX(GPIO15, FUNC2)
```

相关声明：[P_GPIO15_F_UART0_TX](#a29f7714b5ac4a23932d4578e6f9b5f66)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC2](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a0e8023a25dd46655b8eda5b0476ba169)。

<a id="r_ab0e137deae6b997124cc7ec22ebdbbb8"></a>

```c
#define P_AL0_F_GPIO RTS_FP_PINMUX(AL0, FUNC0)
```

相关声明：[P_AL0_F_GPIO](#ab0e137deae6b997124cc7ec22ebdbbb8)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC0](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#aa3ba064ba85ae0da9c55e7cdb8ea09b3)。

<a id="r_ad7d1e7ba132eec31273140101900fa7c"></a>

```c
#define P_AL0_F_PWM RTS_FP_PINMUX(AL0, FUNC1)
```

相关声明：[P_AL0_F_PWM](#ad7d1e7ba132eec31273140101900fa7c)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC1](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a3f9b8eb1b4789fef1da73f4eb041ddfc)。

<a id="r_a3a6636329e5befc21cb2404fca5595c9"></a>

```c
#define P_AL0_F_CS_BRIDGE RTS_FP_PINMUX(AL0, FUNC2)
```

相关声明：[P_AL0_F_CS_BRIDGE](#a3a6636329e5befc21cb2404fca5595c9)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC2](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a0e8023a25dd46655b8eda5b0476ba169)。

<a id="r_a7268786a37ca473d4a6920b2827eaee2"></a>

```c
#define P_AL1_F_GPIO RTS_FP_PINMUX(AL1, FUNC0)
```

相关声明：[P_AL1_F_GPIO](#a7268786a37ca473d4a6920b2827eaee2)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC0](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#aa3ba064ba85ae0da9c55e7cdb8ea09b3)。

<a id="r_a987c4c7374bec922a9fe9aa41c1fa002"></a>

```c
#define P_AL1_F_PWM RTS_FP_PINMUX(AL1, FUNC1)
```

相关声明：[P_AL1_F_PWM](#a987c4c7374bec922a9fe9aa41c1fa002)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC1](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a3f9b8eb1b4789fef1da73f4eb041ddfc)。

<a id="r_a57e518d74fc19d7a5515400a85166476"></a>

```c
#define P_AL2_F_GPIO RTS_FP_PINMUX(AL2, FUNC0)
```

相关声明：[P_AL2_F_GPIO](#a57e518d74fc19d7a5515400a85166476)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC0](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#aa3ba064ba85ae0da9c55e7cdb8ea09b3)。

<a id="r_a33d7e6b888f20c07a18ac7935bff7733"></a>

```c
#define P_AL2_F_PWM RTS_FP_PINMUX(AL2, FUNC1)
```

相关声明：[P_AL2_F_PWM](#a33d7e6b888f20c07a18ac7935bff7733)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC1](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a3f9b8eb1b4789fef1da73f4eb041ddfc)。

<a id="r_adaac95e264f8e1731088778ebd2785c9"></a>

```c
#define P_SNR_RST_F_SNR_RST RTS_FP_PINMUX(SNR_RST, FUNC0)
```

相关声明：[P_SNR_RST_F_SNR_RST](#adaac95e264f8e1731088778ebd2785c9)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC0](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#aa3ba064ba85ae0da9c55e7cdb8ea09b3)。

<a id="r_a628b65e1199daa544ff01a9fc3637772"></a>

```c
#define P_SNR_CS_F_SNR_CS RTS_FP_PINMUX(SNR_CS, FUNC0)
```

相关声明：[P_SNR_CS_F_SNR_CS](#a628b65e1199daa544ff01a9fc3637772)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC0](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#aa3ba064ba85ae0da9c55e7cdb8ea09b3)。

<a id="r_a3dee402796f46cc8ae145b2045348a63"></a>

```c
#define P_SNR_CS_F_GPIO RTS_FP_PINMUX(SNR_CS, FUNC1)
```

相关声明：[P_SNR_CS_F_GPIO](#a3dee402796f46cc8ae145b2045348a63)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC1](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a3f9b8eb1b4789fef1da73f4eb041ddfc)。

<a id="r_a2bd8acf6a66c4292387b9f501b1a182c"></a>

```c
#define P_SNR_GPIO_F_GPIO RTS_FP_PINMUX(SNR_GPIO, FUNC0)
```

相关声明：[P_SNR_GPIO_F_GPIO](#a2bd8acf6a66c4292387b9f501b1a182c)、[RTS_FP_PINMUX](#a060a29a5272edf0e2ace85166ef11e02)、[FUNC0](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#aa3ba064ba85ae0da9c55e7cdb8ea09b3)。

## 58.2\_详细说明（Detailed Documentation）

<a id="a3f88bee83fa4766ff2051db077ea6cf4"></a>

### `IO_POWER_1V8`

```c
#define IO_POWER_1V8 0
```

<a id="a8d8bfbd5ed75971ac5aff402386c66ff"></a>

### `IO_POWER_3V3`

```c
#define IO_POWER_3V3 1
```

<a id="a3a6636329e5befc21cb2404fca5595c9"></a>

### `P_AL0_F_CS_BRIDGE`

```c
#define P_AL0_F_CS_BRIDGE RTS_FP_PINMUX(AL0, FUNC2)
```

<a id="ab0e137deae6b997124cc7ec22ebdbbb8"></a>

### `P_AL0_F_GPIO`

```c
#define P_AL0_F_GPIO RTS_FP_PINMUX(AL0, FUNC0)
```

<a id="ad7d1e7ba132eec31273140101900fa7c"></a>

### `P_AL0_F_PWM`

```c
#define P_AL0_F_PWM RTS_FP_PINMUX(AL0, FUNC1)
```

<a id="a7268786a37ca473d4a6920b2827eaee2"></a>

### `P_AL1_F_GPIO`

```c
#define P_AL1_F_GPIO RTS_FP_PINMUX(AL1, FUNC0)
```

<a id="a987c4c7374bec922a9fe9aa41c1fa002"></a>

### `P_AL1_F_PWM`

```c
#define P_AL1_F_PWM RTS_FP_PINMUX(AL1, FUNC1)
```

<a id="a57e518d74fc19d7a5515400a85166476"></a>

### `P_AL2_F_GPIO`

```c
#define P_AL2_F_GPIO RTS_FP_PINMUX(AL2, FUNC0)
```

<a id="a33d7e6b888f20c07a18ac7935bff7733"></a>

### `P_AL2_F_PWM`

```c
#define P_AL2_F_PWM RTS_FP_PINMUX(AL2, FUNC1)
```

<a id="a4a47f85eebe15efad333c93cea938002"></a>

### `P_CACHE_CS2_F_CACHE_CS2`

```c
#define P_CACHE_CS2_F_CACHE_CS2 RTS_FP_PINMUX(CACHE_CS2, FUNC0)
```

<a id="a7eb42e20cd04a06edba01c6acbe19ab8"></a>

### `P_CACHE_CS2_F_GPIO`

```c
#define P_CACHE_CS2_F_GPIO RTS_FP_PINMUX(CACHE_CS2, FUNC1)
```

<a id="af027eee52f05e8e5fe9bedcca40e9e61"></a>

### `P_GPIO14_F_GPIO`

```c
#define P_GPIO14_F_GPIO RTS_FP_PINMUX(GPIO14, FUNC0)
```

<a id="ae051a3e37c4f9221ee582830b6a80227"></a>

### `P_GPIO14_F_PWM`

```c
#define P_GPIO14_F_PWM RTS_FP_PINMUX(GPIO14, FUNC1)
```

<a id="a51c1cd05aa234df667a7c14a597e1f95"></a>

### `P_GPIO14_F_UART0_RX`

```c
#define P_GPIO14_F_UART0_RX RTS_FP_PINMUX(GPIO14, FUNC2)
```

<a id="a7146167cbb87493d5d02441f57da7230"></a>

### `P_GPIO15_F_GPIO`

```c
#define P_GPIO15_F_GPIO RTS_FP_PINMUX(GPIO15, FUNC0)
```

<a id="ad27d2523cacbdc691954266441c8602b"></a>

### `P_GPIO15_F_PWM`

```c
#define P_GPIO15_F_PWM RTS_FP_PINMUX(GPIO15, FUNC1)
```

<a id="a29f7714b5ac4a23932d4578e6f9b5f66"></a>

### `P_GPIO15_F_UART0_TX`

```c
#define P_GPIO15_F_UART0_TX RTS_FP_PINMUX(GPIO15, FUNC2)
```

<a id="a11be314cdaeaad0a19e63fd90f31b535"></a>

### `P_SCL0_F_ASIC_DBG`

```c
#define P_SCL0_F_ASIC_DBG RTS_FP_PINMUX(SCL0, FUNC5)
```

<a id="a93c9fb1eaf95898cef5e6eea63443575"></a>

### `P_SCL0_F_GPIO`

```c
#define P_SCL0_F_GPIO RTS_FP_PINMUX(SCL0, FUNC0)
```

<a id="a1150a31f7f74337c32a72c3686fb4276"></a>

### `P_SCL0_F_I2C0_SCL`

```c
#define P_SCL0_F_I2C0_SCL RTS_FP_PINMUX(SCL0, FUNC2)
```

<a id="a2b13a1131d870210c1444b6bdc314723"></a>

### `P_SCL0_F_PWM`

```c
#define P_SCL0_F_PWM RTS_FP_PINMUX(SCL0, FUNC1)
```

<a id="a83b71fc16500ad9496e808929d61afd6"></a>

### `P_SCL0_F_SWD_CLK`

```c
#define P_SCL0_F_SWD_CLK RTS_FP_PINMUX(SCL0, FUNC4)
```

<a id="aa0dcb4dc8ab00ed5fa6f1b9f0f40abd2"></a>

### `P_SCL0_F_UART0_RX`

```c
#define P_SCL0_F_UART0_RX RTS_FP_PINMUX(SCL0, FUNC3)
```

<a id="ae613d7ae922cdda329e394247acfcedf"></a>

### `P_SCL1_F_GPIO`

```c
#define P_SCL1_F_GPIO RTS_FP_PINMUX(SCL1, FUNC0)
```

<a id="aa7264cbb291a6b0f6b6f74052a6a7c02"></a>

### `P_SCL1_F_I2C1_SCL`

```c
#define P_SCL1_F_I2C1_SCL RTS_FP_PINMUX(SCL1, FUNC2)
```

<a id="a506f4b9df4725e1a39e9945bb82ffbbf"></a>

### `P_SCL1_F_JTAG_TCK`

```c
#define P_SCL1_F_JTAG_TCK RTS_FP_PINMUX(SCL1, FUNC4)
```

<a id="a6c812b17fafe4a766bb0ade88f9d4f07"></a>

### `P_SCL1_F_PWM`

```c
#define P_SCL1_F_PWM RTS_FP_PINMUX(SCL1, FUNC1)
```

<a id="a281bb69027ca60f1a429a4053fd5ad46"></a>

### `P_SCL2_F_ASIC_DBG`

```c
#define P_SCL2_F_ASIC_DBG RTS_FP_PINMUX(SCL2, FUNC5)
```

<a id="a4db1ceeef550d16b57ba72da2ab41a84"></a>

### `P_SCL2_F_GPIO`

```c
#define P_SCL2_F_GPIO RTS_FP_PINMUX(SCL2, FUNC0)
```

<a id="ae75b90a3e6a35554b5ae701f3119c9d7"></a>

### `P_SCL2_F_I2C2_SCL`

```c
#define P_SCL2_F_I2C2_SCL RTS_FP_PINMUX(SCL2, FUNC2)
```

<a id="a4b3322fcabc5b65b002c1ee689df6406"></a>

### `P_SCL2_F_PWM`

```c
#define P_SCL2_F_PWM RTS_FP_PINMUX(SCL2, FUNC1)
```

<a id="af96067068920171ec2ab22a87a1c936c"></a>

### `P_SCL2_F_SWD_CLK`

```c
#define P_SCL2_F_SWD_CLK RTS_FP_PINMUX(SCL2, FUNC4)
```

<a id="a872027642e6de4b8f8e9a5512aadd987"></a>

### `P_SCL2_F_UART0_RX`

```c
#define P_SCL2_F_UART0_RX RTS_FP_PINMUX(SCL2, FUNC3)
```

<a id="a2b31a4f06153e67068c00c394f6bb9e8"></a>

### `P_SDA0_F_ASIC_DBG`

```c
#define P_SDA0_F_ASIC_DBG RTS_FP_PINMUX(SDA0, FUNC5)
```

<a id="ad1f8b3436416a1ad6e86064501b74383"></a>

### `P_SDA0_F_GPIO`

```c
#define P_SDA0_F_GPIO RTS_FP_PINMUX(SDA0, FUNC0)
```

<a id="a38ea3d58ce7c2c62fb152c49a6af1608"></a>

### `P_SDA0_F_I2C0_SDA`

```c
#define P_SDA0_F_I2C0_SDA RTS_FP_PINMUX(SDA0, FUNC2)
```

<a id="a12ab555c5c3c87aa1dc94d347464d37c"></a>

### `P_SDA0_F_PWM`

```c
#define P_SDA0_F_PWM RTS_FP_PINMUX(SDA0, FUNC1)
```

<a id="aea565a7fa29340c602c53ffa37bd1b28"></a>

### `P_SDA0_F_SWD_DAT`

```c
#define P_SDA0_F_SWD_DAT RTS_FP_PINMUX(SDA0, FUNC4)
```

<a id="a763fb20b5c481b93e632de8c462f2ae1"></a>

### `P_SDA0_F_UART0_TX`

```c
#define P_SDA0_F_UART0_TX RTS_FP_PINMUX(SDA0, FUNC3)
```

<a id="a3de25c1c2e567fce3f0b6478aa97ff68"></a>

### `P_SDA1_F_GPIO`

```c
#define P_SDA1_F_GPIO RTS_FP_PINMUX(SDA1, FUNC0)
```

<a id="a504506040440518430691da469e31e3a"></a>

### `P_SDA1_F_I2C1_SDA`

```c
#define P_SDA1_F_I2C1_SDA RTS_FP_PINMUX(SDA1, FUNC2)
```

<a id="a68abee9633dea12c63bb27fc511b4594"></a>

### `P_SDA1_F_JTAG_TMS`

```c
#define P_SDA1_F_JTAG_TMS RTS_FP_PINMUX(SDA1, FUNC4)
```

<a id="abc0cf4a117b468ac20c8d27f04c14d0b"></a>

### `P_SDA1_F_PWM`

```c
#define P_SDA1_F_PWM RTS_FP_PINMUX(SDA1, FUNC1)
```

<a id="a7b421307c769dd48518866f2277da78d"></a>

### `P_SDA2_F_ASIC_DBG`

```c
#define P_SDA2_F_ASIC_DBG RTS_FP_PINMUX(SDA2, FUNC5)
```

<a id="ada97ecb5a1d5a96d284ab3a8504fe5a0"></a>

### `P_SDA2_F_GPIO`

```c
#define P_SDA2_F_GPIO RTS_FP_PINMUX(SDA2, FUNC0)
```

<a id="a19cbf93bdf3c372ea6c0f90170c5f79a"></a>

### `P_SDA2_F_I2C2_SDA`

```c
#define P_SDA2_F_I2C2_SDA RTS_FP_PINMUX(SDA2, FUNC2)
```

<a id="af9da47bd61d0407339bd91322e32b7ed"></a>

### `P_SDA2_F_PWM`

```c
#define P_SDA2_F_PWM RTS_FP_PINMUX(SDA2, FUNC1)
```

<a id="a5fc2cf735abde2b818f4fe7be6a63136"></a>

### `P_SDA2_F_SWD_DAT`

```c
#define P_SDA2_F_SWD_DAT RTS_FP_PINMUX(SDA2, FUNC4)
```

<a id="ac3c53cf3f39b8b853ad9c347eb3af01e"></a>

### `P_SDA2_F_UART0_TX`

```c
#define P_SDA2_F_UART0_TX RTS_FP_PINMUX(SDA2, FUNC3)
```

<a id="a5893a9757ab75b5f1f584e05e6fb9987"></a>

### `P_SNR_CLK_F_SNR_CLK`

```c
#define P_SNR_CLK_F_SNR_CLK RTS_FP_PINMUX(SNR_CLK, FUNC0)
```

<a id="a3dee402796f46cc8ae145b2045348a63"></a>

### `P_SNR_CS_F_GPIO`

```c
#define P_SNR_CS_F_GPIO RTS_FP_PINMUX(SNR_CS, FUNC1)
```

<a id="a628b65e1199daa544ff01a9fc3637772"></a>

### `P_SNR_CS_F_SNR_CS`

```c
#define P_SNR_CS_F_SNR_CS RTS_FP_PINMUX(SNR_CS, FUNC0)
```

<a id="a2bd8acf6a66c4292387b9f501b1a182c"></a>

### `P_SNR_GPIO_F_GPIO`

```c
#define P_SNR_GPIO_F_GPIO RTS_FP_PINMUX(SNR_GPIO, FUNC0)
```

<a id="a914dd84fdf371645f287b5d1a8c9ba37"></a>

### `P_SNR_MISO_F_SNR_MISO`

```c
#define P_SNR_MISO_F_SNR_MISO RTS_FP_PINMUX(SNR_MISO, FUNC0)
```

<a id="a779b627f86b1a99c58bf49d26743975e"></a>

### `P_SNR_MOSI_F_SNR_MOSI`

```c
#define P_SNR_MOSI_F_SNR_MOSI RTS_FP_PINMUX(SNR_MOSI, FUNC0)
```

<a id="adaac95e264f8e1731088778ebd2785c9"></a>

### `P_SNR_RST_F_SNR_RST`

```c
#define P_SNR_RST_F_SNR_RST RTS_FP_PINMUX(SNR_RST, FUNC0)
```

<a id="ab65122ace4f82cc49f316c4ba934460c"></a>

### `P_SSI_M_CS_F_ASIC_DBG`

```c
#define P_SSI_M_CS_F_ASIC_DBG RTS_FP_PINMUX(SSI_M_CS, FUNC5)
```

<a id="a1b8df3dc04c88e49c732058aa79b7ca8"></a>

### `P_SSI_M_CS_F_GPIO`

```c
#define P_SSI_M_CS_F_GPIO RTS_FP_PINMUX(SSI_M_CS, FUNC0)
```

<a id="abe22111b99c9ed5063d882f77c0370ed"></a>

### `P_SSI_M_CS_F_PWM`

```c
#define P_SSI_M_CS_F_PWM RTS_FP_PINMUX(SSI_M_CS, FUNC1)
```

<a id="a3bd6788c2f836f3f2a905405b89b9514"></a>

### `P_SSI_M_CS_F_SSI_M_CS`

```c
#define P_SSI_M_CS_F_SSI_M_CS RTS_FP_PINMUX(SSI_M_CS, FUNC2)
```

<a id="ac2fb549fcec7dcb6ceb79ad0e9943715"></a>

### `P_SSI_M_CS_F_SSI_S_CS`

```c
#define P_SSI_M_CS_F_SSI_S_CS RTS_FP_PINMUX(SSI_M_CS, FUNC3)
```

<a id="a51e3b5f76120bf89a15a6d6c3aba216a"></a>

### `P_SSI_M_CS_F_UART1_RTS`

```c
#define P_SSI_M_CS_F_UART1_RTS RTS_FP_PINMUX(SSI_M_CS, FUNC4)
```

<a id="ae880b656172f0d138384ab32e19d1c3a"></a>

### `P_SSI_M_MISO_F_ASIC_DBG`

```c
#define P_SSI_M_MISO_F_ASIC_DBG RTS_FP_PINMUX(SSI_M_MISO, FUNC5)
```

<a id="a968286abd075ea533eb5123465bf7e3b"></a>

### `P_SSI_M_MISO_F_GPIO`

```c
#define P_SSI_M_MISO_F_GPIO RTS_FP_PINMUX(SSI_M_MISO, FUNC0)
```

<a id="a92872d21a8eba753b68e00be5bf01bec"></a>

### `P_SSI_M_MISO_F_PWM`

```c
#define P_SSI_M_MISO_F_PWM RTS_FP_PINMUX(SSI_M_MISO, FUNC1)
```

<a id="a2517cac1b8f241397a2b2fbf663202c6"></a>

### `P_SSI_M_MISO_F_SSI_M_MISO`

```c
#define P_SSI_M_MISO_F_SSI_M_MISO RTS_FP_PINMUX(SSI_M_MISO, FUNC2)
```

<a id="a7d1f9550df66688ebc7ff27745faf26e"></a>

### `P_SSI_M_MISO_F_SSI_S_MISO`

```c
#define P_SSI_M_MISO_F_SSI_S_MISO RTS_FP_PINMUX(SSI_M_MISO, FUNC3)
```

<a id="a42722a2eeff4605fb27ed2f52ae8f7a2"></a>

### `P_SSI_M_MISO_F_UART1_RX`

```c
#define P_SSI_M_MISO_F_UART1_RX RTS_FP_PINMUX(SSI_M_MISO, FUNC4)
```

<a id="a537c46eca39aa4680b9025461aeaef8f"></a>

### `P_SSI_M_MOSI_F_ASIC_DBG`

```c
#define P_SSI_M_MOSI_F_ASIC_DBG RTS_FP_PINMUX(SSI_M_MOSI, FUNC5)
```

<a id="ab6b546dc3736b9fa71ce5a5ebb0b704b"></a>

### `P_SSI_M_MOSI_F_GPIO`

```c
#define P_SSI_M_MOSI_F_GPIO RTS_FP_PINMUX(SSI_M_MOSI, FUNC0)
```

<a id="a89b0219e15bfda208c88db5cd141255e"></a>

### `P_SSI_M_MOSI_F_PWM`

```c
#define P_SSI_M_MOSI_F_PWM RTS_FP_PINMUX(SSI_M_MOSI, FUNC1)
```

<a id="a9ab848f2fa4474b22e427f2f5075fbc8"></a>

### `P_SSI_M_MOSI_F_SSI_M_MOSI`

```c
#define P_SSI_M_MOSI_F_SSI_M_MOSI RTS_FP_PINMUX(SSI_M_MOSI, FUNC2)
```

<a id="aaeffb9cfea32f6dd9c549267f5490ce3"></a>

### `P_SSI_M_MOSI_F_SSI_S_MOSI`

```c
#define P_SSI_M_MOSI_F_SSI_S_MOSI RTS_FP_PINMUX(SSI_M_MOSI, FUNC3)
```

<a id="ada4225e71fba9d763e0f5cf75dfad2d8"></a>

### `P_SSI_M_MOSI_F_UART1_TX`

```c
#define P_SSI_M_MOSI_F_UART1_TX RTS_FP_PINMUX(SSI_M_MOSI, FUNC4)
```

<a id="a8a484b24f884fa4fa9d1194e42e4fe86"></a>

### `P_SSI_M_SCK_F_ASIC_DBG`

```c
#define P_SSI_M_SCK_F_ASIC_DBG RTS_FP_PINMUX(SSI_M_SCK, FUNC5)
```

<a id="a6753107bb0c65ac4a225679fdd88a0ad"></a>

### `P_SSI_M_SCK_F_GPIO`

```c
#define P_SSI_M_SCK_F_GPIO RTS_FP_PINMUX(SSI_M_SCK, FUNC0)
```

<a id="a6f5f7429a5c3f63cce754fe14ff555a3"></a>

### `P_SSI_M_SCK_F_PWM`

```c
#define P_SSI_M_SCK_F_PWM RTS_FP_PINMUX(SSI_M_SCK, FUNC1)
```

<a id="a5d532948f33f7a6408a2e4399bec62c5"></a>

### `P_SSI_M_SCK_F_SSI_M_CLK`

```c
#define P_SSI_M_SCK_F_SSI_M_CLK RTS_FP_PINMUX(SSI_M_SCK, FUNC2)
```

<a id="a600061a60422801354dfe023947aef25"></a>

### `P_SSI_M_SCK_F_SSI_S_CLK`

```c
#define P_SSI_M_SCK_F_SSI_S_CLK RTS_FP_PINMUX(SSI_M_SCK, FUNC3)
```

<a id="a91d430908b44ac2875063711acdf0ec7"></a>

### `P_SSI_M_SCK_F_UART1_CTS`

```c
#define P_SSI_M_SCK_F_UART1_CTS RTS_FP_PINMUX(SSI_M_SCK, FUNC4)
```

<a id="ada3dd817c2e6f26dfcc7e9422bf42a72"></a>

### `P_SSI_S_CS_F_GPIO`

```c
#define P_SSI_S_CS_F_GPIO RTS_FP_PINMUX(SSI_S_CS, FUNC0)
```

<a id="ad401a54a361406fc58b03776f3a3c1d8"></a>

### `P_SSI_S_CS_F_JTAG_TDO`

```c
#define P_SSI_S_CS_F_JTAG_TDO RTS_FP_PINMUX(SSI_S_CS, FUNC4)
```

<a id="aabff8435f8d81d4ee92bfc37833434d8"></a>

### `P_SSI_S_CS_F_PWM`

```c
#define P_SSI_S_CS_F_PWM RTS_FP_PINMUX(SSI_S_CS, FUNC1)
```

<a id="a7209d0d1913807b5e222dd7bf5f12985"></a>

### `P_SSI_S_CS_F_SSI_S_CS`

```c
#define P_SSI_S_CS_F_SSI_S_CS RTS_FP_PINMUX(SSI_S_CS, FUNC2)
```

<a id="a3b6ef57f5f78e4d61cb3295f9304688e"></a>

### `P_SSI_S_CS_F_UART1_RTS`

```c
#define P_SSI_S_CS_F_UART1_RTS RTS_FP_PINMUX(SSI_S_CS, FUNC3)
```

<a id="aafb6a04bc4558f1d2b77a3d3b7009f3d"></a>

### `P_SSI_S_MISO_F_GPIO`

```c
#define P_SSI_S_MISO_F_GPIO RTS_FP_PINMUX(SSI_S_MISO, FUNC0)
```

<a id="a7185e30c7b57434d2730d7c4b4c095e2"></a>

### `P_SSI_S_MISO_F_JTAG_TDI`

```c
#define P_SSI_S_MISO_F_JTAG_TDI RTS_FP_PINMUX(SSI_S_MISO, FUNC4)
```

<a id="aa349cf8c8bdc46a4df88a17963b7c0d3"></a>

### `P_SSI_S_MISO_F_PWM`

```c
#define P_SSI_S_MISO_F_PWM RTS_FP_PINMUX(SSI_S_MISO, FUNC1)
```

<a id="aa5581988a5d84c779af1e9ce47c53a05"></a>

### `P_SSI_S_MISO_F_SSI_S_MISO`

```c
#define P_SSI_S_MISO_F_SSI_S_MISO RTS_FP_PINMUX(SSI_S_MISO, FUNC2)
```

<a id="a6169c33982837b7d5890cd0ede361717"></a>

### `P_SSI_S_MISO_F_UART1_RX`

```c
#define P_SSI_S_MISO_F_UART1_RX RTS_FP_PINMUX(SSI_S_MISO, FUNC3)
```

<a id="ac76aa51cd1c264bd35ad8eaefa0f4152"></a>

### `P_SSI_S_MOSI_F_GPIO`

```c
#define P_SSI_S_MOSI_F_GPIO RTS_FP_PINMUX(SSI_S_MOSI, FUNC0)
```

<a id="a4a49ae67ccde030c1269ec1123590cf7"></a>

### `P_SSI_S_MOSI_F_JTAG_TRST`

```c
#define P_SSI_S_MOSI_F_JTAG_TRST RTS_FP_PINMUX(SSI_S_MOSI, FUNC4)
```

<a id="a4fd2db61a823de36465d656a7b2ad16c"></a>

### `P_SSI_S_MOSI_F_PWM`

```c
#define P_SSI_S_MOSI_F_PWM RTS_FP_PINMUX(SSI_S_MOSI, FUNC1)
```

<a id="a36b7e921b0f7d45d955f49636c7ae744"></a>

### `P_SSI_S_MOSI_F_SSI_S_MOSI`

```c
#define P_SSI_S_MOSI_F_SSI_S_MOSI RTS_FP_PINMUX(SSI_S_MOSI, FUNC2)
```

<a id="a13a6d30507cab03e10e1ba439ba68cfd"></a>

### `P_SSI_S_MOSI_F_UART1_TX`

```c
#define P_SSI_S_MOSI_F_UART1_TX RTS_FP_PINMUX(SSI_S_MOSI, FUNC3)
```

<a id="aaa48da5bbc9c147ad1ea190d75d16dd4"></a>

### `P_SSI_S_SCK_F_GPIO`

```c
#define P_SSI_S_SCK_F_GPIO RTS_FP_PINMUX(SSI_S_SCK, FUNC0)
```

<a id="a6dc8d96f02dcdd7c1f79102a24672ec4"></a>

### `P_SSI_S_SCK_F_PWM`

```c
#define P_SSI_S_SCK_F_PWM RTS_FP_PINMUX(SSI_S_SCK, FUNC1)
```

<a id="a75cf8a0c3ff31fc7d71a2f3532dc6540"></a>

### `P_SSI_S_SCK_F_SSI_S_CLK`

```c
#define P_SSI_S_SCK_F_SSI_S_CLK RTS_FP_PINMUX(SSI_S_SCK, FUNC2)
```

<a id="a546660a1370c7fc8ead8b87bee1bb914"></a>

### `P_SSI_S_SCK_F_UART1_CTS`

```c
#define P_SSI_S_SCK_F_UART1_CTS RTS_FP_PINMUX(SSI_S_SCK, FUNC3)
```

<a id="a11be88b633bb336cea17e4aef3ba28b7"></a>

### `RTS_FP_FUNC_MASK`

```c
#define RTS_FP_FUNC_MASK 0x1FU
```

<a id="ad283968ce392871c140457e387567990"></a>

### `RTS_FP_FUNC_SHIFT`

```c
#define RTS_FP_FUNC_SHIFT 8U
```

<a id="afc0d14eb037e42b83a6432ffcb235cb5"></a>

### `RTS_FP_PIN_AL0`

```c
#define RTS_FP_PIN_AL0 26
```

<a id="a39612eeda5cd0c8c627a62da63af4385"></a>

### `RTS_FP_PIN_AL1`

```c
#define RTS_FP_PIN_AL1 27
```

<a id="a608daa00bb6a3fa59c7b92f4daf7fffc"></a>

### `RTS_FP_PIN_AL2`

```c
#define RTS_FP_PIN_AL2 28
```

<a id="a2b0318fe330590ca569bb9c7d97b1d9b"></a>

### `RTS_FP_PIN_CACHE_CS1`

```c
#define RTS_FP_PIN_CACHE_CS1 0
```

<a id="aff5cb40d8aa7f9871f51eeae3715583a"></a>

### `RTS_FP_PIN_CACHE_CS2`

```c
#define RTS_FP_PIN_CACHE_CS2 6
```

<a id="a9e1fb15c389442fdb5e6e36188392b30"></a>

### `RTS_FP_PIN_CACHE_HOLD`

```c
#define RTS_FP_PIN_CACHE_HOLD 5
```

<a id="aef95bc38c6da3249d13fe573f709c650"></a>

### `RTS_FP_PIN_CACHE_MISO`

```c
#define RTS_FP_PIN_CACHE_MISO 1
```

<a id="a2335415d2667631c695c26d6fe65bf7a"></a>

### `RTS_FP_PIN_CACHE_MOSI`

```c
#define RTS_FP_PIN_CACHE_MOSI 2
```

<a id="a5ec21db03582cb1c40014d50f39739ea"></a>

### `RTS_FP_PIN_CACHE_SCK`

```c
#define RTS_FP_PIN_CACHE_SCK 3
```

<a id="a6f58a20107979e2ae576f4f9c8806299"></a>

### `RTS_FP_PIN_CACHE_WP`

```c
#define RTS_FP_PIN_CACHE_WP 4
```

<a id="a389918abc357193b470dbe1a4be0e930"></a>

### `RTS_FP_PIN_FUNC0`

```c
#define RTS_FP_PIN_FUNC0 0
```

<a id="ac54191d52494ba993c22403ef3ef5a54"></a>

### `RTS_FP_PIN_FUNC1`

```c
#define RTS_FP_PIN_FUNC1 1
```

<a id="a1cab4441342ecb8f20fd51edaef4f0ed"></a>

### `RTS_FP_PIN_FUNC2`

```c
#define RTS_FP_PIN_FUNC2 2
```

<a id="ae802eb7552ed8f1654220895d34019f7"></a>

### `RTS_FP_PIN_FUNC3`

```c
#define RTS_FP_PIN_FUNC3 3
```

<a id="acfc7c39167fa068fb091289a1862f6af"></a>

### `RTS_FP_PIN_FUNC4`

```c
#define RTS_FP_PIN_FUNC4 4
```

<a id="a0471cb41a9ba24e43d06509935fed060"></a>

### `RTS_FP_PIN_FUNC5`

```c
#define RTS_FP_PIN_FUNC5 5
```

<a id="a3d60b76983b5a76fe63a264f6371941c"></a>

### `RTS_FP_PIN_FUNC6`

```c
#define RTS_FP_PIN_FUNC6 6
```

<a id="ac2bd93b428d003c7db4a2fdac6feec49"></a>

### `RTS_FP_PIN_FUNC7`

```c
#define RTS_FP_PIN_FUNC7 7
```

<a id="a63cdabfe86d0e1ecf52ee35fef0ae416"></a>

### `RTS_FP_PIN_GPIO14`

```c
#define RTS_FP_PIN_GPIO14 24
```

<a id="a31d8161b0bb58684e62c0f141fb4b154"></a>

### `RTS_FP_PIN_GPIO15`

```c
#define RTS_FP_PIN_GPIO15 25
```

<a id="a6df72421fd2cdd02f6ec00915032bd55"></a>

### `RTS_FP_PIN_MASK`

```c
#define RTS_FP_PIN_MASK 0xFFU
```

<a id="aa7cd95a7032cd1e78381fe7de8bab92c"></a>

### `RTS_FP_PIN_SCL0`

```c
#define RTS_FP_PIN_SCL0 14
```

<a id="ad45589e3484d938e683d77b42c1d7b36"></a>

### `RTS_FP_PIN_SCL1`

```c
#define RTS_FP_PIN_SCL1 18
```

<a id="af622afcdf9071172c1eab379e6138a3e"></a>

### `RTS_FP_PIN_SCL2`

```c
#define RTS_FP_PIN_SCL2 16
```

<a id="a2c6652775ced1755e87c8bf62078073c"></a>

### `RTS_FP_PIN_SDA0`

```c
#define RTS_FP_PIN_SDA0 15
```

<a id="aca4f6d25271a46ba6bf27ff788950249"></a>

### `RTS_FP_PIN_SDA1`

```c
#define RTS_FP_PIN_SDA1 19
```

<a id="a7ed6aaffa10de7aa8ce5ae4f5dbaf0f5"></a>

### `RTS_FP_PIN_SDA2`

```c
#define RTS_FP_PIN_SDA2 17
```

<a id="a0d86d3cc7149941efefca544d9d09687"></a>

### `RTS_FP_PIN_SHIFT`

```c
#define RTS_FP_PIN_SHIFT 0U
```

字段（Fields）：

- 引脚（Pin）：位 [7:0]。
- 功能（Func）：位 [10:8]。

<a id="a64d5158ec376452339d4201b5a02a317"></a>

### `RTS_FP_PIN_SNR_CLK`

```c
#define RTS_FP_PIN_SNR_CLK 9
```

<a id="a909360dbc52ba4280c63a8b78250b9e4"></a>

### `RTS_FP_PIN_SNR_CS`

```c
#define RTS_FP_PIN_SNR_CS 30
```

<a id="a84cc3e4898c14b364662bc7f59e32017"></a>

### `RTS_FP_PIN_SNR_GPIO`

```c
#define RTS_FP_PIN_SNR_GPIO 31
```

<a id="a6c731bd08a3916ab5a4805cf47498c81"></a>

### `RTS_FP_PIN_SNR_MISO`

```c
#define RTS_FP_PIN_SNR_MISO 7
```

<a id="a7776a699ad9f44b2e3804347d97781c9"></a>

### `RTS_FP_PIN_SNR_MOSI`

```c
#define RTS_FP_PIN_SNR_MOSI 8
```

<a id="a06c3a4d8fb8e37c72de299a84db39c3c"></a>

### `RTS_FP_PIN_SNR_RST`

```c
#define RTS_FP_PIN_SNR_RST 29
```

<a id="a96bb7de76d6998603362dec377eedbf1"></a>

### `RTS_FP_PIN_SSI_M_CS`

```c
#define RTS_FP_PIN_SSI_M_CS 12
```

<a id="aac420b01f8d7ac6e331d2c928246d856"></a>

### `RTS_FP_PIN_SSI_M_MISO`

```c
#define RTS_FP_PIN_SSI_M_MISO 10
```

<a id="a48a0f5b8da7f20eeb13eee4f891f340d"></a>

### `RTS_FP_PIN_SSI_M_MOSI`

```c
#define RTS_FP_PIN_SSI_M_MOSI 11
```

<a id="ab369f3cf67ec5ab599e3fc5b12c292e2"></a>

### `RTS_FP_PIN_SSI_M_SCK`

```c
#define RTS_FP_PIN_SSI_M_SCK 13
```

<a id="abd4ba76ad633336cb77b014de0a2ba27"></a>

### `RTS_FP_PIN_SSI_S_CS`

```c
#define RTS_FP_PIN_SSI_S_CS 22
```

<a id="a50e0ea545de7c8889ab802c3146f3a68"></a>

### `RTS_FP_PIN_SSI_S_MISO`

```c
#define RTS_FP_PIN_SSI_S_MISO 20
```

<a id="a15cd9ee6ce0eeb63fdd27a69df1e5dce"></a>

### `RTS_FP_PIN_SSI_S_MOSI`

```c
#define RTS_FP_PIN_SSI_S_MOSI 21
```

<a id="abeaea6bddcc2c78c8fb87899d747a404"></a>

### `RTS_FP_PIN_SSI_S_SCK`

```c
#define RTS_FP_PIN_SSI_S_SCK 23
```

<a id="a060a29a5272edf0e2ace85166ef11e02"></a>

### `RTS_FP_PINMUX`

```c
#define RTS_FP_PINMUX ( pin, func )
```

展开值（Value）：

```c
((((RTS_FP_PIN_##pin) & RTS_FP_PIN_MASK) << RTS_FP_PIN_SHIFT) |                            \
 (((RTS_FP_PIN_##func) & RTS_FP_FUNC_MASK) << RTS_FP_FUNC_SHIFT))
```

<a id="a0b34a17b7f64971b88e2a769f2aa1945"></a>

### `RTS_FP_PINMUX_FUNC`

```c
#define RTS_FP_PINMUX_FUNC ( __pin)
```

展开值（Value）：

```c
(((__pin) >> RTS_FP_FUNC_SHIFT) & RTS_FP_FUNC_MASK)
```

<a id="a00a4b2c0c53fae16f519272161662406"></a>

### `RTS_FP_PINMUX_PIN`

```c
#define RTS_FP_PINMUX_PIN ( __pin)
```

展开值（Value）：

```c
(((__pin) >> RTS_FP_PIN_SHIFT) & RTS_FP_PIN_MASK)
```


## 58.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P739_rts5817_pinctrl.h_源码浏览.md)
- [FUNC0](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#aa3ba064ba85ae0da9c55e7cdb8ea09b3)
- [FUNC1](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a3f9b8eb1b4789fef1da73f4eb041ddfc)
- [FUNC2](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a0e8023a25dd46655b8eda5b0476ba169)
- [FUNC3](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#adeea02cdf0e8b64c27b6fad4d2b3b2b5)
- [FUNC4](../api_file_reference/P346_zephyr__dt-bindings__pinctrl__realtek-rts5912-pinctrl.h_文件参考.md#a769e96bef0ce818be7aa2cb0a0a67753)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="arts5817__pinctrl_8h_html_a0d86d3cc7149941efefca544d9d09687"></a>
<a id="arts5817__pinctrl_8h_html_a11be88b633bb336cea17e4aef3ba28b7"></a>
<a id="arts5817__pinctrl_8h_html_a6df72421fd2cdd02f6ec00915032bd55"></a>
<a id="arts5817__pinctrl_8h_html_ad283968ce392871c140457e387567990"></a>

---

[上一章](P057_zephyr__bluetooth__mesh__rpr.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P059_zephyr__dt-bindings__pinctrl__smartbond-pinctrl.h_文件参考.md)
