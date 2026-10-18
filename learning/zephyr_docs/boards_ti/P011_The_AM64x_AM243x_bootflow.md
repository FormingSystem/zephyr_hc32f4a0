---
id: learning.zephyr-docs.boards-ti.page-11
title: The AM64x AM243x bootflow
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/ti/common/doc/k3/am64x-am243x-bootmodes.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="the-am64x-am243x-bootflow"></a>

# 第11章\_AM64x／AM243x启动流程（Bootflow）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/ti/common/doc/k3/am64x-am243x-bootmodes.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

AM64x／AM243x系列SoC因支持安全启动（Secure Boot）而具有专用启动流程。上电后首先在R5F0_0执行ROM内不可修改的引导加载器（RBL），随后应执行基于TI MCU+ SDK的第二阶段引导加载器（SBL），由其启动最终Zephyr固件。RBL可从外部闪存或UART传输等多种来源取得镜像。仅在AM64x上，也可使用TI SDK预制镜像充当SBL，在Cortex-A上启动Linux，再通过remoteproc将Zephyr固件加载到其他核。

## 译注

本页是AM64x／AM243x共用启动流程。Linux作为SBL后续环境及remoteproc加载只适用于有Cortex-A的AM64x。

---

[上一章](P010_CC3235SF_LaunchXL.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P012_AM64x_AM243x_features.md)
