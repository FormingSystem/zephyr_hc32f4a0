---
id: learning.zephyr-docs.board-samples.page-5
title: STM32的PWM主模式
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/st/pwm/mastermode/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="stm32_pwm_mastermode"></a>

# 第5章\_STM32 PWM 主模式（STM32 pwm mastermode）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/st/pwm/mastermode/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/st/pwm/mastermode/README.rst/..)

<a id="overview"></a>

## 5.1 概述（Overview）

本例展示 STM32 设备的设备树配置：由定时器模块在互连矩阵上产生事件，即主模式选择／触发输出 TRGO；再使用这些触发进行定时器同步，即从模式／触发输入。[PWM API](../hardware/P015_PWM脉宽调制.md#pwm-api) 用于配置脉宽调制（Pulse-Width Modulation，PWM）信号。

<a id="requirements"></a>

## 5.2 前提条件（Requirements）

本示例要求具有两个主／从模式相互兼容的定时器模块。

> 译注——触发连接并非任意配对：官方 nucleo_g071rb 覆盖文件把 TIM1 更新事件配置为 TRGO，TIM3 以 ITR0 接收并采用 reset 从模式；该映射按具体系列手册确定。主定时器可只作为内部触发源，不要求同时输出外部 PWM 引脚。源码先设从端周期 400 微秒、脉宽 100 微秒，再交替把主端周期设为 300／200 微秒；实际同步效果需在所选从端输出引脚观察。

<a id="building-and-running"></a>

## 5.3 构建与运行（Building and Running）

> 译注——执行环境与文件：以下构建命令从读者自己的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行。先按[入门指南](../getting_started/大纲.md)准备工具链、west 工作区和相应板定义；`samples/...` 是官方原有应用目录。原命令给出的板名仅对应示例，未显式给出 `-b` 时应指定实际受支持的板，不能依赖未知缓存。设备树和 Kconfig 片段写入相应配置文件，不作为终端命令执行；构建输出由工具生成。构建成功后按板文档烧录，并按正文核对串口或硬件现象，失败时回查配置、设备就绪和连接条件。本次仅翻译与核对来源，未执行构建、烧录或硬件实验。

> ```text
> west build -b nucleo_g070rb samples/boards/st/pwm/mastermode
> ```

<a id="see-also"></a>

## 5.4 另请参阅（See also）

[PWM](../hardware/P255_PWM公共接口.md)

> 译注——源码入口：[samples/boards/st/pwm/mastermode/src/main.c](../../../samples/boards/st/pwm/mastermode/src/main.c)；[samples/boards/st/pwm/mastermode/prj.conf](../../../samples/boards/st/pwm/mastermode/prj.conf)。链接相对于所在译文，可随仓库移动；本地源码版本可能与官网快照不同。

对应官方文档源码：[samples/boards/st/pwm/mastermode/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/st/pwm/mastermode/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/st/pwm/mastermode/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P004_STM32主时钟输出.md) · [返回大纲](大纲.md) · [下一章](P006_STM32的UART循环DMA.md)
