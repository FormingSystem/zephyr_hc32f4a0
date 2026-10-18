---
id: learning.zephyr-docs.api-file-reference.page-11
title: zephyr__dt-bindings__pinctrl__amebad-pinctrl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/amebad-pinctrl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_amebad-pinctrl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/amebad-pinctrl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 11.1\_宏定义（Macros）

<a id="r_a1a770820da1c7f81c4925cd6a6fab8f4"></a>

```c
#define AMEBA_GPIO 0
```

相关声明：[AMEBA_GPIO](#a1a770820da1c7f81c4925cd6a6fab8f4)。

<a id="r_a741c7c7e636536003ed508abd2d47d97"></a>

```c
#define AMEBA_UART 1
```

相关声明：[AMEBA_UART](#a741c7c7e636536003ed508abd2d47d97)。

<a id="r_a884a5bb4ee3ce7f86a1cd3379049a1e6"></a>

```c
#define AMEBA_UART_RTSCTS 2
```

相关声明：[AMEBA_UART_RTSCTS](#a884a5bb4ee3ce7f86a1cd3379049a1e6)。

<a id="r_a4911982a8e2ed362b76c16ca05960c1f"></a>

```c
#define AMEBA_LOGUART 2
```

相关声明：[AMEBA_LOGUART](#a4911982a8e2ed362b76c16ca05960c1f)。

<a id="r_af65f9fd15193e9507f3d4b1c144dd6fd"></a>

```c
#define AMEBA_SPIM 3
```

相关声明：[AMEBA_SPIM](#af65f9fd15193e9507f3d4b1c144dd6fd)。

<a id="r_a6bcc2325f468726f4fdba85dce1466aa"></a>

```c
#define AMEBA_SPIS 3
```

相关声明：[AMEBA_SPIS](#a6bcc2325f468726f4fdba85dce1466aa)。

<a id="r_a4a27255dcf716433a4665f15cb761bbc"></a>

```c
#define AMEBA_RTC 4
```

相关声明：[AMEBA_RTC](#a4a27255dcf716433a4665f15cb761bbc)。

<a id="r_a3c67799b649719e52586d17b5480ae30"></a>

```c
#define AMEBA_TIMINPUT 4
```

相关声明：[AMEBA_TIMINPUT](#a3c67799b649719e52586d17b5480ae30)。

<a id="r_a611c2639b53263c349b974e3e0b0e8fa"></a>

```c
#define AMEBA_IR 5
```

相关声明：[AMEBA_IR](#a611c2639b53263c349b974e3e0b0e8fa)。

<a id="r_a14595f1773c6cc01f38187a8759f953a"></a>

```c
#define AMEBA_SPIF 6
```

相关声明：[AMEBA_SPIF](#a14595f1773c6cc01f38187a8759f953a)。

<a id="r_a58cef141783253146185ee3557aa02e6"></a>

```c
#define AMEBA_I2C 7
```

相关声明：[AMEBA_I2C](#a58cef141783253146185ee3557aa02e6)。

<a id="r_a9aca27e3812a56c390261fe13b94bc6f"></a>

```c
#define AMEBA_SDIOD 8
```

相关声明：[AMEBA_SDIOD](#a9aca27e3812a56c390261fe13b94bc6f)。

<a id="r_a252f2be2e6c07dee4ffa347119d76b19"></a>

```c
#define AMEBA_SDIOH 8
```

相关声明：[AMEBA_SDIOH](#a252f2be2e6c07dee4ffa347119d76b19)。

<a id="r_a44fcdb0dd2f6b74e88ff4a93a12a34a2"></a>

```c
#define AMEBA_PWM 9
```

相关声明：[AMEBA_PWM](#a44fcdb0dd2f6b74e88ff4a93a12a34a2)。

<a id="r_a6cb424d8b71ce8f76ebb826824a53757"></a>

```c
#define AMEBA_PWM_HS 9
```

相关声明：[AMEBA_PWM_HS](#a6cb424d8b71ce8f76ebb826824a53757)。

<a id="r_a75e163575ce615f408fe6966de18c04b"></a>

```c
#define AMEBA_PWM_LP 10
```

相关声明：[AMEBA_PWM_LP](#a75e163575ce615f408fe6966de18c04b)。

<a id="r_a0d8fdf8ef3539a8cfe2b6e57f8e5db8d"></a>

```c
#define AMEBA_SWD 11
```

相关声明：[AMEBA_SWD](#a0d8fdf8ef3539a8cfe2b6e57f8e5db8d)。

<a id="r_af5b7a1a28498efde7b9494865b82ecee"></a>

```c
#define AMEBA_I2S 12
```

相关声明：[AMEBA_I2S](#af5b7a1a28498efde7b9494865b82ecee)。

<a id="r_a416afde36071953cca572fc91942ce03"></a>

```c
#define AMEBA_DMIC 12
```

相关声明：[AMEBA_DMIC](#a416afde36071953cca572fc91942ce03)。

<a id="r_af2aaf9da6de1071630bca8f706860f4a"></a>

```c
#define AMEBA_LCD 13
```

相关声明：[AMEBA_LCD](#af2aaf9da6de1071630bca8f706860f4a)。

<a id="r_adfeeeb74cd0157b09992ec5e5f4e5397"></a>

```c
#define AMEBA_USB 14
```

相关声明：[AMEBA_USB](#adfeeeb74cd0157b09992ec5e5f4e5397)。

<a id="r_a661bf17015f1e3a56d638fbcdd3e9f98"></a>

```c
#define AMEBA_QDEC 15
```

相关声明：[AMEBA_QDEC](#a661bf17015f1e3a56d638fbcdd3e9f98)。

<a id="r_a98d1ee7519ef6bba75aecd47887a7ace"></a>

```c
#define AMEBA_SGPIO 16
```

相关声明：[AMEBA_SGPIO](#a98d1ee7519ef6bba75aecd47887a7ace)。

<a id="r_a5911b90db9c5d31a1bc08080a49e1735"></a>

```c
#define AMEBA_RFE 18
```

相关声明：[AMEBA_RFE](#a5911b90db9c5d31a1bc08080a49e1735)。

<a id="r_a864850d1e41b6ac7c606b7241e92ee69"></a>

```c
#define AMEBA_BTCOEX 19
```

相关声明：[AMEBA_BTCOEX](#a864850d1e41b6ac7c606b7241e92ee69)。

<a id="r_a078afa091f8ad7680c17b44381233c77"></a>

```c
#define AMEBA_WIFIFW 20
```

相关声明：[AMEBA_WIFIFW](#a078afa091f8ad7680c17b44381233c77)。

<a id="r_ad0291b1ef904ab00c7f261f50f8b911c"></a>

```c
#define AMEBA_EXT_PCM 20
```

相关声明：[AMEBA_EXT_PCM](#ad0291b1ef904ab00c7f261f50f8b911c)。

<a id="r_aba46fb715417b3528ed7ce89eed810c6"></a>

```c
#define AMEBA_EXT_BT 20
```

相关声明：[AMEBA_EXT_BT](#aba46fb715417b3528ed7ce89eed810c6)。

<a id="r_ac875928c66912c87926b355cb5a5d688"></a>

```c
#define AMEBA_BB_PIN 21
```

相关声明：[AMEBA_BB_PIN](#ac875928c66912c87926b355cb5a5d688)。

<a id="r_aafdc733867a4ab1a0d16429679b19cba"></a>

```c
#define AMEBA_SIC 22
```

相关声明：[AMEBA_SIC](#aafdc733867a4ab1a0d16429679b19cba)。

<a id="r_ae2228749d3f79ca7199f4103cf41b845"></a>

```c
#define AMEBA_TIMINPUT_HS 22
```

相关声明：[AMEBA_TIMINPUT_HS](#ae2228749d3f79ca7199f4103cf41b845)。

<a id="r_a3a31ed7b260ec197940788832b74ceb6"></a>

```c
#define AMEBA_DBGPORT 23
```

相关声明：[AMEBA_DBGPORT](#a3a31ed7b260ec197940788832b74ceb6)。

<a id="r_a20b459d6093716b42bb862b844ca8e03"></a>

```c
#define AMEBA_BBDBG 25
```

相关声明：[AMEBA_BBDBG](#a20b459d6093716b42bb862b844ca8e03)。

<a id="r_a841e471857543c0ec213047004c16696"></a>

```c
#define AMEBA_EXT32K 28
```

相关声明：[AMEBA_EXT32K](#a841e471857543c0ec213047004c16696)。

<a id="r_a2780d7daa171a1dd4ac8daf87d7df7a3"></a>

```c
#define AMEBA_RTCOUT 28
```

相关声明：[AMEBA_RTCOUT](#a2780d7daa171a1dd4ac8daf87d7df7a3)。

<a id="r_a91901ed7ce015c4b744d48f1b3867835"></a>

```c
#define AMEBA_KEYSCAN_ROW 29
```

相关声明：[AMEBA_KEYSCAN_ROW](#a91901ed7ce015c4b744d48f1b3867835)。

<a id="r_a868d4fbbc2420d6ba7d2f71b5ed78bed"></a>

```c
#define AMEBA_KEYSCAN_COL 30
```

相关声明：[AMEBA_KEYSCAN_COL](#a868d4fbbc2420d6ba7d2f71b5ed78bed)。

<a id="r_aa1b65d0ef00a458e4b900e2e5d72dbc7"></a>

```c
#define AMEBA_WAKEUP 31
```

相关声明：[AMEBA_WAKEUP](#aa1b65d0ef00a458e4b900e2e5d72dbc7)。

<a id="r_a01f0e522a7c41526681b766c7ac7ce1f"></a>

```c
#define AMEBA_PORT_PIN(port, line)
```

相关声明：[AMEBA_PORT_PIN](#a01f0e522a7c41526681b766c7ac7ce1f)。

<a id="r_a71d265adf87eb5aa7e991bf0dd6c142f"></a>

```c
#define AMEBA_PINMUX(port, line, funcid)
```

相关声明：[AMEBA_PINMUX](#a71d265adf87eb5aa7e991bf0dd6c142f)。

## 11.2\_详细说明（Detailed Documentation）

<a id="ac875928c66912c87926b355cb5a5d688"></a>

### `AMEBA_BB_PIN`

```c
#define AMEBA_BB_PIN 21
```

<a id="a20b459d6093716b42bb862b844ca8e03"></a>

### `AMEBA_BBDBG`

```c
#define AMEBA_BBDBG 25
```

<a id="a864850d1e41b6ac7c606b7241e92ee69"></a>

### `AMEBA_BTCOEX`

```c
#define AMEBA_BTCOEX 19
```

<a id="a3a31ed7b260ec197940788832b74ceb6"></a>

### `AMEBA_DBGPORT`

```c
#define AMEBA_DBGPORT 23
```

<a id="a416afde36071953cca572fc91942ce03"></a>

### `AMEBA_DMIC`

```c
#define AMEBA_DMIC 12
```

<a id="a841e471857543c0ec213047004c16696"></a>

### `AMEBA_EXT32K`

```c
#define AMEBA_EXT32K 28
```

<a id="aba46fb715417b3528ed7ce89eed810c6"></a>

### `AMEBA_EXT_BT`

```c
#define AMEBA_EXT_BT 20
```

<a id="ad0291b1ef904ab00c7f261f50f8b911c"></a>

### `AMEBA_EXT_PCM`

```c
#define AMEBA_EXT_PCM 20
```

<a id="a1a770820da1c7f81c4925cd6a6fab8f4"></a>

### `AMEBA_GPIO`

```c
#define AMEBA_GPIO 0
```

<a id="a58cef141783253146185ee3557aa02e6"></a>

### `AMEBA_I2C`

```c
#define AMEBA_I2C 7
```

<a id="af5b7a1a28498efde7b9494865b82ecee"></a>

### `AMEBA_I2S`

```c
#define AMEBA_I2S 12
```

<a id="a611c2639b53263c349b974e3e0b0e8fa"></a>

### `AMEBA_IR`

```c
#define AMEBA_IR 5
```

<a id="a868d4fbbc2420d6ba7d2f71b5ed78bed"></a>

### `AMEBA_KEYSCAN_COL`

```c
#define AMEBA_KEYSCAN_COL 30
```

<a id="a91901ed7ce015c4b744d48f1b3867835"></a>

### `AMEBA_KEYSCAN_ROW`

```c
#define AMEBA_KEYSCAN_ROW 29
```

<a id="af2aaf9da6de1071630bca8f706860f4a"></a>

### `AMEBA_LCD`

```c
#define AMEBA_LCD 13
```

<a id="a4911982a8e2ed362b76c16ca05960c1f"></a>

### `AMEBA_LOGUART`

```c
#define AMEBA_LOGUART 2
```

<a id="a71d265adf87eb5aa7e991bf0dd6c142f"></a>

### `AMEBA_PINMUX`

```c
#define AMEBA_PINMUX ( port, line, funcid )
```

展开值（Value）：

```c
(((AMEBA_PORT_PIN(port, line)) << 8) | (funcid))
```

<a id="a01f0e522a7c41526681b766c7ac7ce1f"></a>

### `AMEBA_PORT_PIN`

```c
#define AMEBA_PORT_PIN ( port, line )
```

展开值（Value）：

```c
((((port) - 'A') << 5) + (line))
```

<a id="a44fcdb0dd2f6b74e88ff4a93a12a34a2"></a>

### `AMEBA_PWM`

```c
#define AMEBA_PWM 9
```

<a id="a6cb424d8b71ce8f76ebb826824a53757"></a>

### `AMEBA_PWM_HS`

```c
#define AMEBA_PWM_HS 9
```

<a id="a75e163575ce615f408fe6966de18c04b"></a>

### `AMEBA_PWM_LP`

```c
#define AMEBA_PWM_LP 10
```

<a id="a661bf17015f1e3a56d638fbcdd3e9f98"></a>

### `AMEBA_QDEC`

```c
#define AMEBA_QDEC 15
```

<a id="a5911b90db9c5d31a1bc08080a49e1735"></a>

### `AMEBA_RFE`

```c
#define AMEBA_RFE 18
```

<a id="a4a27255dcf716433a4665f15cb761bbc"></a>

### `AMEBA_RTC`

```c
#define AMEBA_RTC 4
```

<a id="a2780d7daa171a1dd4ac8daf87d7df7a3"></a>

### `AMEBA_RTCOUT`

```c
#define AMEBA_RTCOUT 28
```

<a id="a9aca27e3812a56c390261fe13b94bc6f"></a>

### `AMEBA_SDIOD`

```c
#define AMEBA_SDIOD 8
```

<a id="a252f2be2e6c07dee4ffa347119d76b19"></a>

### `AMEBA_SDIOH`

```c
#define AMEBA_SDIOH 8
```

<a id="a98d1ee7519ef6bba75aecd47887a7ace"></a>

### `AMEBA_SGPIO`

```c
#define AMEBA_SGPIO 16
```

<a id="aafdc733867a4ab1a0d16429679b19cba"></a>

### `AMEBA_SIC`

```c
#define AMEBA_SIC 22
```

<a id="a14595f1773c6cc01f38187a8759f953a"></a>

### `AMEBA_SPIF`

```c
#define AMEBA_SPIF 6
```

<a id="af65f9fd15193e9507f3d4b1c144dd6fd"></a>

### `AMEBA_SPIM`

```c
#define AMEBA_SPIM 3
```

<a id="a6bcc2325f468726f4fdba85dce1466aa"></a>

### `AMEBA_SPIS`

```c
#define AMEBA_SPIS 3
```

<a id="a0d8fdf8ef3539a8cfe2b6e57f8e5db8d"></a>

### `AMEBA_SWD`

```c
#define AMEBA_SWD 11
```

<a id="a3c67799b649719e52586d17b5480ae30"></a>

### `AMEBA_TIMINPUT`

```c
#define AMEBA_TIMINPUT 4
```

<a id="ae2228749d3f79ca7199f4103cf41b845"></a>

### `AMEBA_TIMINPUT_HS`

```c
#define AMEBA_TIMINPUT_HS 22
```

<a id="a741c7c7e636536003ed508abd2d47d97"></a>

### `AMEBA_UART`

```c
#define AMEBA_UART 1
```

<a id="a884a5bb4ee3ce7f86a1cd3379049a1e6"></a>

### `AMEBA_UART_RTSCTS`

```c
#define AMEBA_UART_RTSCTS 2
```

<a id="adfeeeb74cd0157b09992ec5e5f4e5397"></a>

### `AMEBA_USB`

```c
#define AMEBA_USB 14
```

<a id="aa1b65d0ef00a458e4b900e2e5d72dbc7"></a>

### `AMEBA_WAKEUP`

```c
#define AMEBA_WAKEUP 31
```

<a id="a078afa091f8ad7680c17b44381233c77"></a>

### `AMEBA_WIFIFW`

```c
#define AMEBA_WIFIFW 20
```


## 11.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_configuration_reference/P003_amebad-pinctrl.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="aamebad-pinctrl_8h_html_a01f0e522a7c41526681b766c7ac7ce1f"></a>

---

[上一章](P010_zephyr__dt-bindings__pinctrl__ambiq-apollo5-pinctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P012_zephyr__dt-bindings__pinctrl__amebadplus-pinctrl.h_文件参考.md)
