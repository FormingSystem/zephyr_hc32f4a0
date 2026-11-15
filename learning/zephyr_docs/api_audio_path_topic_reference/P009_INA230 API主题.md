---
id: learning.zephyr-docs.api-audio-path-topic-reference.page-9
title: INA230 API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ina230__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_INA230 API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__ina230__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Texas Instruments INA230 电流与功率监测器。

<a id="details"></a>

Texas Instruments INA230 电流与功率监测器。

<a id="header-files"></a>
<a id="files"></a>

## 9.1\_文件（Files）

<a id="r_ina230_2Eh"></a>

```c
file ina230.h
```

相关声明：[ina230.h](../api_file_mesh_interrupt_reference/P013_zephyr__dt-bindings__sensor__ina230.h_文件参考.md)。

the TI INA230 power monitor的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 9.2\_宏定义（Macros）

<a id="r_ga0cda48f2739c01d3f0c25e7ba5249cb7"></a>

```c
#define INA230_CONFIG(mode, svct, bvct, avg)
```

相关声明：[INA230_CONFIG](#ga0cda48f2739c01d3f0c25e7ba5249cb7)。

构造 INA230 配置寄存器值（Configuration Register Value）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 9.3\_使 ALERT 引脚置为有效的屏蔽／使能位（Mask/Enable Bits）

使 ALERT 引脚置为有效的屏蔽／使能标志（Mask/Enable Flags）。

<a id="r_gac66cd3c1e640e40e03cfd0fa8eb6b553"></a>

```c
#define INA230_SHUNT_VOLTAGE_OVER BIT(15)
```

相关声明：[INA230_SHUNT_VOLTAGE_OVER](#gac66cd3c1e640e40e03cfd0fa8eb6b553)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

分流电阻电压超过上限（Shunt Voltage Over-limit）。

<a id="r_ga040092c7325a5466a46941a5313cc4e8"></a>

```c
#define INA230_SHUNT_VOLTAGE_UNDER BIT(14)
```

相关声明：[INA230_SHUNT_VOLTAGE_UNDER](#ga040092c7325a5466a46941a5313cc4e8)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

分流电阻电压低于下限（Shunt Voltage Under-limit）。

<a id="r_ga19e8853f4cd17ab415b0dff751019e61"></a>

```c
#define INA230_BUS_VOLTAGE_OVER BIT(13)
```

相关声明：[INA230_BUS_VOLTAGE_OVER](#ga19e8853f4cd17ab415b0dff751019e61)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

总线电压超过上限（Bus Voltage Over-limit）。

<a id="r_ga6358dc1460787287df8248b0ed304784"></a>

```c
#define INA230_BUS_VOLTAGE_UNDER BIT(12)
```

相关声明：[INA230_BUS_VOLTAGE_UNDER](#ga6358dc1460787287df8248b0ed304784)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

总线电压低于下限（Bus Voltage Under-limit）。

<a id="r_ga3b72c1af082ed974c74dfeabe6d8f15b"></a>

```c
#define INA230_OVER_LIMIT_POWER BIT(11)
```

相关声明：[INA230_OVER_LIMIT_POWER](#ga3b72c1af082ed974c74dfeabe6d8f15b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

功率超过上限（Power Over-limit）。

<a id="r_gaa789596e247090cd2829beafbbed6200"></a>

```c
#define INA230_CONVERSION_READY BIT(10)
```

相关声明：[INA230_CONVERSION_READY](#gaa789596e247090cd2829beafbbed6200)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

转换就绪使能（Conversion-ready Enable）。

<a id="r_ga168b1902c7fd80b20a63cc70653ce51a"></a>

```c
#define INA230_ALERT_FUNCTION_FLAG BIT(4)
```

相关声明：[INA230_ALERT_FUNCTION_FLAG](#ga168b1902c7fd80b20a63cc70653ce51a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

告警功能标志（Alert Function Flag）。

<a id="r_ga4985c309b299ca5b69afe92c127bba15"></a>

```c
#define INA230_CONVERSION_READY_FLAG BIT(3)
```

相关声明：[INA230_CONVERSION_READY_FLAG](#ga4985c309b299ca5b69afe92c127bba15)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

转换就绪标志（Conversion-ready Flag）。

<a id="r_ga0a34427f40f5100e98d3aed0e2d92c8f"></a>

```c
#define INA230_MATH_OVERFLOW_FLAG BIT(2)
```

相关声明：[INA230_MATH_OVERFLOW_FLAG](#ga0a34427f40f5100e98d3aed0e2d92c8f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

运算溢出标志（Math Overflow Flag）。

<a id="r_gaa97cd11f72647303d4ec67e49ef3739b"></a>

```c
#define INA230_ALERT_POLARITY BIT(1)
```

相关声明：[INA230_ALERT_POLARITY](#gaa97cd11f72647303d4ec67e49ef3739b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

告警引脚极性（Alert Pin Polarity）。

<a id="r_gaaeafbd49251d2c92f6cfb0f0fc067fc5"></a>

```c
#define INA230_ALERT_LATCH_ENABLE BIT(0)
```

相关声明：[INA230_ALERT_LATCH_ENABLE](#gaaeafbd49251d2c92f6cfb0f0fc067fc5)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

告警锁存使能（Alert Latch Enable）。

## 9.4\_工作模式（Operating mode）

`INA230_CONFIG()` 宏的工作模式参数（Operating-mode Argument）。

<a id="r_gacb3862f380fd234f8109cfc5c600a4d1"></a>

```c
#define INA230_OPER_MODE_POWER_DOWN 0x00
```

相关声明：[INA230_OPER_MODE_POWER_DOWN](#gacb3862f380fd234f8109cfc5c600a4d1)。

掉电（Power-down）。

<a id="r_ga40b158024fc20e70683b264c1b6a15c1"></a>

```c
#define INA230_OPER_MODE_SHUNT_VOLTAGE_TRIG 0x01
```

相关声明：[INA230_OPER_MODE_SHUNT_VOLTAGE_TRIG](#ga40b158024fc20e70683b264c1b6a15c1)。

分流电阻电压（Shunt Voltage），触发模式（Triggered）。

<a id="r_gabacc74f8d1e0890f566d7b8c26c0f999"></a>

```c
#define INA230_OPER_MODE_BUS_VOLTAGE_TRIG 0x02
```

相关声明：[INA230_OPER_MODE_BUS_VOLTAGE_TRIG](#gabacc74f8d1e0890f566d7b8c26c0f999)。

总线电压（Bus Voltage），触发模式（Triggered）。

<a id="r_ga20379c383fc0d36177719d2fd3083375"></a>

```c
#define INA230_OPER_MODE_SHUNT_BUS_VOLTAGE_TRIG 0x03
```

相关声明：[INA230_OPER_MODE_SHUNT_BUS_VOLTAGE_TRIG](#ga20379c383fc0d36177719d2fd3083375)。

分流电阻电压与总线电压（Shunt and Bus），触发模式（Triggered）。

<a id="r_ga0db3092938ca8768f1bdb2911499bd06"></a>

```c
#define INA230_OPER_MODE_SHUNT_VOLTAGE_CONT 0x05
```

相关声明：[INA230_OPER_MODE_SHUNT_VOLTAGE_CONT](#ga0db3092938ca8768f1bdb2911499bd06)。

分流电阻电压（Shunt Voltage），连续模式（Continuous）。

<a id="r_ga3c9319a04c00c3e8c4b3281be91c7274"></a>

```c
#define INA230_OPER_MODE_BUS_VOLTAGE_CONT 0x06
```

相关声明：[INA230_OPER_MODE_BUS_VOLTAGE_CONT](#ga3c9319a04c00c3e8c4b3281be91c7274)。

总线电压（Bus Voltage），连续模式（Continuous）。

<a id="r_ga8aa6b641d5304db934e97a9acc4e8185"></a>

```c
#define INA230_OPER_MODE_SHUNT_BUS_VOLTAGE_CONT 0x07
```

相关声明：[INA230_OPER_MODE_SHUNT_BUS_VOLTAGE_CONT](#ga8aa6b641d5304db934e97a9acc4e8185)。

分流电阻电压与总线电压（Shunt and Bus），连续模式（Continuous）。

## 9.5\_总线电压与分流电阻电压转换时间（Bus and Shunt Voltage Conversion Time）

`INA230_CONFIG()` 宏的转换时间参数（Conversion-time Argument）。

<a id="r_ga609d89e2e03f973897892086c58373b3"></a>

```c
#define INA230_CONV_TIME_140 0x00
```

相关声明：[INA230_CONV_TIME_140](#ga609d89e2e03f973897892086c58373b3)。

140 µs（微秒）。

<a id="r_ga3aaa2b4bbc38c2c6e813af488761d6fd"></a>

```c
#define INA230_CONV_TIME_204 0x01
```

相关声明：[INA230_CONV_TIME_204](#ga3aaa2b4bbc38c2c6e813af488761d6fd)。

204 µs（微秒）。

<a id="r_gafa298eb42a7ef83966d01f41d21694dd"></a>

```c
#define INA230_CONV_TIME_332 0x02
```

相关声明：[INA230_CONV_TIME_332](#gafa298eb42a7ef83966d01f41d21694dd)。

332 µs（微秒）。

<a id="r_ga38d12e2f397fb9606137dd3e8aa9a6d9"></a>

```c
#define INA230_CONV_TIME_588 0x03
```

相关声明：[INA230_CONV_TIME_588](#ga38d12e2f397fb9606137dd3e8aa9a6d9)。

588 µs（微秒）。

<a id="r_gaf3558b94073c94a4a51a18e1138b9d9d"></a>

```c
#define INA230_CONV_TIME_1100 0x04
```

相关声明：[INA230_CONV_TIME_1100](#gaf3558b94073c94a4a51a18e1138b9d9d)。

1100 µs（微秒）。

<a id="r_ga75fa32c27aa4e5759e7b3248536f1478"></a>

```c
#define INA230_CONV_TIME_2116 0x05
```

相关声明：[INA230_CONV_TIME_2116](#ga75fa32c27aa4e5759e7b3248536f1478)。

2116 µs（微秒）。

<a id="r_gada84f5fe71c258478085a519e55bb70c"></a>

```c
#define INA230_CONV_TIME_4156 0x06
```

相关声明：[INA230_CONV_TIME_4156](#gada84f5fe71c258478085a519e55bb70c)。

4156 µs（微秒）。

<a id="r_ga6ce6c967ffd224b2e0df7a41ee77979f"></a>

```c
#define INA230_CONV_TIME_8244 0x07
```

相关声明：[INA230_CONV_TIME_8244](#ga6ce6c967ffd224b2e0df7a41ee77979f)。

8244 µs（微秒）。

## 9.6\_平均模式：采样数（Averaging Mode, Number of Samples）

`INA230_CONFIG()` 宏的平均模式参数（Averaging-mode Argument）。

<a id="r_gaf6170f95a07663623351b693a76c772f"></a>

```c
#define INA230_AVG_MODE_1 0x00
```

相关声明：[INA230_AVG_MODE_1](#gaf6170f95a07663623351b693a76c772f)。

1 个采样（Samples）。

<a id="r_ga41491081f78b148c6776884d81e612be"></a>

```c
#define INA230_AVG_MODE_4 0x01
```

相关声明：[INA230_AVG_MODE_4](#ga41491081f78b148c6776884d81e612be)。

4 个样本（Samples）。

<a id="r_ga9a8f69817a981937f2c61ce89420f9db"></a>

```c
#define INA230_AVG_MODE_16 0x02
```

相关声明：[INA230_AVG_MODE_16](#ga9a8f69817a981937f2c61ce89420f9db)。

16 个样本（Samples）。

<a id="r_ga25553b578940087be9d6c61a1049fa51"></a>

```c
#define INA230_AVG_MODE_64 0x03
```

相关声明：[INA230_AVG_MODE_64](#ga25553b578940087be9d6c61a1049fa51)。

64 个样本（Samples）。

<a id="r_ga1fe17a0d83b831a9e66a41abe09576c6"></a>

```c
#define INA230_AVG_MODE_128 0x04
```

相关声明：[INA230_AVG_MODE_128](#ga1fe17a0d83b831a9e66a41abe09576c6)。

128 个样本（Samples）。

<a id="r_ga1a7c91438e80b95ba61a6096fbae569a"></a>

```c
#define INA230_AVG_MODE_256 0x05
```

相关声明：[INA230_AVG_MODE_256](#ga1a7c91438e80b95ba61a6096fbae569a)。

256 个样本（Samples）。

<a id="r_ga77be8bb5db31c9c610ea9e9b3a00285c"></a>

```c
#define INA230_AVG_MODE_512 0x06
```

相关声明：[INA230_AVG_MODE_512](#ga77be8bb5db31c9c610ea9e9b3a00285c)。

512 个样本（Samples）。

<a id="r_ga02ba7889aa1088a3e0038612b86a8401"></a>

```c
#define INA230_AVG_MODE_1024 0x07
```

相关声明：[INA230_AVG_MODE_1024](#ga02ba7889aa1088a3e0038612b86a8401)。

1024 个采样（Samples）。

## 9.7\_详细说明（Detailed Documentation）

<a id="ga168b1902c7fd80b20a63cc70653ce51a"></a>

### `INA230_ALERT_FUNCTION_FLAG`

```c
#define INA230_ALERT_FUNCTION_FLAG BIT(4)
```

```c
#include <zephyr/dt-bindings/sensor/ina230.h>
```

告警功能标志（Alert Function Flag）。

<a id="gaaeafbd49251d2c92f6cfb0f0fc067fc5"></a>

### `INA230_ALERT_LATCH_ENABLE`

```c
#define INA230_ALERT_LATCH_ENABLE BIT(0)
```

```c
#include <zephyr/dt-bindings/sensor/ina230.h>
```

告警锁存使能（Alert Latch Enable）。

<a id="gaa97cd11f72647303d4ec67e49ef3739b"></a>

### `INA230_ALERT_POLARITY`

```c
#define INA230_ALERT_POLARITY BIT(1)
```

```c
#include <zephyr/dt-bindings/sensor/ina230.h>
```

告警引脚极性（Alert Pin Polarity）。

<a id="gaf6170f95a07663623351b693a76c772f"></a>

### `INA230_AVG_MODE_1`

```c
#define INA230_AVG_MODE_1 0x00
```

```c
#include <zephyr/dt-bindings/sensor/ina230.h>
```

1 个采样（Samples）。

<a id="ga02ba7889aa1088a3e0038612b86a8401"></a>

### `INA230_AVG_MODE_1024`

```c
#define INA230_AVG_MODE_1024 0x07
```

```c
#include <zephyr/dt-bindings/sensor/ina230.h>
```

1024 个采样（Samples）。

<a id="ga1fe17a0d83b831a9e66a41abe09576c6"></a>

### `INA230_AVG_MODE_128`

```c
#define INA230_AVG_MODE_128 0x04
```

```c
#include <zephyr/dt-bindings/sensor/ina230.h>
```

128 个样本（Samples）。

<a id="ga9a8f69817a981937f2c61ce89420f9db"></a>

### `INA230_AVG_MODE_16`

```c
#define INA230_AVG_MODE_16 0x02
```

```c
#include <zephyr/dt-bindings/sensor/ina230.h>
```

16 个样本（Samples）。

<a id="ga1a7c91438e80b95ba61a6096fbae569a"></a>

### `INA230_AVG_MODE_256`

```c
#define INA230_AVG_MODE_256 0x05
```

```c
#include <zephyr/dt-bindings/sensor/ina230.h>
```

256 个样本（Samples）。

<a id="ga41491081f78b148c6776884d81e612be"></a>

### `INA230_AVG_MODE_4`

```c
#define INA230_AVG_MODE_4 0x01
```

```c
#include <zephyr/dt-bindings/sensor/ina230.h>
```

4 个样本（Samples）。

<a id="ga77be8bb5db31c9c610ea9e9b3a00285c"></a>

### `INA230_AVG_MODE_512`

```c
#define INA230_AVG_MODE_512 0x06
```

```c
#include <zephyr/dt-bindings/sensor/ina230.h>
```

512 个样本（Samples）。

<a id="ga25553b578940087be9d6c61a1049fa51"></a>

### `INA230_AVG_MODE_64`

```c
#define INA230_AVG_MODE_64 0x03
```

```c
#include <zephyr/dt-bindings/sensor/ina230.h>
```

64 个样本（Samples）。

<a id="ga19e8853f4cd17ab415b0dff751019e61"></a>

### `INA230_BUS_VOLTAGE_OVER`

```c
#define INA230_BUS_VOLTAGE_OVER BIT(13)
```

```c
#include <zephyr/dt-bindings/sensor/ina230.h>
```

总线电压超过上限（Bus Voltage Over-limit）。

<a id="ga6358dc1460787287df8248b0ed304784"></a>

### `INA230_BUS_VOLTAGE_UNDER`

```c
#define INA230_BUS_VOLTAGE_UNDER BIT(12)
```

```c
#include <zephyr/dt-bindings/sensor/ina230.h>
```

总线电压低于下限（Bus Voltage Under-limit）。

<a id="ga0cda48f2739c01d3f0c25e7ba5249cb7"></a>

### `INA230_CONFIG`

```c
#define INA230_CONFIG ( mode, svct, bvct, avg )
```

```c
#include <zephyr/dt-bindings/sensor/ina230.h>
```

展开值（Value）：

```c
(((avg) << 9) | ((bvct) << 6) | ((svct) << 3) | (mode))
```

构造 INA230 配置寄存器值（Configuration Register Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mode` | 工作模式（Operating Mode），参见 `ina230_oper_mode`。 |
| `svct` | 分流电阻电压转换时间（Shunt Voltage Conversion Time），参见 `ina230_conv_time`。 |
| `bvct` | 总线电压转换时间（Bus Voltage Conversion Time），参见 `ina230_conv_time`。 |
| `avg` | 平均模式（Averaging Mode），参见 `ina230_avg`。 |

<a id="gaf3558b94073c94a4a51a18e1138b9d9d"></a>

### `INA230_CONV_TIME_1100`

```c
#define INA230_CONV_TIME_1100 0x04
```

```c
#include <zephyr/dt-bindings/sensor/ina230.h>
```

1100 µs（微秒）。

<a id="ga609d89e2e03f973897892086c58373b3"></a>

### `INA230_CONV_TIME_140`

```c
#define INA230_CONV_TIME_140 0x00
```

```c
#include <zephyr/dt-bindings/sensor/ina230.h>
```

140 µs（微秒）。

<a id="ga3aaa2b4bbc38c2c6e813af488761d6fd"></a>

### `INA230_CONV_TIME_204`

```c
#define INA230_CONV_TIME_204 0x01
```

```c
#include <zephyr/dt-bindings/sensor/ina230.h>
```

204 µs（微秒）。

<a id="ga75fa32c27aa4e5759e7b3248536f1478"></a>

### `INA230_CONV_TIME_2116`

```c
#define INA230_CONV_TIME_2116 0x05
```

```c
#include <zephyr/dt-bindings/sensor/ina230.h>
```

2116 µs（微秒）。

<a id="gafa298eb42a7ef83966d01f41d21694dd"></a>

### `INA230_CONV_TIME_332`

```c
#define INA230_CONV_TIME_332 0x02
```

```c
#include <zephyr/dt-bindings/sensor/ina230.h>
```

332 µs（微秒）。

<a id="gada84f5fe71c258478085a519e55bb70c"></a>

### `INA230_CONV_TIME_4156`

```c
#define INA230_CONV_TIME_4156 0x06
```

```c
#include <zephyr/dt-bindings/sensor/ina230.h>
```

4156 µs（微秒）。

<a id="ga38d12e2f397fb9606137dd3e8aa9a6d9"></a>

### `INA230_CONV_TIME_588`

```c
#define INA230_CONV_TIME_588 0x03
```

```c
#include <zephyr/dt-bindings/sensor/ina230.h>
```

588 µs（微秒）。

<a id="ga6ce6c967ffd224b2e0df7a41ee77979f"></a>

### `INA230_CONV_TIME_8244`

```c
#define INA230_CONV_TIME_8244 0x07
```

```c
#include <zephyr/dt-bindings/sensor/ina230.h>
```

8244 µs（微秒）。

<a id="gaa789596e247090cd2829beafbbed6200"></a>

### `INA230_CONVERSION_READY`

```c
#define INA230_CONVERSION_READY BIT(10)
```

```c
#include <zephyr/dt-bindings/sensor/ina230.h>
```

转换就绪使能（Conversion-ready Enable）。

<a id="ga4985c309b299ca5b69afe92c127bba15"></a>

### `INA230_CONVERSION_READY_FLAG`

```c
#define INA230_CONVERSION_READY_FLAG BIT(3)
```

```c
#include <zephyr/dt-bindings/sensor/ina230.h>
```

转换就绪标志（Conversion-ready Flag）。

<a id="ga0a34427f40f5100e98d3aed0e2d92c8f"></a>

### `INA230_MATH_OVERFLOW_FLAG`

```c
#define INA230_MATH_OVERFLOW_FLAG BIT(2)
```

```c
#include <zephyr/dt-bindings/sensor/ina230.h>
```

运算溢出标志（Math Overflow Flag）。

<a id="ga3c9319a04c00c3e8c4b3281be91c7274"></a>

### `INA230_OPER_MODE_BUS_VOLTAGE_CONT`

```c
#define INA230_OPER_MODE_BUS_VOLTAGE_CONT 0x06
```

```c
#include <zephyr/dt-bindings/sensor/ina230.h>
```

总线电压（Bus Voltage），连续模式（Continuous）。

<a id="gabacc74f8d1e0890f566d7b8c26c0f999"></a>

### `INA230_OPER_MODE_BUS_VOLTAGE_TRIG`

```c
#define INA230_OPER_MODE_BUS_VOLTAGE_TRIG 0x02
```

```c
#include <zephyr/dt-bindings/sensor/ina230.h>
```

总线电压（Bus Voltage），触发模式（Triggered）。

<a id="gacb3862f380fd234f8109cfc5c600a4d1"></a>

### `INA230_OPER_MODE_POWER_DOWN`

```c
#define INA230_OPER_MODE_POWER_DOWN 0x00
```

```c
#include <zephyr/dt-bindings/sensor/ina230.h>
```

掉电（Power-down）。

<a id="ga8aa6b641d5304db934e97a9acc4e8185"></a>

### `INA230_OPER_MODE_SHUNT_BUS_VOLTAGE_CONT`

```c
#define INA230_OPER_MODE_SHUNT_BUS_VOLTAGE_CONT 0x07
```

```c
#include <zephyr/dt-bindings/sensor/ina230.h>
```

分流电阻电压与总线电压（Shunt and Bus），连续模式（Continuous）。

<a id="ga20379c383fc0d36177719d2fd3083375"></a>

### `INA230_OPER_MODE_SHUNT_BUS_VOLTAGE_TRIG`

```c
#define INA230_OPER_MODE_SHUNT_BUS_VOLTAGE_TRIG 0x03
```

```c
#include <zephyr/dt-bindings/sensor/ina230.h>
```

分流电阻电压与总线电压（Shunt and Bus），触发模式（Triggered）。

<a id="ga0db3092938ca8768f1bdb2911499bd06"></a>

### `INA230_OPER_MODE_SHUNT_VOLTAGE_CONT`

```c
#define INA230_OPER_MODE_SHUNT_VOLTAGE_CONT 0x05
```

```c
#include <zephyr/dt-bindings/sensor/ina230.h>
```

分流电阻电压（Shunt Voltage），连续模式（Continuous）。

<a id="ga40b158024fc20e70683b264c1b6a15c1"></a>

### `INA230_OPER_MODE_SHUNT_VOLTAGE_TRIG`

```c
#define INA230_OPER_MODE_SHUNT_VOLTAGE_TRIG 0x01
```

```c
#include <zephyr/dt-bindings/sensor/ina230.h>
```

分流电阻电压（Shunt Voltage），触发模式（Triggered）。

<a id="ga3b72c1af082ed974c74dfeabe6d8f15b"></a>

### `INA230_OVER_LIMIT_POWER`

```c
#define INA230_OVER_LIMIT_POWER BIT(11)
```

```c
#include <zephyr/dt-bindings/sensor/ina230.h>
```

功率超过上限（Power Over-limit）。

<a id="gac66cd3c1e640e40e03cfd0fa8eb6b553"></a>

### `INA230_SHUNT_VOLTAGE_OVER`

```c
#define INA230_SHUNT_VOLTAGE_OVER BIT(15)
```

```c
#include <zephyr/dt-bindings/sensor/ina230.h>
```

分流电阻电压超过上限（Shunt Voltage Over-limit）。

<a id="ga040092c7325a5466a46941a5313cc4e8"></a>

### `INA230_SHUNT_VOLTAGE_UNDER`

```c
#define INA230_SHUNT_VOLTAGE_UNDER BIT(14)
```

```c
#include <zephyr/dt-bindings/sensor/ina230.h>
```

分流电阻电压低于下限（Shunt Voltage Under-limit）。


## 9.8\_原页交叉引用（Cross References）

- [ina230.h](../api_file_mesh_interrupt_reference/P013_zephyr__dt-bindings__sensor__ina230.h_文件参考.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)

<a id="ina230_oper_mode"></a>
<a id="ina230_conv_time"></a>
<a id="ina230_avg"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P008_gPTP 支持.md) · [返回大纲](大纲.md) · [下一章](P010_LIS2DW12 API主题.md)
