---
id: learning.zephyr-docs.shield-samples.page-9
title: X_NUCLEO_IKS01A1传感器示例
kind: reference
status: maintained
domains: [zephyr, shields, samples]
source_url: https://docs.zephyrproject.org/latest/samples/shields/x_nucleo_iks01a1/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="x-nucleo-iks01a1"></a>

# 第9章\_X-NUCLEO-IKS01A1 扩展板（Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/shields/x_nucleo_iks01a1/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/shields/x_nucleo_iks01a1/README.rst/..)

<a id="overview"></a>

## 9.1 概述（Overview）

本示例启用 X-NUCLEO-IKS01A1 扩展板上的全部传感器，然后周期性读取并显示以下传感器数据：

- HTS221：温度与湿度（Temperature and Humidity）

- LPS25HB：大气压力（Atmospheric Pressure）

- LIS3MDL：三轴磁场强度（3-axis Magnetic Field Intensity）

- LSM6DSL：三轴加速度（3-Axis Acceleration）

> 译注——器件名差异：本行保留官方正文的 LSM6DSL，但本次 main.c 实际使用 DEVICE_DT_GET_ONE(st_lsm6ds0)，扩展板 overlay 也声明 st,lsm6ds0；输出日志相应为 LSM6DS0。不能仅按本行型号选择驱动或替换器件。

<a id="requirements"></a>

## 9.2 硬件与配置要求（Requirements）

本示例通过 I2C 与叠接在 Arduino 接口开发板上的 X-NUCLEO-IKS01A1 通信。开发板必须为 Arduino 接口配置 I2C，包括引脚复用（Pin Muxing）与设备树（Devicetree）。原文指出，不能在已支持扩展板上某种传感器的开发板上运行本示例，例如 disco_l475_iot1，因为 Zephyr 尚不支持同类传感器的多个实例。

> 译注——多实例说明的版本边界：不能把原文表述泛化为当前 Zephyr 传感器框架的统一限制。当前 DEVICE_DT_GET_ONE() 在多个匹配节点中返回任意一个设备，示例没有明确区分板载与扩展板实例；例如当前 LSM6DSO 驱动已按每个启用节点生成设备。移植时仍需核对驱动能力、总线地址与选定节点，避免程序读到另一颗同型号传感器。

<a id="references"></a>

## 9.3 参考资料（References）

X-NUCLEO-IKS01A1：https://www.st.com/en/ecosystems/x-nucleo-iks01a1.html 相关链接：[X-NUCLEO-IKS01A1 官方产品页](https://www.st.com/en/ecosystems/x-nucleo-iks01a1.html)。

> 译注——产品页链接：上述官方原文旧地址在本次网页复核中返回 404；另提供已确认可访问的 [ST IKS01A1 产品页](https://www.st.com/en/evaluation-tools/x-nucleo-iks01a1.html)。原链接保留用于追溯。

<a id="building-and-running"></a>

## 9.4 构建与运行（Building and Running）

> 译注——执行前提：主机命令从读者自己的 Zephyr 源码根目录，用 UCRT64 Bash 或 Linux Bash 执行；先按[入门指南](../getting_started/大纲.md)准备模块、工具链和目标板。CMakeLists.txt 已选择 SHIELD=x_nucleo_iks01a1，所以原命令不必重复指定 --shield。先按本页链接核对扩展板硬件模式、供电和连接，再构建对应应用；设备不就绪时回查模式、总线、设备树与中断接线。下方是原文预期输出，本次未构建、烧录或实测。

本示例可在具有匹配 Arduino 接口并叠接 X-NUCLEO-IKS01A1 的开发板上运行。这里采用 [Nucleo F429ZI](https://docs.zephyrproject.org/latest/boards/st/nucleo_f429zi/doc/index.html#nucleo_f429zi) 开发板。

```text
west build -b nucleo_f429zi samples/shields/x_nucleo_iks01a1
```

<a id="sample-output"></a>

### 9.4.1 示例输出（Sample Output）

> 译注——读数单位：m/s^2 表示加速度，G 表示磁场高斯（Gauss），不是重力加速度单位 g；温度用摄氏度、压力用 kPa。源码在一轮显示后休眠 2000 ms；传感器内部采样、触发更新和控制台刷新是不同节奏，日志数值不表示本次已完成标定或精度验收。

> ```text
> X-NUCLEO-IKS01A1 sensor dashboard
>
> HTS221: Temperature:29.1 C
> HTS221: Relative Humidity:46.0%
> LPS25HB: Pressure:100.0 kPa
> LIS3MDL: Magnetic field (G): x: 0.1, y: -0.4, z: 0.4
> LSM6DS0: Acceleration (m/s^2): x: -0.0, y: -0.1, z: 9.7
>
>
> <updated endlessly every 2 seconds>
> ```

<a id="see-also"></a>

## 9.5 另请参阅（See also）

[传感器（Sensor）](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html)

> 译注——源码入口：[src/main.c](../../../samples/shields/x_nucleo_iks01a1/src/main.c)；[CMakeLists.txt](../../../samples/shields/x_nucleo_iks01a1/CMakeLists.txt)；[prj.conf](../../../samples/shields/x_nucleo_iks01a1/prj.conf)；[boards/shields/x_nucleo_iks01a1/x_nucleo_iks01a1.overlay](../../../boards/shields/x_nucleo_iks01a1/x_nucleo_iks01a1.overlay)；[include/zephyr/device.h](../../../include/zephyr/device.h)；[drivers/sensor/st/lsm6dso/lsm6dso.c](../../../drivers/sensor/st/lsm6dso/lsm6dso.c)。本地源码相对定位，上游快照摘要见来源记录；本地版本可能与原网页不同。

对应官方文档源码：[samples/shields/x_nucleo_iks01a1/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/shields/x_nucleo_iks01a1/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/shields/x_nucleo_iks01a1/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或进行传感器实测。

[上一章](P008_X_NUCLEO_53L0A1测距扩展板.md) · [返回大纲](大纲.md) · [下一章](P010_IKS01A2标准模式.md)
