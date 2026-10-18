---
id: learning.zephyr-docs.stepper-binding-reference.page-13
title: ti_drv84xx
kind: reference
status: maintained
domains: [zephyr, devicetree, stepper]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/stepper/ti/ti,drv84xx.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第13章\_ti_drv84xx

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/stepper/ti/ti,drv84xx.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="ti-drv84xx"></a>
<a id="dtbinding-ti-drv84xx"></a>
<a id="std-dtcompatible-ti-drv84xx"></a>

兼容字符串（Compatible String）：`ti,drv84xx`。厂商：[ Texas Instruments ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-ti)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=ti,drv84xx)。

驱动源码（Driver Source）：[drivers/stepper/ti/drv84xx.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/stepper/ti/drv84xx.c)。

<a id="description"></a>

TI DRV84XX步进电机驱动器（Stepper Motor Driver），兼容drv8424、drv8425、drv8426、drv8434及drv8436。

<a id="examples"></a>

官方设备树示例（Devicetree Example）：

```dts
drv8424: drv8424 {
  status = "okay";
  compatible = "ti,drv84xx";

  fault-gpios = <&arduino_header 16 0>;
  sleep-gpios = <&arduino_header 15 GPIO_ACTIVE_LOW>;
  en-gpios  = <&arduino_header 14 0>;
  m0-gpios = <&mikroe_stepper_gpios 0 0>;
  m1-gpios = <&mikroe_stepper_gpios 1 0>;
};
```

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 13.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `step-width-ns` | `int` | 步进信号（Step Signal）的最小脉冲宽度，单位为纳秒（ns）。；默认值：`970` |
| `fault-gpios` | `phandle-array` | 故障引脚（Fault Pin）。 |
| `sleep-gpios` | `phandle-array` | 休眠引脚（Sleep Pin），低电平有效。 |
| `micro-step-res` | `int` | 初始化设备驱动时设置的微步分辨率（Microstep Resolution）。；默认值：`1`；合法值：`1, 2, 4, 8, 16, 32, 64, 128, 256` |
| `en-gpios` | `phandle-array` | 控制电机驱动器使能信号（Enable Signal）的GPIO引脚。 |
| `m0-gpios` | `phandle-array` | 微步配置引脚（Microstep Configuration Pin）0。 |
| `m1-gpios` | `phandle-array` | 微步配置引脚（Microstep Configuration Pin）1。 |

本页没有已弃用的节点专用属性。

---

[上一章](P012_allegro_a4979.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P014_zephyr_gpio-step-dir-stepper-ctrl.md)
