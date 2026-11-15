---
id: learning.zephyr-docs.api-memory-network-topic-reference.page-14
title: INA237 API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_INA237 API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Texas Instruments INA237 电流与功率监测器。

<a id="details"></a>

Texas Instruments INA237 电流与功率监测器。

<a id="header-files"></a>
<a id="files"></a>

## 14.1\_文件（Files）

<a id="r_ina237_2Eh"></a>

```c
file ina237.h
```

相关声明：[ina237.h](../api_file_clock_network_reference/P014_zephyr__dt-bindings__sensor__ina237.h_文件参考.md)。

the TI INA237 power monitor的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 14.2\_宏定义（Macros）

<a id="r_ga721c648626cab01daf4013fc199aead4"></a>

```c
#define INA237_CONFIG(rst_mode, convdly, adc_range)
```

相关声明：[INA237_CONFIG](#ga721c648626cab01daf4013fc199aead4)。

构建 INA237 配置寄存器值（Configuration Register Value）。

<a id="r_ga7310c76dac4ff27046970be6b24caa59"></a>

```c
#define INA237_ADC_CONFIG(mode, vshct, vbusct, vtct, avg)
```

相关声明：[INA237_ADC_CONFIG](#ga7310c76dac4ff27046970be6b24caa59)。

构建 INA237 ADC 配置寄存器值（ADC Configuration Register Value）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 14.3\_工作模式（Operating mode）

INA237_ADC_CONFIG() 宏的工作模式参数（Operating-mode Argument）。

<a id="r_ga829d7aa6a07bad8da2583a648b6c0be9"></a>

```c
#define INA237_CFG_HIGH_PRECISION BIT(4)
```

相关声明：[INA237_CFG_HIGH_PRECISION](#ga829d7aa6a07bad8da2583a648b6c0be9)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

高精度模式标志（High-precision Mode Flag）。

<a id="r_gab42708837c802141acc358a385f6c5df"></a>

```c
#define INA237_OPER_MODE_SHUTDOWN 0x00
```

相关声明：[INA237_OPER_MODE_SHUTDOWN](#gab42708837c802141acc358a385f6c5df)。

关断（Shutdown）。

<a id="r_ga6ed1315d8bd3eaa1c73fd398e9ce1c62"></a>

```c
#define INA237_OPER_MODE_BUS_VOLTAGE_TRIG 0x01
```

相关声明：[INA237_OPER_MODE_BUS_VOLTAGE_TRIG](#ga6ed1315d8bd3eaa1c73fd398e9ce1c62)。

总线电压（Bus Voltage），触发模式（Triggered）。

<a id="r_ga90c2ca6edab1e6940a37026ca45d38cf"></a>

```c
#define INA237_OPER_MODE_SHUNT_VOLTAGE_TRIG 0x02
```

相关声明：[INA237_OPER_MODE_SHUNT_VOLTAGE_TRIG](#ga90c2ca6edab1e6940a37026ca45d38cf)。

分流电阻电压（Shunt Voltage），触发模式（Triggered）。

<a id="r_ga2313b32f90362ff4f0be94c813c2d915"></a>

```c
#define INA237_OPER_MODE_SHUNT_BUS_VOLTAGE_TRIG 0x03
```

相关声明：[INA237_OPER_MODE_SHUNT_BUS_VOLTAGE_TRIG](#ga2313b32f90362ff4f0be94c813c2d915)。

分流电阻电压与总线电压（Shunt and Bus），触发模式（Triggered）。

<a id="r_gaf48a2674ff69fe726f3161962afb5172"></a>

```c
#define INA237_OPER_MODE_TEMP_TRIG 0x04
```

相关声明：[INA237_OPER_MODE_TEMP_TRIG](#gaf48a2674ff69fe726f3161962afb5172)。

温度，触发模式（Temperature, Triggered）。

<a id="r_ga61bd0c9161348b93c1b781324de3b20f"></a>

```c
#define INA237_OPER_MODE_TEMP_BUS_VOLTAGE_TRIG 0x05
```

相关声明：[INA237_OPER_MODE_TEMP_BUS_VOLTAGE_TRIG](#ga61bd0c9161348b93c1b781324de3b20f)。

温度与总线，触发模式（Temp and Bus, Triggered）。

<a id="r_ga8a83cbfc8a517d8dc696431134f55b8a"></a>

```c
#define INA237_OPER_MODE_TEMP_SHUNT_VOLTAGE_TRIG 0x06
```

相关声明：[INA237_OPER_MODE_TEMP_SHUNT_VOLTAGE_TRIG](#ga8a83cbfc8a517d8dc696431134f55b8a)。

温度与分流器，触发模式（Temp and Shunt, Triggered）。

<a id="r_ga5f524151fa6b5583add8522337aa275b"></a>

```c
#define INA237_OPER_MODE_BUS_SHUNT_VOLTAGE_TEMP_TRIG 0x07
```

相关声明：[INA237_OPER_MODE_BUS_SHUNT_VOLTAGE_TEMP_TRIG](#ga5f524151fa6b5583add8522337aa275b)。

总线、分流器与温度，触发模式（Bus, Shunt and Temp, Triggered）。

<a id="r_ga4a6874ebe2fa43ab99812d4de4d6b2c1"></a>

```c
#define INA237_OPER_MODE_BUS_VOLTAGE_CONT 0x09
```

相关声明：[INA237_OPER_MODE_BUS_VOLTAGE_CONT](#ga4a6874ebe2fa43ab99812d4de4d6b2c1)。

总线电压（Bus Voltage），连续模式（Continuous）。

<a id="r_gae24188265ba63cd1b947585ea96efa42"></a>

```c
#define INA237_OPER_MODE_SHUNT_VOLTAGE_CONT 0x0A
```

相关声明：[INA237_OPER_MODE_SHUNT_VOLTAGE_CONT](#gae24188265ba63cd1b947585ea96efa42)。

分流电阻电压（Shunt Voltage），连续模式（Continuous）。

<a id="r_ga75919399317285114b63746e41fa9aae"></a>

```c
#define INA237_OPER_MODE_SHUNT_BUS_VOLTAGE_CONT 0x0B
```

相关声明：[INA237_OPER_MODE_SHUNT_BUS_VOLTAGE_CONT](#ga75919399317285114b63746e41fa9aae)。

分流电阻电压与总线电压（Shunt and Bus），连续模式（Continuous）。

<a id="r_ga96afd10c7f0e435cdef6a999295afae5"></a>

```c
#define INA237_OPER_MODE_TEMP_CONT 0x0C
```

相关声明：[INA237_OPER_MODE_TEMP_CONT](#ga96afd10c7f0e435cdef6a999295afae5)。

温度，连续模式（Temperature, Continuous）。

<a id="r_ga51366870d0ef5c451ffdc92adf462b80"></a>

```c
#define INA237_OPER_MODE_BUS_VOLTAGE_TEMP_CONT 0x0D
```

相关声明：[INA237_OPER_MODE_BUS_VOLTAGE_TEMP_CONT](#ga51366870d0ef5c451ffdc92adf462b80)。

总线与温度，连续模式（Bus and Temp, Continuous）。

<a id="r_ga51142226eb02138a1462b32e6a6b9c3d"></a>

```c
#define INA237_OPER_MODE_TEMP_SHUNT_VOLTAGE_CONT 0x0E
```

相关声明：[INA237_OPER_MODE_TEMP_SHUNT_VOLTAGE_CONT](#ga51142226eb02138a1462b32e6a6b9c3d)。

温度与分流器，连续模式（Temp and Shunt, Continuous）。

<a id="r_ga5cfe6bc07b3dff06c2eefc3f73101289"></a>

```c
#define INA237_OPER_MODE_BUS_SHUNT_VOLTAGE_TEMP_CONT 0x0F
```

相关声明：[INA237_OPER_MODE_BUS_SHUNT_VOLTAGE_TEMP_CONT](#ga5cfe6bc07b3dff06c2eefc3f73101289)。

总线、分流器与温度，连续模式（Bus, Shunt and Temp, Continuous）。

## 14.4\_总线、分流器与温度转换时间（Bus, Shunt and Temperature Conversion Time）

INA237_ADC_CONFIG() 宏的转换时间参数（Conversion-time Argument）。

<a id="r_ga4c283158c66d3492efcbcb05bc797f43"></a>

```c
#define INA237_CONV_TIME_50 0x00
```

相关声明：[INA237_CONV_TIME_50](#ga4c283158c66d3492efcbcb05bc797f43)。

转换时间（Conversion Time）：50 µs。

<a id="r_gafa48d1d9aab85913e75d4413ca0ade61"></a>

```c
#define INA237_CONV_TIME_84 0x01
```

相关声明：[INA237_CONV_TIME_84](#gafa48d1d9aab85913e75d4413ca0ade61)。

转换时间（Conversion Time）：84 µs。

<a id="r_ga1f9505d58321c288af4324577c98b722"></a>

```c
#define INA237_CONV_TIME_150 0x02
```

相关声明：[INA237_CONV_TIME_150](#ga1f9505d58321c288af4324577c98b722)。

转换时间（Conversion Time）：150 µs。

<a id="r_ga37f20de30929ec2aab29568799d03ba9"></a>

```c
#define INA237_CONV_TIME_280 0x03
```

相关声明：[INA237_CONV_TIME_280](#ga37f20de30929ec2aab29568799d03ba9)。

转换时间（Conversion Time）：280 µs。

<a id="r_gadfe72090337a08de1e334ecec1a83cd2"></a>

```c
#define INA237_CONV_TIME_540 0x04
```

相关声明：[INA237_CONV_TIME_540](#gadfe72090337a08de1e334ecec1a83cd2)。

转换时间（Conversion Time）：540 µs。

<a id="r_ga0c59baa9f6713fb4b651876934babca6"></a>

```c
#define INA237_CONV_TIME_1052 0x05
```

相关声明：[INA237_CONV_TIME_1052](#ga0c59baa9f6713fb4b651876934babca6)。

转换时间（Conversion Time）：1052 µs。

<a id="r_ga73f063d5afcc5956769b1027a8ee7b6d"></a>

```c
#define INA237_CONV_TIME_2074 0x06
```

相关声明：[INA237_CONV_TIME_2074](#ga73f063d5afcc5956769b1027a8ee7b6d)。

转换时间（Conversion Time）：2074 µs。

<a id="r_ga5492b364f79ed890f67b6bc3b51b10ee"></a>

```c
#define INA237_CONV_TIME_4120 0x07
```

相关声明：[INA237_CONV_TIME_4120](#ga5492b364f79ed890f67b6bc3b51b10ee)。

转换时间（Conversion Time）：4120 µs。

## 14.5\_平均模式：采样数（Averaging Mode, Number of Samples）

INA237_ADC_CONFIG() 宏的平均模式参数（Averaging-mode Argument）。

<a id="r_ga3c84d5be0bbca9a23fa823b5d0d01a33"></a>

```c
#define INA237_AVG_MODE_1 0x00
```

相关声明：[INA237_AVG_MODE_1](#ga3c84d5be0bbca9a23fa823b5d0d01a33)。

1 个采样（Samples）。

<a id="r_ga4877129f08b10b594e05372a92e19987"></a>

```c
#define INA237_AVG_MODE_4 0x01
```

相关声明：[INA237_AVG_MODE_4](#ga4877129f08b10b594e05372a92e19987)。

4 个样本（Samples）。

<a id="r_ga3e199273cf3f18cd35cf0cc71f54d395"></a>

```c
#define INA237_AVG_MODE_16 0x02
```

相关声明：[INA237_AVG_MODE_16](#ga3e199273cf3f18cd35cf0cc71f54d395)。

16 个样本（Samples）。

<a id="r_gaa1754bb85646932d2e3d269c6585fc4e"></a>

```c
#define INA237_AVG_MODE_64 0x03
```

相关声明：[INA237_AVG_MODE_64](#gaa1754bb85646932d2e3d269c6585fc4e)。

64 个样本（Samples）。

<a id="r_ga1501acf37a027128d62037757140c84a"></a>

```c
#define INA237_AVG_MODE_128 0x04
```

相关声明：[INA237_AVG_MODE_128](#ga1501acf37a027128d62037757140c84a)。

128 个样本（Samples）。

<a id="r_ga88f55660b69e5620ea60c3a53fafb170"></a>

```c
#define INA237_AVG_MODE_256 0x05
```

相关声明：[INA237_AVG_MODE_256](#ga88f55660b69e5620ea60c3a53fafb170)。

256 个样本（Samples）。

<a id="r_ga8f7c1aad6dd88132e5d791788eb96055"></a>

```c
#define INA237_AVG_MODE_512 0x06
```

相关声明：[INA237_AVG_MODE_512](#ga8f7c1aad6dd88132e5d791788eb96055)。

512 个样本（Samples）。

<a id="r_ga692ea64b27f36b455e361ff9f20eacc9"></a>

```c
#define INA237_AVG_MODE_1024 0x07
```

相关声明：[INA237_AVG_MODE_1024](#ga692ea64b27f36b455e361ff9f20eacc9)。

1024 个采样（Samples）。

## 14.6\_复位模式（Reset Mode）

INA237_CONFIG() 宏的复位模式参数（Reset-mode Argument）。

<a id="r_ga21d67009b5359d2408bcf8c2bfc7bd01"></a>

```c
#define INA237_RST_NORMAL_OPERATION 0x00
```

相关声明：[INA237_RST_NORMAL_OPERATION](#ga21d67009b5359d2408bcf8c2bfc7bd01)。

正常运行（Normal Operation）。

<a id="r_ga79451943b97ee1146c536838b687f926"></a>

```c
#define INA237_RST_SYSTEM_RESET 0x01
```

相关声明：[INA237_RST_SYSTEM_RESET](#ga79451943b97ee1146c536838b687f926)。

触发系统复位（System Reset）。

## 14.7\_初始 ADC 转换延迟（Initial ADC Conversion Delay，步进 2 ms）

INA237_CONFIG() 宏的初始 ADC 延迟参数（Initial ADC-delay Argument）。

<a id="r_ga9bda801d1ba220808ee7bc7cadb4e1a8"></a>

```c
#define INA237_INIT_ADC_DELAY_0_S 0x00
```

相关声明：[INA237_INIT_ADC_DELAY_0_S](#ga9bda801d1ba220808ee7bc7cadb4e1a8)。

0 s，即无延迟（No Delay）。

<a id="r_ga726c19fef618b0b81219b569e3dc318a"></a>

```c
#define INA237_INIT_ADC_DELAY_2_MS 0x01
```

相关声明：[INA237_INIT_ADC_DELAY_2_MS](#ga726c19fef618b0b81219b569e3dc318a)。

2 ms（毫秒）。

<a id="r_gac088479421d24217c570770466f50b4b"></a>

```c
#define INA237_INIT_ADC_DELAY_510_MS 0xFF
```

相关声明：[INA237_INIT_ADC_DELAY_510_MS](#gac088479421d24217c570770466f50b4b)。

延迟（Delay）：510 ms。

## 14.8\_IN+ 与 IN− 之间的分流器满量程范围（Shunt Full-scale Range）

INA237_CONFIG() 宏的分流器满量程范围参数（Shunt Full-scale Range Argument）。

<a id="r_ga5afae9b977793fb53823085c83986bb6"></a>

```c
#define INA237_ADC_RANGE_163_84 0x00
```

相关声明：[INA237_ADC_RANGE_163_84](#ga5afae9b977793fb53823085c83986bb6)。

量程（Range）：±163.84 mV。

<a id="r_gae1c622a578b919b83781d3bc78429009"></a>

```c
#define INA237_ADC_RANGE_40_96 0x01
```

相关声明：[INA237_ADC_RANGE_40_96](#gae1c622a578b919b83781d3bc78429009)。

量程（Range）：±40.96 mV。

## 14.9\_详细说明（Detailed Documentation）

<a id="ga7310c76dac4ff27046970be6b24caa59"></a>

### `INA237_ADC_CONFIG`

```c
#define INA237_ADC_CONFIG ( mode, vshct, vbusct, vtct, avg )
```

```c
#include <zephyr/dt-bindings/sensor/ina237.h>
```

展开值（Value）：

```c
(((mode) << 12) | ((vbusct) << 9) | ((vshct) << 6) | ((vtct) << 3) | (avg))
```

构建 INA237 ADC 配置寄存器值（ADC Configuration Register Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mode` | 工作模式（Operating Mode），参见 ina237_oper_mode。 |
| `vshct` | 分流器电压转换时间（Shunt Voltage Conversion Time），参见 ina237_conv_time。 |
| `vbusct` | 总线电压转换时间（Bus Voltage Conversion Time），参见 ina237_conv_time。 |
| `vtct` | 温度转换时间（Temperature Conversion Time），参见 ina237_conv_time。 |
| `avg` | 平均模式（Averaging Mode），参见 ina237_avg。 |

<a id="ga5afae9b977793fb53823085c83986bb6"></a>

### `INA237_ADC_RANGE_163_84`

```c
#define INA237_ADC_RANGE_163_84 0x00
```

```c
#include <zephyr/dt-bindings/sensor/ina237.h>
```

量程（Range）：±163.84 mV。

<a id="gae1c622a578b919b83781d3bc78429009"></a>

### `INA237_ADC_RANGE_40_96`

```c
#define INA237_ADC_RANGE_40_96 0x01
```

```c
#include <zephyr/dt-bindings/sensor/ina237.h>
```

量程（Range）：±40.96 mV。

<a id="ga3c84d5be0bbca9a23fa823b5d0d01a33"></a>

### `INA237_AVG_MODE_1`

```c
#define INA237_AVG_MODE_1 0x00
```

```c
#include <zephyr/dt-bindings/sensor/ina237.h>
```

1 个采样（Samples）。

<a id="ga692ea64b27f36b455e361ff9f20eacc9"></a>

### `INA237_AVG_MODE_1024`

```c
#define INA237_AVG_MODE_1024 0x07
```

```c
#include <zephyr/dt-bindings/sensor/ina237.h>
```

1024 个采样（Samples）。

<a id="ga1501acf37a027128d62037757140c84a"></a>

### `INA237_AVG_MODE_128`

```c
#define INA237_AVG_MODE_128 0x04
```

```c
#include <zephyr/dt-bindings/sensor/ina237.h>
```

128 个样本（Samples）。

<a id="ga3e199273cf3f18cd35cf0cc71f54d395"></a>

### `INA237_AVG_MODE_16`

```c
#define INA237_AVG_MODE_16 0x02
```

```c
#include <zephyr/dt-bindings/sensor/ina237.h>
```

16 个样本（Samples）。

<a id="ga88f55660b69e5620ea60c3a53fafb170"></a>

### `INA237_AVG_MODE_256`

```c
#define INA237_AVG_MODE_256 0x05
```

```c
#include <zephyr/dt-bindings/sensor/ina237.h>
```

256 个样本（Samples）。

<a id="ga4877129f08b10b594e05372a92e19987"></a>

### `INA237_AVG_MODE_4`

```c
#define INA237_AVG_MODE_4 0x01
```

```c
#include <zephyr/dt-bindings/sensor/ina237.h>
```

4 个样本（Samples）。

<a id="ga8f7c1aad6dd88132e5d791788eb96055"></a>

### `INA237_AVG_MODE_512`

```c
#define INA237_AVG_MODE_512 0x06
```

```c
#include <zephyr/dt-bindings/sensor/ina237.h>
```

512 个样本（Samples）。

<a id="gaa1754bb85646932d2e3d269c6585fc4e"></a>

### `INA237_AVG_MODE_64`

```c
#define INA237_AVG_MODE_64 0x03
```

```c
#include <zephyr/dt-bindings/sensor/ina237.h>
```

64 个样本（Samples）。

<a id="ga829d7aa6a07bad8da2583a648b6c0be9"></a>

### `INA237_CFG_HIGH_PRECISION`

```c
#define INA237_CFG_HIGH_PRECISION BIT(4)
```

```c
#include <zephyr/dt-bindings/sensor/ina237.h>
```

高精度模式标志（High-precision Mode Flag）。

<a id="ga721c648626cab01daf4013fc199aead4"></a>

### `INA237_CONFIG`

```c
#define INA237_CONFIG ( rst_mode, convdly, adc_range )
```

```c
#include <zephyr/dt-bindings/sensor/ina237.h>
```

展开值（Value）：

```c
(((rst_mode) << 15) | ((convdly) << 6) | ((adc_range) << 4))
```

构建 INA237 配置寄存器值（Configuration Register Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `rst_mode` | 复位模式（Reset Mode），参见 ina237_reset。 |
| `convdly` | 初始 ADC 转换延迟（Initial ADC Conversion Delay），参见 ina237_init_adc_delay。 |
| `adc_range` | 分流器满量程范围（Shunt Full-scale Range），参见 ina237_adc_range。 |

<a id="ga0c59baa9f6713fb4b651876934babca6"></a>

### `INA237_CONV_TIME_1052`

```c
#define INA237_CONV_TIME_1052 0x05
```

```c
#include <zephyr/dt-bindings/sensor/ina237.h>
```

转换时间（Conversion Time）：1052 µs。

<a id="ga1f9505d58321c288af4324577c98b722"></a>

### `INA237_CONV_TIME_150`

```c
#define INA237_CONV_TIME_150 0x02
```

```c
#include <zephyr/dt-bindings/sensor/ina237.h>
```

转换时间（Conversion Time）：150 µs。

<a id="ga73f063d5afcc5956769b1027a8ee7b6d"></a>

### `INA237_CONV_TIME_2074`

```c
#define INA237_CONV_TIME_2074 0x06
```

```c
#include <zephyr/dt-bindings/sensor/ina237.h>
```

转换时间（Conversion Time）：2074 µs。

<a id="ga37f20de30929ec2aab29568799d03ba9"></a>

### `INA237_CONV_TIME_280`

```c
#define INA237_CONV_TIME_280 0x03
```

```c
#include <zephyr/dt-bindings/sensor/ina237.h>
```

转换时间（Conversion Time）：280 µs。

<a id="ga5492b364f79ed890f67b6bc3b51b10ee"></a>

### `INA237_CONV_TIME_4120`

```c
#define INA237_CONV_TIME_4120 0x07
```

```c
#include <zephyr/dt-bindings/sensor/ina237.h>
```

转换时间（Conversion Time）：4120 µs。

<a id="ga4c283158c66d3492efcbcb05bc797f43"></a>

### `INA237_CONV_TIME_50`

```c
#define INA237_CONV_TIME_50 0x00
```

```c
#include <zephyr/dt-bindings/sensor/ina237.h>
```

转换时间（Conversion Time）：50 µs。

<a id="gadfe72090337a08de1e334ecec1a83cd2"></a>

### `INA237_CONV_TIME_540`

```c
#define INA237_CONV_TIME_540 0x04
```

```c
#include <zephyr/dt-bindings/sensor/ina237.h>
```

转换时间（Conversion Time）：540 µs。

<a id="gafa48d1d9aab85913e75d4413ca0ade61"></a>

### `INA237_CONV_TIME_84`

```c
#define INA237_CONV_TIME_84 0x01
```

```c
#include <zephyr/dt-bindings/sensor/ina237.h>
```

转换时间（Conversion Time）：84 µs。

<a id="ga9bda801d1ba220808ee7bc7cadb4e1a8"></a>

### `INA237_INIT_ADC_DELAY_0_S`

```c
#define INA237_INIT_ADC_DELAY_0_S 0x00
```

```c
#include <zephyr/dt-bindings/sensor/ina237.h>
```

0 s，即无延迟（No Delay）。

<a id="ga726c19fef618b0b81219b569e3dc318a"></a>

### `INA237_INIT_ADC_DELAY_2_MS`

```c
#define INA237_INIT_ADC_DELAY_2_MS 0x01
```

```c
#include <zephyr/dt-bindings/sensor/ina237.h>
```

2 ms（毫秒）。

<a id="gac088479421d24217c570770466f50b4b"></a>

### `INA237_INIT_ADC_DELAY_510_MS`

```c
#define INA237_INIT_ADC_DELAY_510_MS 0xFF
```

```c
#include <zephyr/dt-bindings/sensor/ina237.h>
```

延迟（Delay）：510 ms。

<a id="ga5cfe6bc07b3dff06c2eefc3f73101289"></a>

### `INA237_OPER_MODE_BUS_SHUNT_VOLTAGE_TEMP_CONT`

```c
#define INA237_OPER_MODE_BUS_SHUNT_VOLTAGE_TEMP_CONT 0x0F
```

```c
#include <zephyr/dt-bindings/sensor/ina237.h>
```

总线、分流器与温度，连续模式（Bus, Shunt and Temp, Continuous）。

<a id="ga5f524151fa6b5583add8522337aa275b"></a>

### `INA237_OPER_MODE_BUS_SHUNT_VOLTAGE_TEMP_TRIG`

```c
#define INA237_OPER_MODE_BUS_SHUNT_VOLTAGE_TEMP_TRIG 0x07
```

```c
#include <zephyr/dt-bindings/sensor/ina237.h>
```

总线、分流器与温度，触发模式（Bus, Shunt and Temp, Triggered）。

<a id="ga4a6874ebe2fa43ab99812d4de4d6b2c1"></a>

### `INA237_OPER_MODE_BUS_VOLTAGE_CONT`

```c
#define INA237_OPER_MODE_BUS_VOLTAGE_CONT 0x09
```

```c
#include <zephyr/dt-bindings/sensor/ina237.h>
```

总线电压（Bus Voltage），连续模式（Continuous）。

<a id="ga51366870d0ef5c451ffdc92adf462b80"></a>

### `INA237_OPER_MODE_BUS_VOLTAGE_TEMP_CONT`

```c
#define INA237_OPER_MODE_BUS_VOLTAGE_TEMP_CONT 0x0D
```

```c
#include <zephyr/dt-bindings/sensor/ina237.h>
```

总线与温度，连续模式（Bus and Temp, Continuous）。

<a id="ga6ed1315d8bd3eaa1c73fd398e9ce1c62"></a>

### `INA237_OPER_MODE_BUS_VOLTAGE_TRIG`

```c
#define INA237_OPER_MODE_BUS_VOLTAGE_TRIG 0x01
```

```c
#include <zephyr/dt-bindings/sensor/ina237.h>
```

总线电压（Bus Voltage），触发模式（Triggered）。

<a id="ga75919399317285114b63746e41fa9aae"></a>

### `INA237_OPER_MODE_SHUNT_BUS_VOLTAGE_CONT`

```c
#define INA237_OPER_MODE_SHUNT_BUS_VOLTAGE_CONT 0x0B
```

```c
#include <zephyr/dt-bindings/sensor/ina237.h>
```

分流电阻电压与总线电压（Shunt and Bus），连续模式（Continuous）。

<a id="ga2313b32f90362ff4f0be94c813c2d915"></a>

### `INA237_OPER_MODE_SHUNT_BUS_VOLTAGE_TRIG`

```c
#define INA237_OPER_MODE_SHUNT_BUS_VOLTAGE_TRIG 0x03
```

```c
#include <zephyr/dt-bindings/sensor/ina237.h>
```

分流电阻电压与总线电压（Shunt and Bus），触发模式（Triggered）。

<a id="gae24188265ba63cd1b947585ea96efa42"></a>

### `INA237_OPER_MODE_SHUNT_VOLTAGE_CONT`

```c
#define INA237_OPER_MODE_SHUNT_VOLTAGE_CONT 0x0A
```

```c
#include <zephyr/dt-bindings/sensor/ina237.h>
```

分流电阻电压（Shunt Voltage），连续模式（Continuous）。

<a id="ga90c2ca6edab1e6940a37026ca45d38cf"></a>

### `INA237_OPER_MODE_SHUNT_VOLTAGE_TRIG`

```c
#define INA237_OPER_MODE_SHUNT_VOLTAGE_TRIG 0x02
```

```c
#include <zephyr/dt-bindings/sensor/ina237.h>
```

分流电阻电压（Shunt Voltage），触发模式（Triggered）。

<a id="gab42708837c802141acc358a385f6c5df"></a>

### `INA237_OPER_MODE_SHUTDOWN`

```c
#define INA237_OPER_MODE_SHUTDOWN 0x00
```

```c
#include <zephyr/dt-bindings/sensor/ina237.h>
```

关断（Shutdown）。

<a id="ga61bd0c9161348b93c1b781324de3b20f"></a>

### `INA237_OPER_MODE_TEMP_BUS_VOLTAGE_TRIG`

```c
#define INA237_OPER_MODE_TEMP_BUS_VOLTAGE_TRIG 0x05
```

```c
#include <zephyr/dt-bindings/sensor/ina237.h>
```

温度与总线，触发模式（Temp and Bus, Triggered）。

<a id="ga96afd10c7f0e435cdef6a999295afae5"></a>

### `INA237_OPER_MODE_TEMP_CONT`

```c
#define INA237_OPER_MODE_TEMP_CONT 0x0C
```

```c
#include <zephyr/dt-bindings/sensor/ina237.h>
```

温度，连续模式（Temperature, Continuous）。

<a id="ga51142226eb02138a1462b32e6a6b9c3d"></a>

### `INA237_OPER_MODE_TEMP_SHUNT_VOLTAGE_CONT`

```c
#define INA237_OPER_MODE_TEMP_SHUNT_VOLTAGE_CONT 0x0E
```

```c
#include <zephyr/dt-bindings/sensor/ina237.h>
```

温度与分流器，连续模式（Temp and Shunt, Continuous）。

<a id="ga8a83cbfc8a517d8dc696431134f55b8a"></a>

### `INA237_OPER_MODE_TEMP_SHUNT_VOLTAGE_TRIG`

```c
#define INA237_OPER_MODE_TEMP_SHUNT_VOLTAGE_TRIG 0x06
```

```c
#include <zephyr/dt-bindings/sensor/ina237.h>
```

温度与分流器，触发模式（Temp and Shunt, Triggered）。

<a id="gaf48a2674ff69fe726f3161962afb5172"></a>

### `INA237_OPER_MODE_TEMP_TRIG`

```c
#define INA237_OPER_MODE_TEMP_TRIG 0x04
```

```c
#include <zephyr/dt-bindings/sensor/ina237.h>
```

温度，触发模式（Temperature, Triggered）。

<a id="ga21d67009b5359d2408bcf8c2bfc7bd01"></a>

### `INA237_RST_NORMAL_OPERATION`

```c
#define INA237_RST_NORMAL_OPERATION 0x00
```

```c
#include <zephyr/dt-bindings/sensor/ina237.h>
```

正常运行（Normal Operation）。

<a id="ga79451943b97ee1146c536838b687f926"></a>

### `INA237_RST_SYSTEM_RESET`

```c
#define INA237_RST_SYSTEM_RESET 0x01
```

```c
#include <zephyr/dt-bindings/sensor/ina237.h>
```

触发系统复位（System Reset）。


## 14.10\_原页交叉引用（Cross References）

- [ina237.h](../api_file_clock_network_reference/P014_zephyr__dt-bindings__sensor__ina237.h_文件参考.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)

<a id="ina237_oper_mode"></a>
<a id="ina237_conv_time"></a>
<a id="ina237_avg"></a>
<a id="ina237_reset"></a>
<a id="ina237_init_adc_delay"></a>
<a id="ina237_adc_range"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P013_IEEE 802.15.4 网络管理（Net Management）.md) · [返回大纲](大纲.md) · [下一章](P015_内核内存管理（Kernel Memory Management）.md)
