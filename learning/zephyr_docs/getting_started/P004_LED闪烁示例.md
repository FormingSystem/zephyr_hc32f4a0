---
id: learning.zephyr-official-intro.blinky
title: LED 闪烁示例
kind: engineering
status: maintained
domains: [zephyr, documentation]
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 本文件为中文翻译；章节编号、导航和明确标出的译注为本地新增。 -->

<a id="blinky"></a>

# 第4章\_LED闪烁示例

原文：[Blinky](https://docs.zephyrproject.org/latest/samples/basic/blinky/README.html)。[浏览示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/basic/blinky)。译文基线：2026-10-12 的 `latest` 页面。

## 4.1\_概述

Blinky 示例通过 **通用输入输出（General-Purpose Input/Output，GPIO）** 接口，让 **发光二极管（Light-Emitting Diode，LED）** 持续闪烁。源码展示了如何：

1. 从设备树取得引脚描述，并以 `gpio_dt_spec` 结构表示。
2. 将 GPIO 引脚配置为输出。
3. 持续翻转引脚状态。

[PWM Blinky](https://docs.zephyrproject.org/latest/samples/basic/blinky_pwm/README.html) 是类似的示例，使用**脉宽调制（Pulse Width Modulation，PWM）**接口。

## 4.2\_要求

开发板必须：

1. 具有连接到 GPIO 引脚的 LED。许多受支持开发板把它称作“用户 LED”。
2. 通过设备树别名 `led0` 配置该 LED。

## 4.3\_构建与运行

按[入门指南](P002_入门指南.md)准备环境后，在 Zephyr 源码根目录构建、烧录。将 `reel_board` 替换为实际开发板目标：

```text
west build -b reel_board samples/basic/blinky
west flash
```

烧录后，LED 开始闪烁，控制台打印当前 LED 状态。如果发生运行时错误，示例退出且不向控制台打印消息。

> 译注：这里翻译的是原文对行为的描述，不是本次运行结果。构建失败时不要继续烧录；示例板配置须与实际目标硬件对应。

## 4.4\_构建错误

如果为不支持此示例的开发板构建，通常会在定义 `struct gpio_dt_spec led` 变量的源码行报错。

使用基于 GCC 的工具链时，错误类似：

```text
error: '__device_dts_ord_DT_N_ALIAS_led_P_gpios_IDX_0_PH_ORD' undeclared here (not in a function)
```

## 4.5\_添加开发板支持

要为开发板添加支持，可以在设备树中加入类似内容：

```dts
/ {
     aliases {
             led0 = &myled0;
     };

     leds {
             compatible = "gpio-leds";
             myled0: led_0 {
                     gpios = <&gpio0 13 GPIO_ACTIVE_LOW>;
             };
     };
};
```

这段代码把开发板的 `led0` 别名指向 GPIO 控制器 `gpio0` 的 13 号引脚。`GPIO_ACTIVE_LOW` 表示低电平有效：引脚为低电平时 LED 点亮，高电平时熄灭。

> 译注：这是官方示例片段，不是可直接复制的 HC32 接线。`gpio0`、13 号引脚和有效电平均需与目标板的设备树及实际电路一致；外接 LED 也必须按实际连接配置。

提示：

- GPIO LED 的设备树定义见 [`gpio-leds` 绑定](https://docs.zephyrproject.org/latest/build/dts/api/bindings/led/gpio-leds.html)。
- 不确定如何定义时，可对照采用相同 **片上系统（System on Chip，SoC）** 的受支持开发板。生成的设备树及头文件查看方式见[设备树操作指南](https://docs.zephyrproject.org/latest/build/dts/howtos.html#get-your-devicetree-and-generated-header)。
- 可用于设备树的引脚标志见 [include/zephyr/dt-bindings/gpio/gpio.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/dt-bindings/gpio/gpio.h)。
- 如果 LED 是开发板自带硬件，别名应定义在开发板的 `BOARD.dts` 中；否则可以通过[设备树覆盖文件](https://docs.zephyrproject.org/latest/build/dts/howtos.html#set-devicetree-overlays)定义。

## 4.6\_相关资料

更多 GPIO 接口说明见 [GPIO 官方文档](https://docs.zephyrproject.org/latest/hardware/peripherals/gpio.html)。

---

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：入门之后](P003_入门之后.md) · [本模块主线目录](../reading/getting_started.md) · [全部主线](../reading/README.md) · [下一篇：Hello World 示例](P005_HelloWorld示例.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：入门之后](P003_入门之后.md) · [返回大纲](大纲.md) · [下一章：Hello World示例](P005_HelloWorld示例.md)

</details>

<!-- reading-navigation:end -->
