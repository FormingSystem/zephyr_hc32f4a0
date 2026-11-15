---
id: learning.zephyr-docs.api-file-clock-network-reference.page-14
title: zephyr__dt-bindings__sensor__ina237.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ina237_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_zephyr\_\_dt-bindings\_\_sensor\_\_ina237.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ina237_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

the TI INA237 power monitor的设备树绑定常量（Devicetree Binding Constants）。

<a id="details"></a>

```c
#include <zephyr/dt-bindings/dt-util.h>
```

查看此文件的源码。

the TI INA237 power monitor的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 14.1\_宏定义（Macros）

<a id="r_ga721c648626cab01daf4013fc199aead4"></a>

```c
#define INA237_CONFIG(rst_mode, convdly, adc_range)
```

相关声明：[INA237_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga721c648626cab01daf4013fc199aead4)。

构建 INA237 配置寄存器值（Configuration Register Value）。

<a id="r_ga7310c76dac4ff27046970be6b24caa59"></a>

```c
#define INA237_ADC_CONFIG(mode, vshct, vbusct, vtct, avg)
```

相关声明：[INA237_ADC_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga7310c76dac4ff27046970be6b24caa59)。

构建 INA237 ADC 配置寄存器值（ADC Configuration Register Value）。

<a id="define-members-0"></a>

### 工作模式（Operating mode）

INA237_ADC_CONFIG() 宏的工作模式参数（Operating-mode Argument）。

<a id="r_ga829d7aa6a07bad8da2583a648b6c0be9"></a>

```c
#define INA237_CFG_HIGH_PRECISION BIT(4)
```

相关声明：[INA237_CFG_HIGH_PRECISION](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga829d7aa6a07bad8da2583a648b6c0be9)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

高精度模式标志（High-precision Mode Flag）。

<a id="r_gab42708837c802141acc358a385f6c5df"></a>

```c
#define INA237_OPER_MODE_SHUTDOWN 0x00
```

相关声明：[INA237_OPER_MODE_SHUTDOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#gab42708837c802141acc358a385f6c5df)。

关断（Shutdown）。

<a id="r_ga6ed1315d8bd3eaa1c73fd398e9ce1c62"></a>

```c
#define INA237_OPER_MODE_BUS_VOLTAGE_TRIG 0x01
```

相关声明：[INA237_OPER_MODE_BUS_VOLTAGE_TRIG](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga6ed1315d8bd3eaa1c73fd398e9ce1c62)。

总线电压（Bus Voltage），触发模式（Triggered）。

<a id="r_ga90c2ca6edab1e6940a37026ca45d38cf"></a>

```c
#define INA237_OPER_MODE_SHUNT_VOLTAGE_TRIG 0x02
```

相关声明：[INA237_OPER_MODE_SHUNT_VOLTAGE_TRIG](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga90c2ca6edab1e6940a37026ca45d38cf)。

分流电阻电压（Shunt Voltage），触发模式（Triggered）。

<a id="r_ga2313b32f90362ff4f0be94c813c2d915"></a>

```c
#define INA237_OPER_MODE_SHUNT_BUS_VOLTAGE_TRIG 0x03
```

相关声明：[INA237_OPER_MODE_SHUNT_BUS_VOLTAGE_TRIG](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga2313b32f90362ff4f0be94c813c2d915)。

分流电阻电压与总线电压（Shunt and Bus），触发模式（Triggered）。

<a id="r_gaf48a2674ff69fe726f3161962afb5172"></a>

```c
#define INA237_OPER_MODE_TEMP_TRIG 0x04
```

相关声明：[INA237_OPER_MODE_TEMP_TRIG](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#gaf48a2674ff69fe726f3161962afb5172)。

温度，触发模式（Temperature, Triggered）。

<a id="r_ga61bd0c9161348b93c1b781324de3b20f"></a>

```c
#define INA237_OPER_MODE_TEMP_BUS_VOLTAGE_TRIG 0x05
```

相关声明：[INA237_OPER_MODE_TEMP_BUS_VOLTAGE_TRIG](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga61bd0c9161348b93c1b781324de3b20f)。

温度与总线，触发模式（Temp and Bus, Triggered）。

<a id="r_ga8a83cbfc8a517d8dc696431134f55b8a"></a>

```c
#define INA237_OPER_MODE_TEMP_SHUNT_VOLTAGE_TRIG 0x06
```

相关声明：[INA237_OPER_MODE_TEMP_SHUNT_VOLTAGE_TRIG](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga8a83cbfc8a517d8dc696431134f55b8a)。

温度与分流器，触发模式（Temp and Shunt, Triggered）。

<a id="r_ga5f524151fa6b5583add8522337aa275b"></a>

```c
#define INA237_OPER_MODE_BUS_SHUNT_VOLTAGE_TEMP_TRIG 0x07
```

相关声明：[INA237_OPER_MODE_BUS_SHUNT_VOLTAGE_TEMP_TRIG](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga5f524151fa6b5583add8522337aa275b)。

总线、分流器与温度，触发模式（Bus, Shunt and Temp, Triggered）。

<a id="r_ga4a6874ebe2fa43ab99812d4de4d6b2c1"></a>

```c
#define INA237_OPER_MODE_BUS_VOLTAGE_CONT 0x09
```

相关声明：[INA237_OPER_MODE_BUS_VOLTAGE_CONT](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga4a6874ebe2fa43ab99812d4de4d6b2c1)。

总线电压（Bus Voltage），连续模式（Continuous）。

<a id="r_gae24188265ba63cd1b947585ea96efa42"></a>

```c
#define INA237_OPER_MODE_SHUNT_VOLTAGE_CONT 0x0A
```

相关声明：[INA237_OPER_MODE_SHUNT_VOLTAGE_CONT](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#gae24188265ba63cd1b947585ea96efa42)。

分流电阻电压（Shunt Voltage），连续模式（Continuous）。

<a id="r_ga75919399317285114b63746e41fa9aae"></a>

```c
#define INA237_OPER_MODE_SHUNT_BUS_VOLTAGE_CONT 0x0B
```

相关声明：[INA237_OPER_MODE_SHUNT_BUS_VOLTAGE_CONT](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga75919399317285114b63746e41fa9aae)。

分流电阻电压与总线电压（Shunt and Bus），连续模式（Continuous）。

<a id="r_ga96afd10c7f0e435cdef6a999295afae5"></a>

```c
#define INA237_OPER_MODE_TEMP_CONT 0x0C
```

相关声明：[INA237_OPER_MODE_TEMP_CONT](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga96afd10c7f0e435cdef6a999295afae5)。

温度，连续模式（Temperature, Continuous）。

<a id="r_ga51366870d0ef5c451ffdc92adf462b80"></a>

```c
#define INA237_OPER_MODE_BUS_VOLTAGE_TEMP_CONT 0x0D
```

相关声明：[INA237_OPER_MODE_BUS_VOLTAGE_TEMP_CONT](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga51366870d0ef5c451ffdc92adf462b80)。

总线与温度，连续模式（Bus and Temp, Continuous）。

<a id="r_ga51142226eb02138a1462b32e6a6b9c3d"></a>

```c
#define INA237_OPER_MODE_TEMP_SHUNT_VOLTAGE_CONT 0x0E
```

相关声明：[INA237_OPER_MODE_TEMP_SHUNT_VOLTAGE_CONT](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga51142226eb02138a1462b32e6a6b9c3d)。

温度与分流器，连续模式（Temp and Shunt, Continuous）。

<a id="r_ga5cfe6bc07b3dff06c2eefc3f73101289"></a>

```c
#define INA237_OPER_MODE_BUS_SHUNT_VOLTAGE_TEMP_CONT 0x0F
```

相关声明：[INA237_OPER_MODE_BUS_SHUNT_VOLTAGE_TEMP_CONT](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga5cfe6bc07b3dff06c2eefc3f73101289)。

总线、分流器与温度，连续模式（Bus, Shunt and Temp, Continuous）。

<a id="define-members-1"></a>

### 总线、分流器与温度转换时间（Bus, Shunt and Temperature Conversion Time）

INA237_ADC_CONFIG() 宏的转换时间参数（Conversion-time Argument）。

<a id="r_ga4c283158c66d3492efcbcb05bc797f43"></a>

```c
#define INA237_CONV_TIME_50 0x00
```

相关声明：[INA237_CONV_TIME_50](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga4c283158c66d3492efcbcb05bc797f43)。

转换时间（Conversion Time）：50 µs。

<a id="r_gafa48d1d9aab85913e75d4413ca0ade61"></a>

```c
#define INA237_CONV_TIME_84 0x01
```

相关声明：[INA237_CONV_TIME_84](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#gafa48d1d9aab85913e75d4413ca0ade61)。

转换时间（Conversion Time）：84 µs。

<a id="r_ga1f9505d58321c288af4324577c98b722"></a>

```c
#define INA237_CONV_TIME_150 0x02
```

相关声明：[INA237_CONV_TIME_150](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga1f9505d58321c288af4324577c98b722)。

转换时间（Conversion Time）：150 µs。

<a id="r_ga37f20de30929ec2aab29568799d03ba9"></a>

```c
#define INA237_CONV_TIME_280 0x03
```

相关声明：[INA237_CONV_TIME_280](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga37f20de30929ec2aab29568799d03ba9)。

转换时间（Conversion Time）：280 µs。

<a id="r_gadfe72090337a08de1e334ecec1a83cd2"></a>

```c
#define INA237_CONV_TIME_540 0x04
```

相关声明：[INA237_CONV_TIME_540](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#gadfe72090337a08de1e334ecec1a83cd2)。

转换时间（Conversion Time）：540 µs。

<a id="r_ga0c59baa9f6713fb4b651876934babca6"></a>

```c
#define INA237_CONV_TIME_1052 0x05
```

相关声明：[INA237_CONV_TIME_1052](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga0c59baa9f6713fb4b651876934babca6)。

转换时间（Conversion Time）：1052 µs。

<a id="r_ga73f063d5afcc5956769b1027a8ee7b6d"></a>

```c
#define INA237_CONV_TIME_2074 0x06
```

相关声明：[INA237_CONV_TIME_2074](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga73f063d5afcc5956769b1027a8ee7b6d)。

转换时间（Conversion Time）：2074 µs。

<a id="r_ga5492b364f79ed890f67b6bc3b51b10ee"></a>

```c
#define INA237_CONV_TIME_4120 0x07
```

相关声明：[INA237_CONV_TIME_4120](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga5492b364f79ed890f67b6bc3b51b10ee)。

转换时间（Conversion Time）：4120 µs。

<a id="define-members-2"></a>

### 平均模式：采样数（Averaging Mode, Number of Samples）

INA237_ADC_CONFIG() 宏的平均模式参数（Averaging-mode Argument）。

<a id="r_ga3c84d5be0bbca9a23fa823b5d0d01a33"></a>

```c
#define INA237_AVG_MODE_1 0x00
```

相关声明：[INA237_AVG_MODE_1](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga3c84d5be0bbca9a23fa823b5d0d01a33)。

1 个采样（Samples）。

<a id="r_ga4877129f08b10b594e05372a92e19987"></a>

```c
#define INA237_AVG_MODE_4 0x01
```

相关声明：[INA237_AVG_MODE_4](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga4877129f08b10b594e05372a92e19987)。

4 个样本（Samples）。

<a id="r_ga3e199273cf3f18cd35cf0cc71f54d395"></a>

```c
#define INA237_AVG_MODE_16 0x02
```

相关声明：[INA237_AVG_MODE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga3e199273cf3f18cd35cf0cc71f54d395)。

16 个样本（Samples）。

<a id="r_gaa1754bb85646932d2e3d269c6585fc4e"></a>

```c
#define INA237_AVG_MODE_64 0x03
```

相关声明：[INA237_AVG_MODE_64](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#gaa1754bb85646932d2e3d269c6585fc4e)。

64 个样本（Samples）。

<a id="r_ga1501acf37a027128d62037757140c84a"></a>

```c
#define INA237_AVG_MODE_128 0x04
```

相关声明：[INA237_AVG_MODE_128](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga1501acf37a027128d62037757140c84a)。

128 个样本（Samples）。

<a id="r_ga88f55660b69e5620ea60c3a53fafb170"></a>

```c
#define INA237_AVG_MODE_256 0x05
```

相关声明：[INA237_AVG_MODE_256](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga88f55660b69e5620ea60c3a53fafb170)。

256 个样本（Samples）。

<a id="r_ga8f7c1aad6dd88132e5d791788eb96055"></a>

```c
#define INA237_AVG_MODE_512 0x06
```

相关声明：[INA237_AVG_MODE_512](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga8f7c1aad6dd88132e5d791788eb96055)。

512 个样本（Samples）。

<a id="r_ga692ea64b27f36b455e361ff9f20eacc9"></a>

```c
#define INA237_AVG_MODE_1024 0x07
```

相关声明：[INA237_AVG_MODE_1024](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga692ea64b27f36b455e361ff9f20eacc9)。

1024 个采样（Samples）。

<a id="define-members-3"></a>

### 复位模式（Reset Mode）

INA237_CONFIG() 宏的复位模式参数（Reset-mode Argument）。

<a id="r_ga21d67009b5359d2408bcf8c2bfc7bd01"></a>

```c
#define INA237_RST_NORMAL_OPERATION 0x00
```

相关声明：[INA237_RST_NORMAL_OPERATION](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga21d67009b5359d2408bcf8c2bfc7bd01)。

正常运行（Normal Operation）。

<a id="r_ga79451943b97ee1146c536838b687f926"></a>

```c
#define INA237_RST_SYSTEM_RESET 0x01
```

相关声明：[INA237_RST_SYSTEM_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga79451943b97ee1146c536838b687f926)。

触发系统复位（System Reset）。

<a id="define-members-4"></a>

### 初始 ADC 转换延迟（Initial ADC Conversion Delay，步进 2 ms）

INA237_CONFIG() 宏的初始 ADC 延迟参数（Initial ADC-delay Argument）。

<a id="r_ga9bda801d1ba220808ee7bc7cadb4e1a8"></a>

```c
#define INA237_INIT_ADC_DELAY_0_S 0x00
```

相关声明：[INA237_INIT_ADC_DELAY_0_S](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga9bda801d1ba220808ee7bc7cadb4e1a8)。

0 s，即无延迟（No Delay）。

<a id="r_ga726c19fef618b0b81219b569e3dc318a"></a>

```c
#define INA237_INIT_ADC_DELAY_2_MS 0x01
```

相关声明：[INA237_INIT_ADC_DELAY_2_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga726c19fef618b0b81219b569e3dc318a)。

2 ms（毫秒）。

<a id="r_gac088479421d24217c570770466f50b4b"></a>

```c
#define INA237_INIT_ADC_DELAY_510_MS 0xFF
```

相关声明：[INA237_INIT_ADC_DELAY_510_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#gac088479421d24217c570770466f50b4b)。

延迟（Delay）：510 ms。

<a id="define-members-5"></a>

### IN+ 与 IN− 之间的分流器满量程范围（Shunt Full-scale Range）

INA237_CONFIG() 宏的分流器满量程范围参数（Shunt Full-scale Range Argument）。

<a id="r_ga5afae9b977793fb53823085c83986bb6"></a>

```c
#define INA237_ADC_RANGE_163_84 0x00
```

相关声明：[INA237_ADC_RANGE_163_84](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga5afae9b977793fb53823085c83986bb6)。

量程（Range）：±163.84 mV。

<a id="r_gae1c622a578b919b83781d3bc78429009"></a>

```c
#define INA237_ADC_RANGE_40_96 0x01
```

相关声明：[INA237_ADC_RANGE_40_96](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#gae1c622a578b919b83781d3bc78429009)。

量程（Range）：±40.96 mV。


## 14.2\_原页交叉引用（Cross References）

- [zephyr/dt-bindings/dt-util.h](../dt_bus_binding_reference/P006_设备树绑定工具头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P361_ina237.h_源码浏览.md)
- [INA237_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga721c648626cab01daf4013fc199aead4)
- [INA237_ADC_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga7310c76dac4ff27046970be6b24caa59)
- [INA237_CFG_HIGH_PRECISION](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga829d7aa6a07bad8da2583a648b6c0be9)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [INA237_OPER_MODE_SHUTDOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#gab42708837c802141acc358a385f6c5df)
- [INA237_OPER_MODE_BUS_VOLTAGE_TRIG](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga6ed1315d8bd3eaa1c73fd398e9ce1c62)
- [INA237_OPER_MODE_SHUNT_VOLTAGE_TRIG](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga90c2ca6edab1e6940a37026ca45d38cf)
- [INA237_OPER_MODE_SHUNT_BUS_VOLTAGE_TRIG](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga2313b32f90362ff4f0be94c813c2d915)
- [INA237_OPER_MODE_TEMP_TRIG](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#gaf48a2674ff69fe726f3161962afb5172)
- [INA237_OPER_MODE_TEMP_BUS_VOLTAGE_TRIG](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga61bd0c9161348b93c1b781324de3b20f)
- [INA237_OPER_MODE_TEMP_SHUNT_VOLTAGE_TRIG](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga8a83cbfc8a517d8dc696431134f55b8a)
- [INA237_OPER_MODE_BUS_SHUNT_VOLTAGE_TEMP_TRIG](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga5f524151fa6b5583add8522337aa275b)
- [INA237_OPER_MODE_BUS_VOLTAGE_CONT](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga4a6874ebe2fa43ab99812d4de4d6b2c1)
- [INA237_OPER_MODE_SHUNT_VOLTAGE_CONT](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#gae24188265ba63cd1b947585ea96efa42)
- [INA237_OPER_MODE_SHUNT_BUS_VOLTAGE_CONT](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga75919399317285114b63746e41fa9aae)
- [INA237_OPER_MODE_TEMP_CONT](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga96afd10c7f0e435cdef6a999295afae5)
- [INA237_OPER_MODE_BUS_VOLTAGE_TEMP_CONT](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga51366870d0ef5c451ffdc92adf462b80)
- [INA237_OPER_MODE_TEMP_SHUNT_VOLTAGE_CONT](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga51142226eb02138a1462b32e6a6b9c3d)
- [INA237_OPER_MODE_BUS_SHUNT_VOLTAGE_TEMP_CONT](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga5cfe6bc07b3dff06c2eefc3f73101289)
- [INA237_CONV_TIME_50](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga4c283158c66d3492efcbcb05bc797f43)
- [INA237_CONV_TIME_84](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#gafa48d1d9aab85913e75d4413ca0ade61)
- [INA237_CONV_TIME_150](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga1f9505d58321c288af4324577c98b722)
- [INA237_CONV_TIME_280](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga37f20de30929ec2aab29568799d03ba9)
- [INA237_CONV_TIME_540](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#gadfe72090337a08de1e334ecec1a83cd2)
- [INA237_CONV_TIME_1052](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga0c59baa9f6713fb4b651876934babca6)
- [INA237_CONV_TIME_2074](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga73f063d5afcc5956769b1027a8ee7b6d)
- [INA237_CONV_TIME_4120](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga5492b364f79ed890f67b6bc3b51b10ee)
- [INA237_AVG_MODE_1](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga3c84d5be0bbca9a23fa823b5d0d01a33)
- [INA237_AVG_MODE_4](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga4877129f08b10b594e05372a92e19987)
- [INA237_AVG_MODE_16](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga3e199273cf3f18cd35cf0cc71f54d395)
- [INA237_AVG_MODE_64](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#gaa1754bb85646932d2e3d269c6585fc4e)
- [INA237_AVG_MODE_128](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga1501acf37a027128d62037757140c84a)
- [INA237_AVG_MODE_256](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga88f55660b69e5620ea60c3a53fafb170)
- [INA237_AVG_MODE_512](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga8f7c1aad6dd88132e5d791788eb96055)
- [INA237_AVG_MODE_1024](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga692ea64b27f36b455e361ff9f20eacc9)
- [INA237_RST_NORMAL_OPERATION](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga21d67009b5359d2408bcf8c2bfc7bd01)
- [INA237_RST_SYSTEM_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga79451943b97ee1146c536838b687f926)
- [INA237_INIT_ADC_DELAY_0_S](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga9bda801d1ba220808ee7bc7cadb4e1a8)
- [INA237_INIT_ADC_DELAY_2_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga726c19fef618b0b81219b569e3dc318a)
- [INA237_INIT_ADC_DELAY_510_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#gac088479421d24217c570770466f50b4b)
- [INA237_ADC_RANGE_163_84](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#ga5afae9b977793fb53823085c83986bb6)
- [INA237_ADC_RANGE_40_96](https://docs.zephyrproject.org/latest/doxygen/html/group__ina237__interface.html#gae1c622a578b919b83781d3bc78429009)

<a id="ina237_oper_mode"></a>
<a id="ina237_conv_time"></a>
<a id="ina237_avg"></a>
<a id="ina237_reset"></a>
<a id="ina237_init_adc_delay"></a>
<a id="ina237_adc_range"></a>
<a id="header-details"></a>

---

[上一章](P013_zephyr__dt-bindings__sensor__iis3dwb.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P015_zephyr__drivers__interrupt_controller__intc_mchp_xec_ecia.h_文件参考.md)
