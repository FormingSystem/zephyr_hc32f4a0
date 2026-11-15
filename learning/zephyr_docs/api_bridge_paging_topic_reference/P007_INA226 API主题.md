---
id: learning.zephyr-docs.api-bridge-paging-topic-reference.page-7
title: INA226 API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ina226__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_INA226 API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__ina226__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Texas Instruments INA226 电流与功率监测器。

<a id="details"></a>

Texas Instruments INA226 电流与功率监测器。

<a id="header-files"></a>
<a id="files"></a>

## 7.1\_文件（Files）

<a id="r_ina226_2Eh"></a>

```c
file ina226.h
```

相关声明：[ina226.h](https://docs.zephyrproject.org/latest/doxygen/html/ina226_8h.html)。

the TI INA226 power monitor的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 7.2\_复位模式（Reset Mode）

复位模式选择（Reset-mode Selection）。

<a id="r_ga8174524d294a89bcedeec335538cc373"></a>

```c
#define INA226_RST_NORMAL_OPERATION 0x00
```

相关声明：[INA226_RST_NORMAL_OPERATION](#ga8174524d294a89bcedeec335538cc373)。

正常运行（Normal Operation）。

<a id="r_ga1369ecef1266f83dd93f970002ff61b7"></a>

```c
#define INA226_RST_SYSTEM_RESET 0x01
```

相关声明：[INA226_RST_SYSTEM_RESET](#ga1369ecef1266f83dd93f970002ff61b7)。

触发系统复位（System Reset）。

## 7.3\_平均模式：采样数（Averaging Mode, Number of Samples）

平均模式选择（Averaging-mode Selection）。

<a id="r_ga5fb596bda9235774ae63f602366b7f75"></a>

```c
#define INA226_AVG_MODE_1 0x00
```

相关声明：[INA226_AVG_MODE_1](#ga5fb596bda9235774ae63f602366b7f75)。

1 个采样（Samples）。

<a id="r_ga23954364dead3a9df1a878c106939275"></a>

```c
#define INA226_AVG_MODE_4 0x01
```

相关声明：[INA226_AVG_MODE_4](#ga23954364dead3a9df1a878c106939275)。

4 个样本（Samples）。

<a id="r_ga55785fdf8ae4aa57531dc5107303dce6"></a>

```c
#define INA226_AVG_MODE_16 0x02
```

相关声明：[INA226_AVG_MODE_16](#ga55785fdf8ae4aa57531dc5107303dce6)。

16 个样本（Samples）。

<a id="r_ga6d0365e097575da1f80cc9dfa20a69f3"></a>

```c
#define INA226_AVG_MODE_64 0x03
```

相关声明：[INA226_AVG_MODE_64](#ga6d0365e097575da1f80cc9dfa20a69f3)。

64 个样本（Samples）。

<a id="r_ga22345ffb861e057d34a31e4df7340d04"></a>

```c
#define INA226_AVG_MODE_128 0x04
```

相关声明：[INA226_AVG_MODE_128](#ga22345ffb861e057d34a31e4df7340d04)。

128 个样本（Samples）。

<a id="r_gadc89cd11a9ece7a53f85c5fb2d81842c"></a>

```c
#define INA226_AVG_MODE_256 0x05
```

相关声明：[INA226_AVG_MODE_256](#gadc89cd11a9ece7a53f85c5fb2d81842c)。

256 个样本（Samples）。

<a id="r_gaf02590f29166255a35e63305e39be4e0"></a>

```c
#define INA226_AVG_MODE_512 0x06
```

相关声明：[INA226_AVG_MODE_512](#gaf02590f29166255a35e63305e39be4e0)。

512 个样本（Samples）。

<a id="r_ga035c1834dcf1ae41135371b2d9e64110"></a>

```c
#define INA226_AVG_MODE_1024 0x07
```

相关声明：[INA226_AVG_MODE_1024](#ga035c1834dcf1ae41135371b2d9e64110)。

1024 个采样（Samples）。

## 7.4\_总线电压与分流电阻电压转换时间（Bus and Shunt Voltage Conversion Time）

总线电压和分流电阻电压的转换时间选择（Bus and Shunt Voltage Conversion-time Selection）。

<a id="r_ga95a71cdbb30e0eddfd05f336c53a0bbb"></a>

```c
#define INA226_CONV_TIME_140 0x00
```

相关声明：[INA226_CONV_TIME_140](#ga95a71cdbb30e0eddfd05f336c53a0bbb)。

140 µs（微秒）。

<a id="r_ga49a08f6e61463403ac18fd89f9f6facb"></a>

```c
#define INA226_CONV_TIME_204 0x01
```

相关声明：[INA226_CONV_TIME_204](#ga49a08f6e61463403ac18fd89f9f6facb)。

204 µs（微秒）。

<a id="r_ga6f45151cb3e367e9b2a66184fbd1ebf8"></a>

```c
#define INA226_CONV_TIME_332 0x02
```

相关声明：[INA226_CONV_TIME_332](#ga6f45151cb3e367e9b2a66184fbd1ebf8)。

332 µs（微秒）。

<a id="r_ga445eaee2b6aa6bbdb1caa106580b6036"></a>

```c
#define INA226_CONV_TIME_588 0x03
```

相关声明：[INA226_CONV_TIME_588](#ga445eaee2b6aa6bbdb1caa106580b6036)。

588 µs（微秒）。

<a id="r_gae063a0b167607657e1ffc1f8e68b2a6c"></a>

```c
#define INA226_CONV_TIME_1100 0x04
```

相关声明：[INA226_CONV_TIME_1100](#gae063a0b167607657e1ffc1f8e68b2a6c)。

1100 µs（微秒）。

<a id="r_ga83b8bb8b54b2e4857793bf014d9f57af"></a>

```c
#define INA226_CONV_TIME_2116 0x05
```

相关声明：[INA226_CONV_TIME_2116](#ga83b8bb8b54b2e4857793bf014d9f57af)。

2116 µs（微秒）。

<a id="r_ga02b694b57e4304736d88639d64cebec4"></a>

```c
#define INA226_CONV_TIME_4156 0x06
```

相关声明：[INA226_CONV_TIME_4156](#ga02b694b57e4304736d88639d64cebec4)。

4156 µs（微秒）。

<a id="r_gaf3037329e3f8b9c984308bf8f4fef851"></a>

```c
#define INA226_CONV_TIME_8244 0x07
```

相关声明：[INA226_CONV_TIME_8244](#gaf3037329e3f8b9c984308bf8f4fef851)。

8244 µs（微秒）。

## 7.5\_工作模式（Operating mode）

工作模式选择（Operating-mode Selection）。

<a id="r_ga8780c1da54c2e5ae863efb7ef1b310b9"></a>

```c
#define INA226_OPER_MODE_POWER_DOWN 0x00
```

相关声明：[INA226_OPER_MODE_POWER_DOWN](#ga8780c1da54c2e5ae863efb7ef1b310b9)。

掉电（Power-down）。

<a id="r_gaed00293346e09e6ef3114dd3167d1ce5"></a>

```c
#define INA226_OPER_MODE_SHUNT_VOLTAGE_TRIG 0x01
```

相关声明：[INA226_OPER_MODE_SHUNT_VOLTAGE_TRIG](#gaed00293346e09e6ef3114dd3167d1ce5)。

分流电阻电压（Shunt Voltage），触发模式（Triggered）。

<a id="r_ga88aa0c1378cfe356b643c89bf1418e3e"></a>

```c
#define INA226_OPER_MODE_BUS_VOLTAGE_TRIG 0x02
```

相关声明：[INA226_OPER_MODE_BUS_VOLTAGE_TRIG](#ga88aa0c1378cfe356b643c89bf1418e3e)。

总线电压（Bus Voltage），触发模式（Triggered）。

<a id="r_ga7e88c1ab79bed8425f3074b37903113b"></a>

```c
#define INA226_OPER_MODE_SHUNT_BUS_VOLTAGE_TRIG 0x03
```

相关声明：[INA226_OPER_MODE_SHUNT_BUS_VOLTAGE_TRIG](#ga7e88c1ab79bed8425f3074b37903113b)。

分流电阻电压与总线电压（Shunt and Bus），触发模式（Triggered）。

<a id="r_gafad378147deb5e1789a40e5dd7611de9"></a>

```c
#define INA226_OPER_MODE_SHUNT_VOLTAGE_CONT 0x05
```

相关声明：[INA226_OPER_MODE_SHUNT_VOLTAGE_CONT](#gafad378147deb5e1789a40e5dd7611de9)。

分流电阻电压（Shunt Voltage），连续模式（Continuous）。

<a id="r_gadcf4265f1272f33a8385cf6a8c20bc42"></a>

```c
#define INA226_OPER_MODE_BUS_VOLTAGE_CONT 0x06
```

相关声明：[INA226_OPER_MODE_BUS_VOLTAGE_CONT](#gadcf4265f1272f33a8385cf6a8c20bc42)。

总线电压（Bus Voltage），连续模式（Continuous）。

<a id="r_gaba344632242e46fcd392eaf7f114f820"></a>

```c
#define INA226_OPER_MODE_SHUNT_BUS_VOLTAGE_CONT 0x07
```

相关声明：[INA226_OPER_MODE_SHUNT_BUS_VOLTAGE_CONT](#gaba344632242e46fcd392eaf7f114f820)。

分流电阻电压与总线电压（Shunt and Bus），连续模式（Continuous）。

## 7.6\_详细说明（Detailed Documentation）

<a id="ga5fb596bda9235774ae63f602366b7f75"></a>

### `INA226_AVG_MODE_1`

```c
#define INA226_AVG_MODE_1 0x00
```

```c
#include <zephyr/dt-bindings/sensor/ina226.h>
```

1 个采样（Samples）。

<a id="ga035c1834dcf1ae41135371b2d9e64110"></a>

### `INA226_AVG_MODE_1024`

```c
#define INA226_AVG_MODE_1024 0x07
```

```c
#include <zephyr/dt-bindings/sensor/ina226.h>
```

1024 个采样（Samples）。

<a id="ga22345ffb861e057d34a31e4df7340d04"></a>

### `INA226_AVG_MODE_128`

```c
#define INA226_AVG_MODE_128 0x04
```

```c
#include <zephyr/dt-bindings/sensor/ina226.h>
```

128 个样本（Samples）。

<a id="ga55785fdf8ae4aa57531dc5107303dce6"></a>

### `INA226_AVG_MODE_16`

```c
#define INA226_AVG_MODE_16 0x02
```

```c
#include <zephyr/dt-bindings/sensor/ina226.h>
```

16 个样本（Samples）。

<a id="gadc89cd11a9ece7a53f85c5fb2d81842c"></a>

### `INA226_AVG_MODE_256`

```c
#define INA226_AVG_MODE_256 0x05
```

```c
#include <zephyr/dt-bindings/sensor/ina226.h>
```

256 个样本（Samples）。

<a id="ga23954364dead3a9df1a878c106939275"></a>

### `INA226_AVG_MODE_4`

```c
#define INA226_AVG_MODE_4 0x01
```

```c
#include <zephyr/dt-bindings/sensor/ina226.h>
```

4 个样本（Samples）。

<a id="gaf02590f29166255a35e63305e39be4e0"></a>

### `INA226_AVG_MODE_512`

```c
#define INA226_AVG_MODE_512 0x06
```

```c
#include <zephyr/dt-bindings/sensor/ina226.h>
```

512 个样本（Samples）。

<a id="ga6d0365e097575da1f80cc9dfa20a69f3"></a>

### `INA226_AVG_MODE_64`

```c
#define INA226_AVG_MODE_64 0x03
```

```c
#include <zephyr/dt-bindings/sensor/ina226.h>
```

64 个样本（Samples）。

<a id="gae063a0b167607657e1ffc1f8e68b2a6c"></a>

### `INA226_CONV_TIME_1100`

```c
#define INA226_CONV_TIME_1100 0x04
```

```c
#include <zephyr/dt-bindings/sensor/ina226.h>
```

1100 µs（微秒）。

<a id="ga95a71cdbb30e0eddfd05f336c53a0bbb"></a>

### `INA226_CONV_TIME_140`

```c
#define INA226_CONV_TIME_140 0x00
```

```c
#include <zephyr/dt-bindings/sensor/ina226.h>
```

140 µs（微秒）。

<a id="ga49a08f6e61463403ac18fd89f9f6facb"></a>

### `INA226_CONV_TIME_204`

```c
#define INA226_CONV_TIME_204 0x01
```

```c
#include <zephyr/dt-bindings/sensor/ina226.h>
```

204 µs（微秒）。

<a id="ga83b8bb8b54b2e4857793bf014d9f57af"></a>

### `INA226_CONV_TIME_2116`

```c
#define INA226_CONV_TIME_2116 0x05
```

```c
#include <zephyr/dt-bindings/sensor/ina226.h>
```

2116 µs（微秒）。

<a id="ga6f45151cb3e367e9b2a66184fbd1ebf8"></a>

### `INA226_CONV_TIME_332`

```c
#define INA226_CONV_TIME_332 0x02
```

```c
#include <zephyr/dt-bindings/sensor/ina226.h>
```

332 µs（微秒）。

<a id="ga02b694b57e4304736d88639d64cebec4"></a>

### `INA226_CONV_TIME_4156`

```c
#define INA226_CONV_TIME_4156 0x06
```

```c
#include <zephyr/dt-bindings/sensor/ina226.h>
```

4156 µs（微秒）。

<a id="ga445eaee2b6aa6bbdb1caa106580b6036"></a>

### `INA226_CONV_TIME_588`

```c
#define INA226_CONV_TIME_588 0x03
```

```c
#include <zephyr/dt-bindings/sensor/ina226.h>
```

588 µs（微秒）。

<a id="gaf3037329e3f8b9c984308bf8f4fef851"></a>

### `INA226_CONV_TIME_8244`

```c
#define INA226_CONV_TIME_8244 0x07
```

```c
#include <zephyr/dt-bindings/sensor/ina226.h>
```

8244 µs（微秒）。

<a id="gadcf4265f1272f33a8385cf6a8c20bc42"></a>

### `INA226_OPER_MODE_BUS_VOLTAGE_CONT`

```c
#define INA226_OPER_MODE_BUS_VOLTAGE_CONT 0x06
```

```c
#include <zephyr/dt-bindings/sensor/ina226.h>
```

总线电压（Bus Voltage），连续模式（Continuous）。

<a id="ga88aa0c1378cfe356b643c89bf1418e3e"></a>

### `INA226_OPER_MODE_BUS_VOLTAGE_TRIG`

```c
#define INA226_OPER_MODE_BUS_VOLTAGE_TRIG 0x02
```

```c
#include <zephyr/dt-bindings/sensor/ina226.h>
```

总线电压（Bus Voltage），触发模式（Triggered）。

<a id="ga8780c1da54c2e5ae863efb7ef1b310b9"></a>

### `INA226_OPER_MODE_POWER_DOWN`

```c
#define INA226_OPER_MODE_POWER_DOWN 0x00
```

```c
#include <zephyr/dt-bindings/sensor/ina226.h>
```

掉电（Power-down）。

<a id="gaba344632242e46fcd392eaf7f114f820"></a>

### `INA226_OPER_MODE_SHUNT_BUS_VOLTAGE_CONT`

```c
#define INA226_OPER_MODE_SHUNT_BUS_VOLTAGE_CONT 0x07
```

```c
#include <zephyr/dt-bindings/sensor/ina226.h>
```

分流电阻电压与总线电压（Shunt and Bus），连续模式（Continuous）。

<a id="ga7e88c1ab79bed8425f3074b37903113b"></a>

### `INA226_OPER_MODE_SHUNT_BUS_VOLTAGE_TRIG`

```c
#define INA226_OPER_MODE_SHUNT_BUS_VOLTAGE_TRIG 0x03
```

```c
#include <zephyr/dt-bindings/sensor/ina226.h>
```

分流电阻电压与总线电压（Shunt and Bus），触发模式（Triggered）。

<a id="gafad378147deb5e1789a40e5dd7611de9"></a>

### `INA226_OPER_MODE_SHUNT_VOLTAGE_CONT`

```c
#define INA226_OPER_MODE_SHUNT_VOLTAGE_CONT 0x05
```

```c
#include <zephyr/dt-bindings/sensor/ina226.h>
```

分流电阻电压（Shunt Voltage），连续模式（Continuous）。

<a id="gaed00293346e09e6ef3114dd3167d1ce5"></a>

### `INA226_OPER_MODE_SHUNT_VOLTAGE_TRIG`

```c
#define INA226_OPER_MODE_SHUNT_VOLTAGE_TRIG 0x01
```

```c
#include <zephyr/dt-bindings/sensor/ina226.h>
```

分流电阻电压（Shunt Voltage），触发模式（Triggered）。

<a id="ga8174524d294a89bcedeec335538cc373"></a>

### `INA226_RST_NORMAL_OPERATION`

```c
#define INA226_RST_NORMAL_OPERATION 0x00
```

```c
#include <zephyr/dt-bindings/sensor/ina226.h>
```

正常运行（Normal Operation）。

<a id="ga1369ecef1266f83dd93f970002ff61b7"></a>

### `INA226_RST_SYSTEM_RESET`

```c
#define INA226_RST_SYSTEM_RESET 0x01
```

```c
#include <zephyr/dt-bindings/sensor/ina226.h>
```

触发系统复位（System Reset）。


## 7.7\_原页交叉引用（Cross References）

- [ina226.h](https://docs.zephyrproject.org/latest/doxygen/html/ina226_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P006_NXP i.MX952电源域（Power Domains）.md) · [返回大纲](大纲.md) · [下一章](P008_BCM283x 中断控制器（Interrupt controllers）.md)
