---
id: learning.zephyr-docs.uart-driver-reference.page-3
title: UART内部头文件参考
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/uart__internal_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_UART内部头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/uart__internal_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入UART公共与内部头文件参考和源码浏览页，再通过接口链接进入完整说明。源码跟踪译注与官方原文分开标示。

UART驱动的内部API（Internal APIs）。

<a id="details"></a>

```c
#include <errno.h>
#include <stddef.h>
#include <zephyr/device.h>
```

查看此文件的源码。

UART驱动的内部API（Internal APIs）。

## 3.1\_源码定位与版本边界

相对源码定位：[UART公共头文件](../../../include/zephyr/drivers/uart.h)、[UART内部头文件](../../../include/zephyr/drivers/uart/uart_internal.h)、[系统调用处理](../../../drivers/serial/uart_handlers.c)、[串口配置选项](../../../drivers/serial/Kconfig)和[控制器绑定](../../../dts/bindings/serial/uart-controller.yaml)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：公共声明与内部实现：uart.h定义配置、事件与公共接口，在末尾包含uart/uart_internal.h和生成的syscalls/uart.h。内部头文件中的uart_driver_api及z_impl_*／内联包装负责把调用转交给驱动函数表；普通应用仍以公共头文件为入口。官方内部参考页将这些内容列为INTERNAL_HIDDEN，只有文件说明与源码入口，不能把它当成缺失了公开成员说明；完整可见代码在本册内部源码页保留。

> 译注——源码核对：枚举编码与配置值：UART_LINE_CTRL_*和UART_ERROR_*是位标志（Bit Flags），而数据位、停止位、奇偶校验与流控制枚举采用各自的顺序编码。UART_CFG_DATA_BITS_8不是整数8，不能直接把设备树data-bits数值赋给uart_config.data_bits；应使用对应枚举。uart_config.baudrate按原文字段说明使用bps，实际速率、格式和流控制是否可用取决于驱动及硬件。绑定中的current-speed、hw-flow-control等是初始化配置来源，不等于运行时已成功调用uart_configure。

> 译注——源码核对：三种传输方式：轮询输入（Polling Input）为非阻塞接口，轮询输出（Polling Output）可能等待发送条件。中断驱动（Interrupt-driven）由IRQ回调处理FIFO，异步API（Asynchronous API）由uart_event回调报告传输进度和完成。三类入口、回调签名与配置条件不同。UART_EXCLUSIVE_API_CALLBACKS在异步与中断接口同时启用时默认使两类回调互斥，具体清除动作由相应驱动落实；不能仅因两组选项都启用就假定同一设备可以同时保留两套回调。

> 译注——源码核对：中断处理顺序：官方公共约定要求先在ISR调用uart_irq_update，再查询RX／TX就绪、发送完成或挂起状态。当前uart_irq_update返回void，内部包装在驱动有irq_update操作时才调用它，不能写成依赖其整数返回值的判断。TX就绪时应填充FIFO并检查实际写入数量；RX就绪时持续读取，直至返回数量小于请求数量，避免假定中断一定按电平触发。错误返回应单独处理，不能把负errno当作成功计数或简单布尔真值。

> 译注——源码核对：异步事件与缓冲区：uart_tx／uart_rx_enable返回的是启动结果，完成与数据可用通过事件通知。UART_RX_RDY给出当前缓冲区内从offset开始、长度为len的新数据，不表示缓冲区已释放，同一缓冲区可以出现多次RDY。收到UART_RX_BUF_REQUEST时可提供下一缓冲区；驱动仍在使用的缓冲区不能再次提交，要等UART_RX_BUF_RELEASED后复用。停收或错误可先通知剩余数据，再释放缓冲区，最后报告UART_RX_DISABLED。

> 译注——源码核对：超时与宽数据单位：异步timeout单位为微秒（Microsecond），TX超时按原约定仅在流控制启用时有效；RX超时是至少收到一个字节后的不活动间隔，没有收到数据时不会单凭该间隔产生RDY。SYS_FOREVER_US禁用超时。带_u16接口以uint16_t容纳宽数据，FIFO与异步传输长度按数据项计；用户态校验也采用len乘sizeof(uint16_t)检查数组范围，不能把len直接当作字节数。公开事件字段的字节措辞按原文保留，宽数据场景仍须核对具体驱动的事件填充。

> 译注——源码核对：错误与空操作边界：运行时配置、线路控制、驱动命令、FIFO及多数中断状态查询，在对应功能未启用时返回-ENOTSUP；已启用但所检查的操作指针为空时返回-ENOSYS。部分void中断使能／禁用包装在缺少操作时不做任何事，宽数据轮询输出在功能未启用时同样为空操作。poll_out以及异步TX、RX和缓冲区提交包装在已编译分支中直接调用相应操作，不统一执行空指针检查。应按所用入口及设备能力判断，不能把一处检查推广给所有UART API。

> 译注——源码核对：用户态与回调边界：uart_handlers.c为系统调用核对设备对象／操作权限及输入输出缓冲区可访问范围；这些校验不代表内核内联包装也自动拥有相同检查。回调安装与rx_buf_rsp未提供同类系统调用入口，原注释明确回调安装不允许来自用户态，缓冲区响应用于ISR回调。自定义驱动命令的cmd是UART命令参数；原Doxygen页面将同名符号链接到显示协处理器函数，相关符号提示按原文保留，该交叉引用不意味着UART具有显示命令功能。

> 译注——源码核对：版本边界：本批核对公共与内部两个头文件、UART系统调用处理、串口Kconfig和公共控制器绑定，共五份官方源码并记录摘要。两份源码浏览页的非注释代码分别与读取的官方原始头文件一致；latest、滚动main与仓库参照版本不自动相同。仓库定位使用相对路径，本次未构建固件、打开串口、发送数据或操作硬件。

本次验证范围为文档与源码对照，未构建固件、打开串口或操作硬件。

## 3.2\_原页交叉引用（Cross References）

- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码](P004_UART内部头文件源码.md)

<a id="header-details"></a>

---

[上一章](P002_UART驱动头文件源码.md) · [返回大纲](大纲.md) · [下一章](P004_UART内部头文件源码.md)
