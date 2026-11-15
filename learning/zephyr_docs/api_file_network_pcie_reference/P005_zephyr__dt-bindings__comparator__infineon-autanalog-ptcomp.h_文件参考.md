---
id: learning.zephyr-docs.api-file-network-pcie-reference.page-5
title: zephyr__dt-bindings__comparator__infineon-autanalog-ptcomp.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ptcomp_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_zephyr\_\_dt-bindings\_\_comparator\_\_infineon-autanalog-ptcomp.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ptcomp_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Infineon AutAnalog PTCOMP的设备树绑定常量（Devicetree Binding Constants）。

查看此文件的源码。

<a id="details"></a>

Infineon AutAnalog PTCOMP 的设备树绑定常量（Devicetree Binding Constants）。这些常量与 PDL 枚举值一致，供配置 AutAnalog 可编程阈值比较器（Programmable Threshold Comparator）及其后处理模块（Post-processing Block）的设备树属性使用。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 功耗模式（Power modes (cy_en_autanalog_ptcomp_comp_pwr_t)）

<a id="r_a4b1d652b24b48443cc5febd738dea51b"></a>

```c
#define IFX_AUTANALOG_PTCOMP_PWR_OFF 0
```

相关声明：[IFX_AUTANALOG_PTCOMP_PWR_OFF](#a4b1d652b24b48443cc5febd738dea51b)。

比较器断电（Comparator Powered Off）。

<a id="r_a4e6f2e178862981d80a4f2a63b7728cd"></a>

```c
#define IFX_AUTANALOG_PTCOMP_PWR_ULP 1
```

相关声明：[IFX_AUTANALOG_PTCOMP_PWR_ULP](#a4e6f2e178862981d80a4f2a63b7728cd)。

超低功耗模式（Ultra Low Power Mode）。

<a id="r_a6e4dffba51be30f5ea1a34abcdcdd343"></a>

```c
#define IFX_AUTANALOG_PTCOMP_PWR_LP 2
```

相关声明：[IFX_AUTANALOG_PTCOMP_PWR_LP](#a6e4dffba51be30f5ea1a34abcdcdd343)。

低功耗模式（Low Power Mode）。

<a id="r_adea94d8f8ccda38ae4fdee874a2d9169"></a>

```c
#define IFX_AUTANALOG_PTCOMP_PWR_NORMAL 3
```

相关声明：[IFX_AUTANALOG_PTCOMP_PWR_NORMAL](#adea94d8f8ccda38ae4fdee874a2d9169)。

正常功耗模式（Normal Power Mode）。

<a id="define-members-1"></a>

### 中断与边沿检测模式（Interrupt and edge detection modes (cy_en_autanalog_ptcomp_comp_int_t)）

<a id="r_a49dec981f509aec2161a87f0df7eb4b7"></a>

```c
#define IFX_AUTANALOG_PTCOMP_INT_DISABLED 0
```

相关声明：[IFX_AUTANALOG_PTCOMP_INT_DISABLED](#a49dec981f509aec2161a87f0df7eb4b7)。

中断已禁用（Interrupt Disabled）。

<a id="r_a354b8b9bef7b7c58d8d694e491001017"></a>

```c
#define IFX_AUTANALOG_PTCOMP_INT_EDGE_RISING 1
```

相关声明：[IFX_AUTANALOG_PTCOMP_INT_EDGE_RISING](#a354b8b9bef7b7c58d8d694e491001017)。

上升沿检测（Rising Edge Detection）。

<a id="r_abe4d013dc59ed59d0d4583812c024c9c"></a>

```c
#define IFX_AUTANALOG_PTCOMP_INT_EDGE_FALLING 2
```

相关声明：[IFX_AUTANALOG_PTCOMP_INT_EDGE_FALLING](#abe4d013dc59ed59d0d4583812c024c9c)。

下降沿检测（Falling Edge Detection）。

<a id="r_a9ecc3c820d21e4938ed2ad6b39649a51"></a>

```c
#define IFX_AUTANALOG_PTCOMP_INT_EDGE_BOTH 3
```

相关声明：[IFX_AUTANALOG_PTCOMP_INT_EDGE_BOTH](#a9ecc3c820d21e4938ed2ad6b39649a51)。

双边沿检测（Both-edge Detection）。

<a id="define-members-2"></a>

### 输入多路复用器选择项（Input mux selectors (cy_en_autanalog_ptcomp_comp_mux_t)）

<a id="r_a89a79c5fb40ccc444c76a22e9df1473e"></a>

```c
#define IFX_AUTANALOG_PTCOMP_MUX_CTB0_PIN1 0
```

相关声明：[IFX_AUTANALOG_PTCOMP_MUX_CTB0_PIN1](#a89a79c5fb40ccc444c76a22e9df1473e)。

CTB0 的 GPIO 引脚（Pin）1。

<a id="r_a62ddf951adb5ffda5d97879dc003d485"></a>

```c
#define IFX_AUTANALOG_PTCOMP_MUX_CTB0_PIN4 1
```

相关声明：[IFX_AUTANALOG_PTCOMP_MUX_CTB0_PIN4](#a62ddf951adb5ffda5d97879dc003d485)。

CTB0 的 GPIO 引脚（Pin）4。

<a id="r_a8dd86eae5d4e5a58f50ab41277117775"></a>

```c
#define IFX_AUTANALOG_PTCOMP_MUX_CTB0_PIN6 2
```

相关声明：[IFX_AUTANALOG_PTCOMP_MUX_CTB0_PIN6](#a8dd86eae5d4e5a58f50ab41277117775)。

CTB0 的 GPIO 引脚（Pin）6。

<a id="r_a1073f9578281cb466a17d0e901a793e2"></a>

```c
#define IFX_AUTANALOG_PTCOMP_MUX_CTB0_PIN7 3
```

相关声明：[IFX_AUTANALOG_PTCOMP_MUX_CTB0_PIN7](#a1073f9578281cb466a17d0e901a793e2)。

CTB0 的 GPIO 引脚（Pin）7。

<a id="r_af3583d95e1eca3e97ca1293d4697899a"></a>

```c
#define IFX_AUTANALOG_PTCOMP_MUX_CTB1_PIN1 4
```

相关声明：[IFX_AUTANALOG_PTCOMP_MUX_CTB1_PIN1](#af3583d95e1eca3e97ca1293d4697899a)。

CTB1 的 GPIO 引脚（Pin）1。

<a id="r_ad840d0c1d51cb2a89104d9fd5c5d8412"></a>

```c
#define IFX_AUTANALOG_PTCOMP_MUX_CTB1_PIN4 5
```

相关声明：[IFX_AUTANALOG_PTCOMP_MUX_CTB1_PIN4](#ad840d0c1d51cb2a89104d9fd5c5d8412)。

CTB1 的 GPIO 引脚（Pin）4。

<a id="r_a27e234b8ad9e4bb5c88582cbf43cc433"></a>

```c
#define IFX_AUTANALOG_PTCOMP_MUX_CTB1_PIN6 6
```

相关声明：[IFX_AUTANALOG_PTCOMP_MUX_CTB1_PIN6](#a27e234b8ad9e4bb5c88582cbf43cc433)。

CTB1 的 GPIO 引脚（Pin）6。

<a id="r_a85c1b51011bc8807cdffcab0fc3d2408"></a>

```c
#define IFX_AUTANALOG_PTCOMP_MUX_CTB1_PIN7 7
```

相关声明：[IFX_AUTANALOG_PTCOMP_MUX_CTB1_PIN7](#a85c1b51011bc8807cdffcab0fc3d2408)。

CTB1 的 GPIO 引脚（Pin）7。

<a id="r_ad02919b1eb80d42c7848791297ef5795"></a>

```c
#define IFX_AUTANALOG_PTCOMP_MUX_CTB0_OA0_OUT 8
```

相关声明：[IFX_AUTANALOG_PTCOMP_MUX_CTB0_OA0_OUT](#ad02919b1eb80d42c7848791297ef5795)。

CTB0 的运算放大器 0 输出（OpAmp0 Output）。

<a id="r_af9ef07fe1e1e2caea20b344ab243419a"></a>

```c
#define IFX_AUTANALOG_PTCOMP_MUX_CTB0_OA1_OUT 9
```

相关声明：[IFX_AUTANALOG_PTCOMP_MUX_CTB0_OA1_OUT](#af9ef07fe1e1e2caea20b344ab243419a)。

CTB0 的运算放大器 1 输出（OpAmp1 Output）。

<a id="r_aa6a8e541333fea50dc73fc06be8f3df1"></a>

```c
#define IFX_AUTANALOG_PTCOMP_MUX_CTB1_OA0_OUT 10
```

相关声明：[IFX_AUTANALOG_PTCOMP_MUX_CTB1_OA0_OUT](#aa6a8e541333fea50dc73fc06be8f3df1)。

CTB1 的运算放大器 0 输出（OpAmp0 Output）。

<a id="r_ad3974446d217a168a866abf3c0d3e10b"></a>

```c
#define IFX_AUTANALOG_PTCOMP_MUX_CTB1_OA1_OUT 11
```

相关声明：[IFX_AUTANALOG_PTCOMP_MUX_CTB1_OA1_OUT](#ad3974446d217a168a866abf3c0d3e10b)。

CTB1 的运算放大器 1 输出（OpAmp1 Output）。

<a id="r_a5c3e4541befd309f4a78e14b484f8c51"></a>

```c
#define IFX_AUTANALOG_PTCOMP_MUX_DAC0 12
```

相关声明：[IFX_AUTANALOG_PTCOMP_MUX_DAC0](#a5c3e4541befd309f4a78e14b484f8c51)。

DAC0 输出（Output）。

<a id="r_a64008ae19113150d812ecd2c5c3553c1"></a>

```c
#define IFX_AUTANALOG_PTCOMP_MUX_DAC1 13
```

相关声明：[IFX_AUTANALOG_PTCOMP_MUX_DAC1](#a64008ae19113150d812ecd2c5c3553c1)。

DAC1 输出（Output）。

<a id="r_a8b8125671a7d26ffecfcf43fd155ff60"></a>

```c
#define IFX_AUTANALOG_PTCOMP_MUX_PRB_OUT0 14
```

相关声明：[IFX_AUTANALOG_PTCOMP_MUX_PRB_OUT0](#a8b8125671a7d26ffecfcf43fd155ff60)。

PRB 输出（Output） 0。

<a id="r_a6dbb59d83d05b656d969a40c064b1a60"></a>

```c
#define IFX_AUTANALOG_PTCOMP_MUX_PRB_OUT1 15
```

相关声明：[IFX_AUTANALOG_PTCOMP_MUX_PRB_OUT1](#a6dbb59d83d05b656d969a40c064b1a60)。

PRB 输出（Output） 1。

<a id="r_a726c4a7aa8aafe396420a4b04d02479f"></a>

```c
#define IFX_AUTANALOG_PTCOMP_MUX_GPIO0 16
```

相关声明：[IFX_AUTANALOG_PTCOMP_MUX_GPIO0](#a726c4a7aa8aafe396420a4b04d02479f)。

GPIO 0。

<a id="r_a3d3c50a51fe3350bc47a8dc063e1dc20"></a>

```c
#define IFX_AUTANALOG_PTCOMP_MUX_GPIO1 17
```

相关声明：[IFX_AUTANALOG_PTCOMP_MUX_GPIO1](#a3d3c50a51fe3350bc47a8dc063e1dc20)。

GPIO 1。

<a id="r_a09bef786d22362a2c0ebd9e9f83a1320"></a>

```c
#define IFX_AUTANALOG_PTCOMP_MUX_GPIO2 18
```

相关声明：[IFX_AUTANALOG_PTCOMP_MUX_GPIO2](#a09bef786d22362a2c0ebd9e9f83a1320)。

GPIO 2。

<a id="r_a0c7a8068598c13c0e24a1dfd08b0a08b"></a>

```c
#define IFX_AUTANALOG_PTCOMP_MUX_GPIO3 19
```

相关声明：[IFX_AUTANALOG_PTCOMP_MUX_GPIO3](#a0c7a8068598c13c0e24a1dfd08b0a08b)。

GPIO 3。

<a id="r_a868d420e9cd0f25c0982a173317b2c35"></a>

```c
#define IFX_AUTANALOG_PTCOMP_MUX_GPIO4 20
```

相关声明：[IFX_AUTANALOG_PTCOMP_MUX_GPIO4](#a868d420e9cd0f25c0982a173317b2c35)。

GPIO 4。

<a id="r_a91d69f0d79f78defc3ee71cb5a0af449"></a>

```c
#define IFX_AUTANALOG_PTCOMP_MUX_GPIO5 21
```

相关声明：[IFX_AUTANALOG_PTCOMP_MUX_GPIO5](#a91d69f0d79f78defc3ee71cb5a0af449)。

GPIO 5。

<a id="r_a883241de0e0b392628f3521c635d4728"></a>

```c
#define IFX_AUTANALOG_PTCOMP_MUX_GPIO6 22
```

相关声明：[IFX_AUTANALOG_PTCOMP_MUX_GPIO6](#a883241de0e0b392628f3521c635d4728)。

GPIO 6。

<a id="r_a90113dd01a1bbd35f4fec139b4dbd473"></a>

```c
#define IFX_AUTANALOG_PTCOMP_MUX_GPIO7 23
```

相关声明：[IFX_AUTANALOG_PTCOMP_MUX_GPIO7](#a90113dd01a1bbd35f4fec139b4dbd473)。

GPIO 7。

<a id="define-members-3"></a>

### 后处理输入源（Post-processing input source (cy_en_autanalog_ptcomp_pp_input_src_t)）

<a id="r_a429c6785e1f83121cdcc77402d36903d"></a>

```c
#define IFX_AUTANALOG_PTCOMP_PP_SRC_DISABLED 0
```

相关声明：[IFX_AUTANALOG_PTCOMP_PP_SRC_DISABLED](#a429c6785e1f83121cdcc77402d36903d)。

后处理输入已禁用（Post-processing Input Disabled）。

<a id="r_a66e053c7e354c11537814453279107d8"></a>

```c
#define IFX_AUTANALOG_PTCOMP_PP_SRC_COMP0 1
```

相关声明：[IFX_AUTANALOG_PTCOMP_PP_SRC_COMP0](#a66e053c7e354c11537814453279107d8)。

比较器 0 输出（Comparator 0 Output）。

<a id="r_a533e0f22932eea1af03af8028155a26c"></a>

```c
#define IFX_AUTANALOG_PTCOMP_PP_SRC_COMP1 2
```

相关声明：[IFX_AUTANALOG_PTCOMP_PP_SRC_COMP1](#a533e0f22932eea1af03af8028155a26c)。

比较器 1 输出（Comparator 1 Output）。

<a id="define-members-4"></a>

### 后处理输入类型（Post-processing input type (cy_en_autanalog_ptcomp_pp_input_type_t)）

<a id="r_a25328fe25c5a02485a55ee0d3670d043"></a>

```c
#define IFX_AUTANALOG_PTCOMP_PP_TYPE_LEVEL 0
```

相关声明：[IFX_AUTANALOG_PTCOMP_PP_TYPE_LEVEL](#a25328fe25c5a02485a55ee0d3670d043)。

电平敏感输入（Level-sensitive Input）。

<a id="r_a2a39251c0661754fb5dfa55c466eee4b"></a>

```c
#define IFX_AUTANALOG_PTCOMP_PP_TYPE_EDGE_RISING 1
```

相关声明：[IFX_AUTANALOG_PTCOMP_PP_TYPE_EDGE_RISING](#a2a39251c0661754fb5dfa55c466eee4b)。

上升沿输入（Rising Edge Input）。

<a id="r_a059f83551f58e84235681c1acdade4dc"></a>

```c
#define IFX_AUTANALOG_PTCOMP_PP_TYPE_EDGE_FALLING 2
```

相关声明：[IFX_AUTANALOG_PTCOMP_PP_TYPE_EDGE_FALLING](#a059f83551f58e84235681c1acdade4dc)。

下降沿输入（Falling Edge Input）。

<a id="r_afb56deef623a39aee5f9678a4d3767b9"></a>

```c
#define IFX_AUTANALOG_PTCOMP_PP_TYPE_EDGE_BOTH 3
```

相关声明：[IFX_AUTANALOG_PTCOMP_PP_TYPE_EDGE_BOTH](#afb56deef623a39aee5f9678a4d3767b9)。

双边沿输入（Both-edge Input）。

<a id="define-members-5"></a>

### 后处理计数器模式（Post-processing counter mode (cy_en_autanalog_ptcomp_pp_cnt_mode_t)）

<a id="r_ab80e2b0e3802b5c19e66893e507d7ac8"></a>

```c
#define IFX_AUTANALOG_PTCOMP_PP_MODE_DIRECT 0
```

相关声明：[IFX_AUTANALOG_PTCOMP_PP_MODE_DIRECT](#ab80e2b0e3802b5c19e66893e507d7ac8)。

直接计数器模式（Direct Counter Mode）。

<a id="r_a2b200d37d26b5301062417630770e2ce"></a>

```c
#define IFX_AUTANALOG_PTCOMP_PP_MODE_FRAME 1
```

相关声明：[IFX_AUTANALOG_PTCOMP_PP_MODE_FRAME](#a2b200d37d26b5301062417630770e2ce)。

帧计数器模式（Frame Counter Mode）。

<a id="r_aa6003730a4505aacd4e6b619014a3dfa"></a>

```c
#define IFX_AUTANALOG_PTCOMP_PP_MODE_WINDOW 2
```

相关声明：[IFX_AUTANALOG_PTCOMP_PP_MODE_WINDOW](#aa6003730a4505aacd4e6b619014a3dfa)。

窗口计数器模式（Window Counter Mode）。

<a id="define-members-6"></a>

### 后处理数据函数／查找表（Post-processing data function / LUT (cy_en_autanalog_ptcomp_pp_data_func_t)）

<a id="r_aff496eeaadcbf3f112a25fa5e1a7c599"></a>

```c
#define IFX_AUTANALOG_PTCOMP_PP_FUNC_A 0
```

相关声明：[IFX_AUTANALOG_PTCOMP_PP_FUNC_A](#aff496eeaadcbf3f112a25fa5e1a7c599)。

直接传递输入 A（Pass Input A）。

<a id="r_aa3d0d48b1a9f45162688becc97dfb9db"></a>

```c
#define IFX_AUTANALOG_PTCOMP_PP_FUNC_A_BAR_AND_B 1
```

相关声明：[IFX_AUTANALOG_PTCOMP_PP_FUNC_A_BAR_AND_B](#aa3d0d48b1a9f45162688becc97dfb9db)。

逻辑运算：非 A 与 B（NOT A AND B）。

<a id="r_a82caa8189b2fa1b26ba5a0cacca34f73"></a>

```c
#define IFX_AUTANALOG_PTCOMP_PP_FUNC_B 2
```

相关声明：[IFX_AUTANALOG_PTCOMP_PP_FUNC_B](#a82caa8189b2fa1b26ba5a0cacca34f73)。

直接传递输入 B（Pass Input B）。

<a id="r_ab2948309a5ce37089946f496d7ec2971"></a>

```c
#define IFX_AUTANALOG_PTCOMP_PP_FUNC_A_AND_B 3
```

相关声明：[IFX_AUTANALOG_PTCOMP_PP_FUNC_A_AND_B](#ab2948309a5ce37089946f496d7ec2971)。

逻辑运算：A 与 B（A AND B）。

<a id="r_adce47666a9e5ba735e2bce617c1e754a"></a>

```c
#define IFX_AUTANALOG_PTCOMP_PP_FUNC_A_AND_B_BAR 4
```

相关声明：[IFX_AUTANALOG_PTCOMP_PP_FUNC_A_AND_B_BAR](#adce47666a9e5ba735e2bce617c1e754a)。

逻辑运算：A 与非 B（A AND NOT B）。

<a id="r_aab2870f9d61e06f225bae4be1dc1291c"></a>

```c
#define IFX_AUTANALOG_PTCOMP_PP_FUNC_A_XOR_B 5
```

相关声明：[IFX_AUTANALOG_PTCOMP_PP_FUNC_A_XOR_B](#aab2870f9d61e06f225bae4be1dc1291c)。

逻辑运算：A 异或 B（A XOR B）。

<a id="r_ac7f6030855748afc21e1d9d46ade3426"></a>

```c
#define IFX_AUTANALOG_PTCOMP_PP_FUNC_A_OR_B 6
```

相关声明：[IFX_AUTANALOG_PTCOMP_PP_FUNC_A_OR_B](#ac7f6030855748afc21e1d9d46ade3426)。

逻辑运算：A 或 B（A OR B）。

<a id="r_a310dcb76dfc574dd53b381e672df7b27"></a>

```c
#define IFX_AUTANALOG_PTCOMP_PP_FUNC_A_NOR_B 7
```

相关声明：[IFX_AUTANALOG_PTCOMP_PP_FUNC_A_NOR_B](#a310dcb76dfc574dd53b381e672df7b27)。

逻辑或非（A NOR B），即 `NOT (A OR B)`。

<a id="r_af98d8481e5eef0cf3014899719b20cbd"></a>

```c
#define IFX_AUTANALOG_PTCOMP_PP_FUNC_A_XNOR_B 8
```

相关声明：[IFX_AUTANALOG_PTCOMP_PP_FUNC_A_XNOR_B](#af98d8481e5eef0cf3014899719b20cbd)。

逻辑同或（A XNOR B），即 `NOT (A XOR B)`。

<a id="r_aa7fade24e47ffbb1397626c48ba0f033"></a>

```c
#define IFX_AUTANALOG_PTCOMP_PP_FUNC_B_BAR 9
```

相关声明：[IFX_AUTANALOG_PTCOMP_PP_FUNC_B_BAR](#aa7fade24e47ffbb1397626c48ba0f033)。

传递逻辑非 B（NOT B）。

<a id="r_a128c14ee3a08bb4a2346a1a3c7065e06"></a>

```c
#define IFX_AUTANALOG_PTCOMP_PP_FUNC_A_OR_B_BAR 10
```

相关声明：[IFX_AUTANALOG_PTCOMP_PP_FUNC_A_OR_B_BAR](#a128c14ee3a08bb4a2346a1a3c7065e06)。

逻辑运算：A 或非 B（A OR NOT B）。

<a id="r_a762c962aed9ab6aef86e149d8b34153d"></a>

```c
#define IFX_AUTANALOG_PTCOMP_PP_FUNC_A_BAR 11
```

相关声明：[IFX_AUTANALOG_PTCOMP_PP_FUNC_A_BAR](#a762c962aed9ab6aef86e149d8b34153d)。

传递逻辑非 A（NOT A）。

<a id="r_a032ea9c1952b4a077340a8c21cf46aaa"></a>

```c
#define IFX_AUTANALOG_PTCOMP_PP_FUNC_A_BAR_OR_B 12
```

相关声明：[IFX_AUTANALOG_PTCOMP_PP_FUNC_A_BAR_OR_B](#a032ea9c1952b4a077340a8c21cf46aaa)。

逻辑运算：非 A 或 B（NOT A OR B）。

<a id="r_a32a3da377723365791b9b7eabf84b0ac"></a>

```c
#define IFX_AUTANALOG_PTCOMP_PP_FUNC_A_NAND_B 13
```

相关声明：[IFX_AUTANALOG_PTCOMP_PP_FUNC_A_NAND_B](#a32a3da377723365791b9b7eabf84b0ac)。

逻辑与非（A NAND B），即 `NOT (A AND B)`。

<a id="define-members-7"></a>

### 后处理窗口大小（Post-processing window size (cy_en_autanalog_ptcomp_pp_window_size_t)）

<a id="r_a70a4da422609f181e568bb0402448949"></a>

```c
#define IFX_AUTANALOG_PTCOMP_PP_WIN_2 0
```

相关声明：[IFX_AUTANALOG_PTCOMP_PP_WIN_2](#a70a4da422609f181e568bb0402448949)。

窗口大小（Window Size）为 2 个样本。

<a id="r_aee57aab8de54ec22cca0ff19dfeea756"></a>

```c
#define IFX_AUTANALOG_PTCOMP_PP_WIN_4 1
```

相关声明：[IFX_AUTANALOG_PTCOMP_PP_WIN_4](#aee57aab8de54ec22cca0ff19dfeea756)。

窗口大小（Window Size）为 4 个样本。

<a id="r_ade18f1a187e678c4bf5df279e061a20d"></a>

```c
#define IFX_AUTANALOG_PTCOMP_PP_WIN_8 2
```

相关声明：[IFX_AUTANALOG_PTCOMP_PP_WIN_8](#ade18f1a187e678c4bf5df279e061a20d)。

窗口大小（Window Size）为 8 个样本。

<a id="r_ab5cf536162dab59d108dee9946eab18b"></a>

```c
#define IFX_AUTANALOG_PTCOMP_PP_WIN_16 3
```

相关声明：[IFX_AUTANALOG_PTCOMP_PP_WIN_16](#ab5cf536162dab59d108dee9946eab18b)。

窗口大小（Window Size）为 16 个样本。

<a id="r_ad21b521403e3678fcaea25670bd55594"></a>

```c
#define IFX_AUTANALOG_PTCOMP_PP_WIN_32 4
```

相关声明：[IFX_AUTANALOG_PTCOMP_PP_WIN_32](#ad21b521403e3678fcaea25670bd55594)。

窗口大小（Window Size）为 32 个样本。

<a id="r_a2a5de60fa514466bd64d53419519dd99"></a>

```c
#define IFX_AUTANALOG_PTCOMP_PP_WIN_64 5
```

相关声明：[IFX_AUTANALOG_PTCOMP_PP_WIN_64](#a2a5de60fa514466bd64d53419519dd99)。

窗口大小（Window Size）为 64 个样本。

<a id="r_a62596dd57277bc9df5301cad4af63721"></a>

```c
#define IFX_AUTANALOG_PTCOMP_PP_WIN_128 6
```

相关声明：[IFX_AUTANALOG_PTCOMP_PP_WIN_128](#a62596dd57277bc9df5301cad4af63721)。

窗口大小（Window Size）为 128 个样本。

<a id="define-members-8"></a>

### 后处理限值条件（Post-processing limit condition (cy_en_autanalog_ptcomp_pp_cond_t)）

<a id="r_a087894c04a05625f5b4441167aa54488"></a>

```c
#define IFX_AUTANALOG_PTCOMP_PP_COND_BELOW 0
```

相关声明：[IFX_AUTANALOG_PTCOMP_PP_COND_BELOW](#a087894c04a05625f5b4441167aa54488)。

结果低于阈值窗口（Threshold Window）。

<a id="r_af01070c224eb3309906eb6fa68603b27"></a>

```c
#define IFX_AUTANALOG_PTCOMP_PP_COND_INSIDE 1
```

相关声明：[IFX_AUTANALOG_PTCOMP_PP_COND_INSIDE](#af01070c224eb3309906eb6fa68603b27)。

结果位于阈值窗口（Threshold Window）内。

<a id="r_a2f7ededb25653489ab83ba4b56baa154"></a>

```c
#define IFX_AUTANALOG_PTCOMP_PP_COND_ABOVE 2
```

相关声明：[IFX_AUTANALOG_PTCOMP_PP_COND_ABOVE](#a2f7ededb25653489ab83ba4b56baa154)。

结果高于阈值窗口（Threshold Window）。

<a id="r_a2d7d9a7c49ddb2eb7c5b8c50546f2bc8"></a>

```c
#define IFX_AUTANALOG_PTCOMP_PP_COND_OUTSIDE 3
```

相关声明：[IFX_AUTANALOG_PTCOMP_PP_COND_OUTSIDE](#a2d7d9a7c49ddb2eb7c5b8c50546f2bc8)。

结果位于阈值窗口（Threshold Window）外。

## 5.2\_详细说明（Detailed Documentation）

<a id="a49dec981f509aec2161a87f0df7eb4b7"></a>

### `IFX_AUTANALOG_PTCOMP_INT_DISABLED`

```c
#define IFX_AUTANALOG_PTCOMP_INT_DISABLED 0
```

中断已禁用（Interrupt Disabled）。

<a id="a9ecc3c820d21e4938ed2ad6b39649a51"></a>

### `IFX_AUTANALOG_PTCOMP_INT_EDGE_BOTH`

```c
#define IFX_AUTANALOG_PTCOMP_INT_EDGE_BOTH 3
```

双边沿检测（Both-edge Detection）。

<a id="abe4d013dc59ed59d0d4583812c024c9c"></a>

### `IFX_AUTANALOG_PTCOMP_INT_EDGE_FALLING`

```c
#define IFX_AUTANALOG_PTCOMP_INT_EDGE_FALLING 2
```

下降沿检测（Falling Edge Detection）。

<a id="a354b8b9bef7b7c58d8d694e491001017"></a>

### `IFX_AUTANALOG_PTCOMP_INT_EDGE_RISING`

```c
#define IFX_AUTANALOG_PTCOMP_INT_EDGE_RISING 1
```

上升沿检测（Rising Edge Detection）。

<a id="ad02919b1eb80d42c7848791297ef5795"></a>

### `IFX_AUTANALOG_PTCOMP_MUX_CTB0_OA0_OUT`

```c
#define IFX_AUTANALOG_PTCOMP_MUX_CTB0_OA0_OUT 8
```

CTB0 的运算放大器 0 输出（OpAmp0 Output）。

<a id="af9ef07fe1e1e2caea20b344ab243419a"></a>

### `IFX_AUTANALOG_PTCOMP_MUX_CTB0_OA1_OUT`

```c
#define IFX_AUTANALOG_PTCOMP_MUX_CTB0_OA1_OUT 9
```

CTB0 的运算放大器 1 输出（OpAmp1 Output）。

<a id="a89a79c5fb40ccc444c76a22e9df1473e"></a>

### `IFX_AUTANALOG_PTCOMP_MUX_CTB0_PIN1`

```c
#define IFX_AUTANALOG_PTCOMP_MUX_CTB0_PIN1 0
```

CTB0 的 GPIO 引脚（Pin）1。

<a id="a62ddf951adb5ffda5d97879dc003d485"></a>

### `IFX_AUTANALOG_PTCOMP_MUX_CTB0_PIN4`

```c
#define IFX_AUTANALOG_PTCOMP_MUX_CTB0_PIN4 1
```

CTB0 的 GPIO 引脚（Pin）4。

<a id="a8dd86eae5d4e5a58f50ab41277117775"></a>

### `IFX_AUTANALOG_PTCOMP_MUX_CTB0_PIN6`

```c
#define IFX_AUTANALOG_PTCOMP_MUX_CTB0_PIN6 2
```

CTB0 的 GPIO 引脚（Pin）6。

<a id="a1073f9578281cb466a17d0e901a793e2"></a>

### `IFX_AUTANALOG_PTCOMP_MUX_CTB0_PIN7`

```c
#define IFX_AUTANALOG_PTCOMP_MUX_CTB0_PIN7 3
```

CTB0 的 GPIO 引脚（Pin）7。

<a id="aa6a8e541333fea50dc73fc06be8f3df1"></a>

### `IFX_AUTANALOG_PTCOMP_MUX_CTB1_OA0_OUT`

```c
#define IFX_AUTANALOG_PTCOMP_MUX_CTB1_OA0_OUT 10
```

CTB1 的运算放大器 0 输出（OpAmp0 Output）。

<a id="ad3974446d217a168a866abf3c0d3e10b"></a>

### `IFX_AUTANALOG_PTCOMP_MUX_CTB1_OA1_OUT`

```c
#define IFX_AUTANALOG_PTCOMP_MUX_CTB1_OA1_OUT 11
```

CTB1 的运算放大器 1 输出（OpAmp1 Output）。

<a id="af3583d95e1eca3e97ca1293d4697899a"></a>

### `IFX_AUTANALOG_PTCOMP_MUX_CTB1_PIN1`

```c
#define IFX_AUTANALOG_PTCOMP_MUX_CTB1_PIN1 4
```

CTB1 的 GPIO 引脚（Pin）1。

<a id="ad840d0c1d51cb2a89104d9fd5c5d8412"></a>

### `IFX_AUTANALOG_PTCOMP_MUX_CTB1_PIN4`

```c
#define IFX_AUTANALOG_PTCOMP_MUX_CTB1_PIN4 5
```

CTB1 的 GPIO 引脚（Pin）4。

<a id="a27e234b8ad9e4bb5c88582cbf43cc433"></a>

### `IFX_AUTANALOG_PTCOMP_MUX_CTB1_PIN6`

```c
#define IFX_AUTANALOG_PTCOMP_MUX_CTB1_PIN6 6
```

CTB1 的 GPIO 引脚（Pin）6。

<a id="a85c1b51011bc8807cdffcab0fc3d2408"></a>

### `IFX_AUTANALOG_PTCOMP_MUX_CTB1_PIN7`

```c
#define IFX_AUTANALOG_PTCOMP_MUX_CTB1_PIN7 7
```

CTB1 的 GPIO 引脚（Pin）7。

<a id="a5c3e4541befd309f4a78e14b484f8c51"></a>

### `IFX_AUTANALOG_PTCOMP_MUX_DAC0`

```c
#define IFX_AUTANALOG_PTCOMP_MUX_DAC0 12
```

DAC0 输出（Output）。

<a id="a64008ae19113150d812ecd2c5c3553c1"></a>

### `IFX_AUTANALOG_PTCOMP_MUX_DAC1`

```c
#define IFX_AUTANALOG_PTCOMP_MUX_DAC1 13
```

DAC1 输出（Output）。

<a id="a726c4a7aa8aafe396420a4b04d02479f"></a>

### `IFX_AUTANALOG_PTCOMP_MUX_GPIO0`

```c
#define IFX_AUTANALOG_PTCOMP_MUX_GPIO0 16
```

GPIO 0。

<a id="a3d3c50a51fe3350bc47a8dc063e1dc20"></a>

### `IFX_AUTANALOG_PTCOMP_MUX_GPIO1`

```c
#define IFX_AUTANALOG_PTCOMP_MUX_GPIO1 17
```

GPIO 1。

<a id="a09bef786d22362a2c0ebd9e9f83a1320"></a>

### `IFX_AUTANALOG_PTCOMP_MUX_GPIO2`

```c
#define IFX_AUTANALOG_PTCOMP_MUX_GPIO2 18
```

GPIO 2。

<a id="a0c7a8068598c13c0e24a1dfd08b0a08b"></a>

### `IFX_AUTANALOG_PTCOMP_MUX_GPIO3`

```c
#define IFX_AUTANALOG_PTCOMP_MUX_GPIO3 19
```

GPIO 3。

<a id="a868d420e9cd0f25c0982a173317b2c35"></a>

### `IFX_AUTANALOG_PTCOMP_MUX_GPIO4`

```c
#define IFX_AUTANALOG_PTCOMP_MUX_GPIO4 20
```

GPIO 4。

<a id="a91d69f0d79f78defc3ee71cb5a0af449"></a>

### `IFX_AUTANALOG_PTCOMP_MUX_GPIO5`

```c
#define IFX_AUTANALOG_PTCOMP_MUX_GPIO5 21
```

GPIO 5。

<a id="a883241de0e0b392628f3521c635d4728"></a>

### `IFX_AUTANALOG_PTCOMP_MUX_GPIO6`

```c
#define IFX_AUTANALOG_PTCOMP_MUX_GPIO6 22
```

GPIO 6。

<a id="a90113dd01a1bbd35f4fec139b4dbd473"></a>

### `IFX_AUTANALOG_PTCOMP_MUX_GPIO7`

```c
#define IFX_AUTANALOG_PTCOMP_MUX_GPIO7 23
```

GPIO 7。

<a id="a8b8125671a7d26ffecfcf43fd155ff60"></a>

### `IFX_AUTANALOG_PTCOMP_MUX_PRB_OUT0`

```c
#define IFX_AUTANALOG_PTCOMP_MUX_PRB_OUT0 14
```

PRB 输出（Output） 0。

<a id="a6dbb59d83d05b656d969a40c064b1a60"></a>

### `IFX_AUTANALOG_PTCOMP_MUX_PRB_OUT1`

```c
#define IFX_AUTANALOG_PTCOMP_MUX_PRB_OUT1 15
```

PRB 输出（Output） 1。

<a id="a2f7ededb25653489ab83ba4b56baa154"></a>

### `IFX_AUTANALOG_PTCOMP_PP_COND_ABOVE`

```c
#define IFX_AUTANALOG_PTCOMP_PP_COND_ABOVE 2
```

结果高于阈值窗口（Threshold Window）。

<a id="a087894c04a05625f5b4441167aa54488"></a>

### `IFX_AUTANALOG_PTCOMP_PP_COND_BELOW`

```c
#define IFX_AUTANALOG_PTCOMP_PP_COND_BELOW 0
```

结果低于阈值窗口（Threshold Window）。

<a id="af01070c224eb3309906eb6fa68603b27"></a>

### `IFX_AUTANALOG_PTCOMP_PP_COND_INSIDE`

```c
#define IFX_AUTANALOG_PTCOMP_PP_COND_INSIDE 1
```

结果位于阈值窗口（Threshold Window）内。

<a id="a2d7d9a7c49ddb2eb7c5b8c50546f2bc8"></a>

### `IFX_AUTANALOG_PTCOMP_PP_COND_OUTSIDE`

```c
#define IFX_AUTANALOG_PTCOMP_PP_COND_OUTSIDE 3
```

结果位于阈值窗口（Threshold Window）外。

<a id="aff496eeaadcbf3f112a25fa5e1a7c599"></a>

### `IFX_AUTANALOG_PTCOMP_PP_FUNC_A`

```c
#define IFX_AUTANALOG_PTCOMP_PP_FUNC_A 0
```

直接传递输入 A（Pass Input A）。

<a id="ab2948309a5ce37089946f496d7ec2971"></a>

### `IFX_AUTANALOG_PTCOMP_PP_FUNC_A_AND_B`

```c
#define IFX_AUTANALOG_PTCOMP_PP_FUNC_A_AND_B 3
```

逻辑运算：A 与 B（A AND B）。

<a id="adce47666a9e5ba735e2bce617c1e754a"></a>

### `IFX_AUTANALOG_PTCOMP_PP_FUNC_A_AND_B_BAR`

```c
#define IFX_AUTANALOG_PTCOMP_PP_FUNC_A_AND_B_BAR 4
```

逻辑运算：A 与非 B（A AND NOT B）。

<a id="a762c962aed9ab6aef86e149d8b34153d"></a>

### `IFX_AUTANALOG_PTCOMP_PP_FUNC_A_BAR`

```c
#define IFX_AUTANALOG_PTCOMP_PP_FUNC_A_BAR 11
```

传递逻辑非 A（NOT A）。

<a id="aa3d0d48b1a9f45162688becc97dfb9db"></a>

### `IFX_AUTANALOG_PTCOMP_PP_FUNC_A_BAR_AND_B`

```c
#define IFX_AUTANALOG_PTCOMP_PP_FUNC_A_BAR_AND_B 1
```

逻辑运算：非 A 与 B（NOT A AND B）。

<a id="a032ea9c1952b4a077340a8c21cf46aaa"></a>

### `IFX_AUTANALOG_PTCOMP_PP_FUNC_A_BAR_OR_B`

```c
#define IFX_AUTANALOG_PTCOMP_PP_FUNC_A_BAR_OR_B 12
```

逻辑运算：非 A 或 B（NOT A OR B）。

<a id="a32a3da377723365791b9b7eabf84b0ac"></a>

### `IFX_AUTANALOG_PTCOMP_PP_FUNC_A_NAND_B`

```c
#define IFX_AUTANALOG_PTCOMP_PP_FUNC_A_NAND_B 13
```

逻辑与非（A NAND B），即 `NOT (A AND B)`。

<a id="a310dcb76dfc574dd53b381e672df7b27"></a>

### `IFX_AUTANALOG_PTCOMP_PP_FUNC_A_NOR_B`

```c
#define IFX_AUTANALOG_PTCOMP_PP_FUNC_A_NOR_B 7
```

逻辑或非（A NOR B），即 `NOT (A OR B)`。

<a id="ac7f6030855748afc21e1d9d46ade3426"></a>

### `IFX_AUTANALOG_PTCOMP_PP_FUNC_A_OR_B`

```c
#define IFX_AUTANALOG_PTCOMP_PP_FUNC_A_OR_B 6
```

逻辑运算：A 或 B（A OR B）。

<a id="a128c14ee3a08bb4a2346a1a3c7065e06"></a>

### `IFX_AUTANALOG_PTCOMP_PP_FUNC_A_OR_B_BAR`

```c
#define IFX_AUTANALOG_PTCOMP_PP_FUNC_A_OR_B_BAR 10
```

逻辑运算：A 或非 B（A OR NOT B）。

<a id="af98d8481e5eef0cf3014899719b20cbd"></a>

### `IFX_AUTANALOG_PTCOMP_PP_FUNC_A_XNOR_B`

```c
#define IFX_AUTANALOG_PTCOMP_PP_FUNC_A_XNOR_B 8
```

逻辑同或（A XNOR B），即 `NOT (A XOR B)`。

<a id="aab2870f9d61e06f225bae4be1dc1291c"></a>

### `IFX_AUTANALOG_PTCOMP_PP_FUNC_A_XOR_B`

```c
#define IFX_AUTANALOG_PTCOMP_PP_FUNC_A_XOR_B 5
```

逻辑运算：A 异或 B（A XOR B）。

<a id="a82caa8189b2fa1b26ba5a0cacca34f73"></a>

### `IFX_AUTANALOG_PTCOMP_PP_FUNC_B`

```c
#define IFX_AUTANALOG_PTCOMP_PP_FUNC_B 2
```

直接传递输入 B（Pass Input B）。

<a id="aa7fade24e47ffbb1397626c48ba0f033"></a>

### `IFX_AUTANALOG_PTCOMP_PP_FUNC_B_BAR`

```c
#define IFX_AUTANALOG_PTCOMP_PP_FUNC_B_BAR 9
```

传递逻辑非 B（NOT B）。

<a id="ab80e2b0e3802b5c19e66893e507d7ac8"></a>

### `IFX_AUTANALOG_PTCOMP_PP_MODE_DIRECT`

```c
#define IFX_AUTANALOG_PTCOMP_PP_MODE_DIRECT 0
```

直接计数器模式（Direct Counter Mode）。

<a id="a2b200d37d26b5301062417630770e2ce"></a>

### `IFX_AUTANALOG_PTCOMP_PP_MODE_FRAME`

```c
#define IFX_AUTANALOG_PTCOMP_PP_MODE_FRAME 1
```

帧计数器模式（Frame Counter Mode）。

<a id="aa6003730a4505aacd4e6b619014a3dfa"></a>

### `IFX_AUTANALOG_PTCOMP_PP_MODE_WINDOW`

```c
#define IFX_AUTANALOG_PTCOMP_PP_MODE_WINDOW 2
```

窗口计数器模式（Window Counter Mode）。

<a id="a66e053c7e354c11537814453279107d8"></a>

### `IFX_AUTANALOG_PTCOMP_PP_SRC_COMP0`

```c
#define IFX_AUTANALOG_PTCOMP_PP_SRC_COMP0 1
```

比较器 0 输出（Comparator 0 Output）。

<a id="a533e0f22932eea1af03af8028155a26c"></a>

### `IFX_AUTANALOG_PTCOMP_PP_SRC_COMP1`

```c
#define IFX_AUTANALOG_PTCOMP_PP_SRC_COMP1 2
```

比较器 1 输出（Comparator 1 Output）。

<a id="a429c6785e1f83121cdcc77402d36903d"></a>

### `IFX_AUTANALOG_PTCOMP_PP_SRC_DISABLED`

```c
#define IFX_AUTANALOG_PTCOMP_PP_SRC_DISABLED 0
```

后处理输入已禁用（Post-processing Input Disabled）。

<a id="afb56deef623a39aee5f9678a4d3767b9"></a>

### `IFX_AUTANALOG_PTCOMP_PP_TYPE_EDGE_BOTH`

```c
#define IFX_AUTANALOG_PTCOMP_PP_TYPE_EDGE_BOTH 3
```

双边沿输入（Both-edge Input）。

<a id="a059f83551f58e84235681c1acdade4dc"></a>

### `IFX_AUTANALOG_PTCOMP_PP_TYPE_EDGE_FALLING`

```c
#define IFX_AUTANALOG_PTCOMP_PP_TYPE_EDGE_FALLING 2
```

下降沿输入（Falling Edge Input）。

<a id="a2a39251c0661754fb5dfa55c466eee4b"></a>

### `IFX_AUTANALOG_PTCOMP_PP_TYPE_EDGE_RISING`

```c
#define IFX_AUTANALOG_PTCOMP_PP_TYPE_EDGE_RISING 1
```

上升沿输入（Rising Edge Input）。

<a id="a25328fe25c5a02485a55ee0d3670d043"></a>

### `IFX_AUTANALOG_PTCOMP_PP_TYPE_LEVEL`

```c
#define IFX_AUTANALOG_PTCOMP_PP_TYPE_LEVEL 0
```

电平敏感输入（Level-sensitive Input）。

<a id="a62596dd57277bc9df5301cad4af63721"></a>

### `IFX_AUTANALOG_PTCOMP_PP_WIN_128`

```c
#define IFX_AUTANALOG_PTCOMP_PP_WIN_128 6
```

窗口大小（Window Size）为 128 个样本。

<a id="ab5cf536162dab59d108dee9946eab18b"></a>

### `IFX_AUTANALOG_PTCOMP_PP_WIN_16`

```c
#define IFX_AUTANALOG_PTCOMP_PP_WIN_16 3
```

窗口大小（Window Size）为 16 个样本。

<a id="a70a4da422609f181e568bb0402448949"></a>

### `IFX_AUTANALOG_PTCOMP_PP_WIN_2`

```c
#define IFX_AUTANALOG_PTCOMP_PP_WIN_2 0
```

窗口大小（Window Size）为 2 个样本。

<a id="ad21b521403e3678fcaea25670bd55594"></a>

### `IFX_AUTANALOG_PTCOMP_PP_WIN_32`

```c
#define IFX_AUTANALOG_PTCOMP_PP_WIN_32 4
```

窗口大小（Window Size）为 32 个样本。

<a id="aee57aab8de54ec22cca0ff19dfeea756"></a>

### `IFX_AUTANALOG_PTCOMP_PP_WIN_4`

```c
#define IFX_AUTANALOG_PTCOMP_PP_WIN_4 1
```

窗口大小（Window Size）为 4 个样本。

<a id="a2a5de60fa514466bd64d53419519dd99"></a>

### `IFX_AUTANALOG_PTCOMP_PP_WIN_64`

```c
#define IFX_AUTANALOG_PTCOMP_PP_WIN_64 5
```

窗口大小（Window Size）为 64 个样本。

<a id="ade18f1a187e678c4bf5df279e061a20d"></a>

### `IFX_AUTANALOG_PTCOMP_PP_WIN_8`

```c
#define IFX_AUTANALOG_PTCOMP_PP_WIN_8 2
```

窗口大小（Window Size）为 8 个样本。

<a id="a6e4dffba51be30f5ea1a34abcdcdd343"></a>

### `IFX_AUTANALOG_PTCOMP_PWR_LP`

```c
#define IFX_AUTANALOG_PTCOMP_PWR_LP 2
```

低功耗模式（Low Power Mode）。

<a id="adea94d8f8ccda38ae4fdee874a2d9169"></a>

### `IFX_AUTANALOG_PTCOMP_PWR_NORMAL`

```c
#define IFX_AUTANALOG_PTCOMP_PWR_NORMAL 3
```

正常功耗模式（Normal Power Mode）。

<a id="a4b1d652b24b48443cc5febd738dea51b"></a>

### `IFX_AUTANALOG_PTCOMP_PWR_OFF`

```c
#define IFX_AUTANALOG_PTCOMP_PWR_OFF 0
```

比较器断电（Comparator Powered Off）。

<a id="a4e6f2e178862981d80a4f2a63b7728cd"></a>

### `IFX_AUTANALOG_PTCOMP_PWR_ULP`

```c
#define IFX_AUTANALOG_PTCOMP_PWR_ULP 1
```

超低功耗模式（Ultra Low Power Mode）。


## 5.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P369_infineon-autanalog-ptcomp.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P004_zephyr__dt-bindings__opamp__infineon-autanalog-ctb.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P006_zephyr__audio__midi.h_文件参考.md)
