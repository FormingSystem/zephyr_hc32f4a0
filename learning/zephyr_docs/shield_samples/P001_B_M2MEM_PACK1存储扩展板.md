---
id: learning.zephyr-docs.shield-samples.page-1
title: B_M2MEM_PACK1存储扩展板
kind: reference
status: maintained
domains: [zephyr, shields, samples]
source_url: https://docs.zephyrproject.org/latest/samples/shields/b_m2mem_pack1/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="b-m2mem-pack1"></a>

# 第1章\_B-M2MEM-PACK1 扩展板（Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/shields/b_m2mem_pack1/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/shields/b_m2mem_pack1/README.rst/..)

<a id="overview"></a>

## 1.1 概述（Overview）

ST B-M2MEM-PACK1 M.2 串行存储模块搭载两种器件：串行 NOR 闪存，以及描述模块信息的 I2C EEPROM。本示例读取 EEPROM，打印模块声明的信息，再对闪存执行三项测试，检查声明是否一致、存储器是否可用。 相关链接：[ST B-M2MEM-PACK1 M.2 串行存储扩展板文档](https://docs.zephyrproject.org/latest/boards/shields/st_b_m2mem_pack1/doc/index.html#st-b-m2mem-pack1-shield)。

测试包括：

> 译注——实际范围：main.c 在闪存偏移 0xff000 处擦除 4096 字节，再写入并回读 13 12 67 69 12 这五个十六进制字节。末尾双灯常亮只表示测试结束，是否通过要看各项结果与计数。

1. 比较 JEDEC 标识：运行时读取闪存的 JEDEC ID，与标识 EEPROM 中该存储位置的记录比较。不一致表示模块实际器件与 EEPROM 描述不符。

2. 擦除（Erase）：擦除一个扇区并检查操作是否成功。后续测试依赖该步骤，因此擦除失败时示例会停止。

> 译注——校验限制：当前 erase_flash_test() 在读到 0xFF 后，在循环体和循环更新处各递增一次索引，实际上只核对偶数偏移字节；flash_erase() 的错误返回值也可能被后续读取覆盖。因此 TEST 2 PASS 不是逐字节验证整个扇区擦除成功的充分证据。这是当前上游源码的行为，译文没有修改示例实现。

3. 写入与回读（Write and read back）：向已擦除的扇区写入已知模式，再读回检查。

第一项测试要求闪存节点包含 `jedec-id` 属性。没有该属性的扩展板变体会跳过第一项，只运行其余两项测试。

结果既输出到控制台，也通过扩展板上的两个 LED 表示，因此没有串口终端也可使用：

| LED 行为 | 含义 |
| --- | --- |
| 交替闪烁 | 即将开始一项测试 |
| 绿灯亮 2 秒 | 该项测试通过 |
| 红灯亮 2 秒 | 该项测试失败 |
| 两灯持续亮起 | 全部测试结束 |

<a id="requirements"></a>

## 1.2 硬件与配置要求（Requirements）

需要一块具有 M.2 Key A 插槽的开发板，按 ST 串行存储连接器引脚定义接线，参见 [UM3611](https://www.st.com/resource/en/user_manual/um3611-m2-serial-memory-pack-for-nucleo144-boards-stmicroelectronics.pdf)；还需提供 `m2mem_connector` 节点及 [ST B-M2MEM-PACK1 M.2 串行存储扩展板文档](https://docs.zephyrproject.org/latest/boards/shields/st_b_m2mem_pack1/doc/index.html#st-b-m2mem-pack1-shield)所列标签，并装入 B-M2MEM-PACK1 模块。测试会向闪存偏移 `0xff000` 处写入，因此该位置原有数据会丢失。

<a id="building-and-running"></a>

## 1.3 构建与运行（Building and Running）

> 译注——执行前提：主机命令在读者自己的 Zephyr 源码根目录，使用 UCRT64 Bash 或 Linux Bash 执行；先按[入门指南](../getting_started/大纲.md)准备模块和工具链，再核对本页指定主开发板、扩展板、接线与配置。设备 Shell 命令在目标板串口执行。遇到构建或设备就绪错误，先回查所选 board／shield 与接线；下方日志是官方预期示例。本次仅核对文档与源码，未构建、烧录、擦写存储或进行实板测量。

本例采用 [Nucleo U3C5ZI Q](https://docs.zephyrproject.org/latest/boards/st/nucleo_u3c5zi_q/doc/index.html#nucleo_u3c5zi_q) 开发板。选择与实际安装模块匹配的扩展板变体：

```text
west build -b nucleo_u3c5zi_q --shield b_m2mem_pack1_mb1928_33lb samples/shields/b_m2mem_pack1
west flash
```

其他变体为 `b_m2mem_pack1_mb1927_18ba`、`b_m2mem_pack1_mb1927_33ba` 和 `b_m2mem_pack1_mb1928_33la`。

<a id="sample-output"></a>

## 1.4 示例输出（Sample Output）

首先打印从 EEPROM 读取的板卡信息，随后按测试逐段输出：

```text
==============================================
 B-M2MEM-PACK1 shield test
==============================================
ID EEPROM size: 16384 bytes
Board: nucleo_u3c5zi_q

EEPROM board information
----------------------------------------------
Card part number:           MB1928-33LB-C01
...

----------------------------------------------
TEST 1: Compare JEDEC ID's:
----------------------------------------------
JEDEC ID - devicetree:       ef 40 15
JEDEC ID - eeprom:           ef 70 15
jedec id stored in eeprom doesn't match one in devicetree.
TEST 1: FAIL
----------------------------------------------

----------------------------------------------
TEST 2: Erase flash section and verify erased:
----------------------------------------------
flash_erase success.
TEST 2: PASS
----------------------------------------------

----------------------------------------------
TEST 3: Write flash section and verify written:
----------------------------------------------
Data written matches data read.
TEST 3: PASS
----------------------------------------------

==============================================
 All tests completed: 2/3 passed
==============================================
```

<a id="known-result-on-mb1928-33lb"></a>

## 1.5 MB1928-33LB 上的已知结果

上方运行结果是该模块的预期表现。它的 EEPROM 记录 JEDEC ID 为 `ef 70 15`，但实际安装的 W25Q16JV 返回 `ef 40 15`。第二个字节表示存储器类型，用于区分同一器件的两种订购选项：`40` 是实际安装的普通 SPI 变体，`70` 是双倍传输率（Double Transfer Rate，DTR）变体。

> 译注——版本差异：原文日志显示 devicetree／eeprom 比较；本次获取的 compare_jedec_test() 调用 flash_read_jedec_id()，再与 EEPROM 的 JEDEC_MemA 前三个字节比较。日志来自官方文档的既有记录，不应要求当前版本逐字输出相同文本。

设备树（Devicetree）中的值是正确的，并且每次启动都会校验：闪存驱动在切换到四线模式（Quad mode）前读取 JEDEC ID，与 `jedec-id` 属性比较；两者不一致时，设备不会进入就绪状态。

错误存在于 ST 发布的参考 EEPROM 记录中，并非某一块模块单独烧写有误，因此 TEST 1 仍保留严格检查。它报告的是真实不一致，而另外两项闪存测试仍会运行并通过。

<a id="see-also"></a>

## 1.6 另请参阅（See also）

[闪存（Flash）](../flash_reference/P001_Flash公共接口.md)

[电可擦可编程只读存储器（EEPROM）](../hardware/P040_EEPROM接口参考.md)

[通用输入输出（GPIO）](../hardware/P266_GPIO公共接口.md)

> 译注——源码入口：[src/main.c（上游）](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/shields/b_m2mem_pack1/src/main.c)；[CMakeLists.txt（上游）](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/shields/b_m2mem_pack1/CMakeLists.txt)；[prj.conf（上游）](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/shields/b_m2mem_pack1/prj.conf)。本地源码使用相对链接；上游快照摘要见来源记录，本地版本可能不同。

对应官方文档源码：[samples/shields/b_m2mem_pack1/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/shields/b_m2mem_pack1/README.rst)。

[返回大纲](大纲.md) · [下一章](P002_LMP90100电阻温度检测.md)
