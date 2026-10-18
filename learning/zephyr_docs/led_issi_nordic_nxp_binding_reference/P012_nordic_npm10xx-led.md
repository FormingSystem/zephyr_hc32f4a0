---
id: learning.zephyr-docs.led-issi-nordic-nxp-binding-reference.page-12
title: nordic_npm10xx-led
kind: reference
status: maintained
domains: [zephyr, devicetree, led]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/led/nordic,npm10xx-led.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第12章\_nordic_npm10xx-led

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/led/nordic,npm10xx-led.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="nordic-npm10xx-led"></a>
<a id="dtbinding-nordic-npm10xx-led"></a>
<a id="std-dtcompatible-nordic-npm10xx-led"></a>

兼容字符串（Compatible String）：`nordic,npm10xx-led`。厂商：[ Nordic Semiconductor ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-nordic)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=nordic,npm10xx-led)。

驱动源码（Driver Source）：[drivers/led/led_npm10xx.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led/led_npm10xx.c)。

<a id="description"></a>

Nordic nPM10系列电源管理集成电路（Power Management Integrated Circuit，PMIC）的LED驱动器（LED Driver）。

Nordic nPM10系列PMIC的LED驱动输出与通用输入输出（General-Purpose Input/Output，GPIO）引脚复用。每个LED子节点通过 `index` 属性指定使用的GPIO编号，因此必须提供该属性。对已经配置为LED的GPIO使用GPIO接口会产生未定义行为（Undefined Behaviour），必须避免。

每个LED都可以由主机片上系统（System on Chip，SoC）控制，也可以自动控制。使用自动模式时，软件只能调节该LED的亮度；`error` 模式是例外，完全不允许软件控制。

硬件限制：传入 `led_blink` API的亮、灭延时由所有LED实例共享，因此不支持不同LED使用不同的闪烁延时。

<a id="examples"></a>

官方设备树配置原例：

```dts
npm1012: pmic@6a {
  /* ... */

  leds {
    compatible = "nordic,npm10xx-led";
    pwm-freq-hz = <488>;

    charge_indicator: led0 {
      index = <1>;
      label = "Charge indication LED on GPIO1";
      led-mode = "charge";
    };

    user_led: led1 {
      index = <0>;
      label = "Red LED on GPIO0";
      drive-current-ma = <10>;
    };
  };

  /* ... */
};
```

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

<a id="top-level-properties"></a>

## 12.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `pwm-freq-hz` | `int` | PWM频率（Frequency），单位为赫兹（Hz）。；默认值：`977`；合法值：`122, 244, 488, 977` |
| `phase-shift-enable` | `boolean` | 启用相位偏移（Phase Shifting），以减小峰值负载电流。在RGB等多个LED同时工作的场景中很有用。 |
| `blink-mode` | `string` | 执行闪烁任务（Blink Task）时，单次闪烁、双次闪烁或持续闪烁。；默认值：`forever`；合法值：`single, double, forever` |

本页没有已弃用的节点专用属性。

<a id="child-node-properties"></a>

## 子节点属性

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `index` | `int` | **必需**。LED在控制器上的索引（Index）。驱动或应用可用它将逻辑LED映射到控制器上的实际位置。例如，当灯阵或灯带上的LED接线顺序与控制器的LED顺序不一致时，可通过此属性建立对应关系。；合法值：`0, 1, 2` |
| `led-mode` | `string` | LED工作模式（Operation Mode）：`host` 通过LED设备驱动API控制亮灭、闪烁与亮度；`charge` 指示充电状态，允许调节亮度；`error` 指示充电错误，不允许任何控制；`vbus-good` 指示 `VBUS GOOD` 状态，允许调节亮度。；默认值：`host`；合法值：`host, charge, error, vbus-good` |
| `drive-current-ma` | `int` | LED驱动电流（Drive Strength），单位为毫安（mA）。；默认值：`5`；合法值：`5, 10` |
| `label` | `string` | 描述LED的可读字符串（Human-Readable String）。应用可用它识别LED，或取得此LED在父设备上的编号／索引，即子节点编号（Child Node Number）。 |
| `color-mapping` | `array` | 多色LED的通道到颜色映射（Channel-to-Color Mapping）。当LED支持多种颜色时，`color-mapping` 描述硬件通道与颜色的对应关系。RGB LED的原例按红、绿、蓝顺序映射，完整配置见后面的原始代码。 |

## RGB通道映射原例

```dts
   color-mapping =
        <LED_COLOR_ID_RED>,
        <LED_COLOR_ID_GREEN>,
        <LED_COLOR_ID_BLUE>;
```

---

[上一章](P011_microchip_xec-bbled.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P013_nordic_npm1300-led.md)
