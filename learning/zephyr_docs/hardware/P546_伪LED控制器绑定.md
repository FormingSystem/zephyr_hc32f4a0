---
id: learning.zephyr-docs.hardware.fakedevsbind-4
title: 伪LED控制器绑定
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/led/zephyr,fake-leds.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第546章\_伪LED控制器绑定

<a id="dtbinding-zephyr-fake-leds"></a>

原文：[zephyr,fake-leds](https://docs.zephyrproject.org/latest/build/dts/api/bindings/led/zephyr,fake-leds.html)。读取日期：2026-10-13，`latest`。

`zephyr,fake-leds` 提供伪**发光二极管（Light-Emitting Diode，LED）**控制器，用作 Zephyr 测试中的**测试桩（Stub）**或**模拟对象（Mock）**。驱动为 [`drivers/led/led_fake.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led/led_fake.c)，相关开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=zephyr,fake-leds)。

## 546.1\_子节点示例

原页没有顶层属性。下面的官方示例创建普通、红色、绿色、蓝色以及**红绿蓝（Red, Green, Blue，RGB）**多色 LED 子节点。`LED_COLOR_ID_RED`、`LED_COLOR_ID_GREEN` 和 `LED_COLOR_ID_BLUE` 是对应颜色的标识常量。

```dts
fake_leds: fake-leds {
  compatible = "zephyr,fake-leds";

  fake_led: fake-led {
    label = "Fake LED";
  };

  fake_red_led: fake-red-led {
    label = "Fake Red LED";
    color-mapping = <LED_COLOR_ID_RED>;
  };

  fake_green_led: fake-green-led {
    label = "Fake Green LED";
    color-mapping = <LED_COLOR_ID_GREEN>;
  };

  fake_blue_led: fake-blue-led {
    label = "Fake Blue LED";
    color-mapping = <LED_COLOR_ID_BLUE>;
  };

  fake_rgb_led: fake-rgb-led {
    label = "Fake RGB LED";
    color-mapping = <LED_COLOR_ID_RED>,
                    <LED_COLOR_ID_GREEN>,
                    <LED_COLOR_ID_BLUE>;
  };
};
```

## 546.2\_索引、标签与颜色映射

以下属性均属于 LED 子节点，`int` 为整数，`string` 为字符串，`array` 为数值数组。

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `index` | `int` | LED 在控制器上的索引；驱动或应用可把逻辑 LED 映射到控制器上的实际位置，适用于灯阵列或灯带接线顺序与控制器 LED 顺序不一致的开发板 |
| `label` | `string` | 人可读的 LED 描述；应用可用它识别 LED，或取得它在父设备中的编号/索引，即子节点编号 |
| `color-mapping` | `array` | 多色 LED 的通道到颜色映射；LED 支持多种颜色时，用它描述硬件通道与颜色的对应关系 |

原文的 RGB 颜色映射片段如下：

```dts
   color-mapping =
        <LED_COLOR_ID_RED>,
        <LED_COLOR_ID_GREEN>,
        <LED_COLOR_ID_BLUE>;
```



---

[上一章：伪PWM控制器绑定](P545_伪PWM控制器绑定.md) · [下一章：伪步进电机控制器绑定](P547_伪步进电机控制器绑定.md) · [返回大纲](大纲.md)
