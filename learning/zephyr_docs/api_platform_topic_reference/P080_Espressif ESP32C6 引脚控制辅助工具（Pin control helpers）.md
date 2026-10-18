---
id: learning.zephyr-docs.api-platform-topic-reference.page-80
title: Espressif ESP32C6 引脚控制辅助工具（Pin control helpers）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__esp32c6.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第80章\_Espressif ESP32C6 引脚控制辅助工具（Pin control helpers）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__esp32c6.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于配置 Espressif ESP32C6 引脚控制（Pin control）的宏。

<a id="details"></a>

Espressif ESP32C6 引脚控制配置（Pin Control Configuration）宏。这些宏遵循命名约定（Naming Convention）`<PERIPHERAL>_<SIGNAL>_GPIO<PIN>`。例如，`I2C0_SCL_GPIO1` 表示将 I2C0 的 SCL 信号映射到 GPIO1。

```c
#include <zephyr/dt-bindings/pinctrl/esp32c6-pinctrl.h>

&pinctrl {
    uart0_default: uart0_default {
        group1 {
            pinmux = <UART0_TX_GPIO21>;
        };
        group2 {
            pinmux = <UART0_RX_GPIO20>;
            bias-pull-up;
        };
    };
};
```

<a id="header-files"></a>
<a id="files"></a>

## 80.1\_文件（Files）

<a id="r_esp32c6-gpio-sigmap_2Eh"></a>

```c
file esp32c6-gpio-sigmap.h
```

相关声明：[esp32c6-gpio-sigmap.h](../api_file_reference/P095_zephyr__dt-bindings__pinctrl__esp32c6-gpio-sigmap.h_文件参考.md)。

ESP32-C6的GPIO信号映射定义（GPIO Signal Map Definitions）。

<a id="r_esp32c6-pinctrl_2Eh"></a>

```c
file esp32c6-pinctrl.h
```

相关声明：[esp32c6-pinctrl.h](../api_file_reference/P096_zephyr__dt-bindings__pinctrl__esp32c6-pinctrl.h_文件参考.md)。

Espressif ESP32C6的设备树引脚控制辅助接口（Devicetree Pin Control Helpers）。


## 80.2\_原页交叉引用（Cross References）

- [esp32c6-gpio-sigmap.h](../api_file_reference/P095_zephyr__dt-bindings__pinctrl__esp32c6-gpio-sigmap.h_文件参考.md)
- [esp32c6-pinctrl.h](../api_file_reference/P096_zephyr__dt-bindings__pinctrl__esp32c6-pinctrl.h_文件参考.md)
- [I2C0_SCL_GPIO1](../api_file_reference/P025_zephyr__dt-bindings__pinctrl__bcm2711-pinctrl.h_文件参考.md#ad7867c2e0f104e72b808749a3be13b1e)

<a id="header-details"></a>

---

[上一章](P079_Espressif ESP32C5 引脚控制辅助工具（Pin control helpers）.md) · [返回大纲](大纲.md) · [下一章](P081_Espressif ESP32C61 引脚控制辅助工具（Pin control helpers）.md)
