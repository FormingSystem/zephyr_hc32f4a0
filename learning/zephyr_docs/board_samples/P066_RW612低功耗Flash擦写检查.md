---
id: learning.zephyr-docs.board-samples.page-66
title: RW612低功耗Flash擦写检查
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/nxp/frdm_rw612/pm_flash_check/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="rw612_pm_flash_check"></a>

# 第66章\_RW612 电源管理后的 Flash 检查（RW612 PM flash check）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/nxp/frdm_rw612/pm_flash_check/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/nxp/frdm_rw612/pm_flash_check/README.rst/..)

<a id="overview"></a>

## 66.1 概述（Overview）

本示例依次进入 FRDM-RW612 支持的各个 Zephyr 低功耗状态：PM1 `RUNTIME_IDLE`、PM2 `SUSPEND_TO_IDLE` 和 PM3 `STANDBY`。每次进入／退出前后，均对外部 NOR Flash 的一个临时扇区执行擦除、写入及读回，以判断 Flash 是否正常工作，并打印各模式的 PASS／FAIL 及最终汇总。判断仅针对功能：如果唤醒后 `flash_erase`、`flash_write`、`flash_read` 工作正常，就认为 Flash 状态正常。

从 PM3 唤醒时，FlexSPI 控制器配置会丢失；ROM 只恢复基于 FCB 的最小 LUT。Flash 驱动的电源域 `TURN_ON` 恢复过程会重新初始化控制器，使 Flash API 继续工作。

> 译注——术语：FCB 是 Flash 配置块（Flash Configuration Block），LUT 是查找表（Lookup Table），SFDP 是串行 Flash 可发现参数（Serial Flash Discoverable Parameters），XIP 是原地执行（eXecute-In-Place）。重新探测用于恢复控制器和 Flash 参数，不能据此将此测试解释成全器件可靠性或寿命验证。

测试使用的临时区是 `app.overlay` 定义的 `scratch` 固定分区，位于 64 MiB NOR 中偏移 48 MiB 处，远离 XIP 镜像。

> 译注——写入范围：这不是只读检查。本次 overlay 的 scratch 分区位于 0x03000000、大小 16 KiB；每次检查从该偏移擦除 4 KiB，写入并读回比较 256 字节。三个模式的进入前后均会重复操作，运行前必须确认该区域可用于测试，不得存放需要保留的数据。

<a id="requirements"></a>

## 66.2 前提条件（Requirements）

- FRDM-RW612 开发板。

- 外部 NOR Flash（W25Q512JV），以及 Flash 驱动中的 FlexSPI PM 恢复支持，即 `PM_DEVICE_ACTION_TURN_ON` 时重新探测。

<a id="building-flashing-and-running"></a>

## 66.3 构建、烧录与运行（Building, Flashing and Running）

> 译注——执行前提：west 命令从读者的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行；先按[入门指南](../getting_started/大纲.md)准备工具链、模块及对应板。构建产物由工具生成，下载与启动按具体板文档核对。本次未执行构建、烧录或硬件测量。

```text
# From the root of the zephyr repository
west build -b frdm_rw612 samples/boards/nxp/frdm_rw612/pm_flash_check
west flash
```

以 115200 波特率打开串口终端，然后复位开发板。预期输出以以下内容结束：

> 译注——验证范围：PASS 表示调用返回成功且读回的 256 字节与写入模式匹配；它不证明所有地址、所有时序或最低功耗都已验证。三个状态请求的睡眠时长依次为 100 ms、200 ms、2000 ms，PM 通知器只打印与当前待测状态匹配的事件。

```text
=== SUMMARY: PASS (0 failures) ===
```

<a id="notes"></a>

## 66.4 说明（Notes）

- 示例使用 `pm_state_force()` 强制选择每个电源状态，使待测状态确定。原文称最后强制选择的状态持续有效，因此示例最后忙等，不返回空闲线程，否则会不断重新进入 PM3 并释放 SWD 调试端口。

> 译注——原文与实现差异：上面“最后状态持续有效、末尾忙等”的说法与下一条一次性说明并不一致。本次 subsys/pm/pm.c 在消费强制状态时将其清空；本次 main.c 末尾实际锁住 STANDBY 和 SUSPEND_TO_IDLE，打印汇总后 k_sleep(K_FOREVER)，不是忙等。正文保留原文，行为以所用版本源码为准。

- `pm_state_force()` 是一次性的：第一次进入空闲时就会消耗该强制状态，因此强制执行 PM3 周期后，在示例线程恢复前，内核可能短暂按默认策略重新进入较浅状态。因此 PM 通知器只报告待测状态。

- `CONFIG_IDLE_STACK_SIZE` 增大到 2048，因为从 PM3 唤醒时，Flash 的 `TURN_ON` 恢复会在空闲线程上下文重新执行 SFDP 探测；探测本身约需 270 字节栈空间。任何将此驱动绑定到电源域的应用都有同样要求，参见 `FLASH_MCUX_FLEXSPI_NOR` 的 Kconfig 帮助。

<a id="see-also"></a>

## 66.5 另请参阅（See also）

[电源管理（Power Management，PM）](../power/P031_电源管理接口分组.md)

[闪存（Flash）](../flash_reference/P001_Flash公共接口.md)

> 译注——源码入口：仓库相对参照：[src/main.c](../../../samples/boards/nxp/frdm_rw612/pm_flash_check/src/main.c)；[prj.conf](../../../samples/boards/nxp/frdm_rw612/pm_flash_check/prj.conf)；[app.overlay](../../../samples/boards/nxp/frdm_rw612/pm_flash_check/app.overlay)；[subsys/pm/pm.c](../../../subsys/pm/pm.c)。本地版本可能与网页不同。

对应官方文档源码：[samples/boards/nxp/frdm_rw612/pm_flash_check/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/nxp/frdm_rw612/pm_flash_check/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/nxp/frdm_rw612/pm_flash_check/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P065_MCXE31B待机与唤醒.md) · [返回大纲](大纲.md) · [下一章](P067_NXP_MCX系统关闭.md)
