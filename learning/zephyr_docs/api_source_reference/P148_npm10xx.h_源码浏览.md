---
id: learning.zephyr-docs.api-source-reference.page-148
title: npm10xx.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2charger_2npm10xx_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第148章\_npm10xx.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2charger_2npm10xx_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2charger_2npm10xx_8h.html)。

## 148.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00022"></a>
<a id="foldopen00024"></a>
<a id="l00024"></a>
<a id="l00027"></a>
<a id="l00030"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="foldopen00048"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="foldopen00070"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="foldopen00093"></a>
<a id="l00093"></a>
<a id="l00095"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00107"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="foldopen00116"></a>
<a id="l00116"></a>
<a id="l00118"></a>
<a id="l00120"></a>
<a id="l00122"></a>
<a id="l00124"></a>
<a id="l00126"></a>
<a id="l00128"></a>
<a id="l00130"></a>
<a id="l00132"></a>
<a id="l00134"></a>
<a id="l00136"></a>
<a id="l00138"></a>
<a id="l00140"></a>
<a id="l00142"></a>
<a id="l00144"></a>
<a id="l00146"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="acharger_8h_html"></a>
<a id="agroup__charger__interface__npm10xx_html_ga0361b1ebfc18e176ed171823a38e12ab"></a>
<a id="agroup__charger__interface__npm10xx_html_ga2de09557c2f7d19ad141ca8ba48e9f5d"></a>
<a id="agroup__charger__interface__npm10xx_html_ga2e2382e875599723272916c8eda7e693"></a>
<a id="agroup__charger__interface__npm10xx_html_ga51fc3e1a4aa657d030209b1e2f640b88"></a>
<a id="agroup__charger__interface__npm10xx_html_ga645f680cc19e3d6f0c777dfa41b3abae"></a>
<a id="agroup__charger__interface__npm10xx_html_gga0361b1ebfc18e176ed171823a38e12aba0959a4ef28fcfd44de6f4c852744e197"></a>
<a id="agroup__charger__interface__npm10xx_html_gga0361b1ebfc18e176ed171823a38e12aba25a044f38b048ff0451e556b42534b67"></a>
<a id="agroup__charger__interface__npm10xx_html_gga0361b1ebfc18e176ed171823a38e12aba44ed6f6aea9feee4577635fffc480dfb"></a>
<a id="agroup__charger__interface__npm10xx_html_gga0361b1ebfc18e176ed171823a38e12aba8ca1895fc6fe1a8660f2e2b2452c5f59"></a>
<a id="agroup__charger__interface__npm10xx_html_gga0361b1ebfc18e176ed171823a38e12aba911e517245594be44d2c4cc971cee1bd"></a>
<a id="agroup__charger__interface__npm10xx_html_gga0361b1ebfc18e176ed171823a38e12abab7aaa32e285208f86889cc7d7a0060c0"></a>
<a id="agroup__charger__interface__npm10xx_html_gga0361b1ebfc18e176ed171823a38e12abad6f6c26c8759613c05a10592ac628d15"></a>
<a id="agroup__charger__interface__npm10xx_html_gga0361b1ebfc18e176ed171823a38e12abae981727f782b8459d41757151b0cdcf7"></a>
<a id="agroup__charger__interface__npm10xx_html_gga0361b1ebfc18e176ed171823a38e12abafa68639f27c5366ad45db5c56f2268af"></a>
<a id="agroup__charger__interface__npm10xx_html_gga2de09557c2f7d19ad141ca8ba48e9f5da16efc7a009faff4fdecb0548cfee8e67"></a>
<a id="agroup__charger__interface__npm10xx_html_gga2de09557c2f7d19ad141ca8ba48e9f5da43de07adf7b4c2ee51c4c415cf767e81"></a>
<a id="agroup__charger__interface__npm10xx_html_gga2de09557c2f7d19ad141ca8ba48e9f5da5b8931185580b5f5b21adb117af0a407"></a>
<a id="agroup__charger__interface__npm10xx_html_gga2de09557c2f7d19ad141ca8ba48e9f5da9bf9927db001f17b40d71665634662c4"></a>
<a id="agroup__charger__interface__npm10xx_html_gga2de09557c2f7d19ad141ca8ba48e9f5dac1783198b9b10317142dcd3c0d614c76"></a>
<a id="agroup__charger__interface__npm10xx_html_gga2de09557c2f7d19ad141ca8ba48e9f5dadd0b75d418d1b9439ed16383185f7b9e"></a>
<a id="agroup__charger__interface__npm10xx_html_gga2de09557c2f7d19ad141ca8ba48e9f5daec4b5f597aff98e289e5b826e2bf0b01"></a>
<a id="agroup__charger__interface__npm10xx_html_gga2e2382e875599723272916c8eda7e693a24a0a5e7f1ab78f0ac8245a59ee4c1b8"></a>
<a id="agroup__charger__interface__npm10xx_html_gga2e2382e875599723272916c8eda7e693a498a1b6c5493c7bd649b6039a1c95c99"></a>
<a id="agroup__charger__interface__npm10xx_html_gga2e2382e875599723272916c8eda7e693a556ac103ce88c27b2e134570f131006f"></a>
<a id="agroup__charger__interface__npm10xx_html_gga2e2382e875599723272916c8eda7e693a608716ba46dc88ed9728aee15ae878aa"></a>
<a id="agroup__charger__interface__npm10xx_html_gga2e2382e875599723272916c8eda7e693a6b73937a3b83e16c6d2829a35d950312"></a>
<a id="agroup__charger__interface__npm10xx_html_gga2e2382e875599723272916c8eda7e693a92a054648b92527a1e40e7373808c398"></a>
<a id="agroup__charger__interface__npm10xx_html_gga2e2382e875599723272916c8eda7e693ac91db4439de44f8137eb8a723491e0cf"></a>
<a id="agroup__charger__interface__npm10xx_html_gga2e2382e875599723272916c8eda7e693af9c1e0e4bb3dbf2a3f59a6dc07e61756"></a>
<a id="agroup__charger__interface__npm10xx_html_gga51fc3e1a4aa657d030209b1e2f640b88a04e8c6f6ca79ef3ce3980ef47c58baa8"></a>
<a id="agroup__charger__interface__npm10xx_html_gga51fc3e1a4aa657d030209b1e2f640b88a2a95bf55e11ce8daad49ada9cf7e051f"></a>
<a id="agroup__charger__interface__npm10xx_html_gga51fc3e1a4aa657d030209b1e2f640b88a3eb7141403396386412f6f50f778dd48"></a>
<a id="agroup__charger__interface__npm10xx_html_gga51fc3e1a4aa657d030209b1e2f640b88a4e45618b333920e65dfe988db66c0f04"></a>
<a id="agroup__charger__interface__npm10xx_html_gga51fc3e1a4aa657d030209b1e2f640b88a67b674f960d97d7e089d6b3d37270e68"></a>
<a id="agroup__charger__interface__npm10xx_html_gga51fc3e1a4aa657d030209b1e2f640b88a7ede8e6af663b49ed5949cc33b1839a3"></a>
<a id="agroup__charger__interface__npm10xx_html_gga51fc3e1a4aa657d030209b1e2f640b88a85a31b2555549cccb5089e58fa0e37ed"></a>
<a id="agroup__charger__interface__npm10xx_html_gga51fc3e1a4aa657d030209b1e2f640b88a8d7fdc23a114a55170c4ae555381fe5b"></a>
<a id="agroup__charger__interface__npm10xx_html_gga51fc3e1a4aa657d030209b1e2f640b88a9d09acf1922030fb519ca092a7527e62"></a>
<a id="agroup__charger__interface__npm10xx_html_gga51fc3e1a4aa657d030209b1e2f640b88a9def6f7f3b2ec46ae1d500541f9f40ee"></a>
<a id="agroup__charger__interface__npm10xx_html_gga51fc3e1a4aa657d030209b1e2f640b88aa2f1d279f26a3225fc198e491ff7fcf6"></a>
<a id="agroup__charger__interface__npm10xx_html_gga51fc3e1a4aa657d030209b1e2f640b88aab2570493e5da1ba860d5a23859163e7"></a>
<a id="agroup__charger__interface__npm10xx_html_gga51fc3e1a4aa657d030209b1e2f640b88acb6321aef264d44040f077bdad150f3f"></a>
<a id="agroup__charger__interface__npm10xx_html_gga51fc3e1a4aa657d030209b1e2f640b88ad0c98d2cd315171789da2e1c9d77aae0"></a>
<a id="agroup__charger__interface__npm10xx_html_gga51fc3e1a4aa657d030209b1e2f640b88ae47eecdc5eb8efa490afb99e495ef054"></a>
<a id="agroup__charger__interface__npm10xx_html_gga51fc3e1a4aa657d030209b1e2f640b88afa5083a75c161410ec281111574b6d18"></a>
<a id="agroup__charger__interface__npm10xx_html_gga645f680cc19e3d6f0c777dfa41b3abaea2158df739371f0cd8dfadb37b56356c7"></a>
<a id="agroup__charger__interface__npm10xx_html_gga645f680cc19e3d6f0c777dfa41b3abaea25c61182f513f6da143e5c77954bece4"></a>
<a id="agroup__charger__interface__npm10xx_html_gga645f680cc19e3d6f0c777dfa41b3abaea634f230faf1547e0ae7a396be6bc4bcb"></a>
<a id="agroup__charger__interface__npm10xx_html_gga645f680cc19e3d6f0c777dfa41b3abaea7b97b37ac08b922c7382d92ce2c22890"></a>
<a id="agroup__charger__interface__npm10xx_html_gga645f680cc19e3d6f0c777dfa41b3abaea870a1db010506badc4f1579d3d1a7d74"></a>
<a id="agroup__charger__interface__npm10xx_html_gga645f680cc19e3d6f0c777dfa41b3abaea9bff02ec00c10b480cbeda27c8e78c8f"></a>
<a id="agroup__charger__interface__npm10xx_html_gga645f680cc19e3d6f0c777dfa41b3abaeaccdcdd78cd8ba973a1a74ba1a629b609"></a>
<a id="agroup__charger__interface__npm10xx_html_gga645f680cc19e3d6f0c777dfa41b3abaeadb4f86e7b444dd47b417489ce074acf1"></a>
<a id="agroup__charger__interface_html_gga6eb3b4cc76e4f1e34732b7853eb860b7a279bd89ce909be3ea95be2fee33b08b3"></a>

```c
/*
 * Copyright (c) 2026 Nordic Semiconductor ASA
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_CHARGER_NPM10XX_H_
#define ZEPHYR_INCLUDE_DRIVERS_CHARGER_NPM10XX_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <zephyr/drivers/charger.h>


enum npm10xx_charger_prop {
        NPM10XX_CHARGER_PROP_TERM_CURRENT = CHARGER_PROP_CUSTOM_BEGIN,
        NPM10XX_CHARGER_PROP_TRICKLE_CURRENT,
        NPM10XX_CHARGER_PROP_THROTTLE_LVL,
        NPM10XX_CHARGER_PROP_CONSTANT_CHARGE_CURRENT_WARM_UA,
        NPM10XX_CHARGER_PROP_CONSTANT_CHARGE_CURRENT_COOL_UA,
        NPM10XX_CHARGER_PROP_CONSTANT_CHARGE_VOLTAGE_WARM_UV,
        NPM10XX_CHARGER_PROP_CONSTANT_CHARGE_VOLTAGE_COOL_UV,
};

enum npm10xx_charger_iterm {
        NPM10XX_CHARGER_ITERM_12P5,
        NPM10XX_CHARGER_ITERM_100P,
        NPM10XX_CHARGER_ITERM_50P,
        NPM10XX_CHARGER_ITERM_25P,
        NPM10XX_CHARGER_ITERM_6P25,
        NPM10XX_CHARGER_ITERM_3P125,
        NPM10XX_CHARGER_ITERM_1P56,
        NPM10XX_CHARGER_ITERM_0P78,
        NPM10XX_CHARGER_CURRENT_PERCENT_MAX,
};

enum npm10xx_charger_itrickle {
        NPM10XX_CHARGER_ITRICKLE_12P5,
        NPM10XX_CHARGER_ITRICKLE_100P,
        NPM10XX_CHARGER_ITRICKLE_50P,
        NPM10XX_CHARGER_ITRICKLE_25P,
        NPM10XX_CHARGER_ITRICKLE_6P25,
        NPM10XX_CHARGER_ITRICKLE_3P125,
        NPM10XX_CHARGER_ITRICKLE_1P56,
        NPM10XX_CHARGER_ITRICKLE_0P78,
};

enum npm10xx_charger_ithrottle {
        NPM10XX_CHARGER_ITHROTTLE_100P = 0x00U,
        NPM10XX_CHARGER_ITHROTTLE_87P5 = 0x10U,
        NPM10XX_CHARGER_ITHROTTLE_75P = 0x20U,
        NPM10XX_CHARGER_ITHROTTLE_62P5 = 0x30U,
        NPM10XX_CHARGER_ITHROTTLE_50P = 0x40U,
        NPM10XX_CHARGER_ITHROTTLE_37P5 = 0x50U,
        NPM10XX_CHARGER_ITHROTTLE_25P = 0x60U,
        NPM10XX_CHARGER_ITHROTTLE_12P5 = 0x70U,
};

enum npm10xx_charger_vthrottle {
        NPM10XX_CHARGER_VTHROTTLE_25MV,
        NPM10XX_CHARGER_VTHROTTLE_50MV,
        NPM10XX_CHARGER_VTHROTTLE_75MV,
        NPM10XX_CHARGER_VTHROTTLE_100MV,
        NPM10XX_CHARGER_VTHROTTLE_125MV,
        NPM10XX_CHARGER_VTHROTTLE_150MV,
        NPM10XX_CHARGER_VTHROTTLE_175MV,
        NPM10XX_CHARGER_VTHROTTLE_200MV,
        NPM10XX_CHARGER_VTHROTTLE_225MV,
        NPM10XX_CHARGER_VTHROTTLE_250MV,
        NPM10XX_CHARGER_VTHROTTLE_275MV,
        NPM10XX_CHARGER_VTHROTTLE_300MV,
        NPM10XX_CHARGER_VTHROTTLE_325MV,
        NPM10XX_CHARGER_VTHROTTLE_350MV,
        NPM10XX_CHARGER_VTHROTTLE_375MV,
        NPM10XX_CHARGER_VTHROTTLE_400MV,
};


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_CHARGER_NPM10XX_H_ */
```

## 148.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 157 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_CHARGER_NPM10XX_H_`。

## 148.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2charger_2npm10xx_8h.html)
- [zephyr/drivers/charger.h](https://docs.zephyrproject.org/latest/doxygen/html/charger_8h.html)
- [npm10xx_charger_prop](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#ga2de09557c2f7d19ad141ca8ba48e9f5d)
- [NPM10XX_CHARGER_PROP_TERM_CURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#gga2de09557c2f7d19ad141ca8ba48e9f5da43de07adf7b4c2ee51c4c415cf767e81)
- [CHARGER_PROP_CUSTOM_BEGIN](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface.html#gga6eb3b4cc76e4f1e34732b7853eb860b7a279bd89ce909be3ea95be2fee33b08b3)
- [NPM10XX_CHARGER_PROP_TRICKLE_CURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#gga2de09557c2f7d19ad141ca8ba48e9f5daec4b5f597aff98e289e5b826e2bf0b01)
- [NPM10XX_CHARGER_PROP_THROTTLE_LVL](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#gga2de09557c2f7d19ad141ca8ba48e9f5dadd0b75d418d1b9439ed16383185f7b9e)
- [NPM10XX_CHARGER_PROP_CONSTANT_CHARGE_CURRENT_WARM_UA](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#gga2de09557c2f7d19ad141ca8ba48e9f5da5b8931185580b5f5b21adb117af0a407)
- [NPM10XX_CHARGER_PROP_CONSTANT_CHARGE_CURRENT_COOL_UA](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#gga2de09557c2f7d19ad141ca8ba48e9f5dac1783198b9b10317142dcd3c0d614c76)
- [NPM10XX_CHARGER_PROP_CONSTANT_CHARGE_VOLTAGE_WARM_UV](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#gga2de09557c2f7d19ad141ca8ba48e9f5da9bf9927db001f17b40d71665634662c4)
- [NPM10XX_CHARGER_PROP_CONSTANT_CHARGE_VOLTAGE_COOL_UV](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#gga2de09557c2f7d19ad141ca8ba48e9f5da16efc7a009faff4fdecb0548cfee8e67)
- [npm10xx_charger_iterm](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#ga0361b1ebfc18e176ed171823a38e12ab)
- [NPM10XX_CHARGER_ITERM_12P5](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#gga0361b1ebfc18e176ed171823a38e12aba0959a4ef28fcfd44de6f4c852744e197)
- [NPM10XX_CHARGER_ITERM_100P](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#gga0361b1ebfc18e176ed171823a38e12abad6f6c26c8759613c05a10592ac628d15)
- [NPM10XX_CHARGER_ITERM_50P](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#gga0361b1ebfc18e176ed171823a38e12aba44ed6f6aea9feee4577635fffc480dfb)
- [NPM10XX_CHARGER_ITERM_25P](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#gga0361b1ebfc18e176ed171823a38e12abab7aaa32e285208f86889cc7d7a0060c0)
- [NPM10XX_CHARGER_ITERM_6P25](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#gga0361b1ebfc18e176ed171823a38e12aba25a044f38b048ff0451e556b42534b67)
- [NPM10XX_CHARGER_ITERM_3P125](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#gga0361b1ebfc18e176ed171823a38e12abae981727f782b8459d41757151b0cdcf7)
- [NPM10XX_CHARGER_ITERM_1P56](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#gga0361b1ebfc18e176ed171823a38e12abafa68639f27c5366ad45db5c56f2268af)
- [NPM10XX_CHARGER_ITERM_0P78](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#gga0361b1ebfc18e176ed171823a38e12aba8ca1895fc6fe1a8660f2e2b2452c5f59)
- [NPM10XX_CHARGER_CURRENT_PERCENT_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#gga0361b1ebfc18e176ed171823a38e12aba911e517245594be44d2c4cc971cee1bd)
- [npm10xx_charger_itrickle](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#ga645f680cc19e3d6f0c777dfa41b3abae)
- [NPM10XX_CHARGER_ITRICKLE_12P5](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#gga645f680cc19e3d6f0c777dfa41b3abaea7b97b37ac08b922c7382d92ce2c22890)
- [NPM10XX_CHARGER_ITRICKLE_100P](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#gga645f680cc19e3d6f0c777dfa41b3abaea870a1db010506badc4f1579d3d1a7d74)
- [NPM10XX_CHARGER_ITRICKLE_50P](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#gga645f680cc19e3d6f0c777dfa41b3abaea25c61182f513f6da143e5c77954bece4)
- [NPM10XX_CHARGER_ITRICKLE_25P](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#gga645f680cc19e3d6f0c777dfa41b3abaeaccdcdd78cd8ba973a1a74ba1a629b609)
- [NPM10XX_CHARGER_ITRICKLE_6P25](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#gga645f680cc19e3d6f0c777dfa41b3abaea2158df739371f0cd8dfadb37b56356c7)
- [NPM10XX_CHARGER_ITRICKLE_3P125](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#gga645f680cc19e3d6f0c777dfa41b3abaea634f230faf1547e0ae7a396be6bc4bcb)
- [NPM10XX_CHARGER_ITRICKLE_1P56](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#gga645f680cc19e3d6f0c777dfa41b3abaeadb4f86e7b444dd47b417489ce074acf1)
- [NPM10XX_CHARGER_ITRICKLE_0P78](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#gga645f680cc19e3d6f0c777dfa41b3abaea9bff02ec00c10b480cbeda27c8e78c8f)
- [npm10xx_charger_ithrottle](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#ga2e2382e875599723272916c8eda7e693)
- [NPM10XX_CHARGER_ITHROTTLE_100P](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#gga2e2382e875599723272916c8eda7e693ac91db4439de44f8137eb8a723491e0cf)
- [NPM10XX_CHARGER_ITHROTTLE_87P5](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#gga2e2382e875599723272916c8eda7e693af9c1e0e4bb3dbf2a3f59a6dc07e61756)
- [NPM10XX_CHARGER_ITHROTTLE_75P](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#gga2e2382e875599723272916c8eda7e693a24a0a5e7f1ab78f0ac8245a59ee4c1b8)
- [NPM10XX_CHARGER_ITHROTTLE_62P5](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#gga2e2382e875599723272916c8eda7e693a556ac103ce88c27b2e134570f131006f)
- [NPM10XX_CHARGER_ITHROTTLE_50P](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#gga2e2382e875599723272916c8eda7e693a6b73937a3b83e16c6d2829a35d950312)
- [NPM10XX_CHARGER_ITHROTTLE_37P5](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#gga2e2382e875599723272916c8eda7e693a498a1b6c5493c7bd649b6039a1c95c99)
- [NPM10XX_CHARGER_ITHROTTLE_25P](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#gga2e2382e875599723272916c8eda7e693a608716ba46dc88ed9728aee15ae878aa)
- [NPM10XX_CHARGER_ITHROTTLE_12P5](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#gga2e2382e875599723272916c8eda7e693a92a054648b92527a1e40e7373808c398)
- [npm10xx_charger_vthrottle](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#ga51fc3e1a4aa657d030209b1e2f640b88)
- [NPM10XX_CHARGER_VTHROTTLE_25MV](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#gga51fc3e1a4aa657d030209b1e2f640b88a8d7fdc23a114a55170c4ae555381fe5b)
- [NPM10XX_CHARGER_VTHROTTLE_50MV](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#gga51fc3e1a4aa657d030209b1e2f640b88a9d09acf1922030fb519ca092a7527e62)
- [NPM10XX_CHARGER_VTHROTTLE_75MV](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#gga51fc3e1a4aa657d030209b1e2f640b88aa2f1d279f26a3225fc198e491ff7fcf6)
- [NPM10XX_CHARGER_VTHROTTLE_100MV](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#gga51fc3e1a4aa657d030209b1e2f640b88a4e45618b333920e65dfe988db66c0f04)
- [NPM10XX_CHARGER_VTHROTTLE_125MV](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#gga51fc3e1a4aa657d030209b1e2f640b88a67b674f960d97d7e089d6b3d37270e68)
- [NPM10XX_CHARGER_VTHROTTLE_150MV](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#gga51fc3e1a4aa657d030209b1e2f640b88ae47eecdc5eb8efa490afb99e495ef054)
- [NPM10XX_CHARGER_VTHROTTLE_175MV](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#gga51fc3e1a4aa657d030209b1e2f640b88a85a31b2555549cccb5089e58fa0e37ed)
- [NPM10XX_CHARGER_VTHROTTLE_200MV](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#gga51fc3e1a4aa657d030209b1e2f640b88a3eb7141403396386412f6f50f778dd48)
- [NPM10XX_CHARGER_VTHROTTLE_225MV](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#gga51fc3e1a4aa657d030209b1e2f640b88a2a95bf55e11ce8daad49ada9cf7e051f)
- [NPM10XX_CHARGER_VTHROTTLE_250MV](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#gga51fc3e1a4aa657d030209b1e2f640b88a04e8c6f6ca79ef3ce3980ef47c58baa8)
- [NPM10XX_CHARGER_VTHROTTLE_275MV](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#gga51fc3e1a4aa657d030209b1e2f640b88aab2570493e5da1ba860d5a23859163e7)
- [NPM10XX_CHARGER_VTHROTTLE_300MV](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#gga51fc3e1a4aa657d030209b1e2f640b88ad0c98d2cd315171789da2e1c9d77aae0)
- [NPM10XX_CHARGER_VTHROTTLE_325MV](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#gga51fc3e1a4aa657d030209b1e2f640b88a7ede8e6af663b49ed5949cc33b1839a3)
- [NPM10XX_CHARGER_VTHROTTLE_350MV](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#gga51fc3e1a4aa657d030209b1e2f640b88afa5083a75c161410ec281111574b6d18)
- [NPM10XX_CHARGER_VTHROTTLE_375MV](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#gga51fc3e1a4aa657d030209b1e2f640b88a9def6f7f3b2ec46ae1d500541f9f40ee)
- [NPM10XX_CHARGER_VTHROTTLE_400MV](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__npm10xx.html#gga51fc3e1a4aa657d030209b1e2f640b88acb6321aef264d44040f077bdad150f3f)
- [charger.h](https://docs.zephyrproject.org/latest/doxygen/html/charger_8h.html)

---

[上一章](P147_emul.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P149_atmel_sam_pmc.h_源码浏览.md)
