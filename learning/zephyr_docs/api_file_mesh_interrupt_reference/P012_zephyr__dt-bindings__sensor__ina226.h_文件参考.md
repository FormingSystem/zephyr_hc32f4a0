---
id: learning.zephyr-docs.api-file-mesh-interrupt-reference.page-12
title: zephyr__dt-bindings__sensor__ina226.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ina226_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_zephyr\_\_dt-bindings\_\_sensor\_\_ina226.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ina226_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

the TI INA226 power monitor的设备树绑定常量（Devicetree Binding Constants）。

<a id="details"></a>

```c
#include <zephyr/dt-bindings/dt-util.h>
```

查看此文件的源码。

the TI INA226 power monitor的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 12.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 复位模式（Reset Mode）

复位模式选择（Reset-mode Selection）。

<a id="r_ga8174524d294a89bcedeec335538cc373"></a>

```c
#define INA226_RST_NORMAL_OPERATION 0x00
```

相关声明：[INA226_RST_NORMAL_OPERATION](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#ga8174524d294a89bcedeec335538cc373)。

正常运行（Normal Operation）。

<a id="r_ga1369ecef1266f83dd93f970002ff61b7"></a>

```c
#define INA226_RST_SYSTEM_RESET 0x01
```

相关声明：[INA226_RST_SYSTEM_RESET](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#ga1369ecef1266f83dd93f970002ff61b7)。

触发系统复位（System Reset）。

<a id="define-members-1"></a>

### 平均模式：采样数（Averaging Mode, Number of Samples）

平均模式选择（Averaging-mode Selection）。

<a id="r_ga5fb596bda9235774ae63f602366b7f75"></a>

```c
#define INA226_AVG_MODE_1 0x00
```

相关声明：[INA226_AVG_MODE_1](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#ga5fb596bda9235774ae63f602366b7f75)。

1 个采样（Samples）。

<a id="r_ga23954364dead3a9df1a878c106939275"></a>

```c
#define INA226_AVG_MODE_4 0x01
```

相关声明：[INA226_AVG_MODE_4](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#ga23954364dead3a9df1a878c106939275)。

4 个样本（Samples）。

<a id="r_ga55785fdf8ae4aa57531dc5107303dce6"></a>

```c
#define INA226_AVG_MODE_16 0x02
```

相关声明：[INA226_AVG_MODE_16](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#ga55785fdf8ae4aa57531dc5107303dce6)。

16 个样本（Samples）。

<a id="r_ga6d0365e097575da1f80cc9dfa20a69f3"></a>

```c
#define INA226_AVG_MODE_64 0x03
```

相关声明：[INA226_AVG_MODE_64](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#ga6d0365e097575da1f80cc9dfa20a69f3)。

64 个样本（Samples）。

<a id="r_ga22345ffb861e057d34a31e4df7340d04"></a>

```c
#define INA226_AVG_MODE_128 0x04
```

相关声明：[INA226_AVG_MODE_128](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#ga22345ffb861e057d34a31e4df7340d04)。

128 个样本（Samples）。

<a id="r_gadc89cd11a9ece7a53f85c5fb2d81842c"></a>

```c
#define INA226_AVG_MODE_256 0x05
```

相关声明：[INA226_AVG_MODE_256](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#gadc89cd11a9ece7a53f85c5fb2d81842c)。

256 个样本（Samples）。

<a id="r_gaf02590f29166255a35e63305e39be4e0"></a>

```c
#define INA226_AVG_MODE_512 0x06
```

相关声明：[INA226_AVG_MODE_512](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#gaf02590f29166255a35e63305e39be4e0)。

512 个样本（Samples）。

<a id="r_ga035c1834dcf1ae41135371b2d9e64110"></a>

```c
#define INA226_AVG_MODE_1024 0x07
```

相关声明：[INA226_AVG_MODE_1024](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#ga035c1834dcf1ae41135371b2d9e64110)。

1024 个采样（Samples）。

<a id="define-members-2"></a>

### 总线电压与分流电阻电压转换时间（Bus and Shunt Voltage Conversion Time）

总线电压和分流电阻电压的转换时间选择（Bus and Shunt Voltage Conversion-time Selection）。

<a id="r_ga95a71cdbb30e0eddfd05f336c53a0bbb"></a>

```c
#define INA226_CONV_TIME_140 0x00
```

相关声明：[INA226_CONV_TIME_140](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#ga95a71cdbb30e0eddfd05f336c53a0bbb)。

140 µs（微秒）。

<a id="r_ga49a08f6e61463403ac18fd89f9f6facb"></a>

```c
#define INA226_CONV_TIME_204 0x01
```

相关声明：[INA226_CONV_TIME_204](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#ga49a08f6e61463403ac18fd89f9f6facb)。

204 µs（微秒）。

<a id="r_ga6f45151cb3e367e9b2a66184fbd1ebf8"></a>

```c
#define INA226_CONV_TIME_332 0x02
```

相关声明：[INA226_CONV_TIME_332](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#ga6f45151cb3e367e9b2a66184fbd1ebf8)。

332 µs（微秒）。

<a id="r_ga445eaee2b6aa6bbdb1caa106580b6036"></a>

```c
#define INA226_CONV_TIME_588 0x03
```

相关声明：[INA226_CONV_TIME_588](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#ga445eaee2b6aa6bbdb1caa106580b6036)。

588 µs（微秒）。

<a id="r_gae063a0b167607657e1ffc1f8e68b2a6c"></a>

```c
#define INA226_CONV_TIME_1100 0x04
```

相关声明：[INA226_CONV_TIME_1100](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#gae063a0b167607657e1ffc1f8e68b2a6c)。

1100 µs（微秒）。

<a id="r_ga83b8bb8b54b2e4857793bf014d9f57af"></a>

```c
#define INA226_CONV_TIME_2116 0x05
```

相关声明：[INA226_CONV_TIME_2116](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#ga83b8bb8b54b2e4857793bf014d9f57af)。

2116 µs（微秒）。

<a id="r_ga02b694b57e4304736d88639d64cebec4"></a>

```c
#define INA226_CONV_TIME_4156 0x06
```

相关声明：[INA226_CONV_TIME_4156](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#ga02b694b57e4304736d88639d64cebec4)。

4156 µs（微秒）。

<a id="r_gaf3037329e3f8b9c984308bf8f4fef851"></a>

```c
#define INA226_CONV_TIME_8244 0x07
```

相关声明：[INA226_CONV_TIME_8244](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#gaf3037329e3f8b9c984308bf8f4fef851)。

8244 µs（微秒）。

<a id="define-members-3"></a>

### 工作模式（Operating mode）

工作模式选择（Operating-mode Selection）。

<a id="r_ga8780c1da54c2e5ae863efb7ef1b310b9"></a>

```c
#define INA226_OPER_MODE_POWER_DOWN 0x00
```

相关声明：[INA226_OPER_MODE_POWER_DOWN](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#ga8780c1da54c2e5ae863efb7ef1b310b9)。

掉电（Power-down）。

<a id="r_gaed00293346e09e6ef3114dd3167d1ce5"></a>

```c
#define INA226_OPER_MODE_SHUNT_VOLTAGE_TRIG 0x01
```

相关声明：[INA226_OPER_MODE_SHUNT_VOLTAGE_TRIG](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#gaed00293346e09e6ef3114dd3167d1ce5)。

分流电阻电压（Shunt Voltage），触发模式（Triggered）。

<a id="r_ga88aa0c1378cfe356b643c89bf1418e3e"></a>

```c
#define INA226_OPER_MODE_BUS_VOLTAGE_TRIG 0x02
```

相关声明：[INA226_OPER_MODE_BUS_VOLTAGE_TRIG](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#ga88aa0c1378cfe356b643c89bf1418e3e)。

总线电压（Bus Voltage），触发模式（Triggered）。

<a id="r_ga7e88c1ab79bed8425f3074b37903113b"></a>

```c
#define INA226_OPER_MODE_SHUNT_BUS_VOLTAGE_TRIG 0x03
```

相关声明：[INA226_OPER_MODE_SHUNT_BUS_VOLTAGE_TRIG](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#ga7e88c1ab79bed8425f3074b37903113b)。

分流电阻电压与总线电压（Shunt and Bus），触发模式（Triggered）。

<a id="r_gafad378147deb5e1789a40e5dd7611de9"></a>

```c
#define INA226_OPER_MODE_SHUNT_VOLTAGE_CONT 0x05
```

相关声明：[INA226_OPER_MODE_SHUNT_VOLTAGE_CONT](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#gafad378147deb5e1789a40e5dd7611de9)。

分流电阻电压（Shunt Voltage），连续模式（Continuous）。

<a id="r_gadcf4265f1272f33a8385cf6a8c20bc42"></a>

```c
#define INA226_OPER_MODE_BUS_VOLTAGE_CONT 0x06
```

相关声明：[INA226_OPER_MODE_BUS_VOLTAGE_CONT](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#gadcf4265f1272f33a8385cf6a8c20bc42)。

总线电压（Bus Voltage），连续模式（Continuous）。

<a id="r_gaba344632242e46fcd392eaf7f114f820"></a>

```c
#define INA226_OPER_MODE_SHUNT_BUS_VOLTAGE_CONT 0x07
```

相关声明：[INA226_OPER_MODE_SHUNT_BUS_VOLTAGE_CONT](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#gaba344632242e46fcd392eaf7f114f820)。

分流电阻电压与总线电压（Shunt and Bus），连续模式（Continuous）。


## 12.2\_原页交叉引用（Cross References）

- [zephyr/dt-bindings/dt-util.h](../dt_bus_binding_reference/P006_设备树绑定工具头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P359_ina226.h_源码浏览.md)
- [INA226_RST_NORMAL_OPERATION](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#ga8174524d294a89bcedeec335538cc373)
- [INA226_RST_SYSTEM_RESET](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#ga1369ecef1266f83dd93f970002ff61b7)
- [INA226_AVG_MODE_1](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#ga5fb596bda9235774ae63f602366b7f75)
- [INA226_AVG_MODE_4](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#ga23954364dead3a9df1a878c106939275)
- [INA226_AVG_MODE_16](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#ga55785fdf8ae4aa57531dc5107303dce6)
- [INA226_AVG_MODE_64](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#ga6d0365e097575da1f80cc9dfa20a69f3)
- [INA226_AVG_MODE_128](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#ga22345ffb861e057d34a31e4df7340d04)
- [INA226_AVG_MODE_256](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#gadc89cd11a9ece7a53f85c5fb2d81842c)
- [INA226_AVG_MODE_512](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#gaf02590f29166255a35e63305e39be4e0)
- [INA226_AVG_MODE_1024](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#ga035c1834dcf1ae41135371b2d9e64110)
- [INA226_CONV_TIME_140](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#ga95a71cdbb30e0eddfd05f336c53a0bbb)
- [INA226_CONV_TIME_204](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#ga49a08f6e61463403ac18fd89f9f6facb)
- [INA226_CONV_TIME_332](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#ga6f45151cb3e367e9b2a66184fbd1ebf8)
- [INA226_CONV_TIME_588](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#ga445eaee2b6aa6bbdb1caa106580b6036)
- [INA226_CONV_TIME_1100](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#gae063a0b167607657e1ffc1f8e68b2a6c)
- [INA226_CONV_TIME_2116](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#ga83b8bb8b54b2e4857793bf014d9f57af)
- [INA226_CONV_TIME_4156](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#ga02b694b57e4304736d88639d64cebec4)
- [INA226_CONV_TIME_8244](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#gaf3037329e3f8b9c984308bf8f4fef851)
- [INA226_OPER_MODE_POWER_DOWN](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#ga8780c1da54c2e5ae863efb7ef1b310b9)
- [INA226_OPER_MODE_SHUNT_VOLTAGE_TRIG](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#gaed00293346e09e6ef3114dd3167d1ce5)
- [INA226_OPER_MODE_BUS_VOLTAGE_TRIG](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#ga88aa0c1378cfe356b643c89bf1418e3e)
- [INA226_OPER_MODE_SHUNT_BUS_VOLTAGE_TRIG](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#ga7e88c1ab79bed8425f3074b37903113b)
- [INA226_OPER_MODE_SHUNT_VOLTAGE_CONT](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#gafad378147deb5e1789a40e5dd7611de9)
- [INA226_OPER_MODE_BUS_VOLTAGE_CONT](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#gadcf4265f1272f33a8385cf6a8c20bc42)
- [INA226_OPER_MODE_SHUNT_BUS_VOLTAGE_CONT](../api_bridge_paging_topic_reference/P007_INA226 API主题.md#gaba344632242e46fcd392eaf7f114f820)

<a id="header-details"></a>

---

[上一章](P011_zephyr__dt-bindings__power__imx952_power.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P013_zephyr__dt-bindings__sensor__ina230.h_文件参考.md)
