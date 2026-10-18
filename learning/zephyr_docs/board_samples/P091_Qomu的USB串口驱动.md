---
id: learning.zephyr-docs.board-samples.page-91
title: Qomu的USB串口驱动
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/quicklogic/qomu/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="zephyr-usbserial-driver-on-qomu"></a>

<a id="qomu-usbserial"></a>

# 第91章\_Qomu 上的 Zephyr USB 串口驱动（Zephyr usbserial driver on Qomu）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/quicklogic/qomu/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

本示例展示如何向 EOS-S3 FPGA 加载比特流（Bitstream），并使用 USB 串口（usbserial）驱动。

> 译注——两层镜像：FPGA 为现场可编程门阵列（Field-Programmable Gate Array）。主机先向 Cortex-M4 加载 Zephyr 固件，main() 再通过 fpga_load() 加载编译进固件的 usb2serial 比特流数组，然后等待两秒让 USB 枚举。M4 应用固件与 FPGA 比特流不是同一种文件。

<a id="requirements"></a>

## 91.1 前提条件（Requirements）

- 启用 printk 的 Zephyr 实时操作系统（RTOS）。

- [QuickLogic Qomu 开发板。](https://www.quicklogic.com/products/eos-s3/quickfeather/)

<a id="building"></a>

## 91.2 构建（Building）

> 译注——执行前提：主机 west 命令从读者的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行；先按[入门指南](../getting_started/大纲.md)准备工具、模块、工具链和具体板。调试器、双镜像及外部下载工具的目录要求分别按本页说明处理。本次未构建、烧录或执行硬件实验。

```text
west build -b qomu samples/boards/quicklogic/qomu
```

<a id="flashing"></a>

## 91.3 烧录（Flashing）

可使用 [TinyFPGA-Programmer-Application](https://github.com/QuickLogic-Corp/TinyFPGA-Programmer-Application) 将示例加载到 Qomu。

> 译注——可移植工具目录：下面将原文绝对路径占位符改为 TINYFPGA_PROGRAMMER_DIR。先在 UCRT64 Bash 或 Linux Bash 中把该变量设为相对于当前 Zephyr 源码根的实际工具目录；脚本须已按官方用户指南准备好。整个命令从该源码根执行，build/zephyr/zephyr.bin 是前一步的固件产物；不是要求读者把工具装到固定磁盘。

```text
python3 "$TINYFPGA_PROGRAMMER_DIR/tinyfpga-programmer-gui.py" --mode m4 --m4app build/zephyr/zephyr.bin --reset
```

关于如何将镜像加载到开发板，参见 [Qomu 用户指南（Qomu User Guide）](https://github.com/QuickLogic-Corp/qomu-dev-board/blob/662f8841bdc1ed35c1539ac381182159d7cd5914/doc/Qomu_UserGuide.pdf)。

<a id="running"></a>

## 91.4 运行（Running）

连接串口控制台后，应看到以下输出：

> 译注——示例边界：当前 main.c 仍引用旧的 zephyr/zephyr.h，并未检查 fpga_load() 返回值。控制台只打印示例横幅，代码没有实现交互式 Shell 命令循环；看见文字不等于所有 FPGA 功能验证通过。是否能在所用版本直接构建，需要按对应板支持核实。

```text
####################
I am Zephyr on Qomu!
####################
```

> 译注——源码入口：[src/main.c](../../../samples/boards/quicklogic/qomu/src/main.c)；[CMakeLists.txt](../../../samples/boards/quicklogic/qomu/CMakeLists.txt)。仓库参照使用相对路径，版本可能与本次上游快照不同。

对应官方文档源码：[samples/boards/quicklogic/qomu/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/quicklogic/qomu/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/quicklogic/qomu/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P090_PHYTEC示例目录.md) · [返回大纲](大纲.md) · [下一章](P092_QuickLogic示例目录.md)
