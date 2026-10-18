---
id: learning.zephyr-docs.hardware.hwapi-crc-sample
title: CRC校验示例
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/crc/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="crc_drivers"></a>

# 第42章\_CRC校验示例

原文：[Cyclic Redundancy Check Drivers (CRC)](https://docs.zephyrproject.org/latest/samples/drivers/crc/README.html)。读取日期：2026-10-13，`latest`。

## 42.1\_示例目的与变体选择

本示例演示 **循环冗余校验（Cyclic Redundancy Check，CRC）**驱动的 **应用程序编程接口（Application Programming Interface，API）**：通过示例的Kconfig选择一种CRC变体，对预定义数据计算结果并写入日志；如果配置了预期值，还会核对结果。

CCITT指 **国际电报电话咨询委员会（International Telegraph and Telephone Consultative Committee）**；IEEE指 **电气与电子工程师协会（Institute of Electrical and Electronics Engineers）**。这里保留它们在变体名中的拼写，便于对应驱动能力和配置。CRC32 C中的C也是变体名的一部分，不是编程语言选择。

Kconfig是Zephyr的配置系统。原文列出的示例配置符号如下；它们是选择计算变体的选项名称。

| Kconfig符号 | 选择的CRC变体 |
| --- | --- |
| `SAMPLE_CRC_VARIANT_CRC8` | CRC8。 |
| `SAMPLE_CRC_VARIANT_CRC16_CCITT` | CRC16 CCITT。 |
| `SAMPLE_CRC_VARIANT_CRC32_IEEE` | CRC32 IEEE。 |
| `SAMPLE_CRC_VARIANT_CRC32_C` | CRC32 C。 |

示例会在构建时检查目标驱动／平台能力。如果所选变体不受支持，编译会失败，并输出解释能力不匹配的错误消息。此时应返回变体选择和目标驱动支持检查，不能把它当作运行时校验失败。

## 42.2\_在RA8M1评估板上构建与运行

以下是官方针对[RA8M1评估套件（RA8M1 Evaluation Kit）](https://docs.zephyrproject.org/latest/boards/renesas/ek_ra8m1/doc/index.html#ek_ra8m1)的命令。前提是已完成Zephyr主机环境、对应工具链和该板烧录工具准备，并连接目标板；从实验Zephyr源码根目录，在Ubuntu Bash或已准备好的UCRT64 Bash中执行。`samples/drivers/crc` 是官方已有示例目录，`build` 是构建工具生成的目录。

```shell
west build -b ek_ra8m1 samples/drivers/crc
west flash
```

`west build` 构建所选板固件，`west flash` 把构建结果写入目标板。切换到另一块受支持的板时，将 `ek_ra8m1` 替换为其板名，并重新核对CRC驱动能力；这不表示任意板都支持全部变体。构建失败时先处理编译错误，再执行烧录。

## 42.3\_观察计算和校验结果

控制台记录选中的变体和计算值；给出预期值时，再记录校验结果。原文输出如下，本次文档翻译没有执行该实板示例。

```text
crc_example: CRC8 result: 0x000000b2
crc_example: CRC8 verification succeeded (expected 0x000000b2)
```

预期行为依次是：对预定义数据计算选中的CRC变体；记录计算出的CRC值；若配置了预期值，则校验并记录成功或失败。示例中的 `0x000000b2` 属于原文给定数据与配置的结果，不能直接套用到不同输入。完整调用约束见[CRC驱动接口参考](P038_CRC驱动接口参考.md)。

[上一章：CAN收发器接口参考](P041_CAN收发器接口参考.md) · [下一章：EEPROM计数示例](P043_EEPROM计数示例.md) · [返回大纲](大纲.md)
