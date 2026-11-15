---
id: learning.zephyr-docs.api-platform-topic-reference.page-75
title: Ambiq Apollo5 引脚控制辅助工具（Pin control helpers）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__apollo5.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第75章\_Ambiq Apollo5 引脚控制辅助工具（Pin control helpers）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__apollo5.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于配置 Ambiq Apollo5 引脚控制（Pin control）的宏。

<a id="details"></a>

Ambiq Apollo5 引脚控制配置（Pin Control Configuration）宏。使用 `APOLLO5_PINMUX()` 为设备树 `pinmux` 属性编码引脚编号（Pin Number）和复用功能（Alternative Function）。

```c
#include <zephyr/dt-bindings/pinctrl/ambiq-apollo5-pinctrl.h>

&pinctrl {
        uart0_default: uart0_default {
                group1 {
                        pinmux = <APOLLO5_PINMUX(60, 4)>;
                };
                group2 {
                        pinmux = <APOLLO5_PINMUX(47, 4)>;
                        input-enable;
                };
        };
};
```

<a id="header-files"></a>
<a id="files"></a>

## 75.1\_文件（Files）

<a id="r_ambiq-apollo5-pinctrl_2Eh"></a>

```c
file ambiq-apollo5-pinctrl.h
```

相关声明：[ambiq-apollo5-pinctrl.h](../api_file_reference/P010_zephyr__dt-bindings__pinctrl__ambiq-apollo5-pinctrl.h_文件参考.md)。

Ambiq Apollo5的设备树引脚控制辅助接口（Devicetree Pin Control Helpers）。


## 75.2\_原页交叉引用（Cross References）

- [ambiq-apollo5-pinctrl.h](../api_file_reference/P010_zephyr__dt-bindings__pinctrl__ambiq-apollo5-pinctrl.h_文件参考.md)

<a id="header-details"></a>

---

[上一章](P074_Ambiq Apollo4 引脚控制辅助工具（Pin control helpers）.md) · [返回大纲](大纲.md) · [下一章](P076_Espressif ESP32 引脚控制辅助工具（Pin control helpers）.md)
