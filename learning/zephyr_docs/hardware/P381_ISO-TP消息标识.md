---
id: learning.zephyr-docs.hardware.isotpstruct-0
title: ISO-TP消息标识
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structisotp__msg__id.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第381章\_ISO-TP消息标识

原文：[structisotp__msg__id](https://docs.zephyrproject.org/latest/doxygen/html/structisotp__msg__id.html)。读取日期：2026-10-13，`latest`。

## 381.1\_用途与结构

`struct isotp_msg_id` 是 ISO-TP 传输协议（Transport Protocol）的消息标识结构，用于向绑定函数 `isotp_bind()` 和发送函数 `isotp_send()` 传递地址。包含头文件 `zephyr/canbus/isotp.h`。

控制器局域网（Controller Area Network，CAN）的标准标识符（Standard Identifier）与扩展标识符（Extended Identifier）共用一个匿名联合体（Anonymous Union）：

```c
struct isotp_msg_id {
    union {
        uint32_t std_id : 11;
        uint32_t ext_id : 29;
    };
    uint8_t ext_addr;
    uint8_t dl;
    uint8_t flags;
};
```

> 译注：上述声明按官方字段表整理；[`std_id`](https://docs.zephyrproject.org/latest/doxygen/html/structisotp__msg__id.html#ac9ded92f8e0afa88609003c5cf819704) 和 [`ext_id`](https://docs.zephyrproject.org/latest/doxygen/html/structisotp__msg__id.html#a3f9d4a6efd9b1c147f889a6396d7ef1c) 的 11 位、29 位位域宽度来自该表，字段详情的小标题没有重复显示位宽。

## 381.2\_地址与标志

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `std_id` | `uint32_t : 11` | CAN 标准标识符，与 `ext_id` 共用存储。 |
| `ext_id` | `uint32_t : 29` | CAN 扩展标识符，与 `std_id` 共用存储。 |
| [`ext_addr`](https://docs.zephyrproject.org/latest/doxygen/html/structisotp__msg__id.html#a7b818e7c6dab02347b32bcc74dfc44a3) | [`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | ISO-TP 扩展地址，在使用扩展寻址时有效。 |
| [`dl`](https://docs.zephyrproject.org/latest/doxygen/html/structisotp__msg__id.html#adc7ff4eac4573221b89a5bb5a5e53d49) | [`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | ISO-TP 帧数据长度（Data Length），具体规则见下一节。 |
| [`flags`](https://docs.zephyrproject.org/latest/doxygen/html/structisotp__msg__id.html#a3185e5b5fddb5d7fc94b86c8d30e61a9) | [`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | 消息标志，参见[消息标识标志](P380_CAN_ISO-TP接口参考.md)。 |

使用 ISO-TP 固定寻址（Fixed Addressing）时，`isotp_bind()` 忽略标识符的源地址（Source Address，SA）与优先级（Priority）部分，并修改流控帧（Flow Control Frame，FC）中的目标地址（Target Address，TA）部分。

## 381.3\_帧数据长度

对于发送（Transmit，TX）地址，`dl` 表示 `TX_DL`；对于接收（Receive，RX）地址，它表示 `RX_DL`。

经典 CAN（Classical CAN）的有效值为 8；灵活数据速率 CAN（CAN with Flexible Data-rate，CAN FD）的有效值为 8、12、16、20、24、32、48、64。

值为 0 时，按 8 解释；设置 `ISOTP_MSG_FDF` 标志时则按 64 解释。

输入传输的 `RX_DL` 根据收到的首帧（First Frame，FF）自动确定，无需在初始化期间设置。

---

[上一章：CAN_ISO-TP接口参考](P380_CAN_ISO-TP接口参考.md) · [下一章：ISO-TP流控选项](P382_ISO-TP流控选项.md) · [返回大纲](大纲.md)
