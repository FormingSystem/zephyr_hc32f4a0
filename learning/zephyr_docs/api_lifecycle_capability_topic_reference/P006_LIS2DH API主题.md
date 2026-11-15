---
id: learning.zephyr-docs.api-lifecycle-capability-topic-reference.page-6
title: LIS2DH API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dh__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_LIS2DH API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dh__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

ST Microelectronics LIS2DH 三轴加速度计（3-axis accelerometer）。

<a id="details"></a>

ST Microelectronics LIS2DH 三轴加速度计（3-axis accelerometer）。

<a id="header-files"></a>
<a id="files"></a>

## 6.1\_文件（Files）

<a id="r_lis2dh_2Eh"></a>

```c
file lis2dh.h
```

相关声明：[lis2dh.h](../api_file_configuration_reference/P018_zephyr__drivers__sensor__lis2dh.h_文件参考.md)。

LIS2DH传感器的扩展API头文件（Extended Sensor API Header）。

```c
file lis2dh.h
```

相关声明：[lis2dh.h](../api_file_system_power_reference/P010_zephyr__dt-bindings__sensor__lis2dh.h_文件参考.md)。

the ST LIS2DH 3-axis accelerometer的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 6.2\_枚举（Enumerations）

<a id="r_ga3a36ff9fb1f811eb0c1ac853f8c27ddb"></a>

```c
enum lis2dh_self_test { LIS2DH_SELF_TEST_DISABLE = 0 , LIS2DH_SELF_TEST_POSITIVE = 1 , LIS2DH_SELF_TEST_NEGATIVE = 2 }
```

相关声明：[lis2dh_self_test](#ga3a36ff9fb1f811eb0c1ac853f8c27ddb)、[LIS2DH_SELF_TEST_DISABLE](#gga3a36ff9fb1f811eb0c1ac853f8c27ddbab79d3f8c64da49e84f2be95507a05e69)、[LIS2DH_SELF_TEST_POSITIVE](#gga3a36ff9fb1f811eb0c1ac853f8c27ddbabc46ce24eeb0bfdf8093de3806cf841e)、[LIS2DH_SELF_TEST_NEGATIVE](#gga3a36ff9fb1f811eb0c1ac853f8c27ddbaa1db870964cb2d719449484cd26f0b26)。

自定义属性（Custom Attribute）`SENSOR_ATTR_LIS2DH_SELF_TEST` 的可用值。

<a id="r_gaffedeefeb4d8ceda71760226eef1b5cd"></a>

```c
enum sensor_attribute_lis2dh { SENSOR_ATTR_LIS2DH_SELF_TEST = SENSOR_ATTR_PRIV_START }
```

相关声明：[sensor_attribute_lis2dh](#gaffedeefeb4d8ceda71760226eef1b5cd)、[SENSOR_ATTR_LIS2DH_SELF_TEST](#ggaffedeefeb4d8ceda71760226eef1b5cdaad1fac97ac7266eee389dff93cb9d8e6)。

LIS2DH 的自定义传感器属性（Custom Sensor Attributes）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 6.3\_GPIO 中断配置（Interrupt Configuration）

设备树属性（Devicetree Properties）`int1-gpio-config` 和 `int2-gpio-config` 的取值。

<a id="r_ga673dad0efc816668086fc88983c13cbb"></a>

```c
#define LIS2DH_DT_GPIO_INT_EDGE_BOTH 0
```

相关声明：[LIS2DH_DT_GPIO_INT_EDGE_BOTH](#ga673dad0efc816668086fc88983c13cbb)。

在信号的两个边沿（Both Signal Edges）均触发。

<a id="r_gafbf7948886682093cbc8034720bbabd5"></a>

```c
#define LIS2DH_DT_GPIO_INT_EDGE_RISING 1
```

相关声明：[LIS2DH_DT_GPIO_INT_EDGE_RISING](#gafbf7948886682093cbc8034720bbabd5)。

在上升沿（Rising Edge）触发。

<a id="r_ga61b4f2c56b4bc253148340c52b1dca74"></a>

```c
#define LIS2DH_DT_GPIO_INT_EDGE_FALLING 2
```

相关声明：[LIS2DH_DT_GPIO_INT_EDGE_FALLING](#ga61b4f2c56b4bc253148340c52b1dca74)。

在下降沿（Falling Edge）触发。

<a id="r_ga044d5fee79faaafcb2ed0363cce9329c"></a>

```c
#define LIS2DH_DT_GPIO_INT_LEVEL_HIGH 3
```

相关声明：[LIS2DH_DT_GPIO_INT_LEVEL_HIGH](#ga044d5fee79faaafcb2ed0363cce9329c)。

在信号为高电平（High）时触发。

<a id="r_ga06837f6473ace3107383e076903fde19"></a>

```c
#define LIS2DH_DT_GPIO_INT_LEVEL_LOW 4
```

相关声明：[LIS2DH_DT_GPIO_INT_LEVEL_LOW](#ga06837f6473ace3107383e076903fde19)。

在信号为低电平（Low）时触发。

## 6.4\_任意运动检测模式（Any-motion Detection Mode）

设备树属性（Devicetree Property）`anym-mode` 的取值。

<a id="r_ga97fdffadeb9f76118134e9c1bc1e1fb5"></a>

```c
#define LIS2DH_DT_ANYM_OR_COMBINATION 0
```

相关声明：[LIS2DH_DT_ANYM_OR_COMBINATION](#ga97fdffadeb9f76118134e9c1bc1e1fb5)。

对已启用轴进行逻辑或组合（OR Combination）。

<a id="r_ga236b804ce12742583a07dd7e342467a3"></a>

```c
#define LIS2DH_DT_ANYM_6D_MOVEMENT 1
```

相关声明：[LIS2DH_DT_ANYM_6D_MOVEMENT](#ga236b804ce12742583a07dd7e342467a3)。

六方向运动识别（6-direction Movement Recognition）。

<a id="r_gaddcd38964fcc1d465fa6d5b4a09ee47a"></a>

```c
#define LIS2DH_DT_ANYM_AND_COMBINATION 2
```

相关声明：[LIS2DH_DT_ANYM_AND_COMBINATION](#gaddcd38964fcc1d465fa6d5b4a09ee47a)。

对已启用轴进行逻辑与组合（AND Combination）。

<a id="r_ga78a545b550b5ec39729cf283afb676ae"></a>

```c
#define LIS2DH_DT_ANYM_6D_POSITION 3
```

相关声明：[LIS2DH_DT_ANYM_6D_POSITION](#ga78a545b550b5ec39729cf283afb676ae)。

六方向位置识别（6-direction Position Recognition）。

## 6.5\_详细说明（Detailed Documentation）

<a id="ga236b804ce12742583a07dd7e342467a3"></a>

### `LIS2DH_DT_ANYM_6D_MOVEMENT`

```c
#define LIS2DH_DT_ANYM_6D_MOVEMENT 1
```

```c
#include <zephyr/dt-bindings/sensor/lis2dh.h>
```

六方向运动识别（6-direction Movement Recognition）。

<a id="ga78a545b550b5ec39729cf283afb676ae"></a>

### `LIS2DH_DT_ANYM_6D_POSITION`

```c
#define LIS2DH_DT_ANYM_6D_POSITION 3
```

```c
#include <zephyr/dt-bindings/sensor/lis2dh.h>
```

六方向位置识别（6-direction Position Recognition）。

<a id="gaddcd38964fcc1d465fa6d5b4a09ee47a"></a>

### `LIS2DH_DT_ANYM_AND_COMBINATION`

```c
#define LIS2DH_DT_ANYM_AND_COMBINATION 2
```

```c
#include <zephyr/dt-bindings/sensor/lis2dh.h>
```

对已启用轴进行逻辑与组合（AND Combination）。

<a id="ga97fdffadeb9f76118134e9c1bc1e1fb5"></a>

### `LIS2DH_DT_ANYM_OR_COMBINATION`

```c
#define LIS2DH_DT_ANYM_OR_COMBINATION 0
```

```c
#include <zephyr/dt-bindings/sensor/lis2dh.h>
```

对已启用轴进行逻辑或组合（OR Combination）。

<a id="ga673dad0efc816668086fc88983c13cbb"></a>

### `LIS2DH_DT_GPIO_INT_EDGE_BOTH`

```c
#define LIS2DH_DT_GPIO_INT_EDGE_BOTH 0
```

```c
#include <zephyr/dt-bindings/sensor/lis2dh.h>
```

在信号的两个边沿（Both Signal Edges）均触发。

<a id="ga61b4f2c56b4bc253148340c52b1dca74"></a>

### `LIS2DH_DT_GPIO_INT_EDGE_FALLING`

```c
#define LIS2DH_DT_GPIO_INT_EDGE_FALLING 2
```

```c
#include <zephyr/dt-bindings/sensor/lis2dh.h>
```

在下降沿（Falling Edge）触发。

<a id="gafbf7948886682093cbc8034720bbabd5"></a>

### `LIS2DH_DT_GPIO_INT_EDGE_RISING`

```c
#define LIS2DH_DT_GPIO_INT_EDGE_RISING 1
```

```c
#include <zephyr/dt-bindings/sensor/lis2dh.h>
```

在上升沿（Rising Edge）触发。

<a id="ga044d5fee79faaafcb2ed0363cce9329c"></a>

### `LIS2DH_DT_GPIO_INT_LEVEL_HIGH`

```c
#define LIS2DH_DT_GPIO_INT_LEVEL_HIGH 3
```

```c
#include <zephyr/dt-bindings/sensor/lis2dh.h>
```

在信号为高电平（High）时触发。

<a id="ga06837f6473ace3107383e076903fde19"></a>

### `LIS2DH_DT_GPIO_INT_LEVEL_LOW`

```c
#define LIS2DH_DT_GPIO_INT_LEVEL_LOW 4
```

```c
#include <zephyr/dt-bindings/sensor/lis2dh.h>
```

在信号为低电平（Low）时触发。

<a id="ga3a36ff9fb1f811eb0c1ac853f8c27ddb"></a>

### `lis2dh_self_test`

```c
enum lis2dh_self_test
```

```c
#include <zephyr/drivers/sensor/lis2dh.h>
```

自定义属性（Custom Attribute）`SENSOR_ATTR_LIS2DH_SELF_TEST` 的可用值。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `LIS2DH_SELF_TEST_DISABLE` | 禁用自检（Self-test Disabled）。 |
| `LIS2DH_SELF_TEST_POSITIVE` | 模拟正方向加速度（Positive-direction Acceleration）。 |
| `LIS2DH_SELF_TEST_NEGATIVE` | 模拟负方向加速度（Negative-direction Acceleration）。 |

<a id="gaffedeefeb4d8ceda71760226eef1b5cd"></a>

### `sensor_attribute_lis2dh`

```c
enum sensor_attribute_lis2dh
```

```c
#include <zephyr/drivers/sensor/lis2dh.h>
```

LIS2DH 的自定义传感器属性（Custom Sensor Attributes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_ATTR_LIS2DH_SELF_TEST` | 设置自检模式（Self-test Mode）。向传感器施加静电力（Electrostatic Force）以模拟加速度，无需实际移动设备。使用 `lis2dh_self_test` 中的值，通过 `sensor_value.val1` 字段传入。 |


## 6.6\_原页交叉引用（Cross References）

- [lis2dh.h](../api_file_configuration_reference/P018_zephyr__drivers__sensor__lis2dh.h_文件参考.md)
- [lis2dh.h](../api_file_system_power_reference/P010_zephyr__dt-bindings__sensor__lis2dh.h_文件参考.md)
- [sensor_value.val1](../sensor_navigation_model_reference/P055_sensor_value_结构体.md#af21dddb084da4c42a7e77b48edf26fbe)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga3a36ff9fb1f811eb0c1ac853f8c27ddbab79d3f8c64da49e84f2be95507a05e69"></a>
<a id="gga3a36ff9fb1f811eb0c1ac853f8c27ddbabc46ce24eeb0bfdf8093de3806cf841e"></a>
<a id="gga3a36ff9fb1f811eb0c1ac853f8c27ddbaa1db870964cb2d719449484cd26f0b26"></a>
<a id="ggaffedeefeb4d8ceda71760226eef1b5cdaad1fac97ac7266eee389dff93cb9d8e6"></a>

---

[上一章](P005_ICM42688 API主题.md) · [返回大纲](大纲.md) · [下一章](P007_文件系统管理（File System Management）.md)
