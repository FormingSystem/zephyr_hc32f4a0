---
id: learning.zephyr-docs.driver_samples.page-8
title: SMBus命令行示例
kind: reference
status: maintained
domains: [zephyr, driver_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/smbus/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="smbus-shell"></a>

# 第8章\_SMBus命令行示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/drivers/smbus/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 8.1\_概览（Overview）

本例提供简单的系统管理总线（System Management Bus，SMBus）命令行（Shell），让具有SMBus驱动支持的开发板探索与外设的通信。

<a id="building-and-running"></a>

## 8.2\_构建与运行（Building and Running）

原文以qemu_x86_64为例：

```bash
west build -b qemu_x86_64 samples/drivers/smbus
west build -t run
```

> 译注——终端边界：以上从Zephyr源码根在主机Shell执行；先完成工具链、模块及QEMU环境准备。启动后出现的uart提示符属于运行中的Zephyr Shell，后续smbus命令输入在那里，不是在主机PowerShell或Bash执行。模拟器中的设备结果不表示真实板上存在相同外设。

<a id="sample-output"></a>

### 8.2.1\_示例输出（Sample Output）

应用启动时的控制台输出：

```text
*** Booting Zephyr OS build zephyr-v3.2.0-804-gfedd72615e82  ***
Start SMBUS shell sample qemu_x86_64
uart:~$
```

输入smbus列出可用命令：

```text
uart:~$ smbus
smbus - smbus commands
Subcommands:
  quick            :SMBus Quick command
                    Usage: quick <device> <addr>
  scan             :Scan SMBus peripheral devices command
                    Usage: scan <device>
  byte_read        :SMBus: byte read command
                    Usage: byte_read <device> <addr>
  byte_write       :SMBus: byte write command
                    Usage: byte_write <device> <addr> <value>
  byte_data_read   :SMBus: byte data read command
                    Usage: byte_data_read <device> <addr> <cmd>
  byte_data_write  :SMBus: byte data write command
                    Usage: byte_data_write <device> <addr> <cmd> <value>
  word_data_read   :SMBus: word data read command
                    Usage: word_data_read <device> <addr> <cmd>
  word_data_write  :SMBus: word data write command
                    Usage: word_data_write <device> <addr> <cmd> <value>
  block_write      :SMBus: Block Write command
                    Usage: block_write <device> <addr> <cmd> [<byte1>, ...]
  block_read       :SMBus: Block Read command
                    Usage: block_read <device> <addr> <cmd>
```

> 译注——命令含义：quick为SMBus快速命令（Quick Command）；scan扫描外设；byte_read／byte_write执行字节读／写；byte_data_read／byte_data_write执行带命令码的字节数据读／写；word_data_read／word_data_write执行字数据读／写；block_read／block_write执行块数据读／写。device为SMBus控制器设备名，addr为外设地址，cmd为SMBus命令码，value或byte列表为写入数据。原帮助中的尖括号表示待替换参数，uart:~$是提示符。

扫描可用SMBus设备：

```text
uart:~$ smbus scan smbus@fb00
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:             -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: 50 51 52 53 54 55 56 57 -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --
8 devices found on smbus@fb00
```

> 译注——扫描结果：该日志在smbus@fb00上发现8个地址，从0x50到0x57。不同目标的设备名、外设与扫描结果可能不同；命令找不到控制器时先检查设备树和驱动配置，不能把示例名称当作所有板的固定名称。

<a id="see-also"></a>

## 8.3\_相关接口（See also）

[SMBus接口参考](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html)。


对应官方文档源码：[samples/drivers/smbus/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/smbus/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/drivers/smbus/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/drivers/smbus/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P007_JESD216闪存参数示例.md) · [返回大纲](大纲.md) · [下一章](P009_单总线器件示例.md)
