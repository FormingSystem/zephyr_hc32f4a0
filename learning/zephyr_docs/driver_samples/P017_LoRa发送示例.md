---
id: learning.zephyr-docs.driver_samples.page-17
title: LoRa发送示例
kind: reference
status: maintained
domains: [zephyr, driver_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/lora/send/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="lora-send"></a>

# 第17章\_LoRa发送示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/drivers/lora/send/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 17.1\_概览（Overview）

本例演示通过LoRa无线电驱动配置编码参数（Encoding Settings）并发送无线数据。在通信范围内的另一块板上构建并烧录配套[LoRa接收示例](P016_LoRa接收示例.md#lora-receive)，即可接收这些消息。

<a id="building-and-running"></a>

## 17.2\_构建与运行（Building and Running）

按以下方式构建并烧录；将b_l072z_lrwan1替换为实际开发板，该板的设备树需有 `lora0` 别名。

```bash
west build -b b_l072z_lrwan1 samples/drivers/lora/send
west flash
```

> 译注——前提：从读者Zephyr源码根执行，先确认工具链、模块、无线电设备与lora0配置。替换板名仍需对应硬件支持，且收发两端的调制参数必须匹配。本页演示直接使用LoRa驱动，不将发送成功日志当作接收端已收到的证明。

<a id="sample-output"></a>

### 17.2.1\_示例输出（Sample Output）

```text
[00:00:00.531,000] <inf> lora_send: Data sent 0!
[00:00:01.828,000] <inf> lora_send: Data sent 1!
[00:00:03.125,000] <inf> lora_send: Data sent 2!
```

> 译注——发送间隔：所读[main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/lora/send/src/main.c)在lora_send返回后休眠1000毫秒，再改变载荷末位字符发送下一包。因此“每秒发送”描述的是循环中的休眠，发送开始时间还受空中传输和其他开销影响；原日志相邻时间约相差1.297秒，与精确1秒周期不同。本批未运行无线发送。

<a id="see-also"></a>

## 17.3\_相关接口（See also）

[LoRa接口参考](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html)。


对应官方文档源码：[samples/drivers/lora/send/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/lora/send/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/drivers/lora/send/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/drivers/lora/send/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P016_LoRa接收示例.md) · [返回大纲](大纲.md) · [下一章](P018_调制解调器示例目录.md)
