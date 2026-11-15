---
id: learning.zephyr-docs.storage.kvsssample-3
title: ZMS循环计数验证示例
kind: reference
status: maintained
domains: [zephyr, storage]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/kvss/zms/zms_cycle_count/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="zms-cycle-count"></a>

# 第90章\_ZMS循环计数验证示例

原文：[ZMS Cycle Count Verification](https://docs.zephyrproject.org/latest/samples/subsys/kvss/zms/zms_cycle_count/README.html)。读取日期：2026-10-13，`latest`。

## 90.1\_验证目标

本示例验证**Zephyr 内存存储（Zephyr Memory Storage，ZMS）**的扇区**再利用循环计数（Recycle Count）**接口：

- [`zms_get_num_cycles()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga31b8d970e70fd7cbb94a0dc068dbdcfc)：查询所有扇区中的最大循环计数。
- [`zms_get_sector_num_cycles()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga4aa193a3c357335a6d403139371803ab)：查询单个扇区循环计数。
- [`zms_sector_use_next()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga90a6f8c47f02641ca33ee42a7c709750)：主动推进到下一个扇区。

它检查多次强制推进扇区后返回的循环计数是否符合预期，并检查越过旧 `uint8_t` 计数器的**回绕（Wraparound）**边界后，计数是否仍正确增长。8 位计数器有 256 个取值，旧字段在这一边界发生回绕。

[官方示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/subsys/kvss/zms/zms_cycle_count)。

## 90.2\_三个验证阶段

| 阶段 | 操作与检查 |
| --- | --- |
| 阶段 1 | 挂载分区、清空，再推进扇区 30 次；检查计数等于 `base + PHASE1_ITERATIONS / SECTOR_COUNT` |
| 阶段 2 | 继续推进，直到相对循环计数超过 256，确认计数跨过历史 `uint8_t` 回绕点后仍增加 |
| 阶段 3 | 对每个扇区调用 [`zms_get_sector_num_cycles()`](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga4aa193a3c357335a6d403139371803ab)，确认各计数均不为 0；另外确认越界扇区索引返回 `-EINVAL` |

这里 `base` 是本次运行的基准计数，`PHASE1_ITERATIONS` 是阶段 1 推进次数常量，`SECTOR_COUNT` 是扇区数量常量；`-EINVAL` 表示无效参数错误。成功时打印 `PASS: cycle count verification succeeded`，即循环计数验证通过。

## 90.3\_要求与构建

要求具备闪存支持的开发板，或使用 `native_sim`。原文列出已测试目标为 `native_sim`、`qemu_x86` 和 `nrf7002dk/nrf5340/cpuapp`。

原网页命令如下：

```shell
west build -b None samples/subsys/kvss/zms/zms_cycle_count
```

译注：原页的 `-b None` 没有给出有效目标。选择上述 `native_sim` 场景时，应替换为 `-b native_sim`，保留示例路径；在已配置 Zephyr 环境的 Linux 终端中，从 Zephyr 源码根目录构建。示例会清空分区并强制多次推进扇区，不能将其当作只读状态查询。本译文未执行测试。

## 90.4\_基准值与官方输出

确切基准取决于存储分区已有状态。在持久闪存上每次重新运行示例，都会增加一个完整循环。下面是新闪存上 `base=1` 的原始记录；后续运行会从更高基准开始、以更高计数结束，但相对增长和 `PASS` 成功消息保持一致。OS 指操作系统（Operating System）。

```console
*** Booting Zephyr OS build v4.4.0-rc2 ***
[00:00:00.000,000] <inf> fs_zms: 3 Sectors of 4096 bytes
[00:00:00.000,000] <inf> fs_zms: alloc wra: 0, fc0
[00:00:00.000,000] <inf> fs_zms: data wra: 0, 0
[00:00:00.000,000] <inf> fs_zms: 3 Sectors of 4096 bytes
[00:00:00.000,000] <inf> fs_zms: alloc wra: 0, fc0
[00:00:00.000,000] <inf> fs_zms: data wra: 0, 0
After mount: num_cycles=1 (base=1)
--- Phase 1: 30 sector advances ---
After sector_use_next[1]: num_cycles=1
After sector_use_next[2]: num_cycles=2
After sector_use_next[3]: num_cycles=2
...
After sector_use_next[30]: num_cycles=11
Phase 1 expected=11, got=11
--- Phase 2: 741 sector advances to exceed 256 cycles above base ---
Phase 2 progress [3/741]: num_cycles=12
Phase 2 progress [6/741]: num_cycles=13
...
Phase 2 progress [741/741]: num_cycles=258
Final expected=258, got=258 (total_advances=771)
--- Phase 3: per-sector cycle count verification ---
Sector 0: cycles=258
Sector 1: cycles=258
Sector 2: cycles=257
PASS: cycle count verification succeeded (num_cycles=258 > 255)
```

该记录阶段 1 结束为 11，阶段 2 结束为 258，总共推进 771 次；三个扇区分别报告 258、258、257。这些数值用于解释官方记录，不表示当前仓库已运行验证。

相关参考：[ZMS接口](P059_Zephyr内存存储接口.md)。

---

[上一章：Zephyr内存存储示例](P089_Zephyr内存存储示例.md) · [下一章：闪存命令行示例](P091_闪存命令行示例.md) · [返回大纲](大纲.md)
