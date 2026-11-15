---
id: learning.zephyr-docs.portability.page-2
title: CMSISRTOS版本1
kind: reference
status: maintained
domains: [zephyr, portability, cmsis]
source_url: https://docs.zephyrproject.org/latest/services/portability/cmsis_rtos_v1.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_CMSISRTOS版本1

原文：[官方页面](https://docs.zephyrproject.org/latest/services/portability/cmsis_rtos_v1.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 2.1\_CMSIS-RTOS 第 1 版

Cortex-M 软件接口标准（Cortex-M Software Interface Standard，CMSIS）RTOS 是面向 Arm Cortex-M 处理器系列、与厂商无关的硬件抽象层，并定义通用工具接口。虽然最初仅面向 Arm Cortex-M 微控制器，也容易扩展到其他微控制器，从而成为通用接口。

更多 CMSIS RTOS v1 信息见 [CMSIS-RTOS1 官方文档](https://arm-software.github.io/CMSIS_5/latest/RTOS/html/index.html)。

译注——名称边界：上段按原页措辞翻译。本册讨论的是实时操作系统（Real-Time Operating System，RTOS）接口兼容层；它与提供处理器内核访问定义的 CMSIS-Core、提供信号处理算法的 CMSIS-DSP 属于不同功能部分。引入厂商 CMSIS 设备头文件不等于已启用 CMSIS-RTOS 兼容接口。Zephyr 的对应入口为 `CONFIG_CMSIS_RTOS_V1`，实现位于 `subsys/portability/cmsis_rtos_v1/`；应用示例见[版本 1 示例目录](P004_CMSISRTOS1示例目录.md)。


译注核对来源：[subsys/portability/cmsis_rtos_v1/Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/cmsis_rtos_v1/Kconfig)。

本仓库的[对应源码](../../../subsys/portability/cmsis_rtos_v1/Kconfig)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="cmsis-rtos-v1"></a>
<a id="id1"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：操作系统抽象入口](P001_操作系统抽象入口.md) · [本模块主线目录](../reading/portability.md) · [全部主线](../reading/README.md) · [下一篇：CMSISRTOS版本2](P003_CMSISRTOS版本2.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P001_操作系统抽象入口.md) · [返回大纲](大纲.md) · [下一章](P003_CMSISRTOS版本2.md)

</details>

<!-- reading-navigation:end -->
