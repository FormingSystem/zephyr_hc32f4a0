---
id: learning.zephyr-docs.led-issi-nordic-nxp-binding-reference.page-3
title: dac-leds
kind: reference
status: maintained
domains: [zephyr, devicetree, led]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/led/dac-leds.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第3章\_dac-leds

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/led/dac-leds.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="dac-leds"></a>
<a id="dtbinding-dac-leds"></a>
<a id="std-dtcompatible-dac-leds"></a>

兼容字符串（Compatible String）：`dac-leds`。厂商：[ 无厂商前缀 ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-no-vendor)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=dac-leds)。

驱动源码（Driver Source）：[drivers/led/led_dac.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led/led_dac.c)。

<a id="description"></a>

由数模转换器（Digital-to-Analog Converter，DAC）控制的一组LED。每个LED都定义在 `dac-leds` 节点的一个子节点中。

<a id="examples"></a>

官方设备树配置原例：

```dts
/ {
        leds {
                compatible = "dac-leds";
                /* led_0 uses dac1 channel 0 with 12 bit resolution. */
                led_0 {
                        dac-dev = <&dac1>;
                        channel = <0>;
                        resolution = <12>;
                };
                /* led_1 uses dac1 channel 1 with 12 bit resolution and is setup to supply an
                 * LED directly.
                 */
                led_1 {
                        dac-dev = <&dac1>;
                        channel = <1>;
                        resolution = <12>;
                        voltage-min-brightness-mv = <1400>;
                        voltage-max-brightness-mv = <2700>;
                        voltage-max-dac-mv = <3300>;
                        output-buffer;
                };
        };
};
```

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

<a id="top-level-properties"></a>

## 3.1\_节点专用属性

这些属性不继承自基础绑定文件。

本页没有节点专用属性。

本页没有已弃用的节点专用属性。

<a id="child-node-properties"></a>

## 子节点属性

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `dac-dev` | `phandle` | **必需**。包含DAC节点引用（Phandle）的属性，例如 `&dac`。 |
| `channel` | `int` | **必需**。DAC通道（Channel）。 |
| `resolution` | `int` | **必需**。使用的DAC分辨率（Resolution）。 |
| `voltage-min-brightness-mv` | `int` | 亮度为0%时的电压（Voltage）。未指定时使用DAC的最小输出电压。 |
| `voltage-max-brightness-mv` | `int` | 亮度为100%时的电压（Voltage）。未指定时使用DAC的最大输出电压。 |
| `voltage-max-dac-mv` | `int` | DAC的最大输出电压（Maximum Output Voltage）。设置了 `voltage-min-brightness-mv` 或 `voltage-max-brightness-mv` 时必须提供此属性。 |
| `output-buffer` | `boolean` | 启用DAC输出缓冲器（Output Buffer）。使用DAC直接驱动LED时必须启用。 |

---

[上一章](P002_awinic_aw9523b-led.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P004_holtek_ht16k33.md)
