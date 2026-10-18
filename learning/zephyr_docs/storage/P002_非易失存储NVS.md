---
id: learning.zephyr-docs.storage.nvs
title: 非易失存储NVS
kind: reference
status: maintained
domains: [zephyr, storage]
source_url: https://docs.zephyrproject.org/latest/services/storage/nvs/nvs.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第2章\_非易失存储NVS

原文：[Non-Volatile Storage (NVS)](https://docs.zephyrproject.org/latest/services/storage/nvs/nvs.html)。读取日期：2026-10-12，`latest`。

**非易失存储（Non-Volatile Storage，NVS）**把 ID 与数据组成的键值对，保存在按 **先进先出（First In, First Out，FIFO）** 管理的 Flash 循环缓冲区中。区域分为多个扇区，条目依次追加到当前扇区；空间耗尽后准备下一个扇区，即擦除它。在擦除前，检查其中需要保留的 ID—数据对是否还存在于正在使用的其他扇区，若不存在就先复制。

ID 是十六位无符号数。NVS 保证每个在用 ID 始终至少有一份 ID—数据对保存在 Flash 中。它能够保存二进制数据块、字符串、整型、长整型以及这些数据的组合。

## 2.1\_存储格式与写入顺序

每个条目包含八字节元数据和数据。元数据表从扇区末端开始写入，数据从扇区起点依次写入。元数据包含 ID、数据在扇区中的偏移、数据长度、未使用的 `part` 字段和 **循环冗余校验（Cyclic Redundancy Check，CRC）**。这里的 CRC 只覆盖元数据，用于确认一次写入已经完成；可通过 Kconfig 配置项 `CONFIG_NVS_DATA_CRC` 为实际数据另加可选的 CRC-32。

> 原文注意：只有读取条目的全部数据才检查数据 CRC。CRC 位于数据区末尾，部分读取不会检查它。对于已有且未启用数据 CRC 的 NVS 内容，随后启用该功能会使所有已有数据失效。

NVS 总是先写数据，再写元数据。初始化时忽略没有对应元数据的数据；也会检查 Flash 中的记录，忽略元数据缺失或错误的内容。写入前先检查 ID—数据对，如果与已有内容相同，则不执行 Flash 写入。

应预留足够空闲空间，避免频繁擦除。NVS 具有防止空闲空间过少时陷入擦除页死循环的保护机制；检测到这种循环时返回空间不足。

## 2.2\_声明存储实例

原文通过下列结构声明 NVS 实例：

```c
static struct nvs_fs fs = {
.flash_device = NVS_FLASH_DEVICE,
.sector_size = NVS_SECTOR_SIZE,
.sector_count = NVS_SECTOR_COUNT,
.offset = NVS_STORAGE_OFFSET,
};
```

| 参数 | 含义与约束 |
| --- | --- |
| `NVS_FLASH_DEVICE` | 所用 Flash 设备引用，设备必须处于可工作状态 |
| `NVS_SECTOR_SIZE` | 扇区大小，必须是 Flash 擦除页大小的整数倍，而且是 2 的幂 |
| `NVS_SECTOR_COUNT` | 扇区数量，至少为 2；始终保留一个空扇区，以便复制现有数据 |
| `NVS_STORAGE_OFFSET` | 存储区域在 Flash 中的偏移 |

## 2.3\_Flash磨损与寿命估算

Flash 寿命受可擦除次数限制，因此写入设计需要研究磨损。Flash 按页擦除，页大小由硬件决定。例如，原文使用 nRF51822 的 1024 字节页和每页约 20,000 次擦除作为估算前提。

假设有一个每分钟变化一次、重启后需要恢复的四字节状态变量；NVS 扇区大小为 1024 字节，共两个扇区。每次记录消耗十二字节，即八字节元数据加四字节数据。按原文近似计算，第一个扇区在 `1024 / 12 = 85.33` 分钟后写满，再过 85.33 分钟第二个也写满；约运行 171 分钟后需要复用并擦除第一个扇区。以 20,000 次擦除估算，总寿命约为 `171 × 20,000` 分钟，即约 6.5 年。

更一般地，设 `NS` 为每分钟存储请求次数，`DS` 为数据字节数，`SECTOR_SIZE` 为扇区字节数，`PAGE_ERASES` 为页可擦除次数，则预期寿命为：

```text
SECTOR_COUNT * SECTOR_SIZE * PAGE_ERASES / (NS * (DS+8)) minutes
```

如果估算寿命太短，可以增加 `SECTOR_COUNT` 或 `SECTOR_SIZE`。

> 译注：以上是原文简化估算，不是任何芯片的寿命保证。实际记录需要整数个槽位，还可能有写对齐、可选 CRC、维护信息、有效记录搬移和额外写入开销；HC32 的擦除粒度和耐久次数应以本芯片手册为准。公式中的 `SECTOR_COUNT` 即配置的扇区数量。

## 2.4\_写块大小迁移

**设备固件升级（Device Firmware Upgrade，DFU）**可能更换 Flash 驱动支持的最小写块大小。只要物理分配表条目（ATE）大小不变，NVS 的 Flash 镜像仍然兼容；尤其允许在 1、2、4、8 字节写块大小之间迁移。

## 2.5\_示例与故障排查

示例位于 `samples/subsys/kvss/nvs`，见 [NVS 存储与读取示例](P088_非易失性存储示例.md)。

原文列出的故障为：使用 NVS 时发生 **内存保护单元（Memory Protection Unit，MPU）** 故障，或返回 `-ETIMEDOUT`。使用 **片上系统（System on Chip，SoC）** 内部 Flash 且启用内存保护单元（MPU）时，相关 Flash 驱动要求对 Flash 内存具备读、写、执行权限，可通过 `CONFIG_MPU_ALLOW_FLASH_WRITE` 配置。如果禁用该选项，且使用内部 Flash 的 NVS 应用是唯一运行的线程，可能发生 MPU 故障；在多线程应用中，原文称另一线程可能截获该故障，最终 NVS **应用程序编程接口（Application Programming Interface，API）** 返回 `-ETIMEDOUT`。

> 译注：这段排查说明依赖具体架构与 Flash 驱动，不能据此断言所有 SoC 的 NVS 都要求可写可执行 Flash，也不能把任意 `-ETIMEDOUT` 都归因于 MPU。应结合实际故障日志、驱动实现和内存保护配置定位。

## 2.6\_API参考

接口由 `nvs.h` 提供，分为 [NVS 数据结构](P054_非易失性存储数据结构目录.md)和 [NVS 操作 API](P055_非易失性存储接口.md)。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Flash分区映射](P001_Flash分区映射.md) · [本模块主线目录](../reading/storage.md) · [全部主线](../reading/README.md) · [下一篇：Flash循环缓冲区](P003_Flash循环缓冲区.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：Flash分区映射](P001_Flash分区映射.md) · [下一章：Flash循环缓冲区](P003_Flash循环缓冲区.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
