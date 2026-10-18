---
id: learning.zephyr-docs.boards-starfive-trenz.page-2
title: VisionFive 2 JH7110
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/starfive/visionfive2/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="visionfive2"></a>

# 第2章\_VisionFive 2 JH7110

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/starfive/visionfive2/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

<a id="id1"></a>

[![官方原图：../../../../_images/visionfive2.webp](images/visionfive2.webp)](images/visionfive2.webp)

VisionFive 2 JH7110

名称（Name）：

`visionfive2`

厂商（Vendor）：

[StarFive Technology Co. Ltd.](https://docs.zephyrproject.org/latest/boards/index.html#vendor=starfive)

状态（Status）：

维护中（Maintained）

架构（Architecture）：

[riscv](https://docs.zephyrproject.org/latest/boards/index.html#arch=riscv)

片上系统（SoC）：

[jh7110](https://docs.zephyrproject.org/latest/boards/index.html#soc=jh7110)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/starfive/visionfive2/doc/index.rst/../..)<a id="overview"></a>

## 概述（Overview）

StarFive VisionFive 2是一块采用JH7110多核64位RISC-V SoC的开发板。

<a id="programming-and-debugging"></a>

## 编程与调试（Programming and Debugging）

`visionfive2`开发板支持下表所列的运行工具（Runners）及相关west命令。

<table>
<tr>
<th></th>
<th>烧录（flash）</th>
<th>调试（debug）</th>
</tr>
</table>

<a id="building"></a>

### 构建（Building）

visionfive2板级配置的应用可按常规方式构建，见“构建应用”，并使用相应板名：（[构建应用（Building an Application）](../application/P001_应用开发.md#build-an-application)）

```text
west build -b visionfive2
```

[spl_tool](https://github.com/starfive-tech/Tools/tree/master/spl_tool/)是JH7110签名工具，用于生成SPL头部信息及zephyr.bin.normal.out。

```text
./spl_tool -c -f build/zephyr/zephyr.bin
```

这会生成可写入的build/zephyr/zephyr.bin.normal.out。Zephyr二进制必须包含SPL头部才能在机器模式（M-Mode）运行；此页尚不支持监管者模式（S-Mode），因此这一步不可省略。

<a id="flashing"></a>

### 烧录（Flashing）

注意（Note）

以下步骤使用minicom，也可采用其他支持XMODEM文件传输的串口终端。原文感谢@orangecms提供vf2-loader工具，简化写入过程。

通过git clone将[https://github.com/orangecms/vf2-loader.git](https://github.com/orangecms/vf2-loader.git)与[https://github.com/orangecms/xmodem.rs.git](https://github.com/orangecms/xmodem.rs.git)克隆到同级目录。

VisionFive 2通过UART写入镜像。按VisionFive 2恢复快速指南连接USB转串口转换器，再上电，用minicom连接串口，按复位键直到出现CCCCCC…提示。（[VisionFive2恢复快速入门指南](https://doc-en.rvspace.org/VisionFive2/Quick_Start_Guide/VisionFive2_SDK_QSG/recovering_bootloader%20-%20vf2.html)）

将build/zephyr/zephyr.bin.normal.out复制到已克隆的vf2-loader目录，进入该目录并执行以下命令写入：

```text
cargo run -- zephyr.bin.normal.out && minicom -D /dev/ttyUSB0
```

```text
cargo run -- zephyr.bin.normal.out && minicom -D /dev/ttyUSB0
Finished dev [unoptimized + debuginfo] target(s) in 0.03s
Running `target/debug/vf2-loader zephyr.bin.normal.out`
Welcome to minicom 2.7.1
OPTIONS: I18n
Compiled on Dec 23 2019, 02:06:26.
Port /dev/ttyUSB0, 14:59:24
Press CTRL-A Z for help on special keys
6*** Booting Zephyr OS build v3.6.0-rc3 ***
Hello World! visionfive2
```

## 译注

VisionFive 2在此页仅支持机器模式（M-mode）。UART加载需要先用spl_tool生成带SPL头的镜像；vf2-loader及xmodem.rs依原文放在同级目录。这里只翻译流程，未执行实板加载。

---

[上一章](P001_StarFive.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P003_Apex_Pro_Mini.md)
