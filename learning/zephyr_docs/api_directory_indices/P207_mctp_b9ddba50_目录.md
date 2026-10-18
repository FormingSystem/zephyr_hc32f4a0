---
id: learning.zephyr-docs.api-directory-indices.page-207
title: mctp目录参考（Directory Reference）
kind: reference
status: maintained
domains: [zephyr, documentation, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dir_b9ddba50a558f73fa88aca7b5c7fba37.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；章节编号和导航为本地新增。 -->

# 第207章\_mctp目录参考（Directory Reference）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dir_b9ddba50a558f73fa88aca7b5c7fba37.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

官方目录层次：`zephyr/pmci/mctp`。

条目说明采用中文译文并附英文原文，便于核对术语与接口；文件名、类型名和符号保持原样。目录树已完整展开，原页的折叠控件不参与本地静态阅读。

<div>
<table>
<tr><td colspan="2"><h2><a id="header-files"></a><span data-translation="0">文件（Files）。</span><br><small lang="en" data-source-prose="0"><a id="files"></a>
Files</small></h2>
</td></tr>

<tr><td><a id="r_mctp_5Fi2c_5Fgpio_5Fcommon_2Eh"></a><a href="https://docs.zephyrproject.org/latest/doxygen/html/mctp__i2c__gpio__common_8h_source.html">源码（Source）</a> </td><td><a href="https://docs.zephyrproject.org/latest/doxygen/html/mctp__i2c__gpio__common_8h.html">mctp_i2c_gpio_common.h</a></td></tr>

<tr><td> </td><td><span data-translation="1">MCTP I2C GPIO控制器与目标绑定（Controller and Target Bindings）共享的内部定义。</span><br><small lang="en" data-source-prose="1">Internal definitions shared by the MCTP I2C GPIO controller and target bindings. <br></small></td></tr>

<tr><td><a id="r_mctp_5Fi2c_5Fgpio_5Fcontroller_2Eh"></a><a href="https://docs.zephyrproject.org/latest/doxygen/html/mctp__i2c__gpio__controller_8h_source.html">源码（Source）</a> </td><td><a href="https://docs.zephyrproject.org/latest/doxygen/html/mctp__i2c__gpio__controller_8h.html">mctp_i2c_gpio_controller.h</a></td></tr>

<tr><td> </td><td><span data-translation="2">基于I2C并使用GPIO传递信号的MCTP总线绑定（Bus Binding），用于控制器端。</span><br><small lang="en" data-source-prose="2">MCTP bus binding over I2C with GPIO signaling, controller side. <br></small></td></tr>

<tr><td><a id="r_mctp_5Fi2c_5Fgpio_5Ftarget_2Eh"></a><a href="https://docs.zephyrproject.org/latest/doxygen/html/mctp__i2c__gpio__target_8h_source.html">源码（Source）</a> </td><td><a href="https://docs.zephyrproject.org/latest/doxygen/html/mctp__i2c__gpio__target_8h.html">mctp_i2c_gpio_target.h</a></td></tr>

<tr><td> </td><td><span data-translation="3">基于I2C并使用GPIO传递信号的MCTP总线绑定（Bus Binding），用于目标端。</span><br><small lang="en" data-source-prose="3">MCTP bus binding over I2C with GPIO signaling, target side. <br></small></td></tr>

<tr><td><a id="r_mctp_5Fi3c_5Fcommon_2Eh"></a><a href="https://docs.zephyrproject.org/latest/doxygen/html/mctp__i3c__common_8h_source.html">源码（Source）</a> </td><td><a href="https://docs.zephyrproject.org/latest/doxygen/html/mctp__i3c__common_8h.html">mctp_i3c_common.h</a></td></tr>

<tr><td> </td><td><span data-translation="4">MCTP I3C控制器与目标绑定（Controller and Target Bindings）共享的内部定义。</span><br><small lang="en" data-source-prose="4">Internal definitions shared by the MCTP I3C controller and target bindings. <br></small></td></tr>

<tr><td><a id="r_mctp_5Fi3c_5Fcontroller_2Eh"></a><a href="https://docs.zephyrproject.org/latest/doxygen/html/mctp__i3c__controller_8h_source.html">源码（Source）</a> </td><td><a href="https://docs.zephyrproject.org/latest/doxygen/html/mctp__i3c__controller_8h.html">mctp_i3c_controller.h</a></td></tr>

<tr><td> </td><td><span data-translation="5">基于I3C并使用带内中断（IBI）传递信号的MCTP总线绑定，用于控制器端。</span><br><small lang="en" data-source-prose="5">MCTP bus binding over I3C using IBI signaling, controller side. <br></small></td></tr>

<tr><td><a id="r_mctp_5Fi3c_5Fendpoint_2Eh"></a><a href="https://docs.zephyrproject.org/latest/doxygen/html/mctp__i3c__endpoint_8h_source.html">源码（Source）</a> </td><td><a href="https://docs.zephyrproject.org/latest/doxygen/html/mctp__i3c__endpoint_8h.html">mctp_i3c_endpoint.h</a></td></tr>

<tr><td> </td><td><span data-translation="6">MCTP I3C端点设备（Endpoint Devices）的内部驱动API。</span><br><small lang="en" data-source-prose="6">Internal driver API for MCTP I3C endpoint devices. <br></small></td></tr>

<tr><td><a id="r_mctp_5Fi3c_5Fpec_2Eh"></a><a href="https://docs.zephyrproject.org/latest/doxygen/html/mctp__i3c__pec_8h_source.html">源码（Source）</a> </td><td><a href="https://docs.zephyrproject.org/latest/doxygen/html/mctp__i3c__pec_8h.html">mctp_i3c_pec.h</a></td></tr>

<tr><td> </td><td><span data-translation="7">基于I3C的MCTP数据包错误码（Packet Error Code，PEC）的辅助接口。</span><br><small lang="en" data-source-prose="7">MCTP-over-I3C Packet Error Code (PEC) helpers. <br></small></td></tr>

<tr><td><a id="r_mctp_5Fi3c_5Ftarget_2Eh"></a><a href="https://docs.zephyrproject.org/latest/doxygen/html/mctp__i3c__target_8h_source.html">源码（Source）</a> </td><td><a href="https://docs.zephyrproject.org/latest/doxygen/html/mctp__i3c__target_8h.html">mctp_i3c_target.h</a></td></tr>

<tr><td> </td><td><span data-translation="8">基于I3C并使用带内中断（IBI）传递信号的MCTP总线绑定，用于目标端。</span><br><small lang="en" data-source-prose="8">MCTP bus binding over I3C using IBI signaling, target side. <br></small></td></tr>

<tr><td><a id="r_mctp_5Fmemory_2Eh"></a><a href="https://docs.zephyrproject.org/latest/doxygen/html/mctp__memory_8h_source.html">源码（Source）</a> </td><td><a href="https://docs.zephyrproject.org/latest/doxygen/html/mctp__memory_8h.html">mctp_memory.h</a></td></tr>

<tr><td> </td><td><span data-translation="9">MCTP内存管理函数（Memory Management Functions）。</span><br><small lang="en" data-source-prose="9">MCTP memory management functions. <br></small></td></tr>

<tr><td><a id="r_mctp_5Fuart_2Eh"></a><a href="https://docs.zephyrproject.org/latest/doxygen/html/mctp__uart_8h_source.html">源码（Source）</a> </td><td><a href="https://docs.zephyrproject.org/latest/doxygen/html/mctp__uart_8h.html">mctp_uart.h</a></td></tr>

<tr><td> </td><td><span data-translation="10">基于Zephyr异步UART接口的MCTP总线绑定（Bus Binding）。</span><br><small lang="en" data-source-prose="10">MCTP bus binding over the Zephyr asynchronous UART interface. <br></small></td></tr>

<tr><td><a id="r_mctp_5Fusb_2Eh"></a><a href="https://docs.zephyrproject.org/latest/doxygen/html/mctp__usb_8h_source.html">源码（Source）</a> </td><td><a href="https://docs.zephyrproject.org/latest/doxygen/html/mctp__usb_8h.html">mctp_usb.h</a></td></tr>

<tr><td> </td><td><span data-translation="11">基于Zephyr USB设备协议栈的MCTP总线绑定（Bus Binding）。</span><br><small lang="en" data-source-prose="11">MCTP bus binding over the Zephyr USB device stack. <br></small></td></tr>

</table>

</div>


---

[上一章](P206_dap_b9947f80_目录.md) · [返回大纲](大纲.md) · [下一章](P208_conn_mgr_ba7fd4b3_目录.md)
