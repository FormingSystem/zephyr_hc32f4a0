---
id: learning.zephyr-official-intro.hello-world
title: Hello World 示例
kind: engineering
status: maintained
domains: [zephyr, documentation]
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 本文件为中文翻译；章节编号、导航和明确标出的译注为本地新增。 -->

<a id="hello_world"></a>

# 第5章\_Hello World示例

原文：[Hello World](https://docs.zephyrproject.org/latest/samples/hello_world/README.html)。[浏览示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/hello_world)。译文基线：2026-10-12 的 `latest` 页面。

## 5.1\_概述

这是一个简单示例，可用于任何受支持的开发板，在控制台输出“Hello World”。

> 译注：如果开发板没有满足 Blinky 要求的 **发光二极管（Light-Emitting Diode，LED）**，可以用本示例开始。下面演示的是 QEMU 模拟运行；它验证软件构建与模拟目标运行，不证明 HC32 实板已可启动。

## 5.2\_构建与运行

完成[入门指南](P002_入门指南.md)的源码、依赖与工具链准备后，在 Zephyr 源码根目录构建并通过 QEMU 执行：

```text
west build -b qemu_x86 samples/hello_world
west build -t run
```

如需为其他开发板构建，将 `qemu_x86` 替换为目标开发板名称。

> 译注：第一条命令生成指定目标的应用，第二条执行该构建所提供的 `run` 目标。替换为实体开发板时，运行方式应按其文档选择，不意味着所有实体板都可通过同一个 `run` 目标启动。若默认构建目录已用于另一块板，按入门指南使用干净构建或独立构建目录。

## 5.3\_示例输出

原文给出的输出为：

```text
Hello World! x86
```

先按 Ctrl+A，再按 X，退出 QEMU。

> 译注：上面是官方示例输出，不是本轮实测日志。若没有输出，先确认构建成功、实际启动了 QEMU，以及所选目标具有正确的控制台配置。

---

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：LED 闪烁示例](P004_LED闪烁示例.md) · [本模块主线目录](../reading/getting_started.md) · [全部主线](../reading/README.md) · [下一篇：术语表](P006_术语表.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：LED闪烁示例](P004_LED闪烁示例.md) · [返回大纲](大纲.md) · [下一章：术语表](P006_术语表.md)

</details>

<!-- reading-navigation:end -->
