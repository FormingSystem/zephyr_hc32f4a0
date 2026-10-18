---
id: learning.zephyr-docs.led-strip-binding-reference.page-11
title: worldsemi_ws2812-rpi_pico-pio
kind: reference
status: maintained
domains: [zephyr, devicetree, led]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/led_strip/worldsemi,ws2812-rpi_pico-pio.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第11章\_worldsemi_ws2812-rpi_pico-pio

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/led_strip/worldsemi,ws2812-rpi_pico-pio.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="worldsemi-ws2812-rpi-pico-pio"></a>
<a id="dtbinding-worldsemi-ws2812-rpi-pico-pio"></a>
<a id="std-dtcompatible-worldsemi-ws2812-rpi_pico-pio"></a>

兼容字符串（Compatible String）：`worldsemi,ws2812-rpi_pico-pio`。厂商：[ Worldsemi ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-worldsemi)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=worldsemi,ws2812-rpi_pico-pio)。

驱动源码（Driver Source）：[drivers/led_strip/ws2812_rpi_pico_pio.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led_strip/ws2812_rpi_pico_pio.c)。

<a id="description"></a>

为WS2812配置的可编程I/O（Programmable I/O，PIO）节点。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

<a id="top-level-properties"></a>

## 11.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `bit-waveform` | `array` | 定义发送一位数据的波形，程序使用数组前三项T0、T1、T2。T0对应数据手册的T0H，T2对应T1L，T1对应`T1H-T0H`或`T0L-T1L`。0位的高、低时段分别为T0和T1+T2；1位分别为T0+T1和T2。<br>频率决定波形周期，T0至T2表示一个周期内的比例。例如T0=3、T1=3、T2=4且频率800 kHz时，`T0H = (1 / 800kHz) * (3/10) = 375ns`，`T0L = (1 / 800kHz) * ((4+3)/10) = 875ns`。下方保留波形字符图及计算原式。 |
| `pinctrl-0` | `phandles` | 第一个状态（State）的引脚配置（Pin Configuration），具体内容取决于所选引脚控制器驱动（Pin Controller Driver）的实现 |
| `pinctrl-1` | `phandles` | 第二个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-2` | `phandles` | 第三个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-3` | `phandles` | 第四个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-4` | `phandles` | 第五个状态的引脚配置，参见pinctrl-0 |
| `pinctrl-names` | `string-array` | 所提供状态的名称，名称数量必须与状态数量一致 |

本页没有已弃用的节点专用属性。

<a id="child-node-properties"></a>

## 子节点属性

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `gpios` | `phandle-array` | **必需**。继承自`ws2812-gpio.yaml`。本驱动不配置输出引脚，必须在父节点配置中使用pinctrl将引脚配置给PIO；本属性仅使用GPIO引脚号，忽略标志。 |
| `frequency` | `int` | 每秒发送代表一位数据的波形次数，等同于每秒位数。WS2812使用800000，WS2811应设为400000。 |
| `dmas` | `phandle-array` | 此灯带发送通道的DMA说明符。 |
| `dma-names` | `string-array` | DMA通道说明符的名称，此灯带必须使用`tx`。 |
| `reset-delay` | `int` | 确保灯带锁存（Latch）信号所需的最短等待时间，单位为µs。省略时默认8 µs。原文说明此默认值适用于WS2812：虽然其数据手册要求50 µs，但观察上约6 µs已经足够，因此默认取8 µs以留出裕量。；默认值：`8` |
| `chain-length` | `int` | **必需**。菊花链（Daisy Chain）中的设备数量。 |
| `color-mapping` | `array` | **必需**。通道到颜色的映射（Channel-to-Color Mapping），也称像素顺序（Pixel Order）。下方保留绿、红、蓝（GRB）顺序的原例。 |

## GRB颜色顺序原例

```dts
   color-mapping = <LED_COLOR_ID_GREEN
                    LED_COLOR_ID_RED
                    LED_COLOR_ID_BLUE>;
```

## PIO原始波形与计算

0位和1位的时序：

```text
Code-0
   +------+                 +---
   |      |                 |
   |  T0  |      T1+T2      |
   |      |                 |
---+      +-----------------+

Code-1
   +---------------+        +---
   |               |        |
   |     T0+T1     |   T2   |
   |               |        |
---+               +--------+
```

T0H原式：

```text
  (1 / 800kHz) * (3/10) = 375ns
```

T0L原式：

```text
  (1 / 800kHz) * ((4+3)/10) = 875ns
```

---

[上一章](P010_worldsemi_ws2812-pulse-io.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P012_worldsemi_ws2812-spi.md)
