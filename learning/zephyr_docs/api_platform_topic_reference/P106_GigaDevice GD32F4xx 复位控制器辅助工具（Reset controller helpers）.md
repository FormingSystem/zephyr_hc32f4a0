---
id: learning.zephyr-docs.api-platform-topic-reference.page-106
title: GigaDevice GD32F4xx 复位控制器辅助工具（Reset controller helpers）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__gd32f4xx.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第106章\_GigaDevice GD32F4xx 复位控制器辅助工具（Reset controller helpers）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__reset__controller__gd32f4xx.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

GigaDevice GD32F4xx 复位控制器辅助工具（Reset controller helpers）

<a id="details"></a>

GigaDevice GD32F4xx 复位控制器辅助宏（Reset Controller Helpers）。复位标识（Reset Identifiers）遵循 `GD32_RESET_<PERIPHERAL>` 格式，其中 `<PERIPHERAL>` 为参考手册中的 GD32F4xx 外设名称。例如，`GD32_RESET_USART0` 复位 USART0，`GD32_RESET_GPIOA` 复位 GPIO 端口 A。将这些标识直接传入 `resets` 属性。

<a id="header-files"></a>
<a id="files"></a>

## 106.1\_文件（Files）

<a id="r_gd32f4xx_2Eh"></a>

```c
file gd32f4xx.h
```

相关声明：[gd32f4xx.h](../api_file_reference/P128_zephyr__dt-bindings__reset__gd32f4xx.h_文件参考.md)。

GigaDevice GD32F4xx的外设复位标识符（Peripheral Reset Identifiers）。


## 106.2\_原页交叉引用（Cross References）

- [gd32f4xx.h](../api_file_reference/P128_zephyr__dt-bindings__reset__gd32f4xx.h_文件参考.md)

<a id="header-details"></a>

---

[上一章](P105_GigaDevice GD32F403 复位控制器辅助工具（Reset controller helpers）.md) · [返回大纲](大纲.md) · [下一章](P107_GigaDevice GD32L23x 复位控制器辅助工具（Reset controller helpers）.md)
