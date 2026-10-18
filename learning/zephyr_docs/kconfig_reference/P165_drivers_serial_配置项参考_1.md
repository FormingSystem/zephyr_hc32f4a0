---
id: learning.zephyr-docs.kconfig-reference.page-165
title: "`drivers/serial`配置项参考（1/5）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第165章\_`drivers/serial`配置项参考（1/5）

本章翻译官方 Kconfig 数据库中 `drivers/serial` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_LEUART_GECKO"></a>

## 165.1 `CONFIG_LEUART_GECKO`

**提示（Prompt）**：Gecko 低能耗 UART（LEUART）驱动

**说明（Help）**

启用 Gecko 低能耗 UART（LEUART）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_GECKO_LEUART_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_SERIAL_SUPPORT_INTERRUPT
CONFIG_SILABS_GECKO_LEUART
```

**定义位置（Location）**：[`drivers/serial/Kconfig.leuart_gecko:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.leuart_gecko#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)、[`CONFIG_SILABS_GECKO_LEUART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_GECKO_LEUART)。

<a id="CONFIG_LPUART_ESP32"></a>

## 165.2 `CONFIG_LPUART_ESP32`

**提示（Prompt）**：ESP32 低功耗 UART（LP UART）驱动

**说明（Help）**

启用 ESP32 低功耗 UART（LP UART）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ESPRESSIF_ESP32_LPUART_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
```

**定义位置（Location）**：[`drivers/serial/Kconfig.esp32:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.esp32#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)。

<a id="CONFIG_SERIAL"></a>

## 165.3 `CONFIG_SERIAL`

**提示（Prompt）**：串行驱动（Serial Drivers）

**说明（Help）**

启用串行驱动（Serial Driver）的相关选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_AUXDISPLAY_ITRON
CONFIG_BIOMETRICS_GT5X
CONFIG_BIOMETRICS_ZFM_X0
CONFIG_BT_UART
CONFIG_TMC6460_UART
CONFIG_STEPPER_ADI_TMC_UART
CONFIG_STEPPER_ADI_TMCM_RS485
CONFIG_W1_ZEPHYR_SERIAL
CONFIG_WIFI_ESWIFI_BUS_UART
CONFIG_GNSS_RTK_SERIAL
CONFIG_SHELL_BACKEND_SERIAL
```

**被弱选择（Implied by）**

```text
CONFIG_MPIPE_PLAYER
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/openthread_rcp_arduino/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/openthread_rcp_arduino/Kconfig.defconfig)。

```text
y if CONFIG_SHIELD_OPENTHREAD_RCP_ARDUINO_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_AUXDISPLAY_ITRON`](P051_drivers_auxdisplay_配置项参考.md#CONFIG_AUXDISPLAY_ITRON)、[`CONFIG_BIOMETRICS_GT5X`](P053_drivers_biometrics_配置项参考.md#CONFIG_BIOMETRICS_GT5X)、[`CONFIG_BIOMETRICS_ZFM_X0`](P053_drivers_biometrics_配置项参考.md#CONFIG_BIOMETRICS_ZFM_X0)、[`CONFIG_BT_UART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_UART)、[`CONFIG_TMC6460_UART`](P123_drivers_misc_配置项参考.md#CONFIG_TMC6460_UART)、[`CONFIG_STEPPER_ADI_TMC_UART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STEPPER_ADI_TMC_UART)、[`CONFIG_STEPPER_ADI_TMCM_RS485`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STEPPER_ADI_TMCM_RS485)、[`CONFIG_W1_ZEPHYR_SERIAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_W1_ZEPHYR_SERIAL)、[`CONFIG_WIFI_ESWIFI_BUS_UART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_ESWIFI_BUS_UART)、[`CONFIG_GNSS_RTK_SERIAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GNSS_RTK_SERIAL)、[`CONFIG_SHELL_BACKEND_SERIAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_BACKEND_SERIAL)、[`CONFIG_MPIPE_PLAYER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MPIPE_PLAYER)、[`CONFIG_SHIELD_OPENTHREAD_RCP_ARDUINO_SERIAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHIELD_OPENTHREAD_RCP_ARDUINO_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_UART`、`CONFIG_SHIELD_OPENTHREAD_RCP_ARDUINO_SERIAL`。

<a id="CONFIG_SERIAL_ESP32_USB"></a>

## 165.4 `CONFIG_SERIAL_ESP32_USB`

**提示（Prompt）**：ESP32 内置 USB 串行驱动

**说明（Help）**

启用部分 Espressif 微控制器（MCU，如 ESP32-Cx）内置的 USB 串行接口。此驱动使用名为 USB Serial/JTAG Controller（`USB_SERIAL_JTAG`）的外设，该外设向 USB 主机呈现为 CDC-ACM 接口。USB 协议栈内置于芯片中，固件通过简化的 API 访问它，方式类似于普通 UART 外设。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ESPRESSIF_ESP32_USB_SERIAL_ENABLED && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SERIAL_HAS_DRIVER
CONFIG_SERIAL_SUPPORT_INTERRUPT
```

**定义位置（Location）**：[`drivers/serial/Kconfig.esp32:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.esp32#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SERIAL_HAS_DRIVER`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_HAS_DRIVER)、[`CONFIG_SERIAL_SUPPORT_INTERRUPT`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_SUPPORT_INTERRUPT)。

<a id="CONFIG_SERIAL_HAS_DRIVER"></a>

## 165.5 `CONFIG_SERIAL_HAS_DRIVER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

由各个串行驱动启用此选项，以表明存在串行驱动。其他依赖串行功能的驱动使用此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SERIAL
```

**被选择（Selected by）**

```text
CONFIG_UART_AESC
CONFIG_UART_ALTERA
CONFIG_UART_ALTERA_JTAG
CONFIG_UART_AMBIQ
CONFIG_UART_AMEBA_LOGUART
CONFIG_UART_APBUART
CONFIG_UART_TELINK_B91
CONFIG_UART_BEE
CONFIG_UART_BFLB
CONFIG_UART_BITBANG
CONFIG_UART_CC13XX_CC26XX
CONFIG_UART_CC23X0
CONFIG_UART_CC32XX
CONFIG_UART_CDNS
CONFIG_UART_CMSDK_APB
CONFIG_UART_EFINIX_SAPPIHIRE
CONFIG_UART_EM32
CONFIG_UART_EMUL
CONFIG_UART_ENE_KB1200
CONFIG_UART_ENE_KB106X
CONFIG_UART_ESP32
CONFIG_SERIAL_ESP32_USB
CONFIG_LPUART_ESP32
CONFIG_UART_FOCALTECH
CONFIG_USART_GD32
CONFIG_UART_GECKO
CONFIG_UART_HOSTLINK
CONFIG_UART_IMX
CONFIG_UART_INFINEON_CAT1_HAL
CONFIG_UART_INFINEON_CAT1_PDL
CONFIG_UART_ASCLIN
CONFIG_UART_INTEL_LW
CONFIG_LEUART_GECKO
CONFIG_UART_LITEX
CONFIG_UART_LPC11U6X
CONFIG_UART_LPC84X
CONFIG_UART_MAX32
CONFIG_UART_MCHP_SERCOM_G1
CONFIG_UART_MCHP_DBGU_G1
CONFIG_UART_MCHP_UART_G1
CONFIG_UART_MCUX
CONFIG_UART_MCUX_FLEXCOMM
CONFIG_UART_MCUX_IUART
CONFIG_UART_MCUX_LPSCI
CONFIG_UART_MCUX_LPUART
CONFIG_UART_MIV
CONFIG_UART_MSP432P4XX
CONFIG_UART_MSPM0
CONFIG_UART_MT8188
CONFIG_UART_NATIVE_PTY
CONFIG_UART_NATIVE_TTY
CONFIG_UART_NEORV32
CONFIG_UART_NPCX
CONFIG_UART_NRFX
CONFIG_UART_NS16550
CONFIG_UART_NUMAKER
CONFIG_UART_NUMICRO
CONFIG_UART_NXP_S32_LINFLEXD
CONFIG_UART_OPENTITAN
CONFIG_UART_PL011
CONFIG_UART_PSOC6
CONFIG_UART_QUICKLOGIC_USBSERIALPORT_S3B
CONFIG_UART_RCAR
CONFIG_UART_SCI_RA
CONFIG_UART_RENESAS_RA_SAU
CONFIG_UART_RA8_SCI_B
CONFIG_UART_RENESAS_RX
CONFIG_UART_RENESAS_RX_SCI_B
CONFIG_UART_RENESAS_RX_QEMU
CONFIG_UART_RENESAS_RZ_SCIF
CONFIG_UART_RENESAS_RZ_SCI
CONFIG_UART_RENESAS_RZ_SCI_B
CONFIG_UART_RENESAS_RZA2M_SCIF
CONFIG_UART_RPI_PICO_PIO
CONFIG_UART_RTT_0
CONFIG_UART_RTT_1
CONFIG_UART_RTT_2
CONFIG_UART_RTT_3
CONFIG_UART_RV32M1_LPUART
CONFIG_UART_RZT2M
CONFIG_UART_SAM0
CONFIG_UART_SEDI
CONFIG_UART_SF32LB
CONFIG_UART_SHAKTI
CONFIG_UART_SI32_USART
CONFIG_UART_SIFIVE
CONFIG_UART_SILABS_EUSART
CONFIG_UART_SILABS_USART
CONFIG_UART_SMARTBOND
CONFIG_UART_STELLARIS
CONFIG_UART_STM32
CONFIG_UART_SY1XX
CONFIG_SERIAL_TEST
CONFIG_UART_TIVA_C
CONFIG_UART_SAM
CONFIG_USART_SAM
CONFIG_UART_WCH_CH5XX
CONFIG_UART_WCH_USART
CONFIG_UART_XEC
CONFIG_UART_XEN_HVC
CONFIG_UART_XEN_HVC_CONSOLEIO
CONFIG_UART_XLNX_PS
CONFIG_UART_XLNX_UARTLITE
CONFIG_UART_XMC4XXX
CONFIG_USB_CDC_ACM
CONFIG_USBD_CDC_ACM_CLASS
```

**定义位置（Location）**：[`drivers/serial/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_UART_AESC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_AESC)、[`CONFIG_UART_ALTERA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ALTERA)、[`CONFIG_UART_ALTERA_JTAG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ALTERA_JTAG)、[`CONFIG_UART_AMBIQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_AMBIQ)、[`CONFIG_UART_AMEBA_LOGUART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_AMEBA_LOGUART)、[`CONFIG_UART_APBUART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_APBUART)、[`CONFIG_UART_TELINK_B91`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_TELINK_B91)、[`CONFIG_UART_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_BEE)、[`CONFIG_UART_BFLB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_BFLB)、[`CONFIG_UART_BITBANG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_BITBANG)、[`CONFIG_UART_CC13XX_CC26XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_CC13XX_CC26XX)、[`CONFIG_UART_CC23X0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_CC23X0)、[`CONFIG_UART_CC32XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_CC32XX)、[`CONFIG_UART_CDNS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_CDNS)、[`CONFIG_UART_CMSDK_APB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_CMSDK_APB)、[`CONFIG_UART_EFINIX_SAPPIHIRE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_EFINIX_SAPPIHIRE)、[`CONFIG_UART_EM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_EM32)、[`CONFIG_UART_EMUL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_EMUL)、[`CONFIG_UART_ENE_KB1200`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ENE_KB1200)、[`CONFIG_UART_ENE_KB106X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ENE_KB106X)、[`CONFIG_UART_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ESP32)、[`CONFIG_SERIAL_ESP32_USB`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_ESP32_USB)、[`CONFIG_LPUART_ESP32`](P165_drivers_serial_配置项参考_1.md#CONFIG_LPUART_ESP32)、[`CONFIG_UART_FOCALTECH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_FOCALTECH)、[`CONFIG_USART_GD32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USART_GD32)、[`CONFIG_UART_GECKO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_GECKO)、[`CONFIG_UART_HOSTLINK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_HOSTLINK)、[`CONFIG_UART_IMX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_IMX)、[`CONFIG_UART_INFINEON_CAT1_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_INFINEON_CAT1_HAL)、[`CONFIG_UART_INFINEON_CAT1_PDL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_INFINEON_CAT1_PDL)、[`CONFIG_UART_ASCLIN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASCLIN)、[`CONFIG_UART_INTEL_LW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_INTEL_LW)、[`CONFIG_LEUART_GECKO`](P165_drivers_serial_配置项参考_1.md#CONFIG_LEUART_GECKO)、[`CONFIG_UART_LITEX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_LITEX)、[`CONFIG_UART_LPC11U6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_LPC11U6X)、[`CONFIG_UART_LPC84X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_LPC84X)、[`CONFIG_UART_MAX32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_MAX32)、[`CONFIG_UART_MCHP_SERCOM_G1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_MCHP_SERCOM_G1)、[`CONFIG_UART_MCHP_DBGU_G1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_MCHP_DBGU_G1)、[`CONFIG_UART_MCHP_UART_G1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_MCHP_UART_G1)、[`CONFIG_UART_MCUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_MCUX)、[`CONFIG_UART_MCUX_FLEXCOMM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_MCUX_FLEXCOMM)、[`CONFIG_UART_MCUX_IUART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_MCUX_IUART)、[`CONFIG_UART_MCUX_LPSCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_MCUX_LPSCI)、[`CONFIG_UART_MCUX_LPUART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_MCUX_LPUART)、[`CONFIG_UART_MIV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_MIV)、[`CONFIG_UART_MSP432P4XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_MSP432P4XX)、[`CONFIG_UART_MSPM0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_MSPM0)、[`CONFIG_UART_MT8188`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_MT8188)、[`CONFIG_UART_NATIVE_PTY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NATIVE_PTY)、[`CONFIG_UART_NATIVE_TTY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NATIVE_TTY)、[`CONFIG_UART_NEORV32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NEORV32)、[`CONFIG_UART_NPCX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NPCX)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_UART_NS16550`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NS16550)、[`CONFIG_UART_NUMAKER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NUMAKER)、[`CONFIG_UART_NUMICRO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NUMICRO)、[`CONFIG_UART_NXP_S32_LINFLEXD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NXP_S32_LINFLEXD)、[`CONFIG_UART_OPENTITAN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_OPENTITAN)、[`CONFIG_UART_PL011`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_PL011)、[`CONFIG_UART_PSOC6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_PSOC6)、[`CONFIG_UART_QUICKLOGIC_USBSERIALPORT_S3B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_QUICKLOGIC_USBSERIALPORT_S3B)、[`CONFIG_UART_RCAR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_RCAR)、[`CONFIG_UART_SCI_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_SCI_RA)、[`CONFIG_UART_RENESAS_RA_SAU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_RENESAS_RA_SAU)、[`CONFIG_UART_RA8_SCI_B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_RA8_SCI_B)、[`CONFIG_UART_RENESAS_RX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_RENESAS_RX)、[`CONFIG_UART_RENESAS_RX_SCI_B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_RENESAS_RX_SCI_B)、[`CONFIG_UART_RENESAS_RX_QEMU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_RENESAS_RX_QEMU)、[`CONFIG_UART_RENESAS_RZ_SCIF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_RENESAS_RZ_SCIF)、[`CONFIG_UART_RENESAS_RZ_SCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_RENESAS_RZ_SCI)、[`CONFIG_UART_RENESAS_RZ_SCI_B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_RENESAS_RZ_SCI_B)、[`CONFIG_UART_RENESAS_RZA2M_SCIF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_RENESAS_RZA2M_SCIF)、[`CONFIG_UART_RPI_PICO_PIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_RPI_PICO_PIO)、[`CONFIG_UART_RTT_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_RTT_0)、[`CONFIG_UART_RTT_1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_RTT_1)、[`CONFIG_UART_RTT_2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_RTT_2)、[`CONFIG_UART_RTT_3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_RTT_3)、[`CONFIG_UART_RV32M1_LPUART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_RV32M1_LPUART)、[`CONFIG_UART_RZT2M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_RZT2M)、[`CONFIG_UART_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_SAM0)、[`CONFIG_UART_SEDI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_SEDI)、[`CONFIG_UART_SF32LB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_SF32LB)、[`CONFIG_UART_SHAKTI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_SHAKTI)、[`CONFIG_UART_SI32_USART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_SI32_USART)、[`CONFIG_UART_SIFIVE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_SIFIVE)、[`CONFIG_UART_SILABS_EUSART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_SILABS_EUSART)、[`CONFIG_UART_SILABS_USART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_SILABS_USART)、[`CONFIG_UART_SMARTBOND`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_SMARTBOND)、[`CONFIG_UART_STELLARIS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_STELLARIS)、[`CONFIG_UART_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_STM32)、[`CONFIG_UART_SY1XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_SY1XX)、[`CONFIG_SERIAL_TEST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SERIAL_TEST)、[`CONFIG_UART_TIVA_C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_TIVA_C)、[`CONFIG_UART_SAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_SAM)、[`CONFIG_USART_SAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USART_SAM)、[`CONFIG_UART_WCH_CH5XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_WCH_CH5XX)、[`CONFIG_UART_WCH_USART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_WCH_USART)、[`CONFIG_UART_XEC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_XEC)、[`CONFIG_UART_XEN_HVC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_XEN_HVC)、[`CONFIG_UART_XEN_HVC_CONSOLEIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_XEN_HVC_CONSOLEIO)、[`CONFIG_UART_XLNX_PS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_XLNX_PS)、[`CONFIG_UART_XLNX_UARTLITE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_XLNX_UARTLITE)、[`CONFIG_UART_XMC4XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_XMC4XXX)、[`CONFIG_USB_CDC_ACM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_CDC_ACM)、[`CONFIG_USBD_CDC_ACM_CLASS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBD_CDC_ACM_CLASS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SERIAL_TEST`。

<a id="CONFIG_SERIAL_HAS_POST_KERNEL_INIT"></a>

## 165.6 `CONFIG_SERIAL_HAS_POST_KERNEL_INIT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

在 `POST_KERNEL` 阶段而非 `PRE_KERNEL` 阶段初始化的串行驱动选择此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SERIAL
```

**被选择（Selected by）**

```text
CONFIG_UART_BITBANG
CONFIG_UART_NATIVE_TTY
CONFIG_UART_RPI_PICO_PIO
CONFIG_UART_RPMSG
CONFIG_UART_VIRTIO_CONSOLE
```

**定义位置（Location）**：[`drivers/serial/Kconfig:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_UART_BITBANG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_BITBANG)、[`CONFIG_UART_NATIVE_TTY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NATIVE_TTY)、[`CONFIG_UART_RPI_PICO_PIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_RPI_PICO_PIO)、[`CONFIG_UART_RPMSG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_RPMSG)、[`CONFIG_UART_VIRTIO_CONSOLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_VIRTIO_CONSOLE)。

<a id="CONFIG_SERIAL_INIT_PRIORITY"></a>

## 165.7 `CONFIG_SERIAL_INIT_PRIORITY`

**提示（Prompt）**：串行驱动初始化优先级（Serial Init Priority）

**说明（Help）**

串行驱动设备的初始化优先级（Device Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SERIAL
```

**默认值（Defaults）**

```text
CONFIG_KERNEL_INIT_PRIORITY_DEVICE
```

**定义位置（Location）**：[`drivers/serial/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_KERNEL_INIT_PRIORITY_DEVICE`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_INIT_PRIORITY_DEVICE)。

<a id="CONFIG_SERIAL_SUPPORT_ASYNC"></a>

## 165.8 `CONFIG_SERIAL_SUPPORT_ASYNC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

由各个串行驱动启用此选项，以表明驱动和硬件支持异步操作（Asynchronous Operation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SERIAL
```

**被选择（Selected by）**

```text
CONFIG_SOC_SR100
CONFIG_UART_AMBIQ
CONFIG_UART_BEE
CONFIG_UART_CC23X0
CONFIG_UART_EMUL
CONFIG_UART_ESP32
CONFIG_UART_INFINEON_CAT1_HAL
CONFIG_UART_INFINEON_CAT1_PDL
CONFIG_UART_MAX32
CONFIG_UART_MCHP_SERCOM_G1
CONFIG_UART_MCUX_FLEXCOMM
CONFIG_UART_NXP_LPUART_ASYNC_API_SUPPORT
CONFIG_UART_NATIVE_PTY
CONFIG_UART_NPCX_USE_MDMA
CONFIG_UART_NRFX
CONFIG_UART_NS16550_INTEL_LPSS_DMA
CONFIG_UART_SCI_RA
CONFIG_UART_RA8_SCI_B
CONFIG_UART_RENESAS_RX
CONFIG_UART_RTT
CONFIG_UART_SAM0
CONFIG_UART_SF32LB
CONFIG_UART_SILABS_EUSART
CONFIG_UART_SILABS_USART
CONFIG_UART_STM32
CONFIG_SERIAL_TEST
CONFIG_UART_XMC4XXX
```

**定义位置（Location）**：[`drivers/serial/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_SOC_SR100`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SR100)、[`CONFIG_UART_AMBIQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_AMBIQ)、[`CONFIG_UART_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_BEE)、[`CONFIG_UART_CC23X0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_CC23X0)、[`CONFIG_UART_EMUL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_EMUL)、[`CONFIG_UART_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ESP32)、[`CONFIG_UART_INFINEON_CAT1_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_INFINEON_CAT1_HAL)、[`CONFIG_UART_INFINEON_CAT1_PDL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_INFINEON_CAT1_PDL)、[`CONFIG_UART_MAX32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_MAX32)、[`CONFIG_UART_MCHP_SERCOM_G1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_MCHP_SERCOM_G1)、[`CONFIG_UART_MCUX_FLEXCOMM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_MCUX_FLEXCOMM)、[`CONFIG_UART_NXP_LPUART_ASYNC_API_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NXP_LPUART_ASYNC_API_SUPPORT)、[`CONFIG_UART_NATIVE_PTY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NATIVE_PTY)、[`CONFIG_UART_NPCX_USE_MDMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NPCX_USE_MDMA)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_UART_NS16550_INTEL_LPSS_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NS16550_INTEL_LPSS_DMA)、[`CONFIG_UART_SCI_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_SCI_RA)、[`CONFIG_UART_RA8_SCI_B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_RA8_SCI_B)、[`CONFIG_UART_RENESAS_RX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_RENESAS_RX)、[`CONFIG_UART_RTT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_RTT)、[`CONFIG_UART_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_SAM0)、[`CONFIG_UART_SF32LB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_SF32LB)、[`CONFIG_UART_SILABS_EUSART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_SILABS_EUSART)、[`CONFIG_UART_SILABS_USART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_SILABS_USART)、[`CONFIG_UART_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_STM32)、[`CONFIG_SERIAL_TEST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SERIAL_TEST)、[`CONFIG_UART_XMC4XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_XMC4XXX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SR100`、`CONFIG_SERIAL_TEST`。

<a id="CONFIG_SERIAL_SUPPORT_INTERRUPT"></a>

## 165.9 `CONFIG_SERIAL_SUPPORT_INTERRUPT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

由各个串行驱动启用此选项，以表明驱动和硬件支持中断（Interrupt）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SERIAL
```

**被选择（Selected by）**

```text
CONFIG_UART_AESC
CONFIG_UART_ALTERA
CONFIG_UART_ALTERA_JTAG_SUPPORT_INTERRUPT
CONFIG_UART_AMBIQ
CONFIG_UART_APBUART
CONFIG_UART_TELINK_B91
CONFIG_UART_BEE
CONFIG_UART_BFLB
CONFIG_UART_BITBANG
CONFIG_UART_BT
CONFIG_UART_CC13XX_CC26XX
CONFIG_UART_CC23X0
CONFIG_UART_CC32XX
CONFIG_UART_CDNS
CONFIG_UART_CMSDK_APB
CONFIG_UART_EMUL
CONFIG_UART_ENE_KB1200
CONFIG_UART_ENE_KB106X
CONFIG_UART_ESP32
CONFIG_SERIAL_ESP32_USB
CONFIG_UART_FOCALTECH
CONFIG_USART_GD32
CONFIG_UART_GECKO
CONFIG_UART_IMX
CONFIG_UART_INFINEON_CAT1_HAL
CONFIG_UART_INFINEON_CAT1_PDL
CONFIG_UART_INTEL_LW
CONFIG_LEUART_GECKO
CONFIG_UART_LITEX
CONFIG_UART_LPC11U6X
CONFIG_UART_LPC84X
CONFIG_UART_MAX32
CONFIG_UART_MCHP_SERCOM_G1
CONFIG_UART_MCHP_UART_G1
CONFIG_UART_MCUX
CONFIG_UART_MCUX_FLEXCOMM
CONFIG_UART_MCUX_IUART
CONFIG_UART_MCUX_LPSCI
CONFIG_UART_MCUX_LPUART
CONFIG_UART_MSP432P4XX
CONFIG_UART_MSPM0
CONFIG_UART_MT8188
CONFIG_UART_NATIVE_PTY
CONFIG_UART_NATIVE_TTY
CONFIG_UART_NEORV32
CONFIG_UART_NPCX
CONFIG_UART_NRFX
CONFIG_UART_NUMAKER
CONFIG_UART_NUMICRO
CONFIG_UART_NXP_S32_LINFLEXD
CONFIG_UART_PL011
CONFIG_UART_PSOC6
CONFIG_UART_RCAR
CONFIG_UART_SCI_RA
CONFIG_UART_RENESAS_RA_SAU
CONFIG_UART_RA8_SCI_B
CONFIG_UART_RENESAS_RX
CONFIG_UART_RENESAS_RZ_SCIF
CONFIG_UART_RENESAS_RZ_SCI
CONFIG_UART_RENESAS_RZ_SCI_B
CONFIG_UART_RENESAS_RZA2M_SCIF
CONFIG_UART_RV32M1_LPUART
CONFIG_UART_RZT2M
CONFIG_UART_SAM0
CONFIG_UART_SEDI
CONFIG_UART_SF32LB
CONFIG_UART_SHAKTI
CONFIG_UART_SI32_USART
CONFIG_UART_SIFIVE
CONFIG_UART_SILABS_EUSART
CONFIG_UART_SILABS_USART
CONFIG_UART_SMARTBOND
CONFIG_UART_STELLARIS
CONFIG_UART_STM32
CONFIG_SERIAL_TEST
CONFIG_UART_SAM
CONFIG_USART_SAM
CONFIG_UART_WCH_CH5XX
CONFIG_UART_WCH_USART
CONFIG_UART_XEC
CONFIG_UART_XEN_HVC
CONFIG_UART_XLNX_PS
CONFIG_UART_XLNX_UARTLITE
CONFIG_UART_XMC4XXX
CONFIG_USB_CDC_ACM
CONFIG_USBD_CDC_ACM_CLASS
```

**被弱选择（Implied by）**

```text
CONFIG_OSDP
```

**定义位置（Location）**：[`drivers/serial/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_UART_AESC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_AESC)、[`CONFIG_UART_ALTERA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ALTERA)、[`CONFIG_UART_ALTERA_JTAG_SUPPORT_INTERRUPT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ALTERA_JTAG_SUPPORT_INTERRUPT)、[`CONFIG_UART_AMBIQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_AMBIQ)、[`CONFIG_UART_APBUART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_APBUART)、[`CONFIG_UART_TELINK_B91`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_TELINK_B91)、[`CONFIG_UART_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_BEE)、[`CONFIG_UART_BFLB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_BFLB)、[`CONFIG_UART_BITBANG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_BITBANG)、[`CONFIG_UART_BT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_BT)、[`CONFIG_UART_CC13XX_CC26XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_CC13XX_CC26XX)、[`CONFIG_UART_CC23X0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_CC23X0)、[`CONFIG_UART_CC32XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_CC32XX)、[`CONFIG_UART_CDNS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_CDNS)、[`CONFIG_UART_CMSDK_APB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_CMSDK_APB)、[`CONFIG_UART_EMUL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_EMUL)、[`CONFIG_UART_ENE_KB1200`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ENE_KB1200)、[`CONFIG_UART_ENE_KB106X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ENE_KB106X)、[`CONFIG_UART_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ESP32)、[`CONFIG_SERIAL_ESP32_USB`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL_ESP32_USB)、[`CONFIG_UART_FOCALTECH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_FOCALTECH)、[`CONFIG_USART_GD32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USART_GD32)、[`CONFIG_UART_GECKO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_GECKO)、[`CONFIG_UART_IMX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_IMX)、[`CONFIG_UART_INFINEON_CAT1_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_INFINEON_CAT1_HAL)、[`CONFIG_UART_INFINEON_CAT1_PDL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_INFINEON_CAT1_PDL)、[`CONFIG_UART_INTEL_LW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_INTEL_LW)、[`CONFIG_LEUART_GECKO`](P165_drivers_serial_配置项参考_1.md#CONFIG_LEUART_GECKO)、[`CONFIG_UART_LITEX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_LITEX)、[`CONFIG_UART_LPC11U6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_LPC11U6X)、[`CONFIG_UART_LPC84X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_LPC84X)、[`CONFIG_UART_MAX32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_MAX32)、[`CONFIG_UART_MCHP_SERCOM_G1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_MCHP_SERCOM_G1)、[`CONFIG_UART_MCHP_UART_G1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_MCHP_UART_G1)、[`CONFIG_UART_MCUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_MCUX)、[`CONFIG_UART_MCUX_FLEXCOMM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_MCUX_FLEXCOMM)、[`CONFIG_UART_MCUX_IUART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_MCUX_IUART)、[`CONFIG_UART_MCUX_LPSCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_MCUX_LPSCI)、[`CONFIG_UART_MCUX_LPUART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_MCUX_LPUART)、[`CONFIG_UART_MSP432P4XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_MSP432P4XX)、[`CONFIG_UART_MSPM0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_MSPM0)、[`CONFIG_UART_MT8188`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_MT8188)、[`CONFIG_UART_NATIVE_PTY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NATIVE_PTY)、[`CONFIG_UART_NATIVE_TTY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NATIVE_TTY)、[`CONFIG_UART_NEORV32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NEORV32)、[`CONFIG_UART_NPCX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NPCX)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_UART_NUMAKER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NUMAKER)、[`CONFIG_UART_NUMICRO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NUMICRO)、[`CONFIG_UART_NXP_S32_LINFLEXD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NXP_S32_LINFLEXD)、[`CONFIG_UART_PL011`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_PL011)、[`CONFIG_UART_PSOC6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_PSOC6)、[`CONFIG_UART_RCAR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_RCAR)、[`CONFIG_UART_SCI_RA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_SCI_RA)、[`CONFIG_UART_RENESAS_RA_SAU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_RENESAS_RA_SAU)、[`CONFIG_UART_RA8_SCI_B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_RA8_SCI_B)、[`CONFIG_UART_RENESAS_RX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_RENESAS_RX)、[`CONFIG_UART_RENESAS_RZ_SCIF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_RENESAS_RZ_SCIF)、[`CONFIG_UART_RENESAS_RZ_SCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_RENESAS_RZ_SCI)、[`CONFIG_UART_RENESAS_RZ_SCI_B`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_RENESAS_RZ_SCI_B)、[`CONFIG_UART_RENESAS_RZA2M_SCIF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_RENESAS_RZA2M_SCIF)、[`CONFIG_UART_RV32M1_LPUART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_RV32M1_LPUART)、[`CONFIG_UART_RZT2M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_RZT2M)、[`CONFIG_UART_SAM0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_SAM0)、[`CONFIG_UART_SEDI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_SEDI)、[`CONFIG_UART_SF32LB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_SF32LB)、[`CONFIG_UART_SHAKTI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_SHAKTI)、[`CONFIG_UART_SI32_USART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_SI32_USART)、[`CONFIG_UART_SIFIVE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_SIFIVE)、[`CONFIG_UART_SILABS_EUSART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_SILABS_EUSART)、[`CONFIG_UART_SILABS_USART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_SILABS_USART)、[`CONFIG_UART_SMARTBOND`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_SMARTBOND)、[`CONFIG_UART_STELLARIS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_STELLARIS)、[`CONFIG_UART_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_STM32)、[`CONFIG_SERIAL_TEST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SERIAL_TEST)、[`CONFIG_UART_SAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_SAM)、[`CONFIG_USART_SAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USART_SAM)、[`CONFIG_UART_WCH_CH5XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_WCH_CH5XX)、[`CONFIG_UART_WCH_USART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_WCH_USART)、[`CONFIG_UART_XEC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_XEC)、[`CONFIG_UART_XEN_HVC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_XEN_HVC)、[`CONFIG_UART_XLNX_PS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_XLNX_PS)、[`CONFIG_UART_XLNX_UARTLITE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_XLNX_UARTLITE)、[`CONFIG_UART_XMC4XXX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_XMC4XXX)、[`CONFIG_USB_CDC_ACM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_CDC_ACM)、[`CONFIG_USBD_CDC_ACM_CLASS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBD_CDC_ACM_CLASS)、[`CONFIG_OSDP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OSDP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SERIAL_TEST`。

<a id="CONFIG_SERIAL_SUPPORT_WIDE_DATA"></a>

## 165.10 `CONFIG_SERIAL_SUPPORT_WIDE_DATA`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

由各个串行驱动启用此选项，以表明驱动和硬件支持超过 8 位的数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

<a id="CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER"></a>

## 165.11 `CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER`

**提示（Prompt）**：使用定时器（TIMER）统计接收（RX）字节数

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_NRFX_GPPI
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_NRFX_GPPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_GPPI)。

<a id="CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY"></a>

## 165.12 `CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY`

**提示（Prompt）**：在旧平台上使用定时器（TIMER）统计接收（RX）字节数

**说明（Help）**

nRF52x、nRF53x 和 nRF91x 系列使用的方法。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && !n && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**主动选择（Selects）**

```text
CONFIG_NRFX_GPPI
```

**被弱选择（Implied by）**

```text
CONFIG_UART_0_COUNT_BYTES_WITH_TIMER_LEGACY
CONFIG_UART_1_COUNT_BYTES_WITH_TIMER_LEGACY
CONFIG_UART_2_COUNT_BYTES_WITH_TIMER_LEGACY
CONFIG_UART_3_COUNT_BYTES_WITH_TIMER_LEGACY
CONFIG_UART_00_COUNT_BYTES_WITH_TIMER_LEGACY
CONFIG_UART_20_COUNT_BYTES_WITH_TIMER_LEGACY
CONFIG_UART_21_COUNT_BYTES_WITH_TIMER_LEGACY
CONFIG_UART_22_COUNT_BYTES_WITH_TIMER_LEGACY
CONFIG_UART_23_COUNT_BYTES_WITH_TIMER_LEGACY
CONFIG_UART_24_COUNT_BYTES_WITH_TIMER_LEGACY
CONFIG_UART_30_COUNT_BYTES_WITH_TIMER_LEGACY
CONFIG_UART_120_COUNT_BYTES_WITH_TIMER_LEGACY
CONFIG_UART_130_COUNT_BYTES_WITH_TIMER_LEGACY
CONFIG_UART_131_COUNT_BYTES_WITH_TIMER_LEGACY
CONFIG_UART_132_COUNT_BYTES_WITH_TIMER_LEGACY
CONFIG_UART_133_COUNT_BYTES_WITH_TIMER_LEGACY
CONFIG_UART_134_COUNT_BYTES_WITH_TIMER_LEGACY
CONFIG_UART_135_COUNT_BYTES_WITH_TIMER_LEGACY
CONFIG_UART_136_COUNT_BYTES_WITH_TIMER_LEGACY
CONFIG_UART_137_COUNT_BYTES_WITH_TIMER_LEGACY
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx:81`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx#L81)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_NRFX_GPPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_GPPI)、[`CONFIG_UART_0_COUNT_BYTES_WITH_TIMER_LEGACY`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_0_COUNT_BYTES_WITH_TIMER_LEGACY)、[`CONFIG_UART_1_COUNT_BYTES_WITH_TIMER_LEGACY`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_1_COUNT_BYTES_WITH_TIMER_LEGACY)、[`CONFIG_UART_2_COUNT_BYTES_WITH_TIMER_LEGACY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_2_COUNT_BYTES_WITH_TIMER_LEGACY)、[`CONFIG_UART_3_COUNT_BYTES_WITH_TIMER_LEGACY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_3_COUNT_BYTES_WITH_TIMER_LEGACY)、[`CONFIG_UART_00_COUNT_BYTES_WITH_TIMER_LEGACY`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_00_COUNT_BYTES_WITH_TIMER_LEGACY)、[`CONFIG_UART_20_COUNT_BYTES_WITH_TIMER_LEGACY`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_20_COUNT_BYTES_WITH_TIMER_LEGACY)、[`CONFIG_UART_21_COUNT_BYTES_WITH_TIMER_LEGACY`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_21_COUNT_BYTES_WITH_TIMER_LEGACY)、[`CONFIG_UART_22_COUNT_BYTES_WITH_TIMER_LEGACY`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_22_COUNT_BYTES_WITH_TIMER_LEGACY)、[`CONFIG_UART_23_COUNT_BYTES_WITH_TIMER_LEGACY`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_23_COUNT_BYTES_WITH_TIMER_LEGACY)、[`CONFIG_UART_24_COUNT_BYTES_WITH_TIMER_LEGACY`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_24_COUNT_BYTES_WITH_TIMER_LEGACY)、[`CONFIG_UART_30_COUNT_BYTES_WITH_TIMER_LEGACY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_30_COUNT_BYTES_WITH_TIMER_LEGACY)、[`CONFIG_UART_120_COUNT_BYTES_WITH_TIMER_LEGACY`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_120_COUNT_BYTES_WITH_TIMER_LEGACY)、[`CONFIG_UART_130_COUNT_BYTES_WITH_TIMER_LEGACY`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_130_COUNT_BYTES_WITH_TIMER_LEGACY)、[`CONFIG_UART_131_COUNT_BYTES_WITH_TIMER_LEGACY`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_131_COUNT_BYTES_WITH_TIMER_LEGACY)、[`CONFIG_UART_132_COUNT_BYTES_WITH_TIMER_LEGACY`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_132_COUNT_BYTES_WITH_TIMER_LEGACY)、[`CONFIG_UART_133_COUNT_BYTES_WITH_TIMER_LEGACY`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_133_COUNT_BYTES_WITH_TIMER_LEGACY)、[`CONFIG_UART_134_COUNT_BYTES_WITH_TIMER_LEGACY`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_134_COUNT_BYTES_WITH_TIMER_LEGACY)、[`CONFIG_UART_135_COUNT_BYTES_WITH_TIMER_LEGACY`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_135_COUNT_BYTES_WITH_TIMER_LEGACY)、[`CONFIG_UART_136_COUNT_BYTES_WITH_TIMER_LEGACY`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_136_COUNT_BYTES_WITH_TIMER_LEGACY)、[`CONFIG_UART_137_COUNT_BYTES_WITH_TIMER_LEGACY`](P166_drivers_serial_配置项参考_2.md#CONFIG_UART_137_COUNT_BYTES_WITH_TIMER_LEGACY)。

<a id="CONFIG_UART_00_ASYNC"></a>

## 165.13 `CONFIG_UART_00_ASYNC`

**提示（Prompt）**：端口 00 的异步 API（Asynchronous API）支持

**说明（Help）**

此选项启用端口 `$(nrfx_uart_num)` 的 UART 异步 API（Asynchronous API）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && !CONFIG_UART_00_INTERRUPT_DRIVEN && CONFIG_HAS_HW_NRF_UARTE00 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_UART_00_INTERRUPT_DRIVEN`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_00_INTERRUPT_DRIVEN)、[`CONFIG_HAS_HW_NRF_UARTE00`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE00)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE00`。

<a id="CONFIG_UART_00_COUNT_BYTES_WITH_TIMER"></a>

## 165.14 `CONFIG_UART_00_COUNT_BYTES_WITH_TIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了一个用于接收（RX）字节计数的 TIMER 外设。适用于 nRF54x 系列等较新目标平台使用的 UARTE 修订版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER`](P165_drivers_serial_配置项参考_1.md#CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER)。

<a id="CONFIG_UART_00_COUNT_BYTES_WITH_TIMER_LEGACY"></a>

## 165.15 `CONFIG_UART_00_COUNT_BYTES_WITH_TIMER_LEGACY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了一个用于接收（RX）字节计数的 TIMER 外设。适用于旧目标平台 nRF52x、nRF53x 和 nRF91x 使用的 UARTE 修订版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_UART_00_NRF_USE_TIMER || CONFIG_UART_00_NRF_HW_ASYNC) && !n && CONFIG_HAS_HW_NRF_UARTE00 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_00_NRF_USE_TIMER`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_00_NRF_USE_TIMER)、[`CONFIG_UART_00_NRF_HW_ASYNC`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_00_NRF_HW_ASYNC)、[`CONFIG_HAS_HW_NRF_UARTE00`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE00)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY`](P165_drivers_serial_配置项参考_1.md#CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE00`。

<a id="CONFIG_UART_00_ENHANCED_POLL_OUT"></a>

## 165.16 `CONFIG_UART_00_ENHANCED_POLL_OUT`

**提示（Prompt）**：端口 00 的高效轮询输出（Efficient Poll Out）

**说明（Help）**

启用时，轮询输出（Polling Out）不会触发用于停止发送（TX）的中断。此功能使用一个可编程外设互连（PPI）通道。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!n && CONFIG_HAS_HW_NRF_UARTE00 && (CONFIG_HAS_HW_NRF_PPI || CONFIG_HAS_HW_NRF_DPPIC) && CONFIG_HAS_HW_NRF_UARTE00 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NRFX_GPPI
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE00`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE00)、[`CONFIG_HAS_HW_NRF_PPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_PPI)、[`CONFIG_HAS_HW_NRF_DPPIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_DPPIC)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_NRFX_GPPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_GPPI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE00`、`CONFIG_HAS_HW_NRF_PPI`、`CONFIG_HAS_HW_NRF_DPPIC`。

<a id="CONFIG_UART_00_INTERRUPT_DRIVEN"></a>

## 165.17 `CONFIG_UART_00_INTERRUPT_DRIVEN`

**提示（Prompt）**：端口 00 的中断支持（Interrupt Support）

**说明（Help）**

此选项启用端口 `$(nrfx_uart_num)` 的 UART 中断支持（Interrupt Support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_INTERRUPT_DRIVEN && CONFIG_HAS_HW_NRF_UARTE00 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_INTERRUPT_DRIVEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_HAS_HW_NRF_UARTE00`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE00)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE00`。

<a id="CONFIG_UART_00_NRF_ASYNC_LOW_POWER"></a>

## 165.18 `CONFIG_UART_00_NRF_ASYNC_LOW_POWER`

**提示（Prompt）**：低功耗模式（Low Power Mode）

**说明（Help）**

启用时，每次发送（TX）或接收（RX）前都会启用 UARTE，不使用时则禁用。在空闲时禁用 UARTE 可以实现最低功耗，但仅在接收器不需要始终开启时可行。启用设备电源管理（PM）时，此选项不起作用，因为设备状态改由 PM 操作控制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE00 && CONFIG_UART_ASYNC_API && CONFIG_HAS_HW_NRF_UARTE00 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y if !CONFIG_PM_DEVICE
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE00`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE00)、[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_PM_DEVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE00`。

<a id="CONFIG_UART_00_NRF_HW_ASYNC"></a>

## 165.19 `CONFIG_UART_00_NRF_HW_ASYNC`

**提示（Prompt）**：使用硬件接收字节计数（Hardware RX Byte Counting）［已弃用，DEPRECATED］

**说明（Help）**

此选项已弃用。请使用设备树（Device Tree）的 `timer` 属性分配 TIMER 外设，以在不使用硬件流控制（HWFC）时实现可靠接收。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && CONFIG_HAS_HW_NRF_UARTE00 && !n && CONFIG_HAS_HW_NRF_UARTE00 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_HAS_HW_NRF_UARTE00`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE00)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE00`。

<a id="CONFIG_UART_00_NRF_HW_ASYNC_TIMER"></a>

## 165.20 `CONFIG_UART_00_NRF_HW_ASYNC_TIMER`

**提示（Prompt）**：定时器实例（Timer Instance）

**说明（Help）**

此选项已弃用。请使用设备树（Device Tree）的 `timer` 属性分配 TIMER 外设，以在不使用硬件流控制（HWFC）时实现可靠接收。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_UART_00_NRF_USE_TIMER && CONFIG_UART_00_NRF_HW_ASYNC && CONFIG_HAS_HW_NRF_UARTE00 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_00_NRF_USE_TIMER`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_00_NRF_USE_TIMER)、[`CONFIG_UART_00_NRF_HW_ASYNC`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_00_NRF_HW_ASYNC)、[`CONFIG_HAS_HW_NRF_UARTE00`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE00)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE00`。

<a id="CONFIG_UART_00_NRF_PARITY_BIT"></a>

## 165.21 `CONFIG_UART_00_NRF_PARITY_BIT`

**提示（Prompt）**：奇偶校验位（Parity Bit）

**说明（Help）**

启用奇偶校验位（Parity Bit）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE00 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE00`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE00)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE00`。

<a id="CONFIG_UART_00_NRF_TX_BUFFER_SIZE"></a>

## 165.22 `CONFIG_UART_00_NRF_TX_BUFFER_SIZE`

**提示（Prompt）**：RAM 缓冲区大小

**说明（Help）**

API 函数 `fifo_fill` 使用的发送缓冲区大小。此值受具体片上系统（SoC）的 `TXD.MAXCNT` 寄存器取值范围限制。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE00 && CONFIG_HAS_HW_NRF_UARTE00 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[1, 65535]
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE00`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE00)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE00`。

<a id="CONFIG_UART_00_NRF_USE_TIMER"></a>

## 165.23 `CONFIG_UART_00_NRF_USE_TIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了用于接收（RX）字节计数的 TIMER 外设。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

<a id="CONFIG_UART_0_ASYNC"></a>

## 165.24 `CONFIG_UART_0_ASYNC`

**提示（Prompt）**：端口 0 的异步 API（Asynchronous API）支持

**说明（Help）**

此选项启用端口 `$(nrfx_uart_num)` 的 UART 异步 API（Asynchronous API）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && !CONFIG_UART_0_INTERRUPT_DRIVEN && (CONFIG_HAS_HW_NRF_UART0 || CONFIG_HAS_HW_NRF_UARTE0) && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_UART_0_INTERRUPT_DRIVEN`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_0_INTERRUPT_DRIVEN)、[`CONFIG_HAS_HW_NRF_UART0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UART0)、[`CONFIG_HAS_HW_NRF_UARTE0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE0)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UART0`、`CONFIG_HAS_HW_NRF_UARTE0`。

<a id="CONFIG_UART_0_COUNT_BYTES_WITH_TIMER"></a>

## 165.25 `CONFIG_UART_0_COUNT_BYTES_WITH_TIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了一个用于接收（RX）字节计数的 TIMER 外设。适用于 nRF54x 系列等较新目标平台使用的 UARTE 修订版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER`](P165_drivers_serial_配置项参考_1.md#CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER)。

<a id="CONFIG_UART_0_COUNT_BYTES_WITH_TIMER_LEGACY"></a>

## 165.26 `CONFIG_UART_0_COUNT_BYTES_WITH_TIMER_LEGACY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了一个用于接收（RX）字节计数的 TIMER 外设。适用于旧目标平台 nRF52x、nRF53x 和 nRF91x 使用的 UARTE 修订版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_UART_0_NRF_USE_TIMER || CONFIG_UART_0_NRF_HW_ASYNC) && !n && (CONFIG_HAS_HW_NRF_UART0 || CONFIG_HAS_HW_NRF_UARTE0) && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_0_NRF_USE_TIMER`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_0_NRF_USE_TIMER)、[`CONFIG_UART_0_NRF_HW_ASYNC`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_0_NRF_HW_ASYNC)、[`CONFIG_HAS_HW_NRF_UART0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UART0)、[`CONFIG_HAS_HW_NRF_UARTE0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE0)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY`](P165_drivers_serial_配置项参考_1.md#CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UART0`、`CONFIG_HAS_HW_NRF_UARTE0`。

<a id="CONFIG_UART_0_ENHANCED_POLL_OUT"></a>

## 165.27 `CONFIG_UART_0_ENHANCED_POLL_OUT`

**提示（Prompt）**：端口 0 的高效轮询输出（Efficient Poll Out）

**说明（Help）**

启用时，轮询输出（Polling Out）不会触发用于停止发送（TX）的中断。此功能使用一个可编程外设互连（PPI）通道。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!n && CONFIG_HAS_HW_NRF_UARTE0 && (CONFIG_HAS_HW_NRF_PPI || CONFIG_HAS_HW_NRF_DPPIC) && (CONFIG_HAS_HW_NRF_UART0 || CONFIG_HAS_HW_NRF_UARTE0) && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NRFX_GPPI
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE0)、[`CONFIG_HAS_HW_NRF_PPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_PPI)、[`CONFIG_HAS_HW_NRF_DPPIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_DPPIC)、[`CONFIG_HAS_HW_NRF_UART0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UART0)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_NRFX_GPPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_GPPI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE0`、`CONFIG_HAS_HW_NRF_PPI`、`CONFIG_HAS_HW_NRF_DPPIC`、`CONFIG_HAS_HW_NRF_UART0`。

<a id="CONFIG_UART_0_INTERRUPT_DRIVEN"></a>

## 165.28 `CONFIG_UART_0_INTERRUPT_DRIVEN`

**提示（Prompt）**：端口 0 的中断支持（Interrupt Support）

**说明（Help）**

此选项启用端口 `$(nrfx_uart_num)` 的 UART 中断支持（Interrupt Support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_INTERRUPT_DRIVEN && (CONFIG_HAS_HW_NRF_UART0 || CONFIG_HAS_HW_NRF_UARTE0) && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_INTERRUPT_DRIVEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_HAS_HW_NRF_UART0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UART0)、[`CONFIG_HAS_HW_NRF_UARTE0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE0)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UART0`、`CONFIG_HAS_HW_NRF_UARTE0`。

<a id="CONFIG_UART_0_NRF_ASYNC_LOW_POWER"></a>

## 165.29 `CONFIG_UART_0_NRF_ASYNC_LOW_POWER`

**提示（Prompt）**：低功耗模式（Low Power Mode）

**说明（Help）**

启用时，每次发送（TX）或接收（RX）前都会启用 UARTE，不使用时则禁用。在空闲时禁用 UARTE 可以实现最低功耗，但仅在接收器不需要始终开启时可行。启用设备电源管理（PM）时，此选项不起作用，因为设备状态改由 PM 操作控制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE0 && CONFIG_UART_ASYNC_API && (CONFIG_HAS_HW_NRF_UART0 || CONFIG_HAS_HW_NRF_UARTE0) && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y if !CONFIG_PM_DEVICE
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE0)、[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_HAS_HW_NRF_UART0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UART0)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_PM_DEVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE0`、`CONFIG_HAS_HW_NRF_UART0`。

<a id="CONFIG_UART_0_NRF_HW_ASYNC"></a>

## 165.30 `CONFIG_UART_0_NRF_HW_ASYNC`

**提示（Prompt）**：使用硬件接收字节计数（Hardware RX Byte Counting）［已弃用，DEPRECATED］

**说明（Help）**

此选项已弃用。请使用设备树（Device Tree）的 `timer` 属性分配 TIMER 外设，以在不使用硬件流控制（HWFC）时实现可靠接收。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && CONFIG_HAS_HW_NRF_UARTE0 && !n && (CONFIG_HAS_HW_NRF_UART0 || CONFIG_HAS_HW_NRF_UARTE0) && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_HAS_HW_NRF_UARTE0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE0)、[`CONFIG_HAS_HW_NRF_UART0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UART0)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE0`、`CONFIG_HAS_HW_NRF_UART0`。

<a id="CONFIG_UART_0_NRF_HW_ASYNC_TIMER"></a>

## 165.31 `CONFIG_UART_0_NRF_HW_ASYNC_TIMER`

**提示（Prompt）**：定时器实例（Timer Instance）

**说明（Help）**

此选项已弃用。请使用设备树（Device Tree）的 `timer` 属性分配 TIMER 外设，以在不使用硬件流控制（HWFC）时实现可靠接收。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_UART_0_NRF_USE_TIMER && CONFIG_UART_0_NRF_HW_ASYNC && (CONFIG_HAS_HW_NRF_UART0 || CONFIG_HAS_HW_NRF_UARTE0) && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_0_NRF_USE_TIMER`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_0_NRF_USE_TIMER)、[`CONFIG_UART_0_NRF_HW_ASYNC`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_0_NRF_HW_ASYNC)、[`CONFIG_HAS_HW_NRF_UART0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UART0)、[`CONFIG_HAS_HW_NRF_UARTE0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE0)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UART0`、`CONFIG_HAS_HW_NRF_UARTE0`。

<a id="CONFIG_UART_0_NRF_PARITY_BIT"></a>

## 165.32 `CONFIG_UART_0_NRF_PARITY_BIT`

**提示（Prompt）**：奇偶校验位（Parity Bit）

**说明（Help）**

启用奇偶校验位（Parity Bit）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_HAS_HW_NRF_UART0 || CONFIG_HAS_HW_NRF_UARTE0) && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UART0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UART0)、[`CONFIG_HAS_HW_NRF_UARTE0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE0)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UART0`、`CONFIG_HAS_HW_NRF_UARTE0`。

<a id="CONFIG_UART_0_NRF_TX_BUFFER_SIZE"></a>

## 165.33 `CONFIG_UART_0_NRF_TX_BUFFER_SIZE`

**提示（Prompt）**：RAM 缓冲区大小

**说明（Help）**

API 函数 `fifo_fill` 使用的发送缓冲区大小。此值受具体片上系统（SoC）的 `TXD.MAXCNT` 寄存器取值范围限制。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE0 && (CONFIG_HAS_HW_NRF_UART0 || CONFIG_HAS_HW_NRF_UARTE0) && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[1, 65535]
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE0)、[`CONFIG_HAS_HW_NRF_UART0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UART0)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE0`、`CONFIG_HAS_HW_NRF_UART0`。

<a id="CONFIG_UART_0_NRF_USE_TIMER"></a>

## 165.34 `CONFIG_UART_0_NRF_USE_TIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了用于接收（RX）字节计数的 TIMER 外设。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

<a id="CONFIG_UART_120_ASYNC"></a>

## 165.35 `CONFIG_UART_120_ASYNC`

**提示（Prompt）**：端口 120 的异步 API（Asynchronous API）支持

**说明（Help）**

此选项启用端口 `$(nrfx_uart_num)` 的 UART 异步 API（Asynchronous API）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && !CONFIG_UART_120_INTERRUPT_DRIVEN && CONFIG_HAS_HW_NRF_UARTE120 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_UART_120_INTERRUPT_DRIVEN`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_120_INTERRUPT_DRIVEN)、[`CONFIG_HAS_HW_NRF_UARTE120`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE120)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE120`。

<a id="CONFIG_UART_120_COUNT_BYTES_WITH_TIMER"></a>

## 165.36 `CONFIG_UART_120_COUNT_BYTES_WITH_TIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了一个用于接收（RX）字节计数的 TIMER 外设。适用于 nRF54x 系列等较新目标平台使用的 UARTE 修订版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER`](P165_drivers_serial_配置项参考_1.md#CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER)。

<a id="CONFIG_UART_120_COUNT_BYTES_WITH_TIMER_LEGACY"></a>

## 165.37 `CONFIG_UART_120_COUNT_BYTES_WITH_TIMER_LEGACY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了一个用于接收（RX）字节计数的 TIMER 外设。适用于旧目标平台 nRF52x、nRF53x 和 nRF91x 使用的 UARTE 修订版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_UART_120_NRF_USE_TIMER || CONFIG_UART_120_NRF_HW_ASYNC) && !n && CONFIG_HAS_HW_NRF_UARTE120 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_120_NRF_USE_TIMER`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_120_NRF_USE_TIMER)、[`CONFIG_UART_120_NRF_HW_ASYNC`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_120_NRF_HW_ASYNC)、[`CONFIG_HAS_HW_NRF_UARTE120`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE120)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY`](P165_drivers_serial_配置项参考_1.md#CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE120`。

<a id="CONFIG_UART_120_ENHANCED_POLL_OUT"></a>

## 165.38 `CONFIG_UART_120_ENHANCED_POLL_OUT`

**提示（Prompt）**：端口 120 的高效轮询输出（Efficient Poll Out）

**说明（Help）**

启用时，轮询输出（Polling Out）不会触发用于停止发送（TX）的中断。此功能使用一个可编程外设互连（PPI）通道。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!n && CONFIG_HAS_HW_NRF_UARTE120 && (CONFIG_HAS_HW_NRF_PPI || CONFIG_HAS_HW_NRF_DPPIC) && CONFIG_HAS_HW_NRF_UARTE120 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NRFX_GPPI
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE120`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE120)、[`CONFIG_HAS_HW_NRF_PPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_PPI)、[`CONFIG_HAS_HW_NRF_DPPIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_DPPIC)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_NRFX_GPPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_GPPI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE120`、`CONFIG_HAS_HW_NRF_PPI`、`CONFIG_HAS_HW_NRF_DPPIC`。

<a id="CONFIG_UART_120_INTERRUPT_DRIVEN"></a>

## 165.39 `CONFIG_UART_120_INTERRUPT_DRIVEN`

**提示（Prompt）**：端口 120 的中断支持（Interrupt Support）

**说明（Help）**

此选项启用端口 `$(nrfx_uart_num)` 的 UART 中断支持（Interrupt Support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_INTERRUPT_DRIVEN && CONFIG_HAS_HW_NRF_UARTE120 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_INTERRUPT_DRIVEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_HAS_HW_NRF_UARTE120`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE120)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE120`。

<a id="CONFIG_UART_120_NRF_ASYNC_LOW_POWER"></a>

## 165.40 `CONFIG_UART_120_NRF_ASYNC_LOW_POWER`

**提示（Prompt）**：低功耗模式（Low Power Mode）

**说明（Help）**

启用时，每次发送（TX）或接收（RX）前都会启用 UARTE，不使用时则禁用。在空闲时禁用 UARTE 可以实现最低功耗，但仅在接收器不需要始终开启时可行。启用设备电源管理（PM）时，此选项不起作用，因为设备状态改由 PM 操作控制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE120 && CONFIG_UART_ASYNC_API && CONFIG_HAS_HW_NRF_UARTE120 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y if !CONFIG_PM_DEVICE
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE120`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE120)、[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_PM_DEVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE120`。

<a id="CONFIG_UART_120_NRF_HW_ASYNC"></a>

## 165.41 `CONFIG_UART_120_NRF_HW_ASYNC`

**提示（Prompt）**：使用硬件接收字节计数（Hardware RX Byte Counting）［已弃用，DEPRECATED］

**说明（Help）**

此选项已弃用。请使用设备树（Device Tree）的 `timer` 属性分配 TIMER 外设，以在不使用硬件流控制（HWFC）时实现可靠接收。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && CONFIG_HAS_HW_NRF_UARTE120 && !n && CONFIG_HAS_HW_NRF_UARTE120 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_HAS_HW_NRF_UARTE120`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE120)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE120`。

<a id="CONFIG_UART_120_NRF_HW_ASYNC_TIMER"></a>

## 165.42 `CONFIG_UART_120_NRF_HW_ASYNC_TIMER`

**提示（Prompt）**：定时器实例（Timer Instance）

**说明（Help）**

此选项已弃用。请使用设备树（Device Tree）的 `timer` 属性分配 TIMER 外设，以在不使用硬件流控制（HWFC）时实现可靠接收。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_UART_120_NRF_USE_TIMER && CONFIG_UART_120_NRF_HW_ASYNC && CONFIG_HAS_HW_NRF_UARTE120 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_120_NRF_USE_TIMER`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_120_NRF_USE_TIMER)、[`CONFIG_UART_120_NRF_HW_ASYNC`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_120_NRF_HW_ASYNC)、[`CONFIG_HAS_HW_NRF_UARTE120`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE120)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE120`。

<a id="CONFIG_UART_120_NRF_PARITY_BIT"></a>

## 165.43 `CONFIG_UART_120_NRF_PARITY_BIT`

**提示（Prompt）**：奇偶校验位（Parity Bit）

**说明（Help）**

启用奇偶校验位（Parity Bit）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE120 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE120`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE120)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE120`。

<a id="CONFIG_UART_120_NRF_TX_BUFFER_SIZE"></a>

## 165.44 `CONFIG_UART_120_NRF_TX_BUFFER_SIZE`

**提示（Prompt）**：RAM 缓冲区大小

**说明（Help）**

API 函数 `fifo_fill` 使用的发送缓冲区大小。此值受具体片上系统（SoC）的 `TXD.MAXCNT` 寄存器取值范围限制。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE120 && CONFIG_HAS_HW_NRF_UARTE120 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[1, 65535]
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE120`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE120)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE120`。

<a id="CONFIG_UART_120_NRF_USE_TIMER"></a>

## 165.45 `CONFIG_UART_120_NRF_USE_TIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了用于接收（RX）字节计数的 TIMER 外设。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

<a id="CONFIG_UART_130_ASYNC"></a>

## 165.46 `CONFIG_UART_130_ASYNC`

**提示（Prompt）**：端口 130 的异步 API（Asynchronous API）支持

**说明（Help）**

此选项启用端口 `$(nrfx_uart_num)` 的 UART 异步 API（Asynchronous API）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && !CONFIG_UART_130_INTERRUPT_DRIVEN && CONFIG_HAS_HW_NRF_UARTE130 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_UART_130_INTERRUPT_DRIVEN`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_130_INTERRUPT_DRIVEN)、[`CONFIG_HAS_HW_NRF_UARTE130`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE130)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE130`。

<a id="CONFIG_UART_130_COUNT_BYTES_WITH_TIMER"></a>

## 165.47 `CONFIG_UART_130_COUNT_BYTES_WITH_TIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了一个用于接收（RX）字节计数的 TIMER 外设。适用于 nRF54x 系列等较新目标平台使用的 UARTE 修订版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER`](P165_drivers_serial_配置项参考_1.md#CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER)。

<a id="CONFIG_UART_130_COUNT_BYTES_WITH_TIMER_LEGACY"></a>

## 165.48 `CONFIG_UART_130_COUNT_BYTES_WITH_TIMER_LEGACY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了一个用于接收（RX）字节计数的 TIMER 外设。适用于旧目标平台 nRF52x、nRF53x 和 nRF91x 使用的 UARTE 修订版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_UART_130_NRF_USE_TIMER || CONFIG_UART_130_NRF_HW_ASYNC) && !n && CONFIG_HAS_HW_NRF_UARTE130 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_130_NRF_USE_TIMER`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_130_NRF_USE_TIMER)、[`CONFIG_UART_130_NRF_HW_ASYNC`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_130_NRF_HW_ASYNC)、[`CONFIG_HAS_HW_NRF_UARTE130`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE130)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY`](P165_drivers_serial_配置项参考_1.md#CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE130`。

<a id="CONFIG_UART_130_ENHANCED_POLL_OUT"></a>

## 165.49 `CONFIG_UART_130_ENHANCED_POLL_OUT`

**提示（Prompt）**：端口 130 的高效轮询输出（Efficient Poll Out）

**说明（Help）**

启用时，轮询输出（Polling Out）不会触发用于停止发送（TX）的中断。此功能使用一个可编程外设互连（PPI）通道。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!n && CONFIG_HAS_HW_NRF_UARTE130 && (CONFIG_HAS_HW_NRF_PPI || CONFIG_HAS_HW_NRF_DPPIC) && CONFIG_HAS_HW_NRF_UARTE130 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NRFX_GPPI
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE130`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE130)、[`CONFIG_HAS_HW_NRF_PPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_PPI)、[`CONFIG_HAS_HW_NRF_DPPIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_DPPIC)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_NRFX_GPPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_GPPI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE130`、`CONFIG_HAS_HW_NRF_PPI`、`CONFIG_HAS_HW_NRF_DPPIC`。

<a id="CONFIG_UART_130_INTERRUPT_DRIVEN"></a>

## 165.50 `CONFIG_UART_130_INTERRUPT_DRIVEN`

**提示（Prompt）**：端口 130 的中断支持（Interrupt Support）

**说明（Help）**

此选项启用端口 `$(nrfx_uart_num)` 的 UART 中断支持（Interrupt Support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_INTERRUPT_DRIVEN && CONFIG_HAS_HW_NRF_UARTE130 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_INTERRUPT_DRIVEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_HAS_HW_NRF_UARTE130`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE130)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE130`。

<a id="CONFIG_UART_130_NRF_ASYNC_LOW_POWER"></a>

## 165.51 `CONFIG_UART_130_NRF_ASYNC_LOW_POWER`

**提示（Prompt）**：低功耗模式（Low Power Mode）

**说明（Help）**

启用时，每次发送（TX）或接收（RX）前都会启用 UARTE，不使用时则禁用。在空闲时禁用 UARTE 可以实现最低功耗，但仅在接收器不需要始终开启时可行。启用设备电源管理（PM）时，此选项不起作用，因为设备状态改由 PM 操作控制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE130 && CONFIG_UART_ASYNC_API && CONFIG_HAS_HW_NRF_UARTE130 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y if !CONFIG_PM_DEVICE
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE130`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE130)、[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_PM_DEVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE130`。

<a id="CONFIG_UART_130_NRF_HW_ASYNC"></a>

## 165.52 `CONFIG_UART_130_NRF_HW_ASYNC`

**提示（Prompt）**：使用硬件接收字节计数（Hardware RX Byte Counting）［已弃用，DEPRECATED］

**说明（Help）**

此选项已弃用。请使用设备树（Device Tree）的 `timer` 属性分配 TIMER 外设，以在不使用硬件流控制（HWFC）时实现可靠接收。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && CONFIG_HAS_HW_NRF_UARTE130 && !n && CONFIG_HAS_HW_NRF_UARTE130 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_HAS_HW_NRF_UARTE130`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE130)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE130`。

<a id="CONFIG_UART_130_NRF_HW_ASYNC_TIMER"></a>

## 165.53 `CONFIG_UART_130_NRF_HW_ASYNC_TIMER`

**提示（Prompt）**：定时器实例（Timer Instance）

**说明（Help）**

此选项已弃用。请使用设备树（Device Tree）的 `timer` 属性分配 TIMER 外设，以在不使用硬件流控制（HWFC）时实现可靠接收。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_UART_130_NRF_USE_TIMER && CONFIG_UART_130_NRF_HW_ASYNC && CONFIG_HAS_HW_NRF_UARTE130 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_130_NRF_USE_TIMER`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_130_NRF_USE_TIMER)、[`CONFIG_UART_130_NRF_HW_ASYNC`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_130_NRF_HW_ASYNC)、[`CONFIG_HAS_HW_NRF_UARTE130`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE130)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE130`。

<a id="CONFIG_UART_130_NRF_PARITY_BIT"></a>

## 165.54 `CONFIG_UART_130_NRF_PARITY_BIT`

**提示（Prompt）**：奇偶校验位（Parity Bit）

**说明（Help）**

启用奇偶校验位（Parity Bit）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE130 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE130`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE130)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE130`。

<a id="CONFIG_UART_130_NRF_TX_BUFFER_SIZE"></a>

## 165.55 `CONFIG_UART_130_NRF_TX_BUFFER_SIZE`

**提示（Prompt）**：RAM 缓冲区大小

**说明（Help）**

API 函数 `fifo_fill` 使用的发送缓冲区大小。此值受具体片上系统（SoC）的 `TXD.MAXCNT` 寄存器取值范围限制。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE130 && CONFIG_HAS_HW_NRF_UARTE130 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[1, 65535]
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE130`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE130)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE130`。

<a id="CONFIG_UART_130_NRF_USE_TIMER"></a>

## 165.56 `CONFIG_UART_130_NRF_USE_TIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了用于接收（RX）字节计数的 TIMER 外设。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

<a id="CONFIG_UART_131_ASYNC"></a>

## 165.57 `CONFIG_UART_131_ASYNC`

**提示（Prompt）**：端口 131 的异步 API（Asynchronous API）支持

**说明（Help）**

此选项启用端口 `$(nrfx_uart_num)` 的 UART 异步 API（Asynchronous API）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && !CONFIG_UART_131_INTERRUPT_DRIVEN && CONFIG_HAS_HW_NRF_UARTE131 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_UART_131_INTERRUPT_DRIVEN`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_131_INTERRUPT_DRIVEN)、[`CONFIG_HAS_HW_NRF_UARTE131`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE131)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE131`。

<a id="CONFIG_UART_131_COUNT_BYTES_WITH_TIMER"></a>

## 165.58 `CONFIG_UART_131_COUNT_BYTES_WITH_TIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了一个用于接收（RX）字节计数的 TIMER 外设。适用于 nRF54x 系列等较新目标平台使用的 UARTE 修订版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER`](P165_drivers_serial_配置项参考_1.md#CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER)。

<a id="CONFIG_UART_131_COUNT_BYTES_WITH_TIMER_LEGACY"></a>

## 165.59 `CONFIG_UART_131_COUNT_BYTES_WITH_TIMER_LEGACY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了一个用于接收（RX）字节计数的 TIMER 外设。适用于旧目标平台 nRF52x、nRF53x 和 nRF91x 使用的 UARTE 修订版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_UART_131_NRF_USE_TIMER || CONFIG_UART_131_NRF_HW_ASYNC) && !n && CONFIG_HAS_HW_NRF_UARTE131 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_131_NRF_USE_TIMER`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_131_NRF_USE_TIMER)、[`CONFIG_UART_131_NRF_HW_ASYNC`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_131_NRF_HW_ASYNC)、[`CONFIG_HAS_HW_NRF_UARTE131`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE131)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY`](P165_drivers_serial_配置项参考_1.md#CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE131`。

<a id="CONFIG_UART_131_ENHANCED_POLL_OUT"></a>

## 165.60 `CONFIG_UART_131_ENHANCED_POLL_OUT`

**提示（Prompt）**：端口 131 的高效轮询输出（Efficient Poll Out）

**说明（Help）**

启用时，轮询输出（Polling Out）不会触发用于停止发送（TX）的中断。此功能使用一个可编程外设互连（PPI）通道。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!n && CONFIG_HAS_HW_NRF_UARTE131 && (CONFIG_HAS_HW_NRF_PPI || CONFIG_HAS_HW_NRF_DPPIC) && CONFIG_HAS_HW_NRF_UARTE131 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NRFX_GPPI
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE131`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE131)、[`CONFIG_HAS_HW_NRF_PPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_PPI)、[`CONFIG_HAS_HW_NRF_DPPIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_DPPIC)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_NRFX_GPPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_GPPI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE131`、`CONFIG_HAS_HW_NRF_PPI`、`CONFIG_HAS_HW_NRF_DPPIC`。

<a id="CONFIG_UART_131_INTERRUPT_DRIVEN"></a>

## 165.61 `CONFIG_UART_131_INTERRUPT_DRIVEN`

**提示（Prompt）**：端口 131 的中断支持（Interrupt Support）

**说明（Help）**

此选项启用端口 `$(nrfx_uart_num)` 的 UART 中断支持（Interrupt Support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_INTERRUPT_DRIVEN && CONFIG_HAS_HW_NRF_UARTE131 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_INTERRUPT_DRIVEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_HAS_HW_NRF_UARTE131`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE131)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE131`。

<a id="CONFIG_UART_131_NRF_ASYNC_LOW_POWER"></a>

## 165.62 `CONFIG_UART_131_NRF_ASYNC_LOW_POWER`

**提示（Prompt）**：低功耗模式（Low Power Mode）

**说明（Help）**

启用时，每次发送（TX）或接收（RX）前都会启用 UARTE，不使用时则禁用。在空闲时禁用 UARTE 可以实现最低功耗，但仅在接收器不需要始终开启时可行。启用设备电源管理（PM）时，此选项不起作用，因为设备状态改由 PM 操作控制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE131 && CONFIG_UART_ASYNC_API && CONFIG_HAS_HW_NRF_UARTE131 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y if !CONFIG_PM_DEVICE
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE131`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE131)、[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_PM_DEVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE131`。

<a id="CONFIG_UART_131_NRF_HW_ASYNC"></a>

## 165.63 `CONFIG_UART_131_NRF_HW_ASYNC`

**提示（Prompt）**：使用硬件接收字节计数（Hardware RX Byte Counting）［已弃用，DEPRECATED］

**说明（Help）**

此选项已弃用。请使用设备树（Device Tree）的 `timer` 属性分配 TIMER 外设，以在不使用硬件流控制（HWFC）时实现可靠接收。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && CONFIG_HAS_HW_NRF_UARTE131 && !n && CONFIG_HAS_HW_NRF_UARTE131 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_HAS_HW_NRF_UARTE131`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE131)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE131`。

<a id="CONFIG_UART_131_NRF_HW_ASYNC_TIMER"></a>

## 165.64 `CONFIG_UART_131_NRF_HW_ASYNC_TIMER`

**提示（Prompt）**：定时器实例（Timer Instance）

**说明（Help）**

此选项已弃用。请使用设备树（Device Tree）的 `timer` 属性分配 TIMER 外设，以在不使用硬件流控制（HWFC）时实现可靠接收。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_UART_131_NRF_USE_TIMER && CONFIG_UART_131_NRF_HW_ASYNC && CONFIG_HAS_HW_NRF_UARTE131 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_131_NRF_USE_TIMER`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_131_NRF_USE_TIMER)、[`CONFIG_UART_131_NRF_HW_ASYNC`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_131_NRF_HW_ASYNC)、[`CONFIG_HAS_HW_NRF_UARTE131`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE131)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE131`。

<a id="CONFIG_UART_131_NRF_PARITY_BIT"></a>

## 165.65 `CONFIG_UART_131_NRF_PARITY_BIT`

**提示（Prompt）**：奇偶校验位（Parity Bit）

**说明（Help）**

启用奇偶校验位（Parity Bit）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE131 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE131`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE131)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE131`。

<a id="CONFIG_UART_131_NRF_TX_BUFFER_SIZE"></a>

## 165.66 `CONFIG_UART_131_NRF_TX_BUFFER_SIZE`

**提示（Prompt）**：RAM 缓冲区大小

**说明（Help）**

API 函数 `fifo_fill` 使用的发送缓冲区大小。此值受具体片上系统（SoC）的 `TXD.MAXCNT` 寄存器取值范围限制。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE131 && CONFIG_HAS_HW_NRF_UARTE131 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[1, 65535]
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE131`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE131)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE131`。

<a id="CONFIG_UART_131_NRF_USE_TIMER"></a>

## 165.67 `CONFIG_UART_131_NRF_USE_TIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了用于接收（RX）字节计数的 TIMER 外设。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

<a id="CONFIG_UART_132_ASYNC"></a>

## 165.68 `CONFIG_UART_132_ASYNC`

**提示（Prompt）**：端口 132 的异步 API（Asynchronous API）支持

**说明（Help）**

此选项启用端口 `$(nrfx_uart_num)` 的 UART 异步 API（Asynchronous API）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && !CONFIG_UART_132_INTERRUPT_DRIVEN && CONFIG_HAS_HW_NRF_UARTE132 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_UART_132_INTERRUPT_DRIVEN`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_132_INTERRUPT_DRIVEN)、[`CONFIG_HAS_HW_NRF_UARTE132`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE132)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE132`。

<a id="CONFIG_UART_132_COUNT_BYTES_WITH_TIMER"></a>

## 165.69 `CONFIG_UART_132_COUNT_BYTES_WITH_TIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了一个用于接收（RX）字节计数的 TIMER 外设。适用于 nRF54x 系列等较新目标平台使用的 UARTE 修订版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER`](P165_drivers_serial_配置项参考_1.md#CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER)。

<a id="CONFIG_UART_132_COUNT_BYTES_WITH_TIMER_LEGACY"></a>

## 165.70 `CONFIG_UART_132_COUNT_BYTES_WITH_TIMER_LEGACY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了一个用于接收（RX）字节计数的 TIMER 外设。适用于旧目标平台 nRF52x、nRF53x 和 nRF91x 使用的 UARTE 修订版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_UART_132_NRF_USE_TIMER || CONFIG_UART_132_NRF_HW_ASYNC) && !n && CONFIG_HAS_HW_NRF_UARTE132 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_132_NRF_USE_TIMER`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_132_NRF_USE_TIMER)、[`CONFIG_UART_132_NRF_HW_ASYNC`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_132_NRF_HW_ASYNC)、[`CONFIG_HAS_HW_NRF_UARTE132`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE132)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY`](P165_drivers_serial_配置项参考_1.md#CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE132`。

<a id="CONFIG_UART_132_ENHANCED_POLL_OUT"></a>

## 165.71 `CONFIG_UART_132_ENHANCED_POLL_OUT`

**提示（Prompt）**：端口 132 的高效轮询输出（Efficient Poll Out）

**说明（Help）**

启用时，轮询输出（Polling Out）不会触发用于停止发送（TX）的中断。此功能使用一个可编程外设互连（PPI）通道。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!n && CONFIG_HAS_HW_NRF_UARTE132 && (CONFIG_HAS_HW_NRF_PPI || CONFIG_HAS_HW_NRF_DPPIC) && CONFIG_HAS_HW_NRF_UARTE132 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NRFX_GPPI
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE132`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE132)、[`CONFIG_HAS_HW_NRF_PPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_PPI)、[`CONFIG_HAS_HW_NRF_DPPIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_DPPIC)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_NRFX_GPPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_GPPI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE132`、`CONFIG_HAS_HW_NRF_PPI`、`CONFIG_HAS_HW_NRF_DPPIC`。

<a id="CONFIG_UART_132_INTERRUPT_DRIVEN"></a>

## 165.72 `CONFIG_UART_132_INTERRUPT_DRIVEN`

**提示（Prompt）**：端口 132 的中断支持（Interrupt Support）

**说明（Help）**

此选项启用端口 `$(nrfx_uart_num)` 的 UART 中断支持（Interrupt Support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_INTERRUPT_DRIVEN && CONFIG_HAS_HW_NRF_UARTE132 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_INTERRUPT_DRIVEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_HAS_HW_NRF_UARTE132`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE132)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE132`。

<a id="CONFIG_UART_132_NRF_ASYNC_LOW_POWER"></a>

## 165.73 `CONFIG_UART_132_NRF_ASYNC_LOW_POWER`

**提示（Prompt）**：低功耗模式（Low Power Mode）

**说明（Help）**

启用时，每次发送（TX）或接收（RX）前都会启用 UARTE，不使用时则禁用。在空闲时禁用 UARTE 可以实现最低功耗，但仅在接收器不需要始终开启时可行。启用设备电源管理（PM）时，此选项不起作用，因为设备状态改由 PM 操作控制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE132 && CONFIG_UART_ASYNC_API && CONFIG_HAS_HW_NRF_UARTE132 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y if !CONFIG_PM_DEVICE
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE132`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE132)、[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_PM_DEVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE132`。

<a id="CONFIG_UART_132_NRF_HW_ASYNC"></a>

## 165.74 `CONFIG_UART_132_NRF_HW_ASYNC`

**提示（Prompt）**：使用硬件接收字节计数（Hardware RX Byte Counting）［已弃用，DEPRECATED］

**说明（Help）**

此选项已弃用。请使用设备树（Device Tree）的 `timer` 属性分配 TIMER 外设，以在不使用硬件流控制（HWFC）时实现可靠接收。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && CONFIG_HAS_HW_NRF_UARTE132 && !n && CONFIG_HAS_HW_NRF_UARTE132 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_HAS_HW_NRF_UARTE132`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE132)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE132`。

<a id="CONFIG_UART_132_NRF_HW_ASYNC_TIMER"></a>

## 165.75 `CONFIG_UART_132_NRF_HW_ASYNC_TIMER`

**提示（Prompt）**：定时器实例（Timer Instance）

**说明（Help）**

此选项已弃用。请使用设备树（Device Tree）的 `timer` 属性分配 TIMER 外设，以在不使用硬件流控制（HWFC）时实现可靠接收。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_UART_132_NRF_USE_TIMER && CONFIG_UART_132_NRF_HW_ASYNC && CONFIG_HAS_HW_NRF_UARTE132 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_132_NRF_USE_TIMER`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_132_NRF_USE_TIMER)、[`CONFIG_UART_132_NRF_HW_ASYNC`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_132_NRF_HW_ASYNC)、[`CONFIG_HAS_HW_NRF_UARTE132`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE132)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE132`。

<a id="CONFIG_UART_132_NRF_PARITY_BIT"></a>

## 165.76 `CONFIG_UART_132_NRF_PARITY_BIT`

**提示（Prompt）**：奇偶校验位（Parity Bit）

**说明（Help）**

启用奇偶校验位（Parity Bit）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE132 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE132`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE132)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE132`。

<a id="CONFIG_UART_132_NRF_TX_BUFFER_SIZE"></a>

## 165.77 `CONFIG_UART_132_NRF_TX_BUFFER_SIZE`

**提示（Prompt）**：RAM 缓冲区大小

**说明（Help）**

API 函数 `fifo_fill` 使用的发送缓冲区大小。此值受具体片上系统（SoC）的 `TXD.MAXCNT` 寄存器取值范围限制。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE132 && CONFIG_HAS_HW_NRF_UARTE132 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[1, 65535]
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE132`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE132)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE132`。

<a id="CONFIG_UART_132_NRF_USE_TIMER"></a>

## 165.78 `CONFIG_UART_132_NRF_USE_TIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了用于接收（RX）字节计数的 TIMER 外设。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

<a id="CONFIG_UART_133_ASYNC"></a>

## 165.79 `CONFIG_UART_133_ASYNC`

**提示（Prompt）**：端口 133 的异步 API（Asynchronous API）支持

**说明（Help）**

此选项启用端口 `$(nrfx_uart_num)` 的 UART 异步 API（Asynchronous API）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && !CONFIG_UART_133_INTERRUPT_DRIVEN && CONFIG_HAS_HW_NRF_UARTE133 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_UART_133_INTERRUPT_DRIVEN`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_133_INTERRUPT_DRIVEN)、[`CONFIG_HAS_HW_NRF_UARTE133`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE133)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE133`。

<a id="CONFIG_UART_133_COUNT_BYTES_WITH_TIMER"></a>

## 165.80 `CONFIG_UART_133_COUNT_BYTES_WITH_TIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了一个用于接收（RX）字节计数的 TIMER 外设。适用于 nRF54x 系列等较新目标平台使用的 UARTE 修订版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER`](P165_drivers_serial_配置项参考_1.md#CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER)。

<a id="CONFIG_UART_133_COUNT_BYTES_WITH_TIMER_LEGACY"></a>

## 165.81 `CONFIG_UART_133_COUNT_BYTES_WITH_TIMER_LEGACY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了一个用于接收（RX）字节计数的 TIMER 外设。适用于旧目标平台 nRF52x、nRF53x 和 nRF91x 使用的 UARTE 修订版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_UART_133_NRF_USE_TIMER || CONFIG_UART_133_NRF_HW_ASYNC) && !n && CONFIG_HAS_HW_NRF_UARTE133 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_133_NRF_USE_TIMER`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_133_NRF_USE_TIMER)、[`CONFIG_UART_133_NRF_HW_ASYNC`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_133_NRF_HW_ASYNC)、[`CONFIG_HAS_HW_NRF_UARTE133`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE133)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY`](P165_drivers_serial_配置项参考_1.md#CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE133`。

<a id="CONFIG_UART_133_ENHANCED_POLL_OUT"></a>

## 165.82 `CONFIG_UART_133_ENHANCED_POLL_OUT`

**提示（Prompt）**：端口 133 的高效轮询输出（Efficient Poll Out）

**说明（Help）**

启用时，轮询输出（Polling Out）不会触发用于停止发送（TX）的中断。此功能使用一个可编程外设互连（PPI）通道。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!n && CONFIG_HAS_HW_NRF_UARTE133 && (CONFIG_HAS_HW_NRF_PPI || CONFIG_HAS_HW_NRF_DPPIC) && CONFIG_HAS_HW_NRF_UARTE133 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NRFX_GPPI
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE133`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE133)、[`CONFIG_HAS_HW_NRF_PPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_PPI)、[`CONFIG_HAS_HW_NRF_DPPIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_DPPIC)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_NRFX_GPPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_GPPI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE133`、`CONFIG_HAS_HW_NRF_PPI`、`CONFIG_HAS_HW_NRF_DPPIC`。

<a id="CONFIG_UART_133_INTERRUPT_DRIVEN"></a>

## 165.83 `CONFIG_UART_133_INTERRUPT_DRIVEN`

**提示（Prompt）**：端口 133 的中断支持（Interrupt Support）

**说明（Help）**

此选项启用端口 `$(nrfx_uart_num)` 的 UART 中断支持（Interrupt Support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_INTERRUPT_DRIVEN && CONFIG_HAS_HW_NRF_UARTE133 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_INTERRUPT_DRIVEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_HAS_HW_NRF_UARTE133`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE133)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE133`。

<a id="CONFIG_UART_133_NRF_ASYNC_LOW_POWER"></a>

## 165.84 `CONFIG_UART_133_NRF_ASYNC_LOW_POWER`

**提示（Prompt）**：低功耗模式（Low Power Mode）

**说明（Help）**

启用时，每次发送（TX）或接收（RX）前都会启用 UARTE，不使用时则禁用。在空闲时禁用 UARTE 可以实现最低功耗，但仅在接收器不需要始终开启时可行。启用设备电源管理（PM）时，此选项不起作用，因为设备状态改由 PM 操作控制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE133 && CONFIG_UART_ASYNC_API && CONFIG_HAS_HW_NRF_UARTE133 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y if !CONFIG_PM_DEVICE
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE133`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE133)、[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_PM_DEVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE133`。

<a id="CONFIG_UART_133_NRF_HW_ASYNC"></a>

## 165.85 `CONFIG_UART_133_NRF_HW_ASYNC`

**提示（Prompt）**：使用硬件接收字节计数（Hardware RX Byte Counting）［已弃用，DEPRECATED］

**说明（Help）**

此选项已弃用。请使用设备树（Device Tree）的 `timer` 属性分配 TIMER 外设，以在不使用硬件流控制（HWFC）时实现可靠接收。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && CONFIG_HAS_HW_NRF_UARTE133 && !n && CONFIG_HAS_HW_NRF_UARTE133 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_HAS_HW_NRF_UARTE133`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE133)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE133`。

<a id="CONFIG_UART_133_NRF_HW_ASYNC_TIMER"></a>

## 165.86 `CONFIG_UART_133_NRF_HW_ASYNC_TIMER`

**提示（Prompt）**：定时器实例（Timer Instance）

**说明（Help）**

此选项已弃用。请使用设备树（Device Tree）的 `timer` 属性分配 TIMER 外设，以在不使用硬件流控制（HWFC）时实现可靠接收。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_UART_133_NRF_USE_TIMER && CONFIG_UART_133_NRF_HW_ASYNC && CONFIG_HAS_HW_NRF_UARTE133 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_133_NRF_USE_TIMER`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_133_NRF_USE_TIMER)、[`CONFIG_UART_133_NRF_HW_ASYNC`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_133_NRF_HW_ASYNC)、[`CONFIG_HAS_HW_NRF_UARTE133`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE133)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE133`。

<a id="CONFIG_UART_133_NRF_PARITY_BIT"></a>

## 165.87 `CONFIG_UART_133_NRF_PARITY_BIT`

**提示（Prompt）**：奇偶校验位（Parity Bit）

**说明（Help）**

启用奇偶校验位（Parity Bit）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE133 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE133`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE133)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE133`。

<a id="CONFIG_UART_133_NRF_TX_BUFFER_SIZE"></a>

## 165.88 `CONFIG_UART_133_NRF_TX_BUFFER_SIZE`

**提示（Prompt）**：RAM 缓冲区大小

**说明（Help）**

API 函数 `fifo_fill` 使用的发送缓冲区大小。此值受具体片上系统（SoC）的 `TXD.MAXCNT` 寄存器取值范围限制。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE133 && CONFIG_HAS_HW_NRF_UARTE133 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[1, 65535]
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE133`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE133)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE133`。

<a id="CONFIG_UART_133_NRF_USE_TIMER"></a>

## 165.89 `CONFIG_UART_133_NRF_USE_TIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了用于接收（RX）字节计数的 TIMER 外设。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

<a id="CONFIG_UART_134_ASYNC"></a>

## 165.90 `CONFIG_UART_134_ASYNC`

**提示（Prompt）**：端口 134 的异步 API（Asynchronous API）支持

**说明（Help）**

此选项启用端口 `$(nrfx_uart_num)` 的 UART 异步 API（Asynchronous API）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && !CONFIG_UART_134_INTERRUPT_DRIVEN && CONFIG_HAS_HW_NRF_UARTE134 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_UART_134_INTERRUPT_DRIVEN`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_134_INTERRUPT_DRIVEN)、[`CONFIG_HAS_HW_NRF_UARTE134`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE134)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE134`。

<a id="CONFIG_UART_134_COUNT_BYTES_WITH_TIMER"></a>

## 165.91 `CONFIG_UART_134_COUNT_BYTES_WITH_TIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了一个用于接收（RX）字节计数的 TIMER 外设。适用于 nRF54x 系列等较新目标平台使用的 UARTE 修订版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER`](P165_drivers_serial_配置项参考_1.md#CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER)。

<a id="CONFIG_UART_134_COUNT_BYTES_WITH_TIMER_LEGACY"></a>

## 165.92 `CONFIG_UART_134_COUNT_BYTES_WITH_TIMER_LEGACY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了一个用于接收（RX）字节计数的 TIMER 外设。适用于旧目标平台 nRF52x、nRF53x 和 nRF91x 使用的 UARTE 修订版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_UART_134_NRF_USE_TIMER || CONFIG_UART_134_NRF_HW_ASYNC) && !n && CONFIG_HAS_HW_NRF_UARTE134 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**弱选择（Implies）**

```text
CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_134_NRF_USE_TIMER`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_134_NRF_USE_TIMER)、[`CONFIG_UART_134_NRF_HW_ASYNC`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_134_NRF_HW_ASYNC)、[`CONFIG_HAS_HW_NRF_UARTE134`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE134)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY`](P165_drivers_serial_配置项参考_1.md#CONFIG_UARTE_NRFX_UARTE_COUNT_BYTES_WITH_TIMER_LEGACY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE134`。

<a id="CONFIG_UART_134_ENHANCED_POLL_OUT"></a>

## 165.93 `CONFIG_UART_134_ENHANCED_POLL_OUT`

**提示（Prompt）**：端口 134 的高效轮询输出（Efficient Poll Out）

**说明（Help）**

启用时，轮询输出（Polling Out）不会触发用于停止发送（TX）的中断。此功能使用一个可编程外设互连（PPI）通道。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!n && CONFIG_HAS_HW_NRF_UARTE134 && (CONFIG_HAS_HW_NRF_PPI || CONFIG_HAS_HW_NRF_DPPIC) && CONFIG_HAS_HW_NRF_UARTE134 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NRFX_GPPI
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE134`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE134)、[`CONFIG_HAS_HW_NRF_PPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_PPI)、[`CONFIG_HAS_HW_NRF_DPPIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_DPPIC)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_NRFX_GPPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_GPPI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE134`、`CONFIG_HAS_HW_NRF_PPI`、`CONFIG_HAS_HW_NRF_DPPIC`。

<a id="CONFIG_UART_134_INTERRUPT_DRIVEN"></a>

## 165.94 `CONFIG_UART_134_INTERRUPT_DRIVEN`

**提示（Prompt）**：端口 134 的中断支持（Interrupt Support）

**说明（Help）**

此选项启用端口 `$(nrfx_uart_num)` 的 UART 中断支持（Interrupt Support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_INTERRUPT_DRIVEN && CONFIG_HAS_HW_NRF_UARTE134 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_INTERRUPT_DRIVEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_HAS_HW_NRF_UARTE134`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE134)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE134`。

<a id="CONFIG_UART_134_NRF_ASYNC_LOW_POWER"></a>

## 165.95 `CONFIG_UART_134_NRF_ASYNC_LOW_POWER`

**提示（Prompt）**：低功耗模式（Low Power Mode）

**说明（Help）**

启用时，每次发送（TX）或接收（RX）前都会启用 UARTE，不使用时则禁用。在空闲时禁用 UARTE 可以实现最低功耗，但仅在接收器不需要始终开启时可行。启用设备电源管理（PM）时，此选项不起作用，因为设备状态改由 PM 操作控制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE134 && CONFIG_UART_ASYNC_API && CONFIG_HAS_HW_NRF_UARTE134 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
y if !CONFIG_PM_DEVICE
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE134`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE134)、[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_PM_DEVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_DEVICE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE134`。

<a id="CONFIG_UART_134_NRF_HW_ASYNC"></a>

## 165.96 `CONFIG_UART_134_NRF_HW_ASYNC`

**提示（Prompt）**：使用硬件接收字节计数（Hardware RX Byte Counting）［已弃用，DEPRECATED］

**说明（Help）**

此选项已弃用。请使用设备树（Device Tree）的 `timer` 属性分配 TIMER 外设，以在不使用硬件流控制（HWFC）时实现可靠接收。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && CONFIG_HAS_HW_NRF_UARTE134 && !n && CONFIG_HAS_HW_NRF_UARTE134 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_HAS_HW_NRF_UARTE134`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE134)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE134`。

<a id="CONFIG_UART_134_NRF_HW_ASYNC_TIMER"></a>

## 165.97 `CONFIG_UART_134_NRF_HW_ASYNC_TIMER`

**提示（Prompt）**：定时器实例（Timer Instance）

**说明（Help）**

此选项已弃用。请使用设备树（Device Tree）的 `timer` 属性分配 TIMER 外设，以在不使用硬件流控制（HWFC）时实现可靠接收。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_UART_134_NRF_USE_TIMER && CONFIG_UART_134_NRF_HW_ASYNC && CONFIG_HAS_HW_NRF_UARTE134 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_134_NRF_USE_TIMER`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_134_NRF_USE_TIMER)、[`CONFIG_UART_134_NRF_HW_ASYNC`](P165_drivers_serial_配置项参考_1.md#CONFIG_UART_134_NRF_HW_ASYNC)、[`CONFIG_HAS_HW_NRF_UARTE134`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE134)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE134`。

<a id="CONFIG_UART_134_NRF_PARITY_BIT"></a>

## 165.98 `CONFIG_UART_134_NRF_PARITY_BIT`

**提示（Prompt）**：奇偶校验位（Parity Bit）

**说明（Help）**

启用奇偶校验位（Parity Bit）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE134 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE134`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE134)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE134`。

<a id="CONFIG_UART_134_NRF_TX_BUFFER_SIZE"></a>

## 165.99 `CONFIG_UART_134_NRF_TX_BUFFER_SIZE`

**提示（Prompt）**：RAM 缓冲区大小

**说明（Help）**

API 函数 `fifo_fill` 使用的发送缓冲区大小。此值受具体片上系统（SoC）的 `TXD.MAXCNT` 寄存器取值范围限制。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HAS_HW_NRF_UARTE134 && CONFIG_HAS_HW_NRF_UARTE134 && CONFIG_UART_NRFX && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[1, 65535]
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_HW_NRF_UARTE134`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_UARTE134)、[`CONFIG_UART_NRFX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_UARTE134`。

<a id="CONFIG_UART_134_NRF_USE_TIMER"></a>

## 165.100 `CONFIG_UART_134_NRF_USE_TIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示设备树（Device Tree）为该实例分配了用于接收（RX）字节计数的 TIMER 外设。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/serial/Kconfig.nrfx_uart_instance:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/Kconfig.nrfx_uart_instance#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → nRF UART nrfx 驱动

<!-- kconfig-navigation -->

[上一章](P164_drivers_sent_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P166_drivers_serial_配置项参考_2.md)
