---
id: learning.zephyr-docs.hardware.boardbasebind-1
title: GPIO指示灯绑定
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/led/gpio-leds.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第564章\_GPIO指示灯绑定

<a id="dtbinding-gpio-leds"></a>

原文：[gpio-leds](https://docs.zephyrproject.org/latest/build/dts/api/bindings/led/gpio-leds.html)。读取日期：2026-10-13，`latest`。

`gpio-leds` 是通用、与厂商无关的 GPIO 控制**发光二极管（Light-Emitting Diode，LED）**组绑定。**通用输入输出（General-Purpose Input/Output，GPIO）**控制各个 LED；每个 LED 由 `gpio-leds` 节点的一个子节点描述。驱动为 [`drivers/led/led_gpio.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led/led_gpio.c)，相关开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=gpio-leds)。

## 564.1\_电平极性与上拉示例

`led_0` 连接 `gpio0` 的引脚 1，标志 `GPIO_ACTIVE_LOW` 表示低电平点亮、高电平熄灭。`led_1` 连接 `gpio0` 的引脚 2，标志 `GPIO_ACTIVE_HIGH` 表示高电平点亮、低电平熄灭。`led_2` 连接 `gpio1` 的引脚 15，低电平点亮，同时通过 `GPIO_PULL_UP` 启用引脚内部的上拉电阻（Pull-Up Resistor）。

官方示例定义这三个 LED，原始代码和注释如下：

```dts
/ {
  leds {
    compatible = "gpio-leds";
    /*
     * led_0 is pin 1 on gpio0.
     * The LED is on when the pin is low, and off when the pin is high.
     */
    led_0 {
      gpios = <&gpio0 1 GPIO_ACTIVE_LOW>;
    };
    /*
     * led_1 is pin 2 on gpio0.
     * The LED is on when the pin is high, and off when it is low.
     */
    led_1 {
      gpios = <&gpio0 2 GPIO_ACTIVE_HIGH>;
    };
    /*
     * led_2 is pin 15 on gpio1.
     * The LED is on when the pin is low, and the pin's internal pull-up resistor should be
     * enabled.
     */
    led_2 {
      gpios = <&gpio1 15 (GPIO_PULL_UP | GPIO_ACTIVE_LOW)>;
    };
  };
};
```

## 564.2\_LED子节点属性

原页没有顶层属性。以下两个属性属于每个 LED 子节点，`phandle-array` 为设备树节点引用及其说明单元数组，`string` 为字符串。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `gpios` | `phandle-array` | 控制 LED 的 GPIO，必需；原页未附额外描述 |
| `label` | `string` | 人可读的 LED 描述；应用可据此识别 LED，或取得它在父设备中的编号/索引，即子节点编号 |



---

[上一章：GPIO按键绑定](P563_GPIO按键绑定.md) · [下一章：PWM指示灯绑定](P565_PWM指示灯绑定.md) · [返回大纲](大纲.md)
