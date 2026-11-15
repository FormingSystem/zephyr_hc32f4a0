---
id: learning.zephyr-docs.api-platform-topic-reference.page-86
title: Nuvoton NuMaker M46x 引脚控制辅助工具（Pin control helpers）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__numaker__m46x.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第86章\_Nuvoton NuMaker M46x 引脚控制辅助工具（Pin control helpers）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__numaker__m46x.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于配置 Nuvoton NuMaker M46x 引脚控制（Pin control）的宏。

<a id="details"></a>

Nuvoton NuMaker M46x 引脚控制配置（Pin Control Configuration）宏。这些宏遵循命名约定（Naming Convention）`<PORT><PIN>MFP_<FUNCTION>`。例如，`PB12MFP_UART0_RXD` 表示将 `UART0_RXD` 功能路由到端口 B 的引脚 12。

```c
#include <zephyr/dt-bindings/pinctrl/numaker-m46x-pinctrl.h>

&pinctrl {
        uart0_default: uart0_default {
                group1 {
                        pinmux = <PB12MFP_UART0_RXD>,
                                 <PB13MFP_UART0_TXD>;
                };
        };
};
```

<a id="header-files"></a>
<a id="files"></a>

## 86.1\_文件（Files）

<a id="r_numaker-m46x-pinctrl_2Eh"></a>

```c
file numaker-m46x-pinctrl.h
```

相关声明：[numaker-m46x-pinctrl.h](../api_file_reference/P260_zephyr__dt-bindings__pinctrl__numaker-m46x-pinctrl.h_文件参考.md)。

Nuvoton NuMaker M46x的设备树引脚控制辅助接口（Devicetree Pin Control Helpers）。


## 86.2\_原页交叉引用（Cross References）

- [numaker-m46x-pinctrl.h](../api_file_reference/P260_zephyr__dt-bindings__pinctrl__numaker-m46x-pinctrl.h_文件参考.md)

<a id="header-details"></a>

---

[上一章](P085_Espressif ESP32S3 引脚控制辅助工具（Pin control helpers）.md) · [返回大纲](大纲.md) · [下一章](P087_SiFli SF32LB52x 引脚控制辅助工具（Pin control helpers）.md)
