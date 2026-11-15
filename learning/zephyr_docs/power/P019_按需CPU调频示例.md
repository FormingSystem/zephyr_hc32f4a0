---
id: learning.zephyr-docs.power.cpufreqsample-1
title: 按需CPU调频示例
kind: reference
status: maintained
domains: [zephyr, power]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/cpu_freq/on_demand/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="cpu_freq_on_demand"></a>

# 第19章\_按需CPU调频示例

原文：[On-demand CPU frequency scaling](https://docs.zephyrproject.org/latest/samples/subsys/cpu_freq/on_demand/README.html)。读取日期：2026-10-13，`latest`。

## 19.1\_概述

本示例展示中央处理器（Central Processing Unit，CPU）调频子系统的[按需策略（On-Demand Policy）](P014_按需CPU调频策略.md)。示例向控制台输出 CPU 负载及调频子系统日志等调试信息，便于观察子系统。

主应用依次模拟几种 CPU 处理场景。

## 19.2\_使用叠加配置构建

要使用 `pstate-stub.overlay` 叠加配置（Overlay）文件，按以下命令构建示例：

```shell
west build -b <board> -p -- -DDTC_OVERLAY_FILE=pstate-stub.overlay
```

译注：原命令未指定应用源码目录，应在本示例目录中执行；`<board>` 替换为目标开发板。这里的桩实现（Stub）用于演练调频子系统；[官方Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/cpu_freq/Kconfig)说明桩设置器本身不会改变实际 CPU 频率。

---

[上一章：CPU调频示例目录](P018_CPU调频示例目录.md) · [下一章：压力CPU调频示例](P020_压力CPU调频示例.md) · [返回大纲](大纲.md)
