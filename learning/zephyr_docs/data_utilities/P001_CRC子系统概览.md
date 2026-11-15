---
id: learning.zephyr-docs.data-utilities.page-1
title: CRC子系统概览
kind: reference
status: maintained
domains: [zephyr, data, development]
source_url: https://docs.zephyrproject.org/latest/services/crc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_CRC子系统概览

原文：[官方页面](https://docs.zephyrproject.org/latest/services/crc/index.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 1.1\_概述（Overview）

CRC 子系统提供多种循环冗余校验（Cyclic Redundancy Check，CRC）算法的软件实现，用于验证数据完整性（Data Integrity）。CRC 常用于检测存储和通信系统中的数据意外变化。

子系统提供 CRC-4、CRC-7、CRC-8、CRC-16、CRC-24 和 CRC-32 等变体，并在可用时提供可选的硬件加速（Hardware Acceleration）。

**原文注意（Note）**：本库与 [CRC硬件驱动API](../hardware/P033_CRC循环冗余校验.md)不同，后者为硬件 CRC 加速外设提供接口。当硬件 CRC 单元可用，且设备树（Devicetree）的 `/chosen` 节点设置了 `zephyr,crc` 属性时，库函数默认使用硬件加速以提高性能；可将 [`CONFIG_CRC_HW_HANDLER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC_HW_HANDLER) 设为 `n` 禁用。

### 用法（Usage）

计算 CRC 时，包含相应头文件并调用所需函数：

```c
#include <zephyr/sys/crc.h>

uint8_t data[] = {0x01, 0x02, 0x03, 0x04};
uint32_t checksum = crc32_ieee(data, sizeof(data));
```

对分块处理的流式数据（Streaming Data），使用 update 变体：

```c
uint32_t crc = 0;
crc = crc32_ieee_update(crc, chunk1, len1);
crc = crc32_ieee_update(crc, chunk2, len2);
/* Final CRC value is in 'crc' */
```

注释意为：“最终 CRC 值保存在 crc 中”。

通用函数 [`crc_by_type()`](P003_CRC计算接口.md#ga5d7f493210e56fb18b8199c9d8a17f33) 提供统一接口，在运行时选择 CRC 算法。

## 1.2\_配置（Configuration）

原页列出的相关配置选项如下：

- [`CONFIG_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC)：启用 CRC 支持。
- [`CONFIG_CRC_HW_HANDLER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC_HW_HANDLER)：启用硬件 CRC 加速。
- [`CONFIG_CRC_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC_SHELL)：启用 CRC Shell 命令。
- [`CONFIG_CRC[0-9].*`](https://docs.zephyrproject.org/latest/kconfig.html#!CONFIG_CRC[0-9].*)：原文说明为“启用特定 CRC 算法的软件实现”。

> 译注：最后一项是用于搜索一组选项的正则表达式（Regular Expression），不是可直接写入 prj.conf 的单个配置名。而且其原文描述与本次读取的官方实现不一致：软件实现以弱符号（Weak Symbol）提供；当 CRC_HW_HANDLER 启用时，crc_hardware.c 中对应 CONFIG_CRC 算法选项控制硬件覆盖函数是否编入。例如 CONFIG_CRC32_IEEE 为 y 会编入对应硬件实现，并非强制软件。若要整体禁用这一硬件处理层，可按上文将 CONFIG_CRC_HW_HANDLER 设为 n。具体算法仍须核对驱动能力及当前版本。

译注的源码依据为[官方Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/crc/Kconfig)、[构建规则](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/crc/CMakeLists.txt)、[硬件处理实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/crc/crc_hardware.c)和[CRC32软件实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/crc/crc32_sw.c)。本仓库的[对应目录](../../../subsys/crc)可作相对路径跟踪，版本不自动等同于官网；读取摘要见[来源记录](../SOURCES.md)。

## 1.3\_API参考与相关示例

- [CRC计算接口](P003_CRC计算接口.md)。
- [CRC子系统示例](P002_CRC子系统示例.md#crc_subsys)：使用 CRC 子系统 API 计算并验证 CRC。


<a id="crc"></a>
<a id="id1"></a>
<a id="overview"></a>
<a id="usage"></a>
<a id="configuration"></a>
<a id="api-reference"></a>

<!-- reading-navigation:start -->

**主线阅读**

[本模块主线目录](../reading/data_utilities.md) · [全部主线](../reading/README.md) · [下一篇：随机数生成](P006_随机数生成.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[返回大纲](大纲.md) · [下一章](P002_CRC子系统示例.md)

</details>

<!-- reading-navigation:end -->
