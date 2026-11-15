---
id: learning.zephyr-docs.data-utilities.page-2
title: CRC子系统示例
kind: reference
status: maintained
domains: [zephyr, data, development]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/crc/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_CRC子系统示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/crc/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 2.1\_概述（Overview）

本示例演示如何使用循环冗余校验子系统（Cyclic Redundancy Check Subsystem，CRC Subsys）。[查看官方源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/subsys/crc)。

## 2.2\_配置选项（Configuration Options）

本示例使用以下 Kconfig 选项：

- [`CONFIG_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC)：启用 CRC 功能。
- [`CONFIG_CRC[0-9].*`](https://docs.zephyrproject.org/latest/kconfig.html#!CONFIG_CRC[0-9].*)：原文写为“如果设备树 `/chosen` 节点已设置 `zephyr,crc` 属性，则强制使用软件 CRC；否则使用硬件加速”。

可在项目 `prj.conf` 文件中修改这些选项，或通过 CMake 参数传入。

> 译注：第二条原文的条件说明有误，不能据此配置。没有有效的硬件选择节点并不能触发硬件加速；具体算法选项在当前硬件处理实现中用于编入相应硬件覆盖函数。软件弱符号和硬件覆盖的关系、禁用硬件处理的开关及源码依据见[CRC配置说明](P001_CRC子系统概览.md)。此处完整保留原文描述并明确纠错，不能把搜索表达式 CONFIG_CRC[0-9].* 当作实际配置赋值。

## 2.3\_构建与运行（Building and Running）

### 为Renesas RA8M1构建与运行

可按以下方式为 [RA8M1评估套件](https://docs.zephyrproject.org/latest/boards/renesas/ek_ra8m1/doc/index.html#ek_ra8m1)构建并执行示例：

```bash
west build -b ek_ra8m1 samples/subsys/crc
west flash
```

要为其他开发板构建，将上面的 `ek_ra8m1` 替换为对应开发板名称。

> 译注：命令以已准备 Zephyr 工作区、目标工具链、west、目标板及其烧录工具为前提，在实际 Zephyr 源码根执行；构建失败时不要继续烧录。原目标是 RA8M1，本文没有把它改写成 HC32 实验，也未执行这些命令。

## 2.4\_示例输出（Sample Output）

```text
subsys_crc_example: Result of CRC32 IEEE: 0xCEA4A6C2
subsys_crc_example: Result of CRC8 CCITT: 0x96
subsys_crc_example: CRC computation completed successfully
```

三行输出分别表示：CRC32 IEEE 结果为 `0xCEA4A6C2`，CRC8 CCITT 结果为 `0x96`，CRC 计算成功完成。

**原文注意（Note）**：如果开发板不支持硬件 CRC 驱动，计算会退回软件实现。

> 译注：这里描述可用实现的选择，不能理解成硬件运行报错后必然动态回退。本次读取的硬件处理函数会检查设备和驱动调用返回值；部分封装在失败后记录日志并返回 0。应核对所用算法的实现与错误信息，不能仅凭数值 0 判断硬件执行成功。

## 2.5\_预期行为（Expected Behavior）

示例运行时应当：

1. 计算预定义数据的 CRC32 和 CRC8 值。
2. 打印计算结果。

## 2.6\_另见（See Also）

[CRC计算接口](P003_CRC计算接口.md)。本仓库[示例目录](../../../samples/subsys/crc)可用于源码对照；上述输出为原文预期结果，不是本轮执行记录。


<a id="crc_subsys"></a>
<a id="overview"></a>
<a id="configuration-options"></a>
<a id="building-and-running"></a>
<a id="building-and-running-for-renesas-ra8m1"></a>
<a id="sample-output"></a>
<a id="expected-behavior"></a>
<a id="see-also"></a>

[上一章](P001_CRC子系统概览.md) · [返回大纲](大纲.md) · [下一章](P003_CRC计算接口.md)
