---
id: learning.zephyr-docs.board-samples.page-1
title: STM32备份SRAM
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/st/backup_sram/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="stm32_backup_sram"></a>

# 第1章\_备份 SRAM（Backup SRAM）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/st/backup_sram/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/st/backup_sram/README.rst/..)

<a id="overview"></a>

## 1.1 概述（Overview）

多种 STM32 微控制器具有一小块备份静态随机存取存储器（Backup SRAM）。当 VBAT 引脚由电压源供电，例如使用纽扣电池时，可将其用作非易失性存储（Non-Volatile Memory，NVM）。

> 译注——保持条件：这里的 NVM 用法依赖备份电源持续有效，SRAM 本身并没有变成断电后仍可永久保存数据的 Flash。断开主电源与断开 VBAT 是不同测试；跳线位置、电压和备份域保持条件按具体板原理图与芯片参考手册确认。

本示例展示如何在备份 SRAM 中定义变量。应用每次运行时先显示当前值，再将其加一；若 VBAT 供电保持有效，下次重新上电时就会显示递增后的值。

注意（Note）

大多数开发板通常通过跳线将 VBAT 接到 VDD。若要使用独立的 VBAT 电源验证本示例，需要移除该跳线。

<a id="building-and-running"></a>

## 1.2 构建与运行（Building and Running）

> 译注——执行环境与文件：以下构建命令从读者自己的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行。先按[入门指南](../getting_started/大纲.md)准备工具链、west 工作区和相应板定义；`samples/...` 是官方原有应用目录。原命令给出的板名仅对应示例，未显式给出 `-b` 时应指定实际受支持的板，不能依赖未知缓存。设备树和 Kconfig 片段写入相应配置文件，不作为终端命令执行；构建输出由工具生成。构建成功后按板文档烧录，并按正文核对串口或硬件现象，失败时回查配置、设备就绪和连接条件。本次仅翻译与核对来源，未执行构建、烧录或硬件实验。

运行本示例前，确保在板级设备树（DT）文件中启用 `backup_sram` 节点。

```text
west build -b nucleo_h743zi samples/boards/st/backup_sram
```

<a id="sample-output"></a>

### 1.2.1 输出示例（Sample Output）

> 译注——初始化与观察：本次 main.c 使用 `BACKUP_MAGIC` 标记判断数据是否有效，无效时将计数清零，再显示当前值并递增；启用数据缓存管理时还会刷新该结构的缓存。因此首次值为 0、后续递增以及失去保持后的重新初始化，应结合魔数检查和供电状态解释，不能仅凭某次数字相同判断保持功能失效。

```text
Current value in backup SRAM: 11
Next reported value should be: 12
Keep VBAT power source and reset the board now!
```

> 译注——源码入口：[samples/boards/st/backup_sram/src/main.c](../../../samples/boards/st/backup_sram/src/main.c)；[samples/boards/st/backup_sram/prj.conf](../../../samples/boards/st/backup_sram/prj.conf)。链接相对于所在译文，可随仓库移动；本地源码版本可能与官网快照不同。

对应官方文档源码：[samples/boards/st/backup_sram/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/st/backup_sram/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/st/backup_sram/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[返回大纲](大纲.md) · [下一章](P002_STM32内核耦合存储器.md)
