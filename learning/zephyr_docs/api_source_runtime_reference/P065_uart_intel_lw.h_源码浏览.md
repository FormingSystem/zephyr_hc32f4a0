---
id: learning.zephyr-docs.api-source-runtime-reference.page-65
title: uart_intel_lw.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/uart__intel__lw_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第65章\_uart\_intel\_lw.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/uart__intel__lw_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../hardware/P355_UARTIntelLW扩展.md)。

## 65.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>

```c
/*
 * Copyright (c) 2023 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_DRIVERS_SERIAL_UART_INTEL_LW_H_
#define ZEPHYR_DRIVERS_SERIAL_UART_INTEL_LW_H_

/* End of packet feature.
 * Driver will trigger interrupt upon receiving end of package character.
 * Please enable CONFIG_UART_INTEL_LW_EOP to use this feature.
 * Use the api: uart_drv_cmd with CMD_ENABLE_EOP to enable the feature.
 * This cmd will write the ip register and also set a flag to the driver.
 * The flag will modify uart_irq_callback_user_data_set
 * to set call back function for eop interrupt.
 * Flag is cleared after uart_irq_callback_user_data_set is called.
 */
#define CMD_ENABLE_EOP          0x01
#define CMD_DISABLE_EOP         0x02

/* Transmit break feature.
 * Use uart_drv_cmd with CMD_TRBK_EN to break ongoing transmit.
 * After this cmd, uart is unable to transmit any data.
 * Please use CMD_TRBK_DIS to resume normal operation.
 * Please also call uart_intel_lw_err_check, to clear the error caused
 * by transmit break.
 */
#define CMD_TRBK_EN             0x03
#define CMD_TRBK_DIS            0x04

/* This driver supports interrupt driven api.
 * Polling for data under normal operation, might cause unexpected behaviour.
 * If users wish to poll for data, please use the api:
 * uart_drv_cmd with CMD_POLL_ASSERT_RTS before polling out/in.
 * Then use CMD_POLL_DEASSERT_RTS to resume normal operation after polling.
 */
#define CMD_POLL_ASSERT_RTS     0x05
#define CMD_POLL_DEASSERT_RTS   0x06

#endif /* ZEPHYR_DRIVERS_SERIAL_UART_INTEL_LW_H_ */
```

## 65.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 14 行

包结束功能（End of packet）。驱动在收到包结束字符时触发中断。要使用此功能，请启用 `CONFIG_UART_INTEL_LW_EOP`。

通过 API `uart_drv_cmd` 携带 `CMD_ENABLE_EOP` 命令来启用该功能。该命令会写入 IP 寄存器，并在驱动中设置一个标志。此标志改变 `uart_irq_callback_user_data_set` 的行为，使其设置包结束（EOP）中断的回调函数。在调用 `uart_irq_callback_user_data_set` 后，标志被清除。

### 注释 3：原第 26 行

发送中断信号功能（Transmit break）。使用 `uart_drv_cmd` 携带 `CMD_TRBK_EN` 来中断正在进行的发送。执行该命令后，UART 无法发送任何数据。请使用 `CMD_TRBK_DIS` 恢复正常操作。还请调用 `uart_intel_lw_err_check`，以清除发送中断信号所导致的错误。

### 注释 4：原第 36 行

此驱动支持中断驱动 API。在正常操作期间轮询数据，可能导致意外行为。如果用户需要轮询数据，应在轮询输出/输入之前，通过 API `uart_drv_cmd` 执行 `CMD_POLL_ASSERT_RTS`。轮询结束后，再使用 `CMD_POLL_DEASSERT_RTS` 恢复正常操作。

### 注释 5：原第 45 行

头文件保护宏（Header guard）标记：`ZEPHYR_DRIVERS_SERIAL_UART_INTEL_LW_H_`。

## 65.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../hardware/P355_UARTIntelLW扩展.md)

---

[上一章](P064_tsl2591.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P066_usb_buf.h_源码浏览.md)
