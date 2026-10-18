---
id: learning.zephyr-docs.api-file-usb-network-reference.page-7
title: zephyr__dt-bindings__sensor__tmag5273.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2tmag5273_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_zephyr\_\_dt-bindings\_\_sensor\_\_tmag5273.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2tmag5273_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

the TI TMAG5273 3-axis Hall-effect sensor的设备树绑定常量（Devicetree Binding Constants）。

<a id="details"></a>

```c
#include <zephyr/dt-bindings/dt-util.h>
```

查看此文件的源码。

the TI TMAG5273 3-axis Hall-effect sensor的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 7.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 工作模式（Operating mode）

设备树属性（Devicetree Property）`operation-mode` 的取值。

<a id="r_ga7c4ac425f1167fca06025db9a2b92153"></a>

```c
#define TMAG5273_DT_OPER_MODE_CONTINUOUS 0
```

相关声明：[TMAG5273_DT_OPER_MODE_CONTINUOUS](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga7c4ac425f1167fca06025db9a2b92153)。

连续转换（Continuous Conversion）。

<a id="r_ga13fea164a14fc3a2d38aebce67e38e12"></a>

```c
#define TMAG5273_DT_OPER_MODE_STANDBY 1
```

相关声明：[TMAG5273_DT_OPER_MODE_STANDBY](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga13fea164a14fc3a2d38aebce67e38e12)。

待机（Standby），按请求进行转换。

<a id="define-members-1"></a>

### 磁场测量轴选择（Magnetic Axis Selection）

设备树属性（Devicetree Property）`axis` 的取值。

<a id="r_ga258a2507f733c059f2b5b212d505ccd8"></a>

```c
#define TMAG5273_DT_AXIS_NONE 0x0
```

相关声明：[TMAG5273_DT_AXIS_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga258a2507f733c059f2b5b212d505ccd8)。

不选择任何轴（No Axis）。

<a id="r_ga3040ac9025679745dbfe52463f95bd9f"></a>

```c
#define TMAG5273_DT_AXIS_X 0x1
```

相关声明：[TMAG5273_DT_AXIS_X](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga3040ac9025679745dbfe52463f95bd9f)。

X 轴（X axis）。

<a id="r_ga0d352bd659851f02169036f205e8b012"></a>

```c
#define TMAG5273_DT_AXIS_Y 0x2
```

相关声明：[TMAG5273_DT_AXIS_Y](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga0d352bd659851f02169036f205e8b012)。

Y 轴（Y axis）。

<a id="r_ga10d89d64876dc4d32398e2765ef5079f"></a>

```c
#define TMAG5273_DT_AXIS_Z 0x4
```

相关声明：[TMAG5273_DT_AXIS_Z](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga10d89d64876dc4d32398e2765ef5079f)。

Z 轴（Z axis）。

<a id="r_ga08aacefba8f390ac1ace72e672de83cc"></a>

```c
#define TMAG5273_DT_AXIS_XY (TMAG5273_DT_AXIS_X | TMAG5273_DT_AXIS_Y)
```

相关声明：[TMAG5273_DT_AXIS_XY](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga08aacefba8f390ac1ace72e672de83cc)、[TMAG5273_DT_AXIS_X](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga3040ac9025679745dbfe52463f95bd9f)、[TMAG5273_DT_AXIS_Y](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga0d352bd659851f02169036f205e8b012)。

X 轴和 Y 轴（Axes）。

<a id="r_ga53b02b4b3cf5126abd4ab939c74fc633"></a>

```c
#define TMAG5273_DT_AXIS_XZ (TMAG5273_DT_AXIS_X | TMAG5273_DT_AXIS_Z)
```

相关声明：[TMAG5273_DT_AXIS_XZ](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga53b02b4b3cf5126abd4ab939c74fc633)、[TMAG5273_DT_AXIS_X](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga3040ac9025679745dbfe52463f95bd9f)、[TMAG5273_DT_AXIS_Z](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga10d89d64876dc4d32398e2765ef5079f)。

X 轴和 Z 轴（Axes）。

<a id="r_ga1ee1d7f126feb9b5652670e53d24f0b6"></a>

```c
#define TMAG5273_DT_AXIS_YZ (TMAG5273_DT_AXIS_Y | TMAG5273_DT_AXIS_Z)
```

相关声明：[TMAG5273_DT_AXIS_YZ](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga1ee1d7f126feb9b5652670e53d24f0b6)、[TMAG5273_DT_AXIS_Y](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga0d352bd659851f02169036f205e8b012)、[TMAG5273_DT_AXIS_Z](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga10d89d64876dc4d32398e2765ef5079f)。

Y 轴和 Z 轴（Axes）。

<a id="r_gae16a8c01eafc1196d8fe0ffcf4976c72"></a>

```c
#define TMAG5273_DT_AXIS_XYZ (TMAG5273_DT_AXIS_X | TMAG5273_DT_AXIS_Y | TMAG5273_DT_AXIS_Z)
```

相关声明：[TMAG5273_DT_AXIS_XYZ](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#gae16a8c01eafc1196d8fe0ffcf4976c72)、[TMAG5273_DT_AXIS_X](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga3040ac9025679745dbfe52463f95bd9f)、[TMAG5273_DT_AXIS_Y](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga0d352bd659851f02169036f205e8b012)、[TMAG5273_DT_AXIS_Z](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga10d89d64876dc4d32398e2765ef5079f)。

全部轴（All Axes）。

<a id="r_ga6dcc34a5877ff11329c570f27184bbe7"></a>

```c
#define TMAG5273_DT_AXIS_XYX 0x8
```

相关声明：[TMAG5273_DT_AXIS_XYX](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga6dcc34a5877ff11329c570f27184bbe7)。

依次为 X 轴、Y 轴、X 轴（Axes）。

<a id="r_ga000a0c930e0cdad6e7e91dc887004e4f"></a>

```c
#define TMAG5273_DT_AXIS_YXY 0x9
```

相关声明：[TMAG5273_DT_AXIS_YXY](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga000a0c930e0cdad6e7e91dc887004e4f)。

依次为 Y 轴、X 轴、Y 轴（Axes）。

<a id="r_gad778956fdac899196bc7782e2306d18d"></a>

```c
#define TMAG5273_DT_AXIS_YZY 0xA
```

相关声明：[TMAG5273_DT_AXIS_YZY](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#gad778956fdac899196bc7782e2306d18d)。

依次为 Y 轴、Z 轴、Y 轴（Axes）。

<a id="r_ga6e1e7c54e34d9f82abe8c8f4e38826ed"></a>

```c
#define TMAG5273_DT_AXIS_XZX 0xB
```

相关声明：[TMAG5273_DT_AXIS_XZX](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga6e1e7c54e34d9f82abe8c8f4e38826ed)。

依次为 X 轴、Z 轴、X 轴（Axes）。

<a id="define-members-2"></a>

### 磁场测量量程（Magnetic Measurement Range）

设备树 `range` 属性的取值。

<a id="r_gad536884f65cfb8d90f35c15b26afec04"></a>

```c
#define TMAG5273_DT_AXIS_RANGE_LOW 0
```

相关声明：[TMAG5273_DT_AXIS_RANGE_LOW](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#gad536884f65cfb8d90f35c15b26afec04)。

低量程（Low Range）。

<a id="r_ga6b279486342219e7dfd5555c34cc7d37"></a>

```c
#define TMAG5273_DT_AXIS_RANGE_HIGH 1
```

相关声明：[TMAG5273_DT_AXIS_RANGE_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga6b279486342219e7dfd5555c34cc7d37)。

高量程（High Range）。

<a id="r_ga2aa9dfa7a74f61a821d2d7f0c2629b55"></a>

```c
#define TMAG5273_DT_AXIS_RANGE_RUNTIME 2
```

相关声明：[TMAG5273_DT_AXIS_RANGE_RUNTIME](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga2aa9dfa7a74f61a821d2d7f0c2629b55)。

运行时选择量程（Range Selected at Runtime）。

<a id="define-members-3"></a>

### 中断路由模式（Interrupt Routing Mode）

中断路由模式（Interrupt Routing Mode）。

<a id="r_gac7a80f12307ebb946ab106381704f2bc"></a>

```c
#define TMAG5273_DT_INT_THROUGH_INT 0
```

相关声明：[TMAG5273_DT_INT_THROUGH_INT](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#gac7a80f12307ebb946ab106381704f2bc)。

通过 INT 引脚产生中断（Interrupt）。

<a id="r_ga97a154a99cf41aaadfbcb4fbaaa0fbdc"></a>

```c
#define TMAG5273_DT_INT_THROUGH_INT_EXC_I2C 1
```

相关声明：[TMAG5273_DT_INT_THROUGH_INT_EXC_I2C](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga97a154a99cf41aaadfbcb4fbaaa0fbdc)。

使用 INT 引脚，但 I2C 总线访问期间除外。

<a id="r_ga47ffb1ce227b6fc8cccda39898dabb96"></a>

```c
#define TMAG5273_DT_INT_THROUGH_SCL 2
```

相关声明：[TMAG5273_DT_INT_THROUGH_SCL](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga47ffb1ce227b6fc8cccda39898dabb96)。

通过 SCL 引脚产生中断（Interrupt）。

<a id="r_ga5757c3a1364e72c3d4c0b30b5cfc0698"></a>

```c
#define TMAG5273_DT_INT_THROUGH_SCL_EXC_I2C 3
```

相关声明：[TMAG5273_DT_INT_THROUGH_SCL_EXC_I2C](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga5757c3a1364e72c3d4c0b30b5cfc0698)。

使用 SCL 引脚，但 I2C 总线访问期间除外。

<a id="define-members-4"></a>

### 阈值越过次数（Threshold Crossing Count）

触发中断前越过阈值的次数（Number of Threshold Crossings）。

<a id="r_ga71b6e856b5a5db7af4e4ed0001de2f66"></a>

```c
#define TMAG5273_DT_THRX_COUNT_1 0
```

相关声明：[TMAG5273_DT_THRX_COUNT_1](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga71b6e856b5a5db7af4e4ed0001de2f66)。

越过阈值 1 次后触发（Trigger after 1 Crossing）。

<a id="r_ga3940888f116795a9d060195fdb717ff1"></a>

```c
#define TMAG5273_DT_THRX_COUNT_4 1
```

相关声明：[TMAG5273_DT_THRX_COUNT_4](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga3940888f116795a9d060195fdb717ff1)。

越过阈值 4 次后触发（Trigger after 4 Crossings）。

<a id="define-members-5"></a>

### 阈值越过方向（Threshold Crossing Direction）

触发中断的阈值越过方向（Threshold-crossing Direction）。

<a id="r_gab59755856b8372698deab44d9b8ec9a2"></a>

```c
#define TMAG5273_DT_THRX_ABOVE 0
```

相关声明：[TMAG5273_DT_THRX_ABOVE](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#gab59755856b8372698deab44d9b8ec9a2)。

磁场强度上升至阈值（Threshold）以上。

<a id="r_ga348bd07ca130ff996bea612ad8cecba3"></a>

```c
#define TMAG5273_DT_THRX_BELOW 1
```

相关声明：[TMAG5273_DT_THRX_BELOW](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga348bd07ca130ff996bea612ad8cecba3)。

磁场强度下降至阈值（Threshold）以下。

<a id="r_ga630c77a70f3db408a139dd10b3a28bb1"></a>

```c
#define TMAG5273_DT_THRX_OUTSIDE 2
```

相关声明：[TMAG5273_DT_THRX_OUTSIDE](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga630c77a70f3db408a139dd10b3a28bb1)。

磁场强度离开阈值窗口（Threshold Window）。

<a id="r_gac0b966cb05b35abe701b8af474fd0498"></a>

```c
#define TMAG5273_DT_THRX_INSIDE 3
```

相关声明：[TMAG5273_DT_THRX_INSIDE](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#gac0b966cb05b35abe701b8af474fd0498)。

磁场强度进入阈值窗口（Threshold Window）。

<a id="define-members-6"></a>

### 磁体温度系数（Magnet Temperature Coefficient）

设备树属性（Devicetree Property）`temperature-coefficient` 的取值。

<a id="r_ga19f4de1abe7275ec75641e5e5ce47826"></a>

```c
#define TMAG5273_DT_TEMP_COEFF_NONE 0
```

相关声明：[TMAG5273_DT_TEMP_COEFF_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga19f4de1abe7275ec75641e5e5ce47826)。

不进行补偿（No Compensation）。

<a id="r_gaf51ec112fe16a5c8a5a55a42dd14fd92"></a>

```c
#define TMAG5273_DT_TEMP_COEFF_NDBFE 1
```

相关声明：[TMAG5273_DT_TEMP_COEFF_NDBFE](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#gaf51ec112fe16a5c8a5a55a42dd14fd92)。

钕铁硼磁体（原文为 NdBFe Magnet），温度系数为 0.12 %/°C。

<a id="r_gaec27747fbae8c0c62912431a3f9d2309"></a>

```c
#define TMAG5273_DT_TEMP_COEFF_CERAMIC 2
```

相关声明：[TMAG5273_DT_TEMP_COEFF_CERAMIC](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#gaec27747fbae8c0c62912431a3f9d2309)。

陶瓷磁体（Ceramic Magnet），温度系数为 0.2 %/°C。

<a id="define-members-7"></a>

### 角度与幅值计算（Angle and Magnitude Calculation）

设备树属性（Devicetree Property）`angle-magnitude-axis` 的取值。

<a id="r_ga7ba462d2a09ae0118a991c655fdca672"></a>

```c
#define TMAG5273_DT_ANGLE_MAG_NONE 0
```

相关声明：[TMAG5273_DT_ANGLE_MAG_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga7ba462d2a09ae0118a991c655fdca672)。

禁用（Disabled）。

<a id="r_gad34b392bf32680634ec9dddacee24c9b"></a>

```c
#define TMAG5273_DT_ANGLE_MAG_XY 1
```

相关声明：[TMAG5273_DT_ANGLE_MAG_XY](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#gad34b392bf32680634ec9dddacee24c9b)。

来自 X 轴和 Y 轴（Axes）。

<a id="r_gaa48cfafa9b65e23e5f5915fc32f65633"></a>

```c
#define TMAG5273_DT_ANGLE_MAG_YZ 2
```

相关声明：[TMAG5273_DT_ANGLE_MAG_YZ](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#gaa48cfafa9b65e23e5f5915fc32f65633)。

来自 Y 轴和 Z 轴（Axes）。

<a id="r_ga074869eda0ffdc0a88138b8b3caaafec"></a>

```c
#define TMAG5273_DT_ANGLE_MAG_XZ 3
```

相关声明：[TMAG5273_DT_ANGLE_MAG_XZ](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga074869eda0ffdc0a88138b8b3caaafec)。

来自 X 轴和 Z 轴（Axes）。

<a id="r_ga88151dfd7f1aaeb43df745e88ef49241"></a>

```c
#define TMAG5273_DT_ANGLE_MAG_RUNTIME 4
```

相关声明：[TMAG5273_DT_ANGLE_MAG_RUNTIME](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga88151dfd7f1aaeb43df745e88ef49241)。

运行时选择轴对（Axis Pair Selected at Runtime）。

<a id="define-members-8"></a>

### 幅值增益校正通道（Magnitude Gain Correction Channel）

设备树属性（Devicetree Property）`ch-mag-gain-correction` 的取值。

<a id="r_ga3d314538e20d924b9f5395b5d88be792"></a>

```c
#define TMAG5273_DT_CORRECTION_CH_1 0
```

相关声明：[TMAG5273_DT_CORRECTION_CH_1](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga3d314538e20d924b9f5395b5d88be792)。

对通道 1 应用增益校正（Gain Correction）。

<a id="r_ga2174de2be873e446dafa512f6c67d4e2"></a>

```c
#define TMAG5273_DT_CORRECTION_CH_2 1
```

相关声明：[TMAG5273_DT_CORRECTION_CH_2](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga2174de2be873e446dafa512f6c67d4e2)。

对通道 2 应用增益校正（Gain Correction）。

<a id="define-members-9"></a>

### 样本平均（Sample Averaging）

设备树属性（Devicetree Property）`average-mode` 的取值。

<a id="r_ga13c1237e1040e5505e52525ab7c73a1a"></a>

```c
#define TMAG5273_DT_AVERAGING_NONE 0
```

相关声明：[TMAG5273_DT_AVERAGING_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga13c1237e1040e5505e52525ab7c73a1a)。

不取平均（No Averaging），使用 1 个样本。

<a id="r_gaed2549fe3a62ba565ec2e81eea214ec1"></a>

```c
#define TMAG5273_DT_AVERAGING_2X 1
```

相关声明：[TMAG5273_DT_AVERAGING_2X](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#gaed2549fe3a62ba565ec2e81eea214ec1)。

对 2 个样本取平均（Samples Averaged）。

<a id="r_ga4150c85cf8a5790fc3385899293aadce"></a>

```c
#define TMAG5273_DT_AVERAGING_4X 2
```

相关声明：[TMAG5273_DT_AVERAGING_4X](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga4150c85cf8a5790fc3385899293aadce)。

对 4 个样本取平均（Samples Averaged）。

<a id="r_ga4981e523e151b8a7d36839b6312dd1ef"></a>

```c
#define TMAG5273_DT_AVERAGING_8X 3
```

相关声明：[TMAG5273_DT_AVERAGING_8X](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga4981e523e151b8a7d36839b6312dd1ef)。

对 8 个样本取平均（Samples Averaged）。

<a id="r_ga2ec0413e64f5688429e28588c6194428"></a>

```c
#define TMAG5273_DT_AVERAGING_16X 4
```

相关声明：[TMAG5273_DT_AVERAGING_16X](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga2ec0413e64f5688429e28588c6194428)。

对 16 个样本取平均（Samples Averaged）。

<a id="r_ga965c7f2fc5ec1ccca97f666060fd24ef"></a>

```c
#define TMAG5273_DT_AVERAGING_32X 5
```

相关声明：[TMAG5273_DT_AVERAGING_32X](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga965c7f2fc5ec1ccca97f666060fd24ef)。

对 32 个样本取平均（Samples Averaged）。

<a id="define-members-10"></a>

### 转换间休眠时间（Sleep Time between Conversions）

待机模式（Standby Mode）下两次转换之间的休眠时间（Sleep Time）。

<a id="r_ga396ab63225a243e75eebb38d37b77b27"></a>

```c
#define TMAG5273_DT_SLEEPTIME_1MS 0
```

相关声明：[TMAG5273_DT_SLEEPTIME_1MS](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga396ab63225a243e75eebb38d37b77b27)。

1 ms（毫秒）。

<a id="r_gab88e09d09437f57ce31d1ab0f58a19cb"></a>

```c
#define TMAG5273_DT_SLEEPTIME_5MS 1
```

相关声明：[TMAG5273_DT_SLEEPTIME_5MS](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#gab88e09d09437f57ce31d1ab0f58a19cb)。

5 ms（毫秒）。

<a id="r_gaee41d1df9c33164ac47213b4e0079f8e"></a>

```c
#define TMAG5273_DT_SLEEPTIME_10MS 2
```

相关声明：[TMAG5273_DT_SLEEPTIME_10MS](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#gaee41d1df9c33164ac47213b4e0079f8e)。

10 ms

<a id="r_ga88cb7a5cdd0d52e31dae2c03b83b5874"></a>

```c
#define TMAG5273_DT_SLEEPTIME_15MS 3
```

相关声明：[TMAG5273_DT_SLEEPTIME_15MS](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga88cb7a5cdd0d52e31dae2c03b83b5874)。

15 ms

<a id="r_gac29e91afbd4636e495726e3252abcea7"></a>

```c
#define TMAG5273_DT_SLEEPTIME_20MS 4
```

相关声明：[TMAG5273_DT_SLEEPTIME_20MS](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#gac29e91afbd4636e495726e3252abcea7)。

20 ms

<a id="r_gaad1cc10df9f35d2bb63cb4a3f021152f"></a>

```c
#define TMAG5273_DT_SLEEPTIME_30MS 5
```

相关声明：[TMAG5273_DT_SLEEPTIME_30MS](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#gaad1cc10df9f35d2bb63cb4a3f021152f)。

30 ms

<a id="r_ga03c1e099cd98b1b09a121bd5c353fc97"></a>

```c
#define TMAG5273_DT_SLEEPTIME_50MS 6
```

相关声明：[TMAG5273_DT_SLEEPTIME_50MS](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga03c1e099cd98b1b09a121bd5c353fc97)。

50 毫秒（ms）。

<a id="r_ga08371bf90c5ffe3ccd3634078c037779"></a>

```c
#define TMAG5273_DT_SLEEPTIME_100MS 7
```

相关声明：[TMAG5273_DT_SLEEPTIME_100MS](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga08371bf90c5ffe3ccd3634078c037779)。

100 毫秒（ms）。

<a id="r_gabc58f37d75364d3f8c7c03ee774ed091"></a>

```c
#define TMAG5273_DT_SLEEPTIME_500MS 8
```

相关声明：[TMAG5273_DT_SLEEPTIME_500MS](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#gabc58f37d75364d3f8c7c03ee774ed091)。

时间：500 ms。

<a id="r_ga7f011c43133f25c7653fa41aae041095"></a>

```c
#define TMAG5273_DT_SLEEPTIME_1000MS 9
```

相关声明：[TMAG5273_DT_SLEEPTIME_1000MS](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga7f011c43133f25c7653fa41aae041095)。

时间：1000 ms。

<a id="r_ga947cb9dc7689e460f1ddbd8bd94bc15b"></a>

```c
#define TMAG5273_DT_SLEEPTIME_2000MS 10
```

相关声明：[TMAG5273_DT_SLEEPTIME_2000MS](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga947cb9dc7689e460f1ddbd8bd94bc15b)。

时间：2000 ms。

<a id="r_gafddb082d0306a7858086c4ac227852e0"></a>

```c
#define TMAG5273_DT_SLEEPTIME_5000MS 11
```

相关声明：[TMAG5273_DT_SLEEPTIME_5000MS](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#gafddb082d0306a7858086c4ac227852e0)。

5000 ms

<a id="r_ga69e543ed3e6df3c2b6df67618b546de3"></a>

```c
#define TMAG5273_DT_SLEEPTIME_20000MS 12
```

相关声明：[TMAG5273_DT_SLEEPTIME_20000MS](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga69e543ed3e6df3c2b6df67618b546de3)。

20000 ms


## 7.2\_原页交叉引用（Cross References）

- [zephyr/dt-bindings/dt-util.h](../dt_bus_binding_reference/P006_设备树绑定工具头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P212_tmag5273.h_源码浏览.md)
- [TMAG5273_DT_OPER_MODE_CONTINUOUS](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga7c4ac425f1167fca06025db9a2b92153)
- [TMAG5273_DT_OPER_MODE_STANDBY](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga13fea164a14fc3a2d38aebce67e38e12)
- [TMAG5273_DT_AXIS_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga258a2507f733c059f2b5b212d505ccd8)
- [TMAG5273_DT_AXIS_X](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga3040ac9025679745dbfe52463f95bd9f)
- [TMAG5273_DT_AXIS_Y](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga0d352bd659851f02169036f205e8b012)
- [TMAG5273_DT_AXIS_Z](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga10d89d64876dc4d32398e2765ef5079f)
- [TMAG5273_DT_AXIS_XY](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga08aacefba8f390ac1ace72e672de83cc)
- [TMAG5273_DT_AXIS_XZ](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga53b02b4b3cf5126abd4ab939c74fc633)
- [TMAG5273_DT_AXIS_YZ](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga1ee1d7f126feb9b5652670e53d24f0b6)
- [TMAG5273_DT_AXIS_XYZ](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#gae16a8c01eafc1196d8fe0ffcf4976c72)
- [TMAG5273_DT_AXIS_XYX](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga6dcc34a5877ff11329c570f27184bbe7)
- [TMAG5273_DT_AXIS_YXY](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga000a0c930e0cdad6e7e91dc887004e4f)
- [TMAG5273_DT_AXIS_YZY](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#gad778956fdac899196bc7782e2306d18d)
- [TMAG5273_DT_AXIS_XZX](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga6e1e7c54e34d9f82abe8c8f4e38826ed)
- [TMAG5273_DT_AXIS_RANGE_LOW](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#gad536884f65cfb8d90f35c15b26afec04)
- [TMAG5273_DT_AXIS_RANGE_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga6b279486342219e7dfd5555c34cc7d37)
- [TMAG5273_DT_AXIS_RANGE_RUNTIME](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga2aa9dfa7a74f61a821d2d7f0c2629b55)
- [TMAG5273_DT_INT_THROUGH_INT](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#gac7a80f12307ebb946ab106381704f2bc)
- [TMAG5273_DT_INT_THROUGH_INT_EXC_I2C](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga97a154a99cf41aaadfbcb4fbaaa0fbdc)
- [TMAG5273_DT_INT_THROUGH_SCL](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga47ffb1ce227b6fc8cccda39898dabb96)
- [TMAG5273_DT_INT_THROUGH_SCL_EXC_I2C](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga5757c3a1364e72c3d4c0b30b5cfc0698)
- [TMAG5273_DT_THRX_COUNT_1](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga71b6e856b5a5db7af4e4ed0001de2f66)
- [TMAG5273_DT_THRX_COUNT_4](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga3940888f116795a9d060195fdb717ff1)
- [TMAG5273_DT_THRX_ABOVE](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#gab59755856b8372698deab44d9b8ec9a2)
- [TMAG5273_DT_THRX_BELOW](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga348bd07ca130ff996bea612ad8cecba3)
- [TMAG5273_DT_THRX_OUTSIDE](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga630c77a70f3db408a139dd10b3a28bb1)
- [TMAG5273_DT_THRX_INSIDE](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#gac0b966cb05b35abe701b8af474fd0498)
- [TMAG5273_DT_TEMP_COEFF_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga19f4de1abe7275ec75641e5e5ce47826)
- [TMAG5273_DT_TEMP_COEFF_NDBFE](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#gaf51ec112fe16a5c8a5a55a42dd14fd92)
- [TMAG5273_DT_TEMP_COEFF_CERAMIC](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#gaec27747fbae8c0c62912431a3f9d2309)
- [TMAG5273_DT_ANGLE_MAG_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga7ba462d2a09ae0118a991c655fdca672)
- [TMAG5273_DT_ANGLE_MAG_XY](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#gad34b392bf32680634ec9dddacee24c9b)
- [TMAG5273_DT_ANGLE_MAG_YZ](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#gaa48cfafa9b65e23e5f5915fc32f65633)
- [TMAG5273_DT_ANGLE_MAG_XZ](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga074869eda0ffdc0a88138b8b3caaafec)
- [TMAG5273_DT_ANGLE_MAG_RUNTIME](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga88151dfd7f1aaeb43df745e88ef49241)
- [TMAG5273_DT_CORRECTION_CH_1](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga3d314538e20d924b9f5395b5d88be792)
- [TMAG5273_DT_CORRECTION_CH_2](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga2174de2be873e446dafa512f6c67d4e2)
- [TMAG5273_DT_AVERAGING_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga13c1237e1040e5505e52525ab7c73a1a)
- [TMAG5273_DT_AVERAGING_2X](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#gaed2549fe3a62ba565ec2e81eea214ec1)
- [TMAG5273_DT_AVERAGING_4X](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga4150c85cf8a5790fc3385899293aadce)
- [TMAG5273_DT_AVERAGING_8X](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga4981e523e151b8a7d36839b6312dd1ef)
- [TMAG5273_DT_AVERAGING_16X](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga2ec0413e64f5688429e28588c6194428)
- [TMAG5273_DT_AVERAGING_32X](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga965c7f2fc5ec1ccca97f666060fd24ef)
- [TMAG5273_DT_SLEEPTIME_1MS](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga396ab63225a243e75eebb38d37b77b27)
- [TMAG5273_DT_SLEEPTIME_5MS](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#gab88e09d09437f57ce31d1ab0f58a19cb)
- [TMAG5273_DT_SLEEPTIME_10MS](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#gaee41d1df9c33164ac47213b4e0079f8e)
- [TMAG5273_DT_SLEEPTIME_15MS](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga88cb7a5cdd0d52e31dae2c03b83b5874)
- [TMAG5273_DT_SLEEPTIME_20MS](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#gac29e91afbd4636e495726e3252abcea7)
- [TMAG5273_DT_SLEEPTIME_30MS](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#gaad1cc10df9f35d2bb63cb4a3f021152f)
- [TMAG5273_DT_SLEEPTIME_50MS](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga03c1e099cd98b1b09a121bd5c353fc97)
- [TMAG5273_DT_SLEEPTIME_100MS](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga08371bf90c5ffe3ccd3634078c037779)
- [TMAG5273_DT_SLEEPTIME_500MS](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#gabc58f37d75364d3f8c7c03ee774ed091)
- [TMAG5273_DT_SLEEPTIME_1000MS](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga7f011c43133f25c7653fa41aae041095)
- [TMAG5273_DT_SLEEPTIME_2000MS](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga947cb9dc7689e460f1ddbd8bd94bc15b)
- [TMAG5273_DT_SLEEPTIME_5000MS](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#gafddb082d0306a7858086c4ac227852e0)
- [TMAG5273_DT_SLEEPTIME_20000MS](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html#ga69e543ed3e6df3c2b6df67618b546de3)

<a id="header-details"></a>

---

[上一章](P006_zephyr__bluetooth__direction.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P008_zephyr__net__ethernet.h_文件参考.md)
