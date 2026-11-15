---
id: learning.zephyr-docs.intercore_reference.ipmsample-78
title: ESP32闪存IPM示例
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/samples/boards/espressif/flash_ipm/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="flash-ipm"></a>

# 第78章\_ESP32闪存IPM示例

原文：[Flash IPM on ESP32](https://docs.zephyrproject.org/latest/samples/boards/espressif/flash_ipm/README.html)。读取日期：2026-10-13，`latest`。

本例展示如何通过处理器间消息（Inter-Processor Messaging，IPM），让运行在CPU1（`appcpu``lpcore`）上的程序调用CPU0（`procpu``hpcore`）执行闪存（Flash）应用程序编程接口（Application Programming Interface，API）操作。CPU 指中央处理器（Central Processing Unit）；括号中的名称按原文保留。当远端CPU1无法直接访问闪存硬件时，可把闪存操作交给负责管理的核心。

原日志中的OS表示操作系统（Operating System），日志版本字符串和计数值按原样保留。


## 78.1\_执行流程与测试过程

CPU0先初始化IPM服务和闪存子系统；CPU0就绪后，CPU1启动并通过IPM通道连接CPU0。

CPU1依次执行：

1. 擦除`storage_partition`存储分区的第一页，共4096字节。
2. 验证该页已擦空。
3. 写入从`0x00`到`0x7F`的简单递增模式。
4. 回读相同数据，验证写入模式。

CPU1输出成功消息后结束；CPU0继续作为闪存管理核心（Flash Supervisor）运行，等待后续请求。

## 78.2\_硬件要求与构建

运行本示例需要带闪存芯片的`esp32s3_devkitc`开发板。通过系统构建（Sysbuild）构建原示例：

```sh
west build -b esp32s3_devkitc/esp32s3/procpu --sysbuild samples/boards/espressif/flash_ipm/
```

## 78.3\_原始输出与读取说明

运行`west espressif monitor`，或使用minicom、PuTTY、screen等串口控制台（Serial Console）程序查看输出。

原输出依次说明程序运行于远端CPU、使用`storage_partition`执行闪存API测试，并提示在主机（Host）CPU控制台手动读取测试区域。擦除、擦空验证、写入模式和回读验证均显示`OK`。末尾保留了两组递增模式的十六进制转储（Hex Dump）。

```text
*** Booting Zephyr OS build v4.3.0-rc1-14-gd840aed36685 ***
uart:~$
Flash IPM sample program (remote CPU)

This program is running on a remote CPU.
Partition storage_partition will be used to perform flash API.

To inspect the test area manually, run on HOST CPU console:
 $ flash read 3b0000 1000

Step 1: Erase
* Erasing first 4096 bytes of partition.. OK
* Verifying page erased.. OK
Step 2: Write
* Write ascii pattern..OK
Step 3: Verify
* Verifying pattern.. OK

uart:~$
uart:~$ flash read 3b0000 100
003B0000: 00 01 02 03 04 05 06 07  08 09 0a 0b 0c 0d 0e 0f |........ ........|
003B0010: 10 11 12 13 14 15 16 17  18 19 1a 1b 1c 1d 1e 1f |........ ........|
003B0020: 20 21 22 23 24 25 26 27  28 29 2a 2b 2c 2d 2e 2f | !"#$%&' ()*+,-./|
003B0030: 30 31 32 33 34 35 36 37  38 39 3a 3b 3c 3d 3e 3f |01234567 89:;<=>?|
003B0040: 40 41 42 43 44 45 46 47  48 49 4a 4b 4c 4d 4e 4f |@ABCDEFG HIJKLMNO|
003B0050: 50 51 52 53 54 55 56 57  58 59 5a 5b 5c 5d 5e 5f |PQRSTUVW XYZ[\]^_|
003B0060: 60 61 62 63 64 65 66 67  68 69 6a 6b 6c 6d 6e 6f |`abcdefg hijklmno|
003B0070: 70 71 72 73 74 75 76 77  78 79 7a 7b 7c 7d 7e 7f |pqrstuvw xyz{|}~.|
003B0080: 00 01 02 03 04 05 06 07  08 09 0a 0b 0c 0d 0e 0f |........ ........|
003B0090: 10 11 12 13 14 15 16 17  18 19 1a 1b 1c 1d 1e 1f |........ ........|
003B00A0: 20 21 22 23 24 25 26 27  28 29 2a 2b 2c 2d 2e 2f | !"#$%&' ()*+,-./|
003B00B0: 30 31 32 33 34 35 36 37  38 39 3a 3b 3c 3d 3e 3f |01234567 89:;<=>?|
003B00C0: 40 41 42 43 44 45 46 47  48 49 4a 4b 4c 4d 4e 4f |@ABCDEFG HIJKLMNO|
003B00D0: 50 51 52 53 54 55 56 57  58 59 5a 5b 5c 5d 5e 5f |PQRSTUVW XYZ[\]^_|
003B00E0: 60 61 62 63 64 65 66 67  68 69 6a 6b 6c 6d 6e 6f |`abcdefg hijklmno|
003B00F0: 70 71 72 73 74 75 76 77  78 79 7a 7b 7c 7d 7e 7f |pqrstuvw xyz{|}~.|
```

**译注：**日志中的`v4.3.0-rc1-14-gd840aed36685`、分区读取地址及长度均为原示例输出；这里保留原值，不将其认定为本仓库或其他板卡的当前分区布局。闪存擦写发生在原例指定的存储分区，以上为文档翻译，没有执行测试。

源码入口：[官方示例目录](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/boards/espressif/flash_ipm)。

另见[IPM公共接口](P058_处理器间消息公共接口.md)。

---

[上一章：ZephyrIPM到邮箱适配绑定](P077_ZephyrIPM到邮箱适配绑定.md) · [下一章：处理器间邮箱示例目录](P079_处理器间邮箱示例目录.md) · [返回大纲](大纲.md)
