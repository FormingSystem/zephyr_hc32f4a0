---
id: learning.zephyr-docs.tfm.page-5
title: TFM与Zephyr集成
kind: reference
status: maintained
domains: [zephyr, tfm, security]
source_url: https://docs.zephyrproject.org/latest/services/tfm/integration.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_TFM与Zephyr集成

原文：[官方页面](https://docs.zephyrproject.org/latest/services/tfm/integration.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 5.1\_集成目标

本节介绍可信固件 M（Trusted Firmware-M，TF-M）与 Zephyr RTOS 的集成方式，帮助读者理解如何在 Cortex-M 平台上集成两者，并在 Zephyr 应用中使用 TF-M 安全运行时服务（Secure Run-Time Services）。

## 5.2\_开发板定义（Board Definitions）

将 [`CONFIG_BUILD_WITH_TFM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BUILD_WITH_TFM) 设为 `y` 后，构建 Zephyr 的同时会为安全处理环境（Secure Processing Environment，SPE）构建 TF-M。

不过，原文指出通常不应在应用层设置这个值，而应在带 `_ns` 后缀的板级变体（Board Variant）中设置 TF-M 所需的全部配置选项。

该变体必须定义合适的 Flash、SRAM 与外设配置，并考虑安全处理环境的初始化过程。还必须通过 [modules/trusted-firmware-m/Kconfig.tfm](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm) 将 [`CONFIG_TFM_BOARD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TFM_BOARD) 设置为 TF-M 期望的目标名称，使其知道应为哪个目标构建安全处理环境。

译注：`_ns` 是原文沿用的名称形式；下面的实际目标采用 `/ns` 限定符。板级配置负责确定安全／非安全资源边界，单独向应用添加开关不能代替处理器安全能力、TF-M 平台移植及内存布局配套。

## 5.3\_示例：mps2/an521/cpu0/ns

`mps2/an521/cpu0` 对应双核 Arm Cortex-M33 评估板，生成安全 Zephyr 二进制镜像。

可选目标 `mps2/an521/cpu0/ns` 额外设置下列 Kconfig 选项，表示 Zephyr 应构建为非安全镜像，以外部项目（External Project）方式集成 TF-M，并可选集成安全引导加载程序（Secure Bootloader）：

- [`CONFIG_TRUSTED_EXECUTION_NONSECURE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRUSTED_EXECUTION_NONSECURE) 为 `y`。
- [`CONFIG_ARM_TRUSTZONE_M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM_TRUSTZONE_M) 为 `y`。

比较 [boards/arm/mps2/mps2_an521_cpu0.dts](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_an521_cpu0.dts) 与 [boards/arm/mps2/mps2_an521_cpu0_ns.dts](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_an521_cpu0_ns.dts)，可看到非安全版本定义 Flash 和 SRAM 中的偏移，为 TF-M 与安全引导加载程序留出所需空间。原文给出的设备树片段如下。

```dts
reserved-memory {
            #address-cells = <1>;
            #size-cells = <1>;
            ranges;

            /* The memory regions defined below must match what the TF-M
             * project has defined for that board - a single image boot is
             * assumed. Please see the memory layout in:
             * https://git.trustedfirmware.org/TF-M/trusted-firmware-m.git/tree/platform/ext/target/mps2/an521/partition/flash_layout.h
             */

            code: memory@100000 {
                    reg = <0x00100000 DT_SIZE_K(512)>;
            };

            ram: memory@28100000 {
                    reg = <0x28100000 DT_SIZE_M(1)>;
            };
    };
```

原文说明：这为安全引导和 TF-M 预留 1 MB 代码存储空间以及 1 MB RAM，使非安全 Zephyr 应用代码从 `0x10000` 开始，RAM 从 `0x28100000` 开始；非安全 Zephyr 镜像可用 512 KB 代码空间及 1 MB RAM。

> 译注——原文地址纠错：上述原文的 `0x10000` 与同页设备树和下方布局不一致，后两者均为 **`0x00100000`**。译文保留原句以便对照，实际分析应核对所用版本的设备树、链接产物与 TF-M 分区定义。

这对应原文所引用的 TF-M `flash_layout.h` 布局：

```text
* 0x0000_0000 BL2 - MCUBoot (0.5 MB)
* 0x0008_0000 Secure image     primary slot (0.5 MB)
* 0x0010_0000 Non-secure image primary slot (0.5 MB)
* 0x0018_0000 Secure image     secondary slot (0.5 MB)
* 0x0020_0000 Non-secure image secondary slot (0.5 MB)
* 0x0028_0000 Scratch area (0.5 MB)
* 0x0030_0000 Protected Storage Area (20 KB)
* 0x0030_5000 Internal Trusted Storage Area (16 KB)
* 0x0030_9000 NV counters area (4 KB)
* 0x0030_A000 Unused (984 KB)
```

布局中的术语依次为：BL2／MCUboot 引导程序；安全镜像主槽（Primary Slot）；非安全镜像主槽；安全镜像次槽（Secondary Slot）；非安全镜像次槽；交换暂存区（Scratch Area）；受保护存储区（Protected Storage Area）；内部可信存储区（Internal Trusted Storage Area）；非易失计数器区（NV Counters Area）；未使用区域（Unused）。

原文通过 [`CONFIG_TFM_BOARD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TFM_BOARD) 指定将 `mps2/an521` 作为板级目标传入 TF-M。

译注——当前官方源码差异：本次核对的 `Kconfig.tfm` 为此目标映射的是 `arm/mps2/an521`。当前 `mps2_an521_cpu0_ns.dts` 通过 `zephyr,code-partition` 选择 `slot0_ns_partition`，起点仍为 `0x00100000`、长度 512 KiB；RAM 从 `0x28100000` 开始，但大小为 **512 KiB**，与原页的 1 MiB 不同。原页片段与布局保留为文档版本记录，不能作为当前所有版本的固定配置。

同一设备树说明 AN521 没有实际 Flash／Flash 控制器，代码也位于 RAM；其 `fake_flash0` 分区是为构建布局保留的描述。因此，跟踪这些节点可以帮助理解镜像位置，但不能将它们直接当作其他开发板的硬件定义。


译注核对来源：[boards/arm/mps2/mps2_an521_cpu0_ns.dts](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_an521_cpu0_ns.dts)、[boards/arm/mps2/mps2_an521_cpu0.dts](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_an521_cpu0.dts)、[boards/arm/mps2/mps2_an521_cpu0_ns_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/mps2/mps2_an521_cpu0_ns_defconfig)、[modules/trusted-firmware-m/Kconfig.tfm](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm)。

本仓库的[对应源码](../../../boards/arm/mps2/mps2_an521_cpu0_ns.dts)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、烧录、密钥生成或存储操作。

<a id="trusted-firmware-m-integration"></a>
<a id="board-definitions"></a>
<a id="example-mps2-an521-cpu0-ns"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：TFM构建系统](P004_TFM构建系统.md) · [本模块主线目录](../reading/tfm.md) · [全部主线](../reading/README.md) · [下一篇：TFM测试套件](P006_TFM测试套件.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P004_TFM构建系统.md) · [返回大纲](大纲.md) · [下一章](P006_TFM测试套件.md)

</details>

<!-- reading-navigation:end -->
