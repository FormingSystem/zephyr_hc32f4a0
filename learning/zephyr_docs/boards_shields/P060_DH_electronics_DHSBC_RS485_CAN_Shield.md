---
id: learning.zephyr-docs.boards-shields.page-60
title: DH electronics DHSBC RS485 CAN Shield
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/dhsbc_rs485_can_shield/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="dh-electronics-dhsbc-rs485-can-shield"></a>

<a id="dhsbc-rs485-can-shield"></a>

# 第60章\_DH electronics DHSBC RS485 CAN扩展板（Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/dhsbc_rs485_can_shield/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

DHSBC RS485 CAN扩展板兼容DHSBC STM32MP25，可直接通过40针排针连接单板计算机。它提供最高500 kbit/s的RS485及最高5 Mbit/s的CAN FD，信号经picoMAX连接器引出。

<a id="id3"></a>

<a id="id5"></a>

更多信息见DHSBC RS485 CAN扩展板主页[注1](#id2)及用户手册[注2](#id4)。（[DHSBC RS485 CAN 扩展板 主页](https://www.dh-electronics.com/en/embedded-products/development-carrier-boards/detail/dhsbc-rs-485-can-shield)；[DHSBC RS485 CAN 扩展板 用户手册](https://www.dh-electronics.com/en/download/file/downloads/USM_DHSBC-RS485-CAN-Shield.pdf)）

<a id="id1"></a>

![官方原图：DHSBC RS485 CAN Shield](images/dhsbc_rs485_can_shield.webp)

DHSBC RS485 CAN扩展板

RS485部分以zephyr,modbus-serial兼容字符串建模为Modbus RTU串口后端，驱动方向控制连接树莓派排针信号。


- GPIO17，第5脚，用作驱动使能DE
- GPIO16，第24脚，用作低有效接收使能RE

扩展板没有独立CAN控制器，直接使用SoC集成控制器，板上只有CAN收发器。


- GPIO23，第9脚，用作CAN-TX
- GPIO24，第10脚，用作CAN-RX

<a id="requirements"></a>

## 前置要求（Requirements）

RS485部分要求开发板提供以下树莓派排针别名：


- `raspberrypi_serial`
- `raspberrypi_header`

树莓派连接器没有规定CAN信号，因此每块开发板的覆盖文件必须提供CAN收发器节点，见[boards/shields/dhsbc_rs485_can_shield/boards/stm32mp255c_dhsbc_stm32mp255cxx_m33.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/dhsbc_rs485_can_shield/boards/stm32mp255c_dhsbc_stm32mp255cxx_m33.overlay)。

插座选择由开发板DTS别名控制，详情见“[扩展板（Shields）](https://docs.zephyrproject.org/latest/hardware/porting/shields.html#shields)”。

<a id="programming"></a>

## 编程（Programming）

调用west build时将扩展板设为dhsbc_rs485_can_shield。

<a id="example-can"></a>

### CAN示例

```text
# From the root of the zephyr repository
west build -b stm32mp255c_dhsbc/stm32mp255cxx/m33 --shield dhsbc_rs485_can_shield samples/drivers/can/babbling
```

<a id="example-rs-485"></a>

### RS-485示例

Modbus RTU服务器示例需要3个LED，但本扩展板未配置LED；它引出了全部树莓派引脚，因此可在排针外接LED。覆盖文件定义如下：


- GPIO26，第25脚，用作LD1
- GPIO20，第26脚，用作LD2
- GPIO21，第27脚，用作LD3

Modbus RTU服务器示例的app.overlay假定Arduino排针，因此必须将其排除在构建之外；将DTC_OVERLAY_FILE设为空字符串即可。

```text
# From the root of the zephyr repository
west build -b stm32mp255c_dhsbc/stm32mp255cxx/m33 --shield dhsbc_rs485_can_shield samples/subsys/modbus/rtu_server -- -DDTC_OVERLAY_FILE=
```


---

<a id="references"></a>

# 第60章\_参考资料（References）

<a id="id2"></a>

〔[1](#id3)〕 [https://www.dh-electronics.com/en/embedded-products/development-carrier-boards/detail/dhsbc-rs-485-can-shield](https://www.dh-electronics.com/en/embedded-products/development-carrier-boards/detail/dhsbc-rs-485-can-shield)

<a id="id4"></a>

〔[2](#id5)〕 [https://www.dh-electronics.com/en/download/file/downloads/USM_DHSBC-RS485-CAN-Shield.pdf](https://www.dh-electronics.com/en/download/file/downloads/USM_DHSBC-RS485-CAN-Shield.pdf)

## 译注

RS485示例使用外接GPIO LED，app.overlay与DTC_OVERLAY_FILE的关系按来源保留；CAN部分为收发器。

---

[上一章](P059_DFRobot_Gravity_TM6605_Haptic_Motor_Driver_Module.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P061_DVP_20-pin_OV7670_Camera_Module.md)
