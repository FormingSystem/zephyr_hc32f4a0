---
id: learning.zephyr-docs.api-file-bluetooth-media-reference.page-3
title: zephyr__dt-bindings__sensor__max30009.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2max30009_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_zephyr\_\_dt-bindings\_\_sensor\_\_max30009.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2max30009_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

the Analog Devices MAX30009 BioZ AFE的设备树绑定常量（Devicetree Binding Constants）。

查看此文件的源码。

<a id="details"></a>

the Analog Devices MAX30009 BioZ AFE的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 生物阻抗数字高通滤波器截止频率（BioZ digital high-pass filter cutoff）

设备树属性（Devicetree Property）`bioz-dhpf` 的取值。

<a id="r_ga8eb31c9c63eadb978c020fccadfac492"></a>

```c
#define MAX30009_DT_DHPF_BYPASS 0
```

相关声明：[MAX30009_DT_DHPF_BYPASS](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga8eb31c9c63eadb978c020fccadfac492)。

数字高通滤波器旁路（DHPF Bypass），禁用滤波器。

<a id="r_gab8608675fcbc8652bbf06df8b44c1c6e"></a>

```c
#define MAX30009_DT_DHPF_0_00025_SR 1
```

相关声明：[MAX30009_DT_DHPF_0_00025_SR](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gab8608675fcbc8652bbf06df8b44c1c6e)。

数字高通滤波器（DHPF）截止频率为 0.00025 × SR_BIOZ。

<a id="r_ga2cd7f98fcd61d9c33694ad94fcc5a67c"></a>

```c
#define MAX30009_DT_DHPF_0_002_SR 2
```

相关声明：[MAX30009_DT_DHPF_0_002_SR](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga2cd7f98fcd61d9c33694ad94fcc5a67c)。

数字高通滤波器（DHPF）截止频率为 0.002 × SR_BIOZ。

<a id="define-members-1"></a>

### 生物阻抗数字低通滤波器截止频率（BioZ digital low-pass filter cutoff）

设备树属性（Devicetree Property）`bioz-dlpf` 的取值。

<a id="r_gabfbc4a0a7a9d01e1c900deeb19e2d348"></a>

```c
#define MAX30009_DT_DLPF_BYPASS 0
```

相关声明：[MAX30009_DT_DLPF_BYPASS](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gabfbc4a0a7a9d01e1c900deeb19e2d348)。

数字低通滤波器旁路（DLPF Bypass），禁用滤波器。

<a id="r_ga1e0976e21749f72a9b1aa23eb7607cd8"></a>

```c
#define MAX30009_DT_DLPF_0_005_SR 1
```

相关声明：[MAX30009_DT_DLPF_0_005_SR](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga1e0976e21749f72a9b1aa23eb7607cd8)。

数字低通滤波器（DLPF）截止频率为 0.005 × SR_BIOZ。

<a id="r_gac0034d299f7b00be54a534c3e946aec1"></a>

```c
#define MAX30009_DT_DLPF_0_02_SR 2
```

相关声明：[MAX30009_DT_DLPF_0_02_SR](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gac0034d299f7b00be54a534c3e946aec1)。

数字低通滤波器（DLPF）截止频率为 0.02 × SR_BIOZ。

<a id="r_ga150857ee16c906db64132f6af02c7ea1"></a>

```c
#define MAX30009_DT_DLPF_0_08_SR 3
```

相关声明：[MAX30009_DT_DLPF_0_08_SR](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga150857ee16c906db64132f6af02c7ea1)。

数字低通滤波器（DLPF）截止频率为 0.08 × SR_BIOZ。

<a id="r_ga700307982ea8aa304c97fcad2fe54a25"></a>

```c
#define MAX30009_DT_DLPF_0_25_SR 4
```

相关声明：[MAX30009_DT_DLPF_0_25_SR](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga700307982ea8aa304c97fcad2fe54a25)。

数字低通滤波器（DLPF）截止频率为 0.25 × SR_BIOZ。

<a id="define-members-2"></a>

### 生物阻抗阈值比较器通道（BioZ threshold comparator channel）

设备树属性（Devicetree Property）`bioz-cmp` 的取值。

<a id="r_ga80d5099867fa89d2056331dc1ad77920"></a>

```c
#define MAX30009_DT_CMP_I 0
```

相关声明：[MAX30009_DT_CMP_I](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga80d5099867fa89d2056331dc1ad77920)。

比较同相通道（I Channel）。

<a id="r_gadfc473e2486322f94dcaec2338524edd"></a>

```c
#define MAX30009_DT_CMP_Q 1
```

相关声明：[MAX30009_DT_CMP_Q](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gadfc473e2486322f94dcaec2338524edd)。

比较正交通道（Q Channel）。

<a id="r_ga97dba7ad62da9497c9ea5a99ec63529e"></a>

```c
#define MAX30009_DT_CMP_Z 2
```

相关声明：[MAX30009_DT_CMP_Z](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga97dba7ad62da9497c9ea5a99ec63529e)。

比较幅值（Magnitude，Z）。

<a id="define-members-3"></a>

### 生物阻抗发送驱动模式（BioZ transmit drive mode）

设备树属性（Devicetree Property）`bioz-drv-mode` 的取值。

<a id="r_ga24babbc19fc375b8f002b58c4a5b9531"></a>

```c
#define MAX30009_DT_DRV_MODE_CURRENT 0
```

相关声明：[MAX30009_DT_DRV_MODE_CURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga24babbc19fc375b8f002b58c4a5b9531)。

电流驱动（Current Drive）。

<a id="r_ga561188fefa0505bb477ea48b14141dad"></a>

```c
#define MAX30009_DT_DRV_MODE_VOLTAGE 1
```

相关声明：[MAX30009_DT_DRV_MODE_VOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga561188fefa0505bb477ea48b14141dad)。

电压驱动（Voltage Drive）。

<a id="r_ga4df2c8a895ec807a3d856595e3b6a7b4"></a>

```c
#define MAX30009_DT_DRV_MODE_HBRIDGE 2
```

相关声明：[MAX30009_DT_DRV_MODE_HBRIDGE](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga4df2c8a895ec807a3d856595e3b6a7b4)。

H 桥驱动（H-bridge Drive）。

<a id="r_gaa77063a044e4363481c8f8e4a01b73b4"></a>

```c
#define MAX30009_DT_DRV_MODE_STANDBY 3
```

相关声明：[MAX30009_DT_DRV_MODE_STANDBY](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gaa77063a044e4363481c8f8e4a01b73b4)。

待机（Standby）。

<a id="define-members-4"></a>

### 生物阻抗内部电流量程电阻（BioZ internal current-range resistor）

设备树属性（Devicetree Property）`bioz-idrv-rge` 的取值。

<a id="r_ga909174a9f6539a49517d87e5b445e125"></a>

```c
#define MAX30009_DT_IDRV_RGE_552_5K 0
```

相关声明：[MAX30009_DT_IDRV_RGE_552_5K](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga909174a9f6539a49517d87e5b445e125)。

552.5 千欧（kOhm）。

<a id="r_ga8aac47687800236427f653ea2a35949a"></a>

```c
#define MAX30009_DT_IDRV_RGE_110_5K 1
```

相关声明：[MAX30009_DT_IDRV_RGE_110_5K](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga8aac47687800236427f653ea2a35949a)。

110.5 千欧（kOhm）。

<a id="r_gac3d066858d16e65904488d8fca3259f2"></a>

```c
#define MAX30009_DT_IDRV_RGE_5_525K 2
```

相关声明：[MAX30009_DT_IDRV_RGE_5_525K](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gac3d066858d16e65904488d8fca3259f2)。

5.525 千欧（kOhm）。

<a id="r_gaa90c7a5f5256ff7e6b3b532bc764b1df"></a>

```c
#define MAX30009_DT_IDRV_RGE_276_25R 3
```

相关声明：[MAX30009_DT_IDRV_RGE_276_25R](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gaa90c7a5f5256ff7e6b3b532bc764b1df)。

276.25 欧姆（Ohm）。

<a id="define-members-5"></a>

### 生物阻抗电压驱动幅度（BioZ voltage-drive magnitude）

设备树属性（Devicetree Property）`bioz-vdrv-mag` 的取值。

<a id="r_gaa90ab9b36f935e203c786a23c6cb28de"></a>

```c
#define MAX30009_DT_VDRV_MAG_50MV 0
```

相关声明：[MAX30009_DT_VDRV_MAG_50MV](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gaa90ab9b36f935e203c786a23c6cb28de)。

50 毫伏峰值（mVpk）。

<a id="r_ga92f2610117e2629038cbfe9a85360907"></a>

```c
#define MAX30009_DT_VDRV_MAG_100MV 1
```

相关声明：[MAX30009_DT_VDRV_MAG_100MV](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga92f2610117e2629038cbfe9a85360907)。

100 毫伏峰值（mVpk）。

<a id="r_gac18eb324c01ca4f5c3e1b769cffb5a3a"></a>

```c
#define MAX30009_DT_VDRV_MAG_250MV 2
```

相关声明：[MAX30009_DT_VDRV_MAG_250MV](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gac18eb324c01ca4f5c3e1b769cffb5a3a)。

250 毫伏峰值（mVpk）。

<a id="r_ga17df936472b4d3f2c5a168301a77a726"></a>

```c
#define MAX30009_DT_VDRV_MAG_500MV 3
```

相关声明：[MAX30009_DT_VDRV_MAG_500MV](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga17df936472b4d3f2c5a168301a77a726)。

500 毫伏峰值（mVpk）。

<a id="define-members-6"></a>

### 生物阻抗模拟高通滤波器选择（BioZ analog high-pass filter (AHPF) selection）

设备树属性（Devicetree Property）`bioz-ahpf` 的取值。

<a id="r_gab17efef4bcc4fcc9ffcd169cfa99ab62"></a>

```c
#define MAX30009_DT_AHPF_100HZ 0
```

相关声明：[MAX30009_DT_AHPF_100HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gab17efef4bcc4fcc9ffcd169cfa99ab62)。

频率：100 Hz。

<a id="r_ga32ad059208543e6a11bd6bc456a667ca"></a>

```c
#define MAX30009_DT_AHPF_200HZ 1
```

相关声明：[MAX30009_DT_AHPF_200HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga32ad059208543e6a11bd6bc456a667ca)。

频率：200 Hz。

<a id="r_ga53c802e1cde30dc561d691f210185ecb"></a>

```c
#define MAX30009_DT_AHPF_500HZ 2
```

相关声明：[MAX30009_DT_AHPF_500HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga53c802e1cde30dc561d691f210185ecb)。

频率（Frequency）：500 Hz。

<a id="r_ga66add46c63a039ba6733a57a05d491be"></a>

```c
#define MAX30009_DT_AHPF_1KHZ 3
```

相关声明：[MAX30009_DT_AHPF_1KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga66add46c63a039ba6733a57a05d491be)。

频率（Frequency）：1 kHz。

<a id="r_gad40a309cec6a02f422da6b32411f48cc"></a>

```c
#define MAX30009_DT_AHPF_2KHZ 4
```

相关声明：[MAX30009_DT_AHPF_2KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gad40a309cec6a02f422da6b32411f48cc)。

频率（Frequency）：2 kHz。

<a id="r_ga34fb05b6b39cb0bc0c12616d7b85a0a1"></a>

```c
#define MAX30009_DT_AHPF_5KHZ 5
```

相关声明：[MAX30009_DT_AHPF_5KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga34fb05b6b39cb0bc0c12616d7b85a0a1)。

5 千赫（kHz）。

<a id="r_ga27c68f77eedb7b000f8f6b9478f888ac"></a>

```c
#define MAX30009_DT_AHPF_10KHZ 6
```

相关声明：[MAX30009_DT_AHPF_10KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga27c68f77eedb7b000f8f6b9478f888ac)。

10 千赫（kHz）。

<a id="r_ga2b94523d3f46d516ec5843bfe0afec9c"></a>

```c
#define MAX30009_DT_AHPF_BYPASS 7
```

相关声明：[MAX30009_DT_AHPF_BYPASS](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga2b94523d3f46d516ec5843bfe0afec9c)。

模拟高通滤波器旁路（AHPF Bypassed），电阻断开，内部电容短接。

<a id="r_gaed5d777b485d170a333bf84879e5c0cd"></a>

```c
#define MAX30009_DT_AHPF_42_4M 8
```

相关声明：[MAX30009_DT_AHPF_42_4M](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gaed5d777b485d170a333bf84879e5c0cd)。

42.4 MOhm，内部电容短接（Internal Capacitors Shorted）。

<a id="r_ga28d875778decaaee769a2d0aba59ccbd"></a>

```c
#define MAX30009_DT_AHPF_21_2M 9
```

相关声明：[MAX30009_DT_AHPF_21_2M](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga28d875778decaaee769a2d0aba59ccbd)。

21.2 MOhm，内部电容短接（Internal Capacitors Shorted）。

<a id="r_ga450809b02e66e5d06e79db8c51078730"></a>

```c
#define MAX30009_DT_AHPF_8_4M 10
```

相关声明：[MAX30009_DT_AHPF_8_4M](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga450809b02e66e5d06e79db8c51078730)。

8.4 MOhm，内部电容短接（Internal Capacitors Shorted）。

<a id="r_gaebfb3f4324cb1de4d8fbe25778485e78"></a>

```c
#define MAX30009_DT_AHPF_4_2M 11
```

相关声明：[MAX30009_DT_AHPF_4_2M](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gaebfb3f4324cb1de4d8fbe25778485e78)。

4.2 MOhm，内部电容短接（Internal Capacitors Shorted）。

<a id="r_ga75b3d909f58ca47a57eea8af9279669f"></a>

```c
#define MAX30009_DT_AHPF_2_2M 12
```

相关声明：[MAX30009_DT_AHPF_2_2M](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga75b3d909f58ca47a57eea8af9279669f)。

2.2 MOhm，内部电容短接（Internal Capacitors Shorted）。

<a id="r_ga5e29b90e65316f2b33a842af25c6d2b3"></a>

```c
#define MAX30009_DT_AHPF_848K 13
```

相关声明：[MAX30009_DT_AHPF_848K](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga5e29b90e65316f2b33a842af25c6d2b3)。

848 kOhm，内部电容短接（Internal Capacitors Shorted）。

<a id="r_gaab05f2c71b42ad45cd2c83f5f10e3fd7"></a>

```c
#define MAX30009_DT_AHPF_848K_ALT 14
```

相关声明：[MAX30009_DT_AHPF_848K_ALT](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gaab05f2c71b42ad45cd2c83f5f10e3fd7)。

848 kOhm，内部电容短接（Internal Capacitors Shorted）。

<a id="r_ga39df781c81760e414d8b4b362a4509aa"></a>

```c
#define MAX30009_DT_AHPF_BYPASS_ALT 15
```

相关声明：[MAX30009_DT_AHPF_BYPASS_ALT](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga39df781c81760e414d8b4b362a4509aa)。

模拟高通滤波器旁路（AHPF Bypassed），电阻断开，内部电容短接。

<a id="define-members-7"></a>

### 生物阻抗仪表放大器功耗模式（BioZ instrumentation amplifier power mode）

设备树属性（Devicetree Property）`bioz-ina-mode` 的取值。

<a id="r_ga3e96103029c7463a22631ed23a5593de"></a>

```c
#define MAX30009_DT_INA_MODE_HIGH_POWER 0
```

相关声明：[MAX30009_DT_INA_MODE_HIGH_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga3e96103029c7463a22631ed23a5593de)。

高功耗、低噪声模式（High-power, Low-noise Mode）。

<a id="r_gaf68570476daff617361570f8ff14fb0a"></a>

```c
#define MAX30009_DT_INA_MODE_LOW_POWER 1
```

相关声明：[MAX30009_DT_INA_MODE_LOW_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gaf68570476daff617361570f8ff14fb0a)。

低功耗模式（Low-power Mode）。

<a id="define-members-8"></a>

### 生物阻抗接收通道增益（BioZ receive-channel gain）

设备树属性（Devicetree Property）`bioz-gain` 的取值。

<a id="r_ga079864685fb2f5db3c438b4d0929d758"></a>

```c
#define MAX30009_DT_GAIN_1X 0
```

相关声明：[MAX30009_DT_GAIN_1X](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga079864685fb2f5db3c438b4d0929d758)。

1 倍增益（Gain）。

<a id="r_ga192b7009387797a9bbd6d23b50b1ddf8"></a>

```c
#define MAX30009_DT_GAIN_2X 1
```

相关声明：[MAX30009_DT_GAIN_2X](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga192b7009387797a9bbd6d23b50b1ddf8)。

2 倍增益（Gain）。

<a id="r_ga87437861657b96c5eb68ae98b0c2194e"></a>

```c
#define MAX30009_DT_GAIN_5X 2
```

相关声明：[MAX30009_DT_GAIN_5X](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga87437861657b96c5eb68ae98b0c2194e)。

5 倍增益（Gain）。

<a id="r_gafff2a350471233f0ee3176dd62d45caa"></a>

```c
#define MAX30009_DT_GAIN_10X 3
```

相关声明：[MAX30009_DT_GAIN_10X](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gafff2a350471233f0ee3176dd62d45caa)。

10 倍增益（Gain）。

<a id="define-members-9"></a>

### 生物阻抗直流恢复开关（BioZ DC-restore switch）

设备树属性（Devicetree Property）`bioz-dc-restore` 的取值。

<a id="r_ga16d78110e066d1e7863e587139662a3b"></a>

```c
#define MAX30009_DT_DC_RESTORE_OPEN 0
```

相关声明：[MAX30009_DT_DC_RESTORE_OPEN](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga16d78110e066d1e7863e587139662a3b)。

DC_RESTORE 开关断开（Open）。

<a id="r_ga5f03bf767c1caeec5e75f155a0803e58"></a>

```c
#define MAX30009_DT_DC_RESTORE_CLOSED 1
```

相关声明：[MAX30009_DT_DC_RESTORE_CLOSED](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga5f03bf767c1caeec5e75f155a0803e58)。

DC_RESTORE 开关闭合（Closed）。

<a id="define-members-10"></a>

### 生物阻抗放大器范围（BioZ amplifier range）

设备树属性（Devicetree Property）`bioz-amp-rge` 的取值。

<a id="r_ga69fb55de7de51ad286c4900665875456"></a>

```c
#define MAX30009_DT_AMP_RGE_LOW 0
```

相关声明：[MAX30009_DT_AMP_RGE_LOW](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga69fb55de7de51ad286c4900665875456)。

低（Low）。

<a id="r_ga952ad7341f0f3d36d282588f7006f285"></a>

```c
#define MAX30009_DT_AMP_RGE_MEDIUM_LOW 1
```

相关声明：[MAX30009_DT_AMP_RGE_MEDIUM_LOW](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga952ad7341f0f3d36d282588f7006f285)。

中低（Medium-low）。

<a id="r_ga0bb9e45e6edd56c36793fc24762354c4"></a>

```c
#define MAX30009_DT_AMP_RGE_MEDIUM_HIGH 2
```

相关声明：[MAX30009_DT_AMP_RGE_MEDIUM_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga0bb9e45e6edd56c36793fc24762354c4)。

中高（Medium-high）。

<a id="r_ga986e2e0493cbe17733548c50aa0770ac"></a>

```c
#define MAX30009_DT_AMP_RGE_HIGH 3
```

相关声明：[MAX30009_DT_AMP_RGE_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga986e2e0493cbe17733548c50aa0770ac)。

高（High）。

<a id="define-members-11"></a>

### 生物阻抗放大器带宽（BioZ amplifier bandwidth）

设备树属性（Devicetree Property）`bioz-amp-bw` 的取值。

<a id="r_ga871b99987851e5c081793b897b95d880"></a>

```c
#define MAX30009_DT_AMP_BW_LOW 0
```

相关声明：[MAX30009_DT_AMP_BW_LOW](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga871b99987851e5c081793b897b95d880)。

低带宽（Low Bandwidth）。

<a id="r_ga21e960883bbc8e142d29eb56c8913e2c"></a>

```c
#define MAX30009_DT_AMP_BW_MEDIUM_LOW 1
```

相关声明：[MAX30009_DT_AMP_BW_MEDIUM_LOW](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga21e960883bbc8e142d29eb56c8913e2c)。

中低带宽（Medium-low Bandwidth）。

<a id="r_ga90b04bf9109310d261e0654c0bdeac4b"></a>

```c
#define MAX30009_DT_AMP_BW_MEDIUM_HIGH 2
```

相关声明：[MAX30009_DT_AMP_BW_MEDIUM_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga90b04bf9109310d261e0654c0bdeac4b)。

中高带宽（Medium-high Bandwidth）。

<a id="r_gab17aff7f8fff6f1567d72332dc9b6122"></a>

```c
#define MAX30009_DT_AMP_BW_HIGH 3
```

相关声明：[MAX30009_DT_AMP_BW_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gab17aff7f8fff6f1567d72332dc9b6122)。

高带宽（High Bandwidth）。

<a id="define-members-12"></a>

### 生物阻抗Q通道解调器时钟相位（BioZ Q-channel demodulator clock phase）

设备树属性（Devicetree Property）`bioz-q-clk-phase` 的取值。

<a id="r_ga0a2058016ddfbf6870615185401a6736"></a>

```c
#define MAX30009_DT_Q_CLK_PHASE_NORMAL 0
```

相关声明：[MAX30009_DT_Q_CLK_PHASE_NORMAL](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga0a2058016ddfbf6870615185401a6736)。

正常工作（Normal Operation），Q 解调器时钟处于正交相位（Quadrature Phase）。

<a id="r_ga21de44938fa077f53f3817ed429d10ba"></a>

```c
#define MAX30009_DT_Q_CLK_PHASE_I 1
```

相关声明：[MAX30009_DT_Q_CLK_PHASE_I](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga21de44938fa077f53f3817ed429d10ba)。

同相（I Phase），Q 解调器时钟与激励同相（In Phase with Stimulus）。

<a id="define-members-13"></a>

### 生物阻抗I通道解调器时钟相位（BioZ I-channel demodulator clock phase）

设备树属性（Devicetree Property）`bioz-i-clk-phase` 的取值。

<a id="r_gae8dfa4eedba8af8604d266ef10dc837a"></a>

```c
#define MAX30009_DT_I_CLK_PHASE_NORMAL 0
```

相关声明：[MAX30009_DT_I_CLK_PHASE_NORMAL](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gae8dfa4eedba8af8604d266ef10dc837a)。

正常工作（Normal Operation），I 解调器时钟与激励同相（In Phase with Stimulus）。

<a id="r_gaac38a313c80db236b306b3c8cdbe5eb5"></a>

```c
#define MAX30009_DT_I_CLK_PHASE_Q 1
```

相关声明：[MAX30009_DT_I_CLK_PHASE_Q](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gaac38a313c80db236b306b3c8cdbe5eb5)。

正交相位（Q Phase），I 解调器时钟处于正交相位（Quadrature Phase）。

<a id="define-members-14"></a>

### 生物阻抗多路复用器内部负载电阻（BioZ mux internal-load resistor）

设备树属性（Devicetree Property）`bmux-rsel` 的取值。

<a id="r_ga24312672f0e42cc46fcb734dcebdca88"></a>

```c
#define MAX30009_DT_BMUX_RSEL_5100R 0
```

相关声明：[MAX30009_DT_BMUX_RSEL_5100R](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga24312672f0e42cc46fcb734dcebdca88)。

5100 欧姆（Ohm）。

<a id="r_gaa4f23600e8aa83a2a5163877a290684d"></a>

```c
#define MAX30009_DT_BMUX_RSEL_900R 1
```

相关声明：[MAX30009_DT_BMUX_RSEL_900R](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gaa4f23600e8aa83a2a5163877a290684d)。

900 欧姆（Ohm）。

<a id="r_gac937d35ad1c6ce11e57124f2fcd40818"></a>

```c
#define MAX30009_DT_BMUX_RSEL_600R 2
```

相关声明：[MAX30009_DT_BMUX_RSEL_600R](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gac937d35ad1c6ce11e57124f2fcd40818)。

600 欧姆（Ohm）。

<a id="r_ga78b2a37b90295e2b05d0b8ddcc58fd4a"></a>

```c
#define MAX30009_DT_BMUX_RSEL_280R 3
```

相关声明：[MAX30009_DT_BMUX_RSEL_280R](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga78b2a37b90295e2b05d0b8ddcc58fd4a)。

280 欧姆（Ohm）。

<a id="define-members-15"></a>

### 生物阻抗皮肤电反应负载电阻（BioZ GSR-load resistor）

设备树属性（Devicetree Property）`bmux-gsr-rsel` 的取值。

<a id="r_gaa544c3b7f90059cf2278e66bd8e471c3"></a>

```c
#define MAX30009_DT_BMUX_GSR_RSEL_25_7K 0
```

相关声明：[MAX30009_DT_BMUX_GSR_RSEL_25_7K](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gaa544c3b7f90059cf2278e66bd8e471c3)。

25.7 千欧（kOhm）。

<a id="r_gacb2476eb94f953517bcd085ecbd7840d"></a>

```c
#define MAX30009_DT_BMUX_GSR_RSEL_101K 1
```

相关声明：[MAX30009_DT_BMUX_GSR_RSEL_101K](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gacb2476eb94f953517bcd085ecbd7840d)。

101 千欧（kOhm）。

<a id="r_ga4726b52019759ead386aee1fb71fb71b"></a>

```c
#define MAX30009_DT_BMUX_GSR_RSEL_505K 2
```

相关声明：[MAX30009_DT_BMUX_GSR_RSEL_505K](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga4726b52019759ead386aee1fb71fb71b)。

505 千欧（kOhm）。

<a id="r_gae915dca5120a07a0c2e6588bd97adf7b"></a>

```c
#define MAX30009_DT_BMUX_GSR_RSEL_1000K 3
```

相关声明：[MAX30009_DT_BMUX_GSR_RSEL_1000K](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gae915dca5120a07a0c2e6588bd97adf7b)。

1000 千欧（kOhm）。

<a id="define-members-16"></a>

### 生物阻抗正输入电极分配（BioZ positive-input (BIP) electrode assignment）

设备树属性（Devicetree Property）`bip-assign` 的取值。

<a id="r_ga6e5853fa1428a3636d1910db83038c47"></a>

```c
#define MAX30009_DT_BIP_ASSIGN_EL1 0
```

相关声明：[MAX30009_DT_BIP_ASSIGN_EL1](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga6e5853fa1428a3636d1910db83038c47)。

电极（Electrode）EL1。

<a id="r_gae5816d626f8efae49fb568f9ea7cfa1b"></a>

```c
#define MAX30009_DT_BIP_ASSIGN_EL2A 1
```

相关声明：[MAX30009_DT_BIP_ASSIGN_EL2A](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gae5816d626f8efae49fb568f9ea7cfa1b)。

电极（Electrode）EL2A。

<a id="r_gafc179d0e7c59bab082bcecb0d0329731"></a>

```c
#define MAX30009_DT_BIP_ASSIGN_EL2B 2
```

相关声明：[MAX30009_DT_BIP_ASSIGN_EL2B](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gafc179d0e7c59bab082bcecb0d0329731)。

电极（Electrode）EL2B。

<a id="define-members-17"></a>

### 生物阻抗负输入电极分配（BioZ negative-input (BIN) electrode assignment）

设备树属性（Devicetree Property）`bin-assign` 的取值。

<a id="r_ga84bcb902a04ebcd18ac4da50b2fed64a"></a>

```c
#define MAX30009_DT_BIN_ASSIGN_EL4 0
```

相关声明：[MAX30009_DT_BIN_ASSIGN_EL4](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga84bcb902a04ebcd18ac4da50b2fed64a)。

电极（Electrode）EL4。

<a id="r_ga2c0398409d8b8d319519866564702ee6"></a>

```c
#define MAX30009_DT_BIN_ASSIGN_EL3A 1
```

相关声明：[MAX30009_DT_BIN_ASSIGN_EL3A](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga2c0398409d8b8d319519866564702ee6)。

电极（Electrode）EL3A。

<a id="r_ga64a1ea825c6b8dce119c55998f164516"></a>

```c
#define MAX30009_DT_BIN_ASSIGN_EL3B 2
```

相关声明：[MAX30009_DT_BIN_ASSIGN_EL3B](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga64a1ea825c6b8dce119c55998f164516)。

电极（Electrode）EL3B。

<a id="define-members-18"></a>

### 生物阻抗正驱动电极分配（BioZ positive-drive (DRVP) electrode assignment）

设备树属性（Devicetree Property）`drvp-assign` 的取值。

<a id="r_gadc0a8cc22365921f8887f92675da3ea2"></a>

```c
#define MAX30009_DT_DRVP_ASSIGN_EL1 0
```

相关声明：[MAX30009_DT_DRVP_ASSIGN_EL1](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gadc0a8cc22365921f8887f92675da3ea2)。

电极（Electrode）EL1，低电阻（Low Resistance）。

<a id="r_ga4ba26c119eca542d11286dae1e3b7386"></a>

```c
#define MAX30009_DT_DRVP_ASSIGN_EL2A 1
```

相关声明：[MAX30009_DT_DRVP_ASSIGN_EL2A](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga4ba26c119eca542d11286dae1e3b7386)。

电极（Electrode）EL2A。

<a id="r_ga70b81356cd3bd1bd866e33e9541c4ec6"></a>

```c
#define MAX30009_DT_DRVP_ASSIGN_EL2B 2
```

相关声明：[MAX30009_DT_DRVP_ASSIGN_EL2B](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga70b81356cd3bd1bd866e33e9541c4ec6)。

电极（Electrode）EL2B。

<a id="define-members-19"></a>

### 生物阻抗负驱动电极分配（BioZ negative-drive (DRVN) electrode assignment）

设备树属性（Devicetree Property）`drvn-assign` 的取值。

<a id="r_gacf78a7f404eac8ae42272fca26600d76"></a>

```c
#define MAX30009_DT_DRVN_ASSIGN_EL4 0
```

相关声明：[MAX30009_DT_DRVN_ASSIGN_EL4](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gacf78a7f404eac8ae42272fca26600d76)。

电极（Electrode）EL4，低电阻（Low Resistance）。

<a id="r_gad7a97e683f5cea347234a08fcdae2a47"></a>

```c
#define MAX30009_DT_DRVN_ASSIGN_EL3A 1
```

相关声明：[MAX30009_DT_DRVN_ASSIGN_EL3A](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gad7a97e683f5cea347234a08fcdae2a47)。

电极（Electrode）EL3A。

<a id="r_ga7d6b1d4efe20541dc7e3ae3719fb22ce"></a>

```c
#define MAX30009_DT_DRVN_ASSIGN_EL3B 2
```

相关声明：[MAX30009_DT_DRVN_ASSIGN_EL3B](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga7d6b1d4efe20541dc7e3ae3719fb22ce)。

电极（Electrode）EL3B。

<a id="define-members-20"></a>

### 直流导联脱落检测电流极性（DC lead-off current polarity）

设备树属性（Devicetree Property）`loff-ipol` 的取值。

<a id="r_ga66b13ba0892e1603802b329556bcd7bc"></a>

```c
#define MAX30009_DT_LOFF_IPOL_NON_INVERTED 0
```

相关声明：[MAX30009_DT_LOFF_IPOL_NON_INVERTED](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga66b13ba0892e1603802b329556bcd7bc)。

不反转（Non-inverted）：BIP 输出电流（Sources），BIN 吸收电流（Sinks）。

<a id="r_gae47f2f0ddc69d863a9cf3e1ac57048aa"></a>

```c
#define MAX30009_DT_LOFF_IPOL_INVERTED 1
```

相关声明：[MAX30009_DT_LOFF_IPOL_INVERTED](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gae47f2f0ddc69d863a9cf3e1ac57048aa)。

反转（Inverted）：BIP 吸收电流（Sinks），BIN 输出电流（Sources）。

<a id="define-members-21"></a>

### 直流导联脱落检测电流大小（DC lead-off current magnitude）

设备树属性（Devicetree Property）`loff-imag` 的取值。

<a id="r_gaa922dc99d310e5d9afc6fac89f6e9903"></a>

```c
#define MAX30009_DT_LOFF_IMAG_0NA 0
```

相关声明：[MAX30009_DT_LOFF_IMAG_0NA](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gaa922dc99d310e5d9afc6fac89f6e9903)。

0 nA，电流源禁用（Sources Disabled）。

<a id="r_gad0c138c2702ff526419ff125c197c53d"></a>

```c
#define MAX30009_DT_LOFF_IMAG_5NA 1
```

相关声明：[MAX30009_DT_LOFF_IMAG_5NA](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gad0c138c2702ff526419ff125c197c53d)。

5 纳安（nA）。

<a id="r_gaa0dc8938e6ff6bb58d4729a9be887d2f"></a>

```c
#define MAX30009_DT_LOFF_IMAG_10NA 2
```

相关声明：[MAX30009_DT_LOFF_IMAG_10NA](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gaa0dc8938e6ff6bb58d4729a9be887d2f)。

10 纳安（nA）。

<a id="r_ga91dad26815f3abcf6446923697fa6f75"></a>

```c
#define MAX30009_DT_LOFF_IMAG_20NA 3
```

相关声明：[MAX30009_DT_LOFF_IMAG_20NA](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga91dad26815f3abcf6446923697fa6f75)。

20 纳安（nA）。

<a id="r_gad3d60a5774a548c7be554cff137a5f2b"></a>

```c
#define MAX30009_DT_LOFF_IMAG_50NA 4
```

相关声明：[MAX30009_DT_LOFF_IMAG_50NA](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gad3d60a5774a548c7be554cff137a5f2b)。

50 纳安（nA）。

<a id="r_ga553fdf3936d294d1a8139378944ec62e"></a>

```c
#define MAX30009_DT_LOFF_IMAG_100NA 5
```

相关声明：[MAX30009_DT_LOFF_IMAG_100NA](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga553fdf3936d294d1a8139378944ec62e)。

100 纳安（nA）。

<a id="define-members-22"></a>

### 导联偏置电阻值（Lead-bias resistor value）

设备树属性（Devicetree Property）`rbias-value` 的取值。

<a id="r_ga58cf97f6f2a776c70525d993dc005a8f"></a>

```c
#define MAX30009_DT_RBIAS_50M 0
```

相关声明：[MAX30009_DT_RBIAS_50M](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga58cf97f6f2a776c70525d993dc005a8f)。

50 兆欧（MOhm）。

<a id="r_gadcc190ecd517146a6440ea4758cdaa04"></a>

```c
#define MAX30009_DT_RBIAS_100M 1
```

相关声明：[MAX30009_DT_RBIAS_100M](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gadcc190ecd517146a6440ea4758cdaa04)。

100 兆欧（MOhm）。

<a id="r_ga742b6c3549081fbbf78eedf24e02e135"></a>

```c
#define MAX30009_DT_RBIAS_200M 2
```

相关声明：[MAX30009_DT_RBIAS_200M](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga742b6c3549081fbbf78eedf24e02e135)。

200 兆欧（MOhm）。


## 3.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P208_max30009.h_源码浏览.md)
- [MAX30009_DT_DHPF_BYPASS](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga8eb31c9c63eadb978c020fccadfac492)
- [MAX30009_DT_DHPF_0_00025_SR](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gab8608675fcbc8652bbf06df8b44c1c6e)
- [MAX30009_DT_DHPF_0_002_SR](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga2cd7f98fcd61d9c33694ad94fcc5a67c)
- [MAX30009_DT_DLPF_BYPASS](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gabfbc4a0a7a9d01e1c900deeb19e2d348)
- [MAX30009_DT_DLPF_0_005_SR](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga1e0976e21749f72a9b1aa23eb7607cd8)
- [MAX30009_DT_DLPF_0_02_SR](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gac0034d299f7b00be54a534c3e946aec1)
- [MAX30009_DT_DLPF_0_08_SR](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga150857ee16c906db64132f6af02c7ea1)
- [MAX30009_DT_DLPF_0_25_SR](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga700307982ea8aa304c97fcad2fe54a25)
- [MAX30009_DT_CMP_I](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga80d5099867fa89d2056331dc1ad77920)
- [MAX30009_DT_CMP_Q](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gadfc473e2486322f94dcaec2338524edd)
- [MAX30009_DT_CMP_Z](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga97dba7ad62da9497c9ea5a99ec63529e)
- [MAX30009_DT_DRV_MODE_CURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga24babbc19fc375b8f002b58c4a5b9531)
- [MAX30009_DT_DRV_MODE_VOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga561188fefa0505bb477ea48b14141dad)
- [MAX30009_DT_DRV_MODE_HBRIDGE](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga4df2c8a895ec807a3d856595e3b6a7b4)
- [MAX30009_DT_DRV_MODE_STANDBY](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gaa77063a044e4363481c8f8e4a01b73b4)
- [MAX30009_DT_IDRV_RGE_552_5K](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga909174a9f6539a49517d87e5b445e125)
- [MAX30009_DT_IDRV_RGE_110_5K](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga8aac47687800236427f653ea2a35949a)
- [MAX30009_DT_IDRV_RGE_5_525K](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gac3d066858d16e65904488d8fca3259f2)
- [MAX30009_DT_IDRV_RGE_276_25R](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gaa90c7a5f5256ff7e6b3b532bc764b1df)
- [MAX30009_DT_VDRV_MAG_50MV](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gaa90ab9b36f935e203c786a23c6cb28de)
- [MAX30009_DT_VDRV_MAG_100MV](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga92f2610117e2629038cbfe9a85360907)
- [MAX30009_DT_VDRV_MAG_250MV](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gac18eb324c01ca4f5c3e1b769cffb5a3a)
- [MAX30009_DT_VDRV_MAG_500MV](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga17df936472b4d3f2c5a168301a77a726)
- [MAX30009_DT_AHPF_100HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gab17efef4bcc4fcc9ffcd169cfa99ab62)
- [MAX30009_DT_AHPF_200HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga32ad059208543e6a11bd6bc456a667ca)
- [MAX30009_DT_AHPF_500HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga53c802e1cde30dc561d691f210185ecb)
- [MAX30009_DT_AHPF_1KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga66add46c63a039ba6733a57a05d491be)
- [MAX30009_DT_AHPF_2KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gad40a309cec6a02f422da6b32411f48cc)
- [MAX30009_DT_AHPF_5KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga34fb05b6b39cb0bc0c12616d7b85a0a1)
- [MAX30009_DT_AHPF_10KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga27c68f77eedb7b000f8f6b9478f888ac)
- [MAX30009_DT_AHPF_BYPASS](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga2b94523d3f46d516ec5843bfe0afec9c)
- [MAX30009_DT_AHPF_42_4M](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gaed5d777b485d170a333bf84879e5c0cd)
- [MAX30009_DT_AHPF_21_2M](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga28d875778decaaee769a2d0aba59ccbd)
- [MAX30009_DT_AHPF_8_4M](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga450809b02e66e5d06e79db8c51078730)
- [MAX30009_DT_AHPF_4_2M](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gaebfb3f4324cb1de4d8fbe25778485e78)
- [MAX30009_DT_AHPF_2_2M](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga75b3d909f58ca47a57eea8af9279669f)
- [MAX30009_DT_AHPF_848K](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga5e29b90e65316f2b33a842af25c6d2b3)
- [MAX30009_DT_AHPF_848K_ALT](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gaab05f2c71b42ad45cd2c83f5f10e3fd7)
- [MAX30009_DT_AHPF_BYPASS_ALT](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga39df781c81760e414d8b4b362a4509aa)
- [MAX30009_DT_INA_MODE_HIGH_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga3e96103029c7463a22631ed23a5593de)
- [MAX30009_DT_INA_MODE_LOW_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gaf68570476daff617361570f8ff14fb0a)
- [MAX30009_DT_GAIN_1X](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga079864685fb2f5db3c438b4d0929d758)
- [MAX30009_DT_GAIN_2X](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga192b7009387797a9bbd6d23b50b1ddf8)
- [MAX30009_DT_GAIN_5X](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga87437861657b96c5eb68ae98b0c2194e)
- [MAX30009_DT_GAIN_10X](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gafff2a350471233f0ee3176dd62d45caa)
- [MAX30009_DT_DC_RESTORE_OPEN](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga16d78110e066d1e7863e587139662a3b)
- [MAX30009_DT_DC_RESTORE_CLOSED](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga5f03bf767c1caeec5e75f155a0803e58)
- [MAX30009_DT_AMP_RGE_LOW](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga69fb55de7de51ad286c4900665875456)
- [MAX30009_DT_AMP_RGE_MEDIUM_LOW](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga952ad7341f0f3d36d282588f7006f285)
- [MAX30009_DT_AMP_RGE_MEDIUM_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga0bb9e45e6edd56c36793fc24762354c4)
- [MAX30009_DT_AMP_RGE_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga986e2e0493cbe17733548c50aa0770ac)
- [MAX30009_DT_AMP_BW_LOW](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga871b99987851e5c081793b897b95d880)
- [MAX30009_DT_AMP_BW_MEDIUM_LOW](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga21e960883bbc8e142d29eb56c8913e2c)
- [MAX30009_DT_AMP_BW_MEDIUM_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga90b04bf9109310d261e0654c0bdeac4b)
- [MAX30009_DT_AMP_BW_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gab17aff7f8fff6f1567d72332dc9b6122)
- [MAX30009_DT_Q_CLK_PHASE_NORMAL](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga0a2058016ddfbf6870615185401a6736)
- [MAX30009_DT_Q_CLK_PHASE_I](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga21de44938fa077f53f3817ed429d10ba)
- [MAX30009_DT_I_CLK_PHASE_NORMAL](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gae8dfa4eedba8af8604d266ef10dc837a)
- [MAX30009_DT_I_CLK_PHASE_Q](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gaac38a313c80db236b306b3c8cdbe5eb5)
- [MAX30009_DT_BMUX_RSEL_5100R](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga24312672f0e42cc46fcb734dcebdca88)
- [MAX30009_DT_BMUX_RSEL_900R](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gaa4f23600e8aa83a2a5163877a290684d)
- [MAX30009_DT_BMUX_RSEL_600R](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gac937d35ad1c6ce11e57124f2fcd40818)
- [MAX30009_DT_BMUX_RSEL_280R](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga78b2a37b90295e2b05d0b8ddcc58fd4a)
- [MAX30009_DT_BMUX_GSR_RSEL_25_7K](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gaa544c3b7f90059cf2278e66bd8e471c3)
- [MAX30009_DT_BMUX_GSR_RSEL_101K](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gacb2476eb94f953517bcd085ecbd7840d)
- [MAX30009_DT_BMUX_GSR_RSEL_505K](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga4726b52019759ead386aee1fb71fb71b)
- [MAX30009_DT_BMUX_GSR_RSEL_1000K](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gae915dca5120a07a0c2e6588bd97adf7b)
- [MAX30009_DT_BIP_ASSIGN_EL1](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga6e5853fa1428a3636d1910db83038c47)
- [MAX30009_DT_BIP_ASSIGN_EL2A](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gae5816d626f8efae49fb568f9ea7cfa1b)
- [MAX30009_DT_BIP_ASSIGN_EL2B](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gafc179d0e7c59bab082bcecb0d0329731)
- [MAX30009_DT_BIN_ASSIGN_EL4](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga84bcb902a04ebcd18ac4da50b2fed64a)
- [MAX30009_DT_BIN_ASSIGN_EL3A](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga2c0398409d8b8d319519866564702ee6)
- [MAX30009_DT_BIN_ASSIGN_EL3B](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga64a1ea825c6b8dce119c55998f164516)
- [MAX30009_DT_DRVP_ASSIGN_EL1](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gadc0a8cc22365921f8887f92675da3ea2)
- [MAX30009_DT_DRVP_ASSIGN_EL2A](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga4ba26c119eca542d11286dae1e3b7386)
- [MAX30009_DT_DRVP_ASSIGN_EL2B](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga70b81356cd3bd1bd866e33e9541c4ec6)
- [MAX30009_DT_DRVN_ASSIGN_EL4](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gacf78a7f404eac8ae42272fca26600d76)
- [MAX30009_DT_DRVN_ASSIGN_EL3A](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gad7a97e683f5cea347234a08fcdae2a47)
- [MAX30009_DT_DRVN_ASSIGN_EL3B](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga7d6b1d4efe20541dc7e3ae3719fb22ce)
- [MAX30009_DT_LOFF_IPOL_NON_INVERTED](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga66b13ba0892e1603802b329556bcd7bc)
- [MAX30009_DT_LOFF_IPOL_INVERTED](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gae47f2f0ddc69d863a9cf3e1ac57048aa)
- [MAX30009_DT_LOFF_IMAG_0NA](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gaa922dc99d310e5d9afc6fac89f6e9903)
- [MAX30009_DT_LOFF_IMAG_5NA](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gad0c138c2702ff526419ff125c197c53d)
- [MAX30009_DT_LOFF_IMAG_10NA](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gaa0dc8938e6ff6bb58d4729a9be887d2f)
- [MAX30009_DT_LOFF_IMAG_20NA](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga91dad26815f3abcf6446923697fa6f75)
- [MAX30009_DT_LOFF_IMAG_50NA](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gad3d60a5774a548c7be554cff137a5f2b)
- [MAX30009_DT_LOFF_IMAG_100NA](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga553fdf3936d294d1a8139378944ec62e)
- [MAX30009_DT_RBIAS_50M](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga58cf97f6f2a776c70525d993dc005a8f)
- [MAX30009_DT_RBIAS_100M](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#gadcc190ecd517146a6440ea4758cdaa04)
- [MAX30009_DT_RBIAS_200M](https://docs.zephyrproject.org/latest/doxygen/html/group__max30009__interface.html#ga742b6c3549081fbbf78eedf24e02e135)

<a id="header-details"></a>

---

[上一章](P002_zephyr__bluetooth__mesh__cdb.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P004_zephyr__bluetooth__gatt.h_文件参考.md)
