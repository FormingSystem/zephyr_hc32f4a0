---
id: learning.zephyr-docs.api-biometric-mesh-topic-reference.page-4
title: NXP S32 正交解码器（QDEC NXP S32）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__qdec__nxp__s32__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_NXP S32 正交解码器（QDEC NXP S32）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__qdec__nxp__s32__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

NXP S32 正交解码器的 TRGMUX 和 LCU 路由。

<a id="details"></a>

NXP S32 正交解码器的 TRGMUX 和 LCU 路由。

<a id="header-files"></a>
<a id="files"></a>

## 4.1\_文件（Files）

<a id="r_qdec_5Fnxp_5Fs32_2Eh"></a>

```c
file qdec_nxp_s32.h
```

相关声明：[qdec_nxp_s32.h](../api_file_mesh_acpi_reference/P008_zephyr__dt-bindings__sensor__qdec_nxp_s32.h_文件参考.md)。

the NXP S32 quadrature decoder的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 4.2\_逻辑触发编号（Logic Trigger Numbers）

`trgmux` 属性使用的逻辑触发标识符（Logic Trigger Identifiers）。

参见 `Trgmux_Ip_Init_PBcfg.h`。

<a id="r_ga5f90d651c87f9d2967cbeb6ed14107d4"></a>

```c
#define TRGMUX_LOGIC_GROUP_0_TRIGGER_0 (0)
```

相关声明：[TRGMUX_LOGIC_GROUP_0_TRIGGER_0](#ga5f90d651c87f9d2967cbeb6ed14107d4)。

逻辑触发（Logic Trigger）0。

<a id="r_gad58ca2f638326d20fa7d6e2f274aa781"></a>

```c
#define TRGMUX_LOGIC_GROUP_0_TRIGGER_1 (1)
```

相关声明：[TRGMUX_LOGIC_GROUP_0_TRIGGER_1](#gad58ca2f638326d20fa7d6e2f274aa781)。

逻辑触发（Logic Trigger）1。

<a id="r_ga5296f2a7a199ced206847e18829aa4ee"></a>

```c
#define TRGMUX_LOGIC_GROUP_1_TRIGGER_0 (2)
```

相关声明：[TRGMUX_LOGIC_GROUP_1_TRIGGER_0](#ga5296f2a7a199ced206847e18829aa4ee)。

逻辑触发（Logic Trigger）2。

<a id="r_ga1f3cdaf240b7aed64a20631eff68f01b"></a>

```c
#define TRGMUX_LOGIC_GROUP_1_TRIGGER_1 (3)
```

相关声明：[TRGMUX_LOGIC_GROUP_1_TRIGGER_1](#ga1f3cdaf240b7aed64a20631eff68f01b)。

逻辑触发（Logic Trigger）3。

## 4.3\_TRGMUX 硬件触发输入（Hardware Trigger Inputs）

`trgmux-io-config` 属性使用的 TRGMUX 触发输入标识符（Trigger Input Identifiers）。

参见 `Trgmux_Ip_Cfg_Defines.h`。

<a id="r_ga61c157ef6f63440cccfdc5c5a85fd310"></a>

```c
#define TRGMUX_IP_INPUT_SIUL2_IN0 (60)
```

相关声明：[TRGMUX_IP_INPUT_SIUL2_IN0](#ga61c157ef6f63440cccfdc5c5a85fd310)。

SIUL2 输入（Input）0。

<a id="r_gab6691aa9e2dd85d252c30c7992c0cc2d"></a>

```c
#define TRGMUX_IP_INPUT_SIUL2_IN1 (61)
```

相关声明：[TRGMUX_IP_INPUT_SIUL2_IN1](#gab6691aa9e2dd85d252c30c7992c0cc2d)。

SIUL2 输入（Input）1。

<a id="r_ga703797c0a4d2b3f2f19ae67a9170c1db"></a>

```c
#define TRGMUX_IP_INPUT_SIUL2_IN2 (62)
```

相关声明：[TRGMUX_IP_INPUT_SIUL2_IN2](#ga703797c0a4d2b3f2f19ae67a9170c1db)。

SIUL2 输入（Input）2。

<a id="r_ga32e367eaa554879dd6e3ddc28a524b25"></a>

```c
#define TRGMUX_IP_INPUT_SIUL2_IN3 (63)
```

相关声明：[TRGMUX_IP_INPUT_SIUL2_IN3](#ga32e367eaa554879dd6e3ddc28a524b25)。

SIUL2 输入（Input）3。

<a id="r_gad6aaa8c5e9d917871085993d82774d4e"></a>

```c
#define TRGMUX_IP_INPUT_SIUL2_IN4 (64)
```

相关声明：[TRGMUX_IP_INPUT_SIUL2_IN4](#gad6aaa8c5e9d917871085993d82774d4e)。

SIUL2 输入（Input）4。

<a id="r_gac8531ab44c60fd98dd55774e6b54033d"></a>

```c
#define TRGMUX_IP_INPUT_SIUL2_IN5 (65)
```

相关声明：[TRGMUX_IP_INPUT_SIUL2_IN5](#gac8531ab44c60fd98dd55774e6b54033d)。

SIUL2 输入（Input）5。

<a id="r_gaf8cd9167bfded6c453f75ddc0a5b38c8"></a>

```c
#define TRGMUX_IP_INPUT_SIUL2_IN6 (66)
```

相关声明：[TRGMUX_IP_INPUT_SIUL2_IN6](#gaf8cd9167bfded6c453f75ddc0a5b38c8)。

SIUL2 输入（Input）6。

<a id="r_gad80f66c40a4b87ef0a1ca4790969f9c2"></a>

```c
#define TRGMUX_IP_INPUT_SIUL2_IN7 (67)
```

相关声明：[TRGMUX_IP_INPUT_SIUL2_IN7](#gad80f66c40a4b87ef0a1ca4790969f9c2)。

SIUL2 输入（Input）7。

<a id="r_ga6ed1b02c78a353bb1e92a45190ad65b5"></a>

```c
#define TRGMUX_IP_INPUT_SIUL2_IN8 (68)
```

相关声明：[TRGMUX_IP_INPUT_SIUL2_IN8](#ga6ed1b02c78a353bb1e92a45190ad65b5)。

SIUL2 输入（Input）8。

<a id="r_gad42232cddb9dc1c2f38e1b9908fcebf4"></a>

```c
#define TRGMUX_IP_INPUT_SIUL2_IN9 (69)
```

相关声明：[TRGMUX_IP_INPUT_SIUL2_IN9](#gad42232cddb9dc1c2f38e1b9908fcebf4)。

SIUL2 输入（Input）9。

<a id="r_ga9b6afac0a7eafb1c04dbfb385c6d18f1"></a>

```c
#define TRGMUX_IP_INPUT_SIUL2_IN10 (70)
```

相关声明：[TRGMUX_IP_INPUT_SIUL2_IN10](#ga9b6afac0a7eafb1c04dbfb385c6d18f1)。

SIUL2 输入（Input）10。

<a id="r_gaa91e26818dd86f102a46a18287fde7e8"></a>

```c
#define TRGMUX_IP_INPUT_SIUL2_IN11 (71)
```

相关声明：[TRGMUX_IP_INPUT_SIUL2_IN11](#gaa91e26818dd86f102a46a18287fde7e8)。

SIUL2 输入（Input）11。

<a id="r_ga914e801b68356386d723ff0af1216b5d"></a>

```c
#define TRGMUX_IP_INPUT_SIUL2_IN12 (72)
```

相关声明：[TRGMUX_IP_INPUT_SIUL2_IN12](#ga914e801b68356386d723ff0af1216b5d)。

SIUL2 输入（Input）12。

<a id="r_gad51c25c87d50d86c12c8f93c8c88460d"></a>

```c
#define TRGMUX_IP_INPUT_SIUL2_IN13 (73)
```

相关声明：[TRGMUX_IP_INPUT_SIUL2_IN13](#gad51c25c87d50d86c12c8f93c8c88460d)。

SIUL2 输入（Input）13。

<a id="r_ga14de227e51575ec405f850632f33ace7"></a>

```c
#define TRGMUX_IP_INPUT_SIUL2_IN14 (74)
```

相关声明：[TRGMUX_IP_INPUT_SIUL2_IN14](#ga14de227e51575ec405f850632f33ace7)。

SIUL2 输入（Input）14。

<a id="r_ga6a45b83389117d94a7f653a15457289a"></a>

```c
#define TRGMUX_IP_INPUT_SIUL2_IN15 (75)
```

相关声明：[TRGMUX_IP_INPUT_SIUL2_IN15](#ga6a45b83389117d94a7f653a15457289a)。

SIUL2 输入（Input）15。

<a id="r_ga0482ac4e3ab453e2e0882551f32af165"></a>

```c
#define TRGMUX_IP_INPUT_LCU1_LC0_OUT_I0 (105)
```

相关声明：[TRGMUX_IP_INPUT_LCU1_LC0_OUT_I0](#ga0482ac4e3ab453e2e0882551f32af165)。

LCU1 LC0 输出（Output）0。

<a id="r_ga85cafa1adddad2741d57aa9a0038522f"></a>

```c
#define TRGMUX_IP_INPUT_LCU1_LC0_OUT_I1 (106)
```

相关声明：[TRGMUX_IP_INPUT_LCU1_LC0_OUT_I1](#ga85cafa1adddad2741d57aa9a0038522f)。

LCU1 LC0 输出（Output）1。

<a id="r_ga535b5e20ee7d59948612e7b4145af06a"></a>

```c
#define TRGMUX_IP_INPUT_LCU1_LC0_OUT_I2 (107)
```

相关声明：[TRGMUX_IP_INPUT_LCU1_LC0_OUT_I2](#ga535b5e20ee7d59948612e7b4145af06a)。

LCU1 LC0 输出（Output）2。

<a id="r_gae87282218e47f09eeaa8e89d49f68f8e"></a>

```c
#define TRGMUX_IP_INPUT_LCU1_LC0_OUT_I3 (108)
```

相关声明：[TRGMUX_IP_INPUT_LCU1_LC0_OUT_I3](#gae87282218e47f09eeaa8e89d49f68f8e)。

LCU1 LC0 输出（Output）3。

## 4.4\_TRGMUX 硬件触发输出（Hardware Trigger Outputs）

`trgmux-io-config` 属性使用的 TRGMUX 触发输出标识符（Trigger Output Identifiers）。

参见 `Trgmux_Ip_Cfg_Defines.h`。

<a id="r_ga348fb8f222fc47542785a9d9b264f2ca"></a>

```c
#define TRGMUX_IP_OUTPUT_LCU1_0_INP_I0 (144)
```

相关声明：[TRGMUX_IP_OUTPUT_LCU1_0_INP_I0](#ga348fb8f222fc47542785a9d9b264f2ca)。

LCU1 实例（Instance）0 的输入（Input）0。

<a id="r_ga6a7b3e2d83c1daaf28863a8bee4f93cc"></a>

```c
#define TRGMUX_IP_OUTPUT_LCU1_0_INP_I1 (145)
```

相关声明：[TRGMUX_IP_OUTPUT_LCU1_0_INP_I1](#ga6a7b3e2d83c1daaf28863a8bee4f93cc)。

LCU1 实例（Instance）0 的输入（Input）1。

<a id="r_gab7c7af569060a90b6918dc4779f222b9"></a>

```c
#define TRGMUX_IP_OUTPUT_LCU1_0_INP_I2 (146)
```

相关声明：[TRGMUX_IP_OUTPUT_LCU1_0_INP_I2](#gab7c7af569060a90b6918dc4779f222b9)。

LCU1 实例（Instance）0 的输入（Input）2。

<a id="r_ga36adf3458bdfd54f696e5e114dd75a21"></a>

```c
#define TRGMUX_IP_OUTPUT_LCU1_0_INP_I3 (147)
```

相关声明：[TRGMUX_IP_OUTPUT_LCU1_0_INP_I3](#ga36adf3458bdfd54f696e5e114dd75a21)。

LCU1 实例（Instance）0 的输入（Input）3。

<a id="r_ga2120ba38a6ca432e117e350621b30b21"></a>

```c
#define TRGMUX_IP_OUTPUT_EMIOS0_CH1_4_IPP_IND_CH1 (32)
```

相关声明：[TRGMUX_IP_OUTPUT_EMIOS0_CH1_4_IPP_IND_CH1](#ga2120ba38a6ca432e117e350621b30b21)。

eMIOS0 通道（Channel）1。

<a id="r_gabcef1065db27c4d5870661e64faf7fd2"></a>

```c
#define TRGMUX_IP_OUTPUT_EMIOS0_CH1_4_IPP_IND_CH2 (33)
```

相关声明：[TRGMUX_IP_OUTPUT_EMIOS0_CH1_4_IPP_IND_CH2](#gabcef1065db27c4d5870661e64faf7fd2)。

eMIOS0 通道（Channel）2。

<a id="r_ga3c997f6ddf11c7a69ce43855bad410f4"></a>

```c
#define TRGMUX_IP_OUTPUT_EMIOS0_CH1_4_IPP_IND_CH3 (34)
```

相关声明：[TRGMUX_IP_OUTPUT_EMIOS0_CH1_4_IPP_IND_CH3](#ga3c997f6ddf11c7a69ce43855bad410f4)。

eMIOS0 通道（Channel）3。

<a id="r_gad9a1b43a14a9f22c0c36a518813a7530"></a>

```c
#define TRGMUX_IP_OUTPUT_EMIOS0_CH1_4_IPP_IND_CH4 (35)
```

相关声明：[TRGMUX_IP_OUTPUT_EMIOS0_CH1_4_IPP_IND_CH4](#gad9a1b43a14a9f22c0c36a518813a7530)。

eMIOS0 通道（Channel）4。

<a id="r_ga3c1c025a09c31c81f29c85ac89e7676d"></a>

```c
#define TRGMUX_IP_OUTPUT_EMIOS0_CH5_9_IPP_IND_CH5 (36)
```

相关声明：[TRGMUX_IP_OUTPUT_EMIOS0_CH5_9_IPP_IND_CH5](#ga3c1c025a09c31c81f29c85ac89e7676d)。

eMIOS0 通道（Channel）5。

<a id="r_gab9bfc47c3cb99c8ba5b4231b8ae6adec"></a>

```c
#define TRGMUX_IP_OUTPUT_EMIOS0_CH5_9_IPP_IND_CH6 (37)
```

相关声明：[TRGMUX_IP_OUTPUT_EMIOS0_CH5_9_IPP_IND_CH6](#gab9bfc47c3cb99c8ba5b4231b8ae6adec)。

eMIOS0 通道（Channel）6。

<a id="r_ga8672923dcb7c73d45a46e3fc8042a819"></a>

```c
#define TRGMUX_IP_OUTPUT_EMIOS0_CH5_9_IPP_IND_CH7 (38)
```

相关声明：[TRGMUX_IP_OUTPUT_EMIOS0_CH5_9_IPP_IND_CH7](#ga8672923dcb7c73d45a46e3fc8042a819)。

eMIOS0 通道（Channel）7。

<a id="r_ga5c4417fc989cc7cfd341d1b271b08ef6"></a>

```c
#define TRGMUX_IP_OUTPUT_EMIOS0_CH5_9_IPP_IND_CH9 (39)
```

相关声明：[TRGMUX_IP_OUTPUT_EMIOS0_CH5_9_IPP_IND_CH9](#ga5c4417fc989cc7cfd341d1b271b08ef6)。

eMIOS0 通道（Channel）9。

<a id="r_ga6479a7d5293501ec23252187bf3c53a7"></a>

```c
#define TRGMUX_IP_OUTPUT_EMIOS0_CH10_13_IPP_IND_CH10 (40)
```

相关声明：[TRGMUX_IP_OUTPUT_EMIOS0_CH10_13_IPP_IND_CH10](#ga6479a7d5293501ec23252187bf3c53a7)。

eMIOS0 通道（Channel）10。

<a id="r_ga820b8f9c7d7e87b8e8bf69f8eb22eb9d"></a>

```c
#define TRGMUX_IP_OUTPUT_EMIOS0_CH10_13_IPP_IND_CH11 (41)
```

相关声明：[TRGMUX_IP_OUTPUT_EMIOS0_CH10_13_IPP_IND_CH11](#ga820b8f9c7d7e87b8e8bf69f8eb22eb9d)。

eMIOS0 通道（Channel）11。

<a id="r_gacd8405722de5780ee34fd070847e74c7"></a>

```c
#define TRGMUX_IP_OUTPUT_EMIOS0_CH10_13_IPP_IND_CH12 (42)
```

相关声明：[TRGMUX_IP_OUTPUT_EMIOS0_CH10_13_IPP_IND_CH12](#gacd8405722de5780ee34fd070847e74c7)。

eMIOS0 通道（Channel）12。

<a id="r_gafd6354704670c0245ab1ef5811f181a4"></a>

```c
#define TRGMUX_IP_OUTPUT_EMIOS0_CH10_13_IPP_IND_CH13 (43)
```

相关声明：[TRGMUX_IP_OUTPUT_EMIOS0_CH10_13_IPP_IND_CH13](#gafd6354704670c0245ab1ef5811f181a4)。

eMIOS0 通道（Channel）13。

<a id="r_ga1f274984088ec4260544e415ef49fb8f"></a>

```c
#define TRGMUX_IP_OUTPUT_EMIOS0_CH14_15_IPP_IND_CH14 (44)
```

相关声明：[TRGMUX_IP_OUTPUT_EMIOS0_CH14_15_IPP_IND_CH14](#ga1f274984088ec4260544e415ef49fb8f)。

eMIOS0 通道（Channel）14。

<a id="r_ga228ce57b6b3f265f4e265f07f49111f5"></a>

```c
#define TRGMUX_IP_OUTPUT_EMIOS0_CH14_15_IPP_IND_CH15 (45)
```

相关声明：[TRGMUX_IP_OUTPUT_EMIOS0_CH14_15_IPP_IND_CH15](#ga228ce57b6b3f265f4e265f07f49111f5)。

eMIOS0 通道（Channel）15。

## 4.5\_逻辑控制单元源多路复用选择（LCU Source Mux Selection）

设备树（Devicetree）属性 `lcu-mux-sel` 的取值。

参见 `Lcu_Ip_Cfg_Defines.h`。

<a id="r_ga1c95e6e44fcc063050abdfb12ff4a53d"></a>

```c
#define LCU_IP_MUX_SEL_LOGIC_0 (0)
```

相关声明：[LCU_IP_MUX_SEL_LOGIC_0](#ga1c95e6e44fcc063050abdfb12ff4a53d)。

恒定逻辑 0（Constant Logic 0）。

<a id="r_ga9c8968bc623e89af46b987b5a266cd7a"></a>

```c
#define LCU_IP_MUX_SEL_LU_IN_0 (1)
```

相关声明：[LCU_IP_MUX_SEL_LU_IN_0](#ga9c8968bc623e89af46b987b5a266cd7a)。

LCU 输入（Input）0。

<a id="r_ga1fcbbd535dde1ee1180bbdb1939ad6fb"></a>

```c
#define LCU_IP_MUX_SEL_LU_IN_1 (2)
```

相关声明：[LCU_IP_MUX_SEL_LU_IN_1](#ga1fcbbd535dde1ee1180bbdb1939ad6fb)。

LCU 输入（Input）1。

<a id="r_ga72bc02b3e8caeb349c8d083e9b355bbb"></a>

```c
#define LCU_IP_MUX_SEL_LU_IN_2 (3)
```

相关声明：[LCU_IP_MUX_SEL_LU_IN_2](#ga72bc02b3e8caeb349c8d083e9b355bbb)。

LCU 输入（Input）2。

<a id="r_gade15633475996e248b63c8c7bc0dd2e1"></a>

```c
#define LCU_IP_MUX_SEL_LU_IN_3 (4)
```

相关声明：[LCU_IP_MUX_SEL_LU_IN_3](#gade15633475996e248b63c8c7bc0dd2e1)。

LCU 输入（Input）3。

<a id="r_ga0749ee1d0b387050d93d4a5fd5ddbac3"></a>

```c
#define LCU_IP_MUX_SEL_LU_IN_4 (5)
```

相关声明：[LCU_IP_MUX_SEL_LU_IN_4](#ga0749ee1d0b387050d93d4a5fd5ddbac3)。

LCU 输入（Input）4。

<a id="r_gab4150fda8780a5dfadb4e10ed2d9a6ef"></a>

```c
#define LCU_IP_MUX_SEL_LU_IN_5 (6)
```

相关声明：[LCU_IP_MUX_SEL_LU_IN_5](#gab4150fda8780a5dfadb4e10ed2d9a6ef)。

LCU 输入（Input）5。

<a id="r_ga01649444e8d4869869adb0a1497d5891"></a>

```c
#define LCU_IP_MUX_SEL_LU_IN_6 (7)
```

相关声明：[LCU_IP_MUX_SEL_LU_IN_6](#ga01649444e8d4869869adb0a1497d5891)。

LCU 输入（Input）6。

<a id="r_gadd4bb12283b964051aadc44e91c64b4a"></a>

```c
#define LCU_IP_MUX_SEL_LU_IN_7 (8)
```

相关声明：[LCU_IP_MUX_SEL_LU_IN_7](#gadd4bb12283b964051aadc44e91c64b4a)。

LCU 输入（Input）7。

<a id="r_gadb1518b38831f5d630baa05e4318ac85"></a>

```c
#define LCU_IP_MUX_SEL_LU_IN_8 (9)
```

相关声明：[LCU_IP_MUX_SEL_LU_IN_8](#gadb1518b38831f5d630baa05e4318ac85)。

LCU 输入（Input）8。

<a id="r_gadec9096085fb58765a665d93df7f48c8"></a>

```c
#define LCU_IP_MUX_SEL_LU_IN_9 (10)
```

相关声明：[LCU_IP_MUX_SEL_LU_IN_9](#gadec9096085fb58765a665d93df7f48c8)。

LCU 输入（Input）9。

<a id="r_ga6150e58658fb96c507b7f837b7e80cd2"></a>

```c
#define LCU_IP_MUX_SEL_LU_IN_10 (11)
```

相关声明：[LCU_IP_MUX_SEL_LU_IN_10](#ga6150e58658fb96c507b7f837b7e80cd2)。

LCU 输入（Input）10。

<a id="r_ga5421da1bd5dda8549da581c84bbd264e"></a>

```c
#define LCU_IP_MUX_SEL_LU_IN_11 (12)
```

相关声明：[LCU_IP_MUX_SEL_LU_IN_11](#ga5421da1bd5dda8549da581c84bbd264e)。

LCU 输入（Input）11。

<a id="r_gaf717610f772ecd118bad267f1e7ef53a"></a>

```c
#define LCU_IP_MUX_SEL_LU_OUT_0 (13)
```

相关声明：[LCU_IP_MUX_SEL_LU_OUT_0](#gaf717610f772ecd118bad267f1e7ef53a)。

LCU 输出（Output）0。

<a id="r_ga806ae23bdcd235b5a8a4998dbf0645fc"></a>

```c
#define LCU_IP_MUX_SEL_LU_OUT_1 (14)
```

相关声明：[LCU_IP_MUX_SEL_LU_OUT_1](#ga806ae23bdcd235b5a8a4998dbf0645fc)。

LCU 输出（Output）1。

<a id="r_gaa7ddcb1426021d8d1cc885cf8887d771"></a>

```c
#define LCU_IP_MUX_SEL_LU_OUT_2 (15)
```

相关声明：[LCU_IP_MUX_SEL_LU_OUT_2](#gaa7ddcb1426021d8d1cc885cf8887d771)。

LCU 输出（Output）2。

<a id="r_gaccf4f6fa723e15466774dd08d119d530"></a>

```c
#define LCU_IP_MUX_SEL_LU_OUT_3 (16)
```

相关声明：[LCU_IP_MUX_SEL_LU_OUT_3](#gaccf4f6fa723e15466774dd08d119d530)。

LCU 输出（Output）3。

<a id="r_gaf248aa0bb1abd496568018bc2f831304"></a>

```c
#define LCU_IP_MUX_SEL_LU_OUT_4 (17)
```

相关声明：[LCU_IP_MUX_SEL_LU_OUT_4](#gaf248aa0bb1abd496568018bc2f831304)。

LCU 输出（Output）4。

<a id="r_ga38ea3916f289680c429509fa3689e7b2"></a>

```c
#define LCU_IP_MUX_SEL_LU_OUT_5 (18)
```

相关声明：[LCU_IP_MUX_SEL_LU_OUT_5](#ga38ea3916f289680c429509fa3689e7b2)。

LCU 输出（Output）5。

<a id="r_ga7d0cbe256823d47406ac5f8b9791373c"></a>

```c
#define LCU_IP_MUX_SEL_LU_OUT_6 (19)
```

相关声明：[LCU_IP_MUX_SEL_LU_OUT_6](#ga7d0cbe256823d47406ac5f8b9791373c)。

LCU 输出（Output）6。

<a id="r_gac24584f60b6cdb639365b0ec29c76911"></a>

```c
#define LCU_IP_MUX_SEL_LU_OUT_7 (20)
```

相关声明：[LCU_IP_MUX_SEL_LU_OUT_7](#gac24584f60b6cdb639365b0ec29c76911)。

LCU 输出（Output）7。

<a id="r_gaf68a610920eb13011d0ca82639938f6f"></a>

```c
#define LCU_IP_MUX_SEL_LU_OUT_8 (21)
```

相关声明：[LCU_IP_MUX_SEL_LU_OUT_8](#gaf68a610920eb13011d0ca82639938f6f)。

LCU 输出（Output）8。

<a id="r_ga6f8c4425dae4f35f7ce1230cb6f6ce35"></a>

```c
#define LCU_IP_MUX_SEL_LU_OUT_9 (22)
```

相关声明：[LCU_IP_MUX_SEL_LU_OUT_9](#ga6f8c4425dae4f35f7ce1230cb6f6ce35)。

LCU 输出（Output）9。

<a id="r_ga09da2f54cacb280bcef7bbcce0efa397"></a>

```c
#define LCU_IP_MUX_SEL_LU_OUT_10 (23)
```

相关声明：[LCU_IP_MUX_SEL_LU_OUT_10](#ga09da2f54cacb280bcef7bbcce0efa397)。

LCU 输出（Output）10。

<a id="r_gac5d851693a2174702cf4edf6da6d4d24"></a>

```c
#define LCU_IP_MUX_SEL_LU_OUT_11 (24)
```

相关声明：[LCU_IP_MUX_SEL_LU_OUT_11](#gac5d851693a2174702cf4edf6da6d4d24)。

LCU 输出（Output）11。

## 4.6\_逻辑控制单元输入（LCU Inputs）

设备树（Devicetree）属性 `lcu-input-idx` 的取值。

<a id="r_ga1d7a73016cff2d6bf94b31e45037c5a0"></a>

```c
#define LCU_IP_IN_0 (0)
```

相关声明：[LCU_IP_IN_0](#ga1d7a73016cff2d6bf94b31e45037c5a0)。

LCU 输入（Input）0。

<a id="r_gafd1723996331f68b68268a843c50ee0c"></a>

```c
#define LCU_IP_IN_1 (1)
```

相关声明：[LCU_IP_IN_1](#gafd1723996331f68b68268a843c50ee0c)。

LCU 输入（Input）1。

<a id="r_ga6a2dc4f41c360fd0ad995a2191c8b40e"></a>

```c
#define LCU_IP_IN_2 (2)
```

相关声明：[LCU_IP_IN_2](#ga6a2dc4f41c360fd0ad995a2191c8b40e)。

LCU 输入（Input）2。

<a id="r_gab7e7a15a25ee912e767cd0867eaec01d"></a>

```c
#define LCU_IP_IN_3 (3)
```

相关声明：[LCU_IP_IN_3](#gab7e7a15a25ee912e767cd0867eaec01d)。

LCU 输入（Input）3。

<a id="r_gaaea5ffc915bd68b1e2ed8c15e428d351"></a>

```c
#define LCU_IP_IN_4 (4)
```

相关声明：[LCU_IP_IN_4](#gaaea5ffc915bd68b1e2ed8c15e428d351)。

LCU 输入（Input）4。

<a id="r_gaa6f3c25854e873cd3cd909772b913b8c"></a>

```c
#define LCU_IP_IN_5 (5)
```

相关声明：[LCU_IP_IN_5](#gaa6f3c25854e873cd3cd909772b913b8c)。

LCU 输入（Input）5。

<a id="r_ga545cda428781141271bb9ae2fbe9ca86"></a>

```c
#define LCU_IP_IN_6 (6)
```

相关声明：[LCU_IP_IN_6](#ga545cda428781141271bb9ae2fbe9ca86)。

LCU 输入（Input）6。

<a id="r_gab60fbbce8800af816f90f86b2cf6edc2"></a>

```c
#define LCU_IP_IN_7 (7)
```

相关声明：[LCU_IP_IN_7](#gab60fbbce8800af816f90f86b2cf6edc2)。

LCU 输入（Input）7。

<a id="r_ga789de245fe9fac9348075d71fac666e0"></a>

```c
#define LCU_IP_IN_8 (8)
```

相关声明：[LCU_IP_IN_8](#ga789de245fe9fac9348075d71fac666e0)。

LCU 输入（Input）8。

<a id="r_gaa6051a5f0ad64dd49f7962b4712e9611"></a>

```c
#define LCU_IP_IN_9 (9)
```

相关声明：[LCU_IP_IN_9](#gaa6051a5f0ad64dd49f7962b4712e9611)。

LCU 输入（Input）9。

<a id="r_gad242f6e9c4c7d6b3ddd879f14e8efacd"></a>

```c
#define LCU_IP_IN_10 (10)
```

相关声明：[LCU_IP_IN_10](#gad242f6e9c4c7d6b3ddd879f14e8efacd)。

LCU 输入（Input）10。

<a id="r_ga74ccacec42db8439d36f7749e45b2bbe"></a>

```c
#define LCU_IP_IN_11 (11)
```

相关声明：[LCU_IP_IN_11](#ga74ccacec42db8439d36f7749e45b2bbe)。

LCU 输入（Input）11。

## 4.7\_详细说明（Detailed Documentation）

<a id="ga1d7a73016cff2d6bf94b31e45037c5a0"></a>

### `LCU_IP_IN_0`

```c
#define LCU_IP_IN_0 (0)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

LCU 输入（Input）0。

<a id="gafd1723996331f68b68268a843c50ee0c"></a>

### `LCU_IP_IN_1`

```c
#define LCU_IP_IN_1 (1)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

LCU 输入（Input）1。

<a id="gad242f6e9c4c7d6b3ddd879f14e8efacd"></a>

### `LCU_IP_IN_10`

```c
#define LCU_IP_IN_10 (10)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

LCU 输入（Input）10。

<a id="ga74ccacec42db8439d36f7749e45b2bbe"></a>

### `LCU_IP_IN_11`

```c
#define LCU_IP_IN_11 (11)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

LCU 输入（Input）11。

<a id="ga6a2dc4f41c360fd0ad995a2191c8b40e"></a>

### `LCU_IP_IN_2`

```c
#define LCU_IP_IN_2 (2)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

LCU 输入（Input）2。

<a id="gab7e7a15a25ee912e767cd0867eaec01d"></a>

### `LCU_IP_IN_3`

```c
#define LCU_IP_IN_3 (3)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

LCU 输入（Input）3。

<a id="gaaea5ffc915bd68b1e2ed8c15e428d351"></a>

### `LCU_IP_IN_4`

```c
#define LCU_IP_IN_4 (4)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

LCU 输入（Input）4。

<a id="gaa6f3c25854e873cd3cd909772b913b8c"></a>

### `LCU_IP_IN_5`

```c
#define LCU_IP_IN_5 (5)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

LCU 输入（Input）5。

<a id="ga545cda428781141271bb9ae2fbe9ca86"></a>

### `LCU_IP_IN_6`

```c
#define LCU_IP_IN_6 (6)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

LCU 输入（Input）6。

<a id="gab60fbbce8800af816f90f86b2cf6edc2"></a>

### `LCU_IP_IN_7`

```c
#define LCU_IP_IN_7 (7)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

LCU 输入（Input）7。

<a id="ga789de245fe9fac9348075d71fac666e0"></a>

### `LCU_IP_IN_8`

```c
#define LCU_IP_IN_8 (8)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

LCU 输入（Input）8。

<a id="gaa6051a5f0ad64dd49f7962b4712e9611"></a>

### `LCU_IP_IN_9`

```c
#define LCU_IP_IN_9 (9)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

LCU 输入（Input）9。

<a id="ga1c95e6e44fcc063050abdfb12ff4a53d"></a>

### `LCU_IP_MUX_SEL_LOGIC_0`

```c
#define LCU_IP_MUX_SEL_LOGIC_0 (0)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

恒定逻辑 0（Constant Logic 0）。

<a id="ga9c8968bc623e89af46b987b5a266cd7a"></a>

### `LCU_IP_MUX_SEL_LU_IN_0`

```c
#define LCU_IP_MUX_SEL_LU_IN_0 (1)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

LCU 输入（Input）0。

<a id="ga1fcbbd535dde1ee1180bbdb1939ad6fb"></a>

### `LCU_IP_MUX_SEL_LU_IN_1`

```c
#define LCU_IP_MUX_SEL_LU_IN_1 (2)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

LCU 输入（Input）1。

<a id="ga6150e58658fb96c507b7f837b7e80cd2"></a>

### `LCU_IP_MUX_SEL_LU_IN_10`

```c
#define LCU_IP_MUX_SEL_LU_IN_10 (11)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

LCU 输入（Input）10。

<a id="ga5421da1bd5dda8549da581c84bbd264e"></a>

### `LCU_IP_MUX_SEL_LU_IN_11`

```c
#define LCU_IP_MUX_SEL_LU_IN_11 (12)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

LCU 输入（Input）11。

<a id="ga72bc02b3e8caeb349c8d083e9b355bbb"></a>

### `LCU_IP_MUX_SEL_LU_IN_2`

```c
#define LCU_IP_MUX_SEL_LU_IN_2 (3)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

LCU 输入（Input）2。

<a id="gade15633475996e248b63c8c7bc0dd2e1"></a>

### `LCU_IP_MUX_SEL_LU_IN_3`

```c
#define LCU_IP_MUX_SEL_LU_IN_3 (4)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

LCU 输入（Input）3。

<a id="ga0749ee1d0b387050d93d4a5fd5ddbac3"></a>

### `LCU_IP_MUX_SEL_LU_IN_4`

```c
#define LCU_IP_MUX_SEL_LU_IN_4 (5)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

LCU 输入（Input）4。

<a id="gab4150fda8780a5dfadb4e10ed2d9a6ef"></a>

### `LCU_IP_MUX_SEL_LU_IN_5`

```c
#define LCU_IP_MUX_SEL_LU_IN_5 (6)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

LCU 输入（Input）5。

<a id="ga01649444e8d4869869adb0a1497d5891"></a>

### `LCU_IP_MUX_SEL_LU_IN_6`

```c
#define LCU_IP_MUX_SEL_LU_IN_6 (7)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

LCU 输入（Input）6。

<a id="gadd4bb12283b964051aadc44e91c64b4a"></a>

### `LCU_IP_MUX_SEL_LU_IN_7`

```c
#define LCU_IP_MUX_SEL_LU_IN_7 (8)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

LCU 输入（Input）7。

<a id="gadb1518b38831f5d630baa05e4318ac85"></a>

### `LCU_IP_MUX_SEL_LU_IN_8`

```c
#define LCU_IP_MUX_SEL_LU_IN_8 (9)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

LCU 输入（Input）8。

<a id="gadec9096085fb58765a665d93df7f48c8"></a>

### `LCU_IP_MUX_SEL_LU_IN_9`

```c
#define LCU_IP_MUX_SEL_LU_IN_9 (10)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

LCU 输入（Input）9。

<a id="gaf717610f772ecd118bad267f1e7ef53a"></a>

### `LCU_IP_MUX_SEL_LU_OUT_0`

```c
#define LCU_IP_MUX_SEL_LU_OUT_0 (13)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

LCU 输出（Output）0。

<a id="ga806ae23bdcd235b5a8a4998dbf0645fc"></a>

### `LCU_IP_MUX_SEL_LU_OUT_1`

```c
#define LCU_IP_MUX_SEL_LU_OUT_1 (14)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

LCU 输出（Output）1。

<a id="ga09da2f54cacb280bcef7bbcce0efa397"></a>

### `LCU_IP_MUX_SEL_LU_OUT_10`

```c
#define LCU_IP_MUX_SEL_LU_OUT_10 (23)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

LCU 输出（Output）10。

<a id="gac5d851693a2174702cf4edf6da6d4d24"></a>

### `LCU_IP_MUX_SEL_LU_OUT_11`

```c
#define LCU_IP_MUX_SEL_LU_OUT_11 (24)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

LCU 输出（Output）11。

<a id="gaa7ddcb1426021d8d1cc885cf8887d771"></a>

### `LCU_IP_MUX_SEL_LU_OUT_2`

```c
#define LCU_IP_MUX_SEL_LU_OUT_2 (15)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

LCU 输出（Output）2。

<a id="gaccf4f6fa723e15466774dd08d119d530"></a>

### `LCU_IP_MUX_SEL_LU_OUT_3`

```c
#define LCU_IP_MUX_SEL_LU_OUT_3 (16)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

LCU 输出（Output）3。

<a id="gaf248aa0bb1abd496568018bc2f831304"></a>

### `LCU_IP_MUX_SEL_LU_OUT_4`

```c
#define LCU_IP_MUX_SEL_LU_OUT_4 (17)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

LCU 输出（Output）4。

<a id="ga38ea3916f289680c429509fa3689e7b2"></a>

### `LCU_IP_MUX_SEL_LU_OUT_5`

```c
#define LCU_IP_MUX_SEL_LU_OUT_5 (18)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

LCU 输出（Output）5。

<a id="ga7d0cbe256823d47406ac5f8b9791373c"></a>

### `LCU_IP_MUX_SEL_LU_OUT_6`

```c
#define LCU_IP_MUX_SEL_LU_OUT_6 (19)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

LCU 输出（Output）6。

<a id="gac24584f60b6cdb639365b0ec29c76911"></a>

### `LCU_IP_MUX_SEL_LU_OUT_7`

```c
#define LCU_IP_MUX_SEL_LU_OUT_7 (20)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

LCU 输出（Output）7。

<a id="gaf68a610920eb13011d0ca82639938f6f"></a>

### `LCU_IP_MUX_SEL_LU_OUT_8`

```c
#define LCU_IP_MUX_SEL_LU_OUT_8 (21)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

LCU 输出（Output）8。

<a id="ga6f8c4425dae4f35f7ce1230cb6f6ce35"></a>

### `LCU_IP_MUX_SEL_LU_OUT_9`

```c
#define LCU_IP_MUX_SEL_LU_OUT_9 (22)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

LCU 输出（Output）9。

<a id="ga0482ac4e3ab453e2e0882551f32af165"></a>

### `TRGMUX_IP_INPUT_LCU1_LC0_OUT_I0`

```c
#define TRGMUX_IP_INPUT_LCU1_LC0_OUT_I0 (105)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

LCU1 LC0 输出（Output）0。

<a id="ga85cafa1adddad2741d57aa9a0038522f"></a>

### `TRGMUX_IP_INPUT_LCU1_LC0_OUT_I1`

```c
#define TRGMUX_IP_INPUT_LCU1_LC0_OUT_I1 (106)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

LCU1 LC0 输出（Output）1。

<a id="ga535b5e20ee7d59948612e7b4145af06a"></a>

### `TRGMUX_IP_INPUT_LCU1_LC0_OUT_I2`

```c
#define TRGMUX_IP_INPUT_LCU1_LC0_OUT_I2 (107)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

LCU1 LC0 输出（Output）2。

<a id="gae87282218e47f09eeaa8e89d49f68f8e"></a>

### `TRGMUX_IP_INPUT_LCU1_LC0_OUT_I3`

```c
#define TRGMUX_IP_INPUT_LCU1_LC0_OUT_I3 (108)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

LCU1 LC0 输出（Output）3。

<a id="ga61c157ef6f63440cccfdc5c5a85fd310"></a>

### `TRGMUX_IP_INPUT_SIUL2_IN0`

```c
#define TRGMUX_IP_INPUT_SIUL2_IN0 (60)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

SIUL2 输入（Input）0。

<a id="gab6691aa9e2dd85d252c30c7992c0cc2d"></a>

### `TRGMUX_IP_INPUT_SIUL2_IN1`

```c
#define TRGMUX_IP_INPUT_SIUL2_IN1 (61)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

SIUL2 输入（Input）1。

<a id="ga9b6afac0a7eafb1c04dbfb385c6d18f1"></a>

### `TRGMUX_IP_INPUT_SIUL2_IN10`

```c
#define TRGMUX_IP_INPUT_SIUL2_IN10 (70)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

SIUL2 输入（Input）10。

<a id="gaa91e26818dd86f102a46a18287fde7e8"></a>

### `TRGMUX_IP_INPUT_SIUL2_IN11`

```c
#define TRGMUX_IP_INPUT_SIUL2_IN11 (71)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

SIUL2 输入（Input）11。

<a id="ga914e801b68356386d723ff0af1216b5d"></a>

### `TRGMUX_IP_INPUT_SIUL2_IN12`

```c
#define TRGMUX_IP_INPUT_SIUL2_IN12 (72)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

SIUL2 输入（Input）12。

<a id="gad51c25c87d50d86c12c8f93c8c88460d"></a>

### `TRGMUX_IP_INPUT_SIUL2_IN13`

```c
#define TRGMUX_IP_INPUT_SIUL2_IN13 (73)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

SIUL2 输入（Input）13。

<a id="ga14de227e51575ec405f850632f33ace7"></a>

### `TRGMUX_IP_INPUT_SIUL2_IN14`

```c
#define TRGMUX_IP_INPUT_SIUL2_IN14 (74)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

SIUL2 输入（Input）14。

<a id="ga6a45b83389117d94a7f653a15457289a"></a>

### `TRGMUX_IP_INPUT_SIUL2_IN15`

```c
#define TRGMUX_IP_INPUT_SIUL2_IN15 (75)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

SIUL2 输入（Input）15。

<a id="ga703797c0a4d2b3f2f19ae67a9170c1db"></a>

### `TRGMUX_IP_INPUT_SIUL2_IN2`

```c
#define TRGMUX_IP_INPUT_SIUL2_IN2 (62)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

SIUL2 输入（Input）2。

<a id="ga32e367eaa554879dd6e3ddc28a524b25"></a>

### `TRGMUX_IP_INPUT_SIUL2_IN3`

```c
#define TRGMUX_IP_INPUT_SIUL2_IN3 (63)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

SIUL2 输入（Input）3。

<a id="gad6aaa8c5e9d917871085993d82774d4e"></a>

### `TRGMUX_IP_INPUT_SIUL2_IN4`

```c
#define TRGMUX_IP_INPUT_SIUL2_IN4 (64)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

SIUL2 输入（Input）4。

<a id="gac8531ab44c60fd98dd55774e6b54033d"></a>

### `TRGMUX_IP_INPUT_SIUL2_IN5`

```c
#define TRGMUX_IP_INPUT_SIUL2_IN5 (65)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

SIUL2 输入（Input）5。

<a id="gaf8cd9167bfded6c453f75ddc0a5b38c8"></a>

### `TRGMUX_IP_INPUT_SIUL2_IN6`

```c
#define TRGMUX_IP_INPUT_SIUL2_IN6 (66)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

SIUL2 输入（Input）6。

<a id="gad80f66c40a4b87ef0a1ca4790969f9c2"></a>

### `TRGMUX_IP_INPUT_SIUL2_IN7`

```c
#define TRGMUX_IP_INPUT_SIUL2_IN7 (67)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

SIUL2 输入（Input）7。

<a id="ga6ed1b02c78a353bb1e92a45190ad65b5"></a>

### `TRGMUX_IP_INPUT_SIUL2_IN8`

```c
#define TRGMUX_IP_INPUT_SIUL2_IN8 (68)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

SIUL2 输入（Input）8。

<a id="gad42232cddb9dc1c2f38e1b9908fcebf4"></a>

### `TRGMUX_IP_INPUT_SIUL2_IN9`

```c
#define TRGMUX_IP_INPUT_SIUL2_IN9 (69)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

SIUL2 输入（Input）9。

<a id="ga6479a7d5293501ec23252187bf3c53a7"></a>

### `TRGMUX_IP_OUTPUT_EMIOS0_CH10_13_IPP_IND_CH10`

```c
#define TRGMUX_IP_OUTPUT_EMIOS0_CH10_13_IPP_IND_CH10 (40)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

eMIOS0 通道（Channel）10。

<a id="ga820b8f9c7d7e87b8e8bf69f8eb22eb9d"></a>

### `TRGMUX_IP_OUTPUT_EMIOS0_CH10_13_IPP_IND_CH11`

```c
#define TRGMUX_IP_OUTPUT_EMIOS0_CH10_13_IPP_IND_CH11 (41)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

eMIOS0 通道（Channel）11。

<a id="gacd8405722de5780ee34fd070847e74c7"></a>

### `TRGMUX_IP_OUTPUT_EMIOS0_CH10_13_IPP_IND_CH12`

```c
#define TRGMUX_IP_OUTPUT_EMIOS0_CH10_13_IPP_IND_CH12 (42)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

eMIOS0 通道（Channel）12。

<a id="gafd6354704670c0245ab1ef5811f181a4"></a>

### `TRGMUX_IP_OUTPUT_EMIOS0_CH10_13_IPP_IND_CH13`

```c
#define TRGMUX_IP_OUTPUT_EMIOS0_CH10_13_IPP_IND_CH13 (43)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

eMIOS0 通道（Channel）13。

<a id="ga1f274984088ec4260544e415ef49fb8f"></a>

### `TRGMUX_IP_OUTPUT_EMIOS0_CH14_15_IPP_IND_CH14`

```c
#define TRGMUX_IP_OUTPUT_EMIOS0_CH14_15_IPP_IND_CH14 (44)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

eMIOS0 通道（Channel）14。

<a id="ga228ce57b6b3f265f4e265f07f49111f5"></a>

### `TRGMUX_IP_OUTPUT_EMIOS0_CH14_15_IPP_IND_CH15`

```c
#define TRGMUX_IP_OUTPUT_EMIOS0_CH14_15_IPP_IND_CH15 (45)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

eMIOS0 通道（Channel）15。

<a id="ga2120ba38a6ca432e117e350621b30b21"></a>

### `TRGMUX_IP_OUTPUT_EMIOS0_CH1_4_IPP_IND_CH1`

```c
#define TRGMUX_IP_OUTPUT_EMIOS0_CH1_4_IPP_IND_CH1 (32)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

eMIOS0 通道（Channel）1。

<a id="gabcef1065db27c4d5870661e64faf7fd2"></a>

### `TRGMUX_IP_OUTPUT_EMIOS0_CH1_4_IPP_IND_CH2`

```c
#define TRGMUX_IP_OUTPUT_EMIOS0_CH1_4_IPP_IND_CH2 (33)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

eMIOS0 通道（Channel）2。

<a id="ga3c997f6ddf11c7a69ce43855bad410f4"></a>

### `TRGMUX_IP_OUTPUT_EMIOS0_CH1_4_IPP_IND_CH3`

```c
#define TRGMUX_IP_OUTPUT_EMIOS0_CH1_4_IPP_IND_CH3 (34)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

eMIOS0 通道（Channel）3。

<a id="gad9a1b43a14a9f22c0c36a518813a7530"></a>

### `TRGMUX_IP_OUTPUT_EMIOS0_CH1_4_IPP_IND_CH4`

```c
#define TRGMUX_IP_OUTPUT_EMIOS0_CH1_4_IPP_IND_CH4 (35)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

eMIOS0 通道（Channel）4。

<a id="ga3c1c025a09c31c81f29c85ac89e7676d"></a>

### `TRGMUX_IP_OUTPUT_EMIOS0_CH5_9_IPP_IND_CH5`

```c
#define TRGMUX_IP_OUTPUT_EMIOS0_CH5_9_IPP_IND_CH5 (36)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

eMIOS0 通道（Channel）5。

<a id="gab9bfc47c3cb99c8ba5b4231b8ae6adec"></a>

### `TRGMUX_IP_OUTPUT_EMIOS0_CH5_9_IPP_IND_CH6`

```c
#define TRGMUX_IP_OUTPUT_EMIOS0_CH5_9_IPP_IND_CH6 (37)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

eMIOS0 通道（Channel）6。

<a id="ga8672923dcb7c73d45a46e3fc8042a819"></a>

### `TRGMUX_IP_OUTPUT_EMIOS0_CH5_9_IPP_IND_CH7`

```c
#define TRGMUX_IP_OUTPUT_EMIOS0_CH5_9_IPP_IND_CH7 (38)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

eMIOS0 通道（Channel）7。

<a id="ga5c4417fc989cc7cfd341d1b271b08ef6"></a>

### `TRGMUX_IP_OUTPUT_EMIOS0_CH5_9_IPP_IND_CH9`

```c
#define TRGMUX_IP_OUTPUT_EMIOS0_CH5_9_IPP_IND_CH9 (39)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

eMIOS0 通道（Channel）9。

<a id="ga348fb8f222fc47542785a9d9b264f2ca"></a>

### `TRGMUX_IP_OUTPUT_LCU1_0_INP_I0`

```c
#define TRGMUX_IP_OUTPUT_LCU1_0_INP_I0 (144)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

LCU1 实例（Instance）0 的输入（Input）0。

<a id="ga6a7b3e2d83c1daaf28863a8bee4f93cc"></a>

### `TRGMUX_IP_OUTPUT_LCU1_0_INP_I1`

```c
#define TRGMUX_IP_OUTPUT_LCU1_0_INP_I1 (145)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

LCU1 实例（Instance）0 的输入（Input）1。

<a id="gab7c7af569060a90b6918dc4779f222b9"></a>

### `TRGMUX_IP_OUTPUT_LCU1_0_INP_I2`

```c
#define TRGMUX_IP_OUTPUT_LCU1_0_INP_I2 (146)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

LCU1 实例（Instance）0 的输入（Input）2。

<a id="ga36adf3458bdfd54f696e5e114dd75a21"></a>

### `TRGMUX_IP_OUTPUT_LCU1_0_INP_I3`

```c
#define TRGMUX_IP_OUTPUT_LCU1_0_INP_I3 (147)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

LCU1 实例（Instance）0 的输入（Input）3。

<a id="ga5f90d651c87f9d2967cbeb6ed14107d4"></a>

### `TRGMUX_LOGIC_GROUP_0_TRIGGER_0`

```c
#define TRGMUX_LOGIC_GROUP_0_TRIGGER_0 (0)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

逻辑触发（Logic Trigger）0。

<a id="gad58ca2f638326d20fa7d6e2f274aa781"></a>

### `TRGMUX_LOGIC_GROUP_0_TRIGGER_1`

```c
#define TRGMUX_LOGIC_GROUP_0_TRIGGER_1 (1)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

逻辑触发（Logic Trigger）1。

<a id="ga5296f2a7a199ced206847e18829aa4ee"></a>

### `TRGMUX_LOGIC_GROUP_1_TRIGGER_0`

```c
#define TRGMUX_LOGIC_GROUP_1_TRIGGER_0 (2)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

逻辑触发（Logic Trigger）2。

<a id="ga1f3cdaf240b7aed64a20631eff68f01b"></a>

### `TRGMUX_LOGIC_GROUP_1_TRIGGER_1`

```c
#define TRGMUX_LOGIC_GROUP_1_TRIGGER_1 (3)
```

```c
#include <zephyr/dt-bindings/sensor/qdec_nxp_s32.h>
```

逻辑触发（Logic Trigger）3。


## 4.8\_原页交叉引用（Cross References）

- [qdec_nxp_s32.h](../api_file_mesh_acpi_reference/P008_zephyr__dt-bindings__sensor__qdec_nxp_s32.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P003_LSM9DS1 API主题.md) · [返回大纲](大纲.md)
