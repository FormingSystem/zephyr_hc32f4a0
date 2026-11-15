---
id: learning.zephyr-docs.api-file-display-chat-reference.page-7
title: zephyr__drivers__sensor__max30009.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2max30009_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_zephyr\_\_drivers\_\_sensor\_\_max30009.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2max30009_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MAX30009传感器的扩展API头文件（Extended Sensor API Header）。

<a id="details"></a>

```c
#include <zephyr/drivers/sensor.h>
```

查看此文件的源码。

MAX30009传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 7.1\_枚举（Enumerations）

<a id="r_a7d25a6904a472858d8f50abb7a516f0c"></a>

```c
enum max30009_sensor_channel { SENSOR_CHAN_BIOZ_I = SENSOR_CHAN_PRIV_START , SENSOR_CHAN_BIOZ_Q }
```

相关声明：[max30009_sensor_channel](#a7d25a6904a472858d8f50abb7a516f0c)、[SENSOR_CHAN_BIOZ_I](#a7d25a6904a472858d8f50abb7a516f0ca750aca5fff60a43969bd4a9a5a04c3cf)、[SENSOR_CHAN_BIOZ_Q](#a7d25a6904a472858d8f50abb7a516f0cace47c5d2dfbe4918369d94c1abf12642)。

MAX30009 专用传感器通道（Sensor Channels）。

<a id="r_a65324d1d56d862c1eed27ac554744f9a"></a>

```c
enum sensor_trigger_max30009 { SENSOR_TRIG_MAX30009_DC_LOFF_NL = SENSOR_TRIG_PRIV_START , SENSOR_TRIG_MAX30009_DC_LOFF_NH , SENSOR_TRIG_MAX30009_DC_LOFF_PL , SENSOR_TRIG_MAX30009_DC_LOFF_PH , SENSOR_TRIG_MAX30009_DRV_OOR , SENSOR_TRIG_MAX30009_BIOZ_UNDR , SENSOR_TRIG_MAX30009_BIOZ_OVER , SENSOR_TRIG_MAX30009_LON }
```

相关声明：[sensor_trigger_max30009](#a65324d1d56d862c1eed27ac554744f9a)、[SENSOR_TRIG_MAX30009_DC_LOFF_NL](#a65324d1d56d862c1eed27ac554744f9aac9459b47e68ba787e18ad97a36cd126a)、[SENSOR_TRIG_MAX30009_DC_LOFF_NH](#a65324d1d56d862c1eed27ac554744f9aa8ae1e5706346f943cdf1a01330df9fc3)、[SENSOR_TRIG_MAX30009_DC_LOFF_PL](#a65324d1d56d862c1eed27ac554744f9aa04399d87079f892c6c348f9a40f00539)、[SENSOR_TRIG_MAX30009_DC_LOFF_PH](#a65324d1d56d862c1eed27ac554744f9aaa9a67a091d792dde5ce900a9688b14d2)、[SENSOR_TRIG_MAX30009_DRV_OOR](#a65324d1d56d862c1eed27ac554744f9aac65258c212a8cde22ae6de4e0657a040)、[SENSOR_TRIG_MAX30009_BIOZ_UNDR](#a65324d1d56d862c1eed27ac554744f9aa2b50e73be8b270b3b98c84968bf48a79)、[SENSOR_TRIG_MAX30009_BIOZ_OVER](#a65324d1d56d862c1eed27ac554744f9aa6055753372c850654a0a3b28eefa0f04)、[SENSOR_TRIG_MAX30009_LON](#a65324d1d56d862c1eed27ac554744f9aaf08af70f5722abc7c85a77e9eeb7b4d9)。

MAX30009 专用传感器触发器（Sensor Triggers）。

<a id="r_a7366cc88a4aa3b7ade63c9014298ade9"></a>

```c
enum sensor_attribute_max30009 { SENSOR_ATTR_MAX30009_DRV_MODE = SENSOR_ATTR_PRIV_START , SENSOR_ATTR_MAX30009_IDRV_RGE , SENSOR_ATTR_MAX30009_VDRV_MAG , SENSOR_ATTR_MAX30009_GAIN , SENSOR_ATTR_MAX30009_AHPF , SENSOR_ATTR_MAX30009_DHPF , SENSOR_ATTR_MAX30009_DLPF , SENSOR_ATTR_MAX30009_AMP_RGE , SENSOR_ATTR_MAX30009_AMP_BW , SENSOR_ATTR_MAX30009_CMP , SENSOR_ATTR_MAX30009_ADC_OSR , SENSOR_ATTR_MAX30009_DAC_OSR , SENSOR_ATTR_MAX30009_HIGH_THRESHOLD , SENSOR_ATTR_MAX30009_LOW_THRESHOLD , SENSOR_ATTR_MAX30009_I_EN , SENSOR_ATTR_MAX30009_Q_EN , SENSOR_ATTR_MAX30009_BG_EN }
```

相关声明：[sensor_attribute_max30009](#a7366cc88a4aa3b7ade63c9014298ade9)、[SENSOR_ATTR_MAX30009_DRV_MODE](#a7366cc88a4aa3b7ade63c9014298ade9a78d09ddb7b344dc0f007e850894def1a)、[SENSOR_ATTR_MAX30009_IDRV_RGE](#a7366cc88a4aa3b7ade63c9014298ade9a31f772c5243e8e90816600cac9f7e36c)、[SENSOR_ATTR_MAX30009_VDRV_MAG](#a7366cc88a4aa3b7ade63c9014298ade9aadd28679aeea94433edac6d091b69f3b)、[SENSOR_ATTR_MAX30009_GAIN](#a7366cc88a4aa3b7ade63c9014298ade9a506f4e2b8156a850fda7bea8651312fc)、[SENSOR_ATTR_MAX30009_AHPF](#a7366cc88a4aa3b7ade63c9014298ade9a0de1e5813fe8bb7c41cee39a07b3f4b4)、[SENSOR_ATTR_MAX30009_DHPF](#a7366cc88a4aa3b7ade63c9014298ade9a8dccb1580469a2fd0b4702d377e25f61)、[SENSOR_ATTR_MAX30009_DLPF](#a7366cc88a4aa3b7ade63c9014298ade9a6d19b4ba476f304c547d4305d24aa4f7)、[SENSOR_ATTR_MAX30009_AMP_RGE](#a7366cc88a4aa3b7ade63c9014298ade9a86f28ee89b48be0c3528cbf7f82cd9ea)、[SENSOR_ATTR_MAX30009_AMP_BW](#a7366cc88a4aa3b7ade63c9014298ade9a51e7ee0949bb80f9ee7eed0ddfc9f5b5)、[SENSOR_ATTR_MAX30009_CMP](#a7366cc88a4aa3b7ade63c9014298ade9a5d92dd9e6512ccb7875a857b58956ebb)、[SENSOR_ATTR_MAX30009_ADC_OSR](#a7366cc88a4aa3b7ade63c9014298ade9a19c1485d07366911422a749caaafaff7)、[SENSOR_ATTR_MAX30009_DAC_OSR](#a7366cc88a4aa3b7ade63c9014298ade9aa11391460a143eae29a5fc849e8d2b7f)、[SENSOR_ATTR_MAX30009_HIGH_THRESHOLD](#a7366cc88a4aa3b7ade63c9014298ade9a4a5b71563c45a57d479bfc74b0403bf4)、[SENSOR_ATTR_MAX30009_LOW_THRESHOLD](#a7366cc88a4aa3b7ade63c9014298ade9a16f233f24884270ef0533c6fe9e293c6)、[SENSOR_ATTR_MAX30009_I_EN](#a7366cc88a4aa3b7ade63c9014298ade9a2094f22b0d46ed37e2947438c37a7267)、[SENSOR_ATTR_MAX30009_Q_EN](#a7366cc88a4aa3b7ade63c9014298ade9ac7963ea5551da9b318b87daddcc648d7)、[SENSOR_ATTR_MAX30009_BG_EN](#a7366cc88a4aa3b7ade63c9014298ade9a65e4e4fd9efa1a0204fd54e797666fc1)。

MAX30009 专用传感器属性（Sensor Attributes）。

## 7.2\_详细说明（Detailed Documentation）

<a id="a7d25a6904a472858d8f50abb7a516f0c"></a>

### `max30009_sensor_channel`

```c
enum max30009_sensor_channel
```

MAX30009 专用传感器通道（Sensor Channels）。

这些通道扩展标准 sensor_channel 枚举，用于提供 MAX30009 生物阻抗（BioZ）的同相（In-phase）和正交（Quadrature）数据。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_CHAN_BIOZ_I` | BioZ 同相（In-phase，I）通道。 |
| `SENSOR_CHAN_BIOZ_Q` | BioZ 正交（Quadrature，Q）通道。 |

<a id="a7366cc88a4aa3b7ade63c9014298ade9"></a>

### `sensor_attribute_max30009`

```c
enum sensor_attribute_max30009
```

MAX30009 专用传感器属性（Sensor Attributes）。

这些属性扩展标准 sensor_attribute 枚举，以支持 MAX30009 专用的生物阻抗（BioZ）配置选项。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_ATTR_MAX30009_DRV_MODE` | BioZ 发送驱动模式（Transmit Drive Mode，BIOZ_DRV_MODE）。 |
| `SENSOR_ATTR_MAX30009_IDRV_RGE` | BioZ 内部电流量程电阻（Internal Current-range Resistor，BIOZ_IDRV_RGE）。 |
| `SENSOR_ATTR_MAX30009_VDRV_MAG` | BioZ 电压驱动幅度（Voltage-drive Magnitude，BIOZ_VDRV_MAG）。 |
| `SENSOR_ATTR_MAX30009_GAIN` | BioZ 接收通道增益（Receive-channel Gain，BIOZ_GAIN）。 |
| `SENSOR_ATTR_MAX30009_AHPF` | BioZ 模拟高通滤波器选择（Analog High-pass Filter Selection，BIOZ_AHPF）。 |
| `SENSOR_ATTR_MAX30009_DHPF` | BioZ 数字高通滤波器截止频率（Digital High-pass Filter Cutoff，BIOZ_DHPF）。 |
| `SENSOR_ATTR_MAX30009_DLPF` | BioZ 数字低通滤波器截止频率（Digital Low-pass Filter Cutoff，BIOZ_DLPF）。 |
| `SENSOR_ATTR_MAX30009_AMP_RGE` | BioZ 放大器量程（Amplifier Range，BIOZ_AMP_RGE）。 |
| `SENSOR_ATTR_MAX30009_AMP_BW` | BioZ 放大器带宽（Amplifier Bandwidth，BIOZ_AMP_BW）。 |
| `SENSOR_ATTR_MAX30009_CMP` | BioZ 阈值比较器通道（Threshold Comparator Channel，BIOZ_CMP）。 |
| `SENSOR_ATTR_MAX30009_ADC_OSR` | BioZ ADC 过采样率（Oversampling Ratio），按自然单位表示，范围为 8..1024（BIOZ_ADC_OSR）。 |
| `SENSOR_ATTR_MAX30009_DAC_OSR` | BioZ DAC 过采样率（Oversampling Ratio），按自然单位表示，范围为 32..256（BIOZ_DAC_OSR）。 |
| `SENSOR_ATTR_MAX30009_HIGH_THRESHOLD` | BioZ 高阈值（High Threshold，BIOZ_HIGH_THRESHOLD）。 |
| `SENSOR_ATTR_MAX30009_LOW_THRESHOLD` | BioZ 低阈值（Low Threshold，BIOZ_LOW_THRESHOLD）。 |
| `SENSOR_ATTR_MAX30009_I_EN` | 启用 BioZ 同相（In-phase，I）通道（BIOZ_I_EN）。 |
| `SENSOR_ATTR_MAX30009_Q_EN` | 启用 BioZ 正交（Quadrature，Q）通道（BIOZ_Q_EN）。 |
| `SENSOR_ATTR_MAX30009_BG_EN` | 启用 BioZ 带隙偏置（Bandgap Bias，BIOZ_BG_EN）。 |

<a id="a65324d1d56d862c1eed27ac554744f9a"></a>

### `sensor_trigger_max30009`

```c
enum sensor_trigger_max30009
```

MAX30009 专用传感器触发器（Sensor Triggers）。

这些触发器扩展标准 sensor_trigger_type 枚举，以支持 MAX30009 的直流导联脱落（DC Lead-off）和量程状态（Range Status）事件。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_TRIG_MAX30009_DC_LOFF_NL` | 直流导联脱落（DC Lead-off）：BIOZN（BIN）电压低于低阈值。 |
| `SENSOR_TRIG_MAX30009_DC_LOFF_NH` | 直流导联脱落（DC Lead-off）：BIOZN（BIN）电压高于高阈值。 |
| `SENSOR_TRIG_MAX30009_DC_LOFF_PL` | 直流导联脱落（DC Lead-off）：BIOZP（BIP）电压低于低阈值。 |
| `SENSOR_TRIG_MAX30009_DC_LOFF_PH` | 直流导联脱落（DC Lead-off）：BIOZP（BIP）电压高于高阈值。 |
| `SENSOR_TRIG_MAX30009_DRV_OOR` | BioZ 电流发生器超出范围（Current Generator Out of Range）：DRVN 峰值超出合规范围，导联脱落。 |
| `SENSOR_TRIG_MAX30009_BIOZ_UNDR` | BioZ 低于量程（Under Range）：BioZ ADC 读数的绝对值低于 BioZ 低阈值。 |
| `SENSOR_TRIG_MAX30009_BIOZ_OVER` | BioZ 超出量程（Over Range）：BioZ ADC 读数的绝对值超过 BioZ 高阈值。 |
| `SENSOR_TRIG_MAX30009_LON` | 检测到直流导联接通（DC Leads-on）：存在 BioZ 导联接通条件。 |


## 7.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](../api_source_transport_clock_reference/P024_sensor.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P179_max30009.h_源码浏览.md)
- [sensor_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gaaa1b502bc029b10d7b23b0a25ef4e934)
- [sensor_attribute](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga0dcb6842bc969492bd1c9eb49708940b)
- [sensor_trigger_type](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga08215279400e8c9eb05ce4e4f0898ffd)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a7d25a6904a472858d8f50abb7a516f0ca750aca5fff60a43969bd4a9a5a04c3cf"></a>
<a id="a7d25a6904a472858d8f50abb7a516f0cace47c5d2dfbe4918369d94c1abf12642"></a>
<a id="a7366cc88a4aa3b7ade63c9014298ade9a78d09ddb7b344dc0f007e850894def1a"></a>
<a id="a7366cc88a4aa3b7ade63c9014298ade9a31f772c5243e8e90816600cac9f7e36c"></a>
<a id="a7366cc88a4aa3b7ade63c9014298ade9aadd28679aeea94433edac6d091b69f3b"></a>
<a id="a7366cc88a4aa3b7ade63c9014298ade9a506f4e2b8156a850fda7bea8651312fc"></a>
<a id="a7366cc88a4aa3b7ade63c9014298ade9a0de1e5813fe8bb7c41cee39a07b3f4b4"></a>
<a id="a7366cc88a4aa3b7ade63c9014298ade9a8dccb1580469a2fd0b4702d377e25f61"></a>
<a id="a7366cc88a4aa3b7ade63c9014298ade9a6d19b4ba476f304c547d4305d24aa4f7"></a>
<a id="a7366cc88a4aa3b7ade63c9014298ade9a86f28ee89b48be0c3528cbf7f82cd9ea"></a>
<a id="a7366cc88a4aa3b7ade63c9014298ade9a51e7ee0949bb80f9ee7eed0ddfc9f5b5"></a>
<a id="a7366cc88a4aa3b7ade63c9014298ade9a5d92dd9e6512ccb7875a857b58956ebb"></a>
<a id="a7366cc88a4aa3b7ade63c9014298ade9a19c1485d07366911422a749caaafaff7"></a>
<a id="a7366cc88a4aa3b7ade63c9014298ade9aa11391460a143eae29a5fc849e8d2b7f"></a>
<a id="a7366cc88a4aa3b7ade63c9014298ade9a4a5b71563c45a57d479bfc74b0403bf4"></a>
<a id="a7366cc88a4aa3b7ade63c9014298ade9a16f233f24884270ef0533c6fe9e293c6"></a>
<a id="a7366cc88a4aa3b7ade63c9014298ade9a2094f22b0d46ed37e2947438c37a7267"></a>
<a id="a7366cc88a4aa3b7ade63c9014298ade9ac7963ea5551da9b318b87daddcc648d7"></a>
<a id="a7366cc88a4aa3b7ade63c9014298ade9a65e4e4fd9efa1a0204fd54e797666fc1"></a>
<a id="a65324d1d56d862c1eed27ac554744f9aac9459b47e68ba787e18ad97a36cd126a"></a>
<a id="a65324d1d56d862c1eed27ac554744f9aa8ae1e5706346f943cdf1a01330df9fc3"></a>
<a id="a65324d1d56d862c1eed27ac554744f9aa04399d87079f892c6c348f9a40f00539"></a>
<a id="a65324d1d56d862c1eed27ac554744f9aaa9a67a091d792dde5ce900a9688b14d2"></a>
<a id="a65324d1d56d862c1eed27ac554744f9aac65258c212a8cde22ae6de4e0657a040"></a>
<a id="a65324d1d56d862c1eed27ac554744f9aa2b50e73be8b270b3b98c84968bf48a79"></a>
<a id="a65324d1d56d862c1eed27ac554744f9aa6055753372c850654a0a3b28eefa0f04"></a>
<a id="a65324d1d56d862c1eed27ac554744f9aaf08af70f5722abc7c85a77e9eeb7b4d9"></a>

---

[上一章](P006_zephyr__drivers__display.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P008_zephyr__drivers__sensor__pac194x.h_文件参考.md)
