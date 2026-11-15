---
id: learning.zephyr-docs.api-file-host-video-reference.page-11
title: zephyr__drivers__mfd__rv3032.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rv3032_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_zephyr\_\_drivers\_\_mfd\_\_rv3032.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/rv3032_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stddef.h>
#include <stdint.h>
#include <zephyr/device.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 11.1\_宏定义（Macros）

<a id="r_afe5b888e8eecb1bfd862e00184392291"></a>

```c
#define RV3032_REG_100TH_SECONDS 0x00
```

相关声明：[RV3032_REG_100TH_SECONDS](#afe5b888e8eecb1bfd862e00184392291)。

<a id="r_a9f7a8ea2eb5b3aa4298289e0f897a88a"></a>

```c
#define RV3032_REG_SECONDS 0x01
```

相关声明：[RV3032_REG_SECONDS](#a9f7a8ea2eb5b3aa4298289e0f897a88a)。

<a id="r_a6bab443072d3d3984f2eaf59171b229e"></a>

```c
#define RV3032_REG_MINUTES 0x02
```

相关声明：[RV3032_REG_MINUTES](#a6bab443072d3d3984f2eaf59171b229e)。

<a id="r_ac1c3416d9387c31a70429c7c4ff5c7fc"></a>

```c
#define RV3032_REG_HOURS 0x03
```

相关声明：[RV3032_REG_HOURS](#ac1c3416d9387c31a70429c7c4ff5c7fc)。

<a id="r_ab940d4ad60eac8a38e48ca8b74a7a125"></a>

```c
#define RV3032_REG_WEEKDAY 0x04
```

相关声明：[RV3032_REG_WEEKDAY](#ab940d4ad60eac8a38e48ca8b74a7a125)。

<a id="r_a3f60f85c074723cbfacb5a56fca94126"></a>

```c
#define RV3032_REG_DATE 0x05
```

相关声明：[RV3032_REG_DATE](#a3f60f85c074723cbfacb5a56fca94126)。

<a id="r_a6c264b9a68cd8af686382033ff1af1c9"></a>

```c
#define RV3032_REG_MONTH 0x06
```

相关声明：[RV3032_REG_MONTH](#a6c264b9a68cd8af686382033ff1af1c9)。

<a id="r_a4afd75ccc6710b3c5c1641490a92b6d3"></a>

```c
#define RV3032_REG_YEAR 0x07
```

相关声明：[RV3032_REG_YEAR](#a4afd75ccc6710b3c5c1641490a92b6d3)。

<a id="r_a24124061c8e21a38bd64bbaab12e35c8"></a>

```c
#define RV3032_REG_ALARM_MINUTES 0x08
```

相关声明：[RV3032_REG_ALARM_MINUTES](#a24124061c8e21a38bd64bbaab12e35c8)。

<a id="r_a2ca9f1e7707d2e8cfa66813ff160b9e3"></a>

```c
#define RV3032_REG_ALARM_HOURS 0x09
```

相关声明：[RV3032_REG_ALARM_HOURS](#a2ca9f1e7707d2e8cfa66813ff160b9e3)。

<a id="r_a59889f4ae3de18fd04550350eb7a0c95"></a>

```c
#define RV3032_REG_ALARM_DATE 0x0A
```

相关声明：[RV3032_REG_ALARM_DATE](#a59889f4ae3de18fd04550350eb7a0c95)。

<a id="r_a0deb81df4d4b8acf6615282774f0a988"></a>

```c
#define RV3032_REG_TIMER_VALUE_0 0x0B
```

相关声明：[RV3032_REG_TIMER_VALUE_0](#a0deb81df4d4b8acf6615282774f0a988)。

<a id="r_a34838817c7baf68e9032f62a5f386f46"></a>

```c
#define RV3032_REG_TIMER_VALUE_1 0x0C
```

相关声明：[RV3032_REG_TIMER_VALUE_1](#a34838817c7baf68e9032f62a5f386f46)。

<a id="r_a0af01504b507738cf6e2975e3778089e"></a>

```c
#define RV3032_REG_STATUS 0x0D
```

相关声明：[RV3032_REG_STATUS](#a0af01504b507738cf6e2975e3778089e)。

<a id="r_ac905325f7cff95a69ae66af1713769a9"></a>

```c
#define RV3032_REG_TEMPERATURE_LSB 0x0E
```

相关声明：[RV3032_REG_TEMPERATURE_LSB](#ac905325f7cff95a69ae66af1713769a9)。

<a id="r_adea8e22cfb7397223a58d6cf0235d378"></a>

```c
#define RV3032_REG_TEMPERATURE_MSB 0x0F
```

相关声明：[RV3032_REG_TEMPERATURE_MSB](#adea8e22cfb7397223a58d6cf0235d378)。

<a id="r_ac278485d71352f8abd73bf5e9a35c384"></a>

```c
#define RV3032_REG_CONTROL1 0x10
```

相关声明：[RV3032_REG_CONTROL1](#ac278485d71352f8abd73bf5e9a35c384)。

<a id="r_a1fc6b1ede3ed031b03693f5ae2f2c2f9"></a>

```c
#define RV3032_REG_CONTROL2 0x11
```

相关声明：[RV3032_REG_CONTROL2](#a1fc6b1ede3ed031b03693f5ae2f2c2f9)。

<a id="r_a724b6a7719d65563ff51b656a4d7636d"></a>

```c
#define RV3032_REG_CONTROL3 0x12
```

相关声明：[RV3032_REG_CONTROL3](#a724b6a7719d65563ff51b656a4d7636d)。

<a id="r_ade46a500e6a8ac675a479f1ad355e407"></a>

```c
#define RV3032_TS_CTRL 0x13
```

相关声明：[RV3032_TS_CTRL](#ade46a500e6a8ac675a479f1ad355e407)。

<a id="r_ab4fca50175b34f114979d9a34c0e8373"></a>

```c
#define RV3032_CLK_INT_MASK 0x14
```

相关声明：[RV3032_CLK_INT_MASK](#ab4fca50175b34f114979d9a34c0e8373)。

<a id="r_a0aac524189c87622d6c47f52ba2170be"></a>

```c
#define RV3032_EVI_CONTROL 0x15
```

相关声明：[RV3032_EVI_CONTROL](#a0aac524189c87622d6c47f52ba2170be)。

<a id="r_a0987b8df0c15f146874be00d6c6a2286"></a>

```c
#define RV3032_REG_TEMP_LOW_THLD 0x16
```

相关声明：[RV3032_REG_TEMP_LOW_THLD](#a0987b8df0c15f146874be00d6c6a2286)。

<a id="r_a4aa1028ef055a6fd32385006bc5618b5"></a>

```c
#define RV3032_REG_TEMP_HIGH_THLD 0x17
```

相关声明：[RV3032_REG_TEMP_HIGH_THLD](#a4aa1028ef055a6fd32385006bc5618b5)。

<a id="r_ac54fb5fc0100af9dc5922bfaebf5eee6"></a>

```c
#define RV3032_REG_EEPROM_ADDRESS 0x3D
```

相关声明：[RV3032_REG_EEPROM_ADDRESS](#ac54fb5fc0100af9dc5922bfaebf5eee6)。

<a id="r_ad8342d74b1332c2078d8f48fe5c4b4e1"></a>

```c
#define RV3032_REG_EEPROM_DATA 0x3E
```

相关声明：[RV3032_REG_EEPROM_DATA](#ad8342d74b1332c2078d8f48fe5c4b4e1)。

<a id="r_ac850dda27873ce75dfd9527acc5063b1"></a>

```c
#define RV3032_REG_EEPROM_COMMAND 0x3F
```

相关声明：[RV3032_REG_EEPROM_COMMAND](#ac850dda27873ce75dfd9527acc5063b1)。

<a id="r_a68ac6c2258db13df7f064aad652c0e02"></a>

```c
#define RV3032_REG_EEPROM_PMU 0xC0
```

相关声明：[RV3032_REG_EEPROM_PMU](#a68ac6c2258db13df7f064aad652c0e02)。

<a id="r_adb45311f8f2390bb78469bf589a7d90a"></a>

```c
#define RV3032_REG_EEPROM_RAM1 0x40
```

相关声明：[RV3032_REG_EEPROM_RAM1](#adb45311f8f2390bb78469bf589a7d90a)。

<a id="r_a34439445411cfb9c3b644bf7756a0f14"></a>

```c
#define RV3032_REG_EEPROM_OFFSET 0xC1
```

相关声明：[RV3032_REG_EEPROM_OFFSET](#a34439445411cfb9c3b644bf7756a0f14)。

<a id="r_a455ae7d58405f883c7b0e08cade19ae6"></a>

```c
#define RV3032_REG_EEPROM_CLKOUT1 0xC2
```

相关声明：[RV3032_REG_EEPROM_CLKOUT1](#a455ae7d58405f883c7b0e08cade19ae6)。

<a id="r_a7032e025dcfe811662f8d191ca9987e5"></a>

```c
#define RV3032_REG_EEPROM_CLKOUT2 0xC3
```

相关声明：[RV3032_REG_EEPROM_CLKOUT2](#a7032e025dcfe811662f8d191ca9987e5)。

<a id="r_aef94f7ffe42778fb8f46ba9748d7594b"></a>

```c
#define RV3032_REG_EEPROM_TREF0 0xC4
```

相关声明：[RV3032_REG_EEPROM_TREF0](#aef94f7ffe42778fb8f46ba9748d7594b)。

<a id="r_a8ea2f9d479487e8c2904450fb1d4a236"></a>

```c
#define RV3032_REG_EEPROM_TREF1 0xC5
```

相关声明：[RV3032_REG_EEPROM_TREF1](#a8ea2f9d479487e8c2904450fb1d4a236)。

<a id="r_a985feb43b3d955fc0075c546e9ce0c6d"></a>

```c
#define RV3032_CONTROL1_TD GENMASK(1, 0)
```

相关声明：[RV3032_CONTROL1_TD](#a985feb43b3d955fc0075c546e9ce0c6d)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_a117be54a0c0600d721800e3bdd07cff3"></a>

```c
#define RV3032_CONTROL1_EERD BIT(2)
```

相关声明：[RV3032_CONTROL1_EERD](#a117be54a0c0600d721800e3bdd07cff3)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a1e3b8873c288b3877e45295248740e98"></a>

```c
#define RV3032_CONTROL1_TE BIT(3)
```

相关声明：[RV3032_CONTROL1_TE](#a1e3b8873c288b3877e45295248740e98)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a62e3ff0425f13fa87fa9c4a6f27b6797"></a>

```c
#define RV3032_CONTROL1_USEL BIT(4)
```

相关声明：[RV3032_CONTROL1_USEL](#a62e3ff0425f13fa87fa9c4a6f27b6797)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a23eb79a456ecdca1912ea38df31e17e7"></a>

```c
#define RV3032_CONTROL1_GP0 BIT(5)
```

相关声明：[RV3032_CONTROL1_GP0](#a23eb79a456ecdca1912ea38df31e17e7)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a5e6284624e6b40fe498c6caa94cd2ef0"></a>

```c
#define RV3032_CONTROL2_STOP BIT(0)
```

相关声明：[RV3032_CONTROL2_STOP](#a5e6284624e6b40fe498c6caa94cd2ef0)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a5929ed9ae6b9fb3d68c28a79ca8746b7"></a>

```c
#define RV3032_CONTROL2_GP1 BIT(1)
```

相关声明：[RV3032_CONTROL2_GP1](#a5929ed9ae6b9fb3d68c28a79ca8746b7)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a5cb2db1dd04d8541faf68d6e92cfab53"></a>

```c
#define RV3032_CONTROL2_EIE BIT(2)
```

相关声明：[RV3032_CONTROL2_EIE](#a5cb2db1dd04d8541faf68d6e92cfab53)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a5e9c905ee5f46318c149926e4fad500b"></a>

```c
#define RV3032_CONTROL2_AIE BIT(3)
```

相关声明：[RV3032_CONTROL2_AIE](#a5e9c905ee5f46318c149926e4fad500b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a3054dd5d4436cf0d9ddc3a94280e86ea"></a>

```c
#define RV3032_CONTROL2_TIE BIT(4)
```

相关声明：[RV3032_CONTROL2_TIE](#a3054dd5d4436cf0d9ddc3a94280e86ea)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a555eddf7a3e3616153b62e92ddb1f0f4"></a>

```c
#define RV3032_CONTROL2_UIE BIT(5)
```

相关声明：[RV3032_CONTROL2_UIE](#a555eddf7a3e3616153b62e92ddb1f0f4)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a955853c76d49c381170f300d650d897a"></a>

```c
#define RV3032_CONTROL2_CLKIE BIT(6)
```

相关声明：[RV3032_CONTROL2_CLKIE](#a955853c76d49c381170f300d650d897a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a52b2c7ffc4ce0dc7ba48cb76394221fc"></a>

```c
#define RV3032_CONTROL3_TLIE BIT(0)
```

相关声明：[RV3032_CONTROL3_TLIE](#a52b2c7ffc4ce0dc7ba48cb76394221fc)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a8b47528e5c088efa7e9162f15a25dd79"></a>

```c
#define RV3032_CONTROL3_THIE BIT(1)
```

相关声明：[RV3032_CONTROL3_THIE](#a8b47528e5c088efa7e9162f15a25dd79)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a72cd2fae236160d85c7c78bb0cfe653b"></a>

```c
#define RV3032_CONTROL3_TLE BIT(2)
```

相关声明：[RV3032_CONTROL3_TLE](#a72cd2fae236160d85c7c78bb0cfe653b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ac3be64f11793ea841d295f229fbfdc98"></a>

```c
#define RV3032_CONTROL3_THE BIT(3)
```

相关声明：[RV3032_CONTROL3_THE](#ac3be64f11793ea841d295f229fbfdc98)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a51f7d94c062d5ea4558d8e5330904012"></a>

```c
#define RV3032_CONTROL3_BSIE BIT(4)
```

相关声明：[RV3032_CONTROL3_BSIE](#a51f7d94c062d5ea4558d8e5330904012)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a613eaf8d67e7105caf5c969be0ffe684"></a>

```c
#define RV3032_100TH_SECONDS_MASK GENMASK(7, 0)
```

相关声明：[RV3032_100TH_SECONDS_MASK](#a613eaf8d67e7105caf5c969be0ffe684)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_a53ef32b486a7d3c0ded16aa29d434f1e"></a>

```c
#define RV3032_SECONDS_MASK GENMASK(6, 0)
```

相关声明：[RV3032_SECONDS_MASK](#a53ef32b486a7d3c0ded16aa29d434f1e)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_a3dd861e1676fd4b5437ce609f1a0c1fa"></a>

```c
#define RV3032_MINUTES_MASK GENMASK(6, 0)
```

相关声明：[RV3032_MINUTES_MASK](#a3dd861e1676fd4b5437ce609f1a0c1fa)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_a44b32cbcdd1f312c81840e67faab117b"></a>

```c
#define RV3032_HOURS_AMPM BIT(5)
```

相关声明：[RV3032_HOURS_AMPM](#a44b32cbcdd1f312c81840e67faab117b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ae89750f5b77b2c3de7e85ff8aea9114e"></a>

```c
#define RV3032_HOURS_12H_MASK GENMASK(4, 0)
```

相关声明：[RV3032_HOURS_12H_MASK](#ae89750f5b77b2c3de7e85ff8aea9114e)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_a05f8db72c25fd24fd390e9a5e5922a6c"></a>

```c
#define RV3032_HOURS_24H_MASK GENMASK(5, 0)
```

相关声明：[RV3032_HOURS_24H_MASK](#a05f8db72c25fd24fd390e9a5e5922a6c)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_a7af85d92b1401cb867b9c9911c5b607c"></a>

```c
#define RV3032_DATE_MASK GENMASK(5, 0)
```

相关声明：[RV3032_DATE_MASK](#a7af85d92b1401cb867b9c9911c5b607c)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_a90e99ab54c2dce004732a5630aef354d"></a>

```c
#define RV3032_WEEKDAY_MASK GENMASK(2, 0)
```

相关声明：[RV3032_WEEKDAY_MASK](#a90e99ab54c2dce004732a5630aef354d)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_a918eaa86a4f197352e92b40e73b324c8"></a>

```c
#define RV3032_MONTH_MASK GENMASK(4, 0)
```

相关声明：[RV3032_MONTH_MASK](#a918eaa86a4f197352e92b40e73b324c8)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_a763c742c8c80124b8fc0680d4241243d"></a>

```c
#define RV3032_YEAR_MASK GENMASK(7, 0)
```

相关声明：[RV3032_YEAR_MASK](#a763c742c8c80124b8fc0680d4241243d)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_afc4e39b520dea4b92399c31ff28fbbac"></a>

```c
#define RV3032_ALARM_MINUTES_AE_M BIT(7)
```

相关声明：[RV3032_ALARM_MINUTES_AE_M](#afc4e39b520dea4b92399c31ff28fbbac)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ab324b06b10b9bde1bc1d5c95b70268f0"></a>

```c
#define RV3032_ALARM_MINUTES_MASK GENMASK(6, 0)
```

相关声明：[RV3032_ALARM_MINUTES_MASK](#ab324b06b10b9bde1bc1d5c95b70268f0)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_a666d117ef4a4813446909a826f2d52b7"></a>

```c
#define RV3032_ALARM_HOURS_AE_H BIT(7)
```

相关声明：[RV3032_ALARM_HOURS_AE_H](#a666d117ef4a4813446909a826f2d52b7)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a50fc6d74289128dd7b4ab78da8fb93bb"></a>

```c
#define RV3032_ALARM_HOURS_AMPM BIT(5)
```

相关声明：[RV3032_ALARM_HOURS_AMPM](#a50fc6d74289128dd7b4ab78da8fb93bb)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a384ddbe578c273f3c89f688b76c70c0d"></a>

```c
#define RV3032_ALARM_HOURS_12H_MASK GENMASK(4, 0)
```

相关声明：[RV3032_ALARM_HOURS_12H_MASK](#a384ddbe578c273f3c89f688b76c70c0d)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_a89d6be890f49a19f77e6b475b03868c7"></a>

```c
#define RV3032_ALARM_HOURS_24H_MASK GENMASK(5, 0)
```

相关声明：[RV3032_ALARM_HOURS_24H_MASK](#a89d6be890f49a19f77e6b475b03868c7)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_ab75fe3f65d91cc875600ac3a985921d0"></a>

```c
#define RV3032_ALARM_DATE_AE_D BIT(7)
```

相关声明：[RV3032_ALARM_DATE_AE_D](#ab75fe3f65d91cc875600ac3a985921d0)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ae5e5af076500b46048dc71c775fc742d"></a>

```c
#define RV3032_ALARM_DATE_MASK GENMASK(5, 0)
```

相关声明：[RV3032_ALARM_DATE_MASK](#ae5e5af076500b46048dc71c775fc742d)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_aed140542291595c08434d8d5cc8556c2"></a>

```c
#define RV3032_STATUS_VLF BIT(0)
```

相关声明：[RV3032_STATUS_VLF](#aed140542291595c08434d8d5cc8556c2)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a8e3b0327b5999b370e8906ce05cac31e"></a>

```c
#define RV3032_STATUS_PORF BIT(1)
```

相关声明：[RV3032_STATUS_PORF](#a8e3b0327b5999b370e8906ce05cac31e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a4a9107dc3b87d239bb7a9c428756ff02"></a>

```c
#define RV3032_STATUS_EVF BIT(2)
```

相关声明：[RV3032_STATUS_EVF](#a4a9107dc3b87d239bb7a9c428756ff02)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a13aa871407da6f68e40358b4ab76c6fb"></a>

```c
#define RV3032_STATUS_AF BIT(3)
```

相关声明：[RV3032_STATUS_AF](#a13aa871407da6f68e40358b4ab76c6fb)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_acf1bf73cfda6a7542fac2d32de61ec68"></a>

```c
#define RV3032_STATUS_TF BIT(4)
```

相关声明：[RV3032_STATUS_TF](#acf1bf73cfda6a7542fac2d32de61ec68)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a6959f1f463d9f59ebe4217962835a3d0"></a>

```c
#define RV3032_STATUS_UF BIT(5)
```

相关声明：[RV3032_STATUS_UF](#a6959f1f463d9f59ebe4217962835a3d0)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a52580fa936730fe8c949f337fbce0067"></a>

```c
#define RV3032_STATUS_TLF BIT(6)
```

相关声明：[RV3032_STATUS_TLF](#a52580fa936730fe8c949f337fbce0067)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_afc3c323cb98cb513c0d14802a6573b18"></a>

```c
#define RV3032_STATUS_THF BIT(7)
```

相关声明：[RV3032_STATUS_THF](#afc3c323cb98cb513c0d14802a6573b18)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a28f1765db25913bd72623f46483ca217"></a>

```c
#define RV3032_EEPROM_CLKOUT1_HFD_LOW GENMASK(7, 0)
```

相关声明：[RV3032_EEPROM_CLKOUT1_HFD_LOW](#a28f1765db25913bd72623f46483ca217)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_aa588e97e0fb2d5ac17d501ca81019cd6"></a>

```c
#define RV3032_TEMPERATURE_BSF BIT(0)
```

相关声明：[RV3032_TEMPERATURE_BSF](#aa588e97e0fb2d5ac17d501ca81019cd6)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a0feb5278fd3a8cdbd2d6a6e00939a222"></a>

```c
#define RV3032_TEMPERATURE_CLKF BIT(1)
```

相关声明：[RV3032_TEMPERATURE_CLKF](#a0feb5278fd3a8cdbd2d6a6e00939a222)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_aeac399f30a5d8639876173c9668315b9"></a>

```c
#define RV3032_TEMPERATURE_EEBUSY BIT(2)
```

相关声明：[RV3032_TEMPERATURE_EEBUSY](#aeac399f30a5d8639876173c9668315b9)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a7e8a22024424fc8649f41f941952b6d1"></a>

```c
#define RV3032_TEMPERATURE_EEF BIT(3)
```

相关声明：[RV3032_TEMPERATURE_EEF](#a7e8a22024424fc8649f41f941952b6d1)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_af40f6c4e9f6212edf0c6ea04ae494440"></a>

```c
#define RV3032_TEMPERATURE_TEMP_LSB GENMASK(7, 4)
```

相关声明：[RV3032_TEMPERATURE_TEMP_LSB](#af40f6c4e9f6212edf0c6ea04ae494440)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_acab3e59acb465261946f11639125a426"></a>

```c
#define RV3032_EEPROM_PMU_NCLKE BIT(6)
```

相关声明：[RV3032_EEPROM_PMU_NCLKE](#acab3e59acb465261946f11639125a426)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a1328b3e0d4f046e56ef32ad4791a6e71"></a>

```c
#define RV3032_EEPROM_PMU_BSM GENMASK(5, 4)
```

相关声明：[RV3032_EEPROM_PMU_BSM](#a1328b3e0d4f046e56ef32ad4791a6e71)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_a6e4e3e6f8f23486724a8f2e2e776a195"></a>

```c
#define RV3032_EEPROM_PMU_TCR GENMASK(3, 2)
```

相关声明：[RV3032_EEPROM_PMU_TCR](#a6e4e3e6f8f23486724a8f2e2e776a195)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_a1b7732f0480f0efae5739a9b58f6fe2c"></a>

```c
#define RV3032_EEPROM_PMU_TCM GENMASK(1, 0)
```

相关声明：[RV3032_EEPROM_PMU_TCM](#a1b7732f0480f0efae5739a9b58f6fe2c)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_af23af0f7502001b155ad787539f3686e"></a>

```c
#define RV3032_EEPROM_CLKOUT2_OS BIT(7)
```

相关声明：[RV3032_EEPROM_CLKOUT2_OS](#af23af0f7502001b155ad787539f3686e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a8f62fc7bd7173f197c3d9285c6564770"></a>

```c
#define RV3032_EEPROM_CLKOUT2_FD GENMASK(6, 5)
```

相关声明：[RV3032_EEPROM_CLKOUT2_FD](#a8f62fc7bd7173f197c3d9285c6564770)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_a7268a5781e77a2646feaf1b9c38b0e9e"></a>

```c
#define RV3032_EEPROM_CLKOUT2_HFD_HIGH GENMASK(4, 0)
```

相关声明：[RV3032_EEPROM_CLKOUT2_HFD_HIGH](#a7268a5781e77a2646feaf1b9c38b0e9e)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

<a id="r_a8ac0a11e501e0fe1b3d0567c1bdd9694"></a>

```c
#define RV3032_YEAR_OFFSET (2000 - 1900)
```

相关声明：[RV3032_YEAR_OFFSET](#a8ac0a11e501e0fe1b3d0567c1bdd9694)。

<a id="r_a14de9e930d633a318721225a9b1b2aa0"></a>

```c
#define RV3032_MONTH_OFFSET 1
```

相关声明：[RV3032_MONTH_OFFSET](#a14de9e930d633a318721225a9b1b2aa0)。

<a id="r_a620baa8b1a454c28dbabc7ee68f93640"></a>

```c
#define mfd_rv3032_set_status(dev, mask)
```

相关声明：[mfd_rv3032_set_status](#a620baa8b1a454c28dbabc7ee68f93640)。

<a id="r_a0d62d933117da3f94f72c678f116b7a7"></a>

```c
#define mfd_rv3032_clear_status(dev, mask)
```

相关声明：[mfd_rv3032_clear_status](#a0d62d933117da3f94f72c678f116b7a7)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 11.2\_类型定义（Typedefs）

<a id="r_af38501b5aa1350ebc2c03be9b6623353"></a>

```c
typedef void(* child_isr_t) (const struct device *dev)
```

相关声明：[child_isr_t](#af38501b5aa1350ebc2c03be9b6623353)、[device](../device_reference/P002_设备对象结构.md)。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 11.3\_枚举（Enumerations）

<a id="r_ae4d56fd30130dc4f332ecf43465a1558"></a>

```c
enum child_dev { RV3032_DEV_REG = 0 , RV3032_DEV_RTC_ALARM , RV3032_DEV_RTC_UPDATE , RV3032_DEV_COUNTER , RV3032_DEV_SENSOR , RV3032_DEV_MAX }
```

相关声明：[child_dev](#ae4d56fd30130dc4f332ecf43465a1558)、[RV3032_DEV_REG](#ae4d56fd30130dc4f332ecf43465a1558a7eab30c06b62ba3fd05aa6b17de65664)、[RV3032_DEV_RTC_ALARM](#ae4d56fd30130dc4f332ecf43465a1558a9cb8727d9c721d301fe0f868b2ac4f6f)、[RV3032_DEV_RTC_UPDATE](#ae4d56fd30130dc4f332ecf43465a1558ad728f5a0673370137d421fc1636a97a4)、[RV3032_DEV_COUNTER](#ae4d56fd30130dc4f332ecf43465a1558a04ef64de3b15eb1183b1c05b0a7b14e1)、[RV3032_DEV_SENSOR](#ae4d56fd30130dc4f332ecf43465a1558a0a0db910452cc15f25178419fcb3f70a)、[RV3032_DEV_MAX](#ae4d56fd30130dc4f332ecf43465a1558ac6dce8a07e4ca4c3927f895b65138c57)。

RV3032 的子设备（Child Device）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 11.4\_函数（Functions）

<a id="r_a3f1be094ac698ce0f41d147d63ceca79"></a>

```c
int mfd_rv3032_read_regs (const struct device *dev, uint8_t addr, void *buf, size_t len)
```

相关声明：[mfd_rv3032_read_regs](#a3f1be094ac698ce0f41d147d63ceca79)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_a822141bf579338c3b66a0f62233c4b80"></a>

```c
int mfd_rv3032_read_reg8 (const struct device *dev, uint8_t addr, uint8_t *val)
```

相关声明：[mfd_rv3032_read_reg8](#a822141bf579338c3b66a0f62233c4b80)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_a114cd42a12443e1e7ee0339ee22c3fb1"></a>

```c
int mfd_rv3032_write_regs (const struct device *dev, uint8_t addr, void *buf, size_t len)
```

相关声明：[mfd_rv3032_write_regs](#a114cd42a12443e1e7ee0339ee22c3fb1)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_a27a9c24a7590b583259ac7f030642d0c"></a>

```c
int mfd_rv3032_write_reg8 (const struct device *dev, uint8_t addr, uint8_t val)
```

相关声明：[mfd_rv3032_write_reg8](#a27a9c24a7590b583259ac7f030642d0c)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_a0690ef025e4ebe7fa96818b18dbe81cb"></a>

```c
int mfd_rv3032_update_reg8 (const struct device *dev, uint8_t addr, uint8_t mask, uint8_t val)
```

相关声明：[mfd_rv3032_update_reg8](#a0690ef025e4ebe7fa96818b18dbe81cb)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

<a id="r_a7d630d2e9e6b76969ba2af9d833736ee"></a>

```c
void mfd_rv3032_set_irq_handler (const struct device *dev, const struct device *child_dev, enum child_dev child_idx, child_isr_t handler)
```

相关声明：[mfd_rv3032_set_irq_handler](#a7d630d2e9e6b76969ba2af9d833736ee)、[device](../device_reference/P002_设备对象结构.md)、[device](../device_reference/P002_设备对象结构.md)、[child_dev](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gae4d56fd30130dc4f332ecf43465a1558)、[child_dev](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gae4d56fd30130dc4f332ecf43465a1558)、[child_isr_t](#af38501b5aa1350ebc2c03be9b6623353)。

<a id="r_a209ce7f7823aef8c4fd013ebfdfe031f"></a>

```c
int mfd_rv3032_update_status (const struct device *dev, uint8_t mask, uint8_t val)
```

相关声明：[mfd_rv3032_update_status](#a209ce7f7823aef8c4fd013ebfdfe031f)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

对状态寄存器执行读－改－写（RMW）更新。

<a id="r_af17edb1eb921a050307cf02c5bb46590"></a>

```c
int mfd_rv3032_update_cfg (const struct device *dev, uint8_t addr, uint8_t mask, uint8_t val)
```

相关声明：[mfd_rv3032_update_cfg](#af17edb1eb921a050307cf02c5bb46590)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

对寄存器执行读－改－写（RMW）更新，并提交到电可擦可编程只读存储器（EEPROM）。

<a id="r_a54576af433c288a6ae9e82523781b0e9"></a>

```c
int mfd_rv3032_enter_eerd (const struct device *dev)
```

相关声明：[mfd_rv3032_enter_eerd](#a54576af433c288a6ae9e82523781b0e9)、[device](../device_reference/P002_设备对象结构.md)。

锁定 EEPROM 互斥锁（Mutex），并禁用 EEPROM 自动刷新（Autorefresh）。

<a id="r_ab517e214d31f981cbda89144cc673f35"></a>

```c
int mfd_rv3032_exit_eerd (const struct device *dev)
```

相关声明：[mfd_rv3032_exit_eerd](#ab517e214d31f981cbda89144cc673f35)、[device](../device_reference/P002_设备对象结构.md)。

解锁 EEPROM 互斥锁（Mutex），并启用 EEPROM 自动刷新（Autorefresh）。

<a id="r_a4bb87fbf0d3c5d50138e8444a956b812"></a>

```c
int mfd_rv3032_eeprom_update (const struct device *dev)
```

相关声明：[mfd_rv3032_eeprom_update](#a4bb87fbf0d3c5d50138e8444a956b812)、[device](../device_reference/P002_设备对象结构.md)。

将配置寄存器（Config Register）提交到 EEPROM。

<a id="r_abc0539b1fcc8cf64617c13bb4749b77c"></a>

```c
int mfd_rv3032_eeprom_refresh (const struct device *dev)
```

相关声明：[mfd_rv3032_eeprom_refresh](#abc0539b1fcc8cf64617c13bb4749b77c)、[device](../device_reference/P002_设备对象结构.md)。

从 EEPROM 加载配置寄存器（Config Register）。

<a id="r_a2248379fbd15362aa8c701498deacca4"></a>

```c
int mfd_rv3032_eeprom_write_one (const struct device *dev, uint8_t addr, uint8_t val)
```

相关声明：[mfd_rv3032_eeprom_write_one](#a2248379fbd15362aa8c701498deacca4)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向 EEPROM 写入一个字节（Byte）。

## 11.5\_详细说明（Detailed Documentation）

<a id="a0d62d933117da3f94f72c678f116b7a7"></a>

### `mfd_rv3032_clear_status`

```c
#define mfd_rv3032_clear_status ( dev, mask )
```

展开值（Value）：

```c
mfd_rv3032_update_status(dev, mask, 0x00)
```

<a id="a620baa8b1a454c28dbabc7ee68f93640"></a>

### `mfd_rv3032_set_status`

```c
#define mfd_rv3032_set_status ( dev, mask )
```

展开值（Value）：

```c
mfd_rv3032_update_status(dev, mask, 0xff)
```

<a id="a613eaf8d67e7105caf5c969be0ffe684"></a>

### `RV3032_100TH_SECONDS_MASK`

```c
#define RV3032_100TH_SECONDS_MASK GENMASK(7, 0)
```

<a id="ab75fe3f65d91cc875600ac3a985921d0"></a>

### `RV3032_ALARM_DATE_AE_D`

```c
#define RV3032_ALARM_DATE_AE_D BIT(7)
```

<a id="ae5e5af076500b46048dc71c775fc742d"></a>

### `RV3032_ALARM_DATE_MASK`

```c
#define RV3032_ALARM_DATE_MASK GENMASK(5, 0)
```

<a id="a384ddbe578c273f3c89f688b76c70c0d"></a>

### `RV3032_ALARM_HOURS_12H_MASK`

```c
#define RV3032_ALARM_HOURS_12H_MASK GENMASK(4, 0)
```

<a id="a89d6be890f49a19f77e6b475b03868c7"></a>

### `RV3032_ALARM_HOURS_24H_MASK`

```c
#define RV3032_ALARM_HOURS_24H_MASK GENMASK(5, 0)
```

<a id="a666d117ef4a4813446909a826f2d52b7"></a>

### `RV3032_ALARM_HOURS_AE_H`

```c
#define RV3032_ALARM_HOURS_AE_H BIT(7)
```

<a id="a50fc6d74289128dd7b4ab78da8fb93bb"></a>

### `RV3032_ALARM_HOURS_AMPM`

```c
#define RV3032_ALARM_HOURS_AMPM BIT(5)
```

<a id="afc4e39b520dea4b92399c31ff28fbbac"></a>

### `RV3032_ALARM_MINUTES_AE_M`

```c
#define RV3032_ALARM_MINUTES_AE_M BIT(7)
```

<a id="ab324b06b10b9bde1bc1d5c95b70268f0"></a>

### `RV3032_ALARM_MINUTES_MASK`

```c
#define RV3032_ALARM_MINUTES_MASK GENMASK(6, 0)
```

<a id="ab4fca50175b34f114979d9a34c0e8373"></a>

### `RV3032_CLK_INT_MASK`

```c
#define RV3032_CLK_INT_MASK 0x14
```

<a id="a117be54a0c0600d721800e3bdd07cff3"></a>

### `RV3032_CONTROL1_EERD`

```c
#define RV3032_CONTROL1_EERD BIT(2)
```

<a id="a23eb79a456ecdca1912ea38df31e17e7"></a>

### `RV3032_CONTROL1_GP0`

```c
#define RV3032_CONTROL1_GP0 BIT(5)
```

<a id="a985feb43b3d955fc0075c546e9ce0c6d"></a>

### `RV3032_CONTROL1_TD`

```c
#define RV3032_CONTROL1_TD GENMASK(1, 0)
```

<a id="a1e3b8873c288b3877e45295248740e98"></a>

### `RV3032_CONTROL1_TE`

```c
#define RV3032_CONTROL1_TE BIT(3)
```

<a id="a62e3ff0425f13fa87fa9c4a6f27b6797"></a>

### `RV3032_CONTROL1_USEL`

```c
#define RV3032_CONTROL1_USEL BIT(4)
```

<a id="a5e9c905ee5f46318c149926e4fad500b"></a>

### `RV3032_CONTROL2_AIE`

```c
#define RV3032_CONTROL2_AIE BIT(3)
```

<a id="a955853c76d49c381170f300d650d897a"></a>

### `RV3032_CONTROL2_CLKIE`

```c
#define RV3032_CONTROL2_CLKIE BIT(6)
```

<a id="a5cb2db1dd04d8541faf68d6e92cfab53"></a>

### `RV3032_CONTROL2_EIE`

```c
#define RV3032_CONTROL2_EIE BIT(2)
```

<a id="a5929ed9ae6b9fb3d68c28a79ca8746b7"></a>

### `RV3032_CONTROL2_GP1`

```c
#define RV3032_CONTROL2_GP1 BIT(1)
```

<a id="a5e6284624e6b40fe498c6caa94cd2ef0"></a>

### `RV3032_CONTROL2_STOP`

```c
#define RV3032_CONTROL2_STOP BIT(0)
```

<a id="a3054dd5d4436cf0d9ddc3a94280e86ea"></a>

### `RV3032_CONTROL2_TIE`

```c
#define RV3032_CONTROL2_TIE BIT(4)
```

<a id="a555eddf7a3e3616153b62e92ddb1f0f4"></a>

### `RV3032_CONTROL2_UIE`

```c
#define RV3032_CONTROL2_UIE BIT(5)
```

<a id="a51f7d94c062d5ea4558d8e5330904012"></a>

### `RV3032_CONTROL3_BSIE`

```c
#define RV3032_CONTROL3_BSIE BIT(4)
```

<a id="ac3be64f11793ea841d295f229fbfdc98"></a>

### `RV3032_CONTROL3_THE`

```c
#define RV3032_CONTROL3_THE BIT(3)
```

<a id="a8b47528e5c088efa7e9162f15a25dd79"></a>

### `RV3032_CONTROL3_THIE`

```c
#define RV3032_CONTROL3_THIE BIT(1)
```

<a id="a72cd2fae236160d85c7c78bb0cfe653b"></a>

### `RV3032_CONTROL3_TLE`

```c
#define RV3032_CONTROL3_TLE BIT(2)
```

<a id="a52b2c7ffc4ce0dc7ba48cb76394221fc"></a>

### `RV3032_CONTROL3_TLIE`

```c
#define RV3032_CONTROL3_TLIE BIT(0)
```

<a id="a7af85d92b1401cb867b9c9911c5b607c"></a>

### `RV3032_DATE_MASK`

```c
#define RV3032_DATE_MASK GENMASK(5, 0)
```

<a id="a28f1765db25913bd72623f46483ca217"></a>

### `RV3032_EEPROM_CLKOUT1_HFD_LOW`

```c
#define RV3032_EEPROM_CLKOUT1_HFD_LOW GENMASK(7, 0)
```

<a id="a8f62fc7bd7173f197c3d9285c6564770"></a>

### `RV3032_EEPROM_CLKOUT2_FD`

```c
#define RV3032_EEPROM_CLKOUT2_FD GENMASK(6, 5)
```

<a id="a7268a5781e77a2646feaf1b9c38b0e9e"></a>

### `RV3032_EEPROM_CLKOUT2_HFD_HIGH`

```c
#define RV3032_EEPROM_CLKOUT2_HFD_HIGH GENMASK(4, 0)
```

<a id="af23af0f7502001b155ad787539f3686e"></a>

### `RV3032_EEPROM_CLKOUT2_OS`

```c
#define RV3032_EEPROM_CLKOUT2_OS BIT(7)
```

<a id="a1328b3e0d4f046e56ef32ad4791a6e71"></a>

### `RV3032_EEPROM_PMU_BSM`

```c
#define RV3032_EEPROM_PMU_BSM GENMASK(5, 4)
```

<a id="acab3e59acb465261946f11639125a426"></a>

### `RV3032_EEPROM_PMU_NCLKE`

```c
#define RV3032_EEPROM_PMU_NCLKE BIT(6)
```

<a id="a1b7732f0480f0efae5739a9b58f6fe2c"></a>

### `RV3032_EEPROM_PMU_TCM`

```c
#define RV3032_EEPROM_PMU_TCM GENMASK(1, 0)
```

<a id="a6e4e3e6f8f23486724a8f2e2e776a195"></a>

### `RV3032_EEPROM_PMU_TCR`

```c
#define RV3032_EEPROM_PMU_TCR GENMASK(3, 2)
```

<a id="a0aac524189c87622d6c47f52ba2170be"></a>

### `RV3032_EVI_CONTROL`

```c
#define RV3032_EVI_CONTROL 0x15
```

<a id="ae89750f5b77b2c3de7e85ff8aea9114e"></a>

### `RV3032_HOURS_12H_MASK`

```c
#define RV3032_HOURS_12H_MASK GENMASK(4, 0)
```

<a id="a05f8db72c25fd24fd390e9a5e5922a6c"></a>

### `RV3032_HOURS_24H_MASK`

```c
#define RV3032_HOURS_24H_MASK GENMASK(5, 0)
```

<a id="a44b32cbcdd1f312c81840e67faab117b"></a>

### `RV3032_HOURS_AMPM`

```c
#define RV3032_HOURS_AMPM BIT(5)
```

<a id="a3dd861e1676fd4b5437ce609f1a0c1fa"></a>

### `RV3032_MINUTES_MASK`

```c
#define RV3032_MINUTES_MASK GENMASK(6, 0)
```

<a id="a918eaa86a4f197352e92b40e73b324c8"></a>

### `RV3032_MONTH_MASK`

```c
#define RV3032_MONTH_MASK GENMASK(4, 0)
```

<a id="a14de9e930d633a318721225a9b1b2aa0"></a>

### `RV3032_MONTH_OFFSET`

```c
#define RV3032_MONTH_OFFSET 1
```

<a id="afe5b888e8eecb1bfd862e00184392291"></a>

### `RV3032_REG_100TH_SECONDS`

```c
#define RV3032_REG_100TH_SECONDS 0x00
```

<a id="a59889f4ae3de18fd04550350eb7a0c95"></a>

### `RV3032_REG_ALARM_DATE`

```c
#define RV3032_REG_ALARM_DATE 0x0A
```

<a id="a2ca9f1e7707d2e8cfa66813ff160b9e3"></a>

### `RV3032_REG_ALARM_HOURS`

```c
#define RV3032_REG_ALARM_HOURS 0x09
```

<a id="a24124061c8e21a38bd64bbaab12e35c8"></a>

### `RV3032_REG_ALARM_MINUTES`

```c
#define RV3032_REG_ALARM_MINUTES 0x08
```

<a id="ac278485d71352f8abd73bf5e9a35c384"></a>

### `RV3032_REG_CONTROL1`

```c
#define RV3032_REG_CONTROL1 0x10
```

<a id="a1fc6b1ede3ed031b03693f5ae2f2c2f9"></a>

### `RV3032_REG_CONTROL2`

```c
#define RV3032_REG_CONTROL2 0x11
```

<a id="a724b6a7719d65563ff51b656a4d7636d"></a>

### `RV3032_REG_CONTROL3`

```c
#define RV3032_REG_CONTROL3 0x12
```

<a id="a3f60f85c074723cbfacb5a56fca94126"></a>

### `RV3032_REG_DATE`

```c
#define RV3032_REG_DATE 0x05
```

<a id="ac54fb5fc0100af9dc5922bfaebf5eee6"></a>

### `RV3032_REG_EEPROM_ADDRESS`

```c
#define RV3032_REG_EEPROM_ADDRESS 0x3D
```

<a id="a455ae7d58405f883c7b0e08cade19ae6"></a>

### `RV3032_REG_EEPROM_CLKOUT1`

```c
#define RV3032_REG_EEPROM_CLKOUT1 0xC2
```

<a id="a7032e025dcfe811662f8d191ca9987e5"></a>

### `RV3032_REG_EEPROM_CLKOUT2`

```c
#define RV3032_REG_EEPROM_CLKOUT2 0xC3
```

<a id="ac850dda27873ce75dfd9527acc5063b1"></a>

### `RV3032_REG_EEPROM_COMMAND`

```c
#define RV3032_REG_EEPROM_COMMAND 0x3F
```

<a id="ad8342d74b1332c2078d8f48fe5c4b4e1"></a>

### `RV3032_REG_EEPROM_DATA`

```c
#define RV3032_REG_EEPROM_DATA 0x3E
```

<a id="a34439445411cfb9c3b644bf7756a0f14"></a>

### `RV3032_REG_EEPROM_OFFSET`

```c
#define RV3032_REG_EEPROM_OFFSET 0xC1
```

<a id="a68ac6c2258db13df7f064aad652c0e02"></a>

### `RV3032_REG_EEPROM_PMU`

```c
#define RV3032_REG_EEPROM_PMU 0xC0
```

<a id="adb45311f8f2390bb78469bf589a7d90a"></a>

### `RV3032_REG_EEPROM_RAM1`

```c
#define RV3032_REG_EEPROM_RAM1 0x40
```

<a id="aef94f7ffe42778fb8f46ba9748d7594b"></a>

### `RV3032_REG_EEPROM_TREF0`

```c
#define RV3032_REG_EEPROM_TREF0 0xC4
```

<a id="a8ea2f9d479487e8c2904450fb1d4a236"></a>

### `RV3032_REG_EEPROM_TREF1`

```c
#define RV3032_REG_EEPROM_TREF1 0xC5
```

<a id="ac1c3416d9387c31a70429c7c4ff5c7fc"></a>

### `RV3032_REG_HOURS`

```c
#define RV3032_REG_HOURS 0x03
```

<a id="a6bab443072d3d3984f2eaf59171b229e"></a>

### `RV3032_REG_MINUTES`

```c
#define RV3032_REG_MINUTES 0x02
```

<a id="a6c264b9a68cd8af686382033ff1af1c9"></a>

### `RV3032_REG_MONTH`

```c
#define RV3032_REG_MONTH 0x06
```

<a id="a9f7a8ea2eb5b3aa4298289e0f897a88a"></a>

### `RV3032_REG_SECONDS`

```c
#define RV3032_REG_SECONDS 0x01
```

<a id="a0af01504b507738cf6e2975e3778089e"></a>

### `RV3032_REG_STATUS`

```c
#define RV3032_REG_STATUS 0x0D
```

<a id="a4aa1028ef055a6fd32385006bc5618b5"></a>

### `RV3032_REG_TEMP_HIGH_THLD`

```c
#define RV3032_REG_TEMP_HIGH_THLD 0x17
```

<a id="a0987b8df0c15f146874be00d6c6a2286"></a>

### `RV3032_REG_TEMP_LOW_THLD`

```c
#define RV3032_REG_TEMP_LOW_THLD 0x16
```

<a id="ac905325f7cff95a69ae66af1713769a9"></a>

### `RV3032_REG_TEMPERATURE_LSB`

```c
#define RV3032_REG_TEMPERATURE_LSB 0x0E
```

<a id="adea8e22cfb7397223a58d6cf0235d378"></a>

### `RV3032_REG_TEMPERATURE_MSB`

```c
#define RV3032_REG_TEMPERATURE_MSB 0x0F
```

<a id="a0deb81df4d4b8acf6615282774f0a988"></a>

### `RV3032_REG_TIMER_VALUE_0`

```c
#define RV3032_REG_TIMER_VALUE_0 0x0B
```

<a id="a34838817c7baf68e9032f62a5f386f46"></a>

### `RV3032_REG_TIMER_VALUE_1`

```c
#define RV3032_REG_TIMER_VALUE_1 0x0C
```

<a id="ab940d4ad60eac8a38e48ca8b74a7a125"></a>

### `RV3032_REG_WEEKDAY`

```c
#define RV3032_REG_WEEKDAY 0x04
```

<a id="a4afd75ccc6710b3c5c1641490a92b6d3"></a>

### `RV3032_REG_YEAR`

```c
#define RV3032_REG_YEAR 0x07
```

<a id="a53ef32b486a7d3c0ded16aa29d434f1e"></a>

### `RV3032_SECONDS_MASK`

```c
#define RV3032_SECONDS_MASK GENMASK(6, 0)
```

<a id="a13aa871407da6f68e40358b4ab76c6fb"></a>

### `RV3032_STATUS_AF`

```c
#define RV3032_STATUS_AF BIT(3)
```

<a id="a4a9107dc3b87d239bb7a9c428756ff02"></a>

### `RV3032_STATUS_EVF`

```c
#define RV3032_STATUS_EVF BIT(2)
```

<a id="a8e3b0327b5999b370e8906ce05cac31e"></a>

### `RV3032_STATUS_PORF`

```c
#define RV3032_STATUS_PORF BIT(1)
```

<a id="acf1bf73cfda6a7542fac2d32de61ec68"></a>

### `RV3032_STATUS_TF`

```c
#define RV3032_STATUS_TF BIT(4)
```

<a id="afc3c323cb98cb513c0d14802a6573b18"></a>

### `RV3032_STATUS_THF`

```c
#define RV3032_STATUS_THF BIT(7)
```

<a id="a52580fa936730fe8c949f337fbce0067"></a>

### `RV3032_STATUS_TLF`

```c
#define RV3032_STATUS_TLF BIT(6)
```

<a id="a6959f1f463d9f59ebe4217962835a3d0"></a>

### `RV3032_STATUS_UF`

```c
#define RV3032_STATUS_UF BIT(5)
```

<a id="aed140542291595c08434d8d5cc8556c2"></a>

### `RV3032_STATUS_VLF`

```c
#define RV3032_STATUS_VLF BIT(0)
```

<a id="aa588e97e0fb2d5ac17d501ca81019cd6"></a>

### `RV3032_TEMPERATURE_BSF`

```c
#define RV3032_TEMPERATURE_BSF BIT(0)
```

<a id="a0feb5278fd3a8cdbd2d6a6e00939a222"></a>

### `RV3032_TEMPERATURE_CLKF`

```c
#define RV3032_TEMPERATURE_CLKF BIT(1)
```

<a id="aeac399f30a5d8639876173c9668315b9"></a>

### `RV3032_TEMPERATURE_EEBUSY`

```c
#define RV3032_TEMPERATURE_EEBUSY BIT(2)
```

<a id="a7e8a22024424fc8649f41f941952b6d1"></a>

### `RV3032_TEMPERATURE_EEF`

```c
#define RV3032_TEMPERATURE_EEF BIT(3)
```

<a id="af40f6c4e9f6212edf0c6ea04ae494440"></a>

### `RV3032_TEMPERATURE_TEMP_LSB`

```c
#define RV3032_TEMPERATURE_TEMP_LSB GENMASK(7, 4)
```

<a id="ade46a500e6a8ac675a479f1ad355e407"></a>

### `RV3032_TS_CTRL`

```c
#define RV3032_TS_CTRL 0x13
```

<a id="a90e99ab54c2dce004732a5630aef354d"></a>

### `RV3032_WEEKDAY_MASK`

```c
#define RV3032_WEEKDAY_MASK GENMASK(2, 0)
```

<a id="a763c742c8c80124b8fc0680d4241243d"></a>

### `RV3032_YEAR_MASK`

```c
#define RV3032_YEAR_MASK GENMASK(7, 0)
```

<a id="a8ac0a11e501e0fe1b3d0567c1bdd9694"></a>

### `RV3032_YEAR_OFFSET`

```c
#define RV3032_YEAR_OFFSET (2000 - 1900)
```

<a id="af38501b5aa1350ebc2c03be9b6623353"></a>

### `child_isr_t`

```c
typedef void(* child_isr_t) (const struct device *dev)
```

<a id="ae4d56fd30130dc4f332ecf43465a1558"></a>

### `child_dev`

```c
enum child_dev
```

RV3032 的子设备（Child Device）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `RV3032_DEV_REG` |  |
| `RV3032_DEV_RTC_ALARM` |  |
| `RV3032_DEV_RTC_UPDATE` |  |
| `RV3032_DEV_COUNTER` |  |
| `RV3032_DEV_SENSOR` |  |
| `RV3032_DEV_MAX` |  |

<a id="abc0539b1fcc8cf64617c13bb4749b77c"></a>

### `mfd_rv3032_eeprom_refresh()`

```c
int mfd_rv3032_eeprom_refresh ( const struct device * dev)
```

从 EEPROM 加载配置寄存器（Config Register）。

将配置寄存器（Config Register）从 EEPROM 加载到 RAM。必须先调用 `mfd_rv3032_enter_eerd`；内部会调用 `mfd_rv3032_exit_eerd`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | RV3032 多功能设备（MFD）。 |

**返回（Returns）**：返回值：成功返回 0，否则返回负错误码。

<a id="a4bb87fbf0d3c5d50138e8444a956b812"></a>

### `mfd_rv3032_eeprom_update()`

```c
int mfd_rv3032_eeprom_update ( const struct device * dev)
```

将配置寄存器（Config Register）提交到 EEPROM。

将配置寄存器（Config Register）持久保存到 EEPROM。必须先调用 `mfd_rv3032_enter_eerd`；内部会调用 `mfd_rv3032_exit_eerd`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | RV3032 多功能设备（MFD）。 |

**返回（Returns）**：返回值：成功返回 0，否则返回负错误码。

<a id="a2248379fbd15362aa8c701498deacca4"></a>

### `mfd_rv3032_eeprom_write_one()`

```c
int mfd_rv3032_eeprom_write_one ( const struct device * dev, uint8_t addr, uint8_t val )
```

向 EEPROM 写入一个字节（Byte）。

向 EEPROM 写入一个字节，不改变 RAM 中的值。必须先调用 `mfd_rv3032_enter_eerd`；内部会调用 `mfd_rv3032_exit_eerd`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | RV3032 多功能设备（MFD）。 |
| `addr` | EEPROM 寄存器地址（Register Address）。 |
| `val` | 要写入的值。 |

**返回（Returns）**：返回值：成功返回 0，否则返回负错误码。

<a id="a54576af433c288a6ae9e82523781b0e9"></a>

### `mfd_rv3032_enter_eerd()`

```c
int mfd_rv3032_enter_eerd ( const struct device * dev)
```

锁定 EEPROM 互斥锁（Mutex），并禁用 EEPROM 自动刷新（Autorefresh）。

在执行任何 EEPROM 操作之前调用。EEPROM 操作会在内部调用 `mfd_rv3032_exit_eerd`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | RV3032 多功能设备（MFD）。 |

**返回（Returns）**：返回值：成功返回 0，否则返回负错误码。

<a id="ab517e214d31f981cbda89144cc673f35"></a>

### `mfd_rv3032_exit_eerd()`

```c
int mfd_rv3032_exit_eerd ( const struct device * dev)
```

解锁 EEPROM 互斥锁（Mutex），并启用 EEPROM 自动刷新（Autorefresh）。

通常不需要显式调用，EEPROM 函数会在内部调用它。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | RV3032 多功能设备（MFD）。 |

**返回（Returns）**：返回值：成功返回 0，否则返回负错误码。

<a id="a822141bf579338c3b66a0f62233c4b80"></a>

### `mfd_rv3032_read_reg8()`

```c
int mfd_rv3032_read_reg8 ( const struct device * dev, uint8_t addr, uint8_t * val )
```

<a id="a3f1be094ac698ce0f41d147d63ceca79"></a>

### `mfd_rv3032_read_regs()`

```c
int mfd_rv3032_read_regs ( const struct device * dev, uint8_t addr, void * buf, size_t len )
```

<a id="a7d630d2e9e6b76969ba2af9d833736ee"></a>

### `mfd_rv3032_set_irq_handler()`

```c
void mfd_rv3032_set_irq_handler ( const struct device * dev, const struct device * child_dev, enum child_dev child_idx, child_isr_t handler )
```

<a id="af17edb1eb921a050307cf02c5bb46590"></a>

### `mfd_rv3032_update_cfg()`

```c
int mfd_rv3032_update_cfg ( const struct device * dev, uint8_t addr, uint8_t mask, uint8_t val )
```

对寄存器执行读－改－写（RMW）更新，并提交到电可擦可编程只读存储器（EEPROM）。

更新 RAM 寄存器并提交到 EEPROM。不要调用 `mfd_rv3032_enter_eerd`，内部会自行调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | RV3032 多功能设备（MFD）。 |
| `addr` | 寄存器地址（Register Address）。 |
| `mask` | 掩码值（Mask Value）。 |
| `val` | 要写入的值。 |

**返回（Returns）**：返回值：成功返回 0，否则返回负错误码。

<a id="a0690ef025e4ebe7fa96818b18dbe81cb"></a>

### `mfd_rv3032_update_reg8()`

```c
int mfd_rv3032_update_reg8 ( const struct device * dev, uint8_t addr, uint8_t mask, uint8_t val )
```

<a id="a209ce7f7823aef8c4fd013ebfdfe031f"></a>

### `mfd_rv3032_update_status()`

```c
int mfd_rv3032_update_status ( const struct device * dev, uint8_t mask, uint8_t val )
```

对状态寄存器执行读－改－写（RMW）更新。

更新状态寄存器（Status Register）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | RV3032 多功能设备（MFD）。 |
| `mask` | 掩码值（Mask Value）。 |
| `val` | 要写入的值。 |

**返回（Returns）**：返回值：成功返回状态寄存器的新值，否则返回负错误码。

<a id="a27a9c24a7590b583259ac7f030642d0c"></a>

### `mfd_rv3032_write_reg8()`

```c
int mfd_rv3032_write_reg8 ( const struct device * dev, uint8_t addr, uint8_t val )
```

<a id="a114cd42a12443e1e7ee0339ee22c3fb1"></a>

### `mfd_rv3032_write_regs()`

```c
int mfd_rv3032_write_regs ( const struct device * dev, uint8_t addr, void * buf, size_t len )
```


## 11.6\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_system_reference/P038_rv3032.h_源码浏览.md)
- [GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [child_dev](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gae4d56fd30130dc4f332ecf43465a1558)
- [child_isr_t](../api_file_reference/P281_zephyr__drivers__mfd__nxp_lp_flexcomm.h_文件参考.md#af38501b5aa1350ebc2c03be9b6623353)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="arv3032_8h_html_a209ce7f7823aef8c4fd013ebfdfe031f"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ae4d56fd30130dc4f332ecf43465a1558a7eab30c06b62ba3fd05aa6b17de65664"></a>
<a id="ae4d56fd30130dc4f332ecf43465a1558a9cb8727d9c721d301fe0f868b2ac4f6f"></a>
<a id="ae4d56fd30130dc4f332ecf43465a1558ad728f5a0673370137d421fc1636a97a4"></a>
<a id="ae4d56fd30130dc4f332ecf43465a1558a04ef64de3b15eb1183b1c05b0a7b14e1"></a>
<a id="ae4d56fd30130dc4f332ecf43465a1558a0a0db910452cc15f25178419fcb3f70a"></a>
<a id="ae4d56fd30130dc4f332ecf43465a1558ac6dce8a07e4ca4c3927f895b65138c57"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P010_zephyr__drivers__clock_control__nrf_clock_control.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P012_zephyr__video__video.h_文件参考.md)
