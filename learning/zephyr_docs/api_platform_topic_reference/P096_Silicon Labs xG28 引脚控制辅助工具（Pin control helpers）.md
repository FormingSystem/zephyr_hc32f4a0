---
id: learning.zephyr-docs.api-platform-topic-reference.page-96
title: Silicon Labs xG28 引脚控制辅助工具（Pin control helpers）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__xg28.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第96章\_Silicon Labs xG28 引脚控制辅助工具（Pin control helpers）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__pinctrl__xg28.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于配置 Silicon Labs xG28 引脚控制（Pin control）的宏。

<a id="details"></a>

Silicon Labs xG28 引脚控制配置（Pin Control Configuration）宏。这些宏遵循命名约定（Naming Convention）`<PERIPHERAL>_<SIGNAL>_P<PORT>_<PIN>`。例如，`USART0_TX_PC0` 表示将 USART0 的 TX 信号映射到路由端口 C 的引脚 0。

```c
#include <zephyr/dt-bindings/pinctrl/silabs/xg28-pinctrl.h>

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
| `HFXO0` | `BUFOUTREQINASYNC` |
| `I2C0` | `SCL`, `SDA` |
| `I2C1` | `SCL`, `SDA` |
| `KEYSCAN` | `COLOUT0`, `COLOUT1`, `COLOUT2`, `COLOUT3`, `COLOUT4`, `COLOUT5`, `COLOUT6`, `COLOUT7`, `ROWSENSE0`, `ROWSENSE1`, `ROWSENSE2`, `ROWSENSE3`, `ROWSENSE4`, `ROWSENSE5` |
| `LESENSE` | `CH0OUT`, `CH10OUT`, `CH11OUT`, `CH12OUT`, `CH13OUT`, `CH14OUT`, `CH15OUT`, `CH1OUT`, `CH2OUT`, `CH3OUT`, `CH4OUT`, `CH5OUT`, `CH6OUT`, `CH7OUT`, `CH8OUT`, `CH9OUT` |
| `LETIMER0` | `OUT0`, `OUT1` |
| `MODEM` | `ANT0`, `ANT1`, `ANTROLLOVER`, `ANTRR0`, `ANTRR1`, `ANTRR2`, `ANTRR3`, `ANTRR4`, `ANTRR5`, `ANTSWEN`, `ANTSWUS`, `ANTTRIG`, `ANTTRIGSTOP`, `DCLK`, `DIN`, `DOUT` |
| `PCNT0` | `S0IN`, `S1IN` |
| `PRS0` | `ASYNCH0`, `ASYNCH1`, `ASYNCH10`, `ASYNCH11`, `ASYNCH2`, `ASYNCH3`, `ASYNCH4`, `ASYNCH5`, `ASYNCH6`, `ASYNCH7`, `ASYNCH8`, `ASYNCH9`, `SYNCH0`, `SYNCH1`, `SYNCH2`, `SYNCH3` |
| `PTI` | `DCLK`, `DFRAME`, `DOUT` |
| `TIMER0` | `CC0`, `CC1`, `CC2`, `CDTI0`, `CDTI1`, `CDTI2` |
| `TIMER1` | `CC0`, `CC1`, `CC2`, `CDTI0`, `CDTI1`, `CDTI2` |
| `TIMER2` | `CC0`, `CC1`, `CC2`, `CDTI0`, `CDTI1`, `CDTI2` |
| `TIMER3` | `CC0`, `CC1`, `CC2`, `CDTI0`, `CDTI1`, `CDTI2` |
| `TIMER4` | `CC0`, `CC1`, `CC2`, `CDTI0`, `CDTI1`, `CDTI2` |
| `USART0` | `CLK`, `CS`, `CTS`, `RTS`, `RX`, `TX` |

<a id="header-files"></a>
<a id="files"></a>

## 96.1\_文件（Files）

<a id="r_xg28-pinctrl_2Eh"></a>

```c
file xg28-pinctrl.h
```

相关声明：[xg28-pinctrl.h](../api_file_reference/P511_zephyr__dt-bindings__pinctrl__silabs__xg28-pinctrl.h_文件参考.md)。

Silicon Labs xG28的设备树引脚控制辅助接口（Devicetree Pin Control Helpers）。


## 96.2\_原页交叉引用（Cross References）

- [xg28-pinctrl.h](../api_file_reference/P511_zephyr__dt-bindings__pinctrl__silabs__xg28-pinctrl.h_文件参考.md)

<a id="header-details"></a>

---

[上一章](P095_Silicon Labs xG27 引脚控制辅助工具（Pin control helpers）.md) · [返回大纲](大纲.md) · [下一章](P097_Silicon Labs xG29 引脚控制辅助工具（Pin control helpers）.md)
