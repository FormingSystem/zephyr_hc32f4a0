---
id: learning.zephyr-docs.led-issi-nordic-nxp-binding-reference.page-10
title: leds-group-multicolor
kind: reference
status: maintained
domains: [zephyr, devicetree, led]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/led/leds-group-multicolor.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第10章\_leds-group-multicolor

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/led/leds-group-multicolor.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="leds-group-multicolor"></a>
<a id="dtbinding-leds-group-multicolor"></a>
<a id="std-dtcompatible-leds-group-multicolor"></a>

兼容字符串（Compatible String）：`leds-group-multicolor`。厂商：[ 无厂商前缀 ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-no-vendor)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=leds-group-multicolor)。

驱动源码（Driver Source）：[drivers/led/leds_group_multicolor.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led/leds_group_multicolor.c)。

<a id="description"></a>

将多个单色LED（Monochromatic LED）组合成一个多色LED（Multicolor LED）。

使用一组由脉宽调制（Pulse Width Modulation，PWM）控制的单色LED来定义RGB LED。注意，`pwms` 属性中的引用及说明符内容取决于PWM控制器型号。

<a id="examples"></a>

官方设备树配置原例：

```dts
/* Example where PWM controller is STM32 */
#include <zephyr/dt-bindings/led/led.h>

/ {
        monochromatic-leds {
                compatible = "pwm-leds";

                red_pwm_led: led-0 {
                        pwms = <&pwm1 1 PWM_MSEC(20) PWM_POLARITY_NORMAL>;
                };

                green_pwm_led: led-1 {
                        pwms = <&pwm2 1 PWM_MSEC(20) PWM_POLARITY_NORMAL>;
                };

                blue_pwm_led: led-2 {
                        pwms = <&pwm3 1 PWM_MSEC(20) PWM_POLARITY_NORMAL>;
                };
        };

        rgb-led {
                compatible = "leds-group-multicolor";

                leds = <&red_pwm_led>, <&green_pwm_led>, <&blue_pwm_led>;
                color-mapping = <LED_COLOR_ID_RED>,
                                <LED_COLOR_ID_GREEN>,
                                <LED_COLOR_ID_BLUE>;
        };
};
```

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 10.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `leds` | `phandles` | **必需**。单色LED节点引用（References to Monochromatic LED Nodes）。 |
| `color-mapping` | `array` | 多色LED的通道到颜色映射（Channel-to-Color Mapping）。当LED支持多种颜色时，`color-mapping` 描述硬件通道与颜色的对应关系。RGB LED的原例按红、绿、蓝顺序映射，完整配置见后面的原始代码。 |

本页没有已弃用的节点专用属性。

## 10.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `label` | `string` | 描述LED的可读字符串（Human-Readable String）。应用可用它识别LED，或取得此LED在父设备上的编号／索引，即子节点编号（Child Node Number）。 |

属性说明中的“重要属性”参见[设备树语法与结构](../devicetree/P003_语法与结构.md#dt-important-props)。

## RGB通道映射原例

```dts
   color-mapping =
        <LED_COLOR_ID_RED>,
        <LED_COLOR_ID_GREEN>,
        <LED_COLOR_ID_BLUE>;
```

---

[上一章](P009_issi_is31fl3733.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P011_microchip_xec-bbled.md)
