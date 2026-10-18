---
id: learning.zephyr-docs.shield-samples.page-8
title: X_NUCLEO_53L0A1测距扩展板
kind: reference
status: maintained
domains: [zephyr, shields, samples]
source_url: https://docs.zephyrproject.org/latest/samples/shields/x_nucleo_53l0a1/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="x-nucleo-53l0a1"></a>

# 第8章\_X-NUCLEO-53L0A1 扩展板（Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/shields/x_nucleo_53l0a1/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/shields/x_nucleo_53l0a1/README.rst/..)

<a id="overview"></a>

## 8.1 概述（Overview）

本示例演示 [X-NUCLEO-53L0A1 测距和手势检测传感器扩展板](https://docs.zephyrproject.org/latest/boards/shields/x_nucleo_53l0a1/doc/index.html#x-nucleo-53l0a1-shield)上的四位七段显示器，以及三个 VL53L0X 测距传感器的用法。

烧录后有两种模式，可按 `sw0` 按钮切换。

<a id="distance-onboard-sensor"></a>

### 8.1.1 距离模式：板载传感器（Distance）

这是启动时的默认模式。中心传感器焊接在扩展板上；距离小于 1.25 米时，四位七段显示器以厘米显示测距值。

> 译注——距离显示：源码把米转换为厘米后传给显示函数；距离大于或等于 1.25 米时关闭显示。读取传感器失败时显示 Err。因此显示为空与读取错误是不同情况，不能都解释为没有发现传感器。

<a id="proximity-onboard-satellites"></a>

### 8.1.2 接近模式：板载传感器加卫星传感器（Proximity）

此模式下，每个传感器检测到附近有物体时，四位七段显示器用三条堆叠水平线表示。最左一位显示左侧传感器，随后是中心传感器、右侧传感器。接近阈值由 [`CONFIG_VL53L0X_PROXIMITY_THRESHOLD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VL53L0X_PROXIMITY_THRESHOLD) 配置。

按 `sw0` 按钮切换模式。

<a id="requirements"></a>

## 8.2 硬件与配置要求（Requirements）

本示例通过 I2C 与叠接在 Arduino 接口开发板上的 X-NUCLEO-53L0A1 通信。开发板的 I2C 必须配置到 Arduino 接口，包括引脚复用（Pin muxing）与设备树配置；设备树还须为板上按钮提供 `sw0` 别名。

> 译注——按钮与构建：CMakeLists.txt 已设置 SHIELD=x_nucleo_53l0a1。main.c 使用 sw0 的 GPIO 上升沿中断切换模式，并要求两次切换间隔超过 300 ms；上升沿具体对应按下还是释放取决于板卡接线。飞行时间（Time of Flight，ToF）测距与接近（Proximity）阈值判定在示例中是不同模式。

<a id="references"></a>

## 8.3 参考资料（References）

- [X-NUCLEO-53L0A1 网站](https://www.st.com/en/evaluation-tools/x-nucleo-53l0a1.html)

<a id="building-and-running"></a>

## 8.4 构建与运行（Building and Running）

> 译注——执行前提：主机命令在读者自己的 Zephyr 源码根目录，使用 UCRT64 Bash 或 Linux Bash 执行；先按[入门指南](../getting_started/大纲.md)准备模块和工具链，再核对本页指定主开发板、扩展板、接线与配置。设备 Shell 命令在目标板串口执行。遇到构建或设备就绪错误，先回查所选 board／shield 与接线；下方日志是官方预期示例。本次仅核对文档与源码，未构建、烧录、擦写存储或进行实板测量。

本示例可在具有匹配 Arduino 接口并叠接 X-NUCLEO-53L0A1 的开发板上运行。这里采用 [Nucleo F429ZI](https://docs.zephyrproject.org/latest/boards/st/nucleo_f429zi/doc/index.html#nucleo_f429zi)。

```text
west build -b nucleo_f429zi samples/shields/x_nucleo_53l0a1
```

<a id="see-also"></a>

## 8.5 另请参阅（See also）

[传感器（Sensor）](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html)

[通用输入输出（GPIO）](../hardware/P266_GPIO公共接口.md)

> 译注——源码入口：[src/main.c](../../../samples/shields/x_nucleo_53l0a1/src/main.c)；[CMakeLists.txt](../../../samples/shields/x_nucleo_53l0a1/CMakeLists.txt)；[prj.conf](../../../samples/shields/x_nucleo_53l0a1/prj.conf)；[src/display_7seg.c](../../../samples/shields/x_nucleo_53l0a1/src/display_7seg.c)。本地源码使用相对链接；上游快照摘要见来源记录，本地版本可能不同。

对应官方文档源码：[samples/shields/x_nucleo_53l0a1/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/shields/x_nucleo_53l0a1/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/shields/x_nucleo_53l0a1/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录、擦写存储或连接设备。

[上一章](P007_Renesas电容触摸扩展板.md) · [返回大纲](大纲.md) · [下一章](P009_X_NUCLEO_IKS01A1传感器示例.md)
