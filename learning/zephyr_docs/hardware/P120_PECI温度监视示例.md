---
id: learning.zephyr-docs.hardware.powersamp-1
title: PECI温度监视示例
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/peci/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="peci"></a>

# 第120章\_PECI温度监视示例

原文：[PECI interface](https://docs.zephyrproject.org/latest/samples/drivers/peci/README.html)。读取日期：2026-10-13，`latest`。

## 120.1\_观察PECI主机交互

本示例演示 **平台环境控制接口（Platform Environment Control Interface，PECI）**的 **应用程序编程接口（Application Programming Interface，API）**。程序注册 **回调函数（Callback Function）**，在控制台输出PECI事件，用于观察与PECI主机的交互。接口概览见[平台环境控制接口](P115_平台环境控制接口.md)。

## 120.2\_构建运行条件与原输出

示例可在支持PECI的开发板上构建和执行。执行时，所使用的微控制器必须连接到 **PECI主机（PECI Host）**。

原页没有给出具体构建命令，仅给出下列输出；其中ID表示 **标识符（Identifier）**，提示读者预期会看到标识读取和温度获取等多次交互：

```text
PECI test
Note: You are expected to see several interactions including ID and
temperature retrieval.
```

## 120.3\_接口与源码

完整声明见[PECI API](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html)，源码见[官方PECI示例目录](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/drivers/peci)。原页将示例用途概括为通过PECI监视 **中央处理器（Central Processing Unit，CPU）**温度；本文未连接PECI主机或读取实际温度。

[上一章：EDAC命令行示例](P119_EDAC命令行示例.md) · [下一章：电池充电示例](P121_电池充电示例.md) · [返回大纲](大纲.md)
