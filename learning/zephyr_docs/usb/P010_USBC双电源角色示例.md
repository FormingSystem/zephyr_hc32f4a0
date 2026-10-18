---
id: learning.zephyr-docs.usb.page-10
title: USBC双电源角色示例
kind: reference
status: maintained
domains: [zephyr, usb, driver]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/usb_c/drp/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_USBC双电源角色示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/usb_c/drp/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 10.1\_概述

本示例展示如何使用 USB-C 子系统创建 USB 电力传输（USB Power Delivery，USB PD）应用。应用实现一个 USB-C 双电源角色（Dual Role Power，DRP）设备，既可以作为供电端（Source），也可以作为受电端（Sink）。

未连接设备时，DRP 设备按照配置的周期和占空比在 Source 与 Sink 角色之间切换。接入设备后，DRP 从端口伙伴的配置通道（Configuration Channel，CC）线上读取电阻通告（Rd/Rp），识别供电角色，并启动相应的策略引擎（Policy Engine，PE）状态机：Sink 使用 `usbc_pe_snk_states`，Source 使用 `usbc_pe_src_states`。它可以作为 Source 提供 5 V／100 mA、9 V／100 mA 或 15 V／100 mA，也可以作为 Sink 取得 5 V／100 mA。

> 译注：当前官方 `prj.conf` 选择 `CONFIG_USBC_CSM_DRP`，周期为 75 ms、Source 占空比为 50%；设备树设置 `power-role = "dual"` 并同时列出两类电源能力。这个切换行为用于未连接阶段识别伙伴。当前 `port0_policy_check()` 对 `CHECK_POWER_ROLE_SWAP` 返回 `false`，因此不能把“支持 DRP”理解为此示例接受连接后的供电角色交换。

## 10.2\_要求

示例使用的 Type-C 端口控制器（Type-C Port Controller，TCPC）由设备树中兼容标识为 `usb-c-connector` 的节点指定。官方说明此示例已经在 `stm32g081b_eval` 上测试，并提供了设备树覆盖文件（Devicetree Overlay）。

## 10.3\_硬件配置

本示例使用 `stm32g081b_eval` 与 UCPD 子板之间的固定硬件连接控制电源，包括 VBUS 供电使能、DC-DC 使能、VCONN 使能和 VBUS 放电控制。具体引脚分配及功能定义在开发板覆盖文件中。详细引脚映射请参阅 STM32G081B-EVAL 开发板数据手册和 UCPD 子板文档。

> 译注：这些是官方示例的板卡前提，不是要求给其他板卡照搬引脚。对应的[覆盖文件](../../../samples/subsys/usb_c/drp/boards/stm32g081b_eval.overlay)和[电源控制实现](../../../samples/subsys/usb_c/common/power_ctrl.c)可用来跟踪电压选择、VCONN 和放电控制；本仓库源码与当前官方版本可能不同。这里没有翻译或引入仓库内的芯片手册。

## 10.4\_构建与运行

按下列命令构建和烧录，将 `stm32g081b_eval` 改成所用开发板：

```bash
west build -b stm32g081b_eval samples/subsys/usb_c/drp
west flash
```

> 译注：命令从所使用的 Zephyr 源码根目录执行，前提是工具链、目标板支持、相应覆盖文件与烧录工具已经就绪。更改板名并不会自动补齐 TCPC、电源控制与实际连线；应先核对前两节要求。构建失败时先处理配置或编译错误，不继续执行 `west flash`。本批仅翻译，没有执行构建、烧录或电源操作。

连接一个 Source 或 Sink 设备，观察控制台输出。

### 10.4.1\_作为受电端的示例输出

```text
# DRP Toggling ...
Unattached.SNK
Unattached.SRC
Unattached.SNK
Unattached.SRC
# Attach Source Device
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
RECV 61a1/6
   [0]0a01912c
   [1]0002d12c
   [2]0003c12c
   [3]0004b12c
   [4]000641f4
   [5]c1a42164
PE_SNK_Evaluate_Capability
PE_SNK_Select_Capability
PRL_Tx_Wait_for_PHY_response
RECV 0161/0
PRL_Tx_Wait_for_Message_Request
RECV 03a3/0
PE_SNK_Transition_Sink
RECV 05a6/0
PE_SNK_Ready
Source Caps:
PDO 0:0x0a01912c
 Type:                FIXED
 Current:             3000
 Voltage:             5000
 Peak Current:        0
 Uchunked Support:    0
 Dual Role Data:      1
 USB Comms:           0
 Unconstrained Pwr:   1
 USB Suspend:         0
 Dual Role Power:     0
PDO 1:0x0002d12c
 Type:                FIXED
 Current:             3000
 Voltage:             9000
 Peak Current:        0
 Uchunked Support:    0
 Dual Role Data:      0
 USB Comms:           0
 Unconstrained Pwr:   0
 USB Suspend:         0
 Dual Role Power:     0
PDO 2:0x0003c12c
 Type:                FIXED
 Current:             3000
 Voltage:             12000
 Peak Current:        0
 Uchunked Support:    0
 Dual Role Data:      0
 USB Comms:           0
 Unconstrained Pwr:   0
 USB Suspend:         0
 Dual Role Power:     0
PDO 3:0x0004b12c
 Type:                FIXED
 Current:             3000
 Voltage:             15000
 Peak Current:        0
 Uchunked Support:    0
 Dual Role Data:      0
 USB Comms:           0
 Unconstrained Pwr:   0
 USB Suspend:         0
 Dual Role Power:     0
PDO 4:0x000641f4
 Type:                FIXED
 Current:             5000
 Voltage:             20000
 Peak Current:        0
 Uchunked Support:    0
 Dual Role Data:      0
 USB Comms:           0
 Unconstrained Pwr:   0
 USB Suspend:         0
 Dual Role Power:     0
PDO 5:0xc1a42164
 Type:                AUGMENTED
 Min Voltage:         3300
 Max Voltage:         21000
 Max Current:         5000
 PPS Power Limited:   0
```

> 译注：前几行显示未连接时在 `Unattached.SNK` 与 `Unattached.SRC` 间切换；接入 Source 后，依次进入等待连接、已连接和受电端协商状态。`Source Caps` 是对端通告的供电能力，电力数据对象（Power Data Object，PDO）列表中的 `Current`／`Voltage` 分别以 mA／mV 显示。对端提供 3 A 或 5 A 等能力，不表示本示例已请求这么大的电流；当前受电端 `build_rdo()` 请求第一个 5 V PDO、100 mA。

原日志中的 `FIXED` 为固定电源类型，`AUGMENTED` 为扩展类型；最后一个对象显示可编程电源（Programmable Power Supply，PPS）的最小／最大电压及最大电流。此段为日志字段译注，原始拼写和数值未改写。

### 10.4.2\_作为供电端的示例输出

```text
# DRP Toggling ...
Unattached.SRC
Unattached.SNK
Unattached.SRC
Unattached.SNK
# Attach Sink Device
Unattached.SRC
AttachWait.SRC
Attached.SRC
PE_SRC_Startup
PRL_INIT
PRL_HR_Wait_for_Request
PRL_Tx_PHY_Layer_Reset
PRL_Tx_Wait_for_Message_Request
PE_SRC_Send_Capabilities
PRL_Tx_Wait_for_PHY_response
PRL_Tx_Wait_for_Message_Request
PE_SRC_Discovery
PE_SRC_Send_Capabilities
PRL_Tx_Wait_for_PHY_response
PRL_Tx_Wait_for_Message_Request
PE_SRC_Discovery
PE_SRC_Send_Capabilities
PRL_Tx_Wait_for_PHY_response
RECV 0a41/0
PRL_Tx_Wait_for_Message_Request
RECV 1082/1
   [0]1680292c
PE_SRC_Negotiate_Capability
PE_SRC_Transition_Supply
PRL_Tx_Wait_for_PHY_response
RECV 0c41/0
PRL_Tx_Wait_for_Message_Request
RDO :0x1680292c
 Type:                FIXED
 Object Position:     1
 Giveback:            0
 Capability Mismatch: 1
 USB Comm Capable:    1
 No USB Suspend:      0
 Unchunk Ext MSG Support: 1
 Operating Current:   100 mA
PE_SRC_Ready
```

> 译注：接入 Sink 后，设备进入 `Attached.SRC`，发送供电能力、接收请求，再进入供电转换和就绪状态。请求数据对象（Request Data Object，RDO）的 `Object Position` 指向所选 PDO，`Operating Current` 是请求的工作电流；`Capability Mismatch` 为能力不匹配标志。这里的输出是官方例子，实际状态次序、伙伴能力与日志细节取决于连接设备及所用版本。

## 10.5\_参见

[USB-C 设备 API](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html)。


译注核对来源：[samples/subsys/usb_c/drp/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb_c/drp/src/main.c)、[samples/subsys/usb_c/drp/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb_c/drp/prj.conf)、[samples/subsys/usb_c/drp/tests.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb_c/drp/tests.yaml)、[samples/subsys/usb_c/drp/boards/stm32g081b_eval.overlay](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb_c/drp/boards/stm32g081b_eval.overlay)、[samples/subsys/usb_c/common/power_ctrl.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb_c/common/power_ctrl.c)、[samples/subsys/usb_c/common/power_ctrl.h](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb_c/common/power_ctrl.h)。

本仓库的[对应源码](../../../samples/subsys/usb_c/drp/src/main.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="usb-c-drp"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="usb-c-drp-sample-requirements"></a>
<a id="hardware-configuration"></a>
<a id="building-and-running"></a>
<a id="sample-sink-output"></a>
<a id="sample-source-output"></a>
<a id="see-also"></a>

[上一章](P009_USBC示例目录.md) · [返回大纲](大纲.md) · [下一章](P011_USBC受电端示例.md)
