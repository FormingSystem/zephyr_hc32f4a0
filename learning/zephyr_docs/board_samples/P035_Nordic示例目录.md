---
id: learning.zephyr-docs.board-samples.page-35
title: Nordic示例目录
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/nordic/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="nordic-semiconductor"></a>

# 第35章\_Nordic Semiconductor

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/nordic/index.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

这些示例展示如何在 Zephyr 中使用 Nordic Semiconductor 开发板。

> 译注——目录范围：以下十八项是官方示例入口，其中部分正文归入本翻译集的核间通信、电源管理或硬件专题。目录与正文分别登记，不将目录完成当成子页自动完成；这些 Nordic 板级示例都来自 Zephyr 官网，不是仓库自有芯片资料的扩展翻译。

- [电池电压测量（Battery Voltage Measurement）](P021_电池电压测量.md#nrf_battery)：测量设备电源电压。

- [CoreSight STM 基准测试（Coresight STM benchmark）](P023_CoreSight_STM基准测试.md#coresight_stm_sample)

- [带远程 Shell 的 CoreSight STM（Coresight STM with remote shell）](P024_CoreSight_STM远程Shell.md#coresight_stm_shell)

- [动态引脚控制（Dynamic Pin Control）](P025_动态引脚控制.md#nrf_dynamic_pinctrl)：在启动时动态改变引脚配置。

- [通过 RPMsg 传输 IEEE 802.15.4（IEEE 802.15.4 over RPMsg）](../intercore_reference/P190_IEEE802154的RPMsg示例.md#nrf_ieee802154_rpmsg)：使用 RPMsg 传输，将 nRF IEEE 802.15.4 无线电驱动提供给其他设备或 CPU。

- [LED 矩阵（LED matrix）](P028_Nordic_LED矩阵.md#nrf_led_matrix)：使用 nRF LED 矩阵显示驱动来驱动 LED 矩阵。

- [Mesh 多模型演示（Mesh Models）](P034_Mesh多模型演示.md#nrf_bluetooth_mesh_onoff_level_lighting_vnd_app)：建立具有多种模型（通用开关、通用等级等）的蓝牙 Mesh 节点。

- [Mesh 开关模型（Mesh OnOff Model）](P033_Mesh开关模型.md#nrf_bluetooth_mesh_onoff)：通过蓝牙 Mesh 开关模型控制 Mesh 网络上的 LED。

- [Nordic 蓝牙低功耗活动期间写入闪存（Nordic flash write during Bluetooth LE activity）](P026_蓝牙活动期间写入Nordic闪存.md#nordic-flash)：在 Bluetooth LE 无线电活动期间写入 Flash。

- [Nordic IronSide SE 固件更新（Nordic IronSide SE firmware update）](P027_Nordic_IronSide_SE固件更新.md#nrf_ironside_update)：更新 Nordic IronSide SE 固件。

- [nRF 时钟控制（nRF clock control）](../timer_reference/P116_nRF时钟控制示例.md#nrf_clock_control)：在运行时请求最低时钟要求。

- [nRF 系统事件（nRF System Events）](P029_nRF系统事件.md#nrf-sys-event)：使用 nRF System Events API 管理 Nordic SoC 的全局恒定延迟模式。

- [nRF5x 时钟偏差（nRF5x Clock Skew）](P022_nRF5x时钟偏差.md#nrf_clock_skew)：测量高频与低频时钟之间的偏差。

- [nrfx](P030_nrfx外设驱动示例.md#nrf_nrfx)：使用 nrfx 库与 nRF 外设交互。

- [nrfx 外设资源共享（nrfx peripheral resource sharing）](P031_nrfx外设资源共享.md#nrf_nrfx_prs)：使用共享同一 ID 与基地址的 nRF 外设。

- [SPIS 唤醒（SPIS wake up）](P032_SPIS唤醒.md#spis-wakeup)：通过处理唤醒线，降低使用 SPIS 时的电流消耗。

- [同步 RTC（Synchronized RTC）](../timer_reference/P068_nRF53同步实时时钟示例.md#nrf_sync_rtc)：同步系统核与网络核的实时时钟（Real-Time Clock，RTC）。

- [系统关闭（System Off）](../power/P051_Nordic系统关闭示例.md#nrf_system_off)：在 Nordic 平台上使用深度睡眠。

对应官方文档源码：[samples/boards/nordic/index.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/nordic/index.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/nordic/index.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P034_Mesh多模型演示.md) · [返回大纲](大纲.md) · [下一章](P036_microbit_LED矩阵显示.md)
