---
id: learning.zephyr-docs.hardware.periph-eeprom-shell
title: EEPROM命令行
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/hardware/peripherals/eeprom/shell.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第37章\_EEPROM命令行

原文：[EEPROM Shell](https://docs.zephyrproject.org/latest/hardware/peripherals/eeprom/shell.html)。读取日期：2026-10-13，`latest`。

## 37.1\_启用交互命令

**电可擦可编程只读存储器（Electrically Erasable Programmable Read-Only Memory，EEPROM）**的 **命令解释器（Shell）**入口提供 `eeprom` 及一组子命令，无需专门编写应用即可交互测试驱动的 **应用程序编程接口（Application Programming Interface，API）**。也可在已有应用启用它，辅助调试EEPROM问题。

必须启用Kconfig配置项 [`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_EEPROM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EEPROM) 和 [`CONFIG_EEPROM_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EEPROM_SHELL)。下面从Zephyr源码根目录为 **原生模拟器（Native Simulator，native_sim）**构建Hello World示例：

```shell
# From the root of the zephyr repository
west build -b native_sim samples/hello_world -- -DCONFIG_SHELL=y -DCONFIG_EEPROM=y -DCONFIG_EEPROM_SHELL=y
```

**译注：**native_sim的运行环境须满足[官方板卡要求](../native_reference/P004_Native_Simulator本机模拟器.md#native_sim)，不能把Windows主机上的构建命令展示理解为它可直接作为普通Windows程序运行。

一般连接方式见[Shell说明](https://docs.zephyrproject.org/latest/services/shell/index.html#shell-api)。除非禁用Kconfig配置项 [`CONFIG_SHELL_HELP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_HELP)，对 `eeprom` 或任一子命令传入 `-h` / `--help` 即可显示帮助；所有子命令支持Tab参数补全。

所有子命令的第一个参数都是EEPROM设备名，也支持补全。启用Kconfig配置项 [`CONFIG_DEVICE_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DEVICE_SHELL) 后，可用 `device list` 列出设备。后续原例设备名均为 `eeprom@0`；`uart:~$` 是设备提示符，不是需要输入的命令内容。

## 37.2\_查询容量

用 `eeprom size` 检查设备容量，原例返回32768字节：

```shell
uart:~$ eeprom size eeprom@0
32768 bytes
```

## 37.3\_写入与填充

`eeprom write` 至少接收设备名、写入起始偏移和一个数据字节。原例从偏移 `0x0` 写入八个十六进制字节 `0d 0e 0a 0d 0b 0e 0e 0f`，随后验证：

```shell
uart:~$ eeprom write eeprom@0 0x0 0x0d 0x0e 0x0a 0x0d 0x0b 0x0e 0x0e 0x0f
Writing 8 bytes to EEPROM...
Verifying...
Verify OK
```

`eeprom fill` 可用同一个字节模式填充区域；原例从偏移 `0x8` 开始，将16字节填为 `0xaa`：

```shell
uart:~$ eeprom fill eeprom@0 0x8 16 0xaa
Writing 16 bytes of 0xaa to EEPROM...
Verifying...
Verify OK
```

输出 `Verify OK` 表示原例校验成功。此处保留官方操作示例，没有向实际EEPROM写入数据。

## 37.4\_读取数据

`eeprom read` 接收设备名、起始偏移和读取字节数三个参数。下例从偏移0读取8字节；左列为偏移，中间为十六进制数据，右侧为字符显示：

```shell
uart:~$ eeprom read eeprom@0 0x0 8
Reading 8 bytes from EEPROM, offset 0...
00000000: 0d 0e 0a 0d 0b 0e 0e 0f                          |........         |
```

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：EEPROM接口](P036_EEPROM接口.md) · [本模块主线目录](../reading/hardware.md) · [全部主线](../reading/README.md) · [下一篇：存储外设入口](P056_存储外设入口.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：EEPROM接口](P036_EEPROM接口.md) · [下一章：CRC驱动接口参考](P038_CRC驱动接口参考.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
