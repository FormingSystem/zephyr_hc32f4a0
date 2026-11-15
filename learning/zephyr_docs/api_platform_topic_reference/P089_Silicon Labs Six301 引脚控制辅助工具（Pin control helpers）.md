---
id: learning.zephyr-docs.api-platform-topic-reference.page-89
title: Silicon Labs Six301 引脚控制辅助工具（Pin control helpers）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__six301.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第89章\_Silicon Labs Six301 引脚控制辅助工具（Pin control helpers）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__six301.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于配置 Silicon Labs Six301 引脚控制（Pin control）的宏。

<a id="details"></a>

Silicon Labs Six301 引脚控制配置（Pin Control Configuration）宏。这些宏遵循命名约定（Naming Convention）`<PERIPHERAL>_<SIGNAL>_P<PORT>_<PIN>`。例如，`USART0_TX_PC0` 表示将 USART0 的 TX 信号映射到路由端口 C 的引脚 0。

```c
#include <zephyr/dt-bindings/pinctrl/silabs/six301-pinctrl.h>

&pinctrl {
        usart0_default: usart0_default {
                group0 {
                        pins = <USART0_TX_PC0>, <USART0_CLK_PC2>;
                        drive-push-pull;
                        output-high;
                };
                group1 {
                        pins = <USART0_RX_PC1>;
                        input-enable;
                };
        };
};
```

有效的外设（Peripherals）和信号（Signals）如下：

| 外设（Peripheral） | 信号（Signals） |
| --- | --- |
| `ACMP0` | `ACMPOUT` |
| `ACMP1` | `ACMPOUT` |
| `CMU` | `CLKIN0`, `CLKOUT0`, `CLKOUT1`, `CLKOUT2` |
| `EUSART0` | `CS`, `CTS`, `RTS`, `RX`, `SCLK`, `TX` |
| `EUSART1` | `CS`, `CTS`, `RTS`, `RX`, `SCLK`, `TX` |
| `EUSART2` | `CS`, `CTS`, `RTS`, `RX`, `SCLK`, `TX` |
| `GPIO` | `SWCLKTCK`, `SWDIOTMS`, `SWV`, `TDI`, `TDO`, `TRACECLK`, `TRACEDATA0`, `TRACEDATA1`, `TRACEDATA2`, `TRACEDATA3` |
| `I2C0` | `SCL`, `SDA` |
| `I2C1` | `SCL`, `SDA` |
| `I2C2` | `SCL`, `SDA` |
| `LETIMER0` | `OUT0`, `OUT1` |
| `LFXO` | `LFXOCLKLVRAW` |
| `MODEM` | `ANT0`, `ANT1`, `ANTROLLOVER`, `ANTRR0`, `ANTRR1`, `ANTRR2`, `ANTRR3`, `ANTRR4`, `ANTRR5`, `ANTSWEN`, `ANTSWUS`, `ANTTRIG`, `ANTTRIGSTOP`, `DCLK`, `DIN`, `DOUT` |
| `PCNT0` | `S0IN`, `S1IN` |
| `PIXELRZ0` | `RZTXOUT` |
| `PIXELRZ1` | `RZTXOUT` |
| `PRS0` | `ASYNCH0`, `ASYNCH1`, `ASYNCH10`, `ASYNCH11`, `ASYNCH2`, `ASYNCH3`, `ASYNCH4`, `ASYNCH5`, `ASYNCH6`, `ASYNCH7`, `ASYNCH8`, `ASYNCH9`, `SYNCH0`, `SYNCH1`, `SYNCH2`, `SYNCH3` |
| `PTI` | `DCLK`, `DFRAME`, `DOUT` |
| `RAC` | `LNAEN`, `PAEN` |
| `TIMER0` | `CC0`, `CC1`, `CC2`, `CDTI0`, `CDTI1`, `CDTI2` |
| `TIMER1` | `CC0`, `CC1`, `CC2`, `CDTI0`, `CDTI1`, `CDTI2` |
| `TIMER2` | `CC0`, `CC1`, `CC2`, `CC3`, `CC4`, `CC5`, `CC6`, `CCC4`, `CCC5`, `CCC6`, `CDTI0`, `CDTI1`, `CDTI2`, `CDTI3`, `CDTI4`, `CDTI5`, `CDTI6` |
| `TIMER3` | `CC0`, `CC1`, `CC2`, `CC3`, `CC4`, `CC5`, `CC6`, `CCC4`, `CCC5`, `CCC6`, `CDTI0`, `CDTI1`, `CDTI2`, `CDTI3`, `CDTI4`, `CDTI5`, `CDTI6` |

<a id="header-files"></a>
<a id="files"></a>

## 89.1\_文件（Files）

<a id="r_six301-pinctrl_2Eh"></a>

```c
file six301-pinctrl.h
```

相关声明：[six301-pinctrl.h](../api_file_reference/P399_zephyr__dt-bindings__pinctrl__silabs__six301-pinctrl.h_文件参考.md)。

Silicon Labs Six301的设备树引脚控制辅助接口（Devicetree Pin Control Helpers）。


## 89.2\_原页交叉引用（Cross References）

- [six301-pinctrl.h](../api_file_reference/P399_zephyr__dt-bindings__pinctrl__silabs__six301-pinctrl.h_文件参考.md)

<a id="header-details"></a>

---

[上一章](P088_Silicon Labs SiWx91x 引脚控制辅助工具（Pin control helpers）.md) · [返回大纲](大纲.md) · [下一章](P090_Silicon Labs xG21 引脚控制辅助工具（Pin control helpers）.md)
