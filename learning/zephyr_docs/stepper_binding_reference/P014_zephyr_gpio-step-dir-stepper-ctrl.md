---
id: learning.zephyr-docs.stepper-binding-reference.page-14
title: zephyr_gpio-step-dir-stepper-ctrl
kind: reference
status: maintained
domains: [zephyr, devicetree, stepper]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/stepper/zephyr,gpio-step-dir-stepper-ctrl.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第14章\_zephyr_gpio-step-dir-stepper-ctrl

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/stepper/zephyr,gpio-step-dir-stepper-ctrl.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="zephyr-gpio-step-dir-stepper-ctrl"></a>
<a id="dtbinding-zephyr-gpio-step-dir-stepper-ctrl"></a>
<a id="std-dtcompatible-zephyr-gpio-step-dir-stepper-ctrl"></a>

兼容字符串（Compatible String）：`zephyr,gpio-step-dir-stepper-ctrl`。厂商：[ Zephyr ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-zephyr)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=zephyr,gpio-step-dir-stepper-ctrl)。

驱动源码（Driver Source）：[drivers/stepper/gpio_stepper/gpio_step_dir_stepper_ctrl.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/stepper/gpio_stepper/gpio_step_dir_stepper_ctrl.c)。

<a id="description"></a>

基于CPU的步进运动控制器（Stepper Motion Controller），通过GPIO控制步进电机，为步进驱动器生成步进信号和方向信号。

<a id="examples"></a>

官方设备树示例（Devicetree Example）：

```dts
step_dir_motion_control: motion-controller {
    compatible = "zephyr,gpio-step-dir-stepper-ctrl";
    step-gpios = <&gpio0 10 GPIO_ACTIVE_HIGH>;
    dir-gpios = <&gpio0 11 GPIO_ACTIVE_HIGH>;
    invert-direction;
    counter = <&counter1>;
    stepper-driver = <&tmc2209>; /* Optional stepper hardware driver reference */
};
```

原例说明：原例注释说明`stepper-driver`是可选的硬件驱动器引用。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 14.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `invert-direction` | `boolean` | 反转电机方向（Direction）。 |
| `step-gpios` | `phandle-array` | 向步进电机发送步进信号的GPIO引脚。 |
| `dir-gpios` | `phandle-array` | 向步进电机发送方向信号的GPIO引脚。正向时输出高电平，反向时输出低电平。 |
| `counter` | `phandle` | 用于生成精确步进脉冲的计数器（Counter），应引用设备树中的计数器节点。存在此属性时，运动控制器采用计数器作为定时源，替代默认的工作队列（Work Queue）定时，以提高步进时序精度。计数器必须同时支持`set_top_value`的两项功能：设置新的顶值（Top Value），以及为计数回绕（Turnaround）绑定中断服务程序（Interrupt Service Routine，ISR）。 |
| `stepper-driver` | `phandle` | 对步进驱动器设备的引用。提供后，将使用步进驱动器节点中的`step-width-ns`和`dual-edge-step`属性配置驱动。 |

本页没有已弃用的节点专用属性。

---

[上一章](P013_ti_drv84xx.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P015_zephyr_h-bridge-stepper-ctrl.md)
