---
id: learning.zephyr-docs.intercore_reference.ipmsample-84
title: ArmMHU双核IPM示例
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/ipm/ipm_mhu_dual_core/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="ipm-mhu-dual-core"></a>

# 第84章\_ArmMHU双核IPM示例

原文：[IPM with ARM MHU](https://docs.zephyrproject.org/latest/samples/drivers/ipm/ipm_mhu_dual_core/README.html)。读取日期：2026-10-13，`latest`。

消息处理单元（Message Handling Unit，MHU）允许软件向处理器核心触发中断。本例通过处理器间邮箱（Inter-Processor Mailbox，IPM）测试双核通信。原概述称目标为具有两个MHU单元的Musca A1开发板，且**只测试MHU0**。

原日志中的OS表示操作系统（Operating System），日志版本字符串和计数值按原样保留。


## 84.1\_测试流程

CPU指中央处理器（Central Processing Unit）。测试依次执行：

1. CPU0初始化后唤醒CPU1。
2. CPU1通过MHU0向CPU0发送中断。
3. CPU0收到MHU0中断后，向CPU1返回同样的中断。
4. CPU1收到MHU0中断时，测试结束。

## 84.2\_在Musca B1上构建和运行

原构建章节使用Musca B1。CPU0项目向控制台输出`IPM MHU sample on musca_b1`，其命令为：

```sh
west build -b v2m_musca_b1/musca_b1 samples/drivers/ipm/ipm_mhu_dual_core
west build -t run
```

CPU1项目输出`IPM MHU sample on v2m_musca_b1_ns`，其命令为：

```sh
west build -b v2m_musca_b1/musca_b1/ns samples/drivers/ipm/ipm_mhu_dual_core
west build -t run
```

**译注：**原概述写Musca A1，本构建章节写Musca B1，后面的历史日志又使用`musca_a`名称；这里保留各处原型号和目标名称，不把它们统一改成某一开发板，也不据此声称这些组合已经验证。

## 84.3\_合并Musca镜像

使用第三方工具srecord生成Intel格式的十六进制镜像（Hex Image）；详细用法见[Srecord手册](https://srecord.sourceforge.net/man/man1/srec_cat.1.html)。

第一条原命令使用`$IMAGE_OFFSET`和`$IMAGE_NS_OFFSET`两个偏移量（Offset）变量，第二条是原文给出的Musca B1示例：

```sh
srec_cat zephyr.bin -Binary -offset $IMAGE_OFFSET zephyr_nonsecure.bin -Binary -offset $IMAGE_NS_OFFSET -o dual_core_zephyr.hex -Intel

# This command is an example for Musca B1
srec_cat zephyr.bin -Binary -offset 0xA000000 zephyr_nonsecure.bin -Binary -offset 0xA060400 -o dual_core_zephyr.hex -Intel
```

注释的意思是“此命令为Musca B1的示例”。原输入文件`zephyr.bin``zephyr_nonsecure.bin`、偏移量`0xA000000``0xA060400`和输出`dual_core_zephyr.hex`均保留。

## 84.4\_串口设置与原始输出

用minicom、PuTTY等串口终端（Serial Terminal）连接开发板，采用速率115200、8个数据位（Data Bits）、无校验（Parity：None）、1个停止位（Stop Bit）。ISR为中断服务程序（Interrupt Service Routine）。复位开发板后，串口输出如下：

```text
***** Booting Zephyr OS zephyr-v1.13.0-3378-g3625524 *****
IPM MHU sample on musca_a
CPU 0, get MHU0 success!
***** Booting Zephyr OS zephyr-v1.13.0-3378-g3625524 *****
IPM MHU sample on musca_a_nonsecure
CPU 1, get MHU0 success!
MHU ISR on CPU 0
MHU ISR on CPU 1
MHU Test Done.
```

`get MHU0 success`表示取得MHU0成功；`ISR`为中断服务程序（Interrupt Service Routine），日志分别显示CPU0与CPU1的中断处理，最后输出测试完成。`zephyr-v1.13.0-3378-g3625524`为原文历史日志版本。

源码入口：[官方示例目录](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/drivers/ipm/ipm_mhu_dual_core)。

另见[IPM公共接口](P058_处理器间消息公共接口.md)。

---

[上一章：NXPLPC处理器间邮箱示例](P083_NXPLPC处理器间邮箱示例.md) · [下一章：处理器间通信服务目录](P085_处理器间通信服务目录.md) · [返回大纲](大纲.md)
