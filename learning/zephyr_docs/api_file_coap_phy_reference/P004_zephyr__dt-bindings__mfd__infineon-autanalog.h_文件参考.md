---
id: learning.zephyr-docs.api-file-coap-phy-reference.page-4
title: zephyr__dt-bindings__mfd__infineon-autanalog.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_zephyr\_\_dt-bindings\_\_mfd\_\_infineon-autanalog.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Infineon AutAnalog Autonomous Controller的设备树绑定常量（Devicetree Binding Constants）。

查看此文件的源码。

<a id="details"></a>

Infineon AutAnalog 自主控制器（Autonomous Controller）的设备树绑定（Devicetree Binding）常量。这些常量与外设驱动库（PDL）的枚举值一致，用于配置 AC 状态转换表（State Transition Table）的设备树属性。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 4.1\_宏定义（Macros）

<a id="define-members-0"></a>

### AC状态转换表动作值（AC STT Action values (cy_en_autanalog_stt_ac_action_t)）

<a id="r_ac26e0487736f9118104c55d5bd36bfc0"></a>

```c
#define IFX_AUTANALOG_AC_ACTION_STOP 0
```

相关声明：[IFX_AUTANALOG_AC_ACTION_STOP](#ac26e0487736f9118104c55d5bd36bfc0)。

停止自主控制器（AC）。

<a id="r_aed381f7635ecab22af10e84cd81acd83"></a>

```c
#define IFX_AUTANALOG_AC_ACTION_NEXT 1
```

相关声明：[IFX_AUTANALOG_AC_ACTION_NEXT](#aed381f7635ecab22af10e84cd81acd83)。

进入下一状态（Next State）。

<a id="r_a39afdbb1030ec015ae5743365aebd6d8"></a>

```c
#define IFX_AUTANALOG_AC_ACTION_WAIT_FOR 2
```

相关声明：[IFX_AUTANALOG_AC_ACTION_WAIT_FOR](#a39afdbb1030ec015ae5743365aebd6d8)。

等待条件（CONDITION）变为 TRUE。

<a id="r_a01dc66a59f5781d2fc7ee3c11d7ea76e"></a>

```c
#define IFX_AUTANALOG_AC_ACTION_BRANCH_IF_TRUE 3
```

相关声明：[IFX_AUTANALOG_AC_ACTION_BRANCH_IF_TRUE](#a01dc66a59f5781d2fc7ee3c11d7ea76e)。

当条件（CONDITION）为 TRUE 时分支跳转。

<a id="r_a2ebe2ed3f6901a7e80b9621559e96a3d"></a>

```c
#define IFX_AUTANALOG_AC_ACTION_BRANCH_IF_FALSE 4
```

相关声明：[IFX_AUTANALOG_AC_ACTION_BRANCH_IF_FALSE](#a2ebe2ed3f6901a7e80b9621559e96a3d)。

当条件（CONDITION）为 FALSE 时分支跳转。

<a id="r_aa51c3264e2ee2c7f88d8529c5d313cee"></a>

```c
#define IFX_AUTANALOG_AC_ACTION_BRANCH_IF_TRUE_CLR 5
```

相关声明：[IFX_AUTANALOG_AC_ACTION_BRANCH_IF_TRUE_CLR](#aa51c3264e2ee2c7f88d8529c5d313cee)。

为 TRUE 时分支跳转并清零计数器（Counter）。

<a id="r_ae84d1c4a82738a10b5615afb90a1cf60"></a>

```c
#define IFX_AUTANALOG_AC_ACTION_BRANCH_IF_FALSE_CLR 6
```

相关声明：[IFX_AUTANALOG_AC_ACTION_BRANCH_IF_FALSE_CLR](#ae84d1c4a82738a10b5615afb90a1cf60)。

为 FALSE 时分支跳转并清零计数器（Counter）。

<a id="define-members-1"></a>

### AC状态转换表条件值（AC STT Condition values (cy_en_autanalog_stt_ac_condition_t)）

<a id="r_aed5d0fbe398ce34acad63b95e3c5cbcc"></a>

```c
#define IFX_AUTANALOG_AC_COND_FALSE 0
```

相关声明：[IFX_AUTANALOG_AC_COND_FALSE](#aed5d0fbe398ce34acad63b95e3c5cbcc)。

无条件为 FALSE。

<a id="r_a1ed711440c168a67a6ab2415c3756693"></a>

```c
#define IFX_AUTANALOG_AC_COND_TRUE 1
```

相关声明：[IFX_AUTANALOG_AC_COND_TRUE](#a1ed711440c168a67a6ab2415c3756693)。

无条件为 TRUE。

<a id="r_a7a482ac589b2737ff9fac20ec58bc2ce"></a>

```c
#define IFX_AUTANALOG_AC_COND_BLOCK_READY 2
```

相关声明：[IFX_AUTANALOG_AC_COND_BLOCK_READY](#a7a482ac589b2737ff9fac20ec58bc2ce)。

子系统（Subsystem）已初始化并就绪。

<a id="r_aa34c654081a48149c5e84649382c221f"></a>

```c
#define IFX_AUTANALOG_AC_COND_CNT_DONE 3
```

相关声明：[IFX_AUTANALOG_AC_COND_CNT_DONE](#aa34c654081a48149c5e84649382c221f)。

计数器（Counter）完成。

<a id="r_a62e782e610b33d131265902fe485e09b"></a>

```c
#define IFX_AUTANALOG_AC_COND_SAR_DONE 4
```

相关声明：[IFX_AUTANALOG_AC_COND_SAR_DONE](#a62e782e610b33d131265902fe485e09b)。

逐次逼近（SAR）序列控制器（Sequencer）完成。

<a id="r_a485bf0b82b62a7528fb9373c0487b759"></a>

```c
#define IFX_AUTANALOG_AC_COND_SAR_EOS 5
```

相关声明：[IFX_AUTANALOG_AC_COND_SAR_EOS](#a485bf0b82b62a7528fb9373c0487b759)。

逐次逼近（SAR）扫描结束（End of Scan）。

<a id="r_a21f6ddbe9d7db5fb214a94c51b773795"></a>

```c
#define IFX_AUTANALOG_AC_COND_SAR_RANGE0 6
```

相关声明：[IFX_AUTANALOG_AC_COND_SAR_RANGE0](#a21f6ddbe9d7db5fb214a94c51b773795)。

SAR 范围（Range）0 检测（Detection）。

<a id="r_a78ccdf5bcac7b8d65537f74516c49599"></a>

```c
#define IFX_AUTANALOG_AC_COND_SAR_RANGE1 7
```

相关声明：[IFX_AUTANALOG_AC_COND_SAR_RANGE1](#a78ccdf5bcac7b8d65537f74516c49599)。

SAR 范围（Range）1 检测（Detection）。

<a id="r_ac90e195f22faba54e1a670e20c86437e"></a>

```c
#define IFX_AUTANALOG_AC_COND_SAR_RANGE2 8
```

相关声明：[IFX_AUTANALOG_AC_COND_SAR_RANGE2](#ac90e195f22faba54e1a670e20c86437e)。

SAR 范围（Range）2 检测（Detection）。

<a id="r_a187aff8fac3d22f83af8b3981a3793fe"></a>

```c
#define IFX_AUTANALOG_AC_COND_SAR_RANGE3 9
```

相关声明：[IFX_AUTANALOG_AC_COND_SAR_RANGE3](#a187aff8fac3d22f83af8b3981a3793fe)。

SAR 范围（Range）3 检测（Detection）。

<a id="r_af7ec6c7e61b7f3abab0d4149c1e4f8af"></a>

```c
#define IFX_AUTANALOG_AC_COND_SAR_BUSY 10
```

相关声明：[IFX_AUTANALOG_AC_COND_SAR_BUSY](#af7ec6c7e61b7f3abab0d4149c1e4f8af)。

逐次逼近（SAR）模块忙。

<a id="r_a1d98307dc3598eb3cbae4a7a4b8db586"></a>

```c
#define IFX_AUTANALOG_AC_COND_SAR_FIR0_DONE 11
```

相关声明：[IFX_AUTANALOG_AC_COND_SAR_FIR0_DONE](#a1d98307dc3598eb3cbae4a7a4b8db586)。

SAR 有限脉冲响应滤波器（FIR）0 完成。

<a id="r_a99e6eb9d40dd9242d5b5f6c30fbcd9f5"></a>

```c
#define IFX_AUTANALOG_AC_COND_SAR_FIR1_DONE 12
```

相关声明：[IFX_AUTANALOG_AC_COND_SAR_FIR1_DONE](#a99e6eb9d40dd9242d5b5f6c30fbcd9f5)。

SAR 有限脉冲响应滤波器（FIR）1 完成。

<a id="r_a60a92c4f9e02a4077798c4440deb98ca"></a>

```c
#define IFX_AUTANALOG_AC_COND_SAR_FIFO_DONE 13
```

相关声明：[IFX_AUTANALOG_AC_COND_SAR_FIFO_DONE](#a60a92c4f9e02a4077798c4440deb98ca)。

SAR 先进先出队列（FIFO）完成。

<a id="r_abcdba475a0708c252e60c26fb126da24"></a>

```c
#define IFX_AUTANALOG_AC_COND_SAR_FIR0_FIFO_DONE 14
```

相关声明：[IFX_AUTANALOG_AC_COND_SAR_FIR0_FIFO_DONE](#abcdba475a0708c252e60c26fb126da24)。

SAR FIR0 的先进先出队列（FIFO）完成。

<a id="r_afbb4ab6cba32780afc838d67cbadec41"></a>

```c
#define IFX_AUTANALOG_AC_COND_SAR_FIR1_FIFO_DONE 15
```

相关声明：[IFX_AUTANALOG_AC_COND_SAR_FIR1_FIFO_DONE](#afbb4ab6cba32780afc838d67cbadec41)。

SAR FIR1 的先进先出队列（FIFO）完成。

<a id="r_a621175cf2e68b44c6fef037fddc65f9e"></a>

```c
#define IFX_AUTANALOG_AC_COND_PTCOMP_STROBE0 16
```

相关声明：[IFX_AUTANALOG_AC_COND_PTCOMP_STROBE0](#a621175cf2e68b44c6fef037fddc65f9e)。

PTComp 选通信号（Strobe） 0。

<a id="r_aa080ad5e42f250537c7227f20f157fc3"></a>

```c
#define IFX_AUTANALOG_AC_COND_PTCOMP_STROBE1 17
```

相关声明：[IFX_AUTANALOG_AC_COND_PTCOMP_STROBE1](#aa080ad5e42f250537c7227f20f157fc3)。

PTComp 选通信号（Strobe） 1。

<a id="r_ab418f84ff25774cfe1f0b57f0a3b7a0f"></a>

```c
#define IFX_AUTANALOG_AC_COND_PTCOMP_CMP0 18
```

相关声明：[IFX_AUTANALOG_AC_COND_PTCOMP_CMP0](#ab418f84ff25774cfe1f0b57f0a3b7a0f)。

PTComp 比较器（Comparator）0。

<a id="r_a412a38e2b404209c527377a7b02561c6"></a>

```c
#define IFX_AUTANALOG_AC_COND_PTCOMP_CMP1 19
```

相关声明：[IFX_AUTANALOG_AC_COND_PTCOMP_CMP1](#a412a38e2b404209c527377a7b02561c6)。

PTComp 比较器（Comparator）1。

<a id="r_a8b0374792e7d1955ddae33371438037a"></a>

```c
#define IFX_AUTANALOG_AC_COND_PTCOMP_RANGE0 20
```

相关声明：[IFX_AUTANALOG_AC_COND_PTCOMP_RANGE0](#a8b0374792e7d1955ddae33371438037a)。

PTComp 范围（Range）0。

<a id="r_ac91f91c7dca2835cf833f185407d8f87"></a>

```c
#define IFX_AUTANALOG_AC_COND_PTCOMP_RANGE1 21
```

相关声明：[IFX_AUTANALOG_AC_COND_PTCOMP_RANGE1](#ac91f91c7dca2835cf833f185407d8f87)。

PTComp 范围（Range）1。

<a id="r_a95a419e3ad5a371ca5f19d29267c32af"></a>

```c
#define IFX_AUTANALOG_AC_COND_CTB0_CMP0 22
```

相关声明：[IFX_AUTANALOG_AC_COND_CTB0_CMP0](#a95a419e3ad5a371ca5f19d29267c32af)。

CTB0 比较器（Comparator）0。

<a id="r_a1565408f57589d89868af6946a166579"></a>

```c
#define IFX_AUTANALOG_AC_COND_CTB0_CMP1 23
```

相关声明：[IFX_AUTANALOG_AC_COND_CTB0_CMP1](#a1565408f57589d89868af6946a166579)。

CTB0 比较器（Comparator）1。

<a id="r_af6fe159448bb3dfd193ae322ee1bc4b3"></a>

```c
#define IFX_AUTANALOG_AC_COND_CTB1_CMP0 24
```

相关声明：[IFX_AUTANALOG_AC_COND_CTB1_CMP0](#af6fe159448bb3dfd193ae322ee1bc4b3)。

CTB1 比较器（Comparator）0。

<a id="r_a586d60863ac4f2bd91832f89665592ef"></a>

```c
#define IFX_AUTANALOG_AC_COND_CTB1_CMP1 25
```

相关声明：[IFX_AUTANALOG_AC_COND_CTB1_CMP1](#a586d60863ac4f2bd91832f89665592ef)。

CTB1 比较器（Comparator）1。

<a id="r_a759ceaeb8ef43db4c6588a186b3c6c43"></a>

```c
#define IFX_AUTANALOG_AC_COND_CHIP_ACTIVE 32
```

相关声明：[IFX_AUTANALOG_AC_COND_CHIP_ACTIVE](#a759ceaeb8ef43db4c6588a186b3c6c43)。

芯片活动模式（Active Mode）状态。

<a id="r_a2b73be734f71e9687b0c0e927f2b5728"></a>

```c
#define IFX_AUTANALOG_AC_COND_CHIP_DEEPSLEEP 33
```

相关声明：[IFX_AUTANALOG_AC_COND_CHIP_DEEPSLEEP](#a2b73be734f71e9687b0c0e927f2b5728)。

芯片深度睡眠模式（Deep Sleep Mode）状态。

<a id="r_a494f86e0974cfebc581cfa0ed60d7253"></a>

```c
#define IFX_AUTANALOG_AC_COND_TR_IN0 34
```

相关声明：[IFX_AUTANALOG_AC_COND_TR_IN0](#a494f86e0974cfebc581cfa0ed60d7253)。

外部／固件触发（External/FW Trigger）0。

<a id="r_a56ce7b915574c39349c2b3198be6f025"></a>

```c
#define IFX_AUTANALOG_AC_COND_TR_IN1 35
```

相关声明：[IFX_AUTANALOG_AC_COND_TR_IN1](#a56ce7b915574c39349c2b3198be6f025)。

外部／固件触发（External/FW Trigger）1。

<a id="r_a20cf5b28b473169f94f6298f79dfaa8d"></a>

```c
#define IFX_AUTANALOG_AC_COND_TR_IN2 36
```

相关声明：[IFX_AUTANALOG_AC_COND_TR_IN2](#a20cf5b28b473169f94f6298f79dfaa8d)。

外部／固件触发（External/FW Trigger）2。

<a id="r_a26f0d9b4d322a8d52822032df218b62b"></a>

```c
#define IFX_AUTANALOG_AC_COND_TR_IN3 37
```

相关声明：[IFX_AUTANALOG_AC_COND_TR_IN3](#a26f0d9b4d322a8d52822032df218b62b)。

外部／固件触发（External/FW Trigger）3。

<a id="r_aae7dfbb92ff1b17a70416df7f2eb4f26"></a>

```c
#define IFX_AUTANALOG_AC_COND_TR_IN_WAKE 38
```

相关声明：[IFX_AUTANALOG_AC_COND_TR_IN_WAKE](#aae7dfbb92ff1b17a70416df7f2eb4f26)。

外部触发唤醒（External Trigger Wakeup）。

<a id="r_a0d64c0bca00b8a34118c00548effa7a5"></a>

```c
#define IFX_AUTANALOG_AC_COND_TIMER_DONE_WAKE 39
```

相关声明：[IFX_AUTANALOG_AC_COND_TIMER_DONE_WAKE](#a0d64c0bca00b8a34118c00548effa7a5)。

定时器唤醒（Timer Wakeup）。

<a id="r_a8a8ce0f1948fba25a2ea813285bcbc09"></a>

```c
#define IFX_AUTANALOG_AC_COND_CTB0_CMP0_WAKE 40
```

相关声明：[IFX_AUTANALOG_AC_COND_CTB0_CMP0_WAKE](#a8a8ce0f1948fba25a2ea813285bcbc09)。

CTB0 比较器（Comparator）0 唤醒（Wakeup）。

<a id="r_a20fd04f8c8b7f026854ba1763e8fcfcc"></a>

```c
#define IFX_AUTANALOG_AC_COND_CTB0_CMP1_WAKE 41
```

相关声明：[IFX_AUTANALOG_AC_COND_CTB0_CMP1_WAKE](#a20fd04f8c8b7f026854ba1763e8fcfcc)。

CTB0 比较器（Comparator）1 唤醒（Wakeup）。

<a id="r_a9a349219e74dc9d36837c5428dd44101"></a>

```c
#define IFX_AUTANALOG_AC_COND_CTB1_CMP0_WAKE 42
```

相关声明：[IFX_AUTANALOG_AC_COND_CTB1_CMP0_WAKE](#a9a349219e74dc9d36837c5428dd44101)。

CTB1 比较器（Comparator）0 唤醒（Wakeup）。

<a id="r_ade405959e09086dfeca9cbf9e6aaa202"></a>

```c
#define IFX_AUTANALOG_AC_COND_CTB1_CMP1_WAKE 43
```

相关声明：[IFX_AUTANALOG_AC_COND_CTB1_CMP1_WAKE](#ade405959e09086dfeca9cbf9e6aaa202)。

CTB1 比较器（Comparator）1 唤醒（Wakeup）。

<a id="r_a3487f8b03839d0013a0eff3a7170cd54"></a>

```c
#define IFX_AUTANALOG_AC_COND_PTCOMP_CMP0_WAKE 44
```

相关声明：[IFX_AUTANALOG_AC_COND_PTCOMP_CMP0_WAKE](#a3487f8b03839d0013a0eff3a7170cd54)。

PTComp 比较器（Comparator）0 唤醒（Wakeup）。

<a id="r_a97ed8d0e7c29eeb90e0a4ecf06b08f99"></a>

```c
#define IFX_AUTANALOG_AC_COND_PTCOMP_CMP1_WAKE 45
```

相关声明：[IFX_AUTANALOG_AC_COND_PTCOMP_CMP1_WAKE](#a97ed8d0e7c29eeb90e0a4ecf06b08f99)。

PTComp 比较器（Comparator）1 唤醒（Wakeup）。

<a id="r_a76e71d48761be7030d1b22976b7c8c6c"></a>

```c
#define IFX_AUTANALOG_AC_COND_FIFO_LEVEL0 46
```

相关声明：[IFX_AUTANALOG_AC_COND_FIFO_LEVEL0](#a76e71d48761be7030d1b22976b7c8c6c)。

FIFO 水位（Level）0。

<a id="r_a4691fe493dc867fcf966a253f2bff58d"></a>

```c
#define IFX_AUTANALOG_AC_COND_FIFO_LEVEL1 47
```

相关声明：[IFX_AUTANALOG_AC_COND_FIFO_LEVEL1](#a4691fe493dc867fcf966a253f2bff58d)。

FIFO 水位（Level）1。

<a id="r_a3fd3b9dc60c33c6840ff5da7dd2358fe"></a>

```c
#define IFX_AUTANALOG_AC_COND_FIFO_LEVEL2 48
```

相关声明：[IFX_AUTANALOG_AC_COND_FIFO_LEVEL2](#a3fd3b9dc60c33c6840ff5da7dd2358fe)。

FIFO 水位（Level）2。

<a id="r_a9c027c6caabf986451ca48a3a3198b5f"></a>

```c
#define IFX_AUTANALOG_AC_COND_FIFO_LEVEL3 49
```

相关声明：[IFX_AUTANALOG_AC_COND_FIFO_LEVEL3](#a9c027c6caabf986451ca48a3a3198b5f)。

FIFO 水位（Level）3。

<a id="r_aed7d55553c6f9166e2b543c06f27c46a"></a>

```c
#define IFX_AUTANALOG_AC_COND_FIFO_LEVEL4 50
```

相关声明：[IFX_AUTANALOG_AC_COND_FIFO_LEVEL4](#aed7d55553c6f9166e2b543c06f27c46a)。

FIFO 水位（Level）4。

<a id="r_ab2035282756f3beed8a28787d3e1162f"></a>

```c
#define IFX_AUTANALOG_AC_COND_FIFO_LEVEL5 51
```

相关声明：[IFX_AUTANALOG_AC_COND_FIFO_LEVEL5](#ab2035282756f3beed8a28787d3e1162f)。

FIFO 水位（Level）5。

<a id="r_ae3c56b39c4b994ca6b2cad290dc1f1b9"></a>

```c
#define IFX_AUTANALOG_AC_COND_FIFO_LEVEL6 52
```

相关声明：[IFX_AUTANALOG_AC_COND_FIFO_LEVEL6](#ae3c56b39c4b994ca6b2cad290dc1f1b9)。

FIFO 水位（Level）6。

<a id="r_a3e3bf3a3ed7320d4cb5006d8ceaa0253"></a>

```c
#define IFX_AUTANALOG_AC_COND_FIFO_LEVEL7 53
```

相关声明：[IFX_AUTANALOG_AC_COND_FIFO_LEVEL7](#a3e3bf3a3ed7320d4cb5006d8ceaa0253)。

FIFO 水位（Level）7。

<a id="r_af12dfd52c48f09d35be364b4e5bc1617"></a>

```c
#define IFX_AUTANALOG_AC_COND_DAC0_RANGE0 54
```

相关声明：[IFX_AUTANALOG_AC_COND_DAC0_RANGE0](#af12dfd52c48f09d35be364b4e5bc1617)。

DAC0 范围（Range）0。

<a id="r_ae07d8b24de701bad184f9beb3698851d"></a>

```c
#define IFX_AUTANALOG_AC_COND_DAC0_RANGE1 55
```

相关声明：[IFX_AUTANALOG_AC_COND_DAC0_RANGE1](#ae07d8b24de701bad184f9beb3698851d)。

DAC0 范围（Range）1。

<a id="r_a25fc05a14a4a21e2185b5055f8017271"></a>

```c
#define IFX_AUTANALOG_AC_COND_DAC0_RANGE2 56
```

相关声明：[IFX_AUTANALOG_AC_COND_DAC0_RANGE2](#a25fc05a14a4a21e2185b5055f8017271)。

DAC0 范围（Range）2。

<a id="r_ae484cbe259da9d08860e760961ed829f"></a>

```c
#define IFX_AUTANALOG_AC_COND_DAC0_EPOCH 57
```

相关声明：[IFX_AUTANALOG_AC_COND_DAC0_EPOCH](#ae484cbe259da9d08860e760961ed829f)。

DAC0 波形结束（End of Waveform）。

<a id="r_a7309b7a779227c6e456e3907c503ee48"></a>

```c
#define IFX_AUTANALOG_AC_COND_DAC0_STROBE 58
```

相关声明：[IFX_AUTANALOG_AC_COND_DAC0_STROBE](#a7309b7a779227c6e456e3907c503ee48)。

DAC0 选通信号（Strobe）。

<a id="r_a0c6abe9f92091e466eb0df6078c0e8af"></a>

```c
#define IFX_AUTANALOG_AC_COND_DAC1_RANGE0 59
```

相关声明：[IFX_AUTANALOG_AC_COND_DAC1_RANGE0](#a0c6abe9f92091e466eb0df6078c0e8af)。

DAC1 范围（Range）0。

<a id="r_a70cc4414203dfe097b78cc921bcb7e15"></a>

```c
#define IFX_AUTANALOG_AC_COND_DAC1_RANGE1 60
```

相关声明：[IFX_AUTANALOG_AC_COND_DAC1_RANGE1](#a70cc4414203dfe097b78cc921bcb7e15)。

DAC1 范围（Range）1。

<a id="r_a80bef915de90959df5f8157beb00b3c6"></a>

```c
#define IFX_AUTANALOG_AC_COND_DAC1_RANGE2 61
```

相关声明：[IFX_AUTANALOG_AC_COND_DAC1_RANGE2](#a80bef915de90959df5f8157beb00b3c6)。

DAC1 范围（Range）2。

<a id="r_a14bf63e7d2ccf70457ee0ee9b4b1d7f3"></a>

```c
#define IFX_AUTANALOG_AC_COND_DAC1_EPOCH 62
```

相关声明：[IFX_AUTANALOG_AC_COND_DAC1_EPOCH](#a14bf63e7d2ccf70457ee0ee9b4b1d7f3)。

DAC1 波形结束（End of Waveform）。

<a id="r_a21f0ab3b02faca9ddb98f208ac4d15f2"></a>

```c
#define IFX_AUTANALOG_AC_COND_DAC1_STROBE 63
```

相关声明：[IFX_AUTANALOG_AC_COND_DAC1_STROBE](#a21f0ab3b02faca9ddb98f208ac4d15f2)。

DAC1 选通信号（Strobe）。

<a id="define-members-2"></a>

### AC状态转换表GPIO输出掩码（AC STT GPIO output masks (cy_en_autanalog_stt_ac_gpio_out_t)）

<a id="r_ad752457ef1b2e3ce1e26e4eaf4e4ed4a"></a>

```c
#define IFX_AUTANALOG_AC_GPIO_OUT_DISABLED 0x0
```

相关声明：[IFX_AUTANALOG_AC_GPIO_OUT_DISABLED](#ad752457ef1b2e3ce1e26e4eaf4e4ed4a)。

禁用 GPIO 输出控制（Output Control）。

<a id="r_a477ca97a0203a592d41ae7668973f080"></a>

```c
#define IFX_AUTANALOG_AC_GPIO_OUT0 0x1
```

相关声明：[IFX_AUTANALOG_AC_GPIO_OUT0](#a477ca97a0203a592d41ae7668973f080)。

GPIO 输出（Output）0。

<a id="r_a534e1d1894ac08f9e6a9924468604cf2"></a>

```c
#define IFX_AUTANALOG_AC_GPIO_OUT1 0x2
```

相关声明：[IFX_AUTANALOG_AC_GPIO_OUT1](#a534e1d1894ac08f9e6a9924468604cf2)。

GPIO 输出（Output）1。

<a id="r_acf7d4d1698079affb4cd2e91e5796e33"></a>

```c
#define IFX_AUTANALOG_AC_GPIO_OUT2 0x4
```

相关声明：[IFX_AUTANALOG_AC_GPIO_OUT2](#acf7d4d1698079affb4cd2e91e5796e33)。

GPIO 输出（Output）2。

<a id="r_abaafa051e64aef8a4603e9121cbbe2a4"></a>

```c
#define IFX_AUTANALOG_AC_GPIO_OUT3 0x8
```

相关声明：[IFX_AUTANALOG_AC_GPIO_OUT3](#abaafa051e64aef8a4603e9121cbbe2a4)。

GPIO 输出（Output）3。

<a id="define-members-3"></a>

### CTB运算放大器增益值（CTB opamp gain values (cy_en_autanalog_stt_ctb_oa_gain_t)）

<a id="r_a5075abf67c4f8cf0d8bec2b96a9972aa"></a>

```c
#define IFX_AUTANALOG_CTB_OA_GAIN_1_00 0
```

相关声明：[IFX_AUTANALOG_CTB_OA_GAIN_1_00](#a5075abf67c4f8cf0d8bec2b96a9972aa)。

增益（Gain）1.00。

<a id="r_a24c35b68bfa86e567d76af7e1d74b6af"></a>

```c
#define IFX_AUTANALOG_CTB_OA_GAIN_1_42 1
```

相关声明：[IFX_AUTANALOG_CTB_OA_GAIN_1_42](#a24c35b68bfa86e567d76af7e1d74b6af)。

增益（Gain）1.42。

<a id="r_a47e4e2c1d49b14fdb9d37a8365ab5a12"></a>

```c
#define IFX_AUTANALOG_CTB_OA_GAIN_2_00 2
```

相关声明：[IFX_AUTANALOG_CTB_OA_GAIN_2_00](#a47e4e2c1d49b14fdb9d37a8365ab5a12)。

增益（Gain）2.00。

<a id="r_a3d9dfd90ac5bd3680a6a1a1a81abe83d"></a>

```c
#define IFX_AUTANALOG_CTB_OA_GAIN_2_78 3
```

相关声明：[IFX_AUTANALOG_CTB_OA_GAIN_2_78](#a3d9dfd90ac5bd3680a6a1a1a81abe83d)。

增益（Gain）2.78。

<a id="r_aae5c58f8dc88257463f7f20cfd85b201"></a>

```c
#define IFX_AUTANALOG_CTB_OA_GAIN_4_00 4
```

相关声明：[IFX_AUTANALOG_CTB_OA_GAIN_4_00](#aae5c58f8dc88257463f7f20cfd85b201)。

增益（Gain）4.00。

<a id="r_adfabe221c6c7837d97e93c8aff7141d7"></a>

```c
#define IFX_AUTANALOG_CTB_OA_GAIN_5_82 5
```

相关声明：[IFX_AUTANALOG_CTB_OA_GAIN_5_82](#adfabe221c6c7837d97e93c8aff7141d7)。

增益（Gain）5.82。

<a id="r_aa56acd2ecf35cfd73ce7bdc65c561af5"></a>

```c
#define IFX_AUTANALOG_CTB_OA_GAIN_8_00 6
```

相关声明：[IFX_AUTANALOG_CTB_OA_GAIN_8_00](#aa56acd2ecf35cfd73ce7bdc65c561af5)。

增益（Gain）8.00。

<a id="r_a47217bf71a3cf0749da83fb41015898a"></a>

```c
#define IFX_AUTANALOG_CTB_OA_GAIN_10_67 7
```

相关声明：[IFX_AUTANALOG_CTB_OA_GAIN_10_67](#a47217bf71a3cf0749da83fb41015898a)。

增益（Gain）10.67。

<a id="r_a4e70a9a2426ca7104516c959e935a234"></a>

```c
#define IFX_AUTANALOG_CTB_OA_GAIN_16_00 8
```

相关声明：[IFX_AUTANALOG_CTB_OA_GAIN_16_00](#a4e70a9a2426ca7104516c959e935a234)。

增益（Gain）16.00。

<a id="r_aad4431885b89783c8469e7fcd82517dc"></a>

```c
#define IFX_AUTANALOG_CTB_OA_GAIN_21_33 9
```

相关声明：[IFX_AUTANALOG_CTB_OA_GAIN_21_33](#aad4431885b89783c8469e7fcd82517dc)。

增益（Gain）21.33。

<a id="r_aff9a5c27d21d4d66c8e41ce8b290ebca"></a>

```c
#define IFX_AUTANALOG_CTB_OA_GAIN_32_00 10
```

相关声明：[IFX_AUTANALOG_CTB_OA_GAIN_32_00](#aff9a5c27d21d4d66c8e41ce8b290ebca)。

增益（Gain）32.00。

<a id="define-members-4"></a>

### DAC方向值（DAC direction values (cy_en_autanalog_stt_dac_dir_t)）

<a id="r_aeff791aee43c37dda07cae0471f2f1bd"></a>

```c
#define IFX_AUTANALOG_DAC_DIR_DISABLED 0
```

相关声明：[IFX_AUTANALOG_DAC_DIR_DISABLED](#aeff791aee43c37dda07cae0471f2f1bd)。

未选择方向（Direction）。

<a id="r_a2331afd96398c2f51f831c84f4ae1c23"></a>

```c
#define IFX_AUTANALOG_DAC_DIR_FORWARD 1
```

相关声明：[IFX_AUTANALOG_DAC_DIR_FORWARD](#a2331afd96398c2f51f831c84f4ae1c23)。

正向／递增（Forward / Increment）。

<a id="r_ae4d3568dd6ea7f235d2499f489ed8bc3"></a>

```c
#define IFX_AUTANALOG_DAC_DIR_REVERSE 2
```

相关声明：[IFX_AUTANALOG_DAC_DIR_REVERSE](#ae4d3568dd6ea7f235d2499f489ed8bc3)。

反向／递减（Backward / Decrement）。

## 4.2\_详细说明（Detailed Documentation）

<a id="a2ebe2ed3f6901a7e80b9621559e96a3d"></a>

### `IFX_AUTANALOG_AC_ACTION_BRANCH_IF_FALSE`

```c
#define IFX_AUTANALOG_AC_ACTION_BRANCH_IF_FALSE 4
```

当条件（CONDITION）为 FALSE 时分支跳转。

<a id="ae84d1c4a82738a10b5615afb90a1cf60"></a>

### `IFX_AUTANALOG_AC_ACTION_BRANCH_IF_FALSE_CLR`

```c
#define IFX_AUTANALOG_AC_ACTION_BRANCH_IF_FALSE_CLR 6
```

为 FALSE 时分支跳转并清零计数器（Counter）。

<a id="a01dc66a59f5781d2fc7ee3c11d7ea76e"></a>

### `IFX_AUTANALOG_AC_ACTION_BRANCH_IF_TRUE`

```c
#define IFX_AUTANALOG_AC_ACTION_BRANCH_IF_TRUE 3
```

当条件（CONDITION）为 TRUE 时分支跳转。

<a id="aa51c3264e2ee2c7f88d8529c5d313cee"></a>

### `IFX_AUTANALOG_AC_ACTION_BRANCH_IF_TRUE_CLR`

```c
#define IFX_AUTANALOG_AC_ACTION_BRANCH_IF_TRUE_CLR 5
```

为 TRUE 时分支跳转并清零计数器（Counter）。

<a id="aed381f7635ecab22af10e84cd81acd83"></a>

### `IFX_AUTANALOG_AC_ACTION_NEXT`

```c
#define IFX_AUTANALOG_AC_ACTION_NEXT 1
```

进入下一状态（Next State）。

<a id="ac26e0487736f9118104c55d5bd36bfc0"></a>

### `IFX_AUTANALOG_AC_ACTION_STOP`

```c
#define IFX_AUTANALOG_AC_ACTION_STOP 0
```

停止自主控制器（AC）。

<a id="a39afdbb1030ec015ae5743365aebd6d8"></a>

### `IFX_AUTANALOG_AC_ACTION_WAIT_FOR`

```c
#define IFX_AUTANALOG_AC_ACTION_WAIT_FOR 2
```

等待条件（CONDITION）变为 TRUE。

<a id="a7a482ac589b2737ff9fac20ec58bc2ce"></a>

### `IFX_AUTANALOG_AC_COND_BLOCK_READY`

```c
#define IFX_AUTANALOG_AC_COND_BLOCK_READY 2
```

子系统（Subsystem）已初始化并就绪。

<a id="a759ceaeb8ef43db4c6588a186b3c6c43"></a>

### `IFX_AUTANALOG_AC_COND_CHIP_ACTIVE`

```c
#define IFX_AUTANALOG_AC_COND_CHIP_ACTIVE 32
```

芯片活动模式（Active Mode）状态。

<a id="a2b73be734f71e9687b0c0e927f2b5728"></a>

### `IFX_AUTANALOG_AC_COND_CHIP_DEEPSLEEP`

```c
#define IFX_AUTANALOG_AC_COND_CHIP_DEEPSLEEP 33
```

芯片深度睡眠模式（Deep Sleep Mode）状态。

<a id="aa34c654081a48149c5e84649382c221f"></a>

### `IFX_AUTANALOG_AC_COND_CNT_DONE`

```c
#define IFX_AUTANALOG_AC_COND_CNT_DONE 3
```

计数器（Counter）完成。

<a id="a95a419e3ad5a371ca5f19d29267c32af"></a>

### `IFX_AUTANALOG_AC_COND_CTB0_CMP0`

```c
#define IFX_AUTANALOG_AC_COND_CTB0_CMP0 22
```

CTB0 比较器（Comparator）0。

<a id="a8a8ce0f1948fba25a2ea813285bcbc09"></a>

### `IFX_AUTANALOG_AC_COND_CTB0_CMP0_WAKE`

```c
#define IFX_AUTANALOG_AC_COND_CTB0_CMP0_WAKE 40
```

CTB0 比较器（Comparator）0 唤醒（Wakeup）。

<a id="a1565408f57589d89868af6946a166579"></a>

### `IFX_AUTANALOG_AC_COND_CTB0_CMP1`

```c
#define IFX_AUTANALOG_AC_COND_CTB0_CMP1 23
```

CTB0 比较器（Comparator）1。

<a id="a20fd04f8c8b7f026854ba1763e8fcfcc"></a>

### `IFX_AUTANALOG_AC_COND_CTB0_CMP1_WAKE`

```c
#define IFX_AUTANALOG_AC_COND_CTB0_CMP1_WAKE 41
```

CTB0 比较器（Comparator）1 唤醒（Wakeup）。

<a id="af6fe159448bb3dfd193ae322ee1bc4b3"></a>

### `IFX_AUTANALOG_AC_COND_CTB1_CMP0`

```c
#define IFX_AUTANALOG_AC_COND_CTB1_CMP0 24
```

CTB1 比较器（Comparator）0。

<a id="a9a349219e74dc9d36837c5428dd44101"></a>

### `IFX_AUTANALOG_AC_COND_CTB1_CMP0_WAKE`

```c
#define IFX_AUTANALOG_AC_COND_CTB1_CMP0_WAKE 42
```

CTB1 比较器（Comparator）0 唤醒（Wakeup）。

<a id="a586d60863ac4f2bd91832f89665592ef"></a>

### `IFX_AUTANALOG_AC_COND_CTB1_CMP1`

```c
#define IFX_AUTANALOG_AC_COND_CTB1_CMP1 25
```

CTB1 比较器（Comparator）1。

<a id="ade405959e09086dfeca9cbf9e6aaa202"></a>

### `IFX_AUTANALOG_AC_COND_CTB1_CMP1_WAKE`

```c
#define IFX_AUTANALOG_AC_COND_CTB1_CMP1_WAKE 43
```

CTB1 比较器（Comparator）1 唤醒（Wakeup）。

<a id="ae484cbe259da9d08860e760961ed829f"></a>

### `IFX_AUTANALOG_AC_COND_DAC0_EPOCH`

```c
#define IFX_AUTANALOG_AC_COND_DAC0_EPOCH 57
```

DAC0 波形结束（End of Waveform）。

<a id="af12dfd52c48f09d35be364b4e5bc1617"></a>

### `IFX_AUTANALOG_AC_COND_DAC0_RANGE0`

```c
#define IFX_AUTANALOG_AC_COND_DAC0_RANGE0 54
```

DAC0 范围（Range）0。

<a id="ae07d8b24de701bad184f9beb3698851d"></a>

### `IFX_AUTANALOG_AC_COND_DAC0_RANGE1`

```c
#define IFX_AUTANALOG_AC_COND_DAC0_RANGE1 55
```

DAC0 范围（Range）1。

<a id="a25fc05a14a4a21e2185b5055f8017271"></a>

### `IFX_AUTANALOG_AC_COND_DAC0_RANGE2`

```c
#define IFX_AUTANALOG_AC_COND_DAC0_RANGE2 56
```

DAC0 范围（Range）2。

<a id="a7309b7a779227c6e456e3907c503ee48"></a>

### `IFX_AUTANALOG_AC_COND_DAC0_STROBE`

```c
#define IFX_AUTANALOG_AC_COND_DAC0_STROBE 58
```

DAC0 选通信号（Strobe）。

<a id="a14bf63e7d2ccf70457ee0ee9b4b1d7f3"></a>

### `IFX_AUTANALOG_AC_COND_DAC1_EPOCH`

```c
#define IFX_AUTANALOG_AC_COND_DAC1_EPOCH 62
```

DAC1 波形结束（End of Waveform）。

<a id="a0c6abe9f92091e466eb0df6078c0e8af"></a>

### `IFX_AUTANALOG_AC_COND_DAC1_RANGE0`

```c
#define IFX_AUTANALOG_AC_COND_DAC1_RANGE0 59
```

DAC1 范围（Range）0。

<a id="a70cc4414203dfe097b78cc921bcb7e15"></a>

### `IFX_AUTANALOG_AC_COND_DAC1_RANGE1`

```c
#define IFX_AUTANALOG_AC_COND_DAC1_RANGE1 60
```

DAC1 范围（Range）1。

<a id="a80bef915de90959df5f8157beb00b3c6"></a>

### `IFX_AUTANALOG_AC_COND_DAC1_RANGE2`

```c
#define IFX_AUTANALOG_AC_COND_DAC1_RANGE2 61
```

DAC1 范围（Range）2。

<a id="a21f0ab3b02faca9ddb98f208ac4d15f2"></a>

### `IFX_AUTANALOG_AC_COND_DAC1_STROBE`

```c
#define IFX_AUTANALOG_AC_COND_DAC1_STROBE 63
```

DAC1 选通信号（Strobe）。

<a id="aed5d0fbe398ce34acad63b95e3c5cbcc"></a>

### `IFX_AUTANALOG_AC_COND_FALSE`

```c
#define IFX_AUTANALOG_AC_COND_FALSE 0
```

无条件为 FALSE。

<a id="a76e71d48761be7030d1b22976b7c8c6c"></a>

### `IFX_AUTANALOG_AC_COND_FIFO_LEVEL0`

```c
#define IFX_AUTANALOG_AC_COND_FIFO_LEVEL0 46
```

FIFO 水位（Level）0。

<a id="a4691fe493dc867fcf966a253f2bff58d"></a>

### `IFX_AUTANALOG_AC_COND_FIFO_LEVEL1`

```c
#define IFX_AUTANALOG_AC_COND_FIFO_LEVEL1 47
```

FIFO 水位（Level）1。

<a id="a3fd3b9dc60c33c6840ff5da7dd2358fe"></a>

### `IFX_AUTANALOG_AC_COND_FIFO_LEVEL2`

```c
#define IFX_AUTANALOG_AC_COND_FIFO_LEVEL2 48
```

FIFO 水位（Level）2。

<a id="a9c027c6caabf986451ca48a3a3198b5f"></a>

### `IFX_AUTANALOG_AC_COND_FIFO_LEVEL3`

```c
#define IFX_AUTANALOG_AC_COND_FIFO_LEVEL3 49
```

FIFO 水位（Level）3。

<a id="aed7d55553c6f9166e2b543c06f27c46a"></a>

### `IFX_AUTANALOG_AC_COND_FIFO_LEVEL4`

```c
#define IFX_AUTANALOG_AC_COND_FIFO_LEVEL4 50
```

FIFO 水位（Level）4。

<a id="ab2035282756f3beed8a28787d3e1162f"></a>

### `IFX_AUTANALOG_AC_COND_FIFO_LEVEL5`

```c
#define IFX_AUTANALOG_AC_COND_FIFO_LEVEL5 51
```

FIFO 水位（Level）5。

<a id="ae3c56b39c4b994ca6b2cad290dc1f1b9"></a>

### `IFX_AUTANALOG_AC_COND_FIFO_LEVEL6`

```c
#define IFX_AUTANALOG_AC_COND_FIFO_LEVEL6 52
```

FIFO 水位（Level）6。

<a id="a3e3bf3a3ed7320d4cb5006d8ceaa0253"></a>

### `IFX_AUTANALOG_AC_COND_FIFO_LEVEL7`

```c
#define IFX_AUTANALOG_AC_COND_FIFO_LEVEL7 53
```

FIFO 水位（Level）7。

<a id="ab418f84ff25774cfe1f0b57f0a3b7a0f"></a>

### `IFX_AUTANALOG_AC_COND_PTCOMP_CMP0`

```c
#define IFX_AUTANALOG_AC_COND_PTCOMP_CMP0 18
```

PTComp 比较器（Comparator）0。

<a id="a3487f8b03839d0013a0eff3a7170cd54"></a>

### `IFX_AUTANALOG_AC_COND_PTCOMP_CMP0_WAKE`

```c
#define IFX_AUTANALOG_AC_COND_PTCOMP_CMP0_WAKE 44
```

PTComp 比较器（Comparator）0 唤醒（Wakeup）。

<a id="a412a38e2b404209c527377a7b02561c6"></a>

### `IFX_AUTANALOG_AC_COND_PTCOMP_CMP1`

```c
#define IFX_AUTANALOG_AC_COND_PTCOMP_CMP1 19
```

PTComp 比较器（Comparator）1。

<a id="a97ed8d0e7c29eeb90e0a4ecf06b08f99"></a>

### `IFX_AUTANALOG_AC_COND_PTCOMP_CMP1_WAKE`

```c
#define IFX_AUTANALOG_AC_COND_PTCOMP_CMP1_WAKE 45
```

PTComp 比较器（Comparator）1 唤醒（Wakeup）。

<a id="a8b0374792e7d1955ddae33371438037a"></a>

### `IFX_AUTANALOG_AC_COND_PTCOMP_RANGE0`

```c
#define IFX_AUTANALOG_AC_COND_PTCOMP_RANGE0 20
```

PTComp 范围（Range）0。

<a id="ac91f91c7dca2835cf833f185407d8f87"></a>

### `IFX_AUTANALOG_AC_COND_PTCOMP_RANGE1`

```c
#define IFX_AUTANALOG_AC_COND_PTCOMP_RANGE1 21
```

PTComp 范围（Range）1。

<a id="a621175cf2e68b44c6fef037fddc65f9e"></a>

### `IFX_AUTANALOG_AC_COND_PTCOMP_STROBE0`

```c
#define IFX_AUTANALOG_AC_COND_PTCOMP_STROBE0 16
```

PTComp 选通信号（Strobe） 0。

<a id="aa080ad5e42f250537c7227f20f157fc3"></a>

### `IFX_AUTANALOG_AC_COND_PTCOMP_STROBE1`

```c
#define IFX_AUTANALOG_AC_COND_PTCOMP_STROBE1 17
```

PTComp 选通信号（Strobe） 1。

<a id="af7ec6c7e61b7f3abab0d4149c1e4f8af"></a>

### `IFX_AUTANALOG_AC_COND_SAR_BUSY`

```c
#define IFX_AUTANALOG_AC_COND_SAR_BUSY 10
```

逐次逼近（SAR）模块忙。

<a id="a62e782e610b33d131265902fe485e09b"></a>

### `IFX_AUTANALOG_AC_COND_SAR_DONE`

```c
#define IFX_AUTANALOG_AC_COND_SAR_DONE 4
```

逐次逼近（SAR）序列控制器（Sequencer）完成。

<a id="a485bf0b82b62a7528fb9373c0487b759"></a>

### `IFX_AUTANALOG_AC_COND_SAR_EOS`

```c
#define IFX_AUTANALOG_AC_COND_SAR_EOS 5
```

逐次逼近（SAR）扫描结束（End of Scan）。

<a id="a60a92c4f9e02a4077798c4440deb98ca"></a>

### `IFX_AUTANALOG_AC_COND_SAR_FIFO_DONE`

```c
#define IFX_AUTANALOG_AC_COND_SAR_FIFO_DONE 13
```

SAR 先进先出队列（FIFO）完成。

<a id="a1d98307dc3598eb3cbae4a7a4b8db586"></a>

### `IFX_AUTANALOG_AC_COND_SAR_FIR0_DONE`

```c
#define IFX_AUTANALOG_AC_COND_SAR_FIR0_DONE 11
```

SAR 有限脉冲响应滤波器（FIR）0 完成。

<a id="abcdba475a0708c252e60c26fb126da24"></a>

### `IFX_AUTANALOG_AC_COND_SAR_FIR0_FIFO_DONE`

```c
#define IFX_AUTANALOG_AC_COND_SAR_FIR0_FIFO_DONE 14
```

SAR FIR0 的先进先出队列（FIFO）完成。

<a id="a99e6eb9d40dd9242d5b5f6c30fbcd9f5"></a>

### `IFX_AUTANALOG_AC_COND_SAR_FIR1_DONE`

```c
#define IFX_AUTANALOG_AC_COND_SAR_FIR1_DONE 12
```

SAR 有限脉冲响应滤波器（FIR）1 完成。

<a id="afbb4ab6cba32780afc838d67cbadec41"></a>

### `IFX_AUTANALOG_AC_COND_SAR_FIR1_FIFO_DONE`

```c
#define IFX_AUTANALOG_AC_COND_SAR_FIR1_FIFO_DONE 15
```

SAR FIR1 的先进先出队列（FIFO）完成。

<a id="a21f6ddbe9d7db5fb214a94c51b773795"></a>

### `IFX_AUTANALOG_AC_COND_SAR_RANGE0`

```c
#define IFX_AUTANALOG_AC_COND_SAR_RANGE0 6
```

SAR 范围（Range）0 检测（Detection）。

<a id="a78ccdf5bcac7b8d65537f74516c49599"></a>

### `IFX_AUTANALOG_AC_COND_SAR_RANGE1`

```c
#define IFX_AUTANALOG_AC_COND_SAR_RANGE1 7
```

SAR 范围（Range）1 检测（Detection）。

<a id="ac90e195f22faba54e1a670e20c86437e"></a>

### `IFX_AUTANALOG_AC_COND_SAR_RANGE2`

```c
#define IFX_AUTANALOG_AC_COND_SAR_RANGE2 8
```

SAR 范围（Range）2 检测（Detection）。

<a id="a187aff8fac3d22f83af8b3981a3793fe"></a>

### `IFX_AUTANALOG_AC_COND_SAR_RANGE3`

```c
#define IFX_AUTANALOG_AC_COND_SAR_RANGE3 9
```

SAR 范围（Range）3 检测（Detection）。

<a id="a0d64c0bca00b8a34118c00548effa7a5"></a>

### `IFX_AUTANALOG_AC_COND_TIMER_DONE_WAKE`

```c
#define IFX_AUTANALOG_AC_COND_TIMER_DONE_WAKE 39
```

定时器唤醒（Timer Wakeup）。

<a id="a494f86e0974cfebc581cfa0ed60d7253"></a>

### `IFX_AUTANALOG_AC_COND_TR_IN0`

```c
#define IFX_AUTANALOG_AC_COND_TR_IN0 34
```

外部／固件触发（External/FW Trigger）0。

<a id="a56ce7b915574c39349c2b3198be6f025"></a>

### `IFX_AUTANALOG_AC_COND_TR_IN1`

```c
#define IFX_AUTANALOG_AC_COND_TR_IN1 35
```

外部／固件触发（External/FW Trigger）1。

<a id="a20cf5b28b473169f94f6298f79dfaa8d"></a>

### `IFX_AUTANALOG_AC_COND_TR_IN2`

```c
#define IFX_AUTANALOG_AC_COND_TR_IN2 36
```

外部／固件触发（External/FW Trigger）2。

<a id="a26f0d9b4d322a8d52822032df218b62b"></a>

### `IFX_AUTANALOG_AC_COND_TR_IN3`

```c
#define IFX_AUTANALOG_AC_COND_TR_IN3 37
```

外部／固件触发（External/FW Trigger）3。

<a id="aae7dfbb92ff1b17a70416df7f2eb4f26"></a>

### `IFX_AUTANALOG_AC_COND_TR_IN_WAKE`

```c
#define IFX_AUTANALOG_AC_COND_TR_IN_WAKE 38
```

外部触发唤醒（External Trigger Wakeup）。

<a id="a1ed711440c168a67a6ab2415c3756693"></a>

### `IFX_AUTANALOG_AC_COND_TRUE`

```c
#define IFX_AUTANALOG_AC_COND_TRUE 1
```

无条件为 TRUE。

<a id="a477ca97a0203a592d41ae7668973f080"></a>

### `IFX_AUTANALOG_AC_GPIO_OUT0`

```c
#define IFX_AUTANALOG_AC_GPIO_OUT0 0x1
```

GPIO 输出（Output）0。

<a id="a534e1d1894ac08f9e6a9924468604cf2"></a>

### `IFX_AUTANALOG_AC_GPIO_OUT1`

```c
#define IFX_AUTANALOG_AC_GPIO_OUT1 0x2
```

GPIO 输出（Output）1。

<a id="acf7d4d1698079affb4cd2e91e5796e33"></a>

### `IFX_AUTANALOG_AC_GPIO_OUT2`

```c
#define IFX_AUTANALOG_AC_GPIO_OUT2 0x4
```

GPIO 输出（Output）2。

<a id="abaafa051e64aef8a4603e9121cbbe2a4"></a>

### `IFX_AUTANALOG_AC_GPIO_OUT3`

```c
#define IFX_AUTANALOG_AC_GPIO_OUT3 0x8
```

GPIO 输出（Output）3。

<a id="ad752457ef1b2e3ce1e26e4eaf4e4ed4a"></a>

### `IFX_AUTANALOG_AC_GPIO_OUT_DISABLED`

```c
#define IFX_AUTANALOG_AC_GPIO_OUT_DISABLED 0x0
```

禁用 GPIO 输出控制（Output Control）。

<a id="a47217bf71a3cf0749da83fb41015898a"></a>

### `IFX_AUTANALOG_CTB_OA_GAIN_10_67`

```c
#define IFX_AUTANALOG_CTB_OA_GAIN_10_67 7
```

增益（Gain）10.67。

<a id="a4e70a9a2426ca7104516c959e935a234"></a>

### `IFX_AUTANALOG_CTB_OA_GAIN_16_00`

```c
#define IFX_AUTANALOG_CTB_OA_GAIN_16_00 8
```

增益（Gain）16.00。

<a id="a5075abf67c4f8cf0d8bec2b96a9972aa"></a>

### `IFX_AUTANALOG_CTB_OA_GAIN_1_00`

```c
#define IFX_AUTANALOG_CTB_OA_GAIN_1_00 0
```

增益（Gain）1.00。

<a id="a24c35b68bfa86e567d76af7e1d74b6af"></a>

### `IFX_AUTANALOG_CTB_OA_GAIN_1_42`

```c
#define IFX_AUTANALOG_CTB_OA_GAIN_1_42 1
```

增益（Gain）1.42。

<a id="aad4431885b89783c8469e7fcd82517dc"></a>

### `IFX_AUTANALOG_CTB_OA_GAIN_21_33`

```c
#define IFX_AUTANALOG_CTB_OA_GAIN_21_33 9
```

增益（Gain）21.33。

<a id="a47e4e2c1d49b14fdb9d37a8365ab5a12"></a>

### `IFX_AUTANALOG_CTB_OA_GAIN_2_00`

```c
#define IFX_AUTANALOG_CTB_OA_GAIN_2_00 2
```

增益（Gain）2.00。

<a id="a3d9dfd90ac5bd3680a6a1a1a81abe83d"></a>

### `IFX_AUTANALOG_CTB_OA_GAIN_2_78`

```c
#define IFX_AUTANALOG_CTB_OA_GAIN_2_78 3
```

增益（Gain）2.78。

<a id="aff9a5c27d21d4d66c8e41ce8b290ebca"></a>

### `IFX_AUTANALOG_CTB_OA_GAIN_32_00`

```c
#define IFX_AUTANALOG_CTB_OA_GAIN_32_00 10
```

增益（Gain）32.00。

<a id="aae5c58f8dc88257463f7f20cfd85b201"></a>

### `IFX_AUTANALOG_CTB_OA_GAIN_4_00`

```c
#define IFX_AUTANALOG_CTB_OA_GAIN_4_00 4
```

增益（Gain）4.00。

<a id="adfabe221c6c7837d97e93c8aff7141d7"></a>

### `IFX_AUTANALOG_CTB_OA_GAIN_5_82`

```c
#define IFX_AUTANALOG_CTB_OA_GAIN_5_82 5
```

增益（Gain）5.82。

<a id="aa56acd2ecf35cfd73ce7bdc65c561af5"></a>

### `IFX_AUTANALOG_CTB_OA_GAIN_8_00`

```c
#define IFX_AUTANALOG_CTB_OA_GAIN_8_00 6
```

增益（Gain）8.00。

<a id="aeff791aee43c37dda07cae0471f2f1bd"></a>

### `IFX_AUTANALOG_DAC_DIR_DISABLED`

```c
#define IFX_AUTANALOG_DAC_DIR_DISABLED 0
```

未选择方向（Direction）。

<a id="a2331afd96398c2f51f831c84f4ae1c23"></a>

### `IFX_AUTANALOG_DAC_DIR_FORWARD`

```c
#define IFX_AUTANALOG_DAC_DIR_FORWARD 1
```

正向／递增（Forward / Increment）。

<a id="ae4d3568dd6ea7f235d2499f489ed8bc3"></a>

### `IFX_AUTANALOG_DAC_DIR_REVERSE`

```c
#define IFX_AUTANALOG_DAC_DIR_REVERSE 2
```

反向／递减（Backward / Decrement）。


## 4.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P370_infineon-autanalog.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P003_zephyr__net__coap.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P005_zephyr__dt-bindings__mfd__infineon-hppass.h_文件参考.md)
