---
id: learning.zephyr-docs.shell-backend-reference.page-12
title: Shell_UART后端头文件源码
kind: reference
status: maintained
domains: [zephyr, kernel, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/shell__uart_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_Shell\_UART后端头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/shell__uart_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；相关页面见[头文件参考](P011_Shell_UART后端头文件参考.md)和[公共接口](P010_Shell_UART后端接口.md)；访问语义和生命周期见本页译注。

## 12.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="foldopen00106"></a>
<a id="agroup__atomic__apis_html_ga124f07c3a788e53c3a40e4e1c06d8af8"></a>
<a id="agroup__shell__api_html_ga265807c2d8eba7b9ea633968627e085d"></a>
<a id="agroup__shell__uart_html_ga1387a797a3940ff66bfba4af9e48e8d6"></a>
<a id="agroup__shell__uart_html_ga633a97c0298e35127e332df5a9490b0c"></a>
<a id="ashell_2shell_8h_html"></a>
<a id="asmp__shell_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructshell__transport__api_html"></a>
<a id="astructshell_html"></a>
<a id="astructsmp__shell__data_html"></a>
<a id="auart__async__rx_8h_html"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2018 Nordic Semiconductor ASA
<a id="l00003"></a> *
<a id="l00004"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00005"></a> */
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>#ifndef ZEPHYR_INCLUDE_SHELL_SHELL_UART_H_
<a id="l00014"></a>#define ZEPHYR_INCLUDE_SHELL_SHELL_UART_H_
<a id="l00015"></a>
<a id="l00016"></a>#include &lt;zephyr/drivers/serial/uart_async_rx.h&gt;
<a id="l00017"></a>#include &lt;zephyr/mgmt/mcumgr/transport/smp_shell.h&gt;
<a id="l00018"></a>#include &lt;zephyr/shell/shell.h&gt;
<a id="l00019"></a>
<a id="l00020"></a>#ifdef __cplusplus
<a id="l00021"></a>extern "C" {
<a id="l00022"></a>#endif
<a id="l00023"></a>
<a id="l00025"></a>extern const struct shell_transport_api shell_uart_transport_api;
<a id="l00026"></a>
<a id="l00027"></a>#ifndef CONFIG_SHELL_BACKEND_SERIAL_RX_RING_BUFFER_SIZE
<a id="l00028"></a>#define CONFIG_SHELL_BACKEND_SERIAL_RX_RING_BUFFER_SIZE 0
<a id="l00029"></a>#endif
<a id="l00030"></a>
<a id="l00031"></a>#ifndef CONFIG_SHELL_BACKEND_SERIAL_TX_RING_BUFFER_SIZE
<a id="l00032"></a>#define CONFIG_SHELL_BACKEND_SERIAL_TX_RING_BUFFER_SIZE 0
<a id="l00033"></a>#endif
<a id="l00034"></a>
<a id="l00035"></a>#ifndef CONFIG_SHELL_BACKEND_SERIAL_ASYNC_RX_BUFFER_COUNT
<a id="l00036"></a>#define CONFIG_SHELL_BACKEND_SERIAL_ASYNC_RX_BUFFER_COUNT 0
<a id="l00037"></a>#endif
<a id="l00038"></a>
<a id="l00039"></a>#ifndef CONFIG_SHELL_BACKEND_SERIAL_ASYNC_RX_BUFFER_SIZE
<a id="l00040"></a>#define CONFIG_SHELL_BACKEND_SERIAL_ASYNC_RX_BUFFER_SIZE 0
<a id="l00041"></a>#endif
<a id="l00042"></a>
<a id="l00043"></a>#define ASYNC_RX_BUF_SIZE (CONFIG_SHELL_BACKEND_SERIAL_ASYNC_RX_BUFFER_COUNT * \
<a id="l00044"></a>                (CONFIG_SHELL_BACKEND_SERIAL_ASYNC_RX_BUFFER_SIZE + \
<a id="l00045"></a>                 UART_ASYNC_RX_BUF_OVERHEAD))
<a id="l00046"></a>
<a id="l00047"></a>struct shell_uart_common {
<a id="l00048"></a>        const struct device *dev;
<a id="l00049"></a>        shell_transport_handler_t handler;
<a id="l00050"></a>        void *context;
<a id="l00051"></a>        bool blocking_tx;
<a id="l00052"></a>#ifdef CONFIG_MCUMGR_TRANSPORT_SHELL
<a id="l00053"></a>        struct smp_shell_data smp;
<a id="l00054"></a>#endif /* CONFIG_MCUMGR_TRANSPORT_SHELL */
<a id="l00055"></a>};
<a id="l00056"></a>
<a id="l00057"></a>struct shell_uart_int_driven {
<a id="l00058"></a>        struct shell_uart_common common;
<a id="l00059"></a>        struct ring_buf tx_ringbuf;
<a id="l00060"></a>        struct ring_buf rx_ringbuf;
<a id="l00061"></a>        uint8_t tx_buf[CONFIG_SHELL_BACKEND_SERIAL_TX_RING_BUFFER_SIZE];
<a id="l00062"></a>        uint8_t rx_buf[CONFIG_SHELL_BACKEND_SERIAL_RX_RING_BUFFER_SIZE];
<a id="l00063"></a>        struct k_timer dtr_timer;
<a id="l00064"></a>        atomic_t tx_busy;
<a id="l00065"></a>};
<a id="l00066"></a>
<a id="l00067"></a>struct shell_uart_async {
<a id="l00068"></a>        struct shell_uart_common common;
<a id="l00069"></a>        struct k_sem tx_sem;
<a id="l00070"></a>        struct uart_async_rx async_rx;
<a id="l00071"></a>        struct uart_async_rx_config async_rx_config;
<a id="l00072"></a>        atomic_t pending_rx_req;
<a id="l00073"></a>        bool rx_enabled;
<a id="l00074"></a>        uint8_t rx_data[ASYNC_RX_BUF_SIZE];
<a id="l00075"></a>};
<a id="l00076"></a>
<a id="l00077"></a>struct shell_uart_polling {
<a id="l00078"></a>        struct shell_uart_common common;
<a id="l00079"></a>        struct ring_buf rx_ringbuf;
<a id="l00080"></a>        uint8_t rx_buf[CONFIG_SHELL_BACKEND_SERIAL_RX_RING_BUFFER_SIZE];
<a id="l00081"></a>        struct k_timer rx_timer;
<a id="l00082"></a>};
<a id="l00083"></a>
<a id="l00084"></a>#ifdef CONFIG_SHELL_BACKEND_SERIAL_API_POLLING
<a id="l00085"></a>#define SHELL_UART_STRUCT struct shell_uart_polling
<a id="l00086"></a>#elif defined(CONFIG_SHELL_BACKEND_SERIAL_API_ASYNC)
<a id="l00087"></a>#define SHELL_UART_STRUCT struct shell_uart_async
<a id="l00088"></a>#else
<a id="l00089"></a>#define SHELL_UART_STRUCT struct shell_uart_int_driven
<a id="l00090"></a>#endif
<a id="l00092"></a>
<a id="l00099"></a>
<a id="l00106"></a>#define SHELL_UART_DEFINE(_name, ...)                                                              \
<a id="l00107"></a>        static SHELL_UART_STRUCT _name##_shell_uart;                                               \
<a id="l00108"></a>        struct shell_transport _name = {                                                           \
<a id="l00109"></a>                .api = &amp;shell_uart_transport_api,                                                  \
<a id="l00110"></a>                .ctx = (struct shell_telnet *)&amp;_name##_shell_uart,                                 \
<a id="l00111"></a>        }
<a id="l00112"></a>
<a id="l00121"></a>const struct shell *shell_backend_uart_get_ptr(void);
<a id="l00122"></a>
<a id="l00128"></a>struct smp_shell_data *shell_uart_smp_shell_data_get_ptr(void);
<a id="l00129"></a>
<a id="l00131"></a>
<a id="l00132"></a>#ifdef __cplusplus
<a id="l00133"></a>}
<a id="l00134"></a>#endif
<a id="l00135"></a>
<a id="l00136"></a>#endif /* ZEPHYR_INCLUDE_SHELL_SHELL_UART_H_ */
</code></pre>

## 12.2\_可见注释译文（Comments）

1. 版权与许可证：Copyright (c) 2018 Nordic Semiconductor ASA；SPDX-License-Identifier: Apache-2.0。原始法律声明保留。

2. CONFIG_MCUMGR_TRANSPORT_SHELL条件编译结束标记。

3. ZEPHYR_INCLUDE_SHELL_SHELL_UART_H_头文件包含保护结束。

## 12.3\_原页符号提示（Symbol Descriptions）

### `atomic_t`

```c
long atomic_t
```

原子整型变量（Atomic Integer Variable）。

定义位置（Definition）：atomic_types.h:34。

符号定位：[atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)。

### `shell_transport_handler_t`

```c
void(* shell_transport_handler_t)(enum shell_transport_evt evt, void *context)
```

Shell传输事件处理回调（Transport Event Handler Callback）。

定义位置（Definition）：shell.h:831。

符号定位：[shell_transport_handler_t](../shell_core_reference/P001_Shell核心接口.md#ga265807c2d8eba7b9ea633968627e085d)。

### `shell_uart_smp_shell_data_get_ptr`

```c
struct smp_shell_data * shell_uart_smp_shell_data_get_ptr(void)
```

此函数提供UART Shell传输的SMP Shell数据指针。

符号定位：[shell_uart_smp_shell_data_get_ptr](P010_Shell_UART后端接口.md#ga1387a797a3940ff66bfba4af9e48e8d6)。

### `shell_backend_uart_get_ptr`

```c
const struct shell * shell_backend_uart_get_ptr(void)
```

此函数提供Shell UART后端实例的指针。

符号定位：[shell_backend_uart_get_ptr](P010_Shell_UART后端接口.md#ga633a97c0298e35127e332df5a9490b0c)。

### `shell.h`

Shell子系统（Shell Subsystem）的头文件。

符号定位：[shell.h](../shell_core_reference/P002_Shell核心头文件参考.md)。

### `smp_shell.h`

用于mcumgr简单管理协议（SMP）的Shell传输。

符号定位：[smp_shell.h](../shell_management_reference/P008_SMP_Shell头文件参考.md)。

### `uint8_t`

```c
__UINT8_TYPE__ uint8_t
```

定义位置（Definition）：stdint.h:88。

符号定位：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

### `shell_transport_api`

统一的Shell传输接口（Transport Interface）。

定义位置（Definition）：shell.h:864。

符号定位：[shell_transport_api](../shell_core_reference/P010_Shell传输接口结构.md)。

### `shell`

Shell实例内部结构（Instance Internals）。

定义位置（Definition）：shell.h:1129。

符号定位：[shell](../shell_core_reference/P004_Shell实例结构.md)。

### `smp_shell_data`

SMP Shell使用的数据。

定义位置（Definition）：smp_shell.h:33。

符号定位：[smp_shell_data](../shell_management_reference/P010_SMP_Shell运行数据.md)。

### `uart_async_rx.h`

通过UART异步API（Asynchronous API）接收数据的辅助模块。

符号定位：[uart_async_rx.h](../hardware/P344_UART异步接收辅助接口.md)。

## 12.4\_源码跟踪译注

> 译注——UART后端按配置选择轮询（Polling）、异步（Asynchronous）或中断驱动（Interrupt-driven）的上下文结构。原始宏仍保留对struct shell_telnet的指针转换；这不是UART传输被切换成Telnet协议的意思。

> 译注——原文说明DEFINE接受但忽略额外参数以兼容旧版本；不要把被忽略的参数当作当前串口配置。未来移除的表述是官方文档的兼容性说明，不预设具体发行版本。

头文件定位：[include/zephyr/shell/shell_uart.h](../../../include/zephyr/shell/shell_uart.h)，关联实现／接口：[subsys/shell/backends/shell_uart.c](../../../subsys/shell/backends/shell_uart.c)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/shell/shell_uart.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/backends/shell_uart.c)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 12.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P011_Shell_UART后端头文件参考.md)
- [zephyr/drivers/serial/uart_async_rx.h](../hardware/P344_UART异步接收辅助接口.md)
- [zephyr/mgmt/mcumgr/transport/smp_shell.h](../shell_management_reference/P008_SMP_Shell头文件参考.md)
- [zephyr/shell/shell.h](../shell_core_reference/P002_Shell核心头文件参考.md)
- [shell_transport_api](../shell_core_reference/P010_Shell传输接口结构.md)
- [shell_transport_handler_t](../shell_core_reference/P001_Shell核心接口.md#ga265807c2d8eba7b9ea633968627e085d)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [shell](../shell_core_reference/P004_Shell实例结构.md)
- [shell_backend_uart_get_ptr](P010_Shell_UART后端接口.md#ga633a97c0298e35127e332df5a9490b0c)
- [smp_shell_data](../shell_management_reference/P010_SMP_Shell运行数据.md)
- [shell_uart_smp_shell_data_get_ptr](P010_Shell_UART后端接口.md#ga1387a797a3940ff66bfba4af9e48e8d6)

---

[上一章](P011_Shell_UART后端头文件参考.md) · [返回大纲](大纲.md) · [下一章](P013_Shell日志后端头文件参考.md)
