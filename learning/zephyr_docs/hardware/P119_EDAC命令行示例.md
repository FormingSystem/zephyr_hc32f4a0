---
id: learning.zephyr-docs.hardware.powersamp-0
title: EDAC命令行示例
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/edac/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="edac"></a>

# 第119章\_EDAC命令行示例

原文：[EDAC shell](https://docs.zephyrproject.org/latest/samples/subsys/edac/README.html)。读取日期：2026-10-13，`latest`。

## 119.1\_用命令行演示EDAC接口

本示例通过简单的 **命令解释器（Shell）**演示 **错误检测与纠正（Error Detection And Correction，EDAC）**驱动的 **应用程序编程接口（Application Programming Interface，API）**；接口概览见[错误检测与纠正](P112_错误检测与纠正.md)。

## 119.2\_构建与运行

以下原命令通过west工作区工具为Intel Elkhart Lake CRB开发板构建示例。`intel_ehl_crb` 是开发板构建目标，命令从Zephyr源码目录执行：

```sh
west build -b intel_ehl_crb samples/subsys/edac
```

生成的Zephyr镜像可按[Elkhart Lake CRB板级说明](https://docs.zephyrproject.org/latest/boards/intel/ehl/doc/index.html#intel_ehl_crb)运行。该目标不是HC32开发板，原例地址也不应作为HC32的硬件配置。

## 119.3\_查看帮助

程序启动后，用 `edac -h` 查看帮助。下面原输出中的 `info` 子命令显示信息，`inject` 子命令注入 **错误纠正码（Error Correction Code，ECC）**错误。`uart:~$` 是串口Shell提示符；UART为 **通用异步收发器（Universal Asynchronous Receiver/Transmitter）**。

```text
uart:~$ edac -h
edac - EDAC information
Subcommands:
  info    :Show EDAC information
           edac info <subcommands>
  inject  :Inject ECC error commands
           edac inject <subcommands>
```

查看 `info` 帮助时，`ecc_error` 子命令提供ECC错误显示与清除操作，`parity_error` 子命令提供 **奇偶校验错误（Parity Error）**显示与清除操作：

```text
uart:~$ edac info -h
info - Show EDAC information
       edac info <subcommands>
Subcommands:
  ecc_error     :ECC Error Show / Clear commands
  parity_error  :Parity Error Show / Clear commands
```

查看注入帮助。`param1`、`param2` 获取或设置注入参数，`trigger` 触发注入，`error_type` 获取或设置错误类型，`test_default` 测试默认注入参数；`disable_nmi` 与 `enable_nmi` 分别禁用、启用 **不可屏蔽中断（Non-Maskable Interrupt，NMI）**：

```text
uart:~$ edac inject -h
inject - Inject ECC error commands
         edac inject <subcommands>
Subcommands:
  param1        :Get / Set injection param 1
  param2        :Get / Set injection param 2
  trigger       :Trigger injection
  error_type    :Get / Set injection error type
  disable_nmi   :Disable NMI
  enable_nmi    :Enable NMI
  test_default  :Test default injection parameters
```

原文提示：各厂商的EDAC实现不同，`param1` 与 `param2` 的确切含义应查看对应驱动实现。关于IBECC错误注入仅用于测试的限制，见[带内错误纠正码](P113_带内错误纠正码.md)。

## 119.4\_原文错误注入过程

首先设置注入参数。原例将参数1设为 `0x1000`、参数2设为 `0x7fffffffc0`，错误类型设为 **可纠正（Correctable）**：

```text
uart:~$ edac inject param1 0x1000
Set injection param1 to: 0x1000

uart:~$ edac inject param2 0x7fffffffc0
Set injection param2 to 7fffffffc0

uart:~$ edac inject error_type correctable
Set injection error type: correctable
```

然后触发注入：

```text
uart:~$ edac inject trigger
Triggering injection
```

接着使用设备内存读写命令 `devmem` 读写注入地址，以触发错误注入。下列原例向 `0x1000` 写入32位数值 `0xabcd`，再读取同一地址；日志中的映射地址也按原文保留：

```text
uart:~$ devmem 0x1000 32 0xabcd
Mapped 0x1000 to 0x2ffcf000

Using data width 32
Writing value 0xabcd

uart:~$ devmem 0x1000
Mapped 0x1000 to 0x2ffce000

Using data width 32
Read value 0xabcd
```

原文预期屏幕出现以下消息，表示收到了ECC事件通知：

```text
Got notification about ECC event
```

## 119.5\_接口与源码

完整接口见[EDAC API](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html)，源码见[官方EDAC示例目录](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/subsys/edac)。本文保存原命令及输出，没有实际执行内存写入、错误注入或NMI切换。

[上一章：时钟频率测量示例](P118_时钟频率测量示例.md) · [下一章：PECI温度监视示例](P120_PECI温度监视示例.md) · [返回大纲](大纲.md)
