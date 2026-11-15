---
id: learning.zephyr-docs.api-file-network-pcie-reference.page-4
title: zephyr__dt-bindings__opamp__infineon-autanalog-ctb.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctb_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_zephyr\_\_dt-bindings\_\_opamp\_\_infineon-autanalog-ctb.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/infineon-autanalog-ctb_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Infineon AutAnalog CTB的设备树绑定常量（Devicetree Binding Constants）。

查看此文件的源码。

<a id="details"></a>

Infineon AutAnalog 连续时间模块（Continuous-Time Block，CTB）的设备树绑定常量（Devicetree Binding Constants）。这些常量与外设驱动库（Peripheral Driver Library，PDL）的枚举值一致，用于配置 AutAnalog CTB 运算放大器（Opamp）和比较器（Comparator）功能的设备树属性。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 4.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 运算放大器功耗模式（Opamp power modes (cy_en_autanalog_ctb_oa_pwr_t)）

<a id="r_ad52f76f54d24f1b8b134afe782270087"></a>

```c
#define IFX_AUTANALOG_CTB_OA_PWR_OFF 0
```

相关声明：[IFX_AUTANALOG_CTB_OA_PWR_OFF](#ad52f76f54d24f1b8b134afe782270087)。

运算放大器（Opamp）断电。

<a id="r_ad784a0b04e92698c468e4fcfb4fd3019"></a>

```c
#define IFX_AUTANALOG_CTB_OA_PWR_ULTRA_LOW 1
```

相关声明：[IFX_AUTANALOG_CTB_OA_PWR_ULTRA_LOW](#ad784a0b04e92698c468e4fcfb4fd3019)。

超低功耗（Ultra Low Power），电荷泵（Charge Pump）关闭。

<a id="r_ac8eccf96dddbd602b2bf00a0325bd28e"></a>

```c
#define IFX_AUTANALOG_CTB_OA_PWR_ULTRA_LOW_RAIL 2
```

相关声明：[IFX_AUTANALOG_CTB_OA_PWR_ULTRA_LOW_RAIL](#ac8eccf96dddbd602b2bf00a0325bd28e)。

超低功耗（Ultra Low Power），电荷泵（Charge Pump）开启。

<a id="r_ad63c1eb722a575cff3525c3bf80a03d3"></a>

```c
#define IFX_AUTANALOG_CTB_OA_PWR_LOW_RAIL 4
```

相关声明：[IFX_AUTANALOG_CTB_OA_PWR_LOW_RAIL](#ad63c1eb722a575cff3525c3bf80a03d3)。

低功耗（Low Power），电荷泵（Charge Pump）开启。

<a id="r_a7723cec22a9a04f1afa2648e379f22a9"></a>

```c
#define IFX_AUTANALOG_CTB_OA_PWR_MEDIUM_RAIL 6
```

相关声明：[IFX_AUTANALOG_CTB_OA_PWR_MEDIUM_RAIL](#a7723cec22a9a04f1afa2648e379f22a9)。

中等功耗（Medium Power），电荷泵（Charge Pump）开启。

<a id="r_ad9a640a1e8191a29f9be2cf6e72d5661"></a>

```c
#define IFX_AUTANALOG_CTB_OA_PWR_HIGH_RAIL 8
```

相关声明：[IFX_AUTANALOG_CTB_OA_PWR_HIGH_RAIL](#ad9a640a1e8191a29f9be2cf6e72d5661)。

高功耗（High Power），电荷泵（Charge Pump）开启。

<a id="r_ab6264b440cc317ca9b6b4a52b66c17f1"></a>

```c
#define IFX_AUTANALOG_CTB_OA_PWR_ULTRA_HIGH_RAIL 10
```

相关声明：[IFX_AUTANALOG_CTB_OA_PWR_ULTRA_HIGH_RAIL](#ab6264b440cc317ca9b6b4a52b66c17f1)。

超高功耗（Ultra High Power），电荷泵（Charge Pump）开启。

<a id="define-members-1"></a>

### 运算放大器拓扑（Opamp topologies (cy_en_autanalog_ctb_oa_topo_t)）

<a id="r_a8fc46b275e0bc269eccf72fe65456532"></a>

```c
#define IFX_AUTANALOG_CTB_OA_TOPO_COMPARATOR 0
```

相关声明：[IFX_AUTANALOG_CTB_OA_TOPO_COMPARATOR](#a8fc46b275e0bc269eccf72fe65456532)。

比较器拓扑（Comparator Topology）。

<a id="r_a67da79c30e9798e6b33d7ae1a3d651ec"></a>

```c
#define IFX_AUTANALOG_CTB_OA_TOPO_PGA 1
```

相关声明：[IFX_AUTANALOG_CTB_OA_TOPO_PGA](#a67da79c30e9798e6b33d7ae1a3d651ec)。

可编程增益放大器拓扑（Programmable Gain Amplifier Topology）。

<a id="r_ac3ad453d628645409b6eba50d58c8208"></a>

```c
#define IFX_AUTANALOG_CTB_OA_TOPO_TIA 2
```

相关声明：[IFX_AUTANALOG_CTB_OA_TOPO_TIA](#ac3ad453d628645409b6eba50d58c8208)。

跨阻放大器拓扑（Transimpedance Amplifier Topology）。

<a id="r_ab127787012ef36285ee17f8875a26022"></a>

```c
#define IFX_AUTANALOG_CTB_OA_TOPO_OPEN_LOOP_OPAMP 3
```

相关声明：[IFX_AUTANALOG_CTB_OA_TOPO_OPEN_LOOP_OPAMP](#ab127787012ef36285ee17f8875a26022)。

开环运算放大器拓扑（Open-Loop Opamp Topology）。

<a id="r_a34598608d43923b48a0fbf2832867a28"></a>

```c
#define IFX_AUTANALOG_CTB_OA_TOPO_DIFF_AMPLIFIER 4
```

相关声明：[IFX_AUTANALOG_CTB_OA_TOPO_DIFF_AMPLIFIER](#a34598608d43923b48a0fbf2832867a28)。

差分放大器拓扑（Differential Amplifier Topology）。

<a id="r_a40db30a0852ac2d6860db3f56357f5ab"></a>

```c
#define IFX_AUTANALOG_CTB_OA_TOPO_HYST_COMPARATOR 5
```

相关声明：[IFX_AUTANALOG_CTB_OA_TOPO_HYST_COMPARATOR](#a40db30a0852ac2d6860db3f56357f5ab)。

迟滞比较器拓扑（Hysteresis Comparator Topology）。

<a id="r_aaad55877b78bd49dc8ae5f2ce07a4145"></a>

```c
#define IFX_AUTANALOG_CTB_OA_TOPO_BUFFER 6
```

相关声明：[IFX_AUTANALOG_CTB_OA_TOPO_BUFFER](#aaad55877b78bd49dc8ae5f2ce07a4145)。

电压跟随器／缓冲器拓扑（Voltage Follower / Buffer Topology）。

<a id="define-members-2"></a>

### 比较器中断与边沿检测模式（Comparator interrupt and edge detection modes (cy_en_autanalog_ctb_comp_int_t)）

<a id="r_a61073cdd5c4ac0588ac4509a76bb4650"></a>

```c
#define IFX_AUTANALOG_CTB_COMP_INT_DISABLED 0
```

相关声明：[IFX_AUTANALOG_CTB_COMP_INT_DISABLED](#a61073cdd5c4ac0588ac4509a76bb4650)。

中断已禁用（Interrupt Disabled）。

<a id="r_a20ead2bbf4207733f6ea909010c2689b"></a>

```c
#define IFX_AUTANALOG_CTB_COMP_INT_EDGE_RISING 1
```

相关声明：[IFX_AUTANALOG_CTB_COMP_INT_EDGE_RISING](#a20ead2bbf4207733f6ea909010c2689b)。

上升沿检测（Rising Edge Detection）。

<a id="r_a69279743fc840b07757feff795d2d58c"></a>

```c
#define IFX_AUTANALOG_CTB_COMP_INT_EDGE_FALLING 2
```

相关声明：[IFX_AUTANALOG_CTB_COMP_INT_EDGE_FALLING](#a69279743fc840b07757feff795d2d58c)。

下降沿检测（Falling Edge Detection）。

<a id="r_a8041e94459e325b36d252ad2d47e81ae"></a>

```c
#define IFX_AUTANALOG_CTB_COMP_INT_EDGE_BOTH 3
```

相关声明：[IFX_AUTANALOG_CTB_COMP_INT_EDGE_BOTH](#a8041e94459e325b36d252ad2d47e81ae)。

双边沿检测（Both-edge Detection）。

<a id="define-members-3"></a>

### 反馈电容（Feedback capacitor (cy_en_autanalog_ctb_oa_fb_cap_t)）

<a id="r_a6f0cdff51fc7888abf2b53ae0a16ec3c"></a>

```c
#define IFX_AUTANALOG_CTB_OA_FB_CAP_0_pF 0
```

相关声明：[IFX_AUTANALOG_CTB_OA_FB_CAP_0_pF](#a6f0cdff51fc7888abf2b53ae0a16ec3c)。

0.0 pF 反馈电容（Feedback Capacitor）。

<a id="r_ad51cc393be793c1961826e37463c9152"></a>

```c
#define IFX_AUTANALOG_CTB_OA_FB_CAP_0_7_pF 1
```

相关声明：[IFX_AUTANALOG_CTB_OA_FB_CAP_0_7_pF](#ad51cc393be793c1961826e37463c9152)。

0.7 pF 反馈电容（Feedback Capacitor）。

<a id="r_ab9043f15c03eb29bcdedcc39e40314b8"></a>

```c
#define IFX_AUTANALOG_CTB_OA_FB_CAP_1_4_pF 2
```

相关声明：[IFX_AUTANALOG_CTB_OA_FB_CAP_1_4_pF](#ab9043f15c03eb29bcdedcc39e40314b8)。

1.4 pF 反馈电容（Feedback Capacitor）。

<a id="r_a7aac9d2fb1ae1138b9c84453e8cf3a60"></a>

```c
#define IFX_AUTANALOG_CTB_OA_FB_CAP_2_1_pF 3
```

相关声明：[IFX_AUTANALOG_CTB_OA_FB_CAP_2_1_pF](#a7aac9d2fb1ae1138b9c84453e8cf3a60)。

2.1 pF 反馈电容（Feedback Capacitor）。

<a id="r_af60e61caee6217e3a7bb883a3be49112"></a>

```c
#define IFX_AUTANALOG_CTB_OA_FB_CAP_2_8_pF 4
```

相关声明：[IFX_AUTANALOG_CTB_OA_FB_CAP_2_8_pF](#af60e61caee6217e3a7bb883a3be49112)。

2.8 pF 反馈电容（Feedback Capacitor）。

<a id="r_a222835d10b33feda5035581ad5222494"></a>

```c
#define IFX_AUTANALOG_CTB_OA_FB_CAP_3_5_pF 5
```

相关声明：[IFX_AUTANALOG_CTB_OA_FB_CAP_3_5_pF](#a222835d10b33feda5035581ad5222494)。

3.5 pF 反馈电容（Feedback Capacitor）。

<a id="r_a2534b6da595f1077eeca9dd13f06a246"></a>

```c
#define IFX_AUTANALOG_CTB_OA_FB_CAP_4_2_pF 6
```

相关声明：[IFX_AUTANALOG_CTB_OA_FB_CAP_4_2_pF](#a2534b6da595f1077eeca9dd13f06a246)。

4.2 pF 反馈电容（Feedback Capacitor）。

<a id="r_aba06d7236a7d2880818a1b6df3baa334"></a>

```c
#define IFX_AUTANALOG_CTB_OA_FB_CAP_4_9_pF 7
```

相关声明：[IFX_AUTANALOG_CTB_OA_FB_CAP_4_9_pF](#aba06d7236a7d2880818a1b6df3baa334)。

4.9 pF 反馈电容（Feedback Capacitor）。

<a id="r_adea95be3992fbdc7ce7545bd533098ab"></a>

```c
#define IFX_AUTANALOG_CTB_OA_FB_CAP_5_6_pF 8
```

相关声明：[IFX_AUTANALOG_CTB_OA_FB_CAP_5_6_pF](#adea95be3992fbdc7ce7545bd533098ab)。

5.6 pF 反馈电容（Feedback Capacitor）。

<a id="r_a2ea399f41f13ab20d45315958e118cf2"></a>

```c
#define IFX_AUTANALOG_CTB_OA_FB_CAP_6_3_pF 9
```

相关声明：[IFX_AUTANALOG_CTB_OA_FB_CAP_6_3_pF](#a2ea399f41f13ab20d45315958e118cf2)。

6.3 pF 反馈电容（Feedback Capacitor）。

<a id="r_ad0212a254c3c338fe8c29bffcc23b2ed"></a>

```c
#define IFX_AUTANALOG_CTB_OA_FB_CAP_7_0_pF 10
```

相关声明：[IFX_AUTANALOG_CTB_OA_FB_CAP_7_0_pF](#ad0212a254c3c338fe8c29bffcc23b2ed)。

7.0 pF 反馈电容（Feedback Capacitor）。

<a id="r_ad956fdf03ae4bf3d479173252288defa"></a>

```c
#define IFX_AUTANALOG_CTB_OA_FB_CAP_7_7_pF 11
```

相关声明：[IFX_AUTANALOG_CTB_OA_FB_CAP_7_7_pF](#ad956fdf03ae4bf3d479173252288defa)。

7.7 pF 反馈电容（Feedback Capacitor）。

<a id="r_a2cd1e9e298b026af54a07a7f724f4d09"></a>

```c
#define IFX_AUTANALOG_CTB_OA_FB_CAP_8_4_pF 12
```

相关声明：[IFX_AUTANALOG_CTB_OA_FB_CAP_8_4_pF](#a2cd1e9e298b026af54a07a7f724f4d09)。

8.4 pF 反馈电容（Feedback Capacitor）。

<a id="r_a903a351fbf6b2e51ebce1e35a112cf9b"></a>

```c
#define IFX_AUTANALOG_CTB_OA_FB_CAP_9_1_pF 13
```

相关声明：[IFX_AUTANALOG_CTB_OA_FB_CAP_9_1_pF](#a903a351fbf6b2e51ebce1e35a112cf9b)。

9.1 pF 反馈电容（Feedback Capacitor）。

<a id="r_aec250b3752da26851b694413e84e5ae6"></a>

```c
#define IFX_AUTANALOG_CTB_OA_FB_CAP_9_8_pF 14
```

相关声明：[IFX_AUTANALOG_CTB_OA_FB_CAP_9_8_pF](#aec250b3752da26851b694413e84e5ae6)。

9.8 pF 反馈电容（Feedback Capacitor）。

<a id="r_a860045afab252c9c4628d50774ffd3b4"></a>

```c
#define IFX_AUTANALOG_CTB_OA_FB_CAP_10_5_pF 15
```

相关声明：[IFX_AUTANALOG_CTB_OA_FB_CAP_10_5_pF](#a860045afab252c9c4628d50774ffd3b4)。

10.5 pF 反馈电容（Feedback Capacitor）。

<a id="define-members-4"></a>

### 补偿电容（Compensation capacitor (cy_en_autanalog_ctb_oa_cc_cap_t)）

<a id="r_a7d1f17dbdd2d1a6ff9c84431b21f5182"></a>

```c
#define IFX_AUTANALOG_CTB_OA_CC_CAP_0_1_pF 0
```

相关声明：[IFX_AUTANALOG_CTB_OA_CC_CAP_0_1_pF](#a7d1f17dbdd2d1a6ff9c84431b21f5182)。

0.1 pF 补偿电容（Compensation Capacitor）。

<a id="r_a6f354e7448f0d0af7ca7f8e5890405f4"></a>

```c
#define IFX_AUTANALOG_CTB_OA_CC_CAP_1_1_pF 1
```

相关声明：[IFX_AUTANALOG_CTB_OA_CC_CAP_1_1_pF](#a6f354e7448f0d0af7ca7f8e5890405f4)。

1.1 pF 补偿电容（Compensation Capacitor）。

<a id="r_abd1506959b9e1d85c32715175831f772"></a>

```c
#define IFX_AUTANALOG_CTB_OA_CC_CAP_2_1_pF 2
```

相关声明：[IFX_AUTANALOG_CTB_OA_CC_CAP_2_1_pF](#abd1506959b9e1d85c32715175831f772)。

2.1 pF 补偿电容（Compensation Capacitor）。

<a id="r_a7f73e6402eba49e7ecfed0d1fb74e8c1"></a>

```c
#define IFX_AUTANALOG_CTB_OA_CC_CAP_3_1_pF 3
```

相关声明：[IFX_AUTANALOG_CTB_OA_CC_CAP_3_1_pF](#a7f73e6402eba49e7ecfed0d1fb74e8c1)。

3.1 pF 补偿电容（Compensation Capacitor）。

<a id="r_a1d6b0cd1b162b2e5ce727aa108324595"></a>

```c
#define IFX_AUTANALOG_CTB_OA_CC_CAP_4_1_pF 4
```

相关声明：[IFX_AUTANALOG_CTB_OA_CC_CAP_4_1_pF](#a1d6b0cd1b162b2e5ce727aa108324595)。

4.1 pF 补偿电容（Compensation Capacitor）。

<a id="r_a173591ef72608bf8242739978e3195a5"></a>

```c
#define IFX_AUTANALOG_CTB_OA_CC_CAP_5_1_pF 5
```

相关声明：[IFX_AUTANALOG_CTB_OA_CC_CAP_5_1_pF](#a173591ef72608bf8242739978e3195a5)。

5.1 pF 补偿电容（Compensation Capacitor）。

<a id="r_a5eb4d75542f6651edc366a393bffd225"></a>

```c
#define IFX_AUTANALOG_CTB_OA_CC_CAP_6_1_pF 6
```

相关声明：[IFX_AUTANALOG_CTB_OA_CC_CAP_6_1_pF](#a5eb4d75542f6651edc366a393bffd225)。

6.1 pF 补偿电容（Compensation Capacitor）。

<a id="r_a134c74701eaad5ac9a0459d3d8be7f1d"></a>

```c
#define IFX_AUTANALOG_CTB_OA_CC_CAP_7_1_pF 7
```

相关声明：[IFX_AUTANALOG_CTB_OA_CC_CAP_7_1_pF](#a134c74701eaad5ac9a0459d3d8be7f1d)。

7.1 pF 补偿电容（Compensation Capacitor）。

<a id="r_af71671b3f49f3dfd69304430c48d4494"></a>

```c
#define IFX_AUTANALOG_CTB_OA_CC_CAP_DISABLED 8
```

相关声明：[IFX_AUTANALOG_CTB_OA_CC_CAP_DISABLED](#af71671b3f49f3dfd69304430c48d4494)。

禁用补偿电容（Compensation Capacitor）。

<a id="define-members-5"></a>

### 同相输入引脚连接（Non-inverting input pin connection (cy_en_autanalog_ctb_oa_ninv_pin_t)）

<a id="r_ac2043c2e03ec5ed504cbddb80f5cf219"></a>

```c
#define IFX_AUTANALOG_CTB_OA_NINV_PIN_DISCONNECT 0
```

相关声明：[IFX_AUTANALOG_CTB_OA_NINV_PIN_DISCONNECT](#ac2043c2e03ec5ed504cbddb80f5cf219)。

引脚断开连接（Pin Disconnected）。

<a id="r_ac86aa8ae834d504871217f78b4dc6b93"></a>

```c
#define IFX_AUTANALOG_CTB_OA_NINV_PIN_OA0_P0_OA1_P5 1
```

相关声明：[IFX_AUTANALOG_CTB_OA_NINV_PIN_OA0_P0_OA1_P5](#ac86aa8ae834d504871217f78b4dc6b93)。

OA0 的 P0 引脚或 OA1 的 P5 引脚（Pin）。

<a id="r_aabfc18593242d54ef4307339bc9f15f4"></a>

```c
#define IFX_AUTANALOG_CTB_OA_NINV_PIN_OA0_P1_OA1_P4 2
```

相关声明：[IFX_AUTANALOG_CTB_OA_NINV_PIN_OA0_P1_OA1_P4](#aabfc18593242d54ef4307339bc9f15f4)。

OA0 的 P1 引脚或 OA1 的 P4 引脚（Pin）。

<a id="define-members-6"></a>

### 同相输入参考源连接（Non-inverting input reference connection (cy_en_autanalog_ctb_oa_ninv_ref_t)）

<a id="r_a526900d4934c85775c660e059821a88f"></a>

```c
#define IFX_AUTANALOG_CTB_OA_NINV_REF_DISCONNECT 0
```

相关声明：[IFX_AUTANALOG_CTB_OA_NINV_REF_DISCONNECT](#a526900d4934c85775c660e059821a88f)。

参考源断开连接（Reference Disconnected）。

<a id="r_a8a4f93898b6b25a3d102323714db034b"></a>

```c
#define IFX_AUTANALOG_CTB_OA_NINV_REF_DAC0 1
```

相关声明：[IFX_AUTANALOG_CTB_OA_NINV_REF_DAC0](#a8a4f93898b6b25a3d102323714db034b)。

DAC0 输出（Output）。

<a id="r_ae701bf2f2d9eb10619abb040f58dbd4b"></a>

```c
#define IFX_AUTANALOG_CTB_OA_NINV_REF_DAC1 2
```

相关声明：[IFX_AUTANALOG_CTB_OA_NINV_REF_DAC1](#ae701bf2f2d9eb10619abb040f58dbd4b)。

DAC1 输出（Output）。

<a id="r_a3688a02a7cef01120c3a9ce4c396ad0c"></a>

```c
#define IFX_AUTANALOG_CTB_OA_NINV_REF_PRB_OUT0 3
```

相关声明：[IFX_AUTANALOG_CTB_OA_NINV_REF_PRB_OUT0](#a3688a02a7cef01120c3a9ce4c396ad0c)。

PRB 输出（Output） 0。

<a id="r_ad05107df31fa3542eca1ab28b31d9423"></a>

```c
#define IFX_AUTANALOG_CTB_OA_NINV_REF_PRB_OUT1 4
```

相关声明：[IFX_AUTANALOG_CTB_OA_NINV_REF_PRB_OUT1](#ad05107df31fa3542eca1ab28b31d9423)。

PRB 输出（Output） 1。

<a id="r_a231108383470c8c69021b67d4658768f"></a>

```c
#define IFX_AUTANALOG_CTB_OA_NINV_REF_VBGR 5
```

相关声明：[IFX_AUTANALOG_CTB_OA_NINV_REF_VBGR](#a231108383470c8c69021b67d4658768f)。

带隙基准（Band-Gap Reference）。

<a id="r_a0269f6e7bcfa9bd1758d4f582bae6b61"></a>

```c
#define IFX_AUTANALOG_CTB_OA_NINV_REF_CTB_OA0_OUT 6
```

相关声明：[IFX_AUTANALOG_CTB_OA_NINV_REF_CTB_OA0_OUT](#a0269f6e7bcfa9bd1758d4f582bae6b61)。

CTB 运算放大器 0 的输出（Opamp 0 Output）。

<a id="r_ad8b8ee4220ba3bd91a96dddb2d4a2ba4"></a>

```c
#define IFX_AUTANALOG_CTB_OA_NINV_REF_CTB_OA1_OUT 7
```

相关声明：[IFX_AUTANALOG_CTB_OA_NINV_REF_CTB_OA1_OUT](#ad8b8ee4220ba3bd91a96dddb2d4a2ba4)。

CTB 运算放大器 1 的输出（Opamp 1 Output）。

<a id="define-members-7"></a>

### 反相输入引脚连接（Inverting input pin connection (cy_en_autanalog_ctb_oa_inv_pin_t)）

<a id="r_a27894247191f782095c88714706ed3d4"></a>

```c
#define IFX_AUTANALOG_CTB_OA_INV_PIN_DISCONNECT 0
```

相关声明：[IFX_AUTANALOG_CTB_OA_INV_PIN_DISCONNECT](#a27894247191f782095c88714706ed3d4)。

引脚断开连接（Pin Disconnected）。

<a id="r_a93722ee274968aeb914568147f299cd2"></a>

```c
#define IFX_AUTANALOG_CTB_OA_INV_PIN_OA0_P0_OA1_P5 1
```

相关声明：[IFX_AUTANALOG_CTB_OA_INV_PIN_OA0_P0_OA1_P5](#a93722ee274968aeb914568147f299cd2)。

OA0 的 P0 引脚或 OA1 的 P5 引脚（Pin）。

<a id="r_afb95879ce35f051369a831343880e6c8"></a>

```c
#define IFX_AUTANALOG_CTB_OA_INV_PIN_OA0_P1_OA1_P4 2
```

相关声明：[IFX_AUTANALOG_CTB_OA_INV_PIN_OA0_P1_OA1_P4](#afb95879ce35f051369a831343880e6c8)。

OA0 的 P1 引脚或 OA1 的 P4 引脚（Pin）。

<a id="define-members-8"></a>

### 电阻梯形网络底端引脚连接（Resistor ladder bottom pin connection (cy_en_autanalog_ctb_oa_res_pin_t)）

<a id="r_a3cf3235719a8870a01da2904cd4fcf60"></a>

```c
#define IFX_AUTANALOG_CTB_OA_RES_PIN_DISCONNECT 0
```

相关声明：[IFX_AUTANALOG_CTB_OA_RES_PIN_DISCONNECT](#a3cf3235719a8870a01da2904cd4fcf60)。

引脚断开连接（Pin Disconnected）。

<a id="r_a97ebbe7fc996aeb21a18d2ee96bcc395"></a>

```c
#define IFX_AUTANALOG_CTB_OA_RES_PIN_OA0_P0_OA1_P5 1
```

相关声明：[IFX_AUTANALOG_CTB_OA_RES_PIN_OA0_P0_OA1_P5](#a97ebbe7fc996aeb21a18d2ee96bcc395)。

OA0 的 P0 引脚或 OA1 的 P5 引脚（Pin）。

<a id="r_ab205259ef9b4b9038abfabb19424cdbd"></a>

```c
#define IFX_AUTANALOG_CTB_OA_RES_PIN_OA0_P1_OA1_P4 2
```

相关声明：[IFX_AUTANALOG_CTB_OA_RES_PIN_OA0_P1_OA1_P4](#ab205259ef9b4b9038abfabb19424cdbd)。

OA0 的 P1 引脚或 OA1 的 P4 引脚（Pin）。

<a id="define-members-9"></a>

### 电阻梯形网络底端参考源连接（Resistor ladder bottom reference connection (cy_en_autanalog_ctb_oa_res_ref_t)）

<a id="r_a9ce75723eacd46d267a6f77ce72bbe30"></a>

```c
#define IFX_AUTANALOG_CTB_OA_RES_REF_DISCONNECT 0
```

相关声明：[IFX_AUTANALOG_CTB_OA_RES_REF_DISCONNECT](#a9ce75723eacd46d267a6f77ce72bbe30)。

参考源断开连接（Reference Disconnected）。

<a id="r_aa3e1b6be9d9dd6cbee4e5ac6d4139716"></a>

```c
#define IFX_AUTANALOG_CTB_OA_RES_REF_DAC0 1
```

相关声明：[IFX_AUTANALOG_CTB_OA_RES_REF_DAC0](#aa3e1b6be9d9dd6cbee4e5ac6d4139716)。

DAC0 输出（Output）。

<a id="r_a129fe165784e7a8974e15884e687e2c8"></a>

```c
#define IFX_AUTANALOG_CTB_OA_RES_REF_DAC1 2
```

相关声明：[IFX_AUTANALOG_CTB_OA_RES_REF_DAC1](#a129fe165784e7a8974e15884e687e2c8)。

DAC1 输出（Output）。

<a id="r_a13f31130855b9a1d0eb8ecc790276cf1"></a>

```c
#define IFX_AUTANALOG_CTB_OA_RES_REF_CTB_OA0_OUT 3
```

相关声明：[IFX_AUTANALOG_CTB_OA_RES_REF_CTB_OA0_OUT](#a13f31130855b9a1d0eb8ecc790276cf1)。

CTB 运算放大器 0 的输出（Opamp 0 Output）。

<a id="r_a12fd77876d5c90c0857bb86d5ec38da1"></a>

```c
#define IFX_AUTANALOG_CTB_OA_RES_REF_CTB_OA1_OUT 4
```

相关声明：[IFX_AUTANALOG_CTB_OA_RES_REF_CTB_OA1_OUT](#a12fd77876d5c90c0857bb86d5ec38da1)。

CTB 运算放大器 1 的输出（Opamp 1 Output）。

<a id="r_a9d6e10c61c9b92132b4cf9938eb87da0"></a>

```c
#define IFX_AUTANALOG_CTB_OA_RES_REF_VSSA 5
```

相关声明：[IFX_AUTANALOG_CTB_OA_RES_REF_VSSA](#a9d6e10c61c9b92132b4cf9938eb87da0)。

模拟地参考（Analog Ground Reference）。

<a id="define-members-10"></a>

### 输入多路复用器连接（Input multiplexer connection (cy_en_autanalog_ctb_oa_mux_in_t)）

<a id="r_acb4f3a9193d85b4afdfe12d00945a160"></a>

```c
#define IFX_AUTANALOG_CTB_OA_MUX_IN_DISCONNECT 0
```

相关声明：[IFX_AUTANALOG_CTB_OA_MUX_IN_DISCONNECT](#acb4f3a9193d85b4afdfe12d00945a160)。

输入多路复用器（Input Mux）断开连接。

<a id="r_acc333110a5920123f2b10b7801ae9a1a"></a>

```c
#define IFX_AUTANALOG_CTB_OA_MUX_IN_P0 1
```

相关声明：[IFX_AUTANALOG_CTB_OA_MUX_IN_P0](#acc333110a5920123f2b10b7801ae9a1a)。

连接引脚（Pin）`P0`。

<a id="r_ada3c2d4a548c6ef89170eb065cb1d507"></a>

```c
#define IFX_AUTANALOG_CTB_OA_MUX_IN_P1 2
```

相关声明：[IFX_AUTANALOG_CTB_OA_MUX_IN_P1](#ada3c2d4a548c6ef89170eb065cb1d507)。

连接引脚（Pin）`P1`。

<a id="r_a73f1ff0e1f8f18de392da17fcd3f72f6"></a>

```c
#define IFX_AUTANALOG_CTB_OA_MUX_IN_P2 3
```

相关声明：[IFX_AUTANALOG_CTB_OA_MUX_IN_P2](#a73f1ff0e1f8f18de392da17fcd3f72f6)。

连接引脚（Pin）`P2`。

<a id="r_a783f81f1ca5ad35f4f54911c12d243ac"></a>

```c
#define IFX_AUTANALOG_CTB_OA_MUX_IN_P3 4
```

相关声明：[IFX_AUTANALOG_CTB_OA_MUX_IN_P3](#a783f81f1ca5ad35f4f54911c12d243ac)。

连接引脚（Pin）`P3`。

<a id="r_aaccf5415608ee248d2c74ca4fe1e098f"></a>

```c
#define IFX_AUTANALOG_CTB_OA_MUX_IN_P4 5
```

相关声明：[IFX_AUTANALOG_CTB_OA_MUX_IN_P4](#aaccf5415608ee248d2c74ca4fe1e098f)。

连接引脚（Pin）`P4`。

<a id="r_a7d9b2b411183a4ac02afa4b5e156cde1"></a>

```c
#define IFX_AUTANALOG_CTB_OA_MUX_IN_P5 6
```

相关声明：[IFX_AUTANALOG_CTB_OA_MUX_IN_P5](#a7d9b2b411183a4ac02afa4b5e156cde1)。

连接引脚（Pin）`P5`。

<a id="r_ab49d2c79d1c301ec8933f215e0936777"></a>

```c
#define IFX_AUTANALOG_CTB_OA_MUX_IN_P6 7
```

相关声明：[IFX_AUTANALOG_CTB_OA_MUX_IN_P6](#ab49d2c79d1c301ec8933f215e0936777)。

连接引脚（Pin）`P6`。

<a id="r_a2098292f745c60a962affa47f5acd2a7"></a>

```c
#define IFX_AUTANALOG_CTB_OA_MUX_IN_P7 8
```

相关声明：[IFX_AUTANALOG_CTB_OA_MUX_IN_P7](#a2098292f745c60a962affa47f5acd2a7)。

连接引脚（Pin）`P7`。

<a id="define-members-11"></a>

### 输出多路复用器连接（Output multiplexer connection (cy_en_autanalog_ctb_oa_mux_out_t)）

<a id="r_a109e3f2316f92f6c7bc3a7cad6d06a19"></a>

```c
#define IFX_AUTANALOG_CTB_OA_MUX_OUT_DISCONNECT 0
```

相关声明：[IFX_AUTANALOG_CTB_OA_MUX_OUT_DISCONNECT](#a109e3f2316f92f6c7bc3a7cad6d06a19)。

输出多路复用器（Output Mux）断开连接。

<a id="r_af69406915eef9ba6b83b7f8005f9553c"></a>

```c
#define IFX_AUTANALOG_CTB_OA_MUX_OUT_NINV 1
```

相关声明：[IFX_AUTANALOG_CTB_OA_MUX_OUT_NINV](#af69406915eef9ba6b83b7f8005f9553c)。

接通同相输入（Non-Inverting Input）的路由。

<a id="r_a03a44b521fac99dc798a453fdec75178"></a>

```c
#define IFX_AUTANALOG_CTB_OA_MUX_OUT_INV 2
```

相关声明：[IFX_AUTANALOG_CTB_OA_MUX_OUT_INV](#a03a44b521fac99dc798a453fdec75178)。

接通反相输入（Inverting Input）的路由。

<a id="r_ad4b3b031658724cac4d49487d996d851"></a>

```c
#define IFX_AUTANALOG_CTB_OA_MUX_OUT_RES 3
```

相关声明：[IFX_AUTANALOG_CTB_OA_MUX_OUT_RES](#ad4b3b031658724cac4d49487d996d851)。

接通电阻梯形网络节点（Resistor Ladder Node）的路由。

## 4.2\_详细说明（Detailed Documentation）

<a id="a61073cdd5c4ac0588ac4509a76bb4650"></a>

### `IFX_AUTANALOG_CTB_COMP_INT_DISABLED`

```c
#define IFX_AUTANALOG_CTB_COMP_INT_DISABLED 0
```

中断已禁用（Interrupt Disabled）。

<a id="a8041e94459e325b36d252ad2d47e81ae"></a>

### `IFX_AUTANALOG_CTB_COMP_INT_EDGE_BOTH`

```c
#define IFX_AUTANALOG_CTB_COMP_INT_EDGE_BOTH 3
```

双边沿检测（Both-edge Detection）。

<a id="a69279743fc840b07757feff795d2d58c"></a>

### `IFX_AUTANALOG_CTB_COMP_INT_EDGE_FALLING`

```c
#define IFX_AUTANALOG_CTB_COMP_INT_EDGE_FALLING 2
```

下降沿检测（Falling Edge Detection）。

<a id="a20ead2bbf4207733f6ea909010c2689b"></a>

### `IFX_AUTANALOG_CTB_COMP_INT_EDGE_RISING`

```c
#define IFX_AUTANALOG_CTB_COMP_INT_EDGE_RISING 1
```

上升沿检测（Rising Edge Detection）。

<a id="a7d1f17dbdd2d1a6ff9c84431b21f5182"></a>

### `IFX_AUTANALOG_CTB_OA_CC_CAP_0_1_pF`

```c
#define IFX_AUTANALOG_CTB_OA_CC_CAP_0_1_pF 0
```

0.1 pF 补偿电容（Compensation Capacitor）。

<a id="a6f354e7448f0d0af7ca7f8e5890405f4"></a>

### `IFX_AUTANALOG_CTB_OA_CC_CAP_1_1_pF`

```c
#define IFX_AUTANALOG_CTB_OA_CC_CAP_1_1_pF 1
```

1.1 pF 补偿电容（Compensation Capacitor）。

<a id="abd1506959b9e1d85c32715175831f772"></a>

### `IFX_AUTANALOG_CTB_OA_CC_CAP_2_1_pF`

```c
#define IFX_AUTANALOG_CTB_OA_CC_CAP_2_1_pF 2
```

2.1 pF 补偿电容（Compensation Capacitor）。

<a id="a7f73e6402eba49e7ecfed0d1fb74e8c1"></a>

### `IFX_AUTANALOG_CTB_OA_CC_CAP_3_1_pF`

```c
#define IFX_AUTANALOG_CTB_OA_CC_CAP_3_1_pF 3
```

3.1 pF 补偿电容（Compensation Capacitor）。

<a id="a1d6b0cd1b162b2e5ce727aa108324595"></a>

### `IFX_AUTANALOG_CTB_OA_CC_CAP_4_1_pF`

```c
#define IFX_AUTANALOG_CTB_OA_CC_CAP_4_1_pF 4
```

4.1 pF 补偿电容（Compensation Capacitor）。

<a id="a173591ef72608bf8242739978e3195a5"></a>

### `IFX_AUTANALOG_CTB_OA_CC_CAP_5_1_pF`

```c
#define IFX_AUTANALOG_CTB_OA_CC_CAP_5_1_pF 5
```

5.1 pF 补偿电容（Compensation Capacitor）。

<a id="a5eb4d75542f6651edc366a393bffd225"></a>

### `IFX_AUTANALOG_CTB_OA_CC_CAP_6_1_pF`

```c
#define IFX_AUTANALOG_CTB_OA_CC_CAP_6_1_pF 6
```

6.1 pF 补偿电容（Compensation Capacitor）。

<a id="a134c74701eaad5ac9a0459d3d8be7f1d"></a>

### `IFX_AUTANALOG_CTB_OA_CC_CAP_7_1_pF`

```c
#define IFX_AUTANALOG_CTB_OA_CC_CAP_7_1_pF 7
```

7.1 pF 补偿电容（Compensation Capacitor）。

<a id="af71671b3f49f3dfd69304430c48d4494"></a>

### `IFX_AUTANALOG_CTB_OA_CC_CAP_DISABLED`

```c
#define IFX_AUTANALOG_CTB_OA_CC_CAP_DISABLED 8
```

禁用补偿电容（Compensation Capacitor）。

<a id="ad51cc393be793c1961826e37463c9152"></a>

### `IFX_AUTANALOG_CTB_OA_FB_CAP_0_7_pF`

```c
#define IFX_AUTANALOG_CTB_OA_FB_CAP_0_7_pF 1
```

0.7 pF 反馈电容（Feedback Capacitor）。

<a id="a6f0cdff51fc7888abf2b53ae0a16ec3c"></a>

### `IFX_AUTANALOG_CTB_OA_FB_CAP_0_pF`

```c
#define IFX_AUTANALOG_CTB_OA_FB_CAP_0_pF 0
```

0.0 pF 反馈电容（Feedback Capacitor）。

<a id="a860045afab252c9c4628d50774ffd3b4"></a>

### `IFX_AUTANALOG_CTB_OA_FB_CAP_10_5_pF`

```c
#define IFX_AUTANALOG_CTB_OA_FB_CAP_10_5_pF 15
```

10.5 pF 反馈电容（Feedback Capacitor）。

<a id="ab9043f15c03eb29bcdedcc39e40314b8"></a>

### `IFX_AUTANALOG_CTB_OA_FB_CAP_1_4_pF`

```c
#define IFX_AUTANALOG_CTB_OA_FB_CAP_1_4_pF 2
```

1.4 pF 反馈电容（Feedback Capacitor）。

<a id="a7aac9d2fb1ae1138b9c84453e8cf3a60"></a>

### `IFX_AUTANALOG_CTB_OA_FB_CAP_2_1_pF`

```c
#define IFX_AUTANALOG_CTB_OA_FB_CAP_2_1_pF 3
```

2.1 pF 反馈电容（Feedback Capacitor）。

<a id="af60e61caee6217e3a7bb883a3be49112"></a>

### `IFX_AUTANALOG_CTB_OA_FB_CAP_2_8_pF`

```c
#define IFX_AUTANALOG_CTB_OA_FB_CAP_2_8_pF 4
```

2.8 pF 反馈电容（Feedback Capacitor）。

<a id="a222835d10b33feda5035581ad5222494"></a>

### `IFX_AUTANALOG_CTB_OA_FB_CAP_3_5_pF`

```c
#define IFX_AUTANALOG_CTB_OA_FB_CAP_3_5_pF 5
```

3.5 pF 反馈电容（Feedback Capacitor）。

<a id="a2534b6da595f1077eeca9dd13f06a246"></a>

### `IFX_AUTANALOG_CTB_OA_FB_CAP_4_2_pF`

```c
#define IFX_AUTANALOG_CTB_OA_FB_CAP_4_2_pF 6
```

4.2 pF 反馈电容（Feedback Capacitor）。

<a id="aba06d7236a7d2880818a1b6df3baa334"></a>

### `IFX_AUTANALOG_CTB_OA_FB_CAP_4_9_pF`

```c
#define IFX_AUTANALOG_CTB_OA_FB_CAP_4_9_pF 7
```

4.9 pF 反馈电容（Feedback Capacitor）。

<a id="adea95be3992fbdc7ce7545bd533098ab"></a>

### `IFX_AUTANALOG_CTB_OA_FB_CAP_5_6_pF`

```c
#define IFX_AUTANALOG_CTB_OA_FB_CAP_5_6_pF 8
```

5.6 pF 反馈电容（Feedback Capacitor）。

<a id="a2ea399f41f13ab20d45315958e118cf2"></a>

### `IFX_AUTANALOG_CTB_OA_FB_CAP_6_3_pF`

```c
#define IFX_AUTANALOG_CTB_OA_FB_CAP_6_3_pF 9
```

6.3 pF 反馈电容（Feedback Capacitor）。

<a id="ad0212a254c3c338fe8c29bffcc23b2ed"></a>

### `IFX_AUTANALOG_CTB_OA_FB_CAP_7_0_pF`

```c
#define IFX_AUTANALOG_CTB_OA_FB_CAP_7_0_pF 10
```

7.0 pF 反馈电容（Feedback Capacitor）。

<a id="ad956fdf03ae4bf3d479173252288defa"></a>

### `IFX_AUTANALOG_CTB_OA_FB_CAP_7_7_pF`

```c
#define IFX_AUTANALOG_CTB_OA_FB_CAP_7_7_pF 11
```

7.7 pF 反馈电容（Feedback Capacitor）。

<a id="a2cd1e9e298b026af54a07a7f724f4d09"></a>

### `IFX_AUTANALOG_CTB_OA_FB_CAP_8_4_pF`

```c
#define IFX_AUTANALOG_CTB_OA_FB_CAP_8_4_pF 12
```

8.4 pF 反馈电容（Feedback Capacitor）。

<a id="a903a351fbf6b2e51ebce1e35a112cf9b"></a>

### `IFX_AUTANALOG_CTB_OA_FB_CAP_9_1_pF`

```c
#define IFX_AUTANALOG_CTB_OA_FB_CAP_9_1_pF 13
```

9.1 pF 反馈电容（Feedback Capacitor）。

<a id="aec250b3752da26851b694413e84e5ae6"></a>

### `IFX_AUTANALOG_CTB_OA_FB_CAP_9_8_pF`

```c
#define IFX_AUTANALOG_CTB_OA_FB_CAP_9_8_pF 14
```

9.8 pF 反馈电容（Feedback Capacitor）。

<a id="a27894247191f782095c88714706ed3d4"></a>

### `IFX_AUTANALOG_CTB_OA_INV_PIN_DISCONNECT`

```c
#define IFX_AUTANALOG_CTB_OA_INV_PIN_DISCONNECT 0
```

引脚断开连接（Pin Disconnected）。

<a id="a93722ee274968aeb914568147f299cd2"></a>

### `IFX_AUTANALOG_CTB_OA_INV_PIN_OA0_P0_OA1_P5`

```c
#define IFX_AUTANALOG_CTB_OA_INV_PIN_OA0_P0_OA1_P5 1
```

OA0 的 P0 引脚或 OA1 的 P5 引脚（Pin）。

<a id="afb95879ce35f051369a831343880e6c8"></a>

### `IFX_AUTANALOG_CTB_OA_INV_PIN_OA0_P1_OA1_P4`

```c
#define IFX_AUTANALOG_CTB_OA_INV_PIN_OA0_P1_OA1_P4 2
```

OA0 的 P1 引脚或 OA1 的 P4 引脚（Pin）。

<a id="acb4f3a9193d85b4afdfe12d00945a160"></a>

### `IFX_AUTANALOG_CTB_OA_MUX_IN_DISCONNECT`

```c
#define IFX_AUTANALOG_CTB_OA_MUX_IN_DISCONNECT 0
```

输入多路复用器（Input Mux）断开连接。

<a id="acc333110a5920123f2b10b7801ae9a1a"></a>

### `IFX_AUTANALOG_CTB_OA_MUX_IN_P0`

```c
#define IFX_AUTANALOG_CTB_OA_MUX_IN_P0 1
```

连接引脚（Pin）`P0`。

<a id="ada3c2d4a548c6ef89170eb065cb1d507"></a>

### `IFX_AUTANALOG_CTB_OA_MUX_IN_P1`

```c
#define IFX_AUTANALOG_CTB_OA_MUX_IN_P1 2
```

连接引脚（Pin）`P1`。

<a id="a73f1ff0e1f8f18de392da17fcd3f72f6"></a>

### `IFX_AUTANALOG_CTB_OA_MUX_IN_P2`

```c
#define IFX_AUTANALOG_CTB_OA_MUX_IN_P2 3
```

连接引脚（Pin）`P2`。

<a id="a783f81f1ca5ad35f4f54911c12d243ac"></a>

### `IFX_AUTANALOG_CTB_OA_MUX_IN_P3`

```c
#define IFX_AUTANALOG_CTB_OA_MUX_IN_P3 4
```

连接引脚（Pin）`P3`。

<a id="aaccf5415608ee248d2c74ca4fe1e098f"></a>

### `IFX_AUTANALOG_CTB_OA_MUX_IN_P4`

```c
#define IFX_AUTANALOG_CTB_OA_MUX_IN_P4 5
```

连接引脚（Pin）`P4`。

<a id="a7d9b2b411183a4ac02afa4b5e156cde1"></a>

### `IFX_AUTANALOG_CTB_OA_MUX_IN_P5`

```c
#define IFX_AUTANALOG_CTB_OA_MUX_IN_P5 6
```

连接引脚（Pin）`P5`。

<a id="ab49d2c79d1c301ec8933f215e0936777"></a>

### `IFX_AUTANALOG_CTB_OA_MUX_IN_P6`

```c
#define IFX_AUTANALOG_CTB_OA_MUX_IN_P6 7
```

连接引脚（Pin）`P6`。

<a id="a2098292f745c60a962affa47f5acd2a7"></a>

### `IFX_AUTANALOG_CTB_OA_MUX_IN_P7`

```c
#define IFX_AUTANALOG_CTB_OA_MUX_IN_P7 8
```

连接引脚（Pin）`P7`。

<a id="a109e3f2316f92f6c7bc3a7cad6d06a19"></a>

### `IFX_AUTANALOG_CTB_OA_MUX_OUT_DISCONNECT`

```c
#define IFX_AUTANALOG_CTB_OA_MUX_OUT_DISCONNECT 0
```

输出多路复用器（Output Mux）断开连接。

<a id="a03a44b521fac99dc798a453fdec75178"></a>

### `IFX_AUTANALOG_CTB_OA_MUX_OUT_INV`

```c
#define IFX_AUTANALOG_CTB_OA_MUX_OUT_INV 2
```

接通反相输入（Inverting Input）的路由。

<a id="af69406915eef9ba6b83b7f8005f9553c"></a>

### `IFX_AUTANALOG_CTB_OA_MUX_OUT_NINV`

```c
#define IFX_AUTANALOG_CTB_OA_MUX_OUT_NINV 1
```

接通同相输入（Non-Inverting Input）的路由。

<a id="ad4b3b031658724cac4d49487d996d851"></a>

### `IFX_AUTANALOG_CTB_OA_MUX_OUT_RES`

```c
#define IFX_AUTANALOG_CTB_OA_MUX_OUT_RES 3
```

接通电阻梯形网络节点（Resistor Ladder Node）的路由。

<a id="ac2043c2e03ec5ed504cbddb80f5cf219"></a>

### `IFX_AUTANALOG_CTB_OA_NINV_PIN_DISCONNECT`

```c
#define IFX_AUTANALOG_CTB_OA_NINV_PIN_DISCONNECT 0
```

引脚断开连接（Pin Disconnected）。

<a id="ac86aa8ae834d504871217f78b4dc6b93"></a>

### `IFX_AUTANALOG_CTB_OA_NINV_PIN_OA0_P0_OA1_P5`

```c
#define IFX_AUTANALOG_CTB_OA_NINV_PIN_OA0_P0_OA1_P5 1
```

OA0 的 P0 引脚或 OA1 的 P5 引脚（Pin）。

<a id="aabfc18593242d54ef4307339bc9f15f4"></a>

### `IFX_AUTANALOG_CTB_OA_NINV_PIN_OA0_P1_OA1_P4`

```c
#define IFX_AUTANALOG_CTB_OA_NINV_PIN_OA0_P1_OA1_P4 2
```

OA0 的 P1 引脚或 OA1 的 P4 引脚（Pin）。

<a id="a0269f6e7bcfa9bd1758d4f582bae6b61"></a>

### `IFX_AUTANALOG_CTB_OA_NINV_REF_CTB_OA0_OUT`

```c
#define IFX_AUTANALOG_CTB_OA_NINV_REF_CTB_OA0_OUT 6
```

CTB 运算放大器 0 的输出（Opamp 0 Output）。

<a id="ad8b8ee4220ba3bd91a96dddb2d4a2ba4"></a>

### `IFX_AUTANALOG_CTB_OA_NINV_REF_CTB_OA1_OUT`

```c
#define IFX_AUTANALOG_CTB_OA_NINV_REF_CTB_OA1_OUT 7
```

CTB 运算放大器 1 的输出（Opamp 1 Output）。

<a id="a8a4f93898b6b25a3d102323714db034b"></a>

### `IFX_AUTANALOG_CTB_OA_NINV_REF_DAC0`

```c
#define IFX_AUTANALOG_CTB_OA_NINV_REF_DAC0 1
```

DAC0 输出（Output）。

<a id="ae701bf2f2d9eb10619abb040f58dbd4b"></a>

### `IFX_AUTANALOG_CTB_OA_NINV_REF_DAC1`

```c
#define IFX_AUTANALOG_CTB_OA_NINV_REF_DAC1 2
```

DAC1 输出（Output）。

<a id="a526900d4934c85775c660e059821a88f"></a>

### `IFX_AUTANALOG_CTB_OA_NINV_REF_DISCONNECT`

```c
#define IFX_AUTANALOG_CTB_OA_NINV_REF_DISCONNECT 0
```

参考源断开连接（Reference Disconnected）。

<a id="a3688a02a7cef01120c3a9ce4c396ad0c"></a>

### `IFX_AUTANALOG_CTB_OA_NINV_REF_PRB_OUT0`

```c
#define IFX_AUTANALOG_CTB_OA_NINV_REF_PRB_OUT0 3
```

PRB 输出（Output） 0。

<a id="ad05107df31fa3542eca1ab28b31d9423"></a>

### `IFX_AUTANALOG_CTB_OA_NINV_REF_PRB_OUT1`

```c
#define IFX_AUTANALOG_CTB_OA_NINV_REF_PRB_OUT1 4
```

PRB 输出（Output） 1。

<a id="a231108383470c8c69021b67d4658768f"></a>

### `IFX_AUTANALOG_CTB_OA_NINV_REF_VBGR`

```c
#define IFX_AUTANALOG_CTB_OA_NINV_REF_VBGR 5
```

带隙基准（Band-Gap Reference）。

<a id="ad9a640a1e8191a29f9be2cf6e72d5661"></a>

### `IFX_AUTANALOG_CTB_OA_PWR_HIGH_RAIL`

```c
#define IFX_AUTANALOG_CTB_OA_PWR_HIGH_RAIL 8
```

高功耗（High Power），电荷泵（Charge Pump）开启。

<a id="ad63c1eb722a575cff3525c3bf80a03d3"></a>

### `IFX_AUTANALOG_CTB_OA_PWR_LOW_RAIL`

```c
#define IFX_AUTANALOG_CTB_OA_PWR_LOW_RAIL 4
```

低功耗（Low Power），电荷泵（Charge Pump）开启。

<a id="a7723cec22a9a04f1afa2648e379f22a9"></a>

### `IFX_AUTANALOG_CTB_OA_PWR_MEDIUM_RAIL`

```c
#define IFX_AUTANALOG_CTB_OA_PWR_MEDIUM_RAIL 6
```

中等功耗（Medium Power），电荷泵（Charge Pump）开启。

<a id="ad52f76f54d24f1b8b134afe782270087"></a>

### `IFX_AUTANALOG_CTB_OA_PWR_OFF`

```c
#define IFX_AUTANALOG_CTB_OA_PWR_OFF 0
```

运算放大器（Opamp）断电。

<a id="ab6264b440cc317ca9b6b4a52b66c17f1"></a>

### `IFX_AUTANALOG_CTB_OA_PWR_ULTRA_HIGH_RAIL`

```c
#define IFX_AUTANALOG_CTB_OA_PWR_ULTRA_HIGH_RAIL 10
```

超高功耗（Ultra High Power），电荷泵（Charge Pump）开启。

<a id="ad784a0b04e92698c468e4fcfb4fd3019"></a>

### `IFX_AUTANALOG_CTB_OA_PWR_ULTRA_LOW`

```c
#define IFX_AUTANALOG_CTB_OA_PWR_ULTRA_LOW 1
```

超低功耗（Ultra Low Power），电荷泵（Charge Pump）关闭。

<a id="ac8eccf96dddbd602b2bf00a0325bd28e"></a>

### `IFX_AUTANALOG_CTB_OA_PWR_ULTRA_LOW_RAIL`

```c
#define IFX_AUTANALOG_CTB_OA_PWR_ULTRA_LOW_RAIL 2
```

超低功耗（Ultra Low Power），电荷泵（Charge Pump）开启。

<a id="a3cf3235719a8870a01da2904cd4fcf60"></a>

### `IFX_AUTANALOG_CTB_OA_RES_PIN_DISCONNECT`

```c
#define IFX_AUTANALOG_CTB_OA_RES_PIN_DISCONNECT 0
```

引脚断开连接（Pin Disconnected）。

<a id="a97ebbe7fc996aeb21a18d2ee96bcc395"></a>

### `IFX_AUTANALOG_CTB_OA_RES_PIN_OA0_P0_OA1_P5`

```c
#define IFX_AUTANALOG_CTB_OA_RES_PIN_OA0_P0_OA1_P5 1
```

OA0 的 P0 引脚或 OA1 的 P5 引脚（Pin）。

<a id="ab205259ef9b4b9038abfabb19424cdbd"></a>

### `IFX_AUTANALOG_CTB_OA_RES_PIN_OA0_P1_OA1_P4`

```c
#define IFX_AUTANALOG_CTB_OA_RES_PIN_OA0_P1_OA1_P4 2
```

OA0 的 P1 引脚或 OA1 的 P4 引脚（Pin）。

<a id="a13f31130855b9a1d0eb8ecc790276cf1"></a>

### `IFX_AUTANALOG_CTB_OA_RES_REF_CTB_OA0_OUT`

```c
#define IFX_AUTANALOG_CTB_OA_RES_REF_CTB_OA0_OUT 3
```

CTB 运算放大器 0 的输出（Opamp 0 Output）。

<a id="a12fd77876d5c90c0857bb86d5ec38da1"></a>

### `IFX_AUTANALOG_CTB_OA_RES_REF_CTB_OA1_OUT`

```c
#define IFX_AUTANALOG_CTB_OA_RES_REF_CTB_OA1_OUT 4
```

CTB 运算放大器 1 的输出（Opamp 1 Output）。

<a id="aa3e1b6be9d9dd6cbee4e5ac6d4139716"></a>

### `IFX_AUTANALOG_CTB_OA_RES_REF_DAC0`

```c
#define IFX_AUTANALOG_CTB_OA_RES_REF_DAC0 1
```

DAC0 输出（Output）。

<a id="a129fe165784e7a8974e15884e687e2c8"></a>

### `IFX_AUTANALOG_CTB_OA_RES_REF_DAC1`

```c
#define IFX_AUTANALOG_CTB_OA_RES_REF_DAC1 2
```

DAC1 输出（Output）。

<a id="a9ce75723eacd46d267a6f77ce72bbe30"></a>

### `IFX_AUTANALOG_CTB_OA_RES_REF_DISCONNECT`

```c
#define IFX_AUTANALOG_CTB_OA_RES_REF_DISCONNECT 0
```

参考源断开连接（Reference Disconnected）。

<a id="a9d6e10c61c9b92132b4cf9938eb87da0"></a>

### `IFX_AUTANALOG_CTB_OA_RES_REF_VSSA`

```c
#define IFX_AUTANALOG_CTB_OA_RES_REF_VSSA 5
```

模拟地参考（Analog Ground Reference）。

<a id="aaad55877b78bd49dc8ae5f2ce07a4145"></a>

### `IFX_AUTANALOG_CTB_OA_TOPO_BUFFER`

```c
#define IFX_AUTANALOG_CTB_OA_TOPO_BUFFER 6
```

电压跟随器／缓冲器拓扑（Voltage Follower / Buffer Topology）。

<a id="a8fc46b275e0bc269eccf72fe65456532"></a>

### `IFX_AUTANALOG_CTB_OA_TOPO_COMPARATOR`

```c
#define IFX_AUTANALOG_CTB_OA_TOPO_COMPARATOR 0
```

比较器拓扑（Comparator Topology）。

<a id="a34598608d43923b48a0fbf2832867a28"></a>

### `IFX_AUTANALOG_CTB_OA_TOPO_DIFF_AMPLIFIER`

```c
#define IFX_AUTANALOG_CTB_OA_TOPO_DIFF_AMPLIFIER 4
```

差分放大器拓扑（Differential Amplifier Topology）。

<a id="a40db30a0852ac2d6860db3f56357f5ab"></a>

### `IFX_AUTANALOG_CTB_OA_TOPO_HYST_COMPARATOR`

```c
#define IFX_AUTANALOG_CTB_OA_TOPO_HYST_COMPARATOR 5
```

迟滞比较器拓扑（Hysteresis Comparator Topology）。

<a id="ab127787012ef36285ee17f8875a26022"></a>

### `IFX_AUTANALOG_CTB_OA_TOPO_OPEN_LOOP_OPAMP`

```c
#define IFX_AUTANALOG_CTB_OA_TOPO_OPEN_LOOP_OPAMP 3
```

开环运算放大器拓扑（Open-Loop Opamp Topology）。

<a id="a67da79c30e9798e6b33d7ae1a3d651ec"></a>

### `IFX_AUTANALOG_CTB_OA_TOPO_PGA`

```c
#define IFX_AUTANALOG_CTB_OA_TOPO_PGA 1
```

可编程增益放大器拓扑（Programmable Gain Amplifier Topology）。

<a id="ac3ad453d628645409b6eba50d58c8208"></a>

### `IFX_AUTANALOG_CTB_OA_TOPO_TIA`

```c
#define IFX_AUTANALOG_CTB_OA_TOPO_TIA 2
```

跨阻放大器拓扑（Transimpedance Amplifier Topology）。


## 4.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P367_infineon-autanalog-ctb.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P003_zephyr__llext__elf.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P005_zephyr__dt-bindings__comparator__infineon-autanalog-ptcomp.h_文件参考.md)
