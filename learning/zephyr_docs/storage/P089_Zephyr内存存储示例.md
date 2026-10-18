---
id: learning.zephyr-docs.storage.kvsssample-2
title: Zephyr内存存储示例
kind: reference
status: maintained
domains: [zephyr, storage]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/kvss/zms/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="zms"></a>

# 第89章\_Zephyr内存存储示例

原文：[Zephyr Memory Storage (ZMS)](https://docs.zephyrproject.org/latest/samples/subsys/kvss/zms/README.html)。读取日期：2026-10-13，`latest`。

## 89.1\_保存、读取与枚举

本示例演示**Zephyr 内存存储（Zephyr Memory Storage，ZMS）**保存、读回和删除**标识符/值对（ID/Value Pair）**的方法。

通过**迭代器（Iterator）**接口 `zms_iter_init()` 和 `zms_iter_next()`，应用可以枚举全部有效条目，不必预先声明标识符列表；通过 `zms_iter_init_with_config()` 还可使用**掩码（Mask）**、**范围（Range）**或**谓词（Predicate）**过滤。每个枚举函数在整个遍历期间持有 `fs->zms_lock`，阻止其他线程同时写入。

[官方示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/subsys/kvss/zms)。

## 89.2\_示例数据与循环流程

原文说明存储以下数据：

| 数据 | 标识符与内容 |
| --- | --- |
| 互联网协议（Internet Protocol，IP）地址字符串 | `id=1`，`data="192.168.1.1"` |
| 二进制数据块（Binary Blob） | `id=0xbeefdead`，`data={0xDE, 0xAD, 0xBE, 0xEF, 0xDE, 0xAD, 0xBE, 0xEF}` |
| 32 位变量 | `id=2`，`data=cnt` |
| 较长数据 | 128 字节 |

循环中先挂载存储系统，再写入上述全部数据。每经过 `CONFIG_DELETE_ITERATION` 配置规定的周期，就删除全部数据并验证删除结果。示例还会生成标识符递增的标识符/值对，将它们写到存储已满，然后删除并验证存储为空。

读写循环完成后，先执行一次完整迭代，再执行一次掩码迭代；每个有效条目输出标识符、当前存储长度及**历史版本深度（Revision Depth）**，即 `zms_read_hist()` 可访问的历史版本数量。

## 89.3\_要求与构建

要求具备闪存支持的开发板，或使用 `native_sim` 主机原生模拟目标。示例可面向多个平台构建，但原页说明当时仅在 `native_sim` 上测试。

官方页面生成的命令如下：

```shell
west build -b None samples/subsys/kvss/zms
```

译注：命令中的 `None` 是原网页内容，不是应直接使用的开发板目标。按本页所述的 `native_sim` 场景构建时，将 `-b None` 改为 `-b native_sim`；其余示例路径保持不变。在已配置 Zephyr 环境的 Linux 开发终端中，从 Zephyr 源码根目录执行构建，再运行生成的主机程序。本文未执行该构建。

## 89.4\_官方输出

在 `native_sim` 上运行后，控制台显示多轮读取、写入、删除操作。以下保留原输出，包括旧操作系统（Operating System，OS）构建标识、长数组换行和最终枚举结果。`ITERATION` 表示循环轮次，`IP_ADDRESS` 表示 IP 地址字段。

```console
*** Booting Zephyr OS build v3.7.0-2383-g624f75400242 ***
[00:00:00.000,000] <inf> fs_zms: 3 Sectors of 4096 bytes
[00:00:00.000,000] <inf> fs_zms: alloc wra: 0, fc0
[00:00:00.000,000] <inf> fs_zms: data wra: 0, 0
ITERATION: 0
Adding IP_ADDRESS 172.16.254.1 at id 1
Adding key/value at id beefdead
Adding counter at id 2
Adding Longarray at id 3
[00:00:00.000,000] <inf> fs_zms: 3 Sectors of 4096 bytes
[00:00:00.000,000] <inf> fs_zms: alloc wra: 0, f80
[00:00:00.000,000] <inf> fs_zms: data wra: 0, 8c
ITERATION: 1
ID: 1, IP Address: 172.16.254.1
Adding IP_ADDRESS 172.16.254.1 at id 1
Id: beefdead, Key: de ad be ef de ad be ef
Adding key/value at id beefdead
Id: 2, loop_cnt: 0
Adding counter at id 2
Id: 3, Longarray: 0 1 2 3 4 5 6 7 8 9 a b c d e f 10 11 12 13 14 15 16 17 18 19 1a 1b 1c 1d 1e 1f 20 21 22 23 24 25 26 27 28 29 2a 2b 2c 2d 2e 2f 30 31 32 33 34 35 36 37 38 39 3a 3b 3c 3d 3e 3f 40 41 42 43 44 45 46 47 48 49 4a 4b 4c 4d 4e 4f 50 51 52 53 5
4 55 56 57 58 59 5a 5b 5c 5d 5e 5f 60 61 62 63 64 65 66 67 68 69 6a 6b 6c 6d 6e 6f 70 71 72 73 74 75 76 77 78 79 7a 7b 7c 7d 7e 7f
Adding Longarray at id 3
.
.
.
.
.
.
[00:00:00.000,000] <inf> fs_zms: 3 Sectors of 4096 bytes
[00:00:00.000,000] <inf> fs_zms: alloc wra: 0, f40
[00:00:00.000,000] <inf> fs_zms: data wra: 0, 80
ITERATION: 299
ID: 1, IP Address: 172.16.254.1
Adding IP_ADDRESS 172.16.254.1 at id 1
Id: beefdead, Key: de ad be ef de ad be ef
Adding key/value at id beefdead
Id: 2, loop_cnt: 298
Adding counter at id 2
Id: 3, Longarray: 0 1 2 3 4 5 6 7 8 9 a b c d e f 10 11 12 13 14 15 16 17 18 19 1a 1b 1c 1d 1e 1f 20 21 22 23 24 25 26 27 28 29 2a 2b 2c 2d 2e 2f 30 31 32 33 34 35 36 37 38 39 3a 3b 3c 3d 3e 3f 40 41 42 43 44 45 46 47 48 49 4a 4b 4c 4d 4e 4f 50 51 52 53 5
4 55 56 57 58 59 5a 5b 5c 5d 5e 5f 60 61 62 63 64 65 66 67 68 69 6a 6b 6c 6d 6e 6f 70 71 72 73 74 75 76 77 78 79 7a 7b 7c 7d 7e 7f
Adding Longarray at id 3
Enumerating live entries with zms_iter_next:
id=0x3, len=128, revisions=9
id=0x2, len=4, revisions=9, data=08000000
id=0xbeefdead, len=8, revisions=9, data=deadbeefdeadbeef
id=0x1, len=12, revisions=9
Memory is full let's delete all items
Free space in storage is 8064 bytes
Sample code finished Successfully
```

译注：概览中的 IP 地址为 `192.168.1.1`，输出却使用 `172.16.254.1`；两处都按原文保留。示例输出最后报告可用空间 8064 字节并成功结束，不是本地测试结果。

相关参考：[ZMS接口](P059_Zephyr内存存储接口.md)。

---

[上一章：非易失性存储示例](P088_非易失性存储示例.md) · [下一章：ZMS循环计数验证示例](P090_ZMS循环计数验证示例.md) · [返回大纲](大纲.md)
