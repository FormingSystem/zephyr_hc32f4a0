---
id: learning.zephyr-docs.driver_samples.page-39
title: SENT接口示例
kind: reference
status: maintained
domains: [zephyr, driver_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/sent/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="sent"></a>

# 第39章\_SENT接口示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/drivers/sent/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 39.1\_概览（Overview）

本例演示通过[单边沿半字节传输（Single Edge Nibble Transmission，SENT）API](../hardware/P139_单边沿半字节传输.md#sent-api)接收数据。半字节（Nibble）指4位数据。

<a id="requirements"></a>

## 39.2\_要求（Requirements）

需要连接一个SENT传感器，并通过`sent0`设备树（Devicetree）别名提供访问。

<a id="building-flashing-and-running"></a>

## 39.3\_构建、烧录与运行（Building, Flashing and Running）

> 译注——执行前提：以下原命令从已配置Zephyr环境的终端、Zephyr源码根目录执行。先按所用板配置确认传感器、控制器和接收通道，构建成功后再烧录；编译或设备配置错误时返回相关前提检查。

```bash
# From the root of the zephyr repository
west build -b s32z2xxdc2/s32z270/rtu0 samples/drivers/sent
west flash
```

原示例输出：

```text
Received a frame on channel 1
```

> 译注——接收类型：所读[main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/sent/src/main.c)在通道1注册串行帧（Serial Frame）和快速帧（Fast Frame）回调并启动监听。当前快速帧回调会打印六个数据半字节及时间戳，串行帧回调会打印ID、数据与时间戳；上面的单行日志是原页摘要，不能替代对具体帧内容的验证。本批未运行传感器接收实验。

<a id="see-also"></a>

## 39.4\_相关接口（See also）

[SENT接口参考](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html)。


对应官方文档源码：[samples/drivers/sent/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/sent/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/drivers/sent/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/drivers/sent/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P038_PSI5接口示例.md) · [返回大纲](大纲.md) · [下一章](P040_脉冲IO示例目录.md)
