---
id: learning.zephyr-docs.api-platform-topic-reference.page-74
title: Ambiq Apollo4 引脚控制辅助工具（Pin control helpers）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__apollo4.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第74章\_Ambiq Apollo4 引脚控制辅助工具（Pin control helpers）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__apollo4.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于配置 Ambiq Apollo4 引脚控制（Pin control）的宏。

<a id="details"></a>

Ambiq Apollo4 引脚控制配置（Pin Control Configuration）宏。这些宏遵循命名约定（Naming Convention）`<FUNCTION>_P<PIN>`。例如，`UART0TX_P60` 表示在引脚 60 上选择 `UART0TX` 功能。

```c
#include <zephyr/dt-bindings/pinctrl/ambiq-apollo4-pinctrl.h>

&pinctrl {
        uart0_default: uart0_default {
                group1 {
                        pinmux = <UART0TX_P60>;
                };
                group2 {
                        pinmux = <UART0RX_P47>;
                        input-enable;
                };
        };
};
```

<a id="header-files"></a>
<a id="files"></a>

## 74.1\_文件（Files）

<a id="r_ambiq-apollo4-pinctrl_2Eh"></a>

```c
file ambiq-apollo4-pinctrl.h
```

相关声明：[ambiq-apollo4-pinctrl.h](../api_file_reference/P009_zephyr__dt-bindings__pinctrl__ambiq-apollo4-pinctrl.h_文件参考.md)。

Ambiq Apollo4的设备树引脚控制辅助接口（Devicetree Pin Control Helpers）。


## 74.2\_原页交叉引用（Cross References）

- [ambiq-apollo4-pinctrl.h](../api_file_reference/P009_zephyr__dt-bindings__pinctrl__ambiq-apollo4-pinctrl.h_文件参考.md)

<a id="header-details"></a>

---

[上一章](P073_Ambiq Apollo3 引脚控制辅助工具（Pin control helpers）.md) · [返回大纲](大纲.md) · [下一章](P075_Ambiq Apollo5 引脚控制辅助工具（Pin control helpers）.md)
