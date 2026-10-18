---
id: learning.zephyr-docs.api-usb-gnss-topic-reference.page-13
title: TMAG5273 API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_TMAG5273 API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__tmag5273__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Texas Instruments TMAG5273 低功耗线性三维霍尔效应传感器（Low-Power Linear 3D Hall-Effect Sensor）。

<a id="details"></a>

Texas Instruments TMAG5273 低功耗线性三维霍尔效应传感器（Low-Power Linear 3D Hall-Effect Sensor）。`SENSOR_CHAN_MAGN_XYZ` 上的 `SENSOR_ATTR_FULL_SCALE` 与磁力计通道本身一样，以高斯（G）表示，例如 TMAG5273A1 上的 400 G 或 800 G。

<a id="header-files"></a>
<a id="files"></a>

## 13.1\_文件（Files）

<a id="r_tmag5273_2Eh"></a>

```c
file tmag5273.h
```

相关声明：[tmag5273.h](../api_file_usb_network_reference/P007_zephyr__dt-bindings__sensor__tmag5273.h_文件参考.md)。

the TI TMAG5273 3-axis Hall-effect sensor的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 13.2\_枚举（Enumerations）

<a id="r_ga3d91dbb6bc6d7dc90ed889651bc34827"></a>

```c
enum tmag5273_sensor_channel { TMAG5273_CHAN_MAGNITUDE = SENSOR_CHAN_PRIV_START , TMAG5273_CHAN_MAGNITUDE_MSB , TMAG5273_CHAN_ANGLE_MAGNITUDE }
```

相关声明：[tmag5273_sensor_channel](#ga3d91dbb6bc6d7dc90ed889651bc34827)、[TMAG5273_CHAN_MAGNITUDE](#gga3d91dbb6bc6d7dc90ed889651bc34827a72c52112337e191ab9ce906aecdff92d)、[TMAG5273_CHAN_MAGNITUDE_MSB](#gga3d91dbb6bc6d7dc90ed889651bc34827a601dad57092c442da3a0a184737d8003)、[TMAG5273_CHAN_ANGLE_MAGNITUDE](#gga3d91dbb6bc6d7dc90ed889651bc34827a2c4ff267102871c1d23353bbb6b30dbc)。

TMAG5273 支持的附加通道（additional channels）。

<a id="r_ga6fadcd6cd3b5fbc9281d27f37bdfe0a2"></a>

```c
enum tmag5273_attribute { TMAG5273_ATTR_ANGLE_MAG_AXIS = SENSOR_ATTR_PRIV_START }
```

相关声明：[tmag5273_attribute](#ga6fadcd6cd3b5fbc9281d27f37bdfe0a2)、[TMAG5273_ATTR_ANGLE_MAG_AXIS](#gga6fadcd6cd3b5fbc9281d27f37bdfe0a2af59c66f9794efa1afa7d7461a134d3d3)。

TMAG5273 支持的附加属性（additional attributes）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 13.3\_角度计算模式（Angle calculation modes）

<a id="r_ga6426061b7a7f444ba7f4d87477144bf0"></a>

```c
#define TMAG5273_ANGLE_CALC_NONE 0
```

相关声明：[TMAG5273_ANGLE_CALC_NONE](#ga6426061b7a7f444ba7f4d87477144bf0)。

不进行角度计算（angle calculation）。

<a id="r_gac93519e03635876d3b693a0b4a11904a"></a>

```c
#define TMAG5273_ANGLE_CALC_XY 1
```

相关声明：[TMAG5273_ANGLE_CALC_XY](#gac93519e03635876d3b693a0b4a11904a)。

先 X，后 Y。

<a id="r_ga863266f03d298268103d394eb37bbac9"></a>

```c
#define TMAG5273_ANGLE_CALC_YZ 2
```

相关声明：[TMAG5273_ANGLE_CALC_YZ](#ga863266f03d298268103d394eb37bbac9)。

先 Y，后 Z。

<a id="r_ga84e780517b8fec1845fd145dd0b16f0c"></a>

```c
#define TMAG5273_ANGLE_CALC_XZ 3
```

相关声明：[TMAG5273_ANGLE_CALC_XZ](#ga84e780517b8fec1845fd145dd0b16f0c)。

先 X，后 Z。

## 13.4\_工作模式（Operating mode）

设备树属性（Devicetree Property）`operation-mode` 的取值。

<a id="r_ga7c4ac425f1167fca06025db9a2b92153"></a>

```c
#define TMAG5273_DT_OPER_MODE_CONTINUOUS 0
```

相关声明：[TMAG5273_DT_OPER_MODE_CONTINUOUS](#ga7c4ac425f1167fca06025db9a2b92153)。

连续转换（Continuous Conversion）。

<a id="r_ga13fea164a14fc3a2d38aebce67e38e12"></a>

```c
#define TMAG5273_DT_OPER_MODE_STANDBY 1
```

相关声明：[TMAG5273_DT_OPER_MODE_STANDBY](#ga13fea164a14fc3a2d38aebce67e38e12)。

待机（Standby），按请求进行转换。

## 13.5\_磁场测量轴选择（Magnetic Axis Selection）

设备树属性（Devicetree Property）`axis` 的取值。

<a id="r_ga258a2507f733c059f2b5b212d505ccd8"></a>

```c
#define TMAG5273_DT_AXIS_NONE 0x0
```

相关声明：[TMAG5273_DT_AXIS_NONE](#ga258a2507f733c059f2b5b212d505ccd8)。

不选择任何轴（No Axis）。

<a id="r_ga3040ac9025679745dbfe52463f95bd9f"></a>

```c
#define TMAG5273_DT_AXIS_X 0x1
```

相关声明：[TMAG5273_DT_AXIS_X](#ga3040ac9025679745dbfe52463f95bd9f)。

X 轴（X axis）。

<a id="r_ga0d352bd659851f02169036f205e8b012"></a>

```c
#define TMAG5273_DT_AXIS_Y 0x2
```

相关声明：[TMAG5273_DT_AXIS_Y](#ga0d352bd659851f02169036f205e8b012)。

Y 轴（Y axis）。

<a id="r_ga10d89d64876dc4d32398e2765ef5079f"></a>

```c
#define TMAG5273_DT_AXIS_Z 0x4
```

相关声明：[TMAG5273_DT_AXIS_Z](#ga10d89d64876dc4d32398e2765ef5079f)。

Z 轴（Z axis）。

<a id="r_ga08aacefba8f390ac1ace72e672de83cc"></a>

```c
#define TMAG5273_DT_AXIS_XY (TMAG5273_DT_AXIS_X | TMAG5273_DT_AXIS_Y)
```

相关声明：[TMAG5273_DT_AXIS_XY](#ga08aacefba8f390ac1ace72e672de83cc)、[TMAG5273_DT_AXIS_X](#ga3040ac9025679745dbfe52463f95bd9f)、[TMAG5273_DT_AXIS_Y](#ga0d352bd659851f02169036f205e8b012)。

X 轴和 Y 轴（Axes）。

<a id="r_ga53b02b4b3cf5126abd4ab939c74fc633"></a>

```c
#define TMAG5273_DT_AXIS_XZ (TMAG5273_DT_AXIS_X | TMAG5273_DT_AXIS_Z)
```

相关声明：[TMAG5273_DT_AXIS_XZ](#ga53b02b4b3cf5126abd4ab939c74fc633)、[TMAG5273_DT_AXIS_X](#ga3040ac9025679745dbfe52463f95bd9f)、[TMAG5273_DT_AXIS_Z](#ga10d89d64876dc4d32398e2765ef5079f)。

X 轴和 Z 轴（Axes）。

<a id="r_ga1ee1d7f126feb9b5652670e53d24f0b6"></a>

```c
#define TMAG5273_DT_AXIS_YZ (TMAG5273_DT_AXIS_Y | TMAG5273_DT_AXIS_Z)
```

相关声明：[TMAG5273_DT_AXIS_YZ](#ga1ee1d7f126feb9b5652670e53d24f0b6)、[TMAG5273_DT_AXIS_Y](#ga0d352bd659851f02169036f205e8b012)、[TMAG5273_DT_AXIS_Z](#ga10d89d64876dc4d32398e2765ef5079f)。

Y 轴和 Z 轴（Axes）。

<a id="r_gae16a8c01eafc1196d8fe0ffcf4976c72"></a>

```c
#define TMAG5273_DT_AXIS_XYZ (TMAG5273_DT_AXIS_X | TMAG5273_DT_AXIS_Y | TMAG5273_DT_AXIS_Z)
```

相关声明：[TMAG5273_DT_AXIS_XYZ](#gae16a8c01eafc1196d8fe0ffcf4976c72)、[TMAG5273_DT_AXIS_X](#ga3040ac9025679745dbfe52463f95bd9f)、[TMAG5273_DT_AXIS_Y](#ga0d352bd659851f02169036f205e8b012)、[TMAG5273_DT_AXIS_Z](#ga10d89d64876dc4d32398e2765ef5079f)。

全部轴（All Axes）。

<a id="r_ga6dcc34a5877ff11329c570f27184bbe7"></a>

```c
#define TMAG5273_DT_AXIS_XYX 0x8
```

相关声明：[TMAG5273_DT_AXIS_XYX](#ga6dcc34a5877ff11329c570f27184bbe7)。

依次为 X 轴、Y 轴、X 轴（Axes）。

<a id="r_ga000a0c930e0cdad6e7e91dc887004e4f"></a>

```c
#define TMAG5273_DT_AXIS_YXY 0x9
```

相关声明：[TMAG5273_DT_AXIS_YXY](#ga000a0c930e0cdad6e7e91dc887004e4f)。

依次为 Y 轴、X 轴、Y 轴（Axes）。

<a id="r_gad778956fdac899196bc7782e2306d18d"></a>

```c
#define TMAG5273_DT_AXIS_YZY 0xA
```

相关声明：[TMAG5273_DT_AXIS_YZY](#gad778956fdac899196bc7782e2306d18d)。

依次为 Y 轴、Z 轴、Y 轴（Axes）。

<a id="r_ga6e1e7c54e34d9f82abe8c8f4e38826ed"></a>

```c
#define TMAG5273_DT_AXIS_XZX 0xB
```

相关声明：[TMAG5273_DT_AXIS_XZX](#ga6e1e7c54e34d9f82abe8c8f4e38826ed)。

依次为 X 轴、Z 轴、X 轴（Axes）。

## 13.6\_磁场测量量程（Magnetic Measurement Range）

设备树 `range` 属性的取值。

<a id="r_gad536884f65cfb8d90f35c15b26afec04"></a>

```c
#define TMAG5273_DT_AXIS_RANGE_LOW 0
```

相关声明：[TMAG5273_DT_AXIS_RANGE_LOW](#gad536884f65cfb8d90f35c15b26afec04)。

低量程（Low Range）。

<a id="r_ga6b279486342219e7dfd5555c34cc7d37"></a>

```c
#define TMAG5273_DT_AXIS_RANGE_HIGH 1
```

相关声明：[TMAG5273_DT_AXIS_RANGE_HIGH](#ga6b279486342219e7dfd5555c34cc7d37)。

高量程（High Range）。

<a id="r_ga2aa9dfa7a74f61a821d2d7f0c2629b55"></a>

```c
#define TMAG5273_DT_AXIS_RANGE_RUNTIME 2
```

相关声明：[TMAG5273_DT_AXIS_RANGE_RUNTIME](#ga2aa9dfa7a74f61a821d2d7f0c2629b55)。

运行时选择量程（Range Selected at Runtime）。

## 13.7\_中断路由模式（Interrupt Routing Mode）

中断路由模式（Interrupt Routing Mode）。

<a id="r_gac7a80f12307ebb946ab106381704f2bc"></a>

```c
#define TMAG5273_DT_INT_THROUGH_INT 0
```

相关声明：[TMAG5273_DT_INT_THROUGH_INT](#gac7a80f12307ebb946ab106381704f2bc)。

通过 INT 引脚产生中断（Interrupt）。

<a id="r_ga97a154a99cf41aaadfbcb4fbaaa0fbdc"></a>

```c
#define TMAG5273_DT_INT_THROUGH_INT_EXC_I2C 1
```

相关声明：[TMAG5273_DT_INT_THROUGH_INT_EXC_I2C](#ga97a154a99cf41aaadfbcb4fbaaa0fbdc)。

使用 INT 引脚，但 I2C 总线访问期间除外。

<a id="r_ga47ffb1ce227b6fc8cccda39898dabb96"></a>

```c
#define TMAG5273_DT_INT_THROUGH_SCL 2
```

相关声明：[TMAG5273_DT_INT_THROUGH_SCL](#ga47ffb1ce227b6fc8cccda39898dabb96)。

通过 SCL 引脚产生中断（Interrupt）。

<a id="r_ga5757c3a1364e72c3d4c0b30b5cfc0698"></a>

```c
#define TMAG5273_DT_INT_THROUGH_SCL_EXC_I2C 3
```

相关声明：[TMAG5273_DT_INT_THROUGH_SCL_EXC_I2C](#ga5757c3a1364e72c3d4c0b30b5cfc0698)。

使用 SCL 引脚，但 I2C 总线访问期间除外。

## 13.8\_阈值越过次数（Threshold Crossing Count）

触发中断前越过阈值的次数（Number of Threshold Crossings）。

<a id="r_ga71b6e856b5a5db7af4e4ed0001de2f66"></a>

```c
#define TMAG5273_DT_THRX_COUNT_1 0
```

相关声明：[TMAG5273_DT_THRX_COUNT_1](#ga71b6e856b5a5db7af4e4ed0001de2f66)。

越过阈值 1 次后触发（Trigger after 1 Crossing）。

<a id="r_ga3940888f116795a9d060195fdb717ff1"></a>

```c
#define TMAG5273_DT_THRX_COUNT_4 1
```

相关声明：[TMAG5273_DT_THRX_COUNT_4](#ga3940888f116795a9d060195fdb717ff1)。

越过阈值 4 次后触发（Trigger after 4 Crossings）。

## 13.9\_阈值越过方向（Threshold Crossing Direction）

触发中断的阈值越过方向（Threshold-crossing Direction）。

<a id="r_gab59755856b8372698deab44d9b8ec9a2"></a>

```c
#define TMAG5273_DT_THRX_ABOVE 0
```

相关声明：[TMAG5273_DT_THRX_ABOVE](#gab59755856b8372698deab44d9b8ec9a2)。

磁场强度上升至阈值（Threshold）以上。

<a id="r_ga348bd07ca130ff996bea612ad8cecba3"></a>

```c
#define TMAG5273_DT_THRX_BELOW 1
```

相关声明：[TMAG5273_DT_THRX_BELOW](#ga348bd07ca130ff996bea612ad8cecba3)。

磁场强度下降至阈值（Threshold）以下。

<a id="r_ga630c77a70f3db408a139dd10b3a28bb1"></a>

```c
#define TMAG5273_DT_THRX_OUTSIDE 2
```

相关声明：[TMAG5273_DT_THRX_OUTSIDE](#ga630c77a70f3db408a139dd10b3a28bb1)。

磁场强度离开阈值窗口（Threshold Window）。

<a id="r_gac0b966cb05b35abe701b8af474fd0498"></a>

```c
#define TMAG5273_DT_THRX_INSIDE 3
```

相关声明：[TMAG5273_DT_THRX_INSIDE](#gac0b966cb05b35abe701b8af474fd0498)。

磁场强度进入阈值窗口（Threshold Window）。

## 13.10\_磁体温度系数（Magnet Temperature Coefficient）

设备树属性（Devicetree Property）`temperature-coefficient` 的取值。

<a id="r_ga19f4de1abe7275ec75641e5e5ce47826"></a>

```c
#define TMAG5273_DT_TEMP_COEFF_NONE 0
```

相关声明：[TMAG5273_DT_TEMP_COEFF_NONE](#ga19f4de1abe7275ec75641e5e5ce47826)。

不进行补偿（No Compensation）。

<a id="r_gaf51ec112fe16a5c8a5a55a42dd14fd92"></a>

```c
#define TMAG5273_DT_TEMP_COEFF_NDBFE 1
```

相关声明：[TMAG5273_DT_TEMP_COEFF_NDBFE](#gaf51ec112fe16a5c8a5a55a42dd14fd92)。

钕铁硼磁体（原文为 NdBFe Magnet），温度系数为 0.12 %/°C。

<a id="r_gaec27747fbae8c0c62912431a3f9d2309"></a>

```c
#define TMAG5273_DT_TEMP_COEFF_CERAMIC 2
```

相关声明：[TMAG5273_DT_TEMP_COEFF_CERAMIC](#gaec27747fbae8c0c62912431a3f9d2309)。

陶瓷磁体（Ceramic Magnet），温度系数为 0.2 %/°C。

## 13.11\_角度与幅值计算（Angle and Magnitude Calculation）

设备树属性（Devicetree Property）`angle-magnitude-axis` 的取值。

<a id="r_ga7ba462d2a09ae0118a991c655fdca672"></a>

```c
#define TMAG5273_DT_ANGLE_MAG_NONE 0
```

相关声明：[TMAG5273_DT_ANGLE_MAG_NONE](#ga7ba462d2a09ae0118a991c655fdca672)。

禁用（Disabled）。

<a id="r_gad34b392bf32680634ec9dddacee24c9b"></a>

```c
#define TMAG5273_DT_ANGLE_MAG_XY 1
```

相关声明：[TMAG5273_DT_ANGLE_MAG_XY](#gad34b392bf32680634ec9dddacee24c9b)。

来自 X 轴和 Y 轴（Axes）。

<a id="r_gaa48cfafa9b65e23e5f5915fc32f65633"></a>

```c
#define TMAG5273_DT_ANGLE_MAG_YZ 2
```

相关声明：[TMAG5273_DT_ANGLE_MAG_YZ](#gaa48cfafa9b65e23e5f5915fc32f65633)。

来自 Y 轴和 Z 轴（Axes）。

<a id="r_ga074869eda0ffdc0a88138b8b3caaafec"></a>

```c
#define TMAG5273_DT_ANGLE_MAG_XZ 3
```

相关声明：[TMAG5273_DT_ANGLE_MAG_XZ](#ga074869eda0ffdc0a88138b8b3caaafec)。

来自 X 轴和 Z 轴（Axes）。

<a id="r_ga88151dfd7f1aaeb43df745e88ef49241"></a>

```c
#define TMAG5273_DT_ANGLE_MAG_RUNTIME 4
```

相关声明：[TMAG5273_DT_ANGLE_MAG_RUNTIME](#ga88151dfd7f1aaeb43df745e88ef49241)。

运行时选择轴对（Axis Pair Selected at Runtime）。

## 13.12\_幅值增益校正通道（Magnitude Gain Correction Channel）

设备树属性（Devicetree Property）`ch-mag-gain-correction` 的取值。

<a id="r_ga3d314538e20d924b9f5395b5d88be792"></a>

```c
#define TMAG5273_DT_CORRECTION_CH_1 0
```

相关声明：[TMAG5273_DT_CORRECTION_CH_1](#ga3d314538e20d924b9f5395b5d88be792)。

对通道 1 应用增益校正（Gain Correction）。

<a id="r_ga2174de2be873e446dafa512f6c67d4e2"></a>

```c
#define TMAG5273_DT_CORRECTION_CH_2 1
```

相关声明：[TMAG5273_DT_CORRECTION_CH_2](#ga2174de2be873e446dafa512f6c67d4e2)。

对通道 2 应用增益校正（Gain Correction）。

## 13.13\_样本平均（Sample Averaging）

设备树属性（Devicetree Property）`average-mode` 的取值。

<a id="r_ga13c1237e1040e5505e52525ab7c73a1a"></a>

```c
#define TMAG5273_DT_AVERAGING_NONE 0
```

相关声明：[TMAG5273_DT_AVERAGING_NONE](#ga13c1237e1040e5505e52525ab7c73a1a)。

不取平均（No Averaging），使用 1 个样本。

<a id="r_gaed2549fe3a62ba565ec2e81eea214ec1"></a>

```c
#define TMAG5273_DT_AVERAGING_2X 1
```

相关声明：[TMAG5273_DT_AVERAGING_2X](#gaed2549fe3a62ba565ec2e81eea214ec1)。

对 2 个样本取平均（Samples Averaged）。

<a id="r_ga4150c85cf8a5790fc3385899293aadce"></a>

```c
#define TMAG5273_DT_AVERAGING_4X 2
```

相关声明：[TMAG5273_DT_AVERAGING_4X](#ga4150c85cf8a5790fc3385899293aadce)。

对 4 个样本取平均（Samples Averaged）。

<a id="r_ga4981e523e151b8a7d36839b6312dd1ef"></a>

```c
#define TMAG5273_DT_AVERAGING_8X 3
```

相关声明：[TMAG5273_DT_AVERAGING_8X](#ga4981e523e151b8a7d36839b6312dd1ef)。

对 8 个样本取平均（Samples Averaged）。

<a id="r_ga2ec0413e64f5688429e28588c6194428"></a>

```c
#define TMAG5273_DT_AVERAGING_16X 4
```

相关声明：[TMAG5273_DT_AVERAGING_16X](#ga2ec0413e64f5688429e28588c6194428)。

对 16 个样本取平均（Samples Averaged）。

<a id="r_ga965c7f2fc5ec1ccca97f666060fd24ef"></a>

```c
#define TMAG5273_DT_AVERAGING_32X 5
```

相关声明：[TMAG5273_DT_AVERAGING_32X](#ga965c7f2fc5ec1ccca97f666060fd24ef)。

对 32 个样本取平均（Samples Averaged）。

## 13.14\_转换间休眠时间（Sleep Time between Conversions）

待机模式（Standby Mode）下两次转换之间的休眠时间（Sleep Time）。

<a id="r_ga396ab63225a243e75eebb38d37b77b27"></a>

```c
#define TMAG5273_DT_SLEEPTIME_1MS 0
```

相关声明：[TMAG5273_DT_SLEEPTIME_1MS](#ga396ab63225a243e75eebb38d37b77b27)。

1 ms（毫秒）。

<a id="r_gab88e09d09437f57ce31d1ab0f58a19cb"></a>

```c
#define TMAG5273_DT_SLEEPTIME_5MS 1
```

相关声明：[TMAG5273_DT_SLEEPTIME_5MS](#gab88e09d09437f57ce31d1ab0f58a19cb)。

5 ms（毫秒）。

<a id="r_gaee41d1df9c33164ac47213b4e0079f8e"></a>

```c
#define TMAG5273_DT_SLEEPTIME_10MS 2
```

相关声明：[TMAG5273_DT_SLEEPTIME_10MS](#gaee41d1df9c33164ac47213b4e0079f8e)。

10 ms

<a id="r_ga88cb7a5cdd0d52e31dae2c03b83b5874"></a>

```c
#define TMAG5273_DT_SLEEPTIME_15MS 3
```

相关声明：[TMAG5273_DT_SLEEPTIME_15MS](#ga88cb7a5cdd0d52e31dae2c03b83b5874)。

15 ms

<a id="r_gac29e91afbd4636e495726e3252abcea7"></a>

```c
#define TMAG5273_DT_SLEEPTIME_20MS 4
```

相关声明：[TMAG5273_DT_SLEEPTIME_20MS](#gac29e91afbd4636e495726e3252abcea7)。

20 ms

<a id="r_gaad1cc10df9f35d2bb63cb4a3f021152f"></a>

```c
#define TMAG5273_DT_SLEEPTIME_30MS 5
```

相关声明：[TMAG5273_DT_SLEEPTIME_30MS](#gaad1cc10df9f35d2bb63cb4a3f021152f)。

30 ms

<a id="r_ga03c1e099cd98b1b09a121bd5c353fc97"></a>

```c
#define TMAG5273_DT_SLEEPTIME_50MS 6
```

相关声明：[TMAG5273_DT_SLEEPTIME_50MS](#ga03c1e099cd98b1b09a121bd5c353fc97)。

50 毫秒（ms）。

<a id="r_ga08371bf90c5ffe3ccd3634078c037779"></a>

```c
#define TMAG5273_DT_SLEEPTIME_100MS 7
```

相关声明：[TMAG5273_DT_SLEEPTIME_100MS](#ga08371bf90c5ffe3ccd3634078c037779)。

100 毫秒（ms）。

<a id="r_gabc58f37d75364d3f8c7c03ee774ed091"></a>

```c
#define TMAG5273_DT_SLEEPTIME_500MS 8
```

相关声明：[TMAG5273_DT_SLEEPTIME_500MS](#gabc58f37d75364d3f8c7c03ee774ed091)。

时间：500 ms。

<a id="r_ga7f011c43133f25c7653fa41aae041095"></a>

```c
#define TMAG5273_DT_SLEEPTIME_1000MS 9
```

相关声明：[TMAG5273_DT_SLEEPTIME_1000MS](#ga7f011c43133f25c7653fa41aae041095)。

时间：1000 ms。

<a id="r_ga947cb9dc7689e460f1ddbd8bd94bc15b"></a>

```c
#define TMAG5273_DT_SLEEPTIME_2000MS 10
```

相关声明：[TMAG5273_DT_SLEEPTIME_2000MS](#ga947cb9dc7689e460f1ddbd8bd94bc15b)。

时间：2000 ms。

<a id="r_gafddb082d0306a7858086c4ac227852e0"></a>

```c
#define TMAG5273_DT_SLEEPTIME_5000MS 11
```

相关声明：[TMAG5273_DT_SLEEPTIME_5000MS](#gafddb082d0306a7858086c4ac227852e0)。

5000 ms

<a id="r_ga69e543ed3e6df3c2b6df67618b546de3"></a>

```c
#define TMAG5273_DT_SLEEPTIME_20000MS 12
```

相关声明：[TMAG5273_DT_SLEEPTIME_20000MS](#ga69e543ed3e6df3c2b6df67618b546de3)。

20000 ms

## 13.15\_详细说明（Detailed Documentation）

<a id="ga6426061b7a7f444ba7f4d87477144bf0"></a>

### `TMAG5273_ANGLE_CALC_NONE`

```c
#define TMAG5273_ANGLE_CALC_NONE 0
```

```c
#include <zephyr/drivers/sensor/tmag5273.h>
```

不进行角度计算（angle calculation）。

<a id="gac93519e03635876d3b693a0b4a11904a"></a>

### `TMAG5273_ANGLE_CALC_XY`

```c
#define TMAG5273_ANGLE_CALC_XY 1
```

```c
#include <zephyr/drivers/sensor/tmag5273.h>
```

先 X，后 Y。

<a id="ga84e780517b8fec1845fd145dd0b16f0c"></a>

### `TMAG5273_ANGLE_CALC_XZ`

```c
#define TMAG5273_ANGLE_CALC_XZ 3
```

```c
#include <zephyr/drivers/sensor/tmag5273.h>
```

先 X，后 Z。

<a id="ga863266f03d298268103d394eb37bbac9"></a>

### `TMAG5273_ANGLE_CALC_YZ`

```c
#define TMAG5273_ANGLE_CALC_YZ 2
```

```c
#include <zephyr/drivers/sensor/tmag5273.h>
```

先 Y，后 Z。

<a id="ga7ba462d2a09ae0118a991c655fdca672"></a>

### `TMAG5273_DT_ANGLE_MAG_NONE`

```c
#define TMAG5273_DT_ANGLE_MAG_NONE 0
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

禁用（Disabled）。

<a id="ga88151dfd7f1aaeb43df745e88ef49241"></a>

### `TMAG5273_DT_ANGLE_MAG_RUNTIME`

```c
#define TMAG5273_DT_ANGLE_MAG_RUNTIME 4
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

运行时选择轴对（Axis Pair Selected at Runtime）。

<a id="gad34b392bf32680634ec9dddacee24c9b"></a>

### `TMAG5273_DT_ANGLE_MAG_XY`

```c
#define TMAG5273_DT_ANGLE_MAG_XY 1
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

来自 X 轴和 Y 轴（Axes）。

<a id="ga074869eda0ffdc0a88138b8b3caaafec"></a>

### `TMAG5273_DT_ANGLE_MAG_XZ`

```c
#define TMAG5273_DT_ANGLE_MAG_XZ 3
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

来自 X 轴和 Z 轴（Axes）。

<a id="gaa48cfafa9b65e23e5f5915fc32f65633"></a>

### `TMAG5273_DT_ANGLE_MAG_YZ`

```c
#define TMAG5273_DT_ANGLE_MAG_YZ 2
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

来自 Y 轴和 Z 轴（Axes）。

<a id="ga2ec0413e64f5688429e28588c6194428"></a>

### `TMAG5273_DT_AVERAGING_16X`

```c
#define TMAG5273_DT_AVERAGING_16X 4
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

对 16 个样本取平均（Samples Averaged）。

<a id="gaed2549fe3a62ba565ec2e81eea214ec1"></a>

### `TMAG5273_DT_AVERAGING_2X`

```c
#define TMAG5273_DT_AVERAGING_2X 1
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

对 2 个样本取平均（Samples Averaged）。

<a id="ga965c7f2fc5ec1ccca97f666060fd24ef"></a>

### `TMAG5273_DT_AVERAGING_32X`

```c
#define TMAG5273_DT_AVERAGING_32X 5
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

对 32 个样本取平均（Samples Averaged）。

<a id="ga4150c85cf8a5790fc3385899293aadce"></a>

### `TMAG5273_DT_AVERAGING_4X`

```c
#define TMAG5273_DT_AVERAGING_4X 2
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

对 4 个样本取平均（Samples Averaged）。

<a id="ga4981e523e151b8a7d36839b6312dd1ef"></a>

### `TMAG5273_DT_AVERAGING_8X`

```c
#define TMAG5273_DT_AVERAGING_8X 3
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

对 8 个样本取平均（Samples Averaged）。

<a id="ga13c1237e1040e5505e52525ab7c73a1a"></a>

### `TMAG5273_DT_AVERAGING_NONE`

```c
#define TMAG5273_DT_AVERAGING_NONE 0
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

不取平均（No Averaging），使用 1 个样本。

<a id="ga258a2507f733c059f2b5b212d505ccd8"></a>

### `TMAG5273_DT_AXIS_NONE`

```c
#define TMAG5273_DT_AXIS_NONE 0x0
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

不选择任何轴（No Axis）。

<a id="ga6b279486342219e7dfd5555c34cc7d37"></a>

### `TMAG5273_DT_AXIS_RANGE_HIGH`

```c
#define TMAG5273_DT_AXIS_RANGE_HIGH 1
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

高量程（High Range）。

<a id="gad536884f65cfb8d90f35c15b26afec04"></a>

### `TMAG5273_DT_AXIS_RANGE_LOW`

```c
#define TMAG5273_DT_AXIS_RANGE_LOW 0
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

低量程（Low Range）。

<a id="ga2aa9dfa7a74f61a821d2d7f0c2629b55"></a>

### `TMAG5273_DT_AXIS_RANGE_RUNTIME`

```c
#define TMAG5273_DT_AXIS_RANGE_RUNTIME 2
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

运行时选择量程（Range Selected at Runtime）。

<a id="ga3040ac9025679745dbfe52463f95bd9f"></a>

### `TMAG5273_DT_AXIS_X`

```c
#define TMAG5273_DT_AXIS_X 0x1
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

X 轴（X axis）。

<a id="ga08aacefba8f390ac1ace72e672de83cc"></a>

### `TMAG5273_DT_AXIS_XY`

```c
#define TMAG5273_DT_AXIS_XY (TMAG5273_DT_AXIS_X | TMAG5273_DT_AXIS_Y)
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

X 轴和 Y 轴（Axes）。

<a id="ga6dcc34a5877ff11329c570f27184bbe7"></a>

### `TMAG5273_DT_AXIS_XYX`

```c
#define TMAG5273_DT_AXIS_XYX 0x8
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

依次为 X 轴、Y 轴、X 轴（Axes）。

<a id="gae16a8c01eafc1196d8fe0ffcf4976c72"></a>

### `TMAG5273_DT_AXIS_XYZ`

```c
#define TMAG5273_DT_AXIS_XYZ (TMAG5273_DT_AXIS_X | TMAG5273_DT_AXIS_Y | TMAG5273_DT_AXIS_Z)
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

全部轴（All Axes）。

<a id="ga53b02b4b3cf5126abd4ab939c74fc633"></a>

### `TMAG5273_DT_AXIS_XZ`

```c
#define TMAG5273_DT_AXIS_XZ (TMAG5273_DT_AXIS_X | TMAG5273_DT_AXIS_Z)
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

X 轴和 Z 轴（Axes）。

<a id="ga6e1e7c54e34d9f82abe8c8f4e38826ed"></a>

### `TMAG5273_DT_AXIS_XZX`

```c
#define TMAG5273_DT_AXIS_XZX 0xB
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

依次为 X 轴、Z 轴、X 轴（Axes）。

<a id="ga0d352bd659851f02169036f205e8b012"></a>

### `TMAG5273_DT_AXIS_Y`

```c
#define TMAG5273_DT_AXIS_Y 0x2
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

Y 轴（Y axis）。

<a id="ga000a0c930e0cdad6e7e91dc887004e4f"></a>

### `TMAG5273_DT_AXIS_YXY`

```c
#define TMAG5273_DT_AXIS_YXY 0x9
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

依次为 Y 轴、X 轴、Y 轴（Axes）。

<a id="ga1ee1d7f126feb9b5652670e53d24f0b6"></a>

### `TMAG5273_DT_AXIS_YZ`

```c
#define TMAG5273_DT_AXIS_YZ (TMAG5273_DT_AXIS_Y | TMAG5273_DT_AXIS_Z)
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

Y 轴和 Z 轴（Axes）。

<a id="gad778956fdac899196bc7782e2306d18d"></a>

### `TMAG5273_DT_AXIS_YZY`

```c
#define TMAG5273_DT_AXIS_YZY 0xA
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

依次为 Y 轴、Z 轴、Y 轴（Axes）。

<a id="ga10d89d64876dc4d32398e2765ef5079f"></a>

### `TMAG5273_DT_AXIS_Z`

```c
#define TMAG5273_DT_AXIS_Z 0x4
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

Z 轴（Z axis）。

<a id="ga3d314538e20d924b9f5395b5d88be792"></a>

### `TMAG5273_DT_CORRECTION_CH_1`

```c
#define TMAG5273_DT_CORRECTION_CH_1 0
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

对通道 1 应用增益校正（Gain Correction）。

<a id="ga2174de2be873e446dafa512f6c67d4e2"></a>

### `TMAG5273_DT_CORRECTION_CH_2`

```c
#define TMAG5273_DT_CORRECTION_CH_2 1
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

对通道 2 应用增益校正（Gain Correction）。

<a id="gac7a80f12307ebb946ab106381704f2bc"></a>

### `TMAG5273_DT_INT_THROUGH_INT`

```c
#define TMAG5273_DT_INT_THROUGH_INT 0
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

通过 INT 引脚产生中断（Interrupt）。

<a id="ga97a154a99cf41aaadfbcb4fbaaa0fbdc"></a>

### `TMAG5273_DT_INT_THROUGH_INT_EXC_I2C`

```c
#define TMAG5273_DT_INT_THROUGH_INT_EXC_I2C 1
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

使用 INT 引脚，但 I2C 总线访问期间除外。

<a id="ga47ffb1ce227b6fc8cccda39898dabb96"></a>

### `TMAG5273_DT_INT_THROUGH_SCL`

```c
#define TMAG5273_DT_INT_THROUGH_SCL 2
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

通过 SCL 引脚产生中断（Interrupt）。

<a id="ga5757c3a1364e72c3d4c0b30b5cfc0698"></a>

### `TMAG5273_DT_INT_THROUGH_SCL_EXC_I2C`

```c
#define TMAG5273_DT_INT_THROUGH_SCL_EXC_I2C 3
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

使用 SCL 引脚，但 I2C 总线访问期间除外。

<a id="ga7c4ac425f1167fca06025db9a2b92153"></a>

### `TMAG5273_DT_OPER_MODE_CONTINUOUS`

```c
#define TMAG5273_DT_OPER_MODE_CONTINUOUS 0
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

连续转换（Continuous Conversion）。

<a id="ga13fea164a14fc3a2d38aebce67e38e12"></a>

### `TMAG5273_DT_OPER_MODE_STANDBY`

```c
#define TMAG5273_DT_OPER_MODE_STANDBY 1
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

待机（Standby），按请求进行转换。

<a id="ga7f011c43133f25c7653fa41aae041095"></a>

### `TMAG5273_DT_SLEEPTIME_1000MS`

```c
#define TMAG5273_DT_SLEEPTIME_1000MS 9
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

时间：1000 ms。

<a id="ga08371bf90c5ffe3ccd3634078c037779"></a>

### `TMAG5273_DT_SLEEPTIME_100MS`

```c
#define TMAG5273_DT_SLEEPTIME_100MS 7
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

100 毫秒（ms）。

<a id="gaee41d1df9c33164ac47213b4e0079f8e"></a>

### `TMAG5273_DT_SLEEPTIME_10MS`

```c
#define TMAG5273_DT_SLEEPTIME_10MS 2
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

10 ms

<a id="ga88cb7a5cdd0d52e31dae2c03b83b5874"></a>

### `TMAG5273_DT_SLEEPTIME_15MS`

```c
#define TMAG5273_DT_SLEEPTIME_15MS 3
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

15 ms

<a id="ga396ab63225a243e75eebb38d37b77b27"></a>

### `TMAG5273_DT_SLEEPTIME_1MS`

```c
#define TMAG5273_DT_SLEEPTIME_1MS 0
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

1 ms（毫秒）。

<a id="ga69e543ed3e6df3c2b6df67618b546de3"></a>

### `TMAG5273_DT_SLEEPTIME_20000MS`

```c
#define TMAG5273_DT_SLEEPTIME_20000MS 12
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

20000 ms

<a id="ga947cb9dc7689e460f1ddbd8bd94bc15b"></a>

### `TMAG5273_DT_SLEEPTIME_2000MS`

```c
#define TMAG5273_DT_SLEEPTIME_2000MS 10
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

时间：2000 ms。

<a id="gac29e91afbd4636e495726e3252abcea7"></a>

### `TMAG5273_DT_SLEEPTIME_20MS`

```c
#define TMAG5273_DT_SLEEPTIME_20MS 4
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

20 ms

<a id="gaad1cc10df9f35d2bb63cb4a3f021152f"></a>

### `TMAG5273_DT_SLEEPTIME_30MS`

```c
#define TMAG5273_DT_SLEEPTIME_30MS 5
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

30 ms

<a id="gafddb082d0306a7858086c4ac227852e0"></a>

### `TMAG5273_DT_SLEEPTIME_5000MS`

```c
#define TMAG5273_DT_SLEEPTIME_5000MS 11
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

5000 ms

<a id="gabc58f37d75364d3f8c7c03ee774ed091"></a>

### `TMAG5273_DT_SLEEPTIME_500MS`

```c
#define TMAG5273_DT_SLEEPTIME_500MS 8
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

时间：500 ms。

<a id="ga03c1e099cd98b1b09a121bd5c353fc97"></a>

### `TMAG5273_DT_SLEEPTIME_50MS`

```c
#define TMAG5273_DT_SLEEPTIME_50MS 6
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

50 毫秒（ms）。

<a id="gab88e09d09437f57ce31d1ab0f58a19cb"></a>

### `TMAG5273_DT_SLEEPTIME_5MS`

```c
#define TMAG5273_DT_SLEEPTIME_5MS 1
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

5 ms（毫秒）。

<a id="gaec27747fbae8c0c62912431a3f9d2309"></a>

### `TMAG5273_DT_TEMP_COEFF_CERAMIC`

```c
#define TMAG5273_DT_TEMP_COEFF_CERAMIC 2
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

陶瓷磁体（Ceramic Magnet），温度系数为 0.2 %/°C。

<a id="gaf51ec112fe16a5c8a5a55a42dd14fd92"></a>

### `TMAG5273_DT_TEMP_COEFF_NDBFE`

```c
#define TMAG5273_DT_TEMP_COEFF_NDBFE 1
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

钕铁硼磁体（原文为 NdBFe Magnet），温度系数为 0.12 %/°C。

<a id="ga19f4de1abe7275ec75641e5e5ce47826"></a>

### `TMAG5273_DT_TEMP_COEFF_NONE`

```c
#define TMAG5273_DT_TEMP_COEFF_NONE 0
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

不进行补偿（No Compensation）。

<a id="gab59755856b8372698deab44d9b8ec9a2"></a>

### `TMAG5273_DT_THRX_ABOVE`

```c
#define TMAG5273_DT_THRX_ABOVE 0
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

磁场强度上升至阈值（Threshold）以上。

<a id="ga348bd07ca130ff996bea612ad8cecba3"></a>

### `TMAG5273_DT_THRX_BELOW`

```c
#define TMAG5273_DT_THRX_BELOW 1
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

磁场强度下降至阈值（Threshold）以下。

<a id="ga71b6e856b5a5db7af4e4ed0001de2f66"></a>

### `TMAG5273_DT_THRX_COUNT_1`

```c
#define TMAG5273_DT_THRX_COUNT_1 0
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

越过阈值 1 次后触发（Trigger after 1 Crossing）。

<a id="ga3940888f116795a9d060195fdb717ff1"></a>

### `TMAG5273_DT_THRX_COUNT_4`

```c
#define TMAG5273_DT_THRX_COUNT_4 1
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

越过阈值 4 次后触发（Trigger after 4 Crossings）。

<a id="gac0b966cb05b35abe701b8af474fd0498"></a>

### `TMAG5273_DT_THRX_INSIDE`

```c
#define TMAG5273_DT_THRX_INSIDE 3
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

磁场强度进入阈值窗口（Threshold Window）。

<a id="ga630c77a70f3db408a139dd10b3a28bb1"></a>

### `TMAG5273_DT_THRX_OUTSIDE`

```c
#define TMAG5273_DT_THRX_OUTSIDE 2
```

```c
#include <zephyr/dt-bindings/sensor/tmag5273.h>
```

磁场强度离开阈值窗口（Threshold Window）。

<a id="ga6fadcd6cd3b5fbc9281d27f37bdfe0a2"></a>

### `tmag5273_attribute`

```c
enum tmag5273_attribute
```

```c
#include <zephyr/drivers/sensor/tmag5273.h>
```

TMAG5273 支持的附加属性（additional attributes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `TMAG5273_ATTR_ANGLE_MAG_AXIS` | 定义轴间关系测量（Axis Relation Measurements）。支持的取值为：`TMAG5273_DT_ANGLE_MAG_NONE`（0）、`TMAG5273_DT_ANGLE_MAG_XY`（1）、`TMAG5273_DT_ANGLE_MAG_YZ`（2）、`TMAG5273_DT_ANGLE_MAG_XZ`（3）。仅当计算源（Calculation Source）可在运行时更改时可用。 |

<a id="ga3d91dbb6bc6d7dc90ed889651bc34827"></a>

### `tmag5273_sensor_channel`

```c
enum tmag5273_sensor_channel
```

```c
#include <zephyr/drivers/sensor/tmag5273.h>
```

TMAG5273 支持的附加通道（additional channels）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `TMAG5273_CHAN_MAGNITUDE` | 两个轴之间的幅值测量结果（Magnitude Measurement Result），以高斯（Gs）为单位。 |
| `TMAG5273_CHAN_MAGNITUDE_MSB` | 传感器返回的幅值测量最高有效字节（Magnitude Measurement MSB）。 |
| `TMAG5273_CHAN_ANGLE_MAGNITUDE` | 两个轴之间的角度结果（Angle Result，以度为单位）、幅值结果（Magnitude Result，以高斯 Gs 为单位）和幅值最高有效字节（Magnitude MSB）。 |


## 13.16\_原页交叉引用（Cross References）

- [tmag5273.h](../api_file_usb_network_reference/P007_zephyr__dt-bindings__sensor__tmag5273.h_文件参考.md)
- [zephyr/drivers/sensor/tmag5273.h](../api_file_management_reference/P011_zephyr__drivers__sensor__tmag5273.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga6fadcd6cd3b5fbc9281d27f37bdfe0a2af59c66f9794efa1afa7d7461a134d3d3"></a>
<a id="gga3d91dbb6bc6d7dc90ed889651bc34827a72c52112337e191ab9ce906aecdff92d"></a>
<a id="gga3d91dbb6bc6d7dc90ed889651bc34827a601dad57092c442da3a0a184737d8003"></a>
<a id="gga3d91dbb6bc6d7dc90ed889651bc34827a2c4ff267102871c1d23353bbb6b30dbc"></a>

---

[上一章](P012_连接端口（Pad）.md) · [返回大纲](大纲.md) · [下一章](P014_USB Type-C API主题.md)
