---
id: learning.zephyr-docs.basic_samples.page-59
title: LoRaWANA类设备示例
kind: reference
status: maintained
domains: [zephyr, basic_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/lorawan/class_a/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="lorawan-class-a"></a>

# 第59章\_LoRaWANA类设备示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/lorawan/class_a/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

[在GitHub上浏览示例源码](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/subsys/lorawan/class_a/README.rst/..)。

<a id="overview"></a>

## 59.1 概述（Overview）

这是一个展示Zephyr [LoRaWAN子系统](../services_overview/P006_LoRa与LoRaWAN.md#lorawan-api)的简单应用。每到第五次上行（Uplink），它请求一次链路检查（Link Check），并记录网络报告的解调余量（Demodulation Margin）和网关数量（Gateway Count）。

> 译注——计数起点：当前源码的循环变量从0开始，通过`i % LINK_CHECK_PERIOD == 0`决定是否请求检查，且`LINK_CHECK_PERIOD`为5。因此它在第1、6、11……次发送循环中请求链路检查，并非从第5次才开始。计数器跟随循环推进，不是仅统计成功发送的消息。请求随下一次上行发送，答复由注册的回调处理。

<a id="building-and-running"></a>

## 59.2 构建与运行（Building and Running）

构建示例之前，务必在`prj.conf`中选择正确的区域（Region）。以下命令构建并烧录示例：

> 译注——执行前提：在已准备Zephyr开发依赖、目标工具链和烧录工具的UCRT64 Bash或Linux Bash中，以Zephyr源码根目录执行。区域选择应与所用网络和射频硬件配置对应；源码中的设备EUI、加入EUI和应用密钥是示例配置，需要按实际网络配置提供。构建成功后再烧录；若设备未就绪或入网失败，应先检查设备树、区域及网络配置，不能把开始入网的日志当成入网成功。

```sh
west build -b nucleo_wl55jc samples/subsys/lorawan/class_a
west flash
```

> 译注——测试入口：当前控制台测试只匹配`Joining network over OTAA`，它位于`lorawan_join()`之前；这条日志只能说明开始尝试空中激活（Over-the-Air Activation，OTAA），不能证明入网或后续收发通过。本文没有接入LoRaWAN网络或发射数据。

<a id="important-notes-for-multiple-runs"></a>

## 59.3 多次运行的重要说明（Important Notes for Multiple Runs）

默认情况下，这个示例只会在第一次运行时成功。后续加入网络时，由于`dev_nonce`被硬编码，LoRaWAN网络服务器可能拒绝加入请求。按照原文所述的LoRaWAN规范要求，每次新的连接尝试都必须递增`dev_nonce`。

如需多次运行示例，请选择以下一种方式：

1. **手动递增`dev_nonce`（Manually Increment dev_nonce）**：修改示例代码，在每次连接尝试之前递增`join_cfg.otaa.dev_nonce`，并确保其值跨重启保存。
2. **使用Zephyr内置Settings实现（Built-in Zephyr Settings Implementation）**：在Kconfig中启用[`CONFIG_LORAWAN_NVM_SETTINGS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORAWAN_NVM_SETTINGS)，使配置设置及`dev_nonce`能够在多次运行之间正确保存和复用。

> 译注——持久化后端条件：当前源码将`join_cfg.otaa.dev_nonce`设为0。`LORAWAN_NVM_SETTINGS`依赖Settings及`LORA_MODULE_BACKEND_LORAMAC_NODE`；在当前LoRaMAC-node实现中，只有选择`LORAWAN_NVM_NONE`时才直接把应用提供的DevNonce写入协议栈上下文。因此，不能把“启用一个配置项”理解为任意LoRaWAN后端都已经具备相同持久化行为；还需核对Settings存储后端和所用协议栈配置。

<a id="see-also"></a>

## 59.4 另请参阅（See also）

- [LoRaWAN API](https://docs.zephyrproject.org/latest/doxygen/html/group__lorawan__api.html)。


> 译注——实现依据：[samples/subsys/lorawan/class_a/prj.conf](../../../samples/subsys/lorawan/class_a/prj.conf)、[samples/subsys/lorawan/class_a/tests.yaml](../../../samples/subsys/lorawan/class_a/tests.yaml)、[subsys/lorawan/nvm/Kconfig](../../../subsys/lorawan/nvm/Kconfig)、[subsys/lorawan/loramac-node/lorawan.c](../../../subsys/lorawan/loramac-node/lorawan.c)。仓库内参照使用相对链接；官方main快照与本地版本可能不同，所核对文件的摘要见[来源记录](../SOURCES.md)。

对应官方文档源码：[samples/subsys/lorawan/class_a/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/lorawan/class_a/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/subsys/lorawan/class_a/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/subsys/lorawan/class_a/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P058_LoRaWAN示例目录.md) · [返回大纲](大纲.md) · [下一章](P060_LoRaWAN空中固件升级示例.md)
