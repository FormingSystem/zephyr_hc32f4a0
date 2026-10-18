---
id: learning.zephyr-docs.board-samples.page-81
title: NXP示例目录
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/nxp/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="nxp"></a>

# 第81章\_NXP

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/nxp/index.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

这些示例展示如何在 Zephyr 中使用 NXP 开发板。

> 译注——目录范围：音频回环和音频输出两个条目沿用相同官方标题，按链接和冒号后的用途区分。模拟信号链、mbox 和挂起到RAM三篇沿用既有专题译文；此目录覆盖官方NXP示例，不代表NXP全部独立开发板、设备树绑定和API参考均已翻译。

- [音频输出 AMP 示例（Audio output AMP sample）](P075_DSP非对称多处理音频回环.md#amp_audio_loopback)：NXP i.MX RTxxx 平台的 AMP 系统示例，演示音频回环。

- [音频输出 AMP 示例（Audio output AMP sample）](P076_DSP非对称多处理音频输出.md#amp_audio_output)：NXP i.MX RTxxx 平台的 AMP 系统示例，演示音频输出。

- [AMP 闪灯示例（Blinky AMP sample）](P077_DSP非对称多处理闪灯.md#amp_blinky)：NXP i.MX RTxxx 平台的 AMP 系统示例，演示 LED 闪烁。

- [FLEXRAM 魔术地址（FLEXRAM magic address）](P072_FLEXRAM魔术地址.md#flexram_magic_addr)：配置在访问 RAM／TCM 地址时触发的中断。

- [FRDM-MCXA156 的低功耗 DAC、运算放大器与低功耗 ADC 示例（lpdac opamp lpadc example）](../hardware/P099_FRDM模拟信号链示例.md#frdm_mcxa156_lpdac_opamp_lpadc)：放大 OPAMP 输入，并通过 ADC 采样。

- [mbox API 的 AMP 示例（mbox API AMP sample）](../intercore_reference/P031_RTxxx非对称多处理邮箱示例.md#amp_mbox)：NXP i.MX RTxxx 平台的 AMP 系统示例，使用 mbox API 进行处理器间通信。

- [使用优化库进行数值计算（Number crunching using optimized library）](P074_DSP优化库计算.md#number_crunching)：设置并使用不同后端执行复杂数学运算。

- [NXP MCX 挂起到 RAM（NXP MCX suspend-to-RAM）](../power/P052_NXP_MCX挂起到RAM示例.md#nxp_mcx_s2ram)：将 MCXA／MCXN SoC 挂起到 RAM，再通过 WUU 唤醒控制器传递的 LPTMR 定时器或按钮事件唤醒并恢复。

- [NXP MCX 系统关闭（NXP MCX system off）](P067_NXP_MCX系统关闭.md#nxp_mcx_system_off)：使 MCXA／MCXN SoC 进入深度掉电，并通过 WUU 唤醒控制器唤醒。

- [NXP SmartDMA 内存到内存传输（NXP SmartDMA memory-to-memory）](P073_SmartDMA内存到内存传输.md#nxp_smartdma_mem_to_mem)：通过 Zephyr DMA API 使用 SmartDMA 协处理器执行内存到内存传输。

- [OpenAMP DSP 非对称多处理示例（OpenAMP DSP AMP Sample）](P078_DSP非对称多处理OpenAMP通信.md#amp_talk)：通过并发的 OpenAMP 通信通道在多个内核之间传递消息。

- [RT1060 系统关闭（RT1060 System Off）](P068_RT1060系统关闭.md#mimxrt1060_evk_system_off)：在 MIMXRT1060-EVK 上使用软关闭。

- [RT595 系统关闭（RT595 System Off）](P069_RT595系统关闭.md#mimxrt595_evk_system_off)：在 MIMXRT595-EVK 上使用软关闭。

- [RT700 EVK 双核电源管理（RT700 EVK dual-core power management）](P070_RT700双核电源管理.md#nxp_rt700_dual_core_pm)：测试两个 Cortex-M33 内核的活动、睡眠、深度睡眠和深度睡眠保持组合。

- [RT700 系统关闭（RT700 System Off）](P071_RT700系统关闭.md#mimxrt700_evk_system_off)：在 MIMXRT700-EVK 上使用系统关闭。

- [RW612 电源管理后的 Flash 检查（RW612 PM flash check）](P066_RW612低功耗Flash擦写检查.md#rw612_pm_flash_check)：检查外部 NOR Flash 跨越 RW612 低功耗状态后的工作情况。

- [S32 网络控制器（S32 Network Controller，NETC）](P079_S32网络控制器.md#nxp_s32_netc)：配置 NXP S32 NETC。

- [系统关闭：MCXE31B 待机（System Off: MCXE31B standby）](P065_MCXE31B待机与唤醒.md#frdm-mcxe31b-system-off)：使用 FRDM-MCXE31B 唯一的低功耗待机模式，并由 RTC 闹钟唤醒。

- [NXP Neutron 上的微控制器 TensorFlow Lite（TensorFlow Lite for Microcontrollers on NXP Neutron）](P080_Neutron微控制器机器学习推理.md#tflite-neutron)：在 Neutron NPU 上使用 MobileNet 模型进行推理。

对应官方文档源码：[samples/boards/nxp/index.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/nxp/index.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/nxp/index.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P080_Neutron微控制器机器学习推理.md) · [返回大纲](大纲.md) · [下一章](P082_ARC安全服务.md)
