---
id: learning.zephyr-docs.basic_samples.page-69
title: LVGL演示合集
kind: reference
status: maintained
domains: [zephyr, basic_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/modules/lvgl/demos/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="lvgl-demos"></a>

# 第69章\_LVGL演示合集

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/modules/lvgl/demos/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 69.1 概述（Overview）

本示例展示上游LVGL演示。

- **音乐（Music）**：音乐播放器展示LVGL可以创建怎样的现代智能手机风格用户界面。
- **基准测试（Benchmark）**：测试各种场景的性能，包括矩形、边框、阴影、文本、图像混合、图像变换、混合模式等。
- **压力测试（Stress）**：包含大量对象创建、删除、动画与样式操作，可用于排查高负载使用时的内存破坏或内存泄漏。
- **控件（Widgets）**：使用内置Material主题，展示控件开箱即用的外观。
- **键盘与编码器（Keypad and Encoder）**：展示如何通过键盘与硬件编码器控制控件。
- **渲染（Render）**：包含多种渲染测试。

<a id="id2"></a>

更多细节见[LVGL演示说明（LVGL demos Readme）](https://github.com/zephyrproject-rtos/lvgl/blob/zephyr/demos/README.md)[1](#id1)。

<a id="requirements"></a>

## 69.2 要求（Requirements）

- 带显示器的开发板，分辨率最好为480×272或更高。
- 指针输入设备（Pointer input device）：触摸板、鼠标或带触摸屏的显示器，与[`zephyr,lvgl-pointer-input`](../input_touch_lvgl_gesture_binding_reference/P020_zephyr_lvgl-pointer-input.md#std-dtcompatible-zephyr-lvgl-pointer-input)兼容。

原文说明，这些演示没有展示其他输入设备类型，即键盘、小键盘（[`zephyr,lvgl-keypad-input`](../input_touch_lvgl_gesture_binding_reference/P019_zephyr_lvgl-keypad-input.md#std-dtcompatible-zephyr-lvgl-keypad-input)）和硬件按键（[`zephyr,lvgl-button-input`](../input_touch_lvgl_gesture_binding_reference/P017_zephyr_lvgl-button-input.md#std-dtcompatible-zephyr-lvgl-button-input)）。下面另行说明`native_sim`中的编码器演示方式。

<a id="keypad-and-encoder-demo-on-native-sim"></a>

## 69.3 native\_sim上的键盘与编码器演示（Keypad and Encoder demo on native\_sim）

在[原生模拟器（Native simulator，native_sim）](../native_reference/P004_Native_Simulator本机模拟器.md#native_sim)上，键盘与编码器演示由SDL鼠标模拟的旋转编码器（Rotary encoder，[`zephyr,lvgl-encoder-input`](../input_touch_lvgl_gesture_binding_reference/P018_zephyr_lvgl-encoder-input.md#std-dtcompatible-zephyr-lvgl-encoder-input)）驱动：鼠标滚轮用于旋转编码器，按下中键／滚轮相当于ENTER，不需要额外硬件。

该演示旨在通过编码器导航，因此禁用了通常从`zephyr,touch` chosen设备派生的LVGL指针，避免指针点击绕过编码器导航。其他演示仍保留指针。

<a id="building-and-running"></a>

## 69.4 构建与运行（Building and Running）

以下命令面向模拟显示环境。为真实开发板构建时，将`native_sim`替换为开发板名称。

音乐演示：

```sh
west build -b native_sim samples/modules/lvgl/demos -- -DCONFIG_LV_Z_DEMO_MUSIC=y
west build -t run
```

基准测试演示：

```sh
west build -b native_sim samples/modules/lvgl/demos -- -DCONFIG_LV_Z_DEMO_BENCHMARK=y
west build -t run
```

压力测试演示：

```sh
west build -b native_sim samples/modules/lvgl/demos -- -DCONFIG_LV_Z_DEMO_STRESS=y
west build -t run
```

控件演示：

```sh
west build -b native_sim samples/modules/lvgl/demos -- -DCONFIG_LV_Z_DEMO_WIDGETS=y
west build -t run
```

键盘与编码器演示：

```sh
west build -b native_sim samples/modules/lvgl/demos -- -DCONFIG_LV_Z_DEMO_KEYPAD_AND_ENCODER=y
west build -t run
```

渲染演示：

```sh
west build -b native_sim samples/modules/lvgl/demos -- -DCONFIG_LV_Z_DEMO_RENDER=y
west build -t run
```

如果构建主机为64位，也可以将上述目标板参数替换为`native_sim/native/64`。

> 译注——选择与执行：以上是不同演示的独立配置。切换演示时应使用新的相对构建目录，或按构建工具要求进行干净构建，避免旧的Kconfig选择残留。`west build -t run`用于运行支持此目标的模拟环境；为真实开发板替换名称后，仍须依据相应开发板文档选择烧录与运行方式，不能将模拟器运行目标等同于硬件烧录。

<a id="references"></a>

## 69.5 参考资料（References）

<a id="id1"></a>

[1] [LVGL演示说明（LVGL demos Readme）](https://github.com/zephyrproject-rtos/lvgl/blob/zephyr/demos/README.md)，[返回引用位置](#id2)。

<a id="see-also"></a>

## 69.6 另请参阅（See also）

[显示接口（Display）](../hardware/P214_显示公共接口.md)。


> 译注——实现依据：[samples/modules/lvgl/demos/Kconfig](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/modules/lvgl/demos/Kconfig)、[samples/modules/lvgl/demos/CMakeLists.txt](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/modules/lvgl/demos/CMakeLists.txt)、[samples/modules/lvgl/demos/boards/native_sim.overlay](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/modules/lvgl/demos/boards/native_sim.overlay)。这些链接对应本次核对的官方main来源，内容会随分支变化，所保存快照的摘要见[来源记录](../SOURCES.md)。下方本仓库源码仅用于版本对照。

对应官方文档源码：[samples/modules/lvgl/demos/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/modules/lvgl/demos/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/modules/lvgl/demos/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/modules/lvgl/demos/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P068_LVGL加速度曲线示例.md) · [返回大纲](大纲.md) · [下一章](P070_LVGL多显示器示例.md)
