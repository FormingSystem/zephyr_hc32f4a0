---
id: learning.zephyr-docs.api-platform-topic-reference.page-88
title: Silicon Labs SiWx91x 引脚控制辅助工具（Pin control helpers）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__siwx91x.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第88章\_Silicon Labs SiWx91x 引脚控制辅助工具（Pin control helpers）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__siwx91x.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于配置 Silicon Labs SiWx91x 引脚控制（Pin control）的宏。

<a id="details"></a>

Silicon Labs SiWx91x 引脚控制配置（Pin Control Configuration）宏。这些宏遵循命名约定（Naming Convention）`<PERIPHERAL>_<SIGNAL>_<PIN>`。例如，`USART0_TX_PC0` 表示将 USART0 的 TX 信号映射到路由端口 C 的引脚 0。

```c
#include <zephyr/dt-bindings/pinctrl/silabs/siwx91x-pinctrl.h>

&pinctrl {
      ulpuart_default: ulpuart_default {
        out {
                pinmux = <ULPUART_TX_ULP11>;
        };
        in {
                pinmux = <ULPUART_RX_ULP9>;
        };
     };
};
```

<a id="header-files"></a>
<a id="files"></a>

## 88.1\_文件（Files）

<a id="r_siwx91x-pinctrl_2Eh"></a>

```c
file siwx91x-pinctrl.h
```

相关声明：[siwx91x-pinctrl.h](../api_file_reference/P396_zephyr__dt-bindings__pinctrl__silabs__siwx91x-pinctrl.h_文件参考.md)。

Silicon Labs SiWx91x的设备树引脚控制辅助接口（Devicetree Pin Control Helpers）。


## 88.2\_原页交叉引用（Cross References）

- [siwx91x-pinctrl.h](../api_file_reference/P396_zephyr__dt-bindings__pinctrl__silabs__siwx91x-pinctrl.h_文件参考.md)

<a id="header-details"></a>

---

[上一章](P087_SiFli SF32LB52x 引脚控制辅助工具（Pin control helpers）.md) · [返回大纲](大纲.md) · [下一章](P089_Silicon Labs Six301 引脚控制辅助工具（Pin control helpers）.md)
