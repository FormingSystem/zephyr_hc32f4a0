---
id: learning.zephyr-docs.shell-backend-reference.page-11
title: Shell_UART后端头文件参考
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/shell__uart_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_Shell\_UART后端头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/shell__uart_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入Shell后端选择、虚拟后端、RTT、UART和日志后端的参考与源码。源码跟踪译注与官方原文分开标示。

Shell UART后端（UART Backend）的头文件。

<a id="details"></a>

```c
#include <zephyr/drivers/serial/uart_async_rx.h>
#include <zephyr/mgmt/mcumgr/transport/smp_shell.h>
#include <zephyr/shell/shell.h>
```

查看此文件的源码。

Shell UART后端（UART Backend）的头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 11.1\_宏定义（Macros）

<a id="r_ga9844dc8d28b8d55529af7718d9f78e12"></a>

```c
#define SHELL_UART_DEFINE(_name, ...)
```

相关声明：[SHELL_UART_DEFINE](P010_Shell_UART后端接口.md#ga9844dc8d28b8d55529af7718d9f78e12)。

创建名为_name的Shell UART传输实例的宏。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 11.2\_函数（Functions）

<a id="r_ga633a97c0298e35127e332df5a9490b0c"></a>

```c
const struct shell * shell_backend_uart_get_ptr (void)
```

相关声明：[shell](../shell_core_reference/P004_Shell实例结构.md)、[shell_backend_uart_get_ptr](P010_Shell_UART后端接口.md#ga633a97c0298e35127e332df5a9490b0c)。

此函数提供Shell UART后端实例的指针。

<a id="r_ga1387a797a3940ff66bfba4af9e48e8d6"></a>

```c
struct smp_shell_data * shell_uart_smp_shell_data_get_ptr (void)
```

相关声明：[smp_shell_data](../shell_management_reference/P010_SMP_Shell运行数据.md)、[shell_uart_smp_shell_data_get_ptr](P010_Shell_UART后端接口.md#ga1387a797a3940ff66bfba4af9e48e8d6)。

此函数提供UART Shell传输的SMP Shell数据指针。

## 11.3\_源码定位与版本边界

源码定位：[include/zephyr/shell/shell_uart.h](../../../include/zephyr/shell/shell_uart.h)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中登记的官方main文件。

> 译注——源码核对：UART后端按配置选择轮询（Polling）、异步（Asynchronous）或中断驱动（Interrupt-driven）的上下文结构。原始宏仍保留对struct shell_telnet的指针转换；这不是UART传输被切换成Telnet协议的意思。

> 译注——源码核对：原文说明DEFINE接受但忽略额外参数以兼容旧版本；不要把被忽略的参数当作当前串口配置。未来移除的表述是官方文档的兼容性说明，不预设具体发行版本。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 11.4\_原页交叉引用（Cross References）

- [zephyr/drivers/serial/uart_async_rx.h](https://docs.zephyrproject.org/latest/doxygen/html/uart__async__rx_8h_source.html)
- [zephyr/mgmt/mcumgr/transport/smp_shell.h](../shell_management_reference/P009_SMP_Shell头文件源码.md)
- [zephyr/shell/shell.h](../shell_core_reference/P003_Shell核心头文件源码.md)
- [查看此文件的源码](P012_Shell_UART后端头文件源码.md)
- [SHELL_UART_DEFINE](P010_Shell_UART后端接口.md#ga9844dc8d28b8d55529af7718d9f78e12)
- [shell](../shell_core_reference/P004_Shell实例结构.md)
- [shell_backend_uart_get_ptr](P010_Shell_UART后端接口.md#ga633a97c0298e35127e332df5a9490b0c)
- [smp_shell_data](../shell_management_reference/P010_SMP_Shell运行数据.md)
- [shell_uart_smp_shell_data_get_ptr](P010_Shell_UART后端接口.md#ga1387a797a3940ff66bfba4af9e48e8d6)

<a id="header-details"></a>

---

[上一章](P010_Shell_UART后端接口.md) · [返回大纲](大纲.md) · [下一章](P012_Shell_UART后端头文件源码.md)
