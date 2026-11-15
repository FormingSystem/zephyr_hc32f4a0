---
id: learning.zephyr-docs.api-platform-topic-reference.page-87
title: SiFli SF32LB52x 引脚控制辅助工具（Pin control helpers）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__sf32lb52x.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第87章\_SiFli SF32LB52x 引脚控制辅助工具（Pin control helpers）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__sf32lb52x.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于配置 SiFli SF32LB52x 引脚控制（Pin control）的宏。

<a id="details"></a>

SiFli SF32LB52x 引脚控制配置（Pin Control Configuration）宏。这些宏遵循命名约定（Naming Convention）`<PAD>_<SIGNAL>`。例如，`PA19_USART1_TXD` 表示将 `USART1_TXD` 信号路由到焊盘（Pad）PA19。

```c
#include <zephyr/dt-bindings/pinctrl/sifli/sf32lb52x-pinctrl.h>

&pinctrl {
        usart1_default: usart1_default {
                group1 {
                        pinmux = <PA19_USART1_TXD>;
                };
                group2 {
                        pinmux = <PA18_USART1_RXD>;
                        input-enable;
                        bias-pull-up;
                };
        };
};
```

<a id="header-files"></a>
<a id="files"></a>

## 87.1\_文件（Files）

<a id="r_sf32lb52x-pinctrl_2Eh"></a>

```c
file sf32lb52x-pinctrl.h
```

相关声明：[sf32lb52x-pinctrl.h](../api_file_reference/P388_zephyr__dt-bindings__pinctrl__sf32lb52x-pinctrl.h_文件参考.md)。

SiFli SF32LB52x的设备树引脚控制辅助接口（Devicetree Pin Control Helpers）。


## 87.2\_原页交叉引用（Cross References）

- [sf32lb52x-pinctrl.h](../api_file_reference/P388_zephyr__dt-bindings__pinctrl__sf32lb52x-pinctrl.h_文件参考.md)

<a id="header-details"></a>

---

[上一章](P086_Nuvoton NuMaker M46x 引脚控制辅助工具（Pin control helpers）.md) · [返回大纲](大纲.md) · [下一章](P088_Silicon Labs SiWx91x 引脚控制辅助工具（Pin control helpers）.md)
