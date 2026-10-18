---
id: learning.zephyr-docs.stepper-binding-reference.page-12
title: allegro_a4979
kind: reference
status: maintained
domains: [zephyr, devicetree, stepper]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/stepper/allegro/allegro,a4979.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第12章\_allegro_a4979

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/stepper/allegro/allegro,a4979.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="allegro-a4979"></a>
<a id="dtbinding-allegro-a4979"></a>
<a id="std-dtcompatible-allegro-a4979"></a>

兼容字符串（Compatible String）：`allegro,a4979`。厂商：[ Allegro MicroSystems ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-allegro)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=allegro,a4979)。

驱动源码（Driver Source）：[drivers/stepper/allegro/a4979.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/stepper/allegro/a4979.c)。

<a id="description"></a>

Allegro A4979微步步进电机驱动器（Microstepping Stepper Motor Driver）。该器件具有灵活的微步控制和内置转换器（Translator），便于操作，设计用于以整步、半步、四分之一步及十六分之一步模式驱动双极性步进电机。

<a id="examples"></a>

官方设备树示例（Devicetree Example）：

```dts
a4979: a4979 {
    status = "okay";
    compatible = "allegro,a4979";
    micro-step-res = <2>;
    reset-gpios = <&gpiod 10 GPIO_ACTIVE_HIGH>;
    en-gpios = <&gpiod 11 GPIO_ACTIVE_HIGH>;
    m0-gpios = <&gpiod 13 0>;
    m1-gpios = <&gpiod 12 0>;
};
```

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 12.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `step-width-ns` | `int` | 步进信号（Step Signal）的最小脉冲宽度，单位为纳秒（ns）。；默认值：`1000` |
| `reset-gpios` | `phandle-array` | **必需**。复位引脚（Reset Pin）。 |
| `micro-step-res` | `int` | 初始化设备驱动时设置的微步分辨率（Microstep Resolution）。；默认值：`1`；合法值：`1, 2, 4, 8, 16, 32, 64, 128, 256` |
| `en-gpios` | `phandle-array` | 控制电机驱动器使能信号（Enable Signal）的GPIO引脚。 |
| `m0-gpios` | `phandle-array` | 微步配置引脚（Microstep Configuration Pin）0。 |
| `m1-gpios` | `phandle-array` | 微步配置引脚（Microstep Configuration Pin）1。 |

本页没有已弃用的节点专用属性。

---

[上一章](P011_adi_tmcm3216.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P013_ti_drv84xx.md)
