---
id: learning.zephyr-docs.api-file-coap-phy-reference.page-5
title: zephyr__dt-bindings__mfd__infineon-hppass.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/infineon-hppass_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_zephyr\_\_dt-bindings\_\_mfd\_\_infineon-hppass.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/infineon-hppass_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Infineon HPPASS Autonomous Controller的设备树绑定常量（Devicetree Binding Constants）。

查看此文件的源码。

<a id="details"></a>

Infineon HPPASS 自主控制器（Autonomous Controller）的设备树绑定（Devicetree Binding）常量。这些常量与外设驱动库（PDL）的枚举值一致，用于配置 AC 状态转换表（State Transition Table）、触发输入（Trigger Input）和触发输出（Trigger Output）的设备树属性。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.1\_宏定义（Macros）

<a id="define-members-0"></a>

### AC状态转换表动作值（AC STT Action values (cy_en_hppass_action_t)）

<a id="r_a0b7f40bcf41715ea0682359b99363b44"></a>

```c
#define IFX_HPPASS_AC_ACTION_STOP 0
```

相关声明：[IFX_HPPASS_AC_ACTION_STOP](#a0b7f40bcf41715ea0682359b99363b44)。

停止自主控制器（AC）。

<a id="r_a33a4aa47f34bdb96f45286702b07a338"></a>

```c
#define IFX_HPPASS_AC_ACTION_NEXT 1
```

相关声明：[IFX_HPPASS_AC_ACTION_NEXT](#a33a4aa47f34bdb96f45286702b07a338)。

进入下一状态（Next State）。

<a id="r_aa357fc61160817b7337ae1a43471c7b5"></a>

```c
#define IFX_HPPASS_AC_ACTION_WAIT_FOR 2
```

相关声明：[IFX_HPPASS_AC_ACTION_WAIT_FOR](#aa357fc61160817b7337ae1a43471c7b5)。

等待条件（CONDITION）变为 TRUE。

<a id="r_aef68f83e90bd0364ef289568350e7a5e"></a>

```c
#define IFX_HPPASS_AC_ACTION_BRANCH_IF_TRUE 3
```

相关声明：[IFX_HPPASS_AC_ACTION_BRANCH_IF_TRUE](#aef68f83e90bd0364ef289568350e7a5e)。

当条件（CONDITION）为 TRUE 时分支跳转。

<a id="r_a53dc97f59e5eca1a75286255580d3ebc"></a>

```c
#define IFX_HPPASS_AC_ACTION_BRANCH_IF_FALSE 4
```

相关声明：[IFX_HPPASS_AC_ACTION_BRANCH_IF_FALSE](#a53dc97f59e5eca1a75286255580d3ebc)。

当条件（CONDITION）为 FALSE 时分支跳转。

<a id="define-members-1"></a>

### AC状态转换表条件值（AC STT Condition values (cy_en_hppass_condition_t)）

<a id="r_ab3b9458cadd0b2a889bf54c7734ee339"></a>

```c
#define IFX_HPPASS_AC_COND_FALSE 0
```

相关声明：[IFX_HPPASS_AC_COND_FALSE](#ab3b9458cadd0b2a889bf54c7734ee339)。

无条件为 FALSE。

<a id="r_a13cde63a5e1672be493df30c37412f5e"></a>

```c
#define IFX_HPPASS_AC_COND_TRUE 1
```

相关声明：[IFX_HPPASS_AC_COND_TRUE](#a13cde63a5e1672be493df30c37412f5e)。

无条件为 TRUE。

<a id="r_a4276da517b99f69f6dfef03bdd88e4ca"></a>

```c
#define IFX_HPPASS_AC_COND_BLOCK_READY 2
```

相关声明：[IFX_HPPASS_AC_COND_BLOCK_READY](#a4276da517b99f69f6dfef03bdd88e4ca)。

已启用的 SAR／CSG 模块就绪（Ready）。

<a id="r_a8470f5a7274e702869b2d8b099ac2cb6"></a>

```c
#define IFX_HPPASS_AC_COND_CNT_DONE 3
```

相关声明：[IFX_HPPASS_AC_COND_CNT_DONE](#a8470f5a7274e702869b2d8b099ac2cb6)。

定时器／计数器（Timer / Counter）计数到期。

<a id="r_a93fc924ff57330ed1dda461a3bdb3074"></a>

```c
#define IFX_HPPASS_AC_COND_SAR_GROUP_0_DONE 4
```

相关声明：[IFX_HPPASS_AC_COND_SAR_GROUP_0_DONE](#a93fc924ff57330ed1dda461a3bdb3074)。

逐次逼近（SAR）组 0 完成（Done）。

<a id="r_acb0c847ff8bc0e57fb7f92fbbdbaa824"></a>

```c
#define IFX_HPPASS_AC_COND_SAR_GROUP_1_DONE 5
```

相关声明：[IFX_HPPASS_AC_COND_SAR_GROUP_1_DONE](#acb0c847ff8bc0e57fb7f92fbbdbaa824)。

逐次逼近（SAR）组 1 完成（Done）。

<a id="r_ae24c0996092d4e28d0668513fd05ff8c"></a>

```c
#define IFX_HPPASS_AC_COND_SAR_GROUP_2_DONE 6
```

相关声明：[IFX_HPPASS_AC_COND_SAR_GROUP_2_DONE](#ae24c0996092d4e28d0668513fd05ff8c)。

逐次逼近（SAR）组 2 完成（Done）。

<a id="r_ad7b08b94e7877df73db6850b2b623737"></a>

```c
#define IFX_HPPASS_AC_COND_SAR_GROUP_3_DONE 7
```

相关声明：[IFX_HPPASS_AC_COND_SAR_GROUP_3_DONE](#ad7b08b94e7877df73db6850b2b623737)。

逐次逼近（SAR）组 3 完成（Done）。

<a id="r_a74a9cf6491c8d8b5db437e5c06a914f1"></a>

```c
#define IFX_HPPASS_AC_COND_SAR_GROUP_4_DONE 8
```

相关声明：[IFX_HPPASS_AC_COND_SAR_GROUP_4_DONE](#a74a9cf6491c8d8b5db437e5c06a914f1)。

逐次逼近（SAR）组 4 完成（Done）。

<a id="r_acca9519de4a76866c69d109b4d589572"></a>

```c
#define IFX_HPPASS_AC_COND_SAR_GROUP_5_DONE 9
```

相关声明：[IFX_HPPASS_AC_COND_SAR_GROUP_5_DONE](#acca9519de4a76866c69d109b4d589572)。

逐次逼近（SAR）组 5 完成（Done）。

<a id="r_a54192c1f3be2e1082fc96aa082b84264"></a>

```c
#define IFX_HPPASS_AC_COND_SAR_GROUP_6_DONE 10
```

相关声明：[IFX_HPPASS_AC_COND_SAR_GROUP_6_DONE](#a54192c1f3be2e1082fc96aa082b84264)。

逐次逼近（SAR）组 6 完成（Done）。

<a id="r_a177afc1a0d96c25d40bcc510f62c5919"></a>

```c
#define IFX_HPPASS_AC_COND_SAR_GROUP_7_DONE 11
```

相关声明：[IFX_HPPASS_AC_COND_SAR_GROUP_7_DONE](#a177afc1a0d96c25d40bcc510f62c5919)。

逐次逼近（SAR）组 7 完成（Done）。

<a id="r_ac918d0c11a408998020fd268e3cf206d"></a>

```c
#define IFX_HPPASS_AC_COND_SAR_LIMIT_0 12
```

相关声明：[IFX_HPPASS_AC_COND_SAR_LIMIT_0](#ac918d0c11a408998020fd268e3cf206d)。

逐次逼近（SAR）限值检测器（Limit Detector）0。

<a id="r_a1c304b54ccec00ff4da421e63c72b49a"></a>

```c
#define IFX_HPPASS_AC_COND_SAR_LIMIT_1 13
```

相关声明：[IFX_HPPASS_AC_COND_SAR_LIMIT_1](#a1c304b54ccec00ff4da421e63c72b49a)。

逐次逼近（SAR）限值检测器（Limit Detector）1。

<a id="r_a2b0a8917bbb0839dd4d645d8131338ac"></a>

```c
#define IFX_HPPASS_AC_COND_SAR_LIMIT_2 14
```

相关声明：[IFX_HPPASS_AC_COND_SAR_LIMIT_2](#a2b0a8917bbb0839dd4d645d8131338ac)。

逐次逼近（SAR）限值检测器（Limit Detector）2。

<a id="r_a2743add8eaa21fa94bb7a1d42f7b7489"></a>

```c
#define IFX_HPPASS_AC_COND_SAR_LIMIT_3 15
```

相关声明：[IFX_HPPASS_AC_COND_SAR_LIMIT_3](#a2743add8eaa21fa94bb7a1d42f7b7489)。

逐次逼近（SAR）限值检测器（Limit Detector）3。

<a id="r_a8141384f3dec367a88ba7b67c034a7ed"></a>

```c
#define IFX_HPPASS_AC_COND_SAR_LIMIT_4 16
```

相关声明：[IFX_HPPASS_AC_COND_SAR_LIMIT_4](#a8141384f3dec367a88ba7b67c034a7ed)。

逐次逼近（SAR）限值检测器（Limit Detector）4。

<a id="r_a4c101ae981deac8cc2ba58bb7c07249c"></a>

```c
#define IFX_HPPASS_AC_COND_SAR_LIMIT_5 17
```

相关声明：[IFX_HPPASS_AC_COND_SAR_LIMIT_5](#a4c101ae981deac8cc2ba58bb7c07249c)。

逐次逼近（SAR）限值检测器（Limit Detector）5。

<a id="r_ac7ccd9ddc6e4727955eb8c127b1df9a6"></a>

```c
#define IFX_HPPASS_AC_COND_SAR_LIMIT_6 18
```

相关声明：[IFX_HPPASS_AC_COND_SAR_LIMIT_6](#ac7ccd9ddc6e4727955eb8c127b1df9a6)。

逐次逼近（SAR）限值检测器（Limit Detector）6。

<a id="r_aef3f8780c34d41b6cf54852966e80828"></a>

```c
#define IFX_HPPASS_AC_COND_SAR_LIMIT_7 19
```

相关声明：[IFX_HPPASS_AC_COND_SAR_LIMIT_7](#aef3f8780c34d41b6cf54852966e80828)。

逐次逼近（SAR）限值检测器（Limit Detector）7。

<a id="r_a525958c4634dc0592c26d5ab6c48e15b"></a>

```c
#define IFX_HPPASS_AC_COND_SAR_BUSY 20
```

相关声明：[IFX_HPPASS_AC_COND_SAR_BUSY](#a525958c4634dc0592c26d5ab6c48e15b)。

逐次逼近（SAR）模块忙。

<a id="r_aea00068d3c695b20b567062975b2c596"></a>

```c
#define IFX_HPPASS_AC_COND_SAR_FIR_0_DONE 21
```

相关声明：[IFX_HPPASS_AC_COND_SAR_FIR_0_DONE](#aea00068d3c695b20b567062975b2c596)。

SAR 有限脉冲响应滤波器（FIR）0 完成。

<a id="r_a471cb11613962c711c0f47da3b36365f"></a>

```c
#define IFX_HPPASS_AC_COND_SAR_FIR_1_DONE 22
```

相关声明：[IFX_HPPASS_AC_COND_SAR_FIR_1_DONE](#a471cb11613962c711c0f47da3b36365f)。

SAR 有限脉冲响应滤波器（FIR）1 完成。

<a id="r_afee978a8ff21eed80bbb76aa52774bcf"></a>

```c
#define IFX_HPPASS_AC_COND_SAR_QUEUE_HI_EMPTY 23
```

相关声明：[IFX_HPPASS_AC_COND_SAR_QUEUE_HI_EMPTY](#afee978a8ff21eed80bbb76aa52774bcf)。

SAR 高优先级队列（High-priority Queue）为空。

<a id="r_a8a9add025dafe8314071b5af90f6ce6c"></a>

```c
#define IFX_HPPASS_AC_COND_SAR_QUEUE_LO_EMPTY 24
```

相关声明：[IFX_HPPASS_AC_COND_SAR_QUEUE_LO_EMPTY](#a8a9add025dafe8314071b5af90f6ce6c)。

SAR 低优先级队列（Low-priority Queue）为空。

<a id="r_ab057818da3f100849eb795c6dead4f46"></a>

```c
#define IFX_HPPASS_AC_COND_SAR_QUEUES_EMPTY 25
```

相关声明：[IFX_HPPASS_AC_COND_SAR_QUEUES_EMPTY](#ab057818da3f100849eb795c6dead4f46)。

SAR 的两个队列（Queue）均为空。

<a id="r_afadf2ef74d8d9bb1d1e5c8c24e3688a9"></a>

```c
#define IFX_HPPASS_AC_COND_TRIG_0 32
```

相关声明：[IFX_HPPASS_AC_COND_TRIG_0](#afadf2ef74d8d9bb1d1e5c8c24e3688a9)。

硬件／固件触发（HW/FW Trigger）0。

<a id="r_a65a62776f37a4db53b3f5f60bd6dbb91"></a>

```c
#define IFX_HPPASS_AC_COND_TRIG_1 33
```

相关声明：[IFX_HPPASS_AC_COND_TRIG_1](#a65a62776f37a4db53b3f5f60bd6dbb91)。

硬件／固件触发（HW/FW Trigger）1。

<a id="r_a1b29317b9826693ef5608491bf01b599"></a>

```c
#define IFX_HPPASS_AC_COND_TRIG_2 34
```

相关声明：[IFX_HPPASS_AC_COND_TRIG_2](#a1b29317b9826693ef5608491bf01b599)。

硬件／固件触发（HW/FW Trigger）2。

<a id="r_aee658692cdc1760964673d917ff8197d"></a>

```c
#define IFX_HPPASS_AC_COND_TRIG_3 35
```

相关声明：[IFX_HPPASS_AC_COND_TRIG_3](#aee658692cdc1760964673d917ff8197d)。

硬件／固件触发（HW/FW Trigger）3。

<a id="r_a4d28591c81cfe48ac2a86b09e4e031af"></a>

```c
#define IFX_HPPASS_AC_COND_TRIG_4 36
```

相关声明：[IFX_HPPASS_AC_COND_TRIG_4](#a4d28591c81cfe48ac2a86b09e4e031af)。

硬件／固件触发（HW/FW Trigger）4。

<a id="r_a70fb58679230267ec373c07ac185ccac"></a>

```c
#define IFX_HPPASS_AC_COND_TRIG_5 37
```

相关声明：[IFX_HPPASS_AC_COND_TRIG_5](#a70fb58679230267ec373c07ac185ccac)。

硬件／固件触发（HW/FW Trigger）5。

<a id="r_a019314e9b5e1555c1dca7ffae538575a"></a>

```c
#define IFX_HPPASS_AC_COND_TRIG_6 38
```

相关声明：[IFX_HPPASS_AC_COND_TRIG_6](#a019314e9b5e1555c1dca7ffae538575a)。

硬件／固件触发（HW/FW Trigger）6。

<a id="r_a2e0ce849306bdf52776bb2afd1abea0a"></a>

```c
#define IFX_HPPASS_AC_COND_TRIG_7 39
```

相关声明：[IFX_HPPASS_AC_COND_TRIG_7](#a2e0ce849306bdf52776bb2afd1abea0a)。

硬件／固件触发（HW/FW Trigger）7。

<a id="r_a3e3e96b8d5a39db52ecea685194a1296"></a>

```c
#define IFX_HPPASS_AC_COND_FIFO_0_LEVEL 42
```

相关声明：[IFX_HPPASS_AC_COND_FIFO_0_LEVEL](#a3e3e96b8d5a39db52ecea685194a1296)。

FIFO 水位（Level）0。

<a id="r_a5d4e6605907cad460acc9a6fd79fc79f"></a>

```c
#define IFX_HPPASS_AC_COND_FIFO_1_LEVEL 43
```

相关声明：[IFX_HPPASS_AC_COND_FIFO_1_LEVEL](#a5d4e6605907cad460acc9a6fd79fc79f)。

FIFO 水位（Level）1。

<a id="r_a5918287d031867bd20394f3121ea16ad"></a>

```c
#define IFX_HPPASS_AC_COND_FIFO_2_LEVEL 44
```

相关声明：[IFX_HPPASS_AC_COND_FIFO_2_LEVEL](#a5918287d031867bd20394f3121ea16ad)。

FIFO 水位（Level）2。

<a id="r_a3d627f0183f20b32b57408a99fc70a88"></a>

```c
#define IFX_HPPASS_AC_COND_FIFO_3_LEVEL 45
```

相关声明：[IFX_HPPASS_AC_COND_FIFO_3_LEVEL](#a3d627f0183f20b32b57408a99fc70a88)。

FIFO 水位（Level）3。

<a id="r_afc19d5fc19776308e39fc63da0330635"></a>

```c
#define IFX_HPPASS_AC_COND_CSG_0_DAC_DONE 48
```

相关声明：[IFX_HPPASS_AC_COND_CSG_0_DAC_DONE](#afc19d5fc19776308e39fc63da0330635)。

CSG0 的 DAC 波形完成（Waveform Done）。

<a id="r_ade32923b770bf9d2ffdf6b33e7c78c97"></a>

```c
#define IFX_HPPASS_AC_COND_CSG_1_DAC_DONE 49
```

相关声明：[IFX_HPPASS_AC_COND_CSG_1_DAC_DONE](#ade32923b770bf9d2ffdf6b33e7c78c97)。

CSG1 的 DAC 波形完成（Waveform Done）。

<a id="r_a19612ce34694a1560210310f70cd241b"></a>

```c
#define IFX_HPPASS_AC_COND_CSG_2_DAC_DONE 50
```

相关声明：[IFX_HPPASS_AC_COND_CSG_2_DAC_DONE](#a19612ce34694a1560210310f70cd241b)。

CSG2 的 DAC 波形完成（Waveform Done）。

<a id="r_a991f1569ca3990c6d22f590566df0944"></a>

```c
#define IFX_HPPASS_AC_COND_CSG_3_DAC_DONE 51
```

相关声明：[IFX_HPPASS_AC_COND_CSG_3_DAC_DONE](#a991f1569ca3990c6d22f590566df0944)。

CSG3 的 DAC 波形完成（Waveform Done）。

<a id="r_a52e7032988171863547953f1157c3370"></a>

```c
#define IFX_HPPASS_AC_COND_CSG_4_DAC_DONE 52
```

相关声明：[IFX_HPPASS_AC_COND_CSG_4_DAC_DONE](#a52e7032988171863547953f1157c3370)。

CSG4 的 DAC 波形完成（Waveform Done）。

<a id="r_ad61d2959a481504656cb0ea63936d17b"></a>

```c
#define IFX_HPPASS_AC_COND_CSG_0_COMP 56
```

相关声明：[IFX_HPPASS_AC_COND_CSG_0_COMP](#ad61d2959a481504656cb0ea63936d17b)。

CSG0 比较器触发（Comparator Trip）。

<a id="r_a6e895d0472b5050eeb80b4f65a543478"></a>

```c
#define IFX_HPPASS_AC_COND_CSG_1_COMP 57
```

相关声明：[IFX_HPPASS_AC_COND_CSG_1_COMP](#a6e895d0472b5050eeb80b4f65a543478)。

CSG1 比较器触发（Comparator Trip）。

<a id="r_aa7c05cbbba28b8fb6828be608dc7cb38"></a>

```c
#define IFX_HPPASS_AC_COND_CSG_2_COMP 58
```

相关声明：[IFX_HPPASS_AC_COND_CSG_2_COMP](#aa7c05cbbba28b8fb6828be608dc7cb38)。

CSG2 比较器触发（Comparator Trip）。

<a id="r_a0a47a9cd96c4ef67b282d04f905d5ee6"></a>

```c
#define IFX_HPPASS_AC_COND_CSG_3_COMP 59
```

相关声明：[IFX_HPPASS_AC_COND_CSG_3_COMP](#a0a47a9cd96c4ef67b282d04f905d5ee6)。

CSG3 比较器触发（Comparator Trip）。

<a id="r_a8d0064477d07613a6af061fbd3f39624"></a>

```c
#define IFX_HPPASS_AC_COND_CSG_4_COMP 60
```

相关声明：[IFX_HPPASS_AC_COND_CSG_4_COMP](#a8d0064477d07613a6af061fbd3f39624)。

CSG4 比较器触发（Comparator Trip）。

<a id="define-members-2"></a>

### AC GPIO输出掩码（AC GPIO output masks (CY_HPPASS_GPIO_OUT_*)）

<a id="r_ac8a3b9a068927e3af0ad26b721743255"></a>

```c
#define IFX_HPPASS_GPIO_OUT_0 0x01
```

相关声明：[IFX_HPPASS_GPIO_OUT_0](#ac8a3b9a068927e3af0ad26b721743255)。

GPIO 输出（Output）0。

<a id="r_a863783df68d608b3e26a89067dc77444"></a>

```c
#define IFX_HPPASS_GPIO_OUT_1 0x02
```

相关声明：[IFX_HPPASS_GPIO_OUT_1](#a863783df68d608b3e26a89067dc77444)。

GPIO 输出（Output）1。

<a id="r_abf19cfdb971b7033e4e64735947ce149"></a>

```c
#define IFX_HPPASS_GPIO_OUT_2 0x04
```

相关声明：[IFX_HPPASS_GPIO_OUT_2](#abf19cfdb971b7033e4e64735947ce149)。

GPIO 输出（Output）2。

<a id="r_ae698a880e8f08f3433700f5f2c0a31b9"></a>

```c
#define IFX_HPPASS_GPIO_OUT_3 0x08
```

相关声明：[IFX_HPPASS_GPIO_OUT_3](#ae698a880e8f08f3433700f5f2c0a31b9)。

GPIO 输出（Output）3。

<a id="r_ab789f6fa2a711f8e83de11142a53fbb9"></a>

```c
#define IFX_HPPASS_GPIO_OUT_4 0x10
```

相关声明：[IFX_HPPASS_GPIO_OUT_4](#ab789f6fa2a711f8e83de11142a53fbb9)。

GPIO 输出（Output）4。

<a id="define-members-3"></a>

### SAR序列控制器组触发掩码（SAR sequencer group trigger masks (CY_HPPASS_SEQ_GRP_*_TRIG)）

<a id="r_ab71b60fe89af462eb704310f62ef0d14"></a>

```c
#define IFX_HPPASS_SAR_GRP_0 0x01
```

相关声明：[IFX_HPPASS_SAR_GRP_0](#ab71b60fe89af462eb704310f62ef0d14)。

逐次逼近（SAR）组 0 触发（Trigger）。

<a id="r_ac10db27f7d1dd79728bd7873b29436c2"></a>

```c
#define IFX_HPPASS_SAR_GRP_1 0x02
```

相关声明：[IFX_HPPASS_SAR_GRP_1](#ac10db27f7d1dd79728bd7873b29436c2)。

逐次逼近（SAR）组 1 触发（Trigger）。

<a id="r_a3473c526c36eb5c9d48cbab6c6cb8516"></a>

```c
#define IFX_HPPASS_SAR_GRP_2 0x04
```

相关声明：[IFX_HPPASS_SAR_GRP_2](#a3473c526c36eb5c9d48cbab6c6cb8516)。

逐次逼近（SAR）组 2 触发（Trigger）。

<a id="r_acb18956d8bc5b6a1ce421d9781feb2c2"></a>

```c
#define IFX_HPPASS_SAR_GRP_3 0x08
```

相关声明：[IFX_HPPASS_SAR_GRP_3](#acb18956d8bc5b6a1ce421d9781feb2c2)。

逐次逼近（SAR）组 3 触发（Trigger）。

<a id="r_a636e15d6579a987b52b888b2c3feb083"></a>

```c
#define IFX_HPPASS_SAR_GRP_4 0x10
```

相关声明：[IFX_HPPASS_SAR_GRP_4](#a636e15d6579a987b52b888b2c3feb083)。

逐次逼近（SAR）组 4 触发（Trigger）。

<a id="r_a04e25afb83c0d24fcab2ee67e52dac48"></a>

```c
#define IFX_HPPASS_SAR_GRP_5 0x20
```

相关声明：[IFX_HPPASS_SAR_GRP_5](#a04e25afb83c0d24fcab2ee67e52dac48)。

逐次逼近（SAR）组 5 触发（Trigger）。

<a id="r_a7eb7b226c512990e319985ba2d034f23"></a>

```c
#define IFX_HPPASS_SAR_GRP_6 0x40
```

相关声明：[IFX_HPPASS_SAR_GRP_6](#a7eb7b226c512990e319985ba2d034f23)。

逐次逼近（SAR）组 6 触发（Trigger）。

<a id="r_a2f0da8676ea92c8c19f712406fb0efd0"></a>

```c
#define IFX_HPPASS_SAR_GRP_7 0x80
```

相关声明：[IFX_HPPASS_SAR_GRP_7](#a2f0da8676ea92c8c19f712406fb0efd0)。

逐次逼近（SAR）组 7 触发（Trigger）。

<a id="define-members-4"></a>

### 触发输入类型（Trigger input type (cy_en_hppass_trig_t)）

<a id="r_a0d7693c705dc2b9cbdac113ab92d748f"></a>

```c
#define IFX_HPPASS_TR_DISABLED 0
```

相关声明：[IFX_HPPASS_TR_DISABLED](#a0d7693c705dc2b9cbdac113ab92d748f)。

关闭触发（Trigger）。

<a id="r_a2acd3f95ea33686b464f92ac65f52568"></a>

```c
#define IFX_HPPASS_TR_HW_A 1
```

相关声明：[IFX_HPPASS_TR_HW_A](#a2acd3f95ea33686b464f92ac65f52568)。

外部硬件触发（External HW Trigger）A。

<a id="r_a8c659cfb4dc0df7785dfc7271f09aa9d"></a>

```c
#define IFX_HPPASS_TR_HW_B 2
```

相关声明：[IFX_HPPASS_TR_HW_B](#a8c659cfb4dc0df7785dfc7271f09aa9d)。

外部硬件触发（External HW Trigger）B。

<a id="r_ad36a3082b34024ce88acfbfb276c6ec9"></a>

```c
#define IFX_HPPASS_TR_FW_PULSE 3
```

相关声明：[IFX_HPPASS_TR_FW_PULSE](#ad36a3082b34024ce88acfbfb276c6ec9)。

固件脉冲触发（FW Pulse Trigger）。

<a id="r_ad6d32ca98bf7b8bdf18cc473fdc73d78"></a>

```c
#define IFX_HPPASS_TR_FW_LEVEL 4
```

相关声明：[IFX_HPPASS_TR_FW_LEVEL](#ad6d32ca98bf7b8bdf18cc473fdc73d78)。

固件电平触发（FW Level Trigger）。

<a id="define-members-5"></a>

### 触发硬件模式（Trigger HW mode (cy_en_hppass_trig_hw_t)）

<a id="r_ae2567f36992250f78edd5e04179e0601"></a>

```c
#define IFX_HPPASS_TR_HW_PULSE_POS_DSYNC 0
```

相关声明：[IFX_HPPASS_TR_HW_PULSE_POS_DSYNC](#ae2567f36992250f78edd5e04179e0601)。

异步（Async），双级同步（Double-sync），在上升沿产生脉冲。

<a id="r_a6751ae17ea6de662b276c6f6da7aece6"></a>

```c
#define IFX_HPPASS_TR_HW_PULSE_NEG_DSYNC 1
```

相关声明：[IFX_HPPASS_TR_HW_PULSE_NEG_DSYNC](#a6751ae17ea6de662b276c6f6da7aece6)。

异步（Async），双级同步（Double-sync），在下降沿产生脉冲。

<a id="r_a5decef62cdb66546d5f66f6002f9a0e0"></a>

```c
#define IFX_HPPASS_TR_HW_PULSE_BOTH_DSYNC 2
```

相关声明：[IFX_HPPASS_TR_HW_PULSE_BOTH_DSYNC](#a5decef62cdb66546d5f66f6002f9a0e0)。

异步（Async），双级同步（Double-sync），在双边沿产生脉冲。

<a id="r_a99c62b3de709116397279502fbac9dc5"></a>

```c
#define IFX_HPPASS_TR_HW_LEVEL_DSYNC 3
```

相关声明：[IFX_HPPASS_TR_HW_LEVEL_DSYNC](#a99c62b3de709116397279502fbac9dc5)。

异步（Async），双级同步（Double-sync），电平触发（Level Trigger）。

<a id="r_aa5d1779a119701a6a6df4c4d11700625"></a>

```c
#define IFX_HPPASS_TR_HW_PULSE_POS_SSYNC 4
```

相关声明：[IFX_HPPASS_TR_HW_PULSE_POS_SSYNC](#aa5d1779a119701a6a6df4c4d11700625)。

同步（Sync），在上升沿产生脉冲。

<a id="r_ab752b691d9e8ffc2d4cfb0b252c53d61"></a>

```c
#define IFX_HPPASS_TR_HW_PULSE_NEG_SSYNC 5
```

相关声明：[IFX_HPPASS_TR_HW_PULSE_NEG_SSYNC](#ab752b691d9e8ffc2d4cfb0b252c53d61)。

同步（Sync），在下降沿产生脉冲。

<a id="r_a3a5b83bf3222915e24696f9bc033af66"></a>

```c
#define IFX_HPPASS_TR_HW_PULSE_BOTH_SSYNC 6
```

相关声明：[IFX_HPPASS_TR_HW_PULSE_BOTH_SSYNC](#a3a5b83bf3222915e24696f9bc033af66)。

同步（Sync），在双边沿产生脉冲。

<a id="r_a0170a4bfdf89da9417472147b56db7d4"></a>

```c
#define IFX_HPPASS_TR_HW_LEVEL_SSYNC 7
```

相关声明：[IFX_HPPASS_TR_HW_LEVEL_SSYNC](#a0170a4bfdf89da9417472147b56db7d4)。

同步（Sync），电平触发（Level Trigger）。

<a id="define-members-6"></a>

### 触发输出脉冲源（Trigger output pulse source (cy_en_hppass_trig_out_pulse_t)）

<a id="r_a48155ee043d177e898ef9ec4e79554f3"></a>

```c
#define IFX_HPPASS_TR_OUT_DISABLED 0
```

相关声明：[IFX_HPPASS_TR_OUT_DISABLED](#a48155ee043d177e898ef9ec4e79554f3)。

禁用触发输出（Trigger Output）。

<a id="r_a603a002173a92becfa54b8c7a6e62c6e"></a>

```c
#define IFX_HPPASS_TR_OUT_SAR_GROUP_0 1
```

相关声明：[IFX_HPPASS_TR_OUT_SAR_GROUP_0](#a603a002173a92becfa54b8c7a6e62c6e)。

逐次逼近（SAR）组 0 完成（Done）。

<a id="r_ad8f8931d4afe4a6bf0c74d004c68612a"></a>

```c
#define IFX_HPPASS_TR_OUT_SAR_GROUP_1 2
```

相关声明：[IFX_HPPASS_TR_OUT_SAR_GROUP_1](#ad8f8931d4afe4a6bf0c74d004c68612a)。

逐次逼近（SAR）组 1 完成（Done）。

<a id="r_a68375c65bdb1a9a0b0f91b1c9f3e6419"></a>

```c
#define IFX_HPPASS_TR_OUT_SAR_GROUP_2 3
```

相关声明：[IFX_HPPASS_TR_OUT_SAR_GROUP_2](#a68375c65bdb1a9a0b0f91b1c9f3e6419)。

逐次逼近（SAR）组 2 完成（Done）。

<a id="r_a432c2a388b08ae7c323fac2b04757a99"></a>

```c
#define IFX_HPPASS_TR_OUT_SAR_GROUP_3 4
```

相关声明：[IFX_HPPASS_TR_OUT_SAR_GROUP_3](#a432c2a388b08ae7c323fac2b04757a99)。

逐次逼近（SAR）组 3 完成（Done）。

<a id="r_a41fd5c0d13a95fab2b16168bed94facf"></a>

```c
#define IFX_HPPASS_TR_OUT_SAR_GROUP_4 5
```

相关声明：[IFX_HPPASS_TR_OUT_SAR_GROUP_4](#a41fd5c0d13a95fab2b16168bed94facf)。

逐次逼近（SAR）组 4 完成（Done）。

<a id="r_a1cd972a20688d0d18b90c4c0256fcae2"></a>

```c
#define IFX_HPPASS_TR_OUT_SAR_GROUP_5 6
```

相关声明：[IFX_HPPASS_TR_OUT_SAR_GROUP_5](#a1cd972a20688d0d18b90c4c0256fcae2)。

逐次逼近（SAR）组 5 完成（Done）。

<a id="r_a2b87a40b41f7bb1c34e163c3d110c79d"></a>

```c
#define IFX_HPPASS_TR_OUT_SAR_GROUP_6 7
```

相关声明：[IFX_HPPASS_TR_OUT_SAR_GROUP_6](#a2b87a40b41f7bb1c34e163c3d110c79d)。

逐次逼近（SAR）组 6 完成（Done）。

<a id="r_a1c3a8794d147bdd0de980e0aa44b4923"></a>

```c
#define IFX_HPPASS_TR_OUT_SAR_GROUP_7 8
```

相关声明：[IFX_HPPASS_TR_OUT_SAR_GROUP_7](#a1c3a8794d147bdd0de980e0aa44b4923)。

逐次逼近（SAR）组 7 完成（Done）。

<a id="r_a9db6f1f3a816008f430d5e1752513089"></a>

```c
#define IFX_HPPASS_TR_OUT_FIR_0 9
```

相关声明：[IFX_HPPASS_TR_OUT_FIR_0](#a9db6f1f3a816008f430d5e1752513089)。

有限脉冲响应滤波器（FIR）0 完成（Done）。

<a id="r_a05dd2a8af999198347a4456b48a223d5"></a>

```c
#define IFX_HPPASS_TR_OUT_FIR_1 10
```

相关声明：[IFX_HPPASS_TR_OUT_FIR_1](#a05dd2a8af999198347a4456b48a223d5)。

有限脉冲响应滤波器（FIR）1 完成（Done）。

<a id="r_a0758c112427a09fcb517059ed10a4c82"></a>

```c
#define IFX_HPPASS_TR_OUT_AC 11
```

相关声明：[IFX_HPPASS_TR_OUT_AC](#a0758c112427a09fcb517059ed10a4c82)。

自主控制器触发输出（AC Trigger Output）。

## 5.2\_详细说明（Detailed Documentation）

<a id="a53dc97f59e5eca1a75286255580d3ebc"></a>

### `IFX_HPPASS_AC_ACTION_BRANCH_IF_FALSE`

```c
#define IFX_HPPASS_AC_ACTION_BRANCH_IF_FALSE 4
```

当条件（CONDITION）为 FALSE 时分支跳转。

<a id="aef68f83e90bd0364ef289568350e7a5e"></a>

### `IFX_HPPASS_AC_ACTION_BRANCH_IF_TRUE`

```c
#define IFX_HPPASS_AC_ACTION_BRANCH_IF_TRUE 3
```

当条件（CONDITION）为 TRUE 时分支跳转。

<a id="a33a4aa47f34bdb96f45286702b07a338"></a>

### `IFX_HPPASS_AC_ACTION_NEXT`

```c
#define IFX_HPPASS_AC_ACTION_NEXT 1
```

进入下一状态（Next State）。

<a id="a0b7f40bcf41715ea0682359b99363b44"></a>

### `IFX_HPPASS_AC_ACTION_STOP`

```c
#define IFX_HPPASS_AC_ACTION_STOP 0
```

停止自主控制器（AC）。

<a id="aa357fc61160817b7337ae1a43471c7b5"></a>

### `IFX_HPPASS_AC_ACTION_WAIT_FOR`

```c
#define IFX_HPPASS_AC_ACTION_WAIT_FOR 2
```

等待条件（CONDITION）变为 TRUE。

<a id="a4276da517b99f69f6dfef03bdd88e4ca"></a>

### `IFX_HPPASS_AC_COND_BLOCK_READY`

```c
#define IFX_HPPASS_AC_COND_BLOCK_READY 2
```

已启用的 SAR／CSG 模块就绪（Ready）。

<a id="a8470f5a7274e702869b2d8b099ac2cb6"></a>

### `IFX_HPPASS_AC_COND_CNT_DONE`

```c
#define IFX_HPPASS_AC_COND_CNT_DONE 3
```

定时器／计数器（Timer / Counter）计数到期。

<a id="ad61d2959a481504656cb0ea63936d17b"></a>

### `IFX_HPPASS_AC_COND_CSG_0_COMP`

```c
#define IFX_HPPASS_AC_COND_CSG_0_COMP 56
```

CSG0 比较器触发（Comparator Trip）。

<a id="afc19d5fc19776308e39fc63da0330635"></a>

### `IFX_HPPASS_AC_COND_CSG_0_DAC_DONE`

```c
#define IFX_HPPASS_AC_COND_CSG_0_DAC_DONE 48
```

CSG0 的 DAC 波形完成（Waveform Done）。

<a id="a6e895d0472b5050eeb80b4f65a543478"></a>

### `IFX_HPPASS_AC_COND_CSG_1_COMP`

```c
#define IFX_HPPASS_AC_COND_CSG_1_COMP 57
```

CSG1 比较器触发（Comparator Trip）。

<a id="ade32923b770bf9d2ffdf6b33e7c78c97"></a>

### `IFX_HPPASS_AC_COND_CSG_1_DAC_DONE`

```c
#define IFX_HPPASS_AC_COND_CSG_1_DAC_DONE 49
```

CSG1 的 DAC 波形完成（Waveform Done）。

<a id="aa7c05cbbba28b8fb6828be608dc7cb38"></a>

### `IFX_HPPASS_AC_COND_CSG_2_COMP`

```c
#define IFX_HPPASS_AC_COND_CSG_2_COMP 58
```

CSG2 比较器触发（Comparator Trip）。

<a id="a19612ce34694a1560210310f70cd241b"></a>

### `IFX_HPPASS_AC_COND_CSG_2_DAC_DONE`

```c
#define IFX_HPPASS_AC_COND_CSG_2_DAC_DONE 50
```

CSG2 的 DAC 波形完成（Waveform Done）。

<a id="a0a47a9cd96c4ef67b282d04f905d5ee6"></a>

### `IFX_HPPASS_AC_COND_CSG_3_COMP`

```c
#define IFX_HPPASS_AC_COND_CSG_3_COMP 59
```

CSG3 比较器触发（Comparator Trip）。

<a id="a991f1569ca3990c6d22f590566df0944"></a>

### `IFX_HPPASS_AC_COND_CSG_3_DAC_DONE`

```c
#define IFX_HPPASS_AC_COND_CSG_3_DAC_DONE 51
```

CSG3 的 DAC 波形完成（Waveform Done）。

<a id="a8d0064477d07613a6af061fbd3f39624"></a>

### `IFX_HPPASS_AC_COND_CSG_4_COMP`

```c
#define IFX_HPPASS_AC_COND_CSG_4_COMP 60
```

CSG4 比较器触发（Comparator Trip）。

<a id="a52e7032988171863547953f1157c3370"></a>

### `IFX_HPPASS_AC_COND_CSG_4_DAC_DONE`

```c
#define IFX_HPPASS_AC_COND_CSG_4_DAC_DONE 52
```

CSG4 的 DAC 波形完成（Waveform Done）。

<a id="ab3b9458cadd0b2a889bf54c7734ee339"></a>

### `IFX_HPPASS_AC_COND_FALSE`

```c
#define IFX_HPPASS_AC_COND_FALSE 0
```

无条件为 FALSE。

<a id="a3e3e96b8d5a39db52ecea685194a1296"></a>

### `IFX_HPPASS_AC_COND_FIFO_0_LEVEL`

```c
#define IFX_HPPASS_AC_COND_FIFO_0_LEVEL 42
```

FIFO 水位（Level）0。

<a id="a5d4e6605907cad460acc9a6fd79fc79f"></a>

### `IFX_HPPASS_AC_COND_FIFO_1_LEVEL`

```c
#define IFX_HPPASS_AC_COND_FIFO_1_LEVEL 43
```

FIFO 水位（Level）1。

<a id="a5918287d031867bd20394f3121ea16ad"></a>

### `IFX_HPPASS_AC_COND_FIFO_2_LEVEL`

```c
#define IFX_HPPASS_AC_COND_FIFO_2_LEVEL 44
```

FIFO 水位（Level）2。

<a id="a3d627f0183f20b32b57408a99fc70a88"></a>

### `IFX_HPPASS_AC_COND_FIFO_3_LEVEL`

```c
#define IFX_HPPASS_AC_COND_FIFO_3_LEVEL 45
```

FIFO 水位（Level）3。

<a id="a525958c4634dc0592c26d5ab6c48e15b"></a>

### `IFX_HPPASS_AC_COND_SAR_BUSY`

```c
#define IFX_HPPASS_AC_COND_SAR_BUSY 20
```

逐次逼近（SAR）模块忙。

<a id="aea00068d3c695b20b567062975b2c596"></a>

### `IFX_HPPASS_AC_COND_SAR_FIR_0_DONE`

```c
#define IFX_HPPASS_AC_COND_SAR_FIR_0_DONE 21
```

SAR 有限脉冲响应滤波器（FIR）0 完成。

<a id="a471cb11613962c711c0f47da3b36365f"></a>

### `IFX_HPPASS_AC_COND_SAR_FIR_1_DONE`

```c
#define IFX_HPPASS_AC_COND_SAR_FIR_1_DONE 22
```

SAR 有限脉冲响应滤波器（FIR）1 完成。

<a id="a93fc924ff57330ed1dda461a3bdb3074"></a>

### `IFX_HPPASS_AC_COND_SAR_GROUP_0_DONE`

```c
#define IFX_HPPASS_AC_COND_SAR_GROUP_0_DONE 4
```

逐次逼近（SAR）组 0 完成（Done）。

<a id="acb0c847ff8bc0e57fb7f92fbbdbaa824"></a>

### `IFX_HPPASS_AC_COND_SAR_GROUP_1_DONE`

```c
#define IFX_HPPASS_AC_COND_SAR_GROUP_1_DONE 5
```

逐次逼近（SAR）组 1 完成（Done）。

<a id="ae24c0996092d4e28d0668513fd05ff8c"></a>

### `IFX_HPPASS_AC_COND_SAR_GROUP_2_DONE`

```c
#define IFX_HPPASS_AC_COND_SAR_GROUP_2_DONE 6
```

逐次逼近（SAR）组 2 完成（Done）。

<a id="ad7b08b94e7877df73db6850b2b623737"></a>

### `IFX_HPPASS_AC_COND_SAR_GROUP_3_DONE`

```c
#define IFX_HPPASS_AC_COND_SAR_GROUP_3_DONE 7
```

逐次逼近（SAR）组 3 完成（Done）。

<a id="a74a9cf6491c8d8b5db437e5c06a914f1"></a>

### `IFX_HPPASS_AC_COND_SAR_GROUP_4_DONE`

```c
#define IFX_HPPASS_AC_COND_SAR_GROUP_4_DONE 8
```

逐次逼近（SAR）组 4 完成（Done）。

<a id="acca9519de4a76866c69d109b4d589572"></a>

### `IFX_HPPASS_AC_COND_SAR_GROUP_5_DONE`

```c
#define IFX_HPPASS_AC_COND_SAR_GROUP_5_DONE 9
```

逐次逼近（SAR）组 5 完成（Done）。

<a id="a54192c1f3be2e1082fc96aa082b84264"></a>

### `IFX_HPPASS_AC_COND_SAR_GROUP_6_DONE`

```c
#define IFX_HPPASS_AC_COND_SAR_GROUP_6_DONE 10
```

逐次逼近（SAR）组 6 完成（Done）。

<a id="a177afc1a0d96c25d40bcc510f62c5919"></a>

### `IFX_HPPASS_AC_COND_SAR_GROUP_7_DONE`

```c
#define IFX_HPPASS_AC_COND_SAR_GROUP_7_DONE 11
```

逐次逼近（SAR）组 7 完成（Done）。

<a id="ac918d0c11a408998020fd268e3cf206d"></a>

### `IFX_HPPASS_AC_COND_SAR_LIMIT_0`

```c
#define IFX_HPPASS_AC_COND_SAR_LIMIT_0 12
```

逐次逼近（SAR）限值检测器（Limit Detector）0。

<a id="a1c304b54ccec00ff4da421e63c72b49a"></a>

### `IFX_HPPASS_AC_COND_SAR_LIMIT_1`

```c
#define IFX_HPPASS_AC_COND_SAR_LIMIT_1 13
```

逐次逼近（SAR）限值检测器（Limit Detector）1。

<a id="a2b0a8917bbb0839dd4d645d8131338ac"></a>

### `IFX_HPPASS_AC_COND_SAR_LIMIT_2`

```c
#define IFX_HPPASS_AC_COND_SAR_LIMIT_2 14
```

逐次逼近（SAR）限值检测器（Limit Detector）2。

<a id="a2743add8eaa21fa94bb7a1d42f7b7489"></a>

### `IFX_HPPASS_AC_COND_SAR_LIMIT_3`

```c
#define IFX_HPPASS_AC_COND_SAR_LIMIT_3 15
```

逐次逼近（SAR）限值检测器（Limit Detector）3。

<a id="a8141384f3dec367a88ba7b67c034a7ed"></a>

### `IFX_HPPASS_AC_COND_SAR_LIMIT_4`

```c
#define IFX_HPPASS_AC_COND_SAR_LIMIT_4 16
```

逐次逼近（SAR）限值检测器（Limit Detector）4。

<a id="a4c101ae981deac8cc2ba58bb7c07249c"></a>

### `IFX_HPPASS_AC_COND_SAR_LIMIT_5`

```c
#define IFX_HPPASS_AC_COND_SAR_LIMIT_5 17
```

逐次逼近（SAR）限值检测器（Limit Detector）5。

<a id="ac7ccd9ddc6e4727955eb8c127b1df9a6"></a>

### `IFX_HPPASS_AC_COND_SAR_LIMIT_6`

```c
#define IFX_HPPASS_AC_COND_SAR_LIMIT_6 18
```

逐次逼近（SAR）限值检测器（Limit Detector）6。

<a id="aef3f8780c34d41b6cf54852966e80828"></a>

### `IFX_HPPASS_AC_COND_SAR_LIMIT_7`

```c
#define IFX_HPPASS_AC_COND_SAR_LIMIT_7 19
```

逐次逼近（SAR）限值检测器（Limit Detector）7。

<a id="afee978a8ff21eed80bbb76aa52774bcf"></a>

### `IFX_HPPASS_AC_COND_SAR_QUEUE_HI_EMPTY`

```c
#define IFX_HPPASS_AC_COND_SAR_QUEUE_HI_EMPTY 23
```

SAR 高优先级队列（High-priority Queue）为空。

<a id="a8a9add025dafe8314071b5af90f6ce6c"></a>

### `IFX_HPPASS_AC_COND_SAR_QUEUE_LO_EMPTY`

```c
#define IFX_HPPASS_AC_COND_SAR_QUEUE_LO_EMPTY 24
```

SAR 低优先级队列（Low-priority Queue）为空。

<a id="ab057818da3f100849eb795c6dead4f46"></a>

### `IFX_HPPASS_AC_COND_SAR_QUEUES_EMPTY`

```c
#define IFX_HPPASS_AC_COND_SAR_QUEUES_EMPTY 25
```

SAR 的两个队列（Queue）均为空。

<a id="afadf2ef74d8d9bb1d1e5c8c24e3688a9"></a>

### `IFX_HPPASS_AC_COND_TRIG_0`

```c
#define IFX_HPPASS_AC_COND_TRIG_0 32
```

硬件／固件触发（HW/FW Trigger）0。

<a id="a65a62776f37a4db53b3f5f60bd6dbb91"></a>

### `IFX_HPPASS_AC_COND_TRIG_1`

```c
#define IFX_HPPASS_AC_COND_TRIG_1 33
```

硬件／固件触发（HW/FW Trigger）1。

<a id="a1b29317b9826693ef5608491bf01b599"></a>

### `IFX_HPPASS_AC_COND_TRIG_2`

```c
#define IFX_HPPASS_AC_COND_TRIG_2 34
```

硬件／固件触发（HW/FW Trigger）2。

<a id="aee658692cdc1760964673d917ff8197d"></a>

### `IFX_HPPASS_AC_COND_TRIG_3`

```c
#define IFX_HPPASS_AC_COND_TRIG_3 35
```

硬件／固件触发（HW/FW Trigger）3。

<a id="a4d28591c81cfe48ac2a86b09e4e031af"></a>

### `IFX_HPPASS_AC_COND_TRIG_4`

```c
#define IFX_HPPASS_AC_COND_TRIG_4 36
```

硬件／固件触发（HW/FW Trigger）4。

<a id="a70fb58679230267ec373c07ac185ccac"></a>

### `IFX_HPPASS_AC_COND_TRIG_5`

```c
#define IFX_HPPASS_AC_COND_TRIG_5 37
```

硬件／固件触发（HW/FW Trigger）5。

<a id="a019314e9b5e1555c1dca7ffae538575a"></a>

### `IFX_HPPASS_AC_COND_TRIG_6`

```c
#define IFX_HPPASS_AC_COND_TRIG_6 38
```

硬件／固件触发（HW/FW Trigger）6。

<a id="a2e0ce849306bdf52776bb2afd1abea0a"></a>

### `IFX_HPPASS_AC_COND_TRIG_7`

```c
#define IFX_HPPASS_AC_COND_TRIG_7 39
```

硬件／固件触发（HW/FW Trigger）7。

<a id="a13cde63a5e1672be493df30c37412f5e"></a>

### `IFX_HPPASS_AC_COND_TRUE`

```c
#define IFX_HPPASS_AC_COND_TRUE 1
```

无条件为 TRUE。

<a id="ac8a3b9a068927e3af0ad26b721743255"></a>

### `IFX_HPPASS_GPIO_OUT_0`

```c
#define IFX_HPPASS_GPIO_OUT_0 0x01
```

GPIO 输出（Output）0。

<a id="a863783df68d608b3e26a89067dc77444"></a>

### `IFX_HPPASS_GPIO_OUT_1`

```c
#define IFX_HPPASS_GPIO_OUT_1 0x02
```

GPIO 输出（Output）1。

<a id="abf19cfdb971b7033e4e64735947ce149"></a>

### `IFX_HPPASS_GPIO_OUT_2`

```c
#define IFX_HPPASS_GPIO_OUT_2 0x04
```

GPIO 输出（Output）2。

<a id="ae698a880e8f08f3433700f5f2c0a31b9"></a>

### `IFX_HPPASS_GPIO_OUT_3`

```c
#define IFX_HPPASS_GPIO_OUT_3 0x08
```

GPIO 输出（Output）3。

<a id="ab789f6fa2a711f8e83de11142a53fbb9"></a>

### `IFX_HPPASS_GPIO_OUT_4`

```c
#define IFX_HPPASS_GPIO_OUT_4 0x10
```

GPIO 输出（Output）4。

<a id="ab71b60fe89af462eb704310f62ef0d14"></a>

### `IFX_HPPASS_SAR_GRP_0`

```c
#define IFX_HPPASS_SAR_GRP_0 0x01
```

逐次逼近（SAR）组 0 触发（Trigger）。

<a id="ac10db27f7d1dd79728bd7873b29436c2"></a>

### `IFX_HPPASS_SAR_GRP_1`

```c
#define IFX_HPPASS_SAR_GRP_1 0x02
```

逐次逼近（SAR）组 1 触发（Trigger）。

<a id="a3473c526c36eb5c9d48cbab6c6cb8516"></a>

### `IFX_HPPASS_SAR_GRP_2`

```c
#define IFX_HPPASS_SAR_GRP_2 0x04
```

逐次逼近（SAR）组 2 触发（Trigger）。

<a id="acb18956d8bc5b6a1ce421d9781feb2c2"></a>

### `IFX_HPPASS_SAR_GRP_3`

```c
#define IFX_HPPASS_SAR_GRP_3 0x08
```

逐次逼近（SAR）组 3 触发（Trigger）。

<a id="a636e15d6579a987b52b888b2c3feb083"></a>

### `IFX_HPPASS_SAR_GRP_4`

```c
#define IFX_HPPASS_SAR_GRP_4 0x10
```

逐次逼近（SAR）组 4 触发（Trigger）。

<a id="a04e25afb83c0d24fcab2ee67e52dac48"></a>

### `IFX_HPPASS_SAR_GRP_5`

```c
#define IFX_HPPASS_SAR_GRP_5 0x20
```

逐次逼近（SAR）组 5 触发（Trigger）。

<a id="a7eb7b226c512990e319985ba2d034f23"></a>

### `IFX_HPPASS_SAR_GRP_6`

```c
#define IFX_HPPASS_SAR_GRP_6 0x40
```

逐次逼近（SAR）组 6 触发（Trigger）。

<a id="a2f0da8676ea92c8c19f712406fb0efd0"></a>

### `IFX_HPPASS_SAR_GRP_7`

```c
#define IFX_HPPASS_SAR_GRP_7 0x80
```

逐次逼近（SAR）组 7 触发（Trigger）。

<a id="a0d7693c705dc2b9cbdac113ab92d748f"></a>

### `IFX_HPPASS_TR_DISABLED`

```c
#define IFX_HPPASS_TR_DISABLED 0
```

关闭触发（Trigger）。

<a id="ad6d32ca98bf7b8bdf18cc473fdc73d78"></a>

### `IFX_HPPASS_TR_FW_LEVEL`

```c
#define IFX_HPPASS_TR_FW_LEVEL 4
```

固件电平触发（FW Level Trigger）。

<a id="ad36a3082b34024ce88acfbfb276c6ec9"></a>

### `IFX_HPPASS_TR_FW_PULSE`

```c
#define IFX_HPPASS_TR_FW_PULSE 3
```

固件脉冲触发（FW Pulse Trigger）。

<a id="a2acd3f95ea33686b464f92ac65f52568"></a>

### `IFX_HPPASS_TR_HW_A`

```c
#define IFX_HPPASS_TR_HW_A 1
```

外部硬件触发（External HW Trigger）A。

<a id="a8c659cfb4dc0df7785dfc7271f09aa9d"></a>

### `IFX_HPPASS_TR_HW_B`

```c
#define IFX_HPPASS_TR_HW_B 2
```

外部硬件触发（External HW Trigger）B。

<a id="a99c62b3de709116397279502fbac9dc5"></a>

### `IFX_HPPASS_TR_HW_LEVEL_DSYNC`

```c
#define IFX_HPPASS_TR_HW_LEVEL_DSYNC 3
```

异步（Async），双级同步（Double-sync），电平触发（Level Trigger）。

<a id="a0170a4bfdf89da9417472147b56db7d4"></a>

### `IFX_HPPASS_TR_HW_LEVEL_SSYNC`

```c
#define IFX_HPPASS_TR_HW_LEVEL_SSYNC 7
```

同步（Sync），电平触发（Level Trigger）。

<a id="a5decef62cdb66546d5f66f6002f9a0e0"></a>

### `IFX_HPPASS_TR_HW_PULSE_BOTH_DSYNC`

```c
#define IFX_HPPASS_TR_HW_PULSE_BOTH_DSYNC 2
```

异步（Async），双级同步（Double-sync），在双边沿产生脉冲。

<a id="a3a5b83bf3222915e24696f9bc033af66"></a>

### `IFX_HPPASS_TR_HW_PULSE_BOTH_SSYNC`

```c
#define IFX_HPPASS_TR_HW_PULSE_BOTH_SSYNC 6
```

同步（Sync），在双边沿产生脉冲。

<a id="a6751ae17ea6de662b276c6f6da7aece6"></a>

### `IFX_HPPASS_TR_HW_PULSE_NEG_DSYNC`

```c
#define IFX_HPPASS_TR_HW_PULSE_NEG_DSYNC 1
```

异步（Async），双级同步（Double-sync），在下降沿产生脉冲。

<a id="ab752b691d9e8ffc2d4cfb0b252c53d61"></a>

### `IFX_HPPASS_TR_HW_PULSE_NEG_SSYNC`

```c
#define IFX_HPPASS_TR_HW_PULSE_NEG_SSYNC 5
```

同步（Sync），在下降沿产生脉冲。

<a id="ae2567f36992250f78edd5e04179e0601"></a>

### `IFX_HPPASS_TR_HW_PULSE_POS_DSYNC`

```c
#define IFX_HPPASS_TR_HW_PULSE_POS_DSYNC 0
```

异步（Async），双级同步（Double-sync），在上升沿产生脉冲。

<a id="aa5d1779a119701a6a6df4c4d11700625"></a>

### `IFX_HPPASS_TR_HW_PULSE_POS_SSYNC`

```c
#define IFX_HPPASS_TR_HW_PULSE_POS_SSYNC 4
```

同步（Sync），在上升沿产生脉冲。

<a id="a0758c112427a09fcb517059ed10a4c82"></a>

### `IFX_HPPASS_TR_OUT_AC`

```c
#define IFX_HPPASS_TR_OUT_AC 11
```

自主控制器触发输出（AC Trigger Output）。

<a id="a48155ee043d177e898ef9ec4e79554f3"></a>

### `IFX_HPPASS_TR_OUT_DISABLED`

```c
#define IFX_HPPASS_TR_OUT_DISABLED 0
```

禁用触发输出（Trigger Output）。

<a id="a9db6f1f3a816008f430d5e1752513089"></a>

### `IFX_HPPASS_TR_OUT_FIR_0`

```c
#define IFX_HPPASS_TR_OUT_FIR_0 9
```

有限脉冲响应滤波器（FIR）0 完成（Done）。

<a id="a05dd2a8af999198347a4456b48a223d5"></a>

### `IFX_HPPASS_TR_OUT_FIR_1`

```c
#define IFX_HPPASS_TR_OUT_FIR_1 10
```

有限脉冲响应滤波器（FIR）1 完成（Done）。

<a id="a603a002173a92becfa54b8c7a6e62c6e"></a>

### `IFX_HPPASS_TR_OUT_SAR_GROUP_0`

```c
#define IFX_HPPASS_TR_OUT_SAR_GROUP_0 1
```

逐次逼近（SAR）组 0 完成（Done）。

<a id="ad8f8931d4afe4a6bf0c74d004c68612a"></a>

### `IFX_HPPASS_TR_OUT_SAR_GROUP_1`

```c
#define IFX_HPPASS_TR_OUT_SAR_GROUP_1 2
```

逐次逼近（SAR）组 1 完成（Done）。

<a id="a68375c65bdb1a9a0b0f91b1c9f3e6419"></a>

### `IFX_HPPASS_TR_OUT_SAR_GROUP_2`

```c
#define IFX_HPPASS_TR_OUT_SAR_GROUP_2 3
```

逐次逼近（SAR）组 2 完成（Done）。

<a id="a432c2a388b08ae7c323fac2b04757a99"></a>

### `IFX_HPPASS_TR_OUT_SAR_GROUP_3`

```c
#define IFX_HPPASS_TR_OUT_SAR_GROUP_3 4
```

逐次逼近（SAR）组 3 完成（Done）。

<a id="a41fd5c0d13a95fab2b16168bed94facf"></a>

### `IFX_HPPASS_TR_OUT_SAR_GROUP_4`

```c
#define IFX_HPPASS_TR_OUT_SAR_GROUP_4 5
```

逐次逼近（SAR）组 4 完成（Done）。

<a id="a1cd972a20688d0d18b90c4c0256fcae2"></a>

### `IFX_HPPASS_TR_OUT_SAR_GROUP_5`

```c
#define IFX_HPPASS_TR_OUT_SAR_GROUP_5 6
```

逐次逼近（SAR）组 5 完成（Done）。

<a id="a2b87a40b41f7bb1c34e163c3d110c79d"></a>

### `IFX_HPPASS_TR_OUT_SAR_GROUP_6`

```c
#define IFX_HPPASS_TR_OUT_SAR_GROUP_6 7
```

逐次逼近（SAR）组 6 完成（Done）。

<a id="a1c3a8794d147bdd0de980e0aa44b4923"></a>

### `IFX_HPPASS_TR_OUT_SAR_GROUP_7`

```c
#define IFX_HPPASS_TR_OUT_SAR_GROUP_7 8
```

逐次逼近（SAR）组 7 完成（Done）。


## 5.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P371_infineon-hppass.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P004_zephyr__dt-bindings__mfd__infineon-autanalog.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P006_zephyr__net__mdio.h_文件参考.md)
