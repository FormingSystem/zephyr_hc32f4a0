---
id: learning.zephyr-docs.usb.page-11
title: USBC受电端示例
kind: reference
status: maintained
domains: [zephyr, usb, driver]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/usb_c/sink/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_USBC受电端示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/usb_c/sink/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 11.1\_概述

本示例展示如何使用 USB-C 子系统创建 USB 电力传输（USB Power Delivery，USB PD）应用，以及如何生成 XML 格式的 USB 厂商信息文件（Vendor Info File，VIF）策略。应用实现一个 USB-C 受电端（Sink）设备。

把该设备接到支持 Power Delivery 的充电器后，它与充电器协商取得 5 V／100 mA，并显示充电器提供的全部电力数据对象（Power Data Object，PDO）。

> 译注：原页将 PDO 写为 Power Delivery Objects；对应协议及源码中的通用名称为 Power Data Object。显示充电器的全部能力与实际请求的供电条件是两回事；当前 `build_rdo()` 选择对象位置 1，并把工作电流与最大工作电流都设置为 100 mA。

## 11.2\_要求

示例使用的 Type-C 端口控制器（Type-C Port Controller，TCPC）由设备树中兼容标识为 `usb-c-connector` 的节点指定。官方说明已经在[B-G474E-DPOW1 Discovery](https://docs.zephyrproject.org/latest/boards/st/b_g474e_dpow1/doc/index.html#b_g474e_dpow1)和[STM32G081B Evaluation](https://docs.zephyrproject.org/latest/boards/st/stm32g081b_eval/doc/index.html#stm32g081b_eval)上测试，并提供这两块开发板的覆盖文件（Overlay）。

## 11.3\_构建与运行

按下列命令构建和烧录，将 `b_g474e_dpow1` 替换为所用开发板：

```bash
west build -b b_g474e_dpow1 samples/subsys/usb_c/sink
west flash
```

> 译注：从所使用的 Zephyr 源码根目录执行，先准备目标工具链、实际开发板、对应 TCPC／VBUS 设备配置和烧录工具。换一个板名并不能代替设备树和硬件适配；构建失败应先排查这些前提。本批没有执行命令或连接充电器。

连接充电器，观察控制台输出。

### 11.3.1\_示例输出

```text
Unattached.SNK
AttachWait.SNK
Attached.SNK
PE_SNK_Startup
PRL_INIT
PRL_HR_Wait_for_Request
PRL_Tx_PHY_Layer_Reset
PRL_Tx_Wait_for_Message_Request
PE_SNK_Discovery
PE_SNK_Wait_For_Capabilities
RECV 4161/4 [0]0a01912c [1]0002d12c [2]0004b12c [3]000640e1
PE_SNK_Evaluate_Capability
PE_SNK_Select_Capability
PRL_Tx_Wait_for_PHY_response
PWR 3A0

RECV 0363/0
PRL_Tx_Wait_for_Message_Request
PE_SNK_Transition_Sink
RECV 0566/0
Source Caps:
PDO 0:
       Type:              FIXED
       Current:           3000
       Voltage:           5000
       Peak Current:      0
       Uchunked Support:  0
       Dual Role Data:    1
       USB Comms:         0
       Unconstrained Pwr: 1
       USB Susspend:      0
       Dual Role Power:   0
PDO 1:
       Type:              FIXED
       Current:           3000
       Voltage:           9000
       Peak Current:      0
       Uchunked Support:  0
       Dual Role Data:    0
       USB Comms:         0
       Unconstrained Pwr: 0
       USB Susspend:      0
       Dual Role Power:   0
PDO 2:
       Type:              FIXED
       Current:           3000
       Voltage:           15000
       Peak Current:      0
       Uchunked Support:  0
       Dual Role Data:    0
       USB Comms:         0
       Unconstrained Pwr: 0
       USB Susspend:      0
       Dual Role Power:   0
PDO 3:
       Type:              FIXED
       Current:           2250
       Voltage:           20000
       Peak Current:      0
       Uchunked Support:  0
       Dual Role Data:    0
       USB Comms:         0
       Unconstrained Pwr: 0
       USB Susspend:      0
       Dual Role Power:   0
PE_SNK_Ready
```

> 译注：`Unattached.SNK`、`AttachWait.SNK`、`Attached.SNK` 分别表示未连接、等待确认连接、已作为受电端连接；`PE_SNK_*` 是受电端策略引擎（Policy Engine，PE）的状态。`PRL_*` 为协议层（Protocol Layer，PRL）状态，`RECV` 表示接收消息。`Source Caps` 后列出的 `Current` 为 mA、`Voltage` 为 mV，因此 3000／5000 表示伙伴的 3 A／5 V 能力，不是样例实际汲取 3 A 的证据。

> 译注：原始输出中的 `Uchunked Support`、`USB Susspend` 等拼写照实保留，以便与原页对照；其含义分别对应未分块消息支持、USB 挂起。版本、日志配置和充电器不同，输出可以变化，不能将本页历史日志当作本机测试结果。

### 11.3.2\_VIF生成过程译注

当前官方 `prj.conf` 启用 `CONFIG_BUILD_OUTPUT_VIF=y`，示例目录中提供输入文件 `vif.xml`。[VIF 构建规则](../../../cmake/vif.cmake)将设备树解析结果与输入 XML 交给生成器，构建注释标示输出为 `zephyr/vif.xml`，实际输出位置由构建目录中的 `PROJECT_BINARY_DIR` 决定。

该 XML 是构建阶段生成的策略描述，不是上面控制台日志的内容，也不需要在运行中的设备上等待生成。这里只核对配置和生成规则，没有实际生成文件。输入路径及其他细节以所用源码版本为准。

## 11.4\_参见

[USB-C 设备 API](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html)。


译注核对来源：[samples/subsys/usb_c/sink/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb_c/sink/src/main.c)、[samples/subsys/usb_c/sink/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb_c/sink/prj.conf)、[samples/subsys/usb_c/sink/tests.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb_c/sink/tests.yaml)、[samples/subsys/usb_c/sink/boards/stm32g081b_eval.overlay](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb_c/sink/boards/stm32g081b_eval.overlay)、[samples/subsys/usb_c/sink/boards/b_g474e_dpow1.overlay](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb_c/sink/boards/b_g474e_dpow1.overlay)、[samples/subsys/usb_c/sink/vif.xml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb_c/sink/vif.xml)、[cmake/vif.cmake](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/cmake/vif.cmake)。

本仓库的[对应源码](../../../samples/subsys/usb_c/sink/src/main.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="usb-c-sink"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="usb-c-sink-sample-requirements"></a>
<a id="building-and-running"></a>
<a id="sample-output"></a>
<a id="see-also"></a>

[上一章](P010_USBC双电源角色示例.md) · [返回大纲](大纲.md) · [下一章](P012_USBC供电端示例.md)
