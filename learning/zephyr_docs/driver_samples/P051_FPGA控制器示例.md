---
id: learning.zephyr-docs.driver_samples.page-51
title: FPGA控制器示例
kind: reference
status: maintained
domains: [zephyr, driver_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/fpga/fpga_controller/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="fpga-controller"></a>

# 第51章\_FPGA控制器示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/drivers/fpga/fpga_controller/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 51.1\_概览（Overview）

该模块提供FPGA驱动，可方便地加载位流（Bitstream）、复位、检查状态，以及启用或禁用FPGA。本例演示FPGA驱动API和FPGA控制器Shell子系统的使用。

<a id="id2"></a>

当前示例适用于[QuickLogic QuickFeather开发板](https://github.com/QuickLogic-Corp/quick-feather-dev-board)，见参考文献[[1]](#id1)。

<a id="requirements"></a>

## 51.2\_要求（Requirements）

- Zephyr实时操作系统（Real-time Operating System，RTOS）；或在运行Shell应用时，使用启用Shell子系统的Zephyr RTOS。
- <a id="id3"></a>[QuickLogic QuickFeather开发板](https://github.com/QuickLogic-Corp/quick-feather-dev-board)，见参考文献[[1]](#id1)。

<a id="building"></a>

## 51.3\_构建（Building）

为QuickLogic QuickFeather开发板构建：

> 译注——主机侧构建：在已配置Zephyr环境的终端、Zephyr源码根目录执行。第一种为普通应用；第二种为Shell应用，是配置选择分支。切换配置时应按现有构建流程重新配置，避免继续使用旧缓存；构建报错时先核对目标板和所选配置文件。

```bash
# From the root of the zephyr repository
west build -b quick_feather samples/drivers/fpga/fpga_controller
```

构建FPGA控制器Shell应用时，使用随附的配置文件`prj_shell.conf`：

```bash
west build -b quick_feather samples/drivers/fpga/fpga_controller -- -DCONF_FILE=prj_shell.conf
```

<a id="running"></a>

## 51.4\_运行（Running）

关于向板卡加载镜像的方法，见[QuickFeather开发板文档](https://docs.zephyrproject.org/latest/boards/quicklogic/quick_feather/doc/index.html#quick_feather)。

<a id="sample-output"></a>

### 51.4.1\_示例输出（Sample output）

完成板卡编程后，LED应交替闪烁红色与绿色。

对于FPGA控制器Shell应用，连接Shell控制台后应看到以下输出：

```text
Address of the bitstream (red): 0xADDR
Address of the bitstream (green): 0xADDR
Size of the bitstream (red): 75960
Size of the bitstream (green): 75960

uart:~$
```

本例已经准备好位流。运行后可以看到它们的存放地址和字节数。随后可使用FPGA控制器命令，语法为`fpga load <device> <address> <size in bytes>`：

```text
uart:~$ fpga load FPGA 0x2001a46c 75960
FPGA: loading bitstream
```

LED应开始闪烁，颜色取决于所选位流。若要再次加载位流，需要先复位FPGA：

```text
uart:~$ fpga reset FPGA
FPGA: resetting FPGA
```

> 译注——目标控制台与地址：带uart:~$提示符的行在开发板Zephyr Shell执行，不在主机PowerShell或Bash中执行；提示符和随后输出无需作为命令输入。0xADDR是输出占位符，0x2001a46c和75960是原示例地址与长度，实际加载应使用本次程序打印的对应位流信息。它们是目标内存地址，不是仓库文件路径。

也可以使用自己的位流。首先用`devmem load`命令把位流写入设备内存；通过`xxd`发送位流时，务必使用`-e`选项：

```text
uart:~$ devmem load -e 0x10000
Loading...
Press ctrl-x + ctrl-q to stop
```

此时加载器正在等待数据。可以直接在控制台输入，也可以从主机发送；把`ttyX`替换为Shell控制台实际对应的设备：

```bash
xxd -p data > /dev/ttyX
```

**必须使用纯十六进制转储（Plain-style Hex Dump）。**传输完成后，按Ctrl-X、Ctrl-Q退出加载器。它会打印读取的总字节数并返回Shell：

```text
Number of bytes read: 75960
uart:~$
```

现在可以再次加载位流：

```text
uart:~$ fpga load FPGA 0x10000 75960
FPGA: loading bitstream
```

> 译注——两次加载的不同对象：主机xxd命令从当前目录读取名为data的位流文件，把纯十六进制文本发送到所选串口；/dev/ttyX是原Linux串口设备示例，需替换为主机实际设备。devmem load先将字节写入目标内存，fpga load再从该内存地址配置FPGA。原0x10000并非适合所有板卡和固件的通用缓冲区，使用前必须确认足够大且可写、不会覆盖运行数据的目标区域。

> 译注——-e与字节序：所读[devmem_service.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/shell/modules/devmem_service.c)把-e解释为小端解析（Little-endian Parse）；未给出该选项时，退出加载后会执行相应字节交换。这里的-e属于开发板devmem load，主机xxd使用的是-p，不能互换。所读[main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/fpga/fpga_controller/src/main.c)区分普通应用自动切换位流和Shell应用打印地址两条路径；本批没有上传镜像、写入目标内存或配置FPGA。

<a id="references"></a>

## 51.5\_参考资料（References）

<a id="id1"></a>

1. [QuickLogic QuickFeather开发板仓库](https://github.com/QuickLogic-Corp/quick-feather-dev-board)。


对应官方文档源码：[samples/drivers/fpga/fpga_controller/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/fpga/fpga_controller/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/drivers/fpga/fpga_controller/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/drivers/fpga/fpga_controller/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P050_FPGA示例目录.md) · [返回大纲](大纲.md) · [下一章](P052_Bouffalolab_GPIO_FIFO串口示例.md)
