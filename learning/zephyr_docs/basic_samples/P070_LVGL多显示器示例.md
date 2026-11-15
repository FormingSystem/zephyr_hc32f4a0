---
id: learning.zephyr-docs.basic_samples.page-70
title: LVGL多显示器示例
kind: reference
status: maintained
domains: [zephyr, basic_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/modules/lvgl/multi_display/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="lvgl-multi-display"></a>

# 第70章\_LVGL多显示器示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/modules/lvgl/multi_display/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 70.1 概述（Overview）

本示例展示Zephyr中的LVGL多显示器（Multi-display）支持。

默认在第一块显示器上运行音乐（Music）演示，在其他显示器上运行控件（Widgets）演示。显示器顺序由设备树中兼容标识（Compatible）为`zephyr,displays`的节点的`displays`属性定义。原文将用于修改演示选择的Kconfig符号写为`CONFIG_LV_Z_DEMO_FIRST_DISP##`与`CONFIG_LV_Z_DEMO_OTHER_DISPS##`。

- **音乐（Music）**：音乐播放器展示LVGL可以创建怎样的现代智能手机风格用户界面。
- **基准测试（Benchmark）**：测试各种场景的性能，包括矩形、边框、阴影、文本、图像混合、图像变换、混合模式等。
- **压力测试（Stress）**：包含大量对象创建、删除、动画与样式操作，可用于排查高负载使用时的内存破坏或内存泄漏。
- **控件（Widgets）**：使用内置Material主题，展示控件开箱即用的外观。

<a id="id2"></a>

更多演示细节见[LVGL演示说明（LVGL demos Readme）](https://github.com/zephyrproject-rtos/lvgl/blob/zephyr/demos/README.md)[1](#id1)。

> 译注——当前配置名称：原文包含`##`的名称不是可直接赋值的实际Kconfig符号。当前选择项为`LV_Z_DEMO_FIRST_DISP`与`LV_Z_DEMO_OTHER_DISPS`；实际选项按演示名称排列，例如`CONFIG_LV_Z_DEMO_MUSIC_FIRST_DISP=y`与`CONFIG_LV_Z_DEMO_WIDGETS_OTHER_DISPS=y`。其他选项将`MUSIC`或`WIDGETS`替换为`BENCHMARK`、`STRESS`等受支持名称，并保留相应显示器后缀。当前默认仍是第一块显示音乐，其他显示控件；实现按设备树显示器顺序逐个设置LVGL默认显示器后创建相应演示。

<a id="requirements"></a>

## 70.2 要求（Requirements）

一块连接至少两个显示器的开发板，显示分辨率最好为480×272或更高。

<a id="building-and-running"></a>

## 70.3 构建与运行（Building and Running）

可以在Linux下为模拟显示环境构建并运行此示例：

```sh
west build -b native_sim/native/64 samples/modules/lvgl/multi_display
west build -t run
```

<a id="references"></a>

## 70.4 参考资料（References）

<a id="id1"></a>

[1] [LVGL演示说明（LVGL demos Readme）](https://github.com/zephyrproject-rtos/lvgl/blob/zephyr/demos/README.md)，[返回引用位置](#id2)。

<a id="see-also"></a>

## 70.5 另请参阅（See also）

[显示接口（Display）](../hardware/P214_显示公共接口.md)。


> 译注——实现依据：[samples/modules/lvgl/multi_display/Kconfig](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/modules/lvgl/multi_display/Kconfig)、[samples/modules/lvgl/multi_display/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/modules/lvgl/multi_display/src/main.c)。这些链接对应本次核对的官方main来源，内容会随分支变化，所保存快照的摘要见[来源记录](../SOURCES.md)。下方本仓库源码仅用于版本对照。

对应官方文档源码：[samples/modules/lvgl/multi_display/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/modules/lvgl/multi_display/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/modules/lvgl/multi_display/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/modules/lvgl/multi_display/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P069_LVGL演示合集.md) · [返回大纲](大纲.md) · [下一章](P071_LVGL屏幕透明度示例.md)
