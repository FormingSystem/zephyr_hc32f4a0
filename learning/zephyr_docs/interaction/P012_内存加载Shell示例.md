---
id: learning.zephyr-docs.interaction.page-12
title: 内存加载Shell示例
kind: reference
status: maintained
domains: [zephyr, shell, input]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/shell/devmem_load/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_内存加载Shell示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/shell/devmem_load/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 12.1\_概述与要求

本模块加入 `devmem load` 命令，把数据加载到设备内存（Device Memory）。该命令支持 Zephyr Shell 能运行的各类传输后端。调用后，设备接收输入并写入指定内存地址；按 Ctrl+X，再按 Ctrl+Q，结束传输。

目标必须配置 Shell 接口，并通过任一后端暴露接口。

## 12.2\_构建与运行

示例支持多个平台。以下原始主机命令在已准备好构建依赖的 Zephyr 源码根目录执行。

### 仿真目标

为 `qemu_x86` 构建并运行：

```sh
west build -b qemu_x86 samples/subsys/shell/devmem_load
west build -t run
```

应用启动后显示 Shell 提示符，此时可以输入 `devmem load`。

**注意：** 通过 UART 使用时，尽量采用中断（Interrupt）方式；若无法使用中断，把波特率（Baud Rate）降至 9600。使用轮询（Polling）方式时，还应采用 `prj_poll.conf`，代替 `prj.conf`。

为不支持 UART 中断的开发板构建，原文以 `native_sim` 为例：

```sh
west build -b native_sim samples/subsys/shell/devmem_load -- -DCONF_FILE=prj_poll.conf
west build -t run
```

### 实板

原文命令如下：

```sh
west build -b nrf52840dk/nrf52840 samples/subsys/shell/shell_module
west flash
```

> 译注——原示例路径差异：本页为 `samples/subsys/shell/devmem_load`，但实板命令写的是 `samples/subsys/shell/shell_module`。当前前者确实存在独立的 `src/main.c`、`prj.conf` 和 `prj_poll.conf`。若要构建本页的独立加载示例，应在所选目标的构建命令中使用 `samples/subsys/shell/devmem_load`；这里保留原命令，未把它改写成已验证的实板结果。

## 12.3\_示例输出与传输

连接 UART 控制台后应看到：

```text
uart:~$
```

随后使用加载命令：

```text
uart:~$ devmem load 0x20020000
Loading...
press ctrl-x ctrl-q to escape
```

提示表示正在加载，并可按 Ctrl+X、Ctrl+Q 退出。此时等待数据输入；既可直接输入，也可由主机发送。下面命令在主机终端执行，把 `ttyX` 换成实际 UART 控制台设备：

```sh
xxd -p data > /dev/ttyX
```

**注意：** 必须使用纯十六进制转储（Plain-style Hex Dump），不能带地址列和 ASCII 侧栏。

传输完成后按 Ctrl+X，再按 Ctrl+Q。Shell 显示读取字节数并返回提示符：

```text
Number of bytes read: 3442
uart:~$
```

输出含义是“已读取 3442 字节”，这是原文的示例值，不是固定长度要求。

## 12.4\_选项与源码核对

原文当前列出一个选项：`-e`，把数据按小端序（Little Endian）解释，例如 `0xDEADBEFF → 0xFFBEADDE`。

> 译注：当前实现先把收到的十六进制字符每两个解析为一个字节并逐字节写入；不带 `-e` 时，退出后还执行按字组交换，带 `-e` 时跳过该交换。上面的数值例子不能替代对实际内存字节顺序的判断。输入应是 `xxd -p` 这样的纯十六进制文本，而不是直接发送原始二进制文件。

> 译注：原示例地址 `0x20020000` 不保证在所选开发板上可用。本实现根据给定地址直接写内存，命令本身没有目标缓冲区容量参数；应用必须先确定可写区域和允许长度，不应把这个地址当成任意板都适用的 RAM 缓冲区。当前旁路状态也只允许一个 Shell 实例使用该加载功能。

参阅：[Shell指南](P001_Shell命令行.md)。


译注核对来源：[samples/subsys/shell/devmem_load/src/main.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/shell/devmem_load/src/main.c)、[samples/subsys/shell/devmem_load/prj_poll.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/shell/devmem_load/prj_poll.conf)、[subsys/shell/modules/devmem_service.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/shell/modules/devmem_service.c)。

本仓库的[对应示例源码](../../../samples/subsys/shell/devmem_load/src/main.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行构建、写内存／闪存或硬件操作。

<a id="shell-devmem-load"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="building-and-running"></a>
<a id="emulation-targets"></a>
<a id="on-hardware"></a>
<a id="sample-output"></a>
<a id="options"></a>
<a id="see-also"></a>

[上一章](P011_文件系统Shell示例.md) · [返回大纲](大纲.md) · [下一章](P013_输入子系统示例目录.md)
