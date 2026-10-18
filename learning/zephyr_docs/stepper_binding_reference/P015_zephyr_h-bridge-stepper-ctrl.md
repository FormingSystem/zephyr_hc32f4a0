---
id: learning.zephyr-docs.stepper-binding-reference.page-15
title: zephyr_h-bridge-stepper-ctrl
kind: reference
status: maintained
domains: [zephyr, devicetree, stepper]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/stepper/zephyr,h-bridge-stepper-ctrl.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第15章\_zephyr_h-bridge-stepper-ctrl

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/stepper/zephyr,h-bridge-stepper-ctrl.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="zephyr-h-bridge-stepper-ctrl"></a>
<a id="dtbinding-zephyr-h-bridge-stepper-ctrl"></a>
<a id="std-dtcompatible-zephyr-h-bridge-stepper-ctrl"></a>

兼容字符串（Compatible String）：`zephyr,h-bridge-stepper-ctrl`。厂商：[ Zephyr ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-zephyr)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=zephyr,h-bridge-stepper-ctrl)。

驱动源码（Driver Source）：[drivers/stepper/gpio_stepper/h_bridge_stepper_ctrl.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/stepper/gpio_stepper/h_bridge_stepper_ctrl.c)。

<a id="description"></a>

用于达林顿晶体管阵列（Darlington Transistor Array）或双H桥（Dual H-bridge）的GPIO步进控制器（Stepper Controller）。

<a id="examples"></a>

官方设备树示例（Devicetree Example）：

```dts
/* Lead A is connected Lead C and Lead B is connected to Lead D*/
h_bridge_stepper: motion-controller {
    compatible = "zephyr,h-bridge-stepper-ctrl";
    gpios = <&gpioa 9 GPIO_ACTIVE_HIGH>,  /* Lead A1/A */
            <&gpioc 7 GPIO_ACTIVE_HIGH>,  /* Lead B1/B */
            <&gpiob 0 GPIO_ACTIVE_HIGH>,  /* Lead A2/C */
            <&gpioa 7 GPIO_ACTIVE_HIGH>;  /* Lead B2/D */
};
```

原例说明：原例首行注释写明A与C相连、B与D相连；四个引脚注释依次为A1／A、B1／B、A2／C、B2／D，均按原文保留。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 15.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `invert-direction` | `boolean` | 反转电机方向（Direction）。 |
| `gpios` | `phandle-array` | **必需**。连接步进电机输入的GPIO引脚数组（GPIO Pin Array）。 |
| `lut-step-gap` | `int` | 步进模式（Step Mode）选择：1为半步模式（Half-step），2为整步模式（Full-step）。；默认值：`1`；合法值：`1, 2` |
| `counter` | `phandle` | 用于生成精确步进脉冲的计数器（Counter），应引用设备树中的计数器节点。存在此属性时，运动控制器采用计数器作为定时源，替代默认的工作队列（Work Queue）定时，以提高步进时序精度。计数器必须同时支持`set_top_value`的两项功能：设置新的顶值（Top Value），以及为计数回绕（Turnaround）绑定中断服务程序（Interrupt Service Routine，ISR）。 |

本页没有已弃用的节点专用属性。

---

[上一章](P014_zephyr_gpio-step-dir-stepper-ctrl.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md)
