---
id: learning.zephyr-docs.led-strip-binding-reference.page-10
title: worldsemi_ws2812-pulse-io
kind: reference
status: maintained
domains: [zephyr, devicetree, led]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/led_strip/worldsemi,ws2812-pulse-io.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第10章\_worldsemi_ws2812-pulse-io

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/led_strip/worldsemi,ws2812-pulse-io.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="worldsemi-ws2812-pulse-io"></a>
<a id="dtbinding-worldsemi-ws2812-pulse-io"></a>
<a id="std-dtcompatible-worldsemi-ws2812-pulse-io"></a>

兼容字符串（Compatible String）：`worldsemi,ws2812-pulse-io`。厂商：[ Worldsemi ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-worldsemi)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=worldsemi,ws2812-pulse-io)。

驱动源码（Driver Source）：[drivers/led_strip/ws2812_pulse_io.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led_strip/ws2812_pulse_io.c)。

<a id="description"></a>

Worldsemi WS2812 LED灯带的脉冲I/O（pulse_io）绑定，通过工作于CELL模式的控制器通道驱动WS2812及兼容灯带。

<a id="examples"></a>

官方设备树配置原例：

```dts
/ {
      led_strip: ws2812 {
          compatible = "worldsemi,ws2812-pulse-io";
          pulse-ios = <&rmt 0>;
          chain-length = <1>;
          color-mapping = <LED_COLOR_ID_GREEN
                           LED_COLOR_ID_RED
                           LED_COLOR_ID_BLUE>;
      };
};
```

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 10.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `pulse-ios` | `phandle-array` | **必需**。驱动灯带数据线的pulse_io控制器及发送通道；引脚通过控制器的pinctrl状态路由。 |
| `reset-delay` | `int` | 确保灯带锁存（Latch）信号所需的最短等待时间，单位为µs。省略时默认8 µs。原文说明此默认值适用于WS2812：虽然其数据手册要求50 µs，但观察上约6 µs已经足够，因此默认取8 µs以留出裕量。；默认值：`8` |
| `chain-length` | `int` | **必需**。菊花链（Daisy Chain）中的设备数量。 |
| `color-mapping` | `array` | **必需**。通道到颜色的映射（Channel-to-Color Mapping），也称像素顺序（Pixel Order）。下方保留绿、红、蓝（GRB）顺序的原例。 |

本页没有已弃用的节点专用属性。

## GRB颜色顺序原例

```dts
   color-mapping = <LED_COLOR_ID_GREEN
                    LED_COLOR_ID_RED
                    LED_COLOR_ID_BLUE>;
```

---

[上一章](P009_worldsemi_ws2812-i2s.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P011_worldsemi_ws2812-rpi_pico-pio.md)
