---
id: learning.zephyr-docs.usb.page-12
title: USBC供电端示例
kind: reference
status: maintained
domains: [zephyr, usb, driver]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/usb_c/source/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_USBC供电端示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/usb_c/source/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 12.1\_概述

本示例展示如何使用 USB-C 子系统创建 USB 电力传输（USB Power Delivery，USB PD）应用，实现一个 USB-C 供电端（Source）设备。

将 USB-C 受电端（Sink）设备接入后，双方协商由 Source 提供 5 V／100 mA、9 V／100 mA 或 15 V／100 mA，并显示请求数据对象（RDO；原页此处写作 Requested Data Object）。原文把这个对象描述为“由 Source 提供”。

> 译注：上述发送方描述有误。请求数据对象的通用名称为 Request Data Object；当前官方实现通过 `port0_policy_cb_check_sink_request()` 接收 Sink 发来的 `request_msg`，保存到 `sink_request`，然后由 `dump_sink_request_rdo()` 打印。Source 通告供电能力 PDO，Sink 发送选择能力的 RDO，二者方向应区分。

## 12.2\_要求

示例使用的 Type-C 端口控制器（Type-C Port Controller，TCPC）由设备树中兼容标识为 `usb-c-connector` 的节点指定。官方说明本示例已在 `stm32g081b_eval` 上测试，并提供对应覆盖文件（Overlay）。

> 译注：当前[开发板覆盖文件](../../../samples/subsys/usb_c/source/boards/stm32g081b_eval.overlay)设置 `power-role = "source"`，列出三个固定供电 PDO，并关联 TCPC、VBUS 测量和电源控制设备。实际电压由公共电源控制实现处理，声明 PDO 本身不会凭空赋予硬件供电能力。

## 12.3\_构建与运行

按下列命令构建和烧录，将 `stm32g081b_eval` 改成所用开发板：

```bash
west build -b stm32g081b_eval samples/subsys/usb_c/source
west flash
```

> 译注：从所使用的 Zephyr 源码根目录执行，需要工具链、目标板配置、电源控制硬件及烧录工具就绪。移到其他板卡时先完成相应适配，不能只替换板名；构建成功后才进入烧录步骤。本批没有执行构建、烧录或改变端口电压。

连接一个受电端设备，观察控制台输出。

### 12.3.1\_示例输出

```text
PRL_TX_SUSPEND
PRL_HR_SUSPEND
PE_SUSPEND
UnattachedWait.SRC
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
PE_SRC_Discover
PE_SRC_Send_Capabilities
PRL_Tx_Wait_for_PHY_response
RECV 1042/1
   [0]1300280a
PRL_Tx_Wait_for_Message_Request
PE_SRC_Negotiate_Capability
PE_SRC_Transition_Supply
PRL_Tx_Wait_for_PHY_response
RECV 0441/0
PRL_Tx_Wait_for_Message_Request
PE_SRC_Ready
PRL_Tx_Wait_for_PHY_response
RECV 0641/0
PRL_Tx_Wait_for_Message_Request
REQUEST RDO: 1300280a
 Object Position:         1
 Giveback:                0
 Capability Mismatch:     0
 USB Comm Capable:        1
 No USB Suspend:          1
 Unchunk Ext MSG Support: 0
 Operating Current:       100 mA
 Min Operating Current:   100 mA
```

> 译注：`Attached.SRC` 表示以供电端身份建立连接；`PE_SRC_Send_Capabilities`、`PE_SRC_Negotiate_Capability`、`PE_SRC_Transition_Supply`、`PE_SRC_Ready` 对应策略引擎（Policy Engine，PE）的能力通告、协商、供电转换和就绪阶段。`REQUEST RDO` 为接收到的请求，`Object Position: 1` 选择第一个 PDO，`Operating Current` 为工作电流。

> 译注：日志同时写 `Giveback: 0` 和 `Min Operating Current`；按官方源码该字段名为 `min_or_max_operating_current`，Sink 示例的 `build_rdo()` 注释说明 GiveBack 为 0 时表示最大工作电流。本次读取的 `dump_sink_request_rdo()` 也使用了这个打印标签，但它与上述字段语义不一致，不能仅按标签把它认定为最小工作电流。原日志标签、十六进制数据和数值保持不变。

## 12.4\_参见

[USB-C 设备 API](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html)。


译注核对来源：[samples/subsys/usb_c/source/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb_c/source/src/main.c)、[samples/subsys/usb_c/source/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb_c/source/prj.conf)、[samples/subsys/usb_c/source/tests.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb_c/source/tests.yaml)、[samples/subsys/usb_c/source/boards/stm32g081b_eval.overlay](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb_c/source/boards/stm32g081b_eval.overlay)、[samples/subsys/usb_c/common/power_ctrl.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb_c/common/power_ctrl.c)、[samples/subsys/usb_c/common/power_ctrl.h](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb_c/common/power_ctrl.h)、[samples/subsys/usb_c/sink/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb_c/sink/src/main.c)。

本仓库的[对应源码](../../../samples/subsys/usb_c/source/src/main.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="usb-c-source"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="usb-c-source-sample-requirements"></a>
<a id="building-and-running"></a>
<a id="sample-output"></a>
<a id="see-also"></a>

[上一章](P011_USBC受电端示例.md) · [返回大纲](大纲.md) · [下一章](P013_USB设备API目录.md)
