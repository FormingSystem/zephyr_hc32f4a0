---
id: learning.zephyr-docs.api-source-supplement-reference.page-231
title: uart_altera.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/uart__altera_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第231章\_uart\_altera.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/uart__altera_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../hardware/P353_UARTAltera扩展.md)。

## 231.1\_原始可见代码（Source Code）

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

```c
/*
 * Copyright (c) 2023 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_DRIVERS_SERIAL_UART_ALTERA_H_
#define ZEPHYR_DRIVERS_SERIAL_UART_ALTERA_H_

/* End of packet feature.
 * Driver will trigger interrupt upon receiving end of package character.
 * Please enable CONFIG_UART_DRV_CMD and CONFIG_UART_ALTERA_EOP to use this feature.
 * Use the api: uart_drv_cmd with CMD_ENABLE_EOP to enable the feature.
 * This cmd will write the ip register and also set a flag to the driver.
 * The flag will modify uart_irq_callback_user_data_set
 * to set call back function for eop interrupt.
 * Flag is cleared after uart_irq_callback_user_data_set is called.
 */
#define CMD_ENABLE_EOP  0x01
#define CMD_DISABLE_EOP 0x02

#endif /* ZEPHYR_DRIVERS_SERIAL_UART_ALTERA_H_ */
```

## 231.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 14 行

包结束功能（End of packet）。驱动在收到包结束字符时触发中断。要使用此功能，请启用 `CONFIG_UART_DRV_CMD` 和 `CONFIG_UART_ALTERA_EOP`。

通过 API `uart_drv_cmd` 携带 `CMD_ENABLE_EOP` 命令来启用该功能。此命令会写入 IP 寄存器，并在驱动中设置一个标志。该标志改变 `uart_irq_callback_user_data_set` 的行为，使其设置包结束（EOP）中断的回调函数。在调用 `uart_irq_callback_user_data_set` 后，标志被清除。

### 注释 3：原第 26 行

头文件保护宏（Header guard）标记：`ZEPHYR_DRIVERS_SERIAL_UART_ALTERA_H_`。

## 231.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../hardware/P353_UARTAltera扩展.md)

---

[上一章](P230_structs.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P232_uart_mcumgr.h_源码浏览.md)
